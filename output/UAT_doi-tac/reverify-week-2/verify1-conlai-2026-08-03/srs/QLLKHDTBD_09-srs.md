# QLLKHDTBD_09 — Cổng 3 (đối chiếu SRS)

> **Case đối tác:** Tuần 2, log row 354 — *"Xuất Excel với điều kiện lọc"*.
> **Đối tác báo:** *"Xuất Excel không theo điều kiện lọc, hệ thống xuất toàn bộ danh sách bài giảng."*
> **Nguồn SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).

> ⚠️ **Lệch tên màn hình — phải xác định trước khi verify.** Tiền tố `QLLKHDTBD` trong dự án này thuộc **Kế hoạch đào tạo** (`/dao-tao/ke-hoach/danh-sach`) — xem tiền lệ `QLLKHDTBD_02` và `QLLKHDTBD_06` tại `reverify-week-2/reverify-audit/QLLKHDTBD_02/audit.md` và `reverify-week-2/bug-reports/Pass-bug-report-UAT-tuan-2.md:359`. Nhưng phần mô tả lỗi của đối tác lại ghi *"danh sách **bài giảng**"* (thuộc Kho tài liệu / Bài giảng, tiền tố `QLKTLBG`). **Người verify phải xem video/ảnh của đối tác để chốt đang test màn nào**, rồi dùng nhánh trích dẫn tương ứng bên dưới. Kết luận SRS cho cả hai màn là như nhau, nhưng dòng trích dẫn khi log bug thì khác — quote nhầm màn → bug invalid.

---

## Mục SRS liên quan

### A. Quy tắc nghiệp vụ toàn hệ thống — BR-DATA-06

**`srs-v3.5.md:5524`** — nguyên văn:

> | BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file | Pattern IP-01 | **Toàn bộ CRUD list** | Báo cáo nhóm IX có xuất Word | Test export limit |

→ Phạm vi áp dụng ghi rõ *"Toàn bộ CRUD list"* → áp cho **mọi** màn danh sách, không cần từng FR nhắc lại. Ngoại lệ duy nhất được liệt kê là *"Báo cáo nhóm IX có xuất Word"* — không liên quan case này.

**`srs-fr-03-dao-tao.md:2220`** — bảng BR nhóm III xác nhận phạm vi (nguyên văn):

> | BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06, FR-III-14 |

### B. Nhánh 1 — nếu màn đang test là **Kế hoạch đào tạo** (SCR-III-00 / FR-III-14)

**`srs-fr-03-dao-tao.md:1752`** — nút Xuất Excel trên màn Kế hoạch đào tạo năm (nguyên văn):

> - Nút "Xuất Excel" (phụ): **xuất danh sách KH theo bộ lọc**, tối đa 10.000 dòng

**`srs-fr-03-dao-tao.md:1147`–`:1153`** — Processing "Xuất Excel" của FR-III-14 (nguyên văn):

> **Processing — Xuất Excel:**
>
> | Bước | Mô tả xử lý | BR áp dụng |
> |------|-------------|-----------|
> | 1 | Kiểm tra quyền | BR-AUTH-01 |
> | 2 | **Lấy danh sách theo filter**, tối đa 10.000 dòng | BR-DATA-06 |
> | 3 | Tạo file Excel + trả về download | — |

**`srs-fr-03-dao-tao.md:1201`** — Acceptance Criteria FR-III-14 (nguyên văn):

> - **Given** CB NV nhấn "Xuất Excel" **Then** tải file ≤ 10.000 dòng

**`srs-fr-03-dao-tao.md:1193`** — mã lỗi khi vượt hạn mức (nguyên văn):

> | E6 | Xuất Excel vượt 10.000 dòng | ERR-KH-06 | "Vượt giới hạn 10.000 dòng, vui lòng lọc nhỏ hơn" | ERROR |

**Bộ lọc của màn này — `srs-fr-03-dao-tao.md:1755`–`:1759`** (nguyên văn):

> **Thành phần 2 — Thanh lọc và tìm kiếm:**
> - Ô từ khóa: "Tìm theo tên kế hoạch"
> - Lọc Năm: dropdown năm
> - Lọc Trạng thái: 5 nhãn — Bản nháp · Chờ duyệt · Bị từ chối · Đã duyệt · Đã công khai
> - Lọc Đơn vị: chỉ TW có quyền lọc đa đơn vị; BN/ĐP mặc định khóa = đơn vị mình

### C. Nhánh 2 — nếu màn đang test là **Kho tài liệu / Bài giảng** (SCR-III-03 / FR-III-08)

**`srs-fr-03-dao-tao.md:1929`** — nút Xuất Excel trên màn Kho tài liệu (nguyên văn):

> - Nút "Xuất Excel" (phụ): **xuất danh sách theo bộ lọc hiện tại**, tối đa 10.000 dòng (BR-DATA-06)

**Bộ lọc của màn này — `srs-fr-03-dao-tao.md:1931`–`:1937`** (nguyên văn):

> **Thành phần 3 — Thanh lọc và tìm kiếm:**
> - Ô từ khóa: "Tìm theo tên bài giảng"
> - Lọc Loại tài liệu: Tất cả / Slide / PDF / Video
> - Lọc Lĩnh vực pháp luật (chọn nhiều — nguồn DANH_MUC loại LINH_VUC_PL)
> - Lọc Công khai: Tất cả / Đã công khai / Chưa công khai `[STT66 UAT 2026-06-02]`
> - Lọc Từ ngày / Đến ngày (theo ngày tạo)
> - Nút "Tìm kiếm" (chính) · "Xóa bộ lọc" (mờ)

### D. Tiền lệ trong cùng nhóm — cách SRS diễn đạt quy tắc này

**`srs-fr-03-dao-tao.md:1885`** — Quy tắc nghiệp vụ của SCR-III-01 (nguyên văn):

> - Xuất Excel tối đa 10.000 dòng **theo bộ lọc hiện tại**

**`srs-fr-03-dao-tao.md:1825`** (nguyên văn):

> - Nút "Xuất Excel" (phụ): xuất danh sách CTDT **theo bộ lọc**, tối đa 10.000 dòng

→ Cả 4 màn của nhóm III (Kế hoạch năm, CTDT, Kho tài liệu, danh sách kết quả) đều dùng **cùng một công thức chữ**: *"theo bộ lọc (hiện tại)"*. Không có màn nào được miễn.

---

## UC Reference

| Mục SRS | UC Reference | Dòng |
|---|---|---|
| **FR-III-14 Lập kế hoạch đào tạo năm** *(nhánh 1)* | **UC 33** | `srs-fr-03-dao-tao.md:1069` — *"**UC Reference:** UC 33 \| **Priority:** Essential \| **Stability:** High"* |
| **FR-III-08 Tìm kiếm tài liệu** *(nhánh 2 — FR sở hữu bộ lọc của SCR-III-03)* | **UC 27** | `srs-fr-03-dao-tao.md:800` |
| FR-III-07 Quản lý kho tài liệu, bài giảng *(nhánh 2)* | UC 26 | `srs-fr-03-dao-tao.md:723` |
| **SCR-III-00 Kế hoạch đào tạo năm** | **KHÔNG có dòng `UC Reference`** — mục đặc tả màn hình không mang trường này. Thay thế: `srs-fr-03-dao-tao.md:1742` (heading) + `:1745` — *"**FR sử dụng:** FR-III-14, FR-III-15, FR-III-16"* | 1742 / 1745 |
| **SCR-III-03 Kho tài liệu / Bài giảng** | **KHÔNG có dòng `UC Reference`.** Thay thế: `srs-fr-03-dao-tao.md:1918` (heading) + `:1921` — *"**FR sử dụng:** FR-III-07 (thêm/sửa/xóa bài giảng), FR-III-08 (tìm kiếm và lọc)"* | 1918 / 1921 |
| **BR-DATA-06** | Không phải UC — là Business Rule, `srs-v3.5.md:5524` | 5524 |

---

## Bảng Cổng 3 (khung, chưa điền cột thực tế web)

**Trước khi điền:** ghi rõ ở đây màn đang test là **Kế hoạch đào tạo** hay **Kho tài liệu / Bài giảng**: `________________`

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| Màn danh sách **có nút "Xuất Excel"** (`srs-fr-03:1752` nhánh 1 / `:1929` nhánh 2) | | |
| Xuất Excel khi **không đặt bộ lọc** → tệp chứa toàn bộ danh sách trong phạm vi quyền — ghi lại **số dòng** làm mốc đối chứng (`srs-v3.5.md:5524`) | | |
| **Đặt 1 bộ lọc rồi xuất** → số dòng trong tệp **bằng** số bản ghi màn hình đang hiển thị sau lọc, **nhỏ hơn** mốc ở trên (`:1752` / `:1929`, `srs-v3.5.md:5524`) | | |
| *(nhánh 1)* Lọc **Trạng thái** (vd chỉ "Bản nháp") → tệp chỉ chứa kế hoạch đúng trạng thái đó (`:1758`) | | |
| *(nhánh 1)* Lọc **Năm** → tệp chỉ chứa kế hoạch đúng năm (`:1757`) | | |
| *(nhánh 1)* Lọc **từ khóa tên kế hoạch** → tệp chỉ chứa bản ghi khớp (`:1756`) | | |
| *(nhánh 2)* Lọc **Loại tài liệu** (vd chỉ "Slide") → tệp chỉ chứa bài giảng đúng loại (`:1933`) | | |
| *(nhánh 2)* Lọc **Công khai** (Đã / Chưa công khai) → tệp chỉ chứa bản ghi đúng trạng thái (`:1935`) | | |
| *(nhánh 2)* Lọc **Từ ngày / Đến ngày** → tệp chỉ chứa bản ghi trong khoảng (`:1936`) | | |
| Kết hợp **≥2 bộ lọc** → tệp áp đồng thời (giao) cả hai điều kiện (`srs-v3.5.md:5524`) | | |
| **Nội dung tệp** đọc được và có cột dữ liệu tương ứng — mở tệp kiểm nội dung, không chỉ xác nhận tải được | | |
| Vượt 10.000 dòng → từ chối kèm thông báo tương ứng **ERR-KH-06** *"Vượt giới hạn 10.000 dòng, vui lòng lọc nhỏ hơn"* (`:1193`) — chỉ kiểm nếu dựng được dữ liệu đủ lớn, không thì ghi "không dựng được" | | |
| Phạm vi dữ liệu vẫn theo đơn vị: BN/ĐP xuất ra chỉ có bản ghi đơn vị mình (`:1759`, BR-AUTH-08 tại `srs-fr-03:2214`) | | |

> **Ghi chú cho người verify:** bắt buộc **mở tệp đọc nội dung** (đếm dòng, đối chiếu giá trị cột lọc), không được dừng ở "tải được tệp". Bằng chứng mạnh nhất là cặp số: *N dòng khi không lọc* vs *M dòng sau khi lọc*, kèm ảnh màn hình danh sách hiển thị "tổng số bản ghi" sau lọc.

---

## SRS có/không quy định

**Kết luận: (a) — SRS quy định RÕ, nếu tệp xuất không bám bộ lọc thì app đang sai → hướng `Open`.**

Bốn căn cứ độc lập, không dòng nào để ngỏ:

1. **`srs-v3.5.md:5524`** — BR-DATA-06 nói thẳng *"File xuất theo bộ lọc hiện tại"*, phạm vi *"Toàn bộ CRUD list"*. Đây là quy tắc toàn hệ thống, ngoại lệ duy nhất được ghi là báo cáo nhóm IX xuất Word.
2. **`srs-fr-03-dao-tao.md:1752`** (Kế hoạch đào tạo) — *"xuất danh sách KH theo bộ lọc"*.
3. **`srs-fr-03-dao-tao.md:1929`** (Kho tài liệu) — *"xuất danh sách theo bộ lọc hiện tại"*, dẫn thẳng BR-DATA-06.
4. **`srs-fr-03-dao-tao.md:1152`** — bước xử lý số 2 của FR-III-14 là *"Lấy danh sách theo filter"*. Bước lấy dữ liệu đã ràng buộc bộ lọc ngay trong luồng xử lý, không phải mô tả giao diện.

→ **Dù màn đang test là màn nào trong hai màn, kết luận SRS vẫn giống nhau.** Việc lệch tên màn chỉ ảnh hưởng **dòng trích dẫn** khi log bug, không ảnh hưởng hướng xử lý. Không có mục nào của SRS cho phép xuất toàn bộ danh sách bỏ qua bộ lọc.

**Không cần BA confirm.** Trường hợp duy nhất phải dừng lại: nếu verify cho thấy tệp xuất **đúng** bộ lọc (không tái hiện được) — khi đó theo tiền lệ dự án, case chuyển hướng "không tái hiện", không phải `BA confirm`.

---

## Câu hỏi cho BA

Không có — SRS quy định rõ, không rơi vào nhánh (b) hay (c).

*(Nếu verify phát hiện app xuất đúng bộ lọc trên màn này nhưng sai trên màn kia, ghi cả hai kết quả vào bảng Cổng 3 và tách case, đừng gộp.)*
