# Audit — TKHDVMTH_07 (verify phản ánh vòng 2)

> **Ngày:** 2026-07-27 · **Tester:** QA nội bộ · **Tài khoản:** `cbnv_tw` (Cán bộ NV Trung ương, BTP · TW)
> **Môi trường:** `https://htpldn-uat.ospgroup.vn` — **chính env đối tác** (đọc từ thanh địa chỉ trong video đối tác)
> **Verdict:** `Open` — ghi cột W (Trạng thái dev fix 2) dòng 123, tab `UAT_TGPL Doanh Nghiệp-tuần 1`
>
> **Re-test:** 2026-07-27 14:14 — ❌ FAIL, lỗi VẪN CÒN NGUYÊN trên env đối tác. Dev đã đổi W từ `Open` → `dev done` sau lần ghi 11:44, nhưng đo lại 6 truy vấn phân biệt cho kết quả **trùng khít lần trước** (B=C=22 · D=E=10 · A=F=4). Giao diện cũng khớp: ô lọc "Tiếp nhận" → thẻ "Đang xử lý 22" active, "Hiển thị 1-20 / 22 kết quả", bảng 4 "Tiếp nhận" + 16 "Đang xử lý". Đã ghi lại W=`Open`. Nhãn `HUY` vẫn là "Hủy" (SRS:1028 quy định "Đã hủy"). Ảnh: [`TKHDVMTH_07-r4-doitac-27-07-loc-tiepnhan-tra-22.png`](TKHDVMTH_07-r4-doitac-27-07-loc-tiepnhan-tra-22.png)

## Claim vòng 2 của đối tác

> "Khi chọn trạng thái *Tiếp nhận*, hệ thống hiển thị các bản ghi bao gồm *Đang xử lý* và *Tiếp nhận*"

Khác hẳn claim vòng 1 ("Tổng số bản ghi trên các tab hiển thị không đúng số lượng" — đã Verify=`Pass` ở vòng 1) → đây là claim MỚI, phải verify lần đầu.

## Cổng 1 — Bằng chứng đối tác

Tải bằng `fetch_evidence.py --row 123 --col-header "Ảnh/video 2"` → `partner-evidence-r2/TKHDVMTH_07_v2.webm` (3.518.935 bytes), trích frame mỗi 3s.

| Frame | Nội dung đọc được |
|---|---|
| `t003.03s.jpg` | URL `htpldn-uat.ospgroup.vn/hoi-dap?sortBy=ngayTao&sortOrder=ASC&page=1&trangThai=TIEP_NHAN` · header **Cán bộ NV Trung ương · CB_NV_TW · BTP·TW** · ô lọc Trạng thái = **"Tiếp nhận"** · thẻ **"Đang xử lý 21"** đang active · bảng toàn dòng "Đang xử lý" · đồng hồ máy 21/07/2026 16:08 |
| `t009.06s.jpg` | Đối tác bôi đen chữ "Tiếp nhận" ở dòng HD-20260510-003 để chỉ ra bảng lẫn cả 2 trạng thái |

**3 dữ kiện neo:** (a) URL + thẻ "Đang xử lý" · (b) bộ lọc Trạng thái = "Tiếp nhận" · (c) dữ liệu có sẵn cả TIEP_NHAN lẫn DANG_XU_LY.

## Cổng 2 — Hiểu bug

- **Evidence đã xem:** `TKHDVMTH_07_v2.webm`, frame lỗi `t003.03s` + `t009.06s` — ô lọc đang là "Tiếp nhận" nhưng bảng vẫn liệt kê hàng loạt dòng "Đang xử lý".
- **Đối tác phản ánh cụ thể:** bộ lọc Trạng thái không loại được bản ghi khác trạng thái (không phải lỗi nhãn hay lỗi đếm badge).
- **Data + bước tái hiện:** đăng nhập CB_NV_TW → Hỏi đáp pháp lý → thẻ "Đang xử lý" → ô lọc Trạng thái = "Tiếp nhận" → Tìm kiếm.

## Phép đo (loại claim: Filter/search/count)

| # | Truy vấn | Số bản ghi | Phân bố trạng thái | Nhận xét |
|---|---|---|---|---|
| A | Chỉ `trangThai=TIEP_NHAN` (không kèm thẻ) | 4 | TIEP_NHAN 4 | ✅ Lọc đúng — baseline |
| B | `trangThai=TIEP_NHAN` **+** `tab=DANG_XU_LY` (đúng thứ giao diện gửi khi bấm Tìm kiếm) | 22 | TIEP_NHAN 4 · DANG_XU_LY 18 | ❌ Bộ lọc trạng thái bị bỏ qua |
| C | Chỉ `tab=DANG_XU_LY` (không có bộ lọc trạng thái) | 22 | TIEP_NHAN 4 · DANG_XU_LY 18 | Kết quả **trùng khít B** → chứng minh tham số trạng thái không được áp dụng |
| D | `trangThai=HUY` + `tab=HOAN_THANH` (chọn "Hủy" trên UI) | 10 | HOAN_THANH 6 · HUY 4 | ❌ Lỗi lặp lại ở thẻ gộp thứ hai |
| E | `trangThai=HOAN_THANH` + `tab=HOAN_THANH` | 10 | HOAN_THANH 6 · HUY 4 | Trùng khít D → 2 lựa chọn khác nhau ra cùng kết quả |
| F | Chỉ `trangThai=HUY` (không kèm thẻ) | 4 | HUY 4 | ✅ Lọc đúng — baseline cho D |
| G | `trangThai=TIEP_NHAN` + `tab=TAT_CA` | 4 | TIEP_NHAN 4 | ✅ Thẻ "Tất cả" không có điều kiện cứng nên lọc chạy đúng |
| H | Đối chứng `trangThai=MOI` + `tab=MOI` | 18 | MOI 18 | Không lộ lỗi vì tập của thẻ trùng tập của bộ lọc |

**Bản chất (suy ra từ A–H):** máy chủ chỉ áp điều kiện của `tab`, bỏ qua `trangThai`. Hai thẻ gộp 2 trạng thái — "Đang xử lý" `IN (TIEP_NHAN, DANG_XU_LY)` và "Hoàn thành" `IN (HOAN_THANH, HUY)` — làm lỗi lộ ra; các thẻ đơn-trạng-thái che lỗi vì kết quả tình cờ trùng đáp án đúng.

**Ràng buộc UI cần biết:** khi người dùng chọn một giá trị ở ô lọc Trạng thái rồi bấm Tìm kiếm, giao diện **tự nhảy sang thẻ chứa trạng thái đó**. Vì vậy tổ hợp kiểu `tab=MOI` + lọc "Tiếp nhận" không thao tác được từ UI — chỉ quan sát được ở tầng truy vấn.

Chuỗi giao diện thực gửi khi bấm Tìm kiếm (đọc từ Performance resource entries của chính lần bấm):

```
/api/v1/hoi-daps?trangThai=TIEP_NHAN&tab=DANG_XU_LY&page=1&pageSize=20&sortBy=ngayTao&sortOrder=DESC
```

→ FE có gửi `trangThai`, BE trả nguyên tập của `tab`. Quan sát trên UI khớp: chân bảng "Hiển thị 1-20 / 22 kết quả".

**Phương pháp thứ hai (bug candidate ≠ bug):** ngoài đo qua API, đã chạy lại đúng thao tác trên UI (click thẻ → chọn ô lọc → bấm Tìm kiếm) và đọc DOM bảng — 20 dòng trang 1 gồm 4 "Tiếp nhận" + 16 "Đang xử lý". Hai phương pháp khớp nhau.

**Ảnh:** [`TKHDVMTH_07-r3-env-doitac-loc-tiepnhan-tra-ca-dangxuly.png`](TKHDVMTH_07-r3-env-doitac-loc-tiepnhan-tra-ca-dangxuly.png) (env đối tác, 27/07/2026 — ô lọc "Tiếp nhận", thẻ "Đang xử lý 22", bảng lẫn 2 trạng thái) · [`TKHDVMTH_07-r3-loc-huy-tra-ca-hoanthanh.png`](TKHDVMTH_07-r3-loc-huy-tra-ca-hoanthanh.png) (ô lọc "Hủy", thẻ "Hoàn thành 10", 6 Hoàn thành + 4 Hủy) · [`TKHDVMTH_07-r2-01-filter-tiepnhan-tra-dangxuly.png`](TKHDVMTH_07-r2-01-filter-tiepnhan-tra-dangxuly.png) (env được giao 18.143.165.120 — cùng hành vi, chụp trước khi biết env đối tác truy cập được).

## Cổng 3 — SRS vs thực tế web

| SRS yêu cầu (dẫn dòng) | Thực tế web | Đủ/Thiếu |
|---|---|:-:|
| `srs-fr-02-hoi-dap.md:466` — FR-II-05 (UC14) AC: "Given CB kết hợp nhiều điều kiện When tìm kiếm Then kết quả **AND logic**" | Thẻ "Đang xử lý" AND Trạng thái "Tiếp nhận" → vẫn trả cả DANG_XU_LY | ❌ Thiếu |
| `srs-fr-02-hoi-dap.md:1032` — SCR-II-01 thành phần 17 nút Tìm kiếm: "AND logic, đồng bộ URL" | Như trên | ❌ Thiếu |
| `srs-fr-02-hoi-dap.md:1028` — SCR-II-01 thành phần 14 ô lọc Trạng thái: `TIEP_NHAN` → "Tiếp nhận" và `DANG_XU_LY` → "Đang xử lý" là **2 lựa chọn tách biệt** | Ô lọc liệt kê đủ 8 lựa chọn đúng nhãn (đúng), nhưng chọn "Tiếp nhận" không thu hẹp kết quả | ❌ Thiếu (ở tầng áp dụng bộ lọc) |
| `srs-fr-02-hoi-dap.md:1021` / `:436` / `:440` — thẻ "Đang xử lý" = filter cứng `trang_thai IN ('TIEP_NHAN','DANG_XU_LY')` | Đúng: thẻ trả về đúng 22 bản ghi thuộc 2 trạng thái này | ✅ Đủ |
| `srs-fr-02-hoi-dap.md:1025` — thẻ "Hoàn thành" = filter cứng `trang_thai IN ('HOAN_THANH','HUY')` | Đúng: thẻ trả về đúng 10 bản ghi thuộc 2 trạng thái này, nhưng ô lọc "Hủy"/"Hoàn thành" đều không thu hẹp được | ❌ Thiếu (cùng gốc) |
| `srs-fr-02-hoi-dap.md:1028` — nhãn hiển thị của `HUY` là **"Đã hủy"** | Web hiển thị **"Hủy"** ở cả ô lọc lẫn cột Trạng thái | ❌ Thiếu (nhãn — Trivial) |

## Ngoài tiêu chí BA — có gì bất thường không?

Đã đọc lại 2 ảnh full-res: phát hiện thêm **1 điểm nhỏ** — nhãn trạng thái `HUY` trên web là **"Hủy"**, trong khi SRS dòng 1028 quy định nhãn hiển thị **"Đã hủy"** (thấy ở cả ô lọc và cột Trạng thái, ảnh `TKHDVMTH_07-r3-loc-huy-tra-ca-hoanthanh.png`). Đã ghi vào note gửi dev cùng bug này (cùng màn, cùng thành phần SRS dòng 1028) thay vì mở dòng TC riêng. Ngoài ra không thấy bất thường khác (cột, badge SLA, phân trang bình thường).
