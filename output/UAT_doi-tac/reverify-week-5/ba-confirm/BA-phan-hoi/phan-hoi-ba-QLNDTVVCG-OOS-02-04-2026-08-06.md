# Phiếu chốt BA — Tư vấn chuyên sâu (FR-X.1)

**Ngày:** 06/08/2026 · Tuần 3 · **2 điểm cần BA quyết**, Dev chưa sửa code cho cả hai.

| # | Điểm | Nguồn |
|---|---|---|
| 1 | `QLNDTVVCG_OOS_04` — nhật ký không hiện lý do từ chối | QA báo |
| 2 | Chuyên gia có được sửa / tạo nội dung tư vấn không? | Dev phát hiện khi rà chỗ hở cùng kiểu |

> `QLNDTVVCG_OOS_02` và `QLNDTVVCG_OOS_03` **đã fix xong**, verify local + 120, không cần BA.

---

# Điểm 1 — `QLNDTVVCG_OOS_04`: nhật ký không hiện lý do từ chối

## Vấn đề

QA báo: chuyên gia từ chối phân công, nhật ký có ghi thao tác nhưng **không thấy lý do từ chối**. Đặc tả `srs-fr-12-tv-chuyen-sau.md:198` yêu cầu *"Ghi nhật ký thao tác (kèm lý do từ chối)"*.

Dev đo lại — **mô tả của QA chưa chính xác**:

- Lý do **CÓ** được lưu vào nhật ký, và **không** bị lượt từ chối sau ghi đè.
- Cán bộ Nghiệp vụ **CÓ** biết lý do ngay lúc bị từ chối (thông báo gửi họ có kèm dòng "Lý do: ...").
- Xem lại được ở màn **Quản trị → Nhật ký hệ thống** — nhưng **chỉ QTHT có quyền vào**.
- Trên khối "Nhật ký thao tác" của chính hồ sơ thì **không hiện** lý do, và không có nút mở rộng.

→ Hệ thống đã ghi nhật ký kèm lý do đúng câu chữ đặc tả, nhưng **Cán bộ Nghiệp vụ — người phải phân công lại — không tra lại được về sau**.

## 👉 Cần BA chốt

> Yêu cầu *"ghi nhật ký kèm lý do từ chối"* tính là **ĐẠT** hay **CHƯA ĐẠT**?

**[ ] ĐẠT** — dữ liệu đã ghi đúng đặc tả và tra cứu được qua Nhật ký hệ thống → ghi **Reject**, không sửa code.

**[ ] CHƯA ĐẠT — sửa theo cách B** *(Dev đề xuất)*: tách nhãn riêng cho thao tác "Từ chối" (hiện gộp chung nhãn "Cập nhật") và hiển thị đúng phần lý do trên hồ sơ.

**[ ] CHƯA ĐẠT — sửa theo cách A**: hiện toàn bộ nội dung chi tiết trên khối Nhật ký thao tác.
⚠️ Dev **không** khuyến nghị — phần này là bản chụp **toàn bộ hồ sơ tại từng thời điểm**, hiện ra sẽ để lộ mọi trường cho bất kỳ ai xem được hồ sơ.

---

# Điểm 2 — Chuyên gia có được sửa / tạo nội dung tư vấn không?

Phát hiện khi rà các chỗ hở **cùng kiểu** với `QLNDTVVCG_OOS_02`. Chưa từng được QA báo.

## Đo được gì

Dùng chính tài khoản chỉ mang vai trò Tư vấn viên + Chuyên gia, gọi lần lượt **mọi thao tác ghi** của màn Tư vấn chuyên sâu:

| Thao tác | Kết quả | Nhận xét |
|---|---|---|
| Phân công (đơn lẻ / hàng loạt) | **403** | đã vá hôm nay |
| Trình duyệt, Phê duyệt, Công khai, Hủy công khai, Xóa | **403** | có quyền riêng, an toàn sẵn |
| Hủy nội dung | **403** | đã xử lý ở QLNDTVVCG_36 |
| **Sửa nội dung** | **200 — SỬA ĐƯỢC THẬT** | nội dung bản ghi bị thay đổi |
| **Tạo mới nội dung** | **qua được tầng quyền** (chỉ báo lỗi dữ liệu nhập) | |

Nghĩa là chuyên gia hiện **sửa được nội dung của bất kỳ hồ sơ tư vấn nào trong đơn vị mình**.

## Vì sao Dev không tự quyết

Đặc tả viết **khác nhau có chủ ý** giữa hai chỗ:

- Bước phân công (dòng 170): *"Kiểm tra quyền **CB NV** và phạm vi đơn vị"* → nêu đích danh vai trò ⇒ Dev đã vá.
- Bước "Ghi nhận hoặc cập nhật nội dung" (dòng 132): *"Kiểm tra quyền và phạm vi đơn vị"* → **không** nêu vai trò.

Phần đầu mục FR-X.1-01 (dòng 97) ghi *"Tác nhân: Cán bộ Nghiệp vụ (TW/BN/ĐP)"* và liệt kê "ghi nhận... cập nhật" trong phạm vi của mục. Nhưng bảng bước xử lý lại không nhắc lại "CB NV" như chỗ phân công.

Hai cách hiểu đều có căn cứ:
- **Hiểu chặt:** tác nhân của cả mục là Cán bộ Nghiệp vụ ⇒ chuyên gia không được sửa/tạo ⇒ đây là lỗ hổng cần vá.
- **Hiểu rộng:** đặc tả cố ý không siết ở hai bước này (khác hẳn cách viết ở bước phân công) ⇒ chuyên gia được phép tham gia soạn nội dung ⇒ **không phải lỗi**.

Cấu hình quyền hiện tại đang theo cách hiểu rộng: vai trò Chuyên gia được cấp sẵn quyền tạo và sửa, kèm ghi chú trong mã nguồn *"UC147: nội dung tư vấn với CG"*.

## Rủi ro nếu siết

Chuyên gia **không** cần thao tác Sửa để lưu kết quả tư vấn — kết quả được gửi kèm ngay trong thao tác "Hoàn thành". Nên theo hiểu biết hiện tại, siết lại **không** chặn luồng nghiệp vụ nào của chuyên gia. Tuy vậy Dev không khẳng định tuyệt đối vì đây là thay đổi phạm vi ngoài phiếu QA và chưa kiểm thử đủ ở mọi màn.

## 👉 Cần BA chốt

**[ ] Giữ nguyên** — chuyên gia được phép tạo/sửa nội dung tư vấn. Ghi nhận là **đúng thiết kế**, không sửa.

**[ ] Siết lại** — chỉ Cán bộ Nghiệp vụ được tạo/sửa; chuyên gia chỉ thao tác qua các nút của luồng (nhận việc, từ chối, hoàn thành). Dev sẽ vá cùng khuôn đã dùng cho phân công và bổ sung kiểm thử cho mọi màn liên quan.

---
Hồ sơ điều tra: `../../reason-bug-bo-sung/CHECKLIST-BUG-BOSUNG-QA-tuan3.md` (mục 06/08/2026)
