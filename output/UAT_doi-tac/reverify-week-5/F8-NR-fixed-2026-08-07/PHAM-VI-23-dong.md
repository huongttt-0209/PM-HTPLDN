# PHẠM VI lô F8 — `Dopai = N/R` + `Trạng thái dev fix = Fixed`

> Đọc từ tab `bug` (spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, gid 1714340219)
> lúc **2026-08-07 ~11:3x giờ VN**. Ảnh chụp nguồn: `/tmp/bug_fresh_f8.json`.
> Nguồn có thể đổi trong lúc chạy → **đọc lại dòng của mình ngay trước khi ghi verdict**.

**Tổng: 23 dòng.**


---

## Dòng 10 — `KTDGKQHT_05` (Tuần 2)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **Fail** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | nếu thêm cột MHV có đc ko |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | KTDGKQHT_05.jpg |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | Màn hình danh sách không hiển thị mã học viên nhưng khi nhập file excel điểm danh hệ thống bắt buộc có mã học viên |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | CÓ — xem cuối file |

**Mô tả (G):**
```
Tải lên tệp Excel điểm danh
```
**Điều kiện (H):**
```
1. Đăng nhập tài khoản
2. Khóa học ở trạng thái "Đang diễn ra" hoặc "Đã kết thúc" và đã có lịch học.
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Đào tạo, tập huấn" -> "Khóa học"
2. Nhấn xem chi tiết khóa học
3. Chọn tab "Điểm danh" 
4. Tải lên tệp Excel
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hiển thị bản xem trước kết quả (số dòng hợp lệ, số dòng lỗi và lý do từng dòng). 
- Nạp thành công, hệ thống hiển thị thông báo "Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ".
```

---

## Dòng 308 — `QLHDTVVCG_02` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Điều kiện tìm kiếm / bộ lọc
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
```

---

## Dòng 309 — `QLHDTVVCG_03` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Tìm kiếm có kết quả
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
2. Tồn tại bản ghi phù hợp
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhập tiêu chí tìm kiếm
3. Nhấn "Tìm kiếm"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Có kết quả, hệ thống hiển thị danh sách hợp đồng phù hợp trên bảng kết quả.
```

---

## Dòng 310 — `QLHDTVVCG_04` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Tìm kiếm không có kết quả
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
2. Không tồn tại bản ghi phù hợp
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhập tiêu chí tìm kiếm
3. Nhấn "Tìm kiếm"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Không có kết quả, bảng dữ liệu để trống và hệ thống hiển thị thông báo "Không tìm thấy hợp đồng phù hợp".
```

---

## Dòng 311 — `QLHDTVVCG_05` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Nhập khoảng ngày với ngày bắt đầu muộn hơn ngày kết thúc
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. nhập khoảng ngày với ngày bắt đầu muộn hơn ngày kết thúc
3. Nhấn "Tìm kiếm"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Hệ thống chặn thao tác và hiển thị thông báo "Ngày bắt đầu phải trước ngày kết thúc".
```

---

## Dòng 314 — `QLHDTVVCG_08` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Biểu mẫu chi tiết — Nhóm 1: Thông tin chung
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn Xem chi tiết
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
```

---

## Dòng 315 — `QLHDTVVCG_09` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Biểu mẫu chi tiết — Nhóm 2: Vụ việc liên kết
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn Xem chi tiết
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
```

---

## Dòng 319 — `QLHDTVVCG_13` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Kiểm tra khi nhấn nút chức năng Thêm hợp đồng
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn"+ Thêm hợp đồng"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống mở màn hình biểu mẫu ở chế độ "Thêm mới" với các trường trống; các trường "Mã hợp đồng" và "Bên A" được hệ thống tự điền.
```

---

## Dòng 321 — `QLHDTVVCG_15` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Thêm hợp đồng thành công
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn"+ Thêm hợp đồng"
3. Nhập thông tin hợp lệ và nhấn Lưu
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Sinh mã hợp đồng HDTV-{YYYYMMDD}-{số thứ tự}, tạo bản ghi hợp đồng cùng toàn bộ mốc tiến độ, thanh toán giai đoạn, liên kết vụ việc, tệp đính kèm đã nhập; gán trạng thái "Đang thực hiện".
- Hệ thống hiển thị thông báo "Đã lưu hợp đồng" và quay về danh sách.
```

---

## Dòng 322 — `QLHDTVVCG_16` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Xuất Excel
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Tìm kiếm hợp lệ
3. Nhấn"Xuất Excel"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống xuất danh sách hợp đồng theo điều kiện lọc hiện tại ra tệp Excel:
+ Áp dụng toàn bộ bộ lọc đang hiển thị (từ khóa, tư vấn viên, khoảng ngày) và phân quyền dữ liệu theo đơn vị của NSD.
+ Tạo tệp định dạng .xlsx gồm các cột đang hiển thị trên màn hình danh sách, giới hạn tối đa 10.000 dòng trong một tệp.
+ Trả tệp về máy NSD với tên dạng HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx.
```

---

## Dòng 323 — `QLHDTVVCG_17` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Xóa Không có vụ việc liên kết
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
2. Không có vụ việc liên kết
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2.  Nhấn"Xóa" và xác nhận
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Hệ thống thực hiện xóa mềm (đánh dấu đã xóa, không xóa vật lý), lưu vết thao tác theo quy định, hiển thị thông báo "Đã xóa hợp đồng" và làm mới danh sách.
```

---

## Dòng 324 — `QLHDTVVCG_18` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Xóa Có vụ việc liên kết
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
2. Có vụ việc liên kết
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2.  Nhấn"Xóa" và xác nhận
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Hệ thống chặn thao tác và hiển thị thông báo "Không thể xóa hợp đồng đang có vụ việc liên kết".
```

---

## Dòng 325 — `QLHDTVVCG_19` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Kiểm tra khi nhấn nút chức năng Sửa
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn"Sửa"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống thống mở màn hình biểu mẫu ở chế độ "Chi tiết" cho phép chỉnh sửa; giữ nguyên mã hợp đồng và Bên A.
```

---

## Dòng 327 — `QLHDTVVCG_21` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Sửa thành công
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Hợp đồng Tư vấn"
2. Nhấn"Sửa"
3. Nhập thông tin hợp lệ và nhấn Lưu
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Giữ nguyên mã hợp đồng, cập nhật các trường thay đổi, thay thế danh sách mốc tiến độ / thanh toán / vụ việc liên kết / tệp đính kèm theo dữ liệu mới.
- Hệ thống hiển thị thông báo "Đã lưu hợp đồng" và quay về danh sách.
```

---

## Dòng 328 — `QLHDTVVCG_22` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Liên kết vụ việc
```
**Điều kiện (H):**
```
1.Điều kiện hiển thị: trong Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết.
```
**Các bước thực hiện (J):**
```
1. Mở Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết.
2. Bấm nút "+ Liên kết vụ việc"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống mở cửa sổ chọn vụ việc với ô tìm kiếm theo mã vụ việc, tên doanh nghiệp hoặc lĩnh vực; cho phép chọn nhiều vụ việc cùng lúc.
- NSD chọn vụ việc và bấm "Xác nhận", hệ thống thêm các vụ việc đã chọn vào bảng liên kết của hợp đồng; bản ghi liên kết nhiều-nhiều
```

---

## Dòng 329 — `QLHDTVVCG_23` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Bỏ liên kết
```
**Điều kiện (H):**
```
1.Điều kiện hiển thị: trên mỗi dòng của bảng vụ việc liên kết (Nhóm 2).
```
**Các bước thực hiện (J):**
```
1. Mở Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết.
2. Bấm nút "Bỏ liên kết"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống hỏi xác nhận "Bạn có chắc chắn muốn bỏ liên kết vụ việc «{mã vụ việc}»?". Nếu xác nhận, hệ thống bỏ dòng khỏi bảng
```

---

## Dòng 330 — `QLHDTVVCG_24` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Thêm mốc
```
**Điều kiện (H):**
```
1.Điều kiện hiển thị: trong Nhóm 3 (Mốc tiến độ) của biểu mẫu chi tiết.
```
**Các bước thực hiện (J):**
```
1. Mở Nhóm 3 (Mốc tiến độ) của biểu mẫu chi tiết.
2. Bấm nút "Thêm mốc"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống thêm một dòng trống vào bảng mốc tiến độ; NSD nhập trực tiếp trên dòng: Tên mốc, Ngày dự kiến, Ngày thực tế (tùy chọn), Trạng thái mốc.
```

---

## Dòng 332 — `QLHDTVVCG_26` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Thêm giai đoạn thanh toán
```
**Điều kiện (H):**
```
1.Điều kiện hiển thị: trong Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết.
```
**Các bước thực hiện (J):**
```
1. Mở Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết.
2. Bấm nút "Thêm giai đoạn thanh toán"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống thêm một dòng trống vào bảng; NSD nhập trực tiếp trên dòng: Giai đoạn, Số tiền, Ngày thanh toán (tùy chọn), Trạng thái thanh toán.
- Khi NSD nhập Số tiền, hệ thống tự cộng dồn và cập nhật thanh tiến trình tổng phía trên bảng. Nếu tổng số tiền các giai đoạn vượt Giá trị hợp đồng, hệ thống đánh dấu cảnh báo
```

---

## Dòng 333 — `QLHDTVVCG_27` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Xóa giai đoạn thanh toán
```
**Điều kiện (H):**
```
1.Điều kiện hiển thị: trên mỗi dòng của bảng thanh toán giai đoạn (Nhóm 4).
```
**Các bước thực hiện (J):**
```
1. Mở Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết.
2. Bấm nút "Xóa giai đoạn thanh toán"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Hệ thống bỏ dòng khỏi bảng và cập nhật lại thanh tiến trình tổng
```

---

## Dòng 341 — `TPDBCKQTHCT_02` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Báo cáo chưa đầy đủ
```
**Điều kiện (H):**
```
1. Đăng nhập hệ thống thành công
2. Báo cáo chưa đầy đủ
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Đợt báo cáo"
2. Mở Trang Chi tiết đợt báo cáo
3. Bấm nút "Trình phê duyệt"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
Hệ thống hiển thị "Vui lòng hoàn chỉnh báo cáo trước khi trình".
```

---

## Dòng 343 — `THBCTHCT_01` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | Tổng hợp báo cáo thực hiện chương trình hỗ trợ pháp lý |
| Tác nhân (F) | Cán bộ nghiệp vụ TW |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Tổng hợp báo cáo thực hiện chương trình từ nhiều đơn vị.
```
**Điều kiện (H):**
```
1. NSD là cán bộ nghiệp vụ cấp Trung ương và có ít nhất một báo cáo từ Bộ/Ngành hoặc Địa phương đã gửi lên.
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Đợt báo cáo"
2. Chọn các báo cáo cần tổng hợp trong bảng danh sách (ô chọn) và bấm nút "Tổng hợp", 
3. Bấm nút "Lưu tổng hợp"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Lưu bản ghi báo cáo tổng hợp toàn quốc.
+ Chuyển trạng thái các đợt báo cáo đã chọn: Đã gửi Trung ương → Đã tổng hợp.
+ Lưu vết thao tác theo quy định.
- Tổng hợp thành công, hệ thống hiển thị thông báo "Đã tổng hợp báo cáo toàn quốc".
```

---

## Dòng 344 — `THBCTHCT_02` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Kiểm tra khi bấm nút "Tổng hợp"
```
**Điều kiện (H):**
```
1. NSD là cán bộ nghiệp vụ cấp Trung ương và có ít nhất một báo cáo từ Bộ/Ngành hoặc Địa phương đã gửi lên.
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Đợt báo cáo"
2. Chọn các báo cáo cần tổng hợp trong bảng danh sách (ô chọn) và bấm nút "Tổng hợp",
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống:
+ Gợi ý số liệu tổng hợp: tính tổng các chỉ tiêu tương ứng theo Biểu 21a và Biểu 21b từ các báo cáo đã chọn.
+ Hiển thị biểu mẫu tổng hợp Biểu 21a, 21b toàn quốc cho phép cán bộ nghiệp vụ cấp Trung ương chỉnh sửa, bổ sung.
```

---

## Dòng 345 — `THBCTHCT_05` (Tuần 4)

| ô | giá trị |
|---|---|
| Tên chức năng (E) | (RỖNG) |
| Tác nhân (F) | (RỖNG) |
| Trạng thái (N) | **N/R** |
| Dopai (O) | N/R |
| Loại vấn đề (P) | (RỖNG) |
| Trạng thái dev fix (R) | **Fixed** |
| Ảnh/vieo 1 (M) | (RỖNG — không có bằng chứng đối tác) |
| Kết quả thực tế (L) | (RỖNG) |
| TKM phản hồi lần 1 (Q) | (RỖNG) |
| DEV phản hồi lần 1 (S) |  |
| Kết quả verify (T) — đã có sẵn? | (RỖNG) |

**Mô tả (G):**
```
Xuất tệp báo cáo tổng hợp
```
**Điều kiện (H):**
```
1. NSD là cán bộ nghiệp vụ cấp Trung ương và có ít nhất một báo cáo từ Bộ/Ngành hoặc Địa phương đã gửi lên.
2. Đã hoàn thành tổng hợp báo cáo toàn quốc và NSD là cán bộ nghiệp vụ cấp Trung ương.
```
**Các bước thực hiện (J):**
```
1. Chọn menu "Đợt báo cáo"
2. Bấm nút "Xuất Excel" hoặc "Xuất Word"
```
**KẾT QUẢ MONG ĐỢI (K) — đây là `expected đối tác`:**
```
- Hệ thống tạo tệp tổng hợp theo biểu mẫu Thông tư số 17/2025/TT-BTP — khổ A4, phông chữ Times New Roman cỡ 13, đầu trang có quốc hiệu và tên cơ quan, cuối trang có ngày ký và chức danh người ký.
- Đặt tên tệp theo định dạng BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}.xlsx hoặc .docx.
```