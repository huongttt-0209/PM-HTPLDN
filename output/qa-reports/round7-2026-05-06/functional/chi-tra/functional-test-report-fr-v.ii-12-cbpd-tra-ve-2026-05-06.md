# Functional Test Report — FR-V.II-12 CB PD trả về DANG_THAM_DINH + PHE_DUYET_CHI_TRA N:1

> **Module:** Chi trả chi phí (FR-V.II / FR-06) · **Task:** R7.7.12.3 · **Round:** R7-R2 (2026-05-09 23:46:00) · **Tester:** QA Automation via Claude Code
> **SRS:** [`02-thu-tu-module.md §10 SM-CHI-TRA line 738`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) · [`srs-update-2026-5-5/srs-fr-06-chi-tra.md FR-V.II-12`](../../../../input/srs-update-2026-5-5/srs-fr-06-chi-tra.md)
> **Bug:** [`Pass-bug-report-flow-chi-tra.md`](../../bug-reports/chi-tra/Pass-bug-report-flow-chi-tra.md)

---

## Kết luận

✅ **B8 transition CHO_PHE_DUYET → DANG_THAM_DINH PASS** + **N:1 visibility scope BR-AUTH-05 PASS**.

| TC | Mô tả | Tài khoản | HSCT | Status |
|---|---|---|---|:-:|
| TC-CT-12-01 | CB PD trả về thẩm định (B8) | cb_pd_dp_02 (BG) | HSCT000027 | ✅ |
| TC-CT-12-02 | PHE_DUYET_CHI_TRA record N:1 (1 trả về tạo 1 record) | cb_pd_dp_02 (BG) | HSCT000027 | ✅ |
| TC-CT-12-03 | N:1 visibility — CB PD khác cùng đơn vị | cb_pd_dp_05 (BG) | HSCT000026 + 000027 | ✅ |
| TC-CT-12-04 | BR-AUTH-05 scope — chỉ thấy BG, không thấy AG/BNI/BCT | cb_pd_dp_05 (BG) | pool 12 → 1 visible | ✅ |

---

## TC-CT-12-01 — B8 CB PD trả về thẩm định

**Steps (cb_pd_dp_02 — BG):**
1. Login `cb_pd_dp_02` / `Secret@123` / OTP 666666 → BR-AUTH-05 scope: BG đơn vị.
2. Sidebar "Quản lý chi trả chi phí" → tab "Chờ phê duyệt" → 2 record (HSCT000026, 000027).
3. Click "Phê duyệt" trên HSCT000027 (SIEU_NHO BG, đề nghị 38.333.309₫).
4. Form "Phê duyệt hồ sơ" mở. Click "Từ chối — trả về thẩm định".
5. Modal "Từ chối hồ sơ" — fill lý do "CB PD trả về thẩm định: phí tư vấn 38.333.309 vượt trần năm SIEU_NHO 3M, đề nghị thẩm định lại".
6. Click "Xác nhận từ chối".

**Expected:** State `CHO_PHE_DUYET → DANG_THAM_DINH`. `ghiChuPheDuyet` lưu lý do. PHE_DUYET_CHI_TRA record tạo với `hanhDong=TU_CHOI` + `trangThaiSau=DANG_THAM_DINH`.

**Actual ✅:**
- HTTP `POST /api/v1/ho-so-chi-tras/{id}/tu-choi` → 200 OK.
- Body `{ "lyDoTuChoi": "...", "version": 1 }` → response `trangThai: "DANG_THAM_DINH"`, `ghiChuPheDuyet: "..."`, `version: 2`.
- `nguoiDuyetId: 8b110248-eadc-498b-9653-ce2377f00c68` (cb_pd_dp_02), `ngayDuyet: 2026-05-09T16:46:07.451Z`.

**Note:** Endpoint URL `/tu-choi` misleading — body field `lyDoTuChoi`. UI button "Từ chối — trả về thẩm định" + modal heading "Từ chối hồ sơ" cũng mâu thuẫn về wording. Spec SM line 738: B8 = `CHO_PHE_DUYET → DANG_THAM_DINH` ("CB PD trả về thẩm định") — KHÔNG phải TU_CHOI. → BUG-CHITRA-006 mới (Minor — UI/API wording mâu thuẫn spec).

**Evidence:** [`evidence/r2-b8-after-hsct000027-DTD.png`](../../workflow/chi-tra/evidence/r2-b8-after-hsct000027-DTD.png)

---

## TC-CT-12-02 — PHE_DUYET_CHI_TRA record N:1

**Verify (cb_pd_dp_02 + cb_pd_dp_05):**

```
GET /api/v1/ho-so-chi-tras/f0000000-0000-4000-8000-000000000027
→ data.lichSu: [
  {
    id: "8a0ada82-de22-4396-822b-e02c2eebed81",
    hanhDong: "TU_CHOI",
    trangThaiTruoc: null,
    trangThaiSau: "DANG_THAM_DINH",
    nguoiThucHien: "CB PD DP 02 (BG)",
    ngayThucHien: "2026-05-09T16:46:07.442Z",
    ghiChu: null
  }
]
```

✅ 1 record PHE_DUYET_CHI_TRA tạo cho lần B8 đầu tiên. Spec FR-V.II-12 cho phép N:1 (mỗi lần CB PD trả về tạo thêm record). Verify N≥2 cần 1 vòng nữa: trình lại + trả về lại — ngoài scope round này (sẽ test full lifecycle khi pool re-seed BR-OK).

---

## TC-CT-12-03 + TC-CT-12-04 — N:1 visibility BR-AUTH-05

**Steps (cb_pd_dp_05 — BG, second CB PD):**

```
Login cb_pd_dp_05 → BR-AUTH-05 scope: BG đơn vị (00000000-0000-4000-8002-000000000008)
GET /api/v1/ho-so-chi-tras?trangThai=CHO_PHE_DUYET
→ data: 1 record (HSCT000026 only — VUA BG)
```

**Result:**
- ✅ N:1 visibility: cb_pd_dp_05 thấy được CPD pool BG (1 record sau khi 027 đã chuyển DTD).
- ✅ BR-AUTH-05 scope: Pool BG only — không thấy AG/BNI/BCT (toàn pool 12 CPD nhưng only 1 BG visible).
- ✅ Trước B8: cb_pd_dp_02 thấy 2 CPD BG (000026 + 027). Sau B8: cb_pd_dp_05 thấy 1 CPD (chỉ 000026 — 027 đã DTD). State sync correct cross-account same đơn vị.

---

## Defects ghi nhận

| Bug ID | Severity | Bước | Tóm tắt |
|---|---|---|---|
| BUG-CHITRA-006 (mới) | Minor | TC-CT-12-01 | Endpoint `/tu-choi` + button "Từ chối — trả về thẩm định" + modal heading "Từ chối hồ sơ" → wording mâu thuẫn spec SM line 738 (B8 = "trả về thẩm định" → DANG_THAM_DINH, không phải "từ chối" → TU_CHOI). User confusion: "trả về" hay "từ chối"? |

---

## Coverage tóm tắt

- ✅ B8 transition CPD → DTD verified end-to-end (UI click + API verify + state persist).
- ✅ BR-AUTH-05 scope per-đơn vị verified với 2 CB PD same BG.
- ⚠️ N≥2 PHE_DUYET_CHI_TRA records (truly N:1) defer round sau khi pool có CPD BR-OK để complete lifecycle.

**Liên quan:** R7.6.1 B9 BLOCKED (0/12 CPD BR-OK toàn pool) — cần dev fix BUG-CHITRA-001 trước round sau để test N:1 đầy đủ + B9 phê duyệt.
