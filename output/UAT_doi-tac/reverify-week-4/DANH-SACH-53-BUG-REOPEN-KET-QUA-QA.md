# Danh sách 53 bug Reopen UAT (OSP báo về) — Kết quả xử lý gửi QA

**Ngày:** 31/07/2026
**Phạm vi:** 53 test case UAT bị Reopen sau lần fix trước (Trạng thái = Fail, Dev fix = Reopen, chưa Pass ở lần 2).
**Nguồn dữ liệu:** File UAT OSP — sheet `UAT_TGPL Doanh Nghiệp` (cột "Mã TC", "Tuần", "Mô tả", lý do reopen của TKM).

## Tóm tắt kết quả

| Nhóm kết quả | Số lượng |
|---|---|
| ✅ Đã fix / Code đã đúng (chờ deploy + retest) | 8 |
| ✅ Không phải bug code — env-drift, OSP chạy bản cũ (cụm "Forbidden") | 44 |
| ⛔ Reject — không phải lỗi (đúng SRS) | 2 (+ một số ý phụ trong các bug khác) |
| **Tổng** | **53** |

**Phân bổ nhanh:**
- **44 bug** đều là màn **Báo cáo thống kê** báo lỗi **"Forbidden"** → **không phải bug code**, do OSP chạy bản cũ lúc retest (env-drift). Đã smoke check OSP UAT live 31/07 (v1.0.3): xem báo cáo + Xuất Excel/PDF = **200, không còn Forbidden**.
- **9 bug lẻ**: 6 đã fix / code đúng (một số chờ deploy), 2 reject theo SRS, 1 fix mới đợt này (QLCHTHXLHS_03 — chờ deploy).

---

## Mục A — 44 bug "Forbidden" ở màn Báo cáo thống kê (đều Tuần 3)

**Lý do reopen (chung):** TKM retest 31/07 — khi Xem báo cáo hoặc Xuất Excel/PDF, hệ thống hiển thị thông báo **"Forbidden"**.

**Kết quả xử lý (áp dụng cho cả 44 bug):** ✅ **ĐÃ HẾT / KHÔNG PHẢI BUG CODE (env-drift).**
- Verify trên build hiện tại (**V1.0.4**): Xem báo cáo và Xuất Excel/PDF đều trả **200**, không Forbidden.
- DB dump OSP 28/07: tài khoản `cbnv_tw` có đủ quyền `read_bao_cao` + `export_bao_cao`.
- **Smoke check OSP UAT live 31/07 (v1.0.3): view + Xuất Excel/PDF = 200, KHÔNG còn Forbidden.**
- **Nguyên nhân:** OSP chạy bản cũ tại thời điểm retest → **QA hard-reload (Ctrl+Shift+R) và retest lại trên OSP.**

| STT | Mã TC | Tuần | Chức năng / Mô tả ngắn | Lý do reopen (TKM) |
|---|---|---|---|---|
| 1 | SLHDVM_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 2 | SLHDVM_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 3 | VVDTN_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 4 | VVDTN_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 5 | VVDHT_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 6 | VVDHT_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 7 | VVDHTHT_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 8 | VVDHTHT_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 9 | VVTTG_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 10 | VVTTG_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 11 | CLDTBDDDR_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 12 | CLDTBDDDR_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 13 | LDTBDDDR_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 14 | LDTBDDDR_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 15 | CGTVPL_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 16 | CGTVPL_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 17 | DGHQHTPL_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 18 | DGHQHTPL_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 19 | CLDTBDPL_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 20 | CLDTBDPL_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 21 | VVTDVQL_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 22 | VVTDVQL_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 23 | VVTLV_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 24 | VVTLV_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 25 | VVTLHDN_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 26 | VVTLHDN_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 27 | VVTTGCT_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 28 | VVTTGCT_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 29 | CPHTCT_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 30 | CPHTCT_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 31 | CPCTHTTDVQL_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 32 | CPCTHTTDVQL_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 33 | CPCTHTTLHDN_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 34 | CPCTHTTLHDN_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 35 | CPCTHTTTG_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 36 | CPCTHTTTG_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 37 | SLCTHT_06 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 38 | SLCTHT_07 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 39 | CTTDVQL_04 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 40 | CTTDVQL_05 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 41 | CTTLV_05 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 42 | CTTLV_06 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |
| 43 | CTTTG_04 | 3 | Báo cáo thống kê – Xuất Excel | Hệ thống hiển thị thông báo "Forbidden" |
| 44 | CTTTG_05 | 3 | Báo cáo thống kê – Xuất PDF | Hệ thống hiển thị thông báo "Forbidden" |

---

## Mục B — 9 bug lẻ (kết luận riêng từng bug)

| STT | Mã TC | Tuần | Chức năng / Mô tả ngắn | Lý do reopen (TKM) | Kết quả xử lý | Ghi chú |
|---|---|---|---|---|---|---|
| 45 | TDHSTVV_13 | 2 | Gửi kết quả thẩm định — kết luận "Yêu cầu bổ sung" | Người hỗ trợ không nhận được thông báo kèm lý do | ✅ **Đã fix** | Code gửi thông báo Người hỗ trợ (in-app + email) khi thẩm định "Yêu cầu bổ sung" (commit `4e4c2c3e8`, có trong v1.0.3). Reopen 25/07 xảy ra **trước** bản fix 30/07 → retest lại. |
| 46 | NHSYC_02 | 2 | Hiển thị các trường thông tin trong form nhập thủ công (Vụ việc) | Lỗi vẫn chưa được fix | ✅ **Phần dev đã fix** | Trường "Ngày tiếp nhận" đã có ở form Vụ việc (bắt buộc, mặc định hôm nay). 7 ý phụ còn lại là quyết định BA/danh mục, không phải lỗi dev. |
| 47 | TKTMBMHD_07 | 3 | Xóa bộ lọc — Thư viện biểu mẫu | Hệ thống không trả về danh sách mặc định | ✅ **Đã fix + verified** | Nút "Xóa bộ lọc" reset về mặc định, gồm cả dãy tab phân loại về "Tất cả". |
| 48 | QLCHTHXLHS_02 | 3 | Thanh thẻ (tab) đầu trang — Cấu hình hệ thống | Lỗi chưa được fix | ⛔ **Reject (không phải lỗi)** | Màn Cấu hình hệ thống hiển thị đúng 3 thẻ theo SRS SCR-VIII-06 v2.1; kỳ vọng 4 thẻ đã lỗi thời (BA chốt 24/07). |
| 49 | QLCHTHXLHS_03 | 3 | Bảng cấu hình SLA ("Thời hạn xử lý / SLA") | SRS có 2 cột Cảnh báo mức 1/mức 2 nhưng hệ thống gộp chung "Vùng cảnh báo"; thiếu cột "Quá hạn (%)"; Loại yêu cầu tràn dữ liệu | ✅ **FIX MỚI đợt này** | PR #66, commit `a370b521e`: tách 2 cột Cảnh báo mức 1/mức 2, thêm cột "Quá hạn (%)", sửa Tag "Loại yêu cầu" tràn. **Chờ deploy để QA retest.** |
| 50 | QLCHTHXLHS_07 | 3 | Popup chỉnh sửa dòng SLA | Thiếu trường "Số ngày bổ sung tối đa" | ✅ **Code đã đúng** | Modal SLA có trường "Số ngày bổ sung tối đa"; OSP báo thiếu do bản OSP cũ (deploy gap). **Chờ redeploy + retest.** |
| 51 | QLTKND_03 | 3 | Thẻ trạng thái (tab nhanh) — Quản lý tài khoản | Thiếu thẻ "Vô hiệu hóa"; thẻ "Chờ kích hoạt" chưa có màu nhấn | ✅ **Đã fix** | 4 thẻ trạng thái đúng SRS. 2 ý đối tác **Reject**: SRS không có thẻ "Vô hiệu hóa" (lọc qua select) + không quy định màu tab. |
| 52 | QLDX_03 | 3 | Tự động đăng xuất khi hết phiên | Không hiển thị hộp thoại cảnh báo, chuyển thẳng màn Đăng nhập + "Đăng xuất thành công" | ⛔ **Reject (không phải lỗi code)** | FE + BE đúng SRS: cảnh báo phút 25, tự đăng xuất phút 30, idle server 30' khớp client. Triệu chứng do môi trường (OSP restart/redeploy hoặc tab chạy nền). |
| 53 | VVDTN_04 | 3 | Biểu đồ & bảng kết quả — BC Vụ việc đã tiếp nhận | Không hiển thị biểu đồ tròn theo lĩnh vực | ✅ **Đã fix** | Bảng thống kê theo lĩnh vực đã render. Ý "thiếu biểu đồ TRÒN" **Reject**: SRS UC125 quy định Bar + Trend + bảng (không bắt buộc pie; pie chỉ ở UC127). |

---

## Ghi chú cho QA

1. **Cụm 44 bug "Forbidden" (Mục A):** Đây là **env-drift** — OSP chạy bản cũ lúc retest, không phải lỗi code. Vui lòng **hard-reload (Ctrl+Shift+R)** rồi retest lại chức năng Xem báo cáo / Xuất Excel / Xuất PDF trên OSP. Đã smoke check OSP live 31/07 (v1.0.3): tất cả trả 200, không còn Forbidden.

2. **Các bug deploy-gap (chờ redeploy rồi retest):**
   - **QLCHTHXLHS_03** — fix mới (PR #66), chờ deploy bản mới.
   - **QLCHTHXLHS_07** — code đã đúng, chờ OSP redeploy.
   - **TDHSTVV_13** — đã có trong v1.0.3 (reopen xảy ra trước bản fix), retest lại.

3. **Các bug đã fix / code đúng — retest trực tiếp:** TKTMBMHD_07, QLTKND_03, VVDTN_04, NHSYC_02 (phần dev).

4. **Các bug Reject (không phải lỗi — đúng SRS), đề nghị đóng:**
   - **QLCHTHXLHS_02** — SRS SCR-VIII-06 v2.1 quy định 3 thẻ (BA chốt 24/07).
   - **QLDX_03** — SRS: cảnh báo phút 25, đăng xuất phút 30; triệu chứng do môi trường.
   - **VVDTN_04 (ý biểu đồ tròn)** — SRS UC125 không yêu cầu biểu đồ tròn (pie chỉ ở UC127).
   - **QLTKND_03 (ý "Vô hiệu hóa" + màu tab)** và **NHSYC_02 (7 ý phụ)** — thuộc quyết định BA/danh mục, không phải lỗi dev.
