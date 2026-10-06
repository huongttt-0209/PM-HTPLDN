# QLDXDTTH_01 — Cổng 1 + Cổng 2 (AGENT-EVIDENCE, 2026-08-03)

> Sheet: `UAT_TGPL Doanh Nghiệp-tuần 2` row **118** · `fetch_evidence.py` **exit 0** (1 link Drive, tải được `QLDXDTTH_01_v2.webm`, 8.845.650 bytes).
> Ô "Ảnh/video 2" (cột T) **trống**. Video dài **~50 giây**, đã trích 17 frame/3s + 26 frame/1s (19–45s) + 17 frame/0,3s (33–38s).

## Cổng 1 — 3 dữ kiện neo

**(a) URL / mã bản ghi đối tác đang đứng**
- `uat.phapluat.gov.vn/danh-sach-ke-hoach-dao-tao` — **CỔNG PHÁP LUẬT QUỐC GIA** (chuyên trang DN/NHT), **KHÔNG phải CMS `htpldn-uat.ospgroup.vn`**.
- Điều hướng trong trang: `DANH MỤC → Đào tạo → Kế hoạch đào tạo`. Tiêu đề màn: **"Kế hoạch đào tạo"**, nút góc phải **"Gửi đề xuất đào tạo"**.
- **Mã đề xuất sau khi gửi: KHÔNG ĐỌC ĐƯỢC** — hệ thống không trả mã trong popup thành công và đối tác không mở màn nào khác.

**(b) Trạng thái entity**
- **TRƯỚC khi gửi** (`t000.00s`, đồng hồ trang `Thứ Năm, 23/07/2026, 16:18:41`): danh sách Kế hoạch đào tạo **đã rỗng sẵn** — *"Không tìm thấy kế hoạch đào tạo nào phù hợp."*
- **SAU khi gửi** (`t037.47s`, `16:19:18`) và **sau khi reload trang** (`t042.60s`, `16:19:23`): vẫn *"Không tìm thấy kế hoạch đào tạo nào phù hợp."*
- Ô tìm kiếm để trống, không có bộ lọc nào được áp.

**(c) Dữ liệu tiền đề**
Nội dung đề xuất đối tác nhập (đọc từ `t029.25s` + `t033.37s`):
| Trường | Giá trị |
|---|---|
| LĨNH VỰC * | `Dân sự` |
| ĐƠN VỊ TIẾP NHẬN * | `Cục Bổ trợ tư pháp – Bộ Tư pháp` |
| NỘI DUNG ĐỀ XUẤT * | `TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026` (51/5000 ký tự) |
| THỜI GIAN MONG MUỐN | `quý 3/2026` |
| ĐỊA ĐIỂM MONG MUỐN | `Hà Nội` |
| SỐ LƯỢNG HỌC VIÊN DỰ KIẾN | `10` |

Mô tả trong form: *"Doanh nghiệp có nhu cầu đào tạo các chủ đề pháp lý khác có thể đề xuất tại đây. Ban thư ký sẽ tiếp nhận và phản hồi."* Nút: `Hủy` / `Gửi đề xuất`.

## Cổng 2 — 3 dòng

**(1) Evidence đã xem + frame chứa LỖI**
`partner-evidence/QLDXDTTH_01_v2.webm`. Chuỗi frame:
- `t033.37s` (16:19:14) — nút submit chuyển sang spinner **"Đang gửi…"**.
- **`t034.26s` (16:19:15) = FRAME THÔNG BÁO THÀNH CÔNG:** modal giữa màn, icon check xanh, tiêu đề **"Đã gửi đề xuất thành công!"**, phụ đề *"Cảm ơn bạn đã gửi ý kiến đóng góp đào tạo. Ban chuyên môn thuộc Câu lạc bộ Pháp chế Doanh nghiệp sẽ nghiên cứu tổng hợp và đưa vào kế hoạch đào tạo sớm nhất."*
- **`t037.47s` (16:19:18) = FRAME LỖI theo cách đối tác hiểu:** đóng modal, quay lại màn "Kế hoạch đào tạo" — bảng vẫn hiện **"Không tìm thấy kế hoạch đào tạo nào phù hợp."** (đối tác bôi đen chính dòng chữ này để chỉ ra).
- `t042.60s` (16:19:23) — đối tác **reload trang** (nút stop `✕` đang hiện trên thanh địa chỉ), kết quả vẫn rỗng y hệt.
- 1 câu tả lỗi: *gửi đề xuất đào tạo xong hệ thống báo "Đã gửi đề xuất thành công!" nhưng danh sách trên màn (Kế hoạch đào tạo, cổng PLQG) vẫn rỗng cả trước lẫn sau khi tải lại trang, người gửi không thấy đề xuất của mình ở đâu.*

**(2) Đối tác phản ánh CỤ THỂ gì**
Không phải thiếu cột, không phải sai message — mà là: **sau khi báo thành công, đề xuất vừa gửi KHÔNG xuất hiện trên màn hình đang đứng**. Kết quả mong đợi ghi ở sheet gồm 3 ý: (i) tạo đề xuất ở trạng thái **"Mới"**, (ii) **gửi thông báo cho Cán bộ nghiệp vụ thuộc đơn vị tiếp nhận**, (iii) hiển thị thông báo "Đã gửi đề xuất đào tạo". Ý (iii) **đã đạt** trong video; đối tác đang than về việc không thấy bản ghi ở đâu (ý (i)).

**(3) Data + bước tái hiện chính xác**
1. Đăng nhập cổng **`uat.phapluat.gov.vn`** bằng tài khoản **Doanh nghiệp / Người hỗ trợ pháp lý** (cột "Tác nhân" của sheet ghi `Doanh nghiệp/Người hỗ trợ`).
2. `DANH MỤC → Đào tạo → Kế hoạch đào tạo` (URL `/danh-sach-ke-hoach-dao-tao`).
3. Bấm **"Gửi đề xuất đào tạo"**.
4. Nhập đúng bộ dữ liệu ở mục (c) phía trên → bấm **"Gửi đề xuất"**.
5. Đóng popup thành công → quan sát danh sách; sau đó **reload** và quan sát lại.

## Vai trò / tài khoản đối tác dùng

**Không xác định được tên/username.** Header cổng PLQG chỉ hiện **ảnh đại diện** (không có tên hiển thị, không mở menu tài khoản trong suốt video). Chắc chắn là **tài khoản đã đăng nhập trên chuyên trang DN/NHT `uat.phapluat.gov.vn`** (có avatar + chuông thông báo), khớp cột "Tác nhân" của sheet = **`Doanh nghiệp/Người hỗ trợ`** — **không phải** tài khoản cán bộ CMS.

## Ghi chú cho người verify

- 🔴 **Đây là case chạy trên CHUYÊN TRANG DN (`uat.phapluat.gov.vn`), không phải CMS.** Cần tài khoản DN/NHT đăng nhập được cổng. Nếu vướng VNeID → xem §External vs Internal của protocol trước khi punt: **việc "sinh thông báo cho Cán bộ nghiệp vụ đơn vị tiếp nhận" là internal, verify được trên CMS** (đăng nhập `cbnv_tw` / đơn vị `Cục Bổ trợ tư pháp` xem màn *Quản lý đề xuất đào tạo, tập huấn* + chuông thông báo).
- ⚠️ **Bẫy suy luận cần tránh:** màn đối tác đứng tên là **"Kế hoạch đào tạo"** — đây là danh sách *kế hoạch đào tạo đã công khai*, **không phải danh sách đề xuất**. Nó **đã rỗng từ trước khi bấm gửi** (`t000.00s`, 16:18:41). Vậy "rỗng sau khi gửi" **chưa chứng minh** đề xuất không được lưu. Muốn kết luận phải kiểm bản ghi ở nơi nó thực sự thuộc về (màn quản lý đề xuất phía CMS, hoặc màn "đề xuất của tôi" nếu SRS có quy định) — **KHÔNG kết luận từ mỗi màn này**.
- ⚠️ Phụ đề popup nói *"Ban chuyên môn … sẽ nghiên cứu tổng hợp và **đưa vào kế hoạch đào tạo sớm nhất**"* — tức chính hệ thống đang ngụ ý đề xuất **không** lên thẳng danh sách kế hoạch. Kỳ vọng của đối tác có thể lệch spec → cân nhắc nhánh `BA confirm`, đọc kỹ mục SRS màn hình trước khi chốt.
- Phản hồi dev ở sheet (cột P=`dev done`, cột R): *"create/list nhất quán (cùng đơn vị) + double-refresh (invalidate+refetch) — triệu chứng do bản build cũ. Đã có trên nhánh fix + deploy 120."* → khi re-verify **phải tải lại trang và ghi lại tên/bản dựng** (bài học đã có: tab MCP mở lâu vẫn chạy JS cũ).
- Cột "TKM phản hồi lần 1" ghi *"25/7: uc này đang lỗi nên các tc bên dưới test sau"* — tức các TC QLDXDTTH_* phía sau đang phụ thuộc case này.

## File evidence + frame đã dùng

| Loại | Đường dẫn tuyệt đối |
|---|---|
| Video gốc | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/QLDXDTTH_01_v2.webm` |
| Frame baseline (list đã rỗng TRƯỚC khi gửi) | `…/frames/QLDXDTTH_01/t000.00s.jpg` |
| Frame form mở, bắt đầu nhập | `…/frames/QLDXDTTH_01/t012.05s.jpg`, `…/t018.07s.jpg` |
| Frame form đã nhập đủ | `…/frames/QLDXDTTH_01/dense/t029.25s.jpg` |
| Frame submit ("Đang gửi…") | `…/frames/QLDXDTTH_01/dense/t033.37s.jpg` |
| **Frame thông báo thành công** | `…/frames/QLDXDTTH_01/toast/t034.26s.jpg` (+ `t035.18s.jpg` đối tác bôi đen chữ) |
| **Frame LỖI — list vẫn rỗng sau khi gửi** | `…/frames/QLDXDTTH_01/dense/t037.47s.jpg` |
| Frame reload trang, vẫn rỗng | `…/frames/QLDXDTTH_01/dense/t042.60s.jpg` |

*(Thư mục gốc frame: `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/frames/QLDXDTTH_01/`)*

## Ngoài lỗi đối tác nêu, trong frame còn thấy gì bất thường? (dựa trên ảnh ĐÃ ĐỌC)

1. **Popup thành công không trả về mã đề xuất, không có nút "Xem đề xuất của tôi"** — người gửi không có bất kỳ đường dẫn nào để tra lại thứ vừa gửi. Đây có thể chính là gốc rễ cảm nhận "không hiển thị" của đối tác.
2. **Cụm menu `DANH MỤC` bên trái không có mục nào kiểu "Đề xuất của tôi"** — chỉ có `Tổng quan / Giới thiệu / Hoạt động Trung tâm / Đào tạo (Kế hoạch đào tạo, Khóa học) / Tư vấn pháp luật / Văn bản pháp luật / Nghiên cứu – trao đổi / Chương trình – kế hoạch`.
3. **Sai lệch từ ngữ giữa spec và UI:** sheet ghi thông báo mong đợi là *"Đã gửi đề xuất đào tạo"*, UI hiện *"Đã gửi đề xuất thành công!"*. Khác chữ nhưng cùng ý — ghi lại để người verify không quy oan.
4. **Phụ đề popup nhắc tới "Câu lạc bộ Pháp chế Doanh nghiệp"** trong khi Đơn vị tiếp nhận đối tác chọn là **"Cục Bổ trợ tư pháp – Bộ Tư pháp"**. Chuỗi thông báo có vẻ hardcode một tổ chức khác với đơn vị người dùng đã chọn — đáng soi.
5. **Tất cả 3 trường không bắt buộc (Thời gian / Địa điểm / Số lượng học viên) vẫn gửi được khi để trống**, và form không hiển thị bất kỳ validate nào — bình thường, chỉ ghi nhận để làm cơ sở nếu TC khác đòi validate.

*(Tất cả đọc trực tiếp từ pixel frame, không suy đoán. Chưa log bug — thuộc quyền người verify.)*
