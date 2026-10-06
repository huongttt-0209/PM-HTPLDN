# CTTLV_01 (row 270) — "Không xác định" — Reconciliation — 2026-07-21

**Verdict: Reject** (web đúng — nhãn "Không xác định" phản ánh đúng CT không gán lĩnh vực). Tài khoản `cbnv_tw_04`, kỳ Năm 2026, Toàn quốc.

## Báo cáo (UI + API `ct-theo-linh-vuc`)

| Lĩnh vực PL | Số CT | Số DN tham gia |
|---|:-:|:-:|
| Không xác định | 3 | 0 |
| Thương mại | 1 | 0 |
| **Tổng** | **4** | **0** |

## Kiểm chứng nguồn (`GET /api/v1/chuong-trinh-htpls`)

| Mã CT | Trạng thái | linhVucId (nguồn) | Nhãn báo cáo | Đúng? |
|---|---|---|---|:-:|
| CT-20260721-0004 (khong linh vuc test) | DA_DUYET | null | Không xác định | ✓ |
| CT-20260721-0003 (Seed QA-B) | HOAN_THANH | null | Không xác định | ✓ |
| CT-20260721-0002 (Seed QA-A) | DANG_THUC_HIEN | null | Không xác định | ✓ |
| CT-20260721-0001 (verify Thương mại) | DA_DUYET | Thương mại | Thương mại | ✓ |
| CTHTPL-SEED-0001 (seed 2026) | DA_CONG_BO | Thương mại | (không đếm) | ⚠ xem ghi chú |

## Kết luận

- Báo cáo **trung thực với nguồn**: 3 CT có `linhVucId=null` → "Không xác định"; CT có lĩnh vực (Thương mại) → map đúng "Thương mại", KHÔNG bị nhầm.
- KHÔNG có lỗi map. "Không xác định" là nhãn đúng cho CT không gán lĩnh vực (do QA seed tạo không lĩnh vực). → **Reject**.

## Ghi chú ngoài case (không log bug)

- `CTHTPL-SEED-0001` (Thương mại, DA_CONG_BO) không được đếm → Thương mại = 1 thay vì 2. Theo `input/input.md`: CT seed này `donVi RỖNG` + `ngayCongBo=null` → loại khỏi scope báo cáo. Seed artifact đã biết, không phải lỗi sản phẩm. Nêu ở phần "bất thường" cuối batch.

Evidence ảnh: `cttlv-report-khongxacdinh.png` (KPI Tổng CT 4; bảng Không xác định 3 / Thương mại 1).
