# Bảng đối chiếu điều kiện — QLNDTVVCG_11 (nút Sửa theo trạng thái TVCS)

- **Mã TC:** QLNDTVVCG_11 (row 282) · **Verdict:** Reject (lỗi đối tác báo KHÔNG tái hiện trên build hiện tại).
- **Màn:** SCR-X1-02 (list + chi tiết) · **SRS:** `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1152` — "Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)".
- **Loại bug:** phụ thuộc **state** (state machine SM-TVCS) → bắt buộc bảng đối chiếu.
- **Tài khoản verdict:** `cbnv_tw_02` / CB_NV_TW, đơn vị BTP·TW (cùng vai trò + đơn vị đối tác trong evidence).

## Điều kiện đối tác (từ evidence full-res QLNDTVVCG_11.jpg — list danh-sach, ospgroup.vn)

Đối tác phản ánh 2 ý:
1. Các record **Tiếp nhận (TIEP_NHAN)** không nhất quán: vài record có nút Sửa (pencil), vài record chỉ có Xem + Phân công.
2. Record **Đang tư vấn (DANG_TU_VAN)** (dòng "TVCS cho VV-HDSD-004", highlight vàng): Hành động chỉ có **Xem (eye)**, KHÔNG có nút Sửa.

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res) | Mình test (nip.io, cbnv_tw_02) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW) | CB_NV_TW `cbnv_tw_02`, cùng đơn vị BTP·TW | Không |
| Entity + **trạng thái** TIEP_NHAN | vài record Tiếp nhận không có Sửa | 3 record TIEP_NHAN (TVCS-...-0001/0002 seed + 0003) — **tất cả đều có nút Sửa** (eye+team+edit+delete) | Không |
| Entity + **trạng thái** PHAN_CONG | (đối tác không nêu riêng) | 1 record PHAN_CONG (TVCS-...-0003) — có nút Sửa (eye+edit) | Không |
| Entity + **trạng thái** DANG_TU_VAN | record Đang tư vấn KHÔNG có Sửa | 1 record DANG_TU_VAN (TVCS-...-0002, seed qua phân công→CG chấp nhận) — **CÓ nút Sửa** (list eye+edit; chi tiết nút "Sửa"; click Sửa mở form editable có [Lưu]) | Không |
| Entity + **trạng thái** DA_DUYET | (đối chứng) | 1 record DA_DUYET (TVCS-SEED-0001) — **KHÔNG có Sửa** (chỉ eye) — đúng SRS | Không |

**0 GAP** — đã seed đủ các state tiền đề (TIEP_NHAN, PHAN_CONG, DANG_TU_VAN, DA_DUYET) trong cùng scope đơn vị + verify bằng đúng vai trò CB NV của đối tác.

## Seed để đóng GAP DANG_TU_VAN (§Nguyên tắc 4)

1. `cbnv_tw_02` tạo TVCS Record B (POST) → TIEP_NHAN.
2. `cbnv_tw_02` phân công CG "QA TVV Seed28 Active" (loaiTvv=CG, HOAT_DONG, cùng đơn vị) → PHAN_CONG.
3. Login `qa_tvvseed28` (đúng CG được phân công) → xác nhận CHAP_NHAN → **DANG_TU_VAN**.
4. Login lại `cbnv_tw_02` → quan sát nút Sửa của record DANG_TU_VAN.

## Kết luận

- Trên build hiện tại (nip.io): record **DANG_TU_VAN CÓ nút Sửa và sửa được** (mở form editable, có [Lưu]) → **đúng SRS dòng 1152**, trái với phản ánh đối tác.
- Các record **TIEP_NHAN đều nhất quán có nút Sửa** → không tái hiện tình trạng "vài record không có Sửa".
- Record **DA_DUYET không có Sửa** → đúng SRS.
- → Lỗi đối tác báo (DANG_TU_VAN thiếu Sửa + TIEP_NHAN không nhất quán) **KHÔNG tái hiện** → **Reject**, đề nghị đối tác kiểm tra lại trên build hiện tại.

## Quan sát ngoài phạm vi (báo BA/QA cân nhắc)

- Record **PHAN_CONG** cũng hiện nút Sửa. SRS dòng 1152 chỉ cho phép mode sửa ở TIEP_NHAN + DANG_TU_VAN (không nêu PHAN_CONG). Đây là sai lệch theo hướng **rộng hơn** SRS (cho sửa ở state SRS không liệt kê) — ngược chiều với phản ánh đối tác. Ghi nhận để BA/QA review (không thuộc claim case 11).

## Evidence

- `reverify-audit/QLNDTVVCG_11/list-4-states-sua-button.png` — list 4 record với action theo state.
- `reverify-audit/QLNDTVVCG_11/detail-dangtuvan-has-sua-button.png` — chi tiết record DANG_TU_VAN có nút "Sửa".
- Partner: `partner-evidence/QLNDTVVCG_11.jpg`.
