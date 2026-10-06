# Bảng đối chiếu điều kiện — QLKCHTV_13 (row 7) — Xuất Excel khi tìm kiếm không có kết quả

**Kết luận:** BA confirm.
- Ý chính **tái hiện được**: bảng rỗng vẫn xuất ra file, không có thông báo chặn. Nhưng bản FR đang hiệu lực **không có** mục Xuất Excel cho Kho câu hỏi, nên không có câu thông báo nào để đối chiếu ⇒ phải để BA chốt, không log thành lỗi spec.
- Ý phụ "file xuất ra là file cũ của QLKCHTV_12" **KHÔNG tái hiện** trên môi trường nip.io — đã chứng minh máy chủ có áp dụng bộ lọc.

| Điều kiện có thể đổi kết quả | Đối tác (evidence video `partner-evidence/QLKCHTV_13.webm`, 17 frame ở `reverify-audit/QLKCHTV_13/frames/`) | Mình test (env nip.io, 27/07/2026 11:22) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", badge "BTP · TW" (đọc rõ ở frame t000, t002, t018, t020, t022, t026) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP | Không |
| Entity + trạng thái (state machine) | Bảng Kho câu hỏi thẻ "Tất cả", kết quả rỗng — hiện "Chưa có câu hỏi nào." | Bảng Kho câu hỏi thẻ "Tất cả", kết quả rỗng — hiện đúng chữ **"Chưa có câu hỏi nào."** (đọc thẳng DOM) | Không |
| Dữ liệu tiền đề | Kho có 44 bản ghi, nhưng bộ lọc cho ra 0 kết quả | Kho có 13 bản ghi, bộ lọc cho ra 0 kết quả — **cùng tình huống** "kho có dữ liệu nhưng bộ lọc rỗng" (không phải kho trống) | Không |
| Input / filter / giá trị nhập | Lọc `linhVucId` = Thuế **+ Từ ngày = 2026-07-29** (ngày tương lai) → 0 kết quả. Bấm [Xuất Excel] 2 lần | Lọc bằng **từ khoá không tồn tại** (`ZZZKHONGTONTAIQA9999`) → 0 kết quả. Bấm [Xuất Excel]. **Bổ sung** 2 phép đo đối chứng với bộ lọc Lĩnh vực để tách bạch nguyên nhân (xem Phương pháp thứ hai) | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Nội dung file xuất + Hành vi)

- File thật tải về khi bảng rỗng: `reverify-audit/QLKCHTV_13/files/loc-rong-kho-cau-hoi-20260727.xlsx` — đã **mở đọc nội dung**: đúng **1 dòng tiêu đề, 0 dòng dữ liệu**, kích thước 6.655 byte.
- Trạng thái màn hình ngay trước khi bấm xuất, đọc thẳng DOM: `"Chưa có câu hỏi nào."`, `soDong = 0`.
- Sau khi bấm [Xuất Excel]: không có khung thông báo nào xuất hiện trên màn (`toastConTrenMan = []`).
- Tầng mạng: `POST /api/v1/kho-cau-hois/export` → **200** (không phải 4xx, không có thông báo chặn).

## Phương pháp thứ hai (bắt buộc)

- **Ba phép đo so sánh kích thước file để kiểm chứng bộ lọc** — đây là phép thử quyết định cho ý "file xuất ra là file cũ":
  - Không lọc — 13 bản ghi trên bảng → file **8.075 byte**
  - Lọc Lĩnh vực = Thuế — 6 bản ghi trên bảng → file **7.433 byte** *(đọc từ `content-length` của phản hồi)*
  - Lọc từ khoá không khớp — 0 bản ghi trên bảng → file **6.655 byte**

  Ba kích thước khác nhau và tăng đúng theo số bản ghi ⇒ **máy chủ CÓ áp dụng bộ lọc**, file xuất KHÔNG phải bản sao của lần xuất trước. Mở file lọc-rỗng ra cũng chỉ có tiêu đề, không có 13 dòng cũ.
- **Đọc thân yêu cầu để loại trừ khả năng giao diện không truyền bộ lọc:** `POST /api/v1/kho-cau-hois/export` body = `{"linhVucId":"bbbbbbbb-0000-4000-8000-000000000018","page":1,"pageSize":20}` ⇒ giao diện có truyền bộ lọc lên máy chủ.
- **Giải thích quan sát của đối tác (không phủ nhận bằng chứng của họ):** video cho thấy tên file đề xuất là `kho-cau-hoi-20260720 (1).xlsx` — hậu tố "(1)" do **trình duyệt** tự thêm khi trùng tên, vì máy chủ luôn đặt cùng một tên `kho-cau-hoi-{YYYYMMDD}.xlsx` (không có giờ phút — chính là ý (a) của QLKCHTV_12). Hai file cùng kích thước 8,0 KB có thể do bộ lọc trên môi trường của đối tác không được áp dụng, hoặc do mở nhầm file đã tải trước đó. Trên nip.io không tái hiện được, nên đề nghị đối tác kiểm lại và ghi rõ kích thước từng file.
- **Đối chiếu đặc tả:** đã tìm toàn bộ SRS v3.5 — **không có** cụm "Không có dữ liệu để xuất" hay tương đương cho Kho câu hỏi. Bản FR `srs-fr-13-tv-nhanh.md` thậm chí không có bước Xuất Excel: Processing chỉ tới bước 7 (dòng 111–119), thanh công cụ SCR-X2-01 (dòng 528) chỉ khai 3 nút *"+ Them cau hoi / Nhap Excel / Lam moi"*. Trong khi đó `CHANGELOG-v3-to-v3.5.md:2443-2449` lại khẳng định đã bổ sung nút [Xuất Excel] và bước 8 vào FR-X.2-01 ⇒ **mô tả trong CHANGELOG chưa được gộp vào FR**. Đây là lý do phải để BA chốt thay vì log lỗi.
