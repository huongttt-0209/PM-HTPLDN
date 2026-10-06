# Bảng đối chiếu điều kiện — QLTKND_15 (row 168)

**Case:** Thêm tài khoản với **tên đăng nhập trùng** → thông báo lỗi bị lặp (2 toast).
**Verdict:** `Open` (1 request → 2 toast — vùng nóng duplicate, đo bằng tools/toast-capture.js).

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLTKND_15.jpg) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT") | admin / QTHT | Không |
| Entity + trạng thái | Form "Thêm tài khoản mới", có TK đã tồn tại `aibox` để nhập trùng | Form "Thêm tài khoản mới", có TK đã tồn tại `cbnv_tw` để nhập trùng | Không |
| Input / filter / giá trị nhập | Tên đăng nhập = `aibox` (trùng), email hợp lệ mới | Tên đăng nhập = `cbnv_tw` (trùng), email mới `qa.dup.uname.0721@htpldn.test` | Không |

**0 GAP.** Cùng thao tác (thêm TK trùng username), cùng vai trò QTHT, cùng điều kiện (username đã tồn tại). Khác username cụ thể (`aibox` vs `cbnv_tw`) không đổi bản chất — cả 2 đều là username đã tồn tại → cùng nhánh validation trùng.

## Kết quả test (real-data, artifact — mandated tool)
- Đo bằng `tools/toast-capture.js` (observer=1 self-check hợp lệ, KHÔNG lọc trùng, đọc innerText, đếm request song song toast).
- **1 request** `POST /api/v1/tai-khoan` → **2 khung thông báo**: "Username đã tồn tại trong hệ thống" + "Tên đăng nhập 'cbnv_tw' đã tồn tại".
- 2 chữ KHÁC nhau (loại trừ artifact observer nhân bản) · toast z-index 2010 > modal 1000 (nổi trên modal, hiển thị thật) · tái hiện ≥5/5 lần.
- Log đầy đủ: `reverify-audit/QLTKND_15/toast-capture-measurement.md`. Evidence đối tác: `partner-evidence/QLTKND_15.jpg` (hiện đúng 2 toast).

## Đối chiếu SRS
- FR-VIII-15 §Error Handling E1 (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:727`): username trùng → `ERR-TK-01` = 1 thông báo "Username '{username}' đã tồn tại".
- → App phát **2** thông báo cho 1 lần vi phạm = lỗi hiển thị FE (lặp thông báo).

## Kết luận
`Open` — 1 lần submit trùng username sinh 2 thông báo lỗi (đặc tả chỉ 1). Cross-ref cụm duplicate B5 (LVPL_19/LHHT_16/LDN_16) + B8 (QLTKND_17). Không tạo bản ghi trùng (chỉ 1 POST, BE từ chối) → mức Medium (lỗi hiển thị, dữ liệu an toàn).
