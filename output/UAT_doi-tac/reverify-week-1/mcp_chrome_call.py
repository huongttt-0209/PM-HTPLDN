#!/usr/bin/env python3
import json
import os
import select
import subprocess
import sys
import time


def read_message(proc, timeout=20):
    end = time.time() + timeout
    fd = proc.stdout.fileno()
    while time.time() < end:
        ready, _, _ = select.select([fd], [], [], 0.2)
        if ready:
            line = proc.stdout.readline()
            if line:
                return json.loads(line)
    stderr = ""
    while True:
        ready, _, _ = select.select([proc.stderr.fileno()], [], [], 0)
        if not ready:
            break
        stderr += proc.stderr.readline()
    raise TimeoutError(f"No MCP response. stderr={stderr}")


def send(proc, payload):
    proc.stdin.write(json.dumps(payload) + "\n")
    proc.stdin.flush()


def main():
    if len(sys.argv) < 2:
        print("Usage: mcp_chrome_call.py <tool-name> [json-args]", file=sys.stderr)
        return 2

    tool = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    browser_url = os.environ.get("CHROME_DEVTOOLS_URL", "http://127.0.0.1:9222")
    cmd = [
        "npx",
        "chrome-devtools-mcp@latest",
        "--browserUrl",
        browser_url,
        "--no-usage-statistics",
        "--no-performance-crux",
    ]
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    try:
        send(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {},
                    "clientInfo": {"name": "codex-mcp-chrome", "version": "1.0"},
                },
            },
        )
        read_message(proc)
        send(proc, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        calls = args if tool == "sequence" else [{"name": tool, "arguments": args}]
        results = []
        for idx, call in enumerate(calls, start=2):
            send(
                proc,
                {
                    "jsonrpc": "2.0",
                    "id": idx,
                    "method": "tools/call",
                    "params": {
                        "name": call["name"],
                        "arguments": call.get("arguments", {}),
                    },
                },
            )
            results.append(read_message(proc, timeout=60))
        print(json.dumps(results if tool == "sequence" else results[0], ensure_ascii=False, indent=2))
    finally:
        proc.kill()


if __name__ == "__main__":
    raise SystemExit(main())
