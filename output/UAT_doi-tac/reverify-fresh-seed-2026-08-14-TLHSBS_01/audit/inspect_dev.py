#!/usr/bin/env python3
"""Read-only API inspector for TLHSBS_01 on DEV.

Secrets and OTPs are intentionally never printed or persisted.
"""

import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone


BASE = "https://18.143.165.120.nip.io"
MAILHOG = "http://18.143.165.120:8025"
PASSWORD = "Test@1234"
ALIASES = {
    "cbnv_tw_02": "diupt01+cb-nv-a-2@gmail.com",
    "cbpd_tw_02": "diupt01+cb-pd-a-2@gmail.com",
    "qa_tvvseed28": "diupt01+cg@gmail.com",
    "0100000001": "seed.publishable@test.htpldn.vn",
    "0109998887": "diupt01+dn-login@gmail.com",
}


def curl(method, url, token=None, data=None):
    cmd = ["curl", "-ksS", "-X", method, url, "--max-time", "90"]
    if token:
        cmd += ["-H", f"Authorization: Bearer {token}"]
    if data is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(data, ensure_ascii=False)]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    try:
        return proc.returncode, json.loads(proc.stdout)
    except json.JSONDecodeError:
        return proc.returncode, {"_raw": proc.stdout[:1000], "_stderr": proc.stderr[:500]}


def login(username):
    started = datetime.now(timezone.utc)
    _, first = curl("POST", f"{BASE}/api/v1/auth/login", data={"username": username, "password": PASSWORD})
    if not first.get("success"):
        raise RuntimeError(f"Login failed for {username}: {first.get('error') or first.get('message')}")
    otp_token = first["data"]["otpToken"]
    recipient = ALIASES[username].lower()
    otp = None
    for _ in range(15):
        time.sleep(1)
        raw = subprocess.run(
            ["curl", "-sS", f"{MAILHOG}/api/v2/messages?limit=50", "--max-time", "30"],
            capture_output=True,
            text=True,
            check=False,
        ).stdout
        messages = json.loads(raw).get("items", [])
        for message in messages:
            created_text = message["Created"]
            created = datetime.fromisoformat(re.sub(r"(\.\d{6})\d+Z$", r"\1+00:00", created_text))
            tos = {f"{item['Mailbox']}@{item['Domain']}".lower() for item in message.get("To", [])}
            if recipient not in tos or created < started:
                continue
            found = re.search(r"\b(\d{6})\b", message.get("Content", {}).get("Body", ""))
            if found:
                otp = found.group(1)
                break
        if otp:
            break
    if not otp:
        raise RuntimeError(f"No fresh MailHog OTP found for {username}")
    _, verified = curl(
        "POST",
        f"{BASE}/api/v1/auth/verify-otp",
        data={"otpToken": otp_token, "otpCode": otp},
    )
    if not verified.get("success"):
        raise RuntimeError(f"OTP verification failed for {username}")
    return verified["data"]["accessToken"]


def unwrap(payload):
    return payload.get("data", payload)


def main():
    token = login("cbnv_tw_02")
    paths = {
        "dashboard": "/api/v1/dashboard?nam=2026",
        "existing_detail": "/api/v1/vu-viecs/cf90a65c-5fe0-4687-bbed-50538b0341c0",
        "existing_check": "/api/v1/vu-viecs/cf90a65c-5fe0-4687-bbed-50538b0341c0/ket-qua-kiem-tra",
        "existing_files": "/api/v1/vu-viecs/cf90a65c-5fe0-4687-bbed-50538b0341c0/ho-so",
        "suggested_assignees": "/api/v1/vu-viecs/goi-y-tvv?linhVucId=bbbbbbbb-0000-4000-8000-00000000001c",
    }
    result = {}
    for name, path in paths.items():
        _, payload = curl("GET", BASE + path, token=token)
        result[name] = unwrap(payload)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
