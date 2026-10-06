# Bảng đối chiếu điều kiện — TKTVV_02 (re-verify sau dev fix, 2026-07-15)

Re-test đúng vai trò/màn/thẻ mà bug gốc mô tả (bug-report §Các bước tái hiện).

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Màn hình | Danh sách Tư vấn viên / Chuyên gia (`/chuyen-gia-tvv/danh-sach`) | Đúng màn `/chuyen-gia-tvv/danh-sach` | Không |
| Thẻ đang đứng | Thẻ cụ thể "Đang hoạt động" | Thẻ "Đang hoạt động" (selected) | Không |
| Thao tác kiểm | Quan sát 3 trường lọc Tổ chức / Trạng thái / Lĩnh vực | Inspect DOM 3 trường + mở dropdown Lĩnh vực chọn 2 giá trị (Thuế + Thương mại) | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix cả 3 ý** — (1) "Tổ chức" là `ant-select` dropdown (không còn ô nhập chữ), (2) "Trạng thái" KHÔNG hiển thị trên thanh lọc khi đang ở tab cụ thể (chỉ còn Ngày công nhận trong Bộ lọc nâng cao), (3) "Lĩnh vực" là `ant-select-multiple` — giữ được đồng thời ≥2 lĩnh vực. Ý "giá trị mặc định = Tất cả" vẫn là BA confirm (không thuộc bug).
