# QLKTLBG_09 — Cổng 3 (đối chiếu SRS)

> **Case đối tác:** Tuần 2, log row 281 — *"Xem bài giảng/tài liệu chứa Slide"*.
> **Đối tác báo:** *"Xem bài giảng dạng Slide: hệ thống tải tệp xuống thay vì trình chiếu inline."*
> **Nguồn SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).

---

## Mục SRS liên quan

### A. FR-III-07 — Quản lý kho tài liệu, bài giảng (UC26)

**`srs-fr-03-dao-tao.md:726`** — nguyên văn:

> **Mô tả:** Quản lý tài liệu/bài giảng dùng chung. 3 loại: Slide (PPTX), PDF, Video (YouTube embed). **Preview inline.** Switch công khai lên chuyên trang.

**`srs-fr-03-dao-tao.md:743`** — ràng buộc định dạng tệp (nguyên văn):

> | 4 | file_bai_giang | structured | Cond | Max 20MB, .pptx/.pdf (bắt buộc nếu SLIDE/PDF) |

**`srs-fr-03-dao-tao.md:790`** và **`:792`** — Acceptance Criteria (nguyên văn):

> - **Given** CB NV thêm bài giảng Slide/PDF **When** upload file ≤ 20MB **Then** lưu thành công + **preview được**
> - **Given** CB NV xem file **When** chọn preview **Then** **hiển thị nội dung trên trình duyệt**

### B. SCR-III-03 — Kho tài liệu / Bài giảng (sub-menu 4)

**`srs-fr-03-dao-tao.md:1920`** — nguyên văn:

> **Loại màn hình:** Danh sách + Bảng xem trước. 3 loại tài liệu: Slide (PPTX), PDF, Video (nhúng YouTube)

**`srs-fr-03-dao-tao.md:1951`** — cột Hành động của bảng tài liệu (nguyên văn):

> | Hành động | — | **Xem trực tuyến** · **Tải về (chỉ Slide/PDF)** · Sửa · Xóa (xóa mềm, có hộp xác nhận) |

→ SRS tách bạch **hai hành động riêng biệt**: "Xem trực tuyến" và "Tải về". Chúng không thay thế nhau.

**`srs-fr-03-dao-tao.md:1955`** — Thành phần 6, đoạn quyết định (nguyên văn):

> **Thành phần 6 — Bảng xem trước:** **Slide/PDF xem trực tiếp trong trình duyệt**; Video nhúng khung YouTube; **định dạng không xem được → "Không thể xem trực tuyến" + nút "Tải về"**. Khối thông tin kèm theo hiển thị **Ảnh đại diện**, **Ngày công khai** (`thoi_gian_dang_tai` — lần công khai gần nhất theo BR-PUBLIC-03), Mô tả công khai, Tệp đính kèm công khai `[STT66 UAT 2026-06-02]`. Tất cả là trường đã có ở entity BAI_GIANG — chỉ bổ sung hiển thị, không đổi cấu trúc.

**`srs-fr-03-dao-tao.md:1944`** — cột Tên bài giảng là điểm vào của Bảng xem trước (nguyên văn):

> | Tên bài giảng | `ten_bai_giang` | Liên kết — mở Bảng xem trước |

### C. Điểm cần chú ý — nhánh "định dạng không xem được"

`:1955` có **nhánh dự phòng hợp lệ**: nếu định dạng không xem được thì hệ thống hiển thị chữ *"Không thể xem trực tuyến"* **kèm nút "Tải về"**. Nhưng nhánh này đòi **hai điều kiện đồng thời**:
1. Có thông báo rõ ràng *"Không thể xem trực tuyến"* trên giao diện;
2. Hành vi là **hiện nút "Tải về"**, không phải **tự động tải xuống**.

`:743` giới hạn tệp Slide chỉ nhận `.pptx` — nên `.pptx` **nằm trong** danh sách phải xem trực tiếp, không rơi vào nhánh dự phòng. Nếu bản ghi đang test dùng đuôi khác (`.ppt`, `.pps`, `.odp`) thì phải ghi rõ trong bằng chứng vì lập luận sẽ đổi.

---

## UC Reference

| Mục SRS | UC Reference | Dòng |
|---|---|---|
| **FR-III-07 Quản lý kho tài liệu, bài giảng** | **UC 26** | `srs-fr-03-dao-tao.md:723` — *"**UC Reference:** UC 26 \| **Priority:** Essential \| **Stability:** High"* |
| FR-III-08 Tìm kiếm tài liệu | UC 27 | `srs-fr-03-dao-tao.md:800` |
| **SCR-III-03 Kho tài liệu / Bài giảng** | **KHÔNG có dòng `UC Reference`** — mục đặc tả màn hình không mang trường này. Thay thế: `srs-fr-03-dao-tao.md:1918` (heading SCR-III-03) + `:1921` — *"**FR sử dụng:** FR-III-07 (thêm/sửa/xóa bài giảng), FR-III-08 (tìm kiếm và lọc)"* | 1918 / 1921 |

> **Lưu ý nguồn thiết kế:** `:1922` ghi bản UX-Spec MH-03.3 đã **DEPRECATED**, và nói rõ: *"Bảng cột đã nội hóa xuống dưới — khi hai bên khác nhau thì lấy mục này làm căn cứ nghiệm thu"*. Tức mục SCR-III-03 trong SRS v3.5 là căn cứ, không phải file thiết kế cũ.

---

## Bảng Cổng 3 (khung, chưa điền cột thực tế web)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| Danh sách có cột Hành động chứa mục **"Xem trực tuyến"** (`srs-fr-03:1951`) | | |
| Danh sách có cột Hành động chứa mục **"Tải về"**, và mục này **chỉ có ở Slide/PDF** (`:1951`) | | |
| Bấm **Tên bài giảng** mở **Bảng xem trước** (`:1944`) | | |
| Bản ghi test là loại **Slide** và tệp có đuôi **.pptx** (`:743`) — ghi rõ tên tệp + đuôi | | |
| Bài giảng **Slide** được **xem trực tiếp trong trình duyệt** — nội dung slide render ngay trên trang, không phải tải về (`:1955`) | | |
| Bài giảng **PDF** được **xem trực tiếp trong trình duyệt** (`:1955`) — dùng làm phép đối chứng: nếu PDF xem được mà Slide không thì lỗi khu trú ở Slide | | |
| Bài giảng **Video** nhúng **khung YouTube** (`:1955`) — phép đối chứng thứ hai | | |
| Bấm "Xem trực tuyến" trên Slide **KHÔNG** kích hoạt tải tệp tự động (`:1951` tách 2 hành động) | | |
| Nếu hệ thống không render được: có hiện đúng chữ **"Không thể xem trực tuyến"** (`:1955`) | | |
| Nếu hệ thống không render được: có hiện **nút "Tải về"** (bấm mới tải) thay vì tự tải (`:1955`) | | |
| Bảng xem trước hiển thị **Ảnh đại diện** (`:1955`) | | |
| Bảng xem trước hiển thị **Ngày công khai** (`thoi_gian_dang_tai`, `:1955`) | | |
| Bảng xem trước hiển thị **Mô tả công khai** (`:1955`) | | |
| Bảng xem trước hiển thị **Tệp đính kèm công khai** (`:1955`) | | |

> **Ghi chú cho người verify:** bằng chứng phải bắt được **chính thao tác** bấm xem — ảnh chụp trang sau khi tệp đã tải về không chứng minh được điều gì. Ghi lại request mạng của thao tác (Content-Disposition `attachment` vs `inline`) là bằng chứng mạnh nhất.

---

## SRS có/không quy định

**Kết luận: (a) — SRS quy định RÕ, nếu app tải xuống thay vì render thì app đang sai → hướng `Open`.**

Ba căn cứ, không dòng nào mơ hồ:

1. **`srs-fr-03-dao-tao.md:1955`** nói thẳng: *"Slide/PDF **xem trực tiếp trong trình duyệt**"*. Đây là mục đặc tả màn hình — theo `:1922` chính là căn cứ nghiệm thu.
2. **`:1951`** liệt kê "Xem trực tuyến" và "Tải về" là **hai hành động khác nhau** trên cùng một dòng. Gộp hai hành động làm một (bấm xem → tải về) là làm mất một chức năng SRS đã đặt ra.
3. **`:792`** có Acceptance Criteria trực tiếp: *"**Given** CB NV xem file **When** chọn preview **Then** hiển thị nội dung trên trình duyệt"*. Đây là tiêu chí nghiệm thu, không phải mô tả tuỳ nghi. `:726` củng cố bằng cụm *"Preview inline"*.

**Hai điều kiện làm kết luận đảo chiều — phải kiểm trước khi chốt:**

- Nếu tệp đang test **không phải `.pptx`** (`:743` chỉ nhận `.pptx` cho Slide) → rơi vào nhánh *"định dạng không xem được"* của `:1955`, khi đó app **được phép** không render. Nhưng vẫn phải hiện chữ *"Không thể xem trực tuyến"* + **nút** "Tải về", chứ không tự động tải.
- Nếu app **có** hiện thông báo *"Không thể xem trực tuyến"* + nút "Tải về" và người dùng phải **bấm nút mới tải** → app đang đi đúng nhánh dự phòng, chuyển thành `BA confirm` (hỏi vì sao `.pptx` bị xếp vào "không xem được").

---

## Câu hỏi cho BA

*(chỉ dùng nếu verify rơi vào một trong hai điều kiện đảo chiều ở trên)*

1. `.pptx` có **bắt buộc** phải render được nội dung slide ngay trong trình duyệt, hay được phép rơi vào nhánh *"định dạng không xem được"* của `srs-fr-03-dao-tao.md:1955`? (bắt buộc render / được phép fallback)
2. Nếu được phép fallback: hệ thống có bắt buộc hiện đúng chuỗi *"Không thể xem trực tuyến"* + **nút** "Tải về" (người dùng bấm mới tải), thay vì tự động tải tệp xuống ngay khi bấm xem? (có/không)
