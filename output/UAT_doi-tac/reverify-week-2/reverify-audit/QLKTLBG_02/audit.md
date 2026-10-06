# Audit verify vòng 2 — QLKTLBG_02 (row 8, tab tuần 2)

**Verdict:** `BA confirm` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/QLKTLBG_02-r2.md`](../../cond/QLKTLBG_02-r2.md)

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `QLKTLBG_02_v2.jpg` (269.187 byte, ảnh tĩnh) |
| Nội dung lỗi thấy trong ảnh | Bảng danh sách Kho tài liệu / Bài giảng chỉ có Tên bài giảng · Loại tài liệu · Dung lượng · (cột ngày bị cắt bởi vùng cuộn ngang) · Thao tác — không có cột Ảnh xem trước, Lĩnh vực, Người tạo |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` · (b) màn danh sách, bộ lọc mặc định "Bộ lọc nâng cao (2)" · (c) vai trò CB_NV_TW, BTP·TW |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Hiển thị)

Web thực tế có **đúng 6 cột** (đọc trực tiếp DOM `.ant-table-thead th`):
`Tên bài giảng · Loại tài liệu · Dung lượng · Ngày tạo · Công khai · Thao tác`.
⇒ **Quan sát của đối tác là ĐÚNG**: 3 trường họ nêu thật sự không có trong bảng danh sách.

| Trường đối tác đòi | SRS nói gì (dẫn line) | Kết luận |
|---|---|---|
| **Ảnh xem trước** | `srs-fr-03-dao-tao.md:1906` (SCR-III-03, STT66 UAT 2026-06-02): "**Panel chi tiết/preview** hiển thị thêm **Ảnh đại diện** (`anh_dai_dien`)…" — SRS đặt trường này ở **panel xem trước**, KHÔNG phải cột danh sách | Web **đúng SRS**: panel "Xem trước" có mục "Ảnh đại diện" (ảnh `QLKTLBG_02-r2-panel-xem-truoc.png`). Kỳ vọng đối tác (là cột trong bảng) khác vị trí SRS quy định |
| **Lĩnh vực** | `srs-fr-03-dao-tao.md:739` — `linh_vuc_ids` chỉ được quy định là **Input** khi thêm/sửa bài giảng; KHÔNG có trong Outputs (`:760-768`) và không được SCR-III-03 nêu là cột danh sách | **SRS silent** về cột Lĩnh vực trong bảng. Web có **bộ lọc** "Lĩnh vực pháp lý" nhưng không có cột |
| **Người tạo** | Không xuất hiện ở Inputs (`:735-746`), Outputs (`:760-768`) hay SCR-III-03 (`:1900-1906`) | **SRS silent** hoàn toàn |

**Điểm phát sinh khi soi (nêu để BA chốt cùng, KHÔNG log thành bug riêng):** FR-III-07 Outputs `:765` có trường
`khoa_hoc` ("Khóa học liên kết") nhưng bảng danh sách cũng không hiển thị. Tức bảng cột hiện tại không khớp trọn vẹn
với Outputs của FR — càng cho thấy SRS chưa chốt dứt khoát danh sách cột của SCR-III-03.

**Vì sao KHÔNG phải `Reject`:** đối tác quan sát đúng thực tế (3 trường thật sự vắng mặt) — không chứng minh được họ thao tác hay hiểu sai.
Bất đồng ở đây là về **ĐẶC TẢ** (kỳ vọng theo bản thiết kế vs SRS), nên theo QA_VERIFY_PROTOCOL §Verdict phải là `BA confirm`.

**Vì sao KHÔNG phải `Open`:** SRS không nêu tên 3 cột này ở bất kỳ chỗ nào cho màn danh sách; riêng "Ảnh đại diện" SRS
còn chỉ định rõ đặt ở panel preview và web đã làm đúng như vậy. Không có clause SRS nào để nói web sai.

## Phép đo đã chạy (artifact QUAN SÁT — loại claim: Hiển thị/render)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Đọc DOM header bảng | 6 cột: `Tên bài giảng, Loại tài liệu, Dung lượng, Ngày tạo, Công khai, Thao tác` | — |
| 2 | Ảnh full-res bảng danh sách ở viewport 1920 (đủ 6 cột, không cắt cụt) | Xác nhận không có Ảnh xem trước / Lĩnh vực / Người tạo | `QLKTLBG_02-r2-bang-danh-sach-full.png` |
| 3 | Mở panel "Xem trước" của 1 bài giảng | Panel có: Công khai · Ngày công khai · **Ảnh đại diện** · Mô tả công khai + khung preview file | `QLKTLBG_02-r2-panel-xem-truoc.png` |
| 4 | Ảnh bảng ở viewport 1440 (tái hiện đúng khung hình đối tác) | Bảng cuộn ngang, 2 cột Ngày tạo + Công khai bị đẩy khỏi vùng nhìn — giống hiện tượng cột bị cắt trong ảnh đối tác | `QLKTLBG_02-r2-bang-danh-sach-6-cot.png` |

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có 1 điểm về trải nghiệm, chưa đủ căn cứ SRS để log bug:** ở viewport 1440 (khung hình đối tác đang dùng), bảng bị cuộn ngang
làm 2 cột "Ngày tạo" và "Công khai" nằm ngoài vùng nhìn trong khi vùng trống bên phải vẫn còn — đây chính là lý do ảnh của đối tác
thấy cột ngày bị cắt. Đã gộp vào câu hỏi BA (chốt danh sách cột) thay vì log riêng, vì SRS không quy định bố cục/độ rộng cột.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- SRS `:1904` trỏ tới bản thiết kế `dac-ta-man-hinh-chuc-nang-v2.md — MH-03.3`. **File này KHÔNG có trong repo** (đã `find` toàn repo, 0 kết quả)
  → không đối chiếu được kỳ vọng của đối tác với bản thiết kế đã duyệt. Đây là lý do phải đẩy BA chốt chứ QA không tự quyết được.
- Phiên đăng nhập bị đá về `/login` 2 lần trong lúc đang thao tác (không idle), `GET /api/v1/auth/me` → 401. Ghi nhận để theo dõi tần suất,
  chưa đủ căn cứ kết luận là lỗi sản phẩm hay nhiễu môi trường/công cụ.
