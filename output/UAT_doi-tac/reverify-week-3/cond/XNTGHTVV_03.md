# Bảng đối chiếu điều kiện — XNTGHTVV_03

Loại bug: **phụ thuộc role + state + data** (workflow) → BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `huongcg` — vai trò **TVV · CG**, đơn vị **BTP · TW** (đọc từ header + dòng "Vai trò hiện tại: TVV CG" trên màn 403, frame t012.09s/t018.45s) | `qa_tvvseed28` — vai trò **TVV · CG** (đã gán thêm vai trò CG "Chuyên gia tư vấn" qua Quản trị hệ thống → Tài khoản & phân quyền → Quản lý vai trò), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp = **BTP · TW**, cấp TW; `auth/me` trả `vaiTro:["TVV","CG"]` | Không |
| Entity + trạng thái (state machine) | Vụ việc ở **Đã phân công** (DA_PHAN_CONG) — detail render đủ 2 nút [Chấp nhận] [Từ chối] + badge "Còn 7 ngày LV", stepper bước 5 | Vụ việc **VV-BTP-TW-20260712-005** ở **Đã phân công**, stepper bước 5, đủ 2 nút [Chấp nhận] [Từ chối], badge "Còn 9 ngày LV" (ảnh `06-tvv-cg-detail-truoc-tu-choi.png`) | Không |
| Dữ liệu tiền đề (bản ghi phân công) | VV phân công cho **chính tài khoản đang đăng nhập** — cột "Người xử lý / Tổ chức" = `huongcg` ở mọi dòng danh sách | `nguoiXuLyId` = `5432719c-c542-4a5d-8c3a-db1b8a918bbf` = **đúng userId** của `qa_tvvseed28`; bảng Phân công hiện "QA TVV Seed28 Active · Chờ xác nhận" → thoả SRS PRE-02 (`srs-fr-05-vu-viec.md:806`) | Không |
| Input / giá trị nhập (lý do từ chối) | "TKM test từ chối thành công" — 27/1000 ký tự, hợp lệ (≥10) | "QA verify XNTGHTVV_03 lan 2 - vai tro TVV va CG - tu choi tham gia" — hợp lệ (≥10), cùng modal "Từ chối phân công", cùng giới hạn 1000 ký tự | Không |

**Kết luận: 0 GAP.** GAP vai trò được đóng bằng **test thật** (gán vai trò CG → đăng nhập lại → `auth/me` xác nhận `["TVV","CG"]` → chạy lại thao tác), KHÔNG đóng bằng lập luận.

**Tái hiện 2/2:** lần 1 vai trò TVV trên VV-BTP-TW-20260712-001 → màn 403; lần 2 vai trò TVV·CG (khớp đối tác) trên VV-BTP-TW-20260712-005 → màn 403 y hệt, in "Vai trò hiện tại: TVV CG".

Chi tiết phép đo, kiểm chứng API, và phân tích ý 2 của đối tác: xem [`../reverify-audit/XNTGHTVV_03/audit.md`](../reverify-audit/XNTGHTVV_03/audit.md).
