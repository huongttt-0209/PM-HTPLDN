# Bảng đối chiếu điều kiện — QLDMTCTV_02 (dòng 317) — Bảng danh sách Tổ chức tư vấn thiếu ô tích chọn + cột STT

**Kết luận:** Pass — bảng nay đã có ô tích chọn (kèm ô chọn tất cả) và cột STT đánh số theo trang; ô tích chọn dùng được thật.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw + cbpd_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Đối tác không ghi rõ; vòng 1 đo bằng Cán bộ Nghiệp vụ TW | `cbnv_tw` (CB_NV_TW, Cục Bổ trợ tư pháp – Bộ Tư pháp) — bảng có ô tích chọn + STT. Đối chiếu thêm `cbpd_tw` (CB_PD_TW) ở thẻ "Chờ phê duyệt": cũng có ô tích chọn + STT | Không |
| Màn hình / entity + trạng thái | Mạng lưới Tư vấn viên → Tổ chức tư vấn, bảng danh sách | Đúng màn `/chuyen-gia-tvv/to-chuc`. Đo ở thẻ "Đang hoạt động" (8 dòng), "Mới đăng ký" (1 dòng), "Chờ phê duyệt" (3 dòng) — thẻ nào có dữ liệu cũng có ô tích chọn + STT | Không |
| Dữ liệu tiền đề | Bảng phải có ≥1 dòng mới thấy được ô tích chọn/STT | Có 12 tổ chức: 8 Đang hoạt động · 3 Chờ phê duyệt · 1 Mới đăng ký. Thẻ rỗng thì hiện trạng thái rỗng (đúng thiết kế) | Không |
| Thao tác / input | Chỉ mở màn danh sách rồi quan sát | Mở danh sách + **bấm thật** ô tích chọn dòng → hiện thanh thao tác hàng loạt "Đã chọn 1 tổ chức tư vấn" kèm nút Công khai / Hủy công khai / Bỏ chọn; ở thẻ "Chờ phê duyệt" (cbpd_tw) chọn 3 dòng → hiện "Phê duyệt hàng loạt" | Không |
| Các cột còn lại (yêu cầu "đúng định dạng, không tràn/đè, đồng nhất tiếng Việt") | Đối tác chỉ nêu thiếu ô tích chọn + STT | Header đọc được đủ 11 cột: (ô tích chọn) · STT · Mã tổ chức · Tên tổ chức · Loại hình · Lĩnh vực · Đơn vị quản lý · Người đại diện · Trạng thái · Công khai · Hành động. Chữ tiếng Việt thống nhất, không thấy tràn/đè | Không |

**Bằng chứng:**
- `image/QLDMTCTV_02-v2-01-bang-co-o-tich-chon-va-cot-STT.png` — ảnh toàn trang thẻ "Đang hoạt động": hàng tiêu đề có ô tích chọn ngoài cùng bên trái, cột **STT** đánh số 1→8, kèm các cột Mã tổ chức / Tên tổ chức / Loại hình / Lĩnh vực / Đơn vị quản lý và cột Hành động ghim bên phải.
- `image/QLDMTCTV_02-v2-02-cuon-ngang-cot-nguoi-dai-dien-trang-thai-cong-khai-hanh-dong.png` — cuộn ngang: thấy rõ Người đại diện, Trạng thái (nhãn xanh "Đang hoạt động"), Công khai (công tắc + chữ "Chưa công khai"), Hành động (3 biểu tượng mắt / bút chì / ba chấm).
- `image/QLDMTCTV_02-v2-03-tich-chon-dong-hien-thanh-thao-tac-hang-loat.png` — tích 1 dòng: ô tích xanh, thanh xanh "Đã chọn 1 tổ chức tư vấn" + Công khai / Hủy công khai / Bỏ chọn.
- `image/QLDMTCTV_02-v2-04-cbpd_tw-tich-chon-hien-nut-phe-duyet-hang-loat.png` — vai trò Cán bộ PD Trung ương, thẻ "Chờ phê duyệt", chọn 3 dòng → "Đã chọn 3 tổ chức tư vấn" + "Phê duyệt hàng loạt".
- Đối chiếu đặc tả: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1637 (Ô chọn – checkbox) và dòng 1638 (Số thứ tự – tự động đánh số theo trang).
- Network: `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200] → tổng 12 bản ghi, khớp số dòng từng thẻ.
