#!/usr/bin/env python3
"""Seed one fresh TLHSBS_01 case through the real VuViec workflow on DEV.

The script records only business-state evidence. Access tokens, passwords and OTPs
are never printed or written to disk.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from inspect_dev import BASE, curl as base_curl, login, unwrap


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "audit"
FIXTURE = ROOT.parent / "reverify-2026-08-14-dashboard-bug" / "image" / "TLHSBS_01-dashboard-live.png"
CHECKLIST_IDS = [f"00000000-0000-4000-8000-000000000c0{i}" for i in range(1, 7)]
TVV_ID = "98cfd963-3cd3-4c8a-bfa9-625460824d6d"  # qa_tvvseed28 profile in the same TW unit


def call(method, path, token, data=None, multipart_file=None):
    cmd = ["curl", "-ksS", "-X", method, BASE + path, "--max-time", "90", "-H", f"Authorization: Bearer {token}"]
    if multipart_file:
        cmd += ["-F", f"file=@{multipart_file}"]
    elif data is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(data, ensure_ascii=False)]
    cmd += ["-w", "\n%{http_code}"]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    body, _, status_text = proc.stdout.rpartition("\n")
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        payload = {"_raw": body[:1000], "_stderr": proc.stderr[:500]}
    return int(status_text or 0), payload


def data(payload):
    return payload.get("data", payload)


def detail(token, case_id):
    status, payload = call("GET", f"/api/v1/vu-viecs/{case_id}", token)
    if status != 200 or not payload.get("success"):
        raise RuntimeError(f"Cannot read case detail: HTTP {status} {payload.get('error')}")
    return data(payload)


def dashboard(token):
    status, payload = call("GET", "/api/v1/dashboard?nam=2026", token)
    if status != 200 or not payload.get("success"):
        raise RuntimeError(f"Cannot read dashboard: HTTP {status} {payload.get('error')}")
    kpis = {item["kpiCode"]: item for item in data(payload)["kpis"]}
    return {
        "completed": kpis["VU_VIEC_HOAN_THANH"]["giaTri"],
        "supplement_rate": kpis["TY_LE_HO_SO_BO_SUNG"]["giaTri"],
        "filter": kpis["TY_LE_HO_SO_BO_SUNG"]["appliedFilter"],
    }


def state_snapshot(token, case_id, step):
    item = detail(token, case_id)
    return {
        "step": step,
        "id": item["id"],
        "maVuViec": item["maVuViec"],
        "trangThai": item["trangThai"],
        "version": item["version"],
        "daYeuCauBoSung": item.get("daYeuCauBoSung"),
        "boSungCount": item.get("boSungCount"),
        "ngayYeuCauBoSung": item.get("ngayYeuCauBoSung"),
        "ngayHoanThanh": item.get("ngayHoanThanh"),
    }


def require_success(status, payload, label, expected=(200, 201)):
    if status not in expected or not payload.get("success"):
        raise RuntimeError(f"{label} failed: HTTP {status} {payload.get('error') or payload.get('message')}")
    return data(payload)


def main():
    cbnv = login("cbnv_tw_02")
    evidence = {"startedAt": datetime.now().astimezone().isoformat(), "baseline": dashboard(cbnv), "states": [], "operations": []}

    case_id = os.environ.get("TLHSBS_CASE_ID")
    if case_id:
        created = detail(cbnv, case_id)
        evidence["operations"].append({"step": "resume_existing_YEU_CAU_BO_SUNG", "http": 200})
        evidence["states"].append(state_snapshot(cbnv, case_id, "resumed_YEU_CAU_BO_SUNG"))
    else:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        create_body = {
            "kenhTiepNhan": "TRUC_TIEP",
            "tieuDe": f"QA TLHSBS_01 fresh YCBS {stamp}",
            "moTa": "Hồ sơ QA mới dùng riêng để kiểm chứng KPI sau khi thực sự đi qua trạng thái Yêu cầu bổ sung rồi hoàn thành trong kỳ.",
            "linhVucId": "bbbbbbbb-0000-4000-8000-00000000001c",
            "loaiHinhHtId": "4f09df19-224f-4a00-bcf7-479f8d77f476",
            "doanhNghiepId": "829abcac-b0af-4cde-9af9-ec51bc79014c",
        }
        status, payload = call("POST", "/api/v1/vu-viecs/manual", cbnv, create_body)
        created = require_success(status, payload, "create case")
        case_id = created["id"]
        evidence["operations"].append({"step": "create", "http": status})
        evidence["states"].append(state_snapshot(cbnv, case_id, "created"))

        current = detail(cbnv, case_id)
        ycb_body = {
            "checklist": [
                {"hangMucId": item_id, "dat": False if index == 0 else True, "ghiChu": "Thiếu tài liệu Mẫu 01 để kiểm chứng trạng thái bổ sung" if index == 0 else None}
                for index, item_id in enumerate(CHECKLIST_IDS)
            ],
            "ketLuan": "YEU_CAU_BO_SUNG",
            "lyDo": "QA TLHSBS_01: yêu cầu bổ sung Mẫu 01 để tạo lịch sử trạng thái thật.",
            "version": current["version"],
        }
        status, payload = call("POST", f"/api/v1/vu-viecs/{case_id}/kiem-tra", cbnv, ycb_body)
        require_success(status, payload, "mark YEU_CAU_BO_SUNG")
        evidence["operations"].append({"step": "mark_YEU_CAU_BO_SUNG", "http": status})
        evidence["states"].append(state_snapshot(cbnv, case_id, "after_YEU_CAU_BO_SUNG"))

    current = detail(cbnv, case_id)
    if current["trangThai"] == "YEU_CAU_BO_SUNG":
        status, payload = call("POST", "/api/v1/vu-viecs/upload", cbnv, multipart_file=FIXTURE)
        uploaded = require_success(status, payload, "upload supplement")
        file_id = uploaded["id"]
        evidence["operations"].append({"step": "upload_supplement", "http": status})

        status, payload = call(
            "POST",
            f"/api/v1/vu-viecs/{case_id}/bo-sung",
            cbnv,
            {"taiLieuDinhKem": [{"fileId": file_id, "loaiTaiLieu": "MAU_01"}], "ghiChu": "QA bổ sung tài liệu mới sau yêu cầu bổ sung."},
        )
        require_success(status, payload, "attach supplement")
        evidence["operations"].append({"step": "supplement_endpoint", "http": status})
        evidence["states"].append(state_snapshot(cbnv, case_id, "after_supplement_endpoint"))

        current = detail(cbnv, case_id)
        dat_body = {
            "checklist": [{"hangMucId": item_id, "dat": True} for item_id in CHECKLIST_IDS],
            "ketLuan": "DAT",
            "version": current["version"],
        }
        status, payload = call("POST", f"/api/v1/vu-viecs/{case_id}/kiem-tra", cbnv, dat_body)
        require_success(status, payload, "re-check DAT")
        evidence["operations"].append({"step": "recheck_DAT", "http": status})
        evidence["states"].append(state_snapshot(cbnv, case_id, "after_recheck_DAT"))
    elif current["trangThai"] == "DANG_KIEM_TRA":
        evidence["operations"].append({"step": "resume_after_recheck_DAT", "http": 200})
    else:
        raise RuntimeError(f"Unexpected state before assignment: {current['trangThai']}")

    status, payload = call(
        "POST",
        f"/api/v1/vu-viecs/{case_id}/phan-cong",
        cbnv,
        {"tvvId": TVV_ID, "ghiChu": "Phân công QA để hoàn tất hồ sơ kiểm chứng TLHSBS_01."},
    )
    require_success(status, payload, "assign qa_tvvseed28")
    evidence["operations"].append({"step": "assign", "http": status})
    evidence["states"].append(state_snapshot(cbnv, case_id, "after_assign"))

    tvv = login("qa_tvvseed28")
    status, payload = call("POST", f"/api/v1/vu-viecs/{case_id}/nhan-phan-cong", tvv, {})
    require_success(status, payload, "accept assignment")
    evidence["operations"].append({"step": "accept_assignment", "http": status})
    evidence["states"].append(state_snapshot(tvv, case_id, "after_accept_assignment"))

    current = detail(tvv, case_id)
    status, payload = call(
        "POST",
        f"/api/v1/vu-viecs/{case_id}/cap-nhat-ket-qua",
        tvv,
        {
            "noiDungKetQua": "QA TLHSBS_01: đã xử lý hồ sơ bổ sung mới và hoàn tất nội dung hỗ trợ.",
            "ketLuan": "Hồ sơ đáp ứng yêu cầu sau bổ sung.",
            "ghiChu": "Dữ liệu chỉ phục vụ kiểm chứng KPI.",
            "version": current["version"],
        },
    )
    require_success(status, payload, "update result")
    evidence["operations"].append({"step": "update_result", "http": status})

    status, payload = call(
        "POST",
        f"/api/v1/vu-viecs/{case_id}/trinh-phe-duyet",
        tvv,
        {"ghiChuTrinh": "Trình duyệt hồ sơ QA TLHSBS_01 sau bổ sung."},
    )
    require_success(status, payload, "submit approval")
    evidence["operations"].append({"step": "submit_approval", "http": status})
    evidence["states"].append(state_snapshot(tvv, case_id, "after_submit_approval"))

    cbpd = login("cbpd_tw_02")
    status, payload = call(
        "POST",
        f"/api/v1/vu-viecs/{case_id}/phe-duyet",
        cbpd,
        {"quyetDinh": "PHE_DUYET"},
    )
    require_success(status, payload, "approve")
    evidence["operations"].append({"step": "approve", "http": status})
    evidence["states"].append(state_snapshot(cbpd, case_id, "after_approve"))

    current = detail(cbnv, case_id)
    status, payload = call(
        "POST",
        f"/api/v1/vu-viecs/{case_id}/hoan-thanh",
        cbnv,
        {
            "ketLuanCuoi": "QA TLHSBS_01: hoàn thành hồ sơ mới đã thực sự qua trạng thái Yêu cầu bổ sung.",
            "ketQuaXuLy": "THANH_CONG",
            "version": current["version"],
        },
    )
    require_success(status, payload, "complete case")
    evidence["operations"].append({"step": "complete", "http": status})
    evidence["states"].append(state_snapshot(cbnv, case_id, "after_complete"))

    status, payload = call("GET", f"/api/v1/vu-viecs/{case_id}/lich-su?page=1&pageSize=100", cbnv)
    require_success(status, payload, "read history")
    history_payload = data(payload)
    history_items = history_payload.get("data", history_payload) if isinstance(history_payload, dict) else history_payload
    evidence["history"] = [
        {
            "hanhDong": item.get("hanhDong"),
            "trangThaiCu": (item.get("duLieuCu") or {}).get("trangThai"),
            "trangThaiMoi": (item.get("duLieuMoi") or {}).get("trangThai"),
            "thoiGian": item.get("thoiGian") or item.get("ngayTao"),
        }
        for item in (history_items or [])
    ]
    evidence["after"] = dashboard(cbnv)
    evidence["finishedAt"] = datetime.now().astimezone().isoformat()
    output = AUDIT / "fresh-seed-result.json"
    output.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"caseId": case_id, "maVuViec": created["maVuViec"], "baseline": evidence["baseline"], "after": evidence["after"], "output": str(output)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"SEED_FAILED: {exc}", file=sys.stderr)
        raise
