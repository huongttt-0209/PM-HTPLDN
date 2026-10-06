# KTDGKQHT_02 — Cổng 3 (đối chiếu SRS)

> **Case đối tác:** Tuần 2, log row 260 — *"Kiểm tra dữ liệu hiển thị trong mỗi tab"*.
> **Đối tác báo:** Tab **Kết quả kiểm tra** thiếu các trường *Số buổi có mặt · Số buổi vắng có phép · Số buổi vắng không phép · Tổng số buổi*.
> **Nguồn SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25). Không dùng `input/srs-update-2026-5-5/`.

---

## Mục SRS liên quan

### A. Đặc tả màn hình — SCR-III-02 (Khóa học, 8 tab)

**`srs-fr-03-dao-tao.md:1891`** — nguyên văn:

> **Loại màn hình:** Chi tiết với **8 tabs** (Thay đổi 4 thêm Tab Lịch học; Thay đổi 9 thay Tab Chứng nhận v3 bằng Tab Công bố kết quả; STT 25 UAT 2026-05-26 thêm Tab Đề kiểm tra):

**`srs-fr-03-dao-tao.md:1896`** — Tab 4 **Điểm danh** (nguyên văn):

> 4. **Tab 4 — Điểm danh** `[v3.5 — Thay đổi 7+11; KTDGKQHT_03 UAT 2026-07-16 — bổ sung bộ chọn buổi + trạng thái rỗng]`: Cột STT · **Họ tên** · **Email** · **Số điện thoại** · **Đơn vị** · Buổi học (FK lich_hoc_id) · Trạng thái điểm danh (**Có mặt** / **Vắng có phép** / **Vắng không phép** — enum 3 trạng thái) · Ghi chú. Hỗ trợ Import Excel hàng loạt.

**`srs-fr-03-dao-tao.md:1901`** — Tab 5 **Kết quả kiểm tra** (nguyên văn — đây là tab đối tác đang test):

> 5. **Tab 5 — Kết quả kiểm tra** `[v3.5 — Thay đổi 7+10; KTDGKQHT_08 UAT 2026-07-16 — bổ sung điều kiện hiển thị + nhãn tạm tính]`: Cột STT · **Họ tên** · **Email** · **Số điện thoại** · **Đơn vị** · Đề kiểm tra · Điểm · Xếp loại (Giỏi/Khá/Trung bình/Không đạt — auto BR-KQ-01) · Kết quả (Đạt/Không đạt — auto BR-KQ-02) · Ghi chú.

→ **Danh sách cột Tab 5 do SRS liệt kê KHÔNG chứa 4 trường đối tác đòi.** Danh sách cột Tab 4 cũng không chứa (Tab 4 là điểm danh **per-buổi**, không phải số liệu tổng hợp).

### B. FR-III-05 — Quản lý kiểm tra, đánh giá kết quả (UC24)

**`srs-fr-03-dao-tao.md:520`** (nguyên văn):

> **Màn hình:** SCR-III-02 (chi tiet Khoa hoc — Tab 3 "Lich hoc & Diem danh" + Tab 4 "Ket qua kiem tra")

> ⚠️ **Cảnh báo trích dẫn:** dòng `:520` đánh số tab **cũ/lệch** (Tab 3 / Tab 4). Bản SCR-III-02 hiện hành và chính các dòng khác trong FR-III-05 (`:567`, `:633`, `:636`) đều dùng **Tab 4 = Điểm danh, Tab 5 = Kết quả kiểm tra**. Khi log bug phải dùng đánh số của SCR-III-02 (`:1896` / `:1901`), KHÔNG quote `:520`.

**`srs-fr-03-dao-tao.md:591`–`:607`** — bảng **Outputs** của FR-III-05 (nguyên văn các dòng liên quan):

> **Outputs `[v3.5 — Thay đổi 7+11 cổng duyệt 2026-05-06]`:**
>
> | # | Tên field | Kiểu logic | Mô tả |
> |---|----------|-----------|-------|
> | 6 | so_buoi_co_mat | number | Số buổi có mặt (CO_MAT) |
> | 7 | so_buoi_vang_phep | number | Số buổi vắng có phép (VANG_PHEP) |
> | 8 | so_buoi_vang_khong_phep | number | Số buổi vắng không phép (VANG_KHONG_PHEP) |
> | 9 | tong_buoi | number | Tổng số buổi |
> | 10 | ty_le_chuyen_can | number | % chuyên cần = (so_buoi_co_mat + so_buoi_vang_phep) / tong_buoi × 100 |

→ **4 trường đối tác đòi CÓ trong bảng Outputs của UC24** (dòng 600–603), kèm `ty_le_chuyen_can` (dòng 604). Nhưng bảng Outputs này mô tả **kết quả trả về của use case** (dùng chung cho cả 2 nhánh nhập liệu + luồng Xuất Excel `:583`–`:589`), **không phải danh sách cột của Tab 5**.

**`srs-fr-03-dao-tao.md:628`–`:637`** — Acceptance Criteria FR-III-05: **không có** AC nào yêu cầu Tab 5 hiển thị 4 trường chuyên cần. AC liên quan Tab 5 (`:633`) nguyên văn:

> - **Given** khóa học ở `DANG_DIEN_RA` **When** CB NV mở Tab 5 "Kết quả kiểm tra" **Then** hiển thị danh sách học viên + cho nhập điểm (A2) kèm nhãn "Kết quả tạm tính"

### C. BR-KQ-02 — nơi 4 trường được dùng làm đầu vào công thức

**`srs-fr-03-dao-tao.md:2250`–`:2252`** (nguyên văn):

> 1. **Tỷ lệ chuyên cần ≥ ngưỡng tối thiểu của khóa**
>    - `ty_le_chuyen_can` = (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi × 100
>    - Ngưỡng tối thiểu lưu tại trường `KHOA_HOC.ty_le_chuyen_can_toi_thieu` (mặc định 80%, cấu hình per khóa khi tạo)

### D. Entity — 4 trường là số liệu DẪN XUẤT, không lưu DB

**`srs-v3.5.md:2566`** §3.4.3.23 KET_QUA_DAO_TAO — bảng 16 trường (`:2573`–`:2588`) **không có** `so_buoi_co_mat` / `so_buoi_vang_phep` / `so_buoi_vang_khong_phep` / `tong_buoi` / `ty_le_chuyen_can`. Chỉ có `diem_danh` per-buổi (`:2577`, nguyên văn):

> | 5 | diem_danh | text | N | CHECK IN ('CO_MAT','VANG_PHEP','VANG_KHONG_PHEP') | — | Điểm danh per-buổi 3-giá-trị (F-16 GAP-III-08). Phân biệt vắng có phép vs không phép cho xếp loại chuyên cần |

→ 4 trường là **aggregate tính runtime** từ các bản ghi điểm danh per-buổi, không phải cột DB.

---

## UC Reference

| Mục SRS | UC Reference | Dòng |
|---|---|---|
| FR-III-05 Quản lý kiểm tra, đánh giá kết quả | **UC 24** | `srs-fr-03-dao-tao.md:519` — *"**UC Reference:** UC 24 \| **Priority:** Essential \| **Stability:** High"* |
| FR-III-06 Tìm kiếm kết quả | UC 25 | `srs-fr-03-dao-tao.md:651` |
| FR-III-17 Ghi nhận kết quả (chốt cuối khóa) | UC 36 | `srs-fr-03-dao-tao.md:1271` |
| **SCR-III-02 Khóa học** | **KHÔNG có dòng `UC Reference`** — mục đặc tả màn hình trong SRS v3.5 không mang trường này. Thay thế: `srs-fr-03-dao-tao.md:1889` (heading SCR-III-02) + `:1911` — *"**FR sử dụng:** FR-III-01, FR-III-05, FR-III-06, FR-III-17, FR-III-18, FR-III-19, FR-III-22, FR-III-NEW-04"* | 1889 / 1911 |

---

## Bảng Cổng 3 (khung, chưa điền cột thực tế web)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| Tab 5 "Kết quả kiểm tra" có cột **STT** (`srs-fr-03:1901`) | | |
| Tab 5 có cột **Họ tên** (`:1901`) | | |
| Tab 5 có cột **Email** (`:1901`) | | |
| Tab 5 có cột **Số điện thoại** (`:1901`) | | |
| Tab 5 có cột **Đơn vị** (`:1901`) | | |
| Tab 5 có cột **Đề kiểm tra** (`:1901`) | | |
| Tab 5 có cột **Điểm** (`:1901`) | | |
| Tab 5 có cột **Xếp loại** — auto theo BR-KQ-01 (`:1901`, `:2230`–`:2240`) | | |
| Tab 5 có cột **Kết quả** Đạt/Không đạt — auto theo BR-KQ-02 (`:1901`, `:2246`–`:2256`) | | |
| Tab 5 có cột **Ghi chú** (`:1901`) | | |
| Tab 5 hiển thị **nhãn "Kết quả tạm tính"** khi khóa chưa `DA_KET_THUC` (`:1903`) | | |
| Tab 4 "Điểm danh" có **bộ chọn buổi học** (dropdown Ngày · Khung giờ · Nội dung, KHÔNG date-picker) (`:1897`) | | |
| Tab 4 có cột **Trạng thái điểm danh** 3 giá trị Có mặt / Vắng có phép / Vắng không phép (`:1896`) | | |
| **[Trường đối tác đòi]** Hiển thị **Số buổi có mặt** — SRS đặt ở Outputs UC24 `:600`, KHÔNG đặt ở cột Tab 5 `:1901` | | |
| **[Trường đối tác đòi]** Hiển thị **Số buổi vắng có phép** — Outputs UC24 `:601`, không ở cột Tab 5 | | |
| **[Trường đối tác đòi]** Hiển thị **Số buổi vắng không phép** — Outputs UC24 `:602`, không ở cột Tab 5 | | |
| **[Trường đối tác đòi]** Hiển thị **Tổng số buổi** — Outputs UC24 `:603`, không ở cột Tab 5 | | |
| **[Liên quan]** Hiển thị **% chuyên cần** (`ty_le_chuyen_can`) — Outputs UC24 `:604` + đầu vào BR-KQ-02 `:2251` | | |
| **[Kiểm chéo]** 4 trường trên có xuất hiện ở **luồng Xuất Excel kết quả** (`:583`–`:589` Processing Xuất Excel) không | | |
| **[Kiểm chéo]** 4 trường trên có xuất hiện ở **màn khác** (Tab 4 tổng hợp / Tab 8 Công bố kết quả `:1909` / chi tiết học viên) không | | |

> **Ghi chú cho người verify:** phải điền cả 5 dòng cuối. Nếu app hiển thị 4 trường ở **Tab 4 Điểm danh** hoặc trong **file Excel xuất kết quả**, thì đó là "app đáp ứng cách khác" → khác hoàn toàn với "app thiếu chức năng".

---

## SRS có/không quy định

**Kết luận: (b) — SRS quy định nghiệp vụ chung, app có thể đáp ứng cách khác → hướng `BA confirm`.**

Ba căn cứ:

1. **Đặc tả màn hình nói NGƯỢC với kỳ vọng đối tác.** `srs-fr-03-dao-tao.md:1901` liệt kê **đầy đủ và đóng** 10 cột của Tab 5, không có 4 trường chuyên cần. Theo tiền lệ dự án, mục SCR là căn cứ nghiệm thu màn hình (xem chính `:1912` — *"mục SCR này tự mô tả đủ Thành phần, dùng làm căn cứ nghiệm thu"*). Chấm theo SCR thì **app đang đúng**, không phải bug.

2. **Nhưng 4 trường KHÔNG bị SRS loại bỏ** — chúng nằm ở bảng **Outputs của UC24** (`:600`–`:603`) và là đầu vào bắt buộc của công thức BR-KQ-02 (`:2251`). Nghĩa là hệ thống **phải tính được** chúng; SRS chỉ **không chỉ định hiển thị ở tab nào**.

3. **SRS không có dòng nào cấm** đưa 4 trường lên Tab 5, cũng **không có AC nào yêu cầu** đưa lên. Đây là khoảng trống đặc tả về **vị trí hiển thị**, không phải sai chức năng.

→ Không đủ căn cứ chấm `Open`. Cũng không nên chấm "không phải bug" gọn lỏn, vì bảng Outputs `:600`–`:603` cho đối tác một điểm tựa hợp lệ.

---

## Câu hỏi cho BA

1. Bốn trường `so_buoi_co_mat` / `so_buoi_vang_phep` / `so_buoi_vang_khong_phep` / `tong_buoi` (Outputs UC24, `srs-fr-03-dao-tao.md:600`–`:603`) **có bắt buộc hiển thị thành cột trên Tab 5 "Kết quả kiểm tra"** hay không? (có/không)
2. Nếu **không** — danh sách 10 cột tại `srs-fr-03-dao-tao.md:1901` có phải là danh sách **đóng** (app hiển thị đủ 10 cột là đạt) hay không? (có/không)
3. Nếu **có** — 4 trường đó thuộc Tab 5 "Kết quả kiểm tra" hay Tab 4 "Điểm danh"? (chọn 1) Và có cần bổ sung cả cột **% chuyên cần** (`ty_le_chuyen_can`, `:604`) để người dùng đối chiếu được kết quả Đạt/Không đạt theo BR-KQ-02 không? (có/không)
4. Việc 4 trường đó chỉ xuất hiện trong **file Excel xuất kết quả** (Processing Xuất Excel, `:583`–`:589`) có được coi là đáp ứng yêu cầu không? (có/không)
5. Dòng `srs-fr-03-dao-tao.md:520` đang đánh số tab lệch (Tab 3/Tab 4) so với SCR-III-02 (Tab 4/Tab 5) — BA xác nhận `:520` là dòng cũ cần sửa, và mọi trích dẫn phải theo SCR-III-02? (có/không)
