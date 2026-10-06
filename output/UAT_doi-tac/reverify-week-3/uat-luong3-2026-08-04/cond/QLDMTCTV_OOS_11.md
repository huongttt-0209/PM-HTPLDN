# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_11 (dòng 337) — Màn Chi tiết thiếu 3 tab và vùng tệp đính kèm

**Kết luận:** Pass — màn Chi tiết nay có đủ 3 tab, có vùng tệp đính kèm kèm nút Xem/Tải xuống, có mục Lĩnh vực, và đường dẫn kèm tên tổ chức.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (`cbnv_tw`, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` — cùng vai trò, cùng đơn vị | Không |
| Màn hình / entity + trạng thái | Màn Chi tiết Tổ chức tư vấn (`/chuyen-gia-tvv/to-chuc/{id}`); vòng 1 dùng hồ sơ trạng thái "Mới đăng ký" | Cùng màn, hồ sơ **TC-BTP-TW-0001** trạng thái "Đang hoạt động". Trạng thái khác nhau không ảnh hưởng: đặc tả dòng 1729–1732 không cho ẩn tab theo trạng thái, và 3 tab hiện đủ | Không |
| Dữ liệu tiền đề — tổ chức phải CÓ tệp | Vòng 1 dùng hồ sơ có 1 tệp PDF | Đo API: cả 12 tổ chức trên môi trường đều `fileDinhKem = []` ⇒ **tự dựng**: mở Sửa TC-BTP-TW-0001, đính kèm `qd-cong-bo-alpha-reverify-v2.pdf`, bấm Lưu (`PATCH` 200, thông báo "Cập nhật thành công") | Không |
| Dữ liệu tiền đề — tổ chức phải CÓ tư vấn viên liên kết | Không kiểm được vì không có tab | Chọn TC-BTP-TW-0001 vì `soTvvLienKet = 2` ⇒ tab thứ 2 có dữ liệu thật để soi | Không |
| Thao tác / input — ý 1: số tab | 0 tab | Đếm `.ant-tabs-tab` = **3**: "Thông tin" · "Tư vấn viên liên kết" · "Lịch sử". Mở từng tab: tab 2 có bảng 7 cột + 2 dòng; tab 3 có bảng 4 cột + 9 dòng nhật ký | Không |
| Thao tác / input — ý 2: vùng tệp + nút Xem/Tải xuống | Không có mục tệp, phải vào Sửa mới thấy | Có khối "Tệp đính kèm" ngay tab Thông tin, liệt kê tệp + **nút Xem** + **nút Tải xuống**. Bấm thật nút Xem → mở trình xem PDF đúng tệp, 1/1 trang | Không |
| Thao tác / input — ý 3: mục Lĩnh vực | Thiếu dù tổ chức có lĩnh vực | Bảng có dòng "Lĩnh vực pháp luật" với 3 thẻ: Doanh nghiệp · Lao động · Thương mại | Không |
| Thao tác / input — ý 4: đường dẫn | `… / Tổ chức tư vấn / Chi tiết` | `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Công ty Luật TNHH Alpha Hà Nội**` | Không |

**Bằng chứng:**
- `image/QLDMTCTV_OOS_11-v2-01-chi-tiet-3-tab-va-vung-tep-dinh-kem.png` — 3 tab trên đầu; bảng thông tin có "Lĩnh vực pháp luật" (3 thẻ) và "Số TVV liên kết 2"; khối "Tệp đính kèm" với `qd-cong-bo-alpha-reverify-v2.pdf` kèm nút Xem + Tải xuống; đường dẫn kết thúc bằng tên tổ chức.
- `image/QLDMTCTV_OOS_11-v2-02-tab-tu-van-vien-lien-ket-co-2-dong.png` — tab "Tư vấn viên liên kết": bảng STT/Mã TVV/Họ tên/Loại/Trạng thái TVV/Ngày tham gia/Trạng thái liên kết, 2 dòng (TVV-BTP-TW-0059, TVV-BTP-TW-0055).
- `image/QLDMTCTV_OOS_11-v2-03-tab-lich-su-9-dong-nhat-ky.png` — tab "Lịch sử": Thời gian/Người thực hiện/Hành động/Ghi chú-lý do, 9 dòng.
- `image/QLDMTCTV_OOS_11-v2-04-bam-Xem-mo-tep-PDF.png` — bấm "Xem" mở trình xem PDF đúng tệp.
- network `PATCH /api/v1/to-chuc-tu-vans/beb25e6f-…` [200] (dựng tiền đề tệp) · `GET /api/v1/to-chuc-tu-vans/{id}` [200] xác nhận `fileDinhKem` 1 tệp, `trangThaiQuet: SACH`.

**Ghi nhận thêm (không đổi verdict):** cột "Ngày tham gia" hiện "—" cho cả 2 dòng liên kết cũ; nút quay lại ghi "← Danh sách" trong khi đặc tả dòng 1716 ghi "← Quay lại danh sách".
