# Kết quả re-verify vòng 2 — 54 case dev báo đã fix

**Ngày chạy:** 2026-08-03 · **Môi trường:** https://htpldn-uat.ospgroup.vn · **Build:** HTPLDN **V1.0.4**
**Tài khoản:** `cbnv_tw` / `Test@1234` (vai trò `CB_NV_TW`, phạm vi Toàn quốc)
**Công cụ:** Chrome DevTools MCP (UI-driven, không verify bằng gọi API trực tiếp)
**Nguồn bug:** [DANH-SACH-53-BUG-REOPEN-KET-QUA-QA.md](../DANH-SACH-53-BUG-REOPEN-KET-QUA-QA.md) + `TLCTCDG_11`

> **Verdict tổng (chốt 2026-08-03):** đã chạy lại đủ **54/54** case trên web bằng Chrome DevTools MCP — **30 Pass · 3 Reopen · 21 BA confirm**.
> - **30 Pass** — chạy lại đúng luồng, đúng vai trò/state/data, kết quả khớp "Kết quả mong đợi" của phiếu.
> - **3 Reopen** — `CLDTBDPL_07` (bản PDF thiếu cột "Tỷ lệ đạt") · `TKTMBMHD_07` ("Xóa bộ lọc" reset thẻ nhưng danh sách vẫn lọc theo từ khóa cũ) · `QLTKND_03` (thẻ tab đã đúng 4, còn sai bảng màu badge cột Trạng thái).
> - **21 BA confirm** — đều là case xuất PDF báo cáo thống kê: bản xuất chạy được, nhưng đặc tả mâu thuẫn về khung trình bày (Thông tư 17/2025 vs mô tả riêng của báo cáo thống kê) nên cần BA chốt trước khi kết luận đúng/sai.
>
> Đối soát report ↔ sheet: **54/54 khớp**, không dòng nào ghi nhầm sang cột của dev.

> 📤 **Tài liệu gửi BA cho 21 case BA confirm:** [`GUI-BA-2026-08-03/`](GUI-BA-2026-08-03/) — đọc [`README-gui-ba-2026-08-03.md`](GUI-BA-2026-08-03/README-gui-ba-2026-08-03.md) trước, gửi nguyên thư mục là đủ.

---

## Phạm vi (chốt với user trước khi chạy)

| Nhóm | Số dòng | Ghi chú |
|---|---|---|
| Khớp file md ∩ sheet `Trạng thái dev fix 2` = `dev done` | 51 | `Verify 2` đang trống |
| `TLCTCDG_11` — `dev done`, `Verify 2` trống, không có trong file md | 1 | user chốt đưa vào phạm vi |
| `QLCHTHXLHS_02`, `QLDX_03` — sheet để `Reject` | 2 | user chốt vẫn verify thật, giữ nguyên cột W của dev |
| **Tổng** | **54** | |

**Ngoài phạm vi:** 11 dòng tuần 2 (`DKTGKH_12`, `QLKTLBG_02`, `QLGVTG_07`, `QLTVV_02`, `QLTVV_24`, `DKTGMLTVV_03`, `CNHSNLTVV_02`, `QLHSTVV_03`, `QLHSTVV_05`, `TDHSTVV_08`, `TDHSTVV_14`) — đã có `Verify 2 = Pass` từ vòng trước.

---

## Quy ước ghi sheet

| Kết quả | `Trạng thái dev fix 2` (W) | `Verify 2` (X) | `DEV phản hồi lần 2` (Y) |
|---|---|---|---|
| Pass | giữ nguyên | `Pass` | giữ nguyên |
| Reopen | `Reopen` | `Reopen` | ghi đè mô tả triệu chứng đang thấy |
| BA confirm | giữ nguyên | `BA confirm` | ghi câu hỏi gửi BA |

---

## Bảng 1 — Trạng thái toàn bộ case (snapshot LATEST)

| # | Mã TC | Tab · Dòng | Chức năng | Kết quả | Ghi chú |
|---|---|---|---|---|---|
| 1 | SLHDVM_06 | T3 · 191 | BC Số lượng hỏi đáp — Xuất Excel | ✅ Pass | Tải được file, đủ 4 header, số khớp màn hình |
| 2 | SLHDVM_07 | T3 · 192 | BC Số lượng hỏi đáp — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 3 | VVDTN_06 | T3 · 196 | BC Vụ việc đã tiếp nhận — Xuất Excel | ✅ Pass | Tải được file, đủ header, số khớp màn hình |
| 4 | VVDTN_07 | T3 · 197 | BC Vụ việc đã tiếp nhận — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 5 | VVDHT_06 | T3 · 203 | BC Vụ việc đang hỗ trợ — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 6 | VVDHT_07 | T3 · 204 | BC Vụ việc đang hỗ trợ — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 7 | VVDHTHT_06 | T3 · 209 | BC Vụ việc đã hoàn thành — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 8 | VVDHTHT_07 | T3 · 210 | BC Vụ việc đã hoàn thành — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 9 | VVTTG_05 | T3 · 216 | BC Vụ việc theo thời gian — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 10 | VVTTG_06 | T3 · 217 | BC Vụ việc theo thời gian — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 11 | CLDTBDDDR_06 | T3 · 222 | BC Lớp đào tạo đang diễn ra — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 12 | CLDTBDDDR_07 | T3 · 223 | BC Lớp đào tạo đang diễn ra — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 13 | LDTBDDDR_06 | T3 · 227 | BC Lớp đào tạo đã diễn ra — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 14 | LDTBDDDR_07 | T3 · 228 | BC Lớp đào tạo đã diễn ra — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 15 | CGTVPL_06 | T3 · 230 | BC Số lượng CG/TVV — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 16 | CGTVPL_07 | T3 · 231 | BC Số lượng CG/TVV — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 17 | DGHQHTPL_06 | T3 · 233 | BC Đánh giá hiệu quả HTPL — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 18 | DGHQHTPL_07 | T3 · 234 | BC Đánh giá hiệu quả HTPL — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 19 | CLDTBDPL_06 | T3 · 237 | BC Chất lượng đào tạo — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 20 | CLDTBDPL_07 | T3 · 238 | BC Chất lượng đào tạo — Xuất PDF | ❌ Reopen | Hết Forbidden nhưng PDF thiếu cột Tỷ lệ đạt |
| 21 | VVTDVQL_06 | T3 · 239 | BC Vụ việc theo đơn vị quản lý — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 22 | VVTDVQL_07 | T3 · 240 | BC Vụ việc theo đơn vị quản lý — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 23 | VVTLV_05 | T3 · 243 | BC Vụ việc theo lĩnh vực — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 24 | VVTLV_06 | T3 · 244 | BC Vụ việc theo lĩnh vực — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 25 | VVTLHDN_05 | T3 · 246 | BC Vụ việc theo loại hình DN — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 26 | VVTLHDN_06 | T3 · 247 | BC Vụ việc theo loại hình DN — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 27 | VVTTGCT_05 | T3 · 248 | BC Vụ việc theo thời gian chi tiết — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 28 | VVTTGCT_06 | T3 · 249 | BC Vụ việc theo thời gian chi tiết — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 29 | CPHTCT_06 | T3 · 250 | BC Chi phí chi trả hỗ trợ — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 30 | CPHTCT_07 | T3 · 251 | BC Chi phí chi trả hỗ trợ — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 31 | CPCTHTTDVQL_06 | T3 · 253 | BC Chi phí theo đơn vị — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 32 | CPCTHTTDVQL_07 | T3 · 254 | BC Chi phí theo đơn vị — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 33 | CPCTHTTLHDN_06 | T3 · 257 | BC Chi phí theo loại hình DN — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 34 | CPCTHTTLHDN_07 | T3 · 258 | BC Chi phí theo loại hình DN — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 35 | CPCTHTTTG_05 | T3 · 260 | BC Chi phí theo thời gian — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 36 | CPCTHTTTG_06 | T3 · 261 | BC Chi phí theo thời gian — Xuất PDF | ⚠️ BA confirm | Hết Forbidden, số liệu khớp; chờ BA chốt cách trình bày |
| 37 | SLCTHT_06 | T3 · 264 | BC Số lượng chương trình hỗ trợ — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 38 | SLCTHT_07 | T3 · 265 | BC Số lượng chương trình hỗ trợ — Xuất PDF | ⚠️ BA confirm | Không tái hiện Forbidden; xuất PDF OK — phần quốc hiệu/khối ký chờ BA chốt |
| 39 | CTTDVQL_04 | T3 · 268 | BC Chương trình theo đơn vị — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 40 | CTTDVQL_05 | T3 · 269 | BC Chương trình theo đơn vị — Xuất PDF | ⚠️ BA confirm | Không tái hiện Forbidden; xuất PDF OK — phần quốc hiệu/khối ký chờ BA chốt |
| 41 | CTTLV_05 | T3 · 273 | BC Chương trình theo lĩnh vực — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 42 | CTTLV_06 | T3 · 274 | BC Chương trình theo lĩnh vực — Xuất PDF | ⚠️ BA confirm | Không tái hiện Forbidden; xuất PDF OK — phần quốc hiệu/khối ký chờ BA chốt |
| 43 | CTTTG_04 | T3 · 275 | BC Chương trình theo thời gian — Xuất Excel | ✅ Pass | Không tái hiện Forbidden; xuất Excel OK, số liệu khớp |
| 44 | CTTTG_05 | T3 · 276 | BC Chương trình theo thời gian — Xuất PDF | ⚠️ BA confirm | Không tái hiện Forbidden; xuất PDF OK — phần quốc hiệu/khối ký chờ BA chốt |
| 45 | VVDTN_04 | T3 · 195 | BC Vụ việc đã tiếp nhận — thống kê theo lĩnh vực | ✅ Pass | Đã có mục theo lĩnh vực, số khớp; UC125 không có biểu đồ tròn |
| 46 | TKTMBMHD_07 | T3 · 91 | Thư mục biểu mẫu — nút "Xóa bộ lọc" | ❌ Reopen | Tab đã reset nhưng danh sách vẫn bị lọc theo từ khóa cũ |
| 47 | QLCHTHXLHS_02 | T3 · 152 | Cấu hình hệ thống — số thẻ trên màn hình | ✅ Pass | Đúng 3 thẻ theo đặc tả, mỗi thẻ mở được nội dung |
| 48 | QLCHTHXLHS_03 | T3 · 153 | Cấu hình hệ thống — bảng cấu hình SLA | ✅ Pass | Đủ cột CB mức 1/2 riêng + Quá hạn (%); không tràn |
| 49 | QLCHTHXLHS_07 | T3 · 156 | Form sửa cấu hình SLA — trường "Số ngày bổ sung tối đa" | ✅ Pass | Form đã có trường, lưu và giữ giá trị; hết Hệ số quá hạn |
| 50 | QLTKND_03 | T3 · 166 | Thẻ trạng thái (tab nhanh) — Quản lý tài khoản | ❌ Reopen | Thẻ đã đúng 4; còn sai bảng màu badge Trạng thái 3/4 |
| 51 | TLCTCDG_11 | T3 · 58 | Tiêu chí đánh giá — cảnh báo tổng trọng số ≠ 100% | ✅ Pass | Lưu OK + đúng cảnh báo 90%, đã kiểm tra lưu bền |
| 52 | TDHSTVV_13 | T2 · 67 | Thẩm định hồ sơ TVV — kết luận Yêu cầu bổ sung | ✅ Pass | Đủ 4 ý: đổi trạng thái, thông báo kèm lý do, lưu vết, câu xác nhận |
| 53 | NHSYC_02 | T2 · 88 | Form "Nhập thủ công" vụ việc HTPL | ✅ Pass | Đã có Ngày tiếp nhận; lưu thật VV-...-002, hiển thị lại đúng |
| 54 | QLDX_03 | T3 · 184 | Tự động đăng xuất khi hết phiên | ✅ Pass | Hộp thoại bật đúng 25 phút, tự đăng xuất đúng 30 phút |

**Tiến độ:** 54/54 · ✅ Pass 30 · ❌ Reopen 3 · ⚠️ BA confirm 21

## Bảng 2 — Case chưa xong / còn lỗi
| Mã TC | Vì sao | Cần làm gì | Ai làm |
|---|---|---|---|
| CLDTBDPL_07 | Tệp PDF thiếu cột "Tỷ lệ đạt" trong bảng danh sách khóa học so với màn hình và bản Excel | Triển khai bản mới lên môi trường đối tác rồi xuất lại đối chiếu — mã nguồn bản mới đã render đủ cột | Infra |
| CPCTHTTLHDN_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA xác nhận báo cáo thống kê có phải theo khung văn bản hành chính và quy ước đặt tên tệp riêng hay không | BA |
| CPCTHTTTG_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| SLCTHT_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CTTDVQL_05 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CTTLV_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CTTTG_05 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| SLHDVM_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVDTN_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVDHT_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVDHTHT_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVTTG_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CLDTBDDDR_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| LDTBDDDR_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CGTVPL_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| DGHQHTPL_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVTDVQL_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVTLV_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVTLHDN_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| VVTTGCT_06 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CPHTCT_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| CPCTHTTDVQL_07 | Đặc tả mâu thuẫn về cách trình bày tệp PDF (Thông tư 17/2025 vs mô tả đầu tệp riêng của báo cáo thống kê) | BA chốt báo cáo thống kê có phải theo khung văn bản hành chính không, và xác nhận quy ước tên tệp + ký số là bổ sung hay bỏ | BA |
| TKTMBMHD_07 | Nút "Xóa bộ lọc" xóa được giá trị trên giao diện nhưng không xóa tham số lọc khỏi truy vấn danh sách | Cho [Xóa bộ lọc] xóa cả tham số truy vấn (keyword, linhVucId, trạng thái, khoảng ngày) rồi tải lại danh sách mặc định; kiểm lại tổng số bản ghi phải bằng lúc mới vào màn | Dev FE |
| QLTKND_03 | Bảng màu badge cột Trạng thái lệch đặc tả 3/4 (Chờ kích hoạt xám thay vì vàng, Tạm khóa hổ phách thay vì đỏ, Vô hiệu hóa đỏ thay vì đen) | Gán lại màu badge theo đặc tả SCR-VIII-03 item 15; phần thẻ lọc giữ nguyên | Dev FE |

---

## Lỗi phát hiện thêm (ngoài 54 case — KHÔNG ghi vào sheet đối tác)

| Bug ID | Màn hình | Tóm tắt | Mức | File |
|---|---|---|---|---|
| BUG-QLCHTHXLHS-SLA-01 | Cấu hình hệ thống → Thời hạn xử lý (SLA) | Lưu được "Ngưỡng cảnh báo 2" = 100% trong khi đặc tả yêu cầu CB1 < CB2 < 100 (ô chặn ở ≤100 thay vì <100); cả 6/6 dòng đang để 100%, trùng mốc "Quá hạn" nên cảnh báo mức 2 mất tác dụng báo trước | Medium | [bug-report-qtht-vong-2.md](bug-reports/qtht/bug-report-qtht-vong-2.md) |

> Gặp khi chạy lại các case cấu hình SLA của vòng 2. Đã chạy lại đủ luồng lưu (99% → 100%) và **trả cấu hình về đúng trạng thái ban đầu** sau khi kiểm.

---

## Chi tiết từng case

### 1. ✅ SLHDVM_06 — BC Số lượng hỏi đáp/vướng mắc pháp luật · Xuất Excel (T3 dòng 191)

**Lý do reopen của TKM (31/07):** Hệ thống hiển thị thông báo "Forbidden".
**KQ mong đợi:** Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.

**Luồng đã chạy lại:** Đăng nhập `cbnv_tw` → menu **Báo cáo thống kê** → Loại báo cáo = *BC Số lượng hỏi đáp/vướng mắc pháp luật* → Kỳ = **Năm** (01/01/2026 – 31/12/2026) → Đơn vị = **Toàn quốc** → **[Xem báo cáo]** → **[Xuất Excel]**.

**Quan sát:**
- `GET /api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**, không Forbidden.
- Toast bắt bằng `MutationObserver`: chỉ có `Đang tạo file...`, **không** có toast lỗi, **không** có chữ "Forbidden".
- File tự tải về: `bao-cao-hoi-dap-2026-08-03.xlsx` (7 404 byte).
- Đọc nội dung file (openpyxl): đủ **4 dòng header** — tiêu đề · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 03/08/2026`.
- Số liệu trong file **khớp màn hình**: Tổng 61 · Đã trả lời 20 · Chờ trả lời 41 · Tỷ lệ 32,8% · Lao động 21 · Thuế 10 · Doanh nghiệp 7…

**Kết luận:** Không tái hiện "Forbidden", luồng xuất Excel chạy trọn vẹn và nội dung đúng → **Pass**.
**Bằng chứng:** [evidence/SLHDVM_06.log](evidence/SLHDVM_06.log) · [file xuất](evidence/SLHDVM_06-bao-cao-hoi-dap.xlsx) · [bảng điều kiện](cond/SLHDVM_06.md)
**Sheet:** tuần 3 dòng 191 → `Verify 2` = `Pass` ✅

### 2. ⚠️ SLHDVM_07 — BC Số lượng hỏi đáp — Xuất PDF (T3 dòng 192)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Tạo tệp PDF theo mẫu Thông tư 17/2025/TT-BTP — A4, Times New Roman 13, có header; tự tải về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Số lượng hỏi đáp/vướng mắc pháp luật* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → chọn A4 / Dọc → [Xuất file]

**Quan sát:**
- POST /api/v1/bao-cao/export → **200**, `content-type: application/pdf`, `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-08-03.pdf"` — không Forbidden
- Toast (MutationObserver): chỉ `Đang tạo file...` — không có toast lỗi, không có chữ "Forbidden"
- File tự động tải về `~/Downloads/bao-cao-hoi-dap-2026-08-03.pdf` (28 746 byte)
- Khổ giấy PDF = 595×842 pt = **A4** ✔ · font `Tinos-Regular/Bold` (bộ metric tương đương Times New Roman) ✔
- Đủ 3 dòng header dưới tiêu đề: `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 03/08/2026` ✔
- Số liệu trong PDF khớp màn hình: Tổng 61 · Đã trả lời 20 · Chờ 41 · 32.8% · Lao động 21 · Thuế 10…
- ⚠️ Còn lệch so với câu chữ KQ mong đợi (tồn tại từ vòng 1, không phải lỗi mới): thiếu quốc hiệu + tên cơ quan đầu trang, thiếu ngày ký + chức danh người ký cuối trang; tên tệp là `bao-cao-hoi-dap-YYYY-MM-DD.pdf` thay vì `BaoCaoHoiDap_{YYYYMMDD_HHmm}.pdf`

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/SLHDVM_07.log](evidence/SLHDVM_07.log) · [SLHDVM_07-bao-cao-hoi-dap.pdf](evidence/SLHDVM_07-bao-cao-hoi-dap.pdf) · [bảng điều kiện](cond/SLHDVM_07.md)
**Sheet:** tuần 3 dòng 192 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 3. ✅ VVDTN_06 — BC Vụ việc đã tiếp nhận — Xuất Excel (T3 dòng 196)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đã tiếp nhận* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Màn báo cáo render bình thường: Tổng vụ việc **51**, bảng Kênh tiếp nhận / Lĩnh vực PL / Đơn vị — không Forbidden
- Toast (MutationObserver): chỉ `Đang tạo file...` — không toast lỗi, không có chữ "Forbidden"
- File **tự động tải về** `~/Downloads/bao-cao-vu-viec-tiep-nhan-2026-08-03.xlsx` (7 234 byte)

**Kết luận:** Không tái hiện "Forbidden"; xuất Excel chạy trọn vẹn, nội dung file khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVDTN_06.log](evidence/VVDTN_06.log) · [VVDTN_06-bao-cao-vu-viec-tiep-nhan.xlsx](evidence/VVDTN_06-bao-cao-vu-viec-tiep-nhan.xlsx) · [bảng điều kiện](cond/VVDTN_06.md)
**Sheet:** tuần 3 dòng 196 → `Verify 2` = `Pass` ✅

### 4. ⚠️ VVDTN_07 — BC Vụ việc đã tiếp nhận — Xuất PDF (T3 dòng 197)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Tạo tệp PDF theo mẫu Thông tư 17/2025/TT-BTP — A4, Times New Roman 13, có header; tự tải về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đã tiếp nhận* → Kỳ = Năm → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → A4 / Dọc → [Xuất file]

**Quan sát:**
- Màn báo cáo render bình thường (Tổng vụ việc 51) — không Forbidden
- Toast: chỉ `Đang tạo file...` — không toast lỗi, không có chữ "Forbidden"
- File **tự động tải về** `~/Downloads/bao-cao-vu-viec-tiep-nhan-2026-08-03.pdf` (26 510 byte)
- Khổ giấy 595×842 pt = **A4** ✔ · đủ 3 dòng header (`Kỳ báo cáo` · `Đơn vị: Toàn quốc` · `Ngày tạo: 03/08/2026`) ✔
- Số liệu PDF khớp màn hình: Tổng 51 · Trực tiếp 39 · Hệ thống khác 6 · Doanh nghiệp 20 · Lao động 11…
- ⚠️ Lệch câu chữ KQ mong đợi có từ vòng 1 (không phải lỗi mới): thiếu quốc hiệu/tên cơ quan, thiếu ngày ký + chức danh; tên tệp `bao-cao-...-YYYY-MM-DD.pdf` thay vì `BaoCaoHoiDap_{YYYYMMDD_HHmm}.pdf`

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVDTN_07.log](evidence/VVDTN_07.log) · [VVDTN_07-bao-cao-vu-viec-tiep-nhan.pdf](evidence/VVDTN_07-bao-cao-vu-viec-tiep-nhan.pdf) · [bảng điều kiện](cond/VVDTN_07.md)
**Sheet:** tuần 3 dòng 197 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 5. ✅ VVDHT_06 — BC Vụ việc đang hỗ trợ — Xuất Excel (T3 dòng 203)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc đang hỗ trợ và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đang hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng vụ việc 31 — Bình thường 0 · Sắp hết hạn 0 · Quá hạn 5 · Quá hạn nghiêm trọng 26
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-dang-ho-tro-2026-08-03.xlsx (7.239 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 31; SLA 0/0/5/26; bảng theo NHT và bảng theo đơn vị (Cục Bổ trợ tư pháp 22 · An Giang 6 · Bắc Giang 2 · Bắc Ninh 1) — tổng cộng khớp 31
- ⚠️ Điểm nhỏ: dòng người hỗ trợ không xác định để trống ô tên trong tệp, trong khi màn hình hiển thị "(Không xác định)"; số lượng vẫn khớp — không ảnh hưởng kết luận

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVDHT_06.log](evidence/VVDHT_06.log) · [VVDHT_06-bao-cao-vu-viec-dang-ho-tro.xlsx](evidence/VVDHT_06-bao-cao-vu-viec-dang-ho-tro.xlsx) · [bảng điều kiện](cond/VVDHT_06.md)
**Sheet:** tuần 3 dòng 203 → `Verify 2` = `Pass` ✅

### 6. ⚠️ VVDHT_07 — BC Vụ việc đang hỗ trợ — Xuất PDF (T3 dòng 204)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc đang hỗ trợ và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đang hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng vụ việc 31 — Bình thường 0 · Sắp hết hạn 0 · Quá hạn 5 · Quá hạn nghiêm trọng 26
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-dang-ho-tro-2026-08-03.pdf (27.932 bytes), 2 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC ĐANG HỖ TRỢ" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 31; SLA 0/0/5/26; bảng theo NHT và bảng theo đơn vị (Cục Bổ trợ tư pháp 22 · An Giang 6 · Bắc Giang 2 · Bắc Ninh 1) — tổng cộng khớp 31
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVDHT_07.log](evidence/VVDHT_07.log) · [VVDHT_07-bao-cao-vu-viec-dang-ho-tro.pdf](evidence/VVDHT_07-bao-cao-vu-viec-dang-ho-tro.pdf) · [bảng điều kiện](cond/VVDHT_07.md)
**Sheet:** tuần 3 dòng 204 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 7. ✅ VVDHTHT_06 — BC Vụ việc đã hoàn thành — Xuất Excel (T3 dòng 209)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc đã hoàn thành và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đã hoàn thành* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng vụ việc 10 — Thành công 10 · Không thành công 0 · Tỷ lệ thành công 100%
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-hoan-thanh-2026-08-03.xlsx (7.060 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 10; Thành công 10; Không thành công 0; Tỷ lệ 100%; theo lĩnh vực (Doanh nghiệp 4 · Lao động 3 · Thuế 2 · Đầu tư 1 = 10); theo đơn vị (Cục Bổ trợ tư pháp 5 · An Giang 5 = 10)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVDHTHT_06.log](evidence/VVDHTHT_06.log) · [VVDHTHT_06-bao-cao-vu-viec-hoan-thanh.xlsx](evidence/VVDHTHT_06-bao-cao-vu-viec-hoan-thanh.xlsx) · [bảng điều kiện](cond/VVDHTHT_06.md)
**Sheet:** tuần 3 dòng 209 → `Verify 2` = `Pass` ✅

### 8. ⚠️ VVDHTHT_07 — BC Vụ việc đã hoàn thành — Xuất PDF (T3 dòng 210)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc đã hoàn thành và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc đã hoàn thành* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng vụ việc 10 — Thành công 10 · Không thành công 0 · Tỷ lệ thành công 100%
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-hoan-thanh-2026-08-03.pdf (24.891 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC ĐÃ HOÀN THÀNH" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 10; Thành công 10; Không thành công 0; Tỷ lệ 100%; theo lĩnh vực (Doanh nghiệp 4 · Lao động 3 · Thuế 2 · Đầu tư 1 = 10); theo đơn vị (Cục Bổ trợ tư pháp 5 · An Giang 5 = 10)
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVDHTHT_07.log](evidence/VVDHTHT_07.log) · [VVDHTHT_07-bao-cao-vu-viec-hoan-thanh.pdf](evidence/VVDHTHT_07-bao-cao-vu-viec-hoan-thanh.pdf) · [bảng điều kiện](cond/VVDHTHT_07.md)
**Sheet:** tuần 3 dòng 210 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 9. ✅ VVTTG_05 — BC Vụ việc theo thời gian — Xuất Excel (T3 dòng 216)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc theo thời gian và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng vụ việc toàn kỳ 51 — kỳ Năm 2026 tiếp nhận 51, hoàn thành 10
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-thoi-gian-2026-08-03.xlsx (6.911 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có đủ cột kỳ: bảng "Theo kỳ" gồm Kỳ / Từ ngày / Đến ngày / Tiếp nhận / Hoàn thành — dòng "Năm 2026 | 01/01/2026 | 31/12/2026 | 51 | 10" khớp màn hình
- Bảng theo đơn vị trong tệp khớp màn hình: Bắc Ninh 1 · Bắc Giang 2 · An Giang 20 · Bộ Kế hoạch và Đầu tư 1 · Cục Bổ trợ tư pháp 27 — cộng lại đúng 51

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, có cột kỳ và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVTTG_05.log](evidence/VVTTG_05.log) · [VVTTG_05-bao-cao-vu-viec-theo-thoi-gian.xlsx](evidence/VVTTG_05-bao-cao-vu-viec-theo-thoi-gian.xlsx) · [bảng điều kiện](cond/VVTTG_05.md)
**Sheet:** tuần 3 dòng 216 → `Verify 2` = `Pass` ✅

### 10. ⚠️ VVTTG_06 — BC Vụ việc theo thời gian — Xuất PDF (T3 dòng 217)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc theo thời gian và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng vụ việc toàn kỳ 51 — kỳ Năm 2026 tiếp nhận 51, hoàn thành 10
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-thoi-gian-2026-08-03.pdf (23.686 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC THEO THỜI GIAN" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có đủ cột kỳ: bảng "Theo kỳ" gồm Kỳ / Từ ngày / Đến ngày / Tiếp nhận / Hoàn thành — dòng "Năm 2026 | 01/01/2026 | 31/12/2026 | 51 | 10" khớp màn hình
- Bảng theo đơn vị trong tệp khớp màn hình: Bắc Ninh 1 · Bắc Giang 2 · An Giang 20 · Bộ Kế hoạch và Đầu tư 1 · Cục Bổ trợ tư pháp 27 — cộng lại đúng 51
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVTTG_06.log](evidence/VVTTG_06.log) · [VVTTG_06-bao-cao-vu-viec-theo-thoi-gian.pdf](evidence/VVTTG_06-bao-cao-vu-viec-theo-thoi-gian.pdf) · [bảng điều kiện](cond/VVTTG_06.md)
**Sheet:** tuần 3 dòng 217 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 11. ✅ CLDTBDDDR_06 — BC Lớp đào tạo đang diễn ra — Xuất Excel (T3 dòng 222)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Lớp đào tạo đang diễn ra và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Lớp đào tạo đang diễn ra* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng số 6 — Số trực tuyến 6 · Số trực tiếp 0
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-lop-dao-tao-dang-dien-ra-2026-08-03.xlsx (6.782 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 6; Trực tuyến 6; Trực tiếp 0; theo đơn vị (Cục Bổ trợ tư pháp 5 · An Giang 1 = 6)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CLDTBDDDR_06.log](evidence/CLDTBDDDR_06.log) · [CLDTBDDDR_06-bao-cao-lop-dao-tao-dang-dien-ra.xlsx](evidence/CLDTBDDDR_06-bao-cao-lop-dao-tao-dang-dien-ra.xlsx) · [bảng điều kiện](cond/CLDTBDDDR_06.md)
**Sheet:** tuần 3 dòng 222 → `Verify 2` = `Pass` ✅

### 12. ⚠️ CLDTBDDDR_07 — BC Lớp đào tạo đang diễn ra — Xuất PDF (T3 dòng 223)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Lớp đào tạo đang diễn ra và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Lớp đào tạo đang diễn ra* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng số 6 — Số trực tuyến 6 · Số trực tiếp 0
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-lop-dao-tao-dang-dien-ra-2026-08-03.pdf (23.493 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC LỚP ĐÀO TẠO ĐANG DIỄN RA" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 6; Trực tuyến 6; Trực tiếp 0; theo đơn vị (Cục Bổ trợ tư pháp 5 · An Giang 1 = 6)
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/CLDTBDDDR_07.log](evidence/CLDTBDDDR_07.log) · [CLDTBDDDR_07-bao-cao-lop-dao-tao-dang-dien-ra.pdf](evidence/CLDTBDDDR_07-bao-cao-lop-dao-tao-dang-dien-ra.pdf) · [bảng điều kiện](cond/CLDTBDDDR_07.md)
**Sheet:** tuần 3 dòng 223 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 13. ✅ LDTBDDDR_06 — BC Lớp đào tạo đã diễn ra — Xuất Excel (T3 dòng 227)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Lớp đào tạo đã diễn ra và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Lớp đào tạo đã diễn ra* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng khóa học 9 · Tổng học viên 15
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-lop-dao-tao-da-dien-ra-2026-08-03.xlsx (6.760 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng khóa học 9; Tổng học viên 15; theo đơn vị (Cục Bổ trợ tư pháp 8 khóa/10 học viên/7 trực tuyến/1 trực tiếp · An Giang 1 khóa/5 học viên/0 trực tuyến/1 trực tiếp)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/LDTBDDDR_06.log](evidence/LDTBDDDR_06.log) · [LDTBDDDR_06-bao-cao-lop-dao-tao-da-dien-ra.xlsx](evidence/LDTBDDDR_06-bao-cao-lop-dao-tao-da-dien-ra.xlsx) · [bảng điều kiện](cond/LDTBDDDR_06.md)
**Sheet:** tuần 3 dòng 227 → `Verify 2` = `Pass` ✅

### 14. ⚠️ LDTBDDDR_07 — BC Lớp đào tạo đã diễn ra — Xuất PDF (T3 dòng 228)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Lớp đào tạo đã diễn ra và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Lớp đào tạo đã diễn ra* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng khóa học 9 · Tổng học viên 15
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-lop-dao-tao-da-dien-ra-2026-08-03.pdf (23.287 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC LỚP ĐÀO TẠO ĐÃ DIỄN RA" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng khóa học 9; Tổng học viên 15; theo đơn vị (Cục Bổ trợ tư pháp 8 khóa/10 học viên/7 trực tuyến/1 trực tiếp · An Giang 1 khóa/5 học viên/0 trực tuyến/1 trực tiếp)
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/LDTBDDDR_07.log](evidence/LDTBDDDR_07.log) · [LDTBDDDR_07-bao-cao-lop-dao-tao-da-dien-ra.pdf](evidence/LDTBDDDR_07-bao-cao-lop-dao-tao-da-dien-ra.pdf) · [bảng điều kiện](cond/LDTBDDDR_07.md)
**Sheet:** tuần 3 dòng 228 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 15. ✅ CGTVPL_06 — BC Số lượng CG/TVV — Xuất Excel (T3 dòng 230)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Số lượng CG/TVV và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Số lượng CG/TVV* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng Tư vấn viên 11 — Số Tư vấn viên 6 · Số Chuyên gia 5
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-so-luong-cg-tvv-2026-08-03.xlsx (6.991 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 11; TVV 6; CG 5; theo đơn vị (Cục Bổ trợ tư pháp 5 TVV/5 CG/tổng 10 · An Giang 1/0/1 = 11); thêm bảng theo lĩnh vực pháp luật (Lao động 6 · Thuế 6 · Đất đai 4 · Doanh nghiệp 4 · Hành chính 1 · Dân sự 1 · Hình sự 1)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CGTVPL_06.log](evidence/CGTVPL_06.log) · [CGTVPL_06-bao-cao-so-luong-cg-tvv.xlsx](evidence/CGTVPL_06-bao-cao-so-luong-cg-tvv.xlsx) · [bảng điều kiện](cond/CGTVPL_06.md)
**Sheet:** tuần 3 dòng 230 → `Verify 2` = `Pass` ✅

### 16. ⚠️ CGTVPL_07 — BC Số lượng CG/TVV — Xuất PDF (T3 dòng 231)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Số lượng CG/TVV và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Số lượng CG/TVV* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng Tư vấn viên 11 — Số Tư vấn viên 6 · Số Chuyên gia 5
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-so-luong-cg-tvv-2026-08-03.pdf (23.790 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC SỐ LƯỢNG CG/TVV" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: Tổng 11; TVV 6; CG 5; theo đơn vị (Cục Bổ trợ tư pháp 5/5/10 · An Giang 1/0/1 = 11); bảng theo lĩnh vực pháp luật (Lao động 6 · Thuế 6 · Đất đai 4 · Doanh nghiệp 4 · Hành chính 1 · Dân sự 1 · Hình sự 1)
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/CGTVPL_07.log](evidence/CGTVPL_07.log) · [CGTVPL_07-bao-cao-so-luong-cg-tvv.pdf](evidence/CGTVPL_07-bao-cao-so-luong-cg-tvv.pdf) · [bảng điều kiện](cond/CGTVPL_07.md)
**Sheet:** tuần 3 dòng 231 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 17. ✅ DGHQHTPL_06 — BC Đánh giá hiệu quả HTPL — Xuất Excel (T3 dòng 233)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Đánh giá hiệu quả HTPL và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Đánh giá hiệu quả HTPL* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng đợt đánh giá 7 · Tổng lượt đánh giá 7 · Tổng số vụ việc đã đánh giá 5
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-danh-gia-hieu-qua-2026-08-03.xlsx (7.387 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: 7 đợt · 7 lượt · 5 vụ việc; điểm trung bình chung 7,83 đúng với 7,8 hiển thị ở bảng theo đơn vị (Cục Bổ trợ tư pháp 7,83 — 7 lượt — 5 vụ việc); có đủ bảng theo tiêu chí kèm trọng số và điểm TB

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/DGHQHTPL_06.log](evidence/DGHQHTPL_06.log) · [DGHQHTPL_06-bao-cao-danh-gia-hieu-qua.xlsx](evidence/DGHQHTPL_06-bao-cao-danh-gia-hieu-qua.xlsx) · [bảng điều kiện](cond/DGHQHTPL_06.md)
**Sheet:** tuần 3 dòng 233 → `Verify 2` = `Pass` ✅

### 18. ⚠️ DGHQHTPL_07 — BC Đánh giá hiệu quả HTPL — Xuất PDF (T3 dòng 234)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Đánh giá hiệu quả HTPL và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Đánh giá hiệu quả HTPL* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng đợt đánh giá 7 · Tổng lượt đánh giá 7 · Tổng số vụ việc đã đánh giá 5
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-danh-gia-hieu-qua-2026-08-03.pdf (27.034 bytes), 2 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC ĐÁNH GIÁ HIỆU QUẢ HTPL" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: 7 đợt · 7 lượt · 5 vụ việc; điểm trung bình chung 7,83; bảng theo đơn vị (Cục Bổ trợ tư pháp 7,83 — 7 lượt — 5 vụ việc); bảng theo tiêu chí đủ 15 dòng kèm trọng số và điểm TB, trang 2 lặp lại tiêu đề cột
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/DGHQHTPL_07.log](evidence/DGHQHTPL_07.log) · [DGHQHTPL_07-bao-cao-danh-gia-hieu-qua.pdf](evidence/DGHQHTPL_07-bao-cao-danh-gia-hieu-qua.pdf) · [bảng điều kiện](cond/DGHQHTPL_07.md)
**Sheet:** tuần 3 dòng 234 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 19. ✅ CLDTBDPL_06 — BC Chất lượng đào tạo — Xuất Excel (T3 dòng 237)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Chất lượng đào tạo và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chất lượng đào tạo* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng khóa học 5 · Tổng học viên 14 · Tỷ lệ đạt 58,0%
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-chat-luong-dao-tao-2026-08-03.xlsx (7.247 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Số liệu trong tệp khớp màn hình: 5 khóa học · 14 học viên · điểm TB chung 7,94 · tỷ lệ đạt 58%; danh sách khóa học đủ 5 dòng kèm mã khóa, tên khóa, đơn vị, số học viên, điểm TB, tỷ lệ đạt (cộng học viên 2+1+1+5+5 = 14, khớp)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CLDTBDPL_06.log](evidence/CLDTBDPL_06.log) · [CLDTBDPL_06-bao-cao-chat-luong-dao-tao.xlsx](evidence/CLDTBDPL_06-bao-cao-chat-luong-dao-tao.xlsx) · [bảng điều kiện](cond/CLDTBDPL_06.md)
**Sheet:** tuần 3 dòng 237 → `Verify 2` = `Pass` ✅

### 20. ❌ CLDTBDPL_07 — BC Chất lượng đào tạo — Xuất PDF (T3 dòng 238)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Chất lượng đào tạo và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chất lượng đào tạo* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Lỗi Forbidden KHÔNG còn tái hiện: không có thông báo "Forbidden" ở bước nào, tệp PDF vẫn tạo và tải về được
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy: bao-cao-chat-luong-dao-tao-2026-08-03.pdf (27.163 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC CHẤT LƯỢNG ĐÀO TẠO" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Các chỉ tiêu tổng trong tệp khớp màn hình: 5 khóa học · 14 học viên · điểm TB chung 7,94 · tỷ lệ đạt tổng 58%
- ❌ THIẾU DỮ LIỆU so với màn hình: bảng "Danh sách khóa học" trong tệp PDF chỉ có 5 cột (Mã khóa học · Tên khóa học · Đơn vị · Số học viên · Điểm TB), thiếu hẳn cột "Tỷ lệ đạt"
- Đối chiếu màn hình: bảng có 6 cột, cột "Tỷ lệ đạt" hiển thị đủ giá trị 5 khóa học (50% · 0% · 100% · 80% · 60%)
- Đối chiếu bản Excel cùng báo cáo (case CLDTBDPL_06): vẫn có đủ cột "Tỷ lệ đạt (%)" kèm số liệu 50/0/100/80/60 — chỉ riêng bản PDF bị thiếu cột
- Kiểm tra thêm bằng tọa độ chữ trong tệp: cột cuối cùng của bảng kết thúc ở "Điểm TB", không có chuỗi "Tỷ lệ đạt" hay các giá trị 50%/80%/100% trong bảng — cột bị thiếu thật, không phải bị che khuất ngoài lề trang
- Đã xuất lại lần 2 cùng điều kiện lọc: kết quả y hệt, vẫn thiếu cột "Tỷ lệ đạt" — lỗi tái hiện ổn định, không phải ngẫu nhiên
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

- 🔎 **Đối chiếu chéo bản dựng khác (nội bộ, 03/08 21:47):** chạy lại đúng luồng này trên bản **V1.0.5** (`cbnv_tw_01`) thì bảng "Danh sách khóa học" trong PDF **CÓ đủ cột "Tỷ lệ đạt (%)"**, 7/7 dòng, số khớp màn hình (0,0 · 66,7 · 50,0 · 66,7 · 100,0 · 0,0 · 0,0). So header 2 tệp PDF thật: V1.0.4 = 5 cột (kết thúc ở "Điểm TB") · V1.0.5 = 6 cột. ⇒ **mã nguồn đã sửa xong; môi trường đối tác đang chạy bản cũ (deploy-gap)**, không phải dev chưa làm.

**Kết luận:** Trên môi trường của vòng re-verify (V1.0.4) lỗi **vẫn tái hiện ổn định 2/2 lần** nên giữ **Reopen**; nguyên nhân đã xác định là chưa triển khai bản mới chứ không phải thiếu code → việc cần làm là **redeploy rồi retest**, không cần dev viết thêm
**Bằng chứng:** [evidence/CLDTBDPL_07.log](evidence/CLDTBDPL_07.log) · [CLDTBDPL_07-bao-cao-chat-luong-dao-tao.pdf](evidence/CLDTBDPL_07-bao-cao-chat-luong-dao-tao.pdf) (V1.0.4 — thiếu cột) · [CLDTBDPL_07-nipio-V105-co-cot-ty-le-dat.pdf](evidence/CLDTBDPL_07-nipio-V105-co-cot-ty-le-dat.pdf) (V1.0.5 — đủ cột) · [bảng điều kiện](cond/CLDTBDPL_07.md)
**Sheet:** tuần 3 dòng 238 → `Trạng thái dev fix 2` = `Reopen` · `Verify 2` = `Reopen` · `DEV phản hồi lần 2` = mô tả lỗi ❌

### 21. ✅ VVTDVQL_06 — BC Vụ việc theo đơn vị quản lý — Xuất Excel (T3 dòng 239)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc theo đơn vị quản lý và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo đơn vị quản lý* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị bảng theo đơn vị đủ 6 cột (Đơn vị · Mới · Tiếp nhận · Đang hỗ trợ · Hoàn thành · Tổng số) với 6 dòng đơn vị
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-don-vi-2026-08-03.xlsx (6.921 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 6 cột đúng như màn hình, không thiếu cột nào; 6 dòng đơn vị trùng khớp (Bộ GTVT 0/2/0/0/2 · Bộ KH&ĐT 0/0/0/0/1 · Cục Bổ trợ tư pháp 1/2/20/5/28 · An Giang 0/0/9/5/20 · Bắc Giang 0/1/1/0/2 · Bắc Ninh 0/0/1/0/1)
- Tổng số vụ việc trong tệp là 54, đúng bằng tổng cột "Tổng số" của 6 đơn vị (2+1+28+20+2+1)

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, đủ cột và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVTDVQL_06.log](evidence/VVTDVQL_06.log) · [VVTDVQL_06-bao-cao-vu-viec-theo-don-vi.xlsx](evidence/VVTDVQL_06-bao-cao-vu-viec-theo-don-vi.xlsx) · [bảng điều kiện](cond/VVTDVQL_06.md)
**Sheet:** tuần 3 dòng 239 → `Verify 2` = `Pass` ✅

### 22. ⚠️ VVTDVQL_07 — BC Vụ việc theo đơn vị quản lý — Xuất PDF (T3 dòng 240)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc theo đơn vị quản lý và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo đơn vị quản lý* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị bảng theo đơn vị đủ 6 cột (Đơn vị · Mới · Tiếp nhận · Đang hỗ trợ · Hoàn thành · Tổng số)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-don-vi-2026-08-03.pdf (24.145 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC THEO ĐƠN VỊ QUẢN LÝ" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp PDF giữ đủ 6 cột đúng như màn hình, không thiếu cột nào; 6 dòng đơn vị trùng khớp (Bộ GTVT 0/2/0/0/2 · Bộ KH&ĐT 0/0/0/0/1 · Cục Bổ trợ tư pháp 1/2/20/5/28 · An Giang 0/0/9/5/20 · Bắc Giang 0/1/1/0/2 · Bắc Ninh 0/0/1/0/1)
- Tổng số vụ việc trong tệp là 54, đúng bằng tổng cột "Tổng số" của 6 đơn vị
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVTDVQL_07.log](evidence/VVTDVQL_07.log) · [VVTDVQL_07-bao-cao-vu-viec-theo-don-vi.pdf](evidence/VVTDVQL_07-bao-cao-vu-viec-theo-don-vi.pdf) · [bảng điều kiện](cond/VVTDVQL_07.md)
**Sheet:** tuần 3 dòng 240 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 23. ✅ VVTLV_05 — BC Vụ việc theo lĩnh vực — Xuất Excel (T3 dòng 243)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc theo lĩnh vực và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo lĩnh vực* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị bảng chéo lĩnh vực x đơn vị đủ 8 cột (Lĩnh vực PL · 6 đơn vị · Tổng số)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-linh-vuc-2026-08-03.xlsx (7.150 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 8 cột đúng thứ tự như màn hình (Bắc Giang · Cục Bổ trợ tư pháp · Bộ GTVT · Bắc Ninh · An Giang · Bộ KH&ĐT · Tổng số), không thiếu cột nào
- Đủ 9 dòng lĩnh vực: Dân sự 2 · Đất đai 6 · Đầu tư 2 · Doanh nghiệp 20 · Hành chính 2 · Lao động 11 · Sở hữu trí tuệ 1 · Thuế 8 · Thương mại 1 — cộng đúng 53, khớp chỉ tiêu "Tổng số vụ việc 53"

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, đủ cột và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVTLV_05.log](evidence/VVTLV_05.log) · [VVTLV_05-bao-cao-vu-viec-theo-linh-vuc.xlsx](evidence/VVTLV_05-bao-cao-vu-viec-theo-linh-vuc.xlsx) · [bảng điều kiện](cond/VVTLV_05.md)
**Sheet:** tuần 3 dòng 243 → `Verify 2` = `Pass` ✅

### 24. ⚠️ VVTLV_06 — BC Vụ việc theo lĩnh vực — Xuất PDF (T3 dòng 244)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc theo lĩnh vực và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo lĩnh vực* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị bảng chéo lĩnh vực x đơn vị đủ 8 cột (Lĩnh vực PL · 6 đơn vị · Tổng số)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-linh-vuc-2026-08-03.pdf (24.953 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC THEO LĨNH VỰC" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp PDF giữ đủ 8 cột đúng thứ tự như màn hình (Bắc Giang · Cục Bổ trợ tư pháp · Bộ GTVT · Bắc Ninh · An Giang · Bộ KH&ĐT · Tổng số), không thiếu cột nào dù bảng khá rộng
- Đủ 9 dòng lĩnh vực: Dân sự 2 · Đất đai 6 · Đầu tư 2 · Doanh nghiệp 20 · Hành chính 2 · Lao động 11 · Sở hữu trí tuệ 1 · Thuế 8 · Thương mại 1 — cộng đúng 53, khớp chỉ tiêu "Tổng số vụ việc 53"
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVTLV_06.log](evidence/VVTLV_06.log) · [VVTLV_06-bao-cao-vu-viec-theo-linh-vuc.pdf](evidence/VVTLV_06-bao-cao-vu-viec-theo-linh-vuc.pdf) · [bảng điều kiện](cond/VVTLV_06.md)
**Sheet:** tuần 3 dòng 244 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 25. ✅ VVTLHDN_05 — BC Vụ việc theo loại hình DN — Xuất Excel (T3 dòng 246)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc theo loại hình DN và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo loại hình DN* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị bảng chéo loại hình DN x đơn vị đủ 8 cột (Loại hình DN · 6 đơn vị · Tổng số)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-loai-dn-2026-08-03.xlsx (6.912 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 8 cột đúng thứ tự như màn hình (Cục Bổ trợ tư pháp · Bộ KH&ĐT · An Giang · Bắc Giang · Bắc Ninh · Bộ GTVT · Tổng số), không thiếu cột nào
- Đủ 4 dòng dữ liệu: Nhỏ 21 · Siêu nhỏ 21 · Vừa 5 · (Không phân loại) 5 — cộng đúng 52, khớp chỉ tiêu "Tổng số vụ việc 52"
- ⚠️ Khác biệt nhỏ về nhãn (không ảnh hưởng số liệu): tiêu đề cột đầu tiên trong tệp ghi "Quy mô DN", còn trên màn hình ghi "Loại hình DN"; toàn bộ giá trị và số liệu vẫn trùng khớp

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, đủ cột và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVTLHDN_05.log](evidence/VVTLHDN_05.log) · [VVTLHDN_05-bao-cao-vu-viec-theo-loai-dn.xlsx](evidence/VVTLHDN_05-bao-cao-vu-viec-theo-loai-dn.xlsx) · [bảng điều kiện](cond/VVTLHDN_05.md)
**Sheet:** tuần 3 dòng 246 → `Verify 2` = `Pass` ✅

### 26. ⚠️ VVTLHDN_06 — BC Vụ việc theo loại hình DN — Xuất PDF (T3 dòng 247)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc theo loại hình DN và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo loại hình DN* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị bảng chéo loại hình DN x đơn vị đủ 8 cột (Loại hình DN · 6 đơn vị · Tổng số)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-loai-dn-2026-08-03.pdf (23.797 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC THEO LOẠI HÌNH DN" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp PDF giữ đủ 8 cột đúng thứ tự như màn hình (Cục Bổ trợ tư pháp · Bộ KH&ĐT · An Giang · Bắc Giang · Bắc Ninh · Bộ GTVT · Tổng số), không thiếu cột nào
- Đủ 4 dòng dữ liệu: Nhỏ 21 · Siêu nhỏ 21 · Vừa 5 · (Không phân loại) 5 — cộng đúng 52, khớp chỉ tiêu "Tổng số vụ việc 52"
- ⚠️ Khác biệt nhỏ về nhãn (không ảnh hưởng số liệu): tiêu đề cột đầu tiên trong tệp ghi "Quy mô DN", còn trên màn hình ghi "Loại hình DN"; toàn bộ giá trị và số liệu vẫn trùng khớp
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVTLHDN_06.log](evidence/VVTLHDN_06.log) · [VVTLHDN_06-bao-cao-vu-viec-theo-loai-dn.pdf](evidence/VVTLHDN_06-bao-cao-vu-viec-theo-loai-dn.pdf) · [bảng điều kiện](cond/VVTLHDN_06.md)
**Sheet:** tuần 3 dòng 247 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 27. ✅ VVTTGCT_05 — BC Vụ việc theo thời gian chi tiết — Xuất Excel (T3 dòng 248)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Vụ việc theo thời gian chi tiết và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo thời gian chi tiết* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị bảng theo kỳ đủ 6 cột (Kỳ · Mới · Tiếp nhận · Đang hỗ trợ · Hoàn thành · Tổng số), dòng dữ liệu: Năm 2026 | 1 | 5 | 30 | 10 | 53
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-tg-chi-tiet-2026-08-03.xlsx (6.634 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có cột kỳ: tệp giữ đủ 6 cột đúng như màn hình và dòng "Năm 2026 | 1 | 5 | 30 | 10 | 53" trùng khớp tuyệt đối với dòng trên màn hình
- Chỉ tiêu "Tổng số vụ việc 53" trong tệp khớp với cột Tổng số trên màn hình

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, đủ cột và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/VVTTGCT_05.log](evidence/VVTTGCT_05.log) · [VVTTGCT_05-bao-cao-vu-viec-theo-tg-chi-tiet.xlsx](evidence/VVTTGCT_05-bao-cao-vu-viec-theo-tg-chi-tiet.xlsx) · [bảng điều kiện](cond/VVTTGCT_05.md)
**Sheet:** tuần 3 dòng 248 → `Verify 2` = `Pass` ✅

### 28. ⚠️ VVTTGCT_06 — BC Vụ việc theo thời gian chi tiết — Xuất PDF (T3 dòng 249)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Vụ việc theo thời gian chi tiết và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Vụ việc theo thời gian chi tiết* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị bảng theo kỳ đủ 6 cột (Kỳ · Mới · Tiếp nhận · Đang hỗ trợ · Hoàn thành · Tổng số), dòng dữ liệu: Năm 2026 | 1 | 5 | 30 | 10 | 53
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-vu-viec-theo-tg-chi-tiet-2026-08-03.pdf (21.008 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC VỤ VIỆC THEO THỜI GIAN CHI TIẾT" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có cột kỳ: tệp giữ đủ 6 cột đúng như màn hình và dòng "Năm 2026 | 1 | 5 | 30 | 10 | 53" trùng khớp tuyệt đối với dòng trên màn hình
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/VVTTGCT_06.log](evidence/VVTTGCT_06.log) · [VVTTGCT_06-bao-cao-vu-viec-theo-tg-chi-tiet.pdf](evidence/VVTTGCT_06-bao-cao-vu-viec-theo-tg-chi-tiet.pdf) · [bảng điều kiện](cond/VVTTGCT_06.md)
**Sheet:** tuần 3 dòng 249 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 29. ✅ CPHTCT_06 — BC Chi phí chi trả hỗ trợ — Xuất Excel (T3 dòng 250)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Chi phí chi trả hỗ trợ và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí chi trả hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng chi phí 226.308.268 ₫ · Tổng hồ sơ 25 · Trung bình/hồ sơ 9.052.331 ₫
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-chi-phi-chi-tra-2026-08-03.xlsx (7.310 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Ba chỉ tiêu tổng trong tệp khớp màn hình: 25 hồ sơ · 226.308.268 ₫ · 9.052.331 ₫/hồ sơ
- Bảng theo đơn vị đủ 4 cột và đủ 7 dòng trùng khớp màn hình (Bắc Giang 6/103.417.226 · An Giang 9/36.269.068 · Bộ KH&ĐT 2/34.666.619 · Cục Bổ trợ tư pháp 3/15.802.407 · Bắc Ninh 3/15.283.887 · Bộ Tài chính 1/12.622.206 · Bộ Công Thương 1/8.246.855) — cộng đúng 25 hồ sơ và 226.308.268 ₫
- Tệp còn có thêm bảng "Theo quy mô doanh nghiệp" kèm trần chi phí và chênh lệch (Nhỏ · Siêu nhỏ · Vừa) — dữ liệu đầy đủ, không thiếu mục nào

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CPHTCT_06.log](evidence/CPHTCT_06.log) · [CPHTCT_06-bao-cao-chi-phi-chi-tra.xlsx](evidence/CPHTCT_06-bao-cao-chi-phi-chi-tra.xlsx) · [bảng điều kiện](cond/CPHTCT_06.md)
**Sheet:** tuần 3 dòng 250 → `Verify 2` = `Pass` ✅

### 30. ⚠️ CPHTCT_07 — BC Chi phí chi trả hỗ trợ — Xuất PDF (T3 dòng 251)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Chi phí chi trả hỗ trợ và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí chi trả hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng chi phí 226.308.268 ₫ · Tổng hồ sơ 25 · Trung bình/hồ sơ 9.052.331 ₫
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-chi-phi-chi-tra-2026-08-03.pdf (26.817 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC CHI PHÍ CHI TRẢ HỖ TRỢ" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Ba chỉ tiêu tổng trong tệp khớp màn hình: 25 hồ sơ · 226.308.268 ₫ · 9.052.331 ₫/hồ sơ
- Bảng theo đơn vị đủ 4 cột và đủ 7 dòng trùng khớp màn hình (Bắc Giang 6/103.417.226 · An Giang 9/36.269.068 · Bộ KH&ĐT 2/34.666.619 · Cục Bổ trợ tư pháp 3/15.802.407 · Bắc Ninh 3/15.283.887 · Bộ Tài chính 1/12.622.206 · Bộ Công Thương 1/8.246.855) — cộng đúng 25 hồ sơ và 226.308.268 ₫
- Tệp còn có đủ bảng "Theo quy mô doanh nghiệp" 5 cột kèm trần chi phí và chênh lệch (Nhỏ · Siêu nhỏ · Vừa)
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/CPHTCT_07.log](evidence/CPHTCT_07.log) · [CPHTCT_07-bao-cao-chi-phi-chi-tra.pdf](evidence/CPHTCT_07-bao-cao-chi-phi-chi-tra.pdf) · [bảng điều kiện](cond/CPHTCT_07.md)
**Sheet:** tuần 3 dòng 251 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 31. ✅ CPCTHTTDVQL_06 — BC Chi phí theo đơn vị — Xuất Excel (T3 dòng 253)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp Excel báo cáo Chi phí theo đơn vị và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo đơn vị* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng hồ sơ 25 · Tổng chi phí 226.308.268 ₫
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-chi-phi-theo-don-vi-2026-08-03.xlsx (7.002 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 4 cột như màn hình và đủ 7 dòng đơn vị trùng khớp (Bắc Giang 6/103.417.226 · An Giang 9/36.269.068 · Bộ KH&ĐT 2/34.666.619 · Cục Bổ trợ tư pháp 3/15.802.407 · Bắc Ninh 3/15.283.887 · Bộ Tài chính 1/12.622.206 · Bộ Công Thương 1/8.246.855)
- Cộng kiểm tra: 7 dòng cộng đúng 25 hồ sơ và 226.308.268 ₫, khớp hai chỉ tiêu tổng

**Kết luận:** Không tái hiện lỗi Forbidden. Xem báo cáo và Xuất Excel đều chạy được, tệp tải về đủ đầu đề, đủ cột và số liệu khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CPCTHTTDVQL_06.log](evidence/CPCTHTTDVQL_06.log) · [CPCTHTTDVQL_06-bao-cao-chi-phi-theo-don-vi.xlsx](evidence/CPCTHTTDVQL_06-bao-cao-chi-phi-theo-don-vi.xlsx) · [bảng điều kiện](cond/CPCTHTTDVQL_06.md)
**Sheet:** tuần 3 dòng 253 → `Verify 2` = `Pass` ✅

### 32. ⚠️ CPCTHTTDVQL_07 — BC Chi phí theo đơn vị — Xuất PDF (T3 dòng 254)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Chi phí theo đơn vị và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo đơn vị* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Màn hình hiển thị số liệu thật: Tổng hồ sơ 25 · Tổng chi phí 226.308.268 ₫
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy thành công: bao-cao-chi-phi-theo-don-vi-2026-08-03.pdf (23.905 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Nội dung tệp đủ 4 dòng đầu đề: "BC CHI PHÍ THEO ĐƠN VỊ" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp PDF giữ đủ 4 cột như màn hình và đủ 7 dòng đơn vị trùng khớp (Bắc Giang 6/103.417.226 · An Giang 9/36.269.068 · Bộ KH&ĐT 2/34.666.619 · Cục Bổ trợ tư pháp 3/15.802.407 · Bắc Ninh 3/15.283.887 · Bộ Tài chính 1/12.622.206 · Bộ Công Thương 1/8.246.855)
- Cộng kiểm tra: 7 dòng cộng đúng 25 hồ sơ và 226.308.268 ₫, khớp hai chỉ tiêu tổng
- ⚠️ Tồn tại đã ghi nhận từ vòng 1 (không tính lỗi mới): tệp PDF chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký và chức danh người ký ở cuối trang; tên tệp là bao-cao-<tên>-YYYY-MM-DD.pdf

**Kết luận:** Lỗi Forbidden đã hết và số liệu trong tệp khớp màn hình; phần trình bày (quốc hiệu, khối ký) đang vướng mâu thuẫn trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/CPCTHTTDVQL_07.log](evidence/CPCTHTTDVQL_07.log) · [CPCTHTTDVQL_07-bao-cao-chi-phi-theo-don-vi.pdf](evidence/CPCTHTTDVQL_07-bao-cao-chi-phi-theo-don-vi.pdf) · [bảng điều kiện](cond/CPCTHTTDVQL_07.md)
**Sheet:** tuần 3 dòng 254 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 33. ✅ CPCTHTTLHDN_06 — BC Chi phí theo loại hình DN — Xuất Excel (T3 dòng 257)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Chi phí theo loại hình DN ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo loại hình DN* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng hồ sơ 25 · Tổng chi phí 226.308.268 ₫
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-chi-phi-theo-loai-dn-2026-08-03.xlsx (6.923 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 7 cột như màn hình (Quy mô DN · Số hồ sơ · Tổng chi phí · Mức hỗ trợ % · Trần/hồ sơ · Trần chi phí · Chênh lệch), không thiếu cột nào
- Đủ 3 dòng dữ liệu trùng khớp màn hình: Nhỏ 11/118.156.629/30% · Siêu nhỏ 8/67.525.761/100% · Vừa 6/40.625.878/10% — cộng đúng 25 hồ sơ và 226.308.268 ₫

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CPCTHTTLHDN_06.log](evidence/CPCTHTTLHDN_06.log) · [CPCTHTTLHDN_06-bao-cao-chi-phi-theo-loai-dn.xlsx](evidence/CPCTHTTLHDN_06-bao-cao-chi-phi-theo-loai-dn.xlsx) · [bảng điều kiện](cond/CPCTHTTLHDN_06.md)
**Sheet:** tuần 3 dòng 257 → `Verify 2` = `Pass` ✅

### 34. ⚠️ CPCTHTTLHDN_07 — BC Chi phí theo loại hình DN — Xuất PDF (T3 dòng 258)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Chi phí theo loại hình DN và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo loại hình DN* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Lỗi Forbidden KHÔNG còn tái hiện: không có thông báo "Forbidden" ở bước nào, tệp PDF tạo và tải về máy bình thường
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy: bao-cao-chi-phi-theo-loai-dn-2026-08-03.pdf (23.838 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Phông chữ nhúng trong tệp là Tinos (bộ phông cùng hệ đo với Times New Roman), đúng yêu cầu phông của đặc tả
- Đầu tệp đủ 4 dòng: "BC CHI PHÍ THEO LOẠI HÌNH DN" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: tệp giữ đủ 7 cột như màn hình (Quy mô DN · Số hồ sơ · Tổng chi phí · Mức hỗ trợ % · Trần/hồ sơ · Trần chi phí · Chênh lệch), không thiếu cột nào
- Đủ 3 dòng dữ liệu trùng khớp màn hình: Nhỏ 11/118.156.629/30% · Siêu nhỏ 8/67.525.761/100% · Vừa 6/40.625.878/10% — cộng đúng 25 hồ sơ và 226.308.268 ₫
- Điểm còn lệch so với "Kết quả mong đợi" của phiếu: tệp chưa có quốc hiệu và tên cơ quan đầu trang, chưa có ngày ký và chức danh người ký cuối trang; tên tệp theo dạng bao-cao-<tên>-YYYY-MM-DD.pdf
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn (vừa buộc theo Thông tư 17/2025 vừa mô tả đầu tệp chỉ gồm tên BC/kỳ/đơn vị/ngày tạo, và chính đặc tả ghi chú phần trích dẫn Thông tư chưa tra cứu lại) — chuyển BA chốt

**Kết luận:** Lỗi Forbidden đã hết và nội dung số liệu khớp màn hình; phần trình bày theo khung văn bản hành chính và quy ước tên tệp chưa có trong đặc tả nên chuyển BA xác nhận → **BA confirm**
**Bằng chứng:** [evidence/CPCTHTTLHDN_07.log](evidence/CPCTHTTLHDN_07.log) · [CPCTHTTLHDN_07-bao-cao-chi-phi-theo-loai-dn.pdf](evidence/CPCTHTTLHDN_07-bao-cao-chi-phi-theo-loai-dn.pdf) · [bảng điều kiện](cond/CPCTHTTLHDN_07.md)
**Sheet:** tuần 3 dòng 258 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 35. ✅ CPCTHTTTG_05 — BC Chi phí theo thời gian — Xuất Excel (T3 dòng 260)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Chi phí theo thời gian ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng chi phí toàn kỳ 226.308.268 ₫ · Tổng hồ sơ toàn kỳ 25
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-chi-phi-theo-thoi-gian-2026-08-03.xlsx (6.663 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có đủ cột kỳ: bảng "Theo kỳ" gồm Kỳ / Từ ngày / Đến ngày / Số hồ sơ / Tổng chi phí — dòng "Năm 2026 | 01/01/2026 | 31/12/2026 | 25 | 226.308.268" trùng khớp tuyệt đối dòng trên màn hình
- Hai chỉ tiêu tổng trong tệp khớp màn hình: 226.308.268 ₫ và 25 hồ sơ

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CPCTHTTTG_05.log](evidence/CPCTHTTTG_05.log) · [CPCTHTTTG_05-bao-cao-chi-phi-theo-thoi-gian.xlsx](evidence/CPCTHTTTG_05-bao-cao-chi-phi-theo-thoi-gian.xlsx) · [bảng điều kiện](cond/CPCTHTTTG_05.md)
**Sheet:** tuần 3 dòng 260 → `Verify 2` = `Pass` ✅

### 36. ⚠️ CPCTHTTTG_06 — BC Chi phí theo thời gian — Xuất PDF (T3 dòng 261)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất được tệp PDF báo cáo Chi phí theo thời gian và tải về máy, nội dung khớp số liệu trên màn hình

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chi phí theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → hộp thoại Tùy chọn in giữ mặc định A4/Dọc → [Xuất file]

**Quan sát:**
- Lỗi Forbidden KHÔNG còn tái hiện: không có thông báo "Forbidden" ở bước nào, tệp PDF tạo và tải về máy bình thường
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tải về máy: bao-cao-chi-phi-theo-thoi-gian-2026-08-03.pdf (21.570 bytes), 1 trang, khổ giấy 595x842 pt đúng A4 dọc
- Phông chữ nhúng trong tệp là Tinos (bộ phông cùng hệ đo với Times New Roman)
- Đầu tệp đủ 4 dòng: "BC CHI PHÍ THEO THỜI GIAN" · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Báo cáo theo thời gian có đủ cột kỳ: bảng "Theo kỳ" gồm Kỳ / Từ ngày / Đến ngày / Số hồ sơ / Tổng chi phí — dòng "Năm 2026 | 01/01/2026 | 31/12/2026 | 25 | 226.308.268" trùng khớp tuyệt đối dòng trên màn hình
- Hai chỉ tiêu tổng trong tệp khớp màn hình: 226.308.268 ₫ và 25 hồ sơ
- Điểm còn lệch so với "Kết quả mong đợi" của phiếu: tệp chưa có quốc hiệu và tên cơ quan đầu trang, chưa có ngày ký và chức danh người ký cuối trang; tên tệp theo dạng bao-cao-<tên>-YYYY-MM-DD.pdf
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn (vừa buộc theo Thông tư 17/2025 vừa mô tả đầu tệp chỉ gồm tên BC/kỳ/đơn vị/ngày tạo, và chính đặc tả ghi chú phần trích dẫn Thông tư chưa tra cứu lại) — chuyển BA chốt

**Kết luận:** Lỗi Forbidden đã hết và nội dung số liệu khớp màn hình; phần trình bày theo khung văn bản hành chính và quy ước tên tệp đang vướng mâu thuẫn trong đặc tả nên chuyển BA chốt → **BA confirm**
**Bằng chứng:** [evidence/CPCTHTTTG_06.log](evidence/CPCTHTTTG_06.log) · [CPCTHTTTG_06-bao-cao-chi-phi-theo-thoi-gian.pdf](evidence/CPCTHTTTG_06-bao-cao-chi-phi-theo-thoi-gian.pdf) · [bảng điều kiện](cond/CPCTHTTTG_06.md)
**Sheet:** tuần 3 dòng 261 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 37. ✅ SLCTHT_06 — BC Số lượng chương trình hỗ trợ — Xuất Excel (T3 dòng 264)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Số lượng chương trình hỗ trợ ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Số lượng chương trình hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: Tổng chương trình 5; bảng theo đơn vị 3 dòng (Cục Bổ trợ tư pháp 3 · Bộ KH&ĐT 1 · An Giang 1)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-so-luong-ct-ho-tro-2026-08-03.xlsx (7.034 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng theo đơn vị trong tệp giữ đủ 4 cột như màn hình và 3 dòng trùng khớp (Cục Bổ trợ tư pháp 3/2/1 · Bộ KH&ĐT 1/1/0 · An Giang 1/1/0) — cộng đúng 5 chương trình
- Tệp còn có đủ các mục: Tổng số chương trình 5 · Đang thực hiện 4 · Hoàn thành 1 · bảng Theo trạng thái · bảng Theo kỳ (Năm 2026 | 01/01/2026 | 31/12/2026 | 5)

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/SLCTHT_06.log](evidence/SLCTHT_06.log) · [SLCTHT_06-bao-cao-so-luong-ct-ho-tro.xlsx](evidence/SLCTHT_06-bao-cao-so-luong-ct-ho-tro.xlsx) · [bảng điều kiện](cond/SLCTHT_06.md)
**Sheet:** tuần 3 dòng 264 → `Verify 2` = `Pass` ✅

### 38. ⚠️ SLCTHT_07 — BC Số lượng chương trình hỗ trợ — Xuất PDF (T3 dòng 265)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất báo cáo ra tệp PDF đúng định dạng văn bản hành chính và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Số lượng chương trình hỗ trợ* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-so-luong-ct-ho-tro-2026-08-03.pdf (24.169 bytes, 1 trang)
- Khổ giấy đúng A4 (595 x 842 pt); phông chữ nhúng trong tệp là Tinos (bộ phông tương đương Times New Roman)
- Đầu tệp có 4 dòng: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo đơn vị" trong tệp giữ đủ 4 cột như màn hình và 3 dòng trùng khớp (Cục Bổ trợ tư pháp 3/2/1 · Bộ KH&ĐT 1/1/0 · An Giang 1/1/0)
- Tệp còn đủ các mục: Tổng số chương trình 5 · Đang thực hiện 4 · Hoàn thành 1 · bảng Theo trạng thái · bảng Theo kỳ (Năm 2026 | 01/01/2026 | 31/12/2026 | 5)
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn — chuyển BA chốt: tệp chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký + chức danh người ký ở cuối trang; tên tệp theo dạng bao-cao-<slug>-YYYY-MM-DD.pdf

**Kết luận:** Không tái hiện lỗi Forbidden; xuất PDF và tải tệp thành công, nội dung khớp màn hình. Phần trình bày văn bản hành chính đang mâu thuẫn trong đặc tả — chuyển BA chốt → **BA confirm**
**Bằng chứng:** [evidence/SLCTHT_07.log](evidence/SLCTHT_07.log) · [SLCTHT_07-bao-cao-so-luong-ct-ho-tro.pdf](evidence/SLCTHT_07-bao-cao-so-luong-ct-ho-tro.pdf) · [bảng điều kiện](cond/SLCTHT_07.md)
**Sheet:** tuần 3 dòng 265 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 39. ✅ CTTDVQL_04 — BC Chương trình theo đơn vị — Xuất Excel (T3 dòng 268)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Chương trình theo đơn vị ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo đơn vị* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: bảng theo đơn vị 4 cột, 3 dòng (Cục Bổ trợ tư pháp TW 3 · 100.000.000 ₫; Bộ KH&ĐT BN 1 · 0 ₫; Sở Tư pháp An Giang DP 1 · 0 ₫)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-don-vi-2026-08-03.xlsx (6.797 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo đơn vị" trong tệp giữ đủ 4 cột như màn hình (Đơn vị · Cấp đơn vị · Số chương trình · Tổng ngân sách) và 3 dòng số liệu trùng khớp
- Tệp còn có các mục: Tổng số chương trình 5 · Tổng ngân sách 100.000.000 ₫ — cộng đúng theo bảng chi tiết

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CTTDVQL_04.log](evidence/CTTDVQL_04.log) · [CTTDVQL_04-bao-cao-ct-theo-don-vi.xlsx](evidence/CTTDVQL_04-bao-cao-ct-theo-don-vi.xlsx) · [bảng điều kiện](cond/CTTDVQL_04.md)
**Sheet:** tuần 3 dòng 268 → `Verify 2` = `Pass` ✅

### 40. ⚠️ CTTDVQL_05 — BC Chương trình theo đơn vị — Xuất PDF (T3 dòng 269)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất báo cáo ra tệp PDF đúng định dạng văn bản hành chính và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo đơn vị* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-don-vi-2026-08-03.pdf (23.455 bytes, 1 trang)
- Khổ giấy đúng A4 (595 x 842 pt); phông chữ nhúng trong tệp là Tinos (bộ phông tương đương Times New Roman)
- Đầu tệp có 4 dòng: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo đơn vị" trong tệp giữ đủ 4 cột như màn hình (Đơn vị · Cấp đơn vị · Số chương trình · Tổng ngân sách) và 3 dòng trùng khớp (Cục Bổ trợ tư pháp TW 3 · 100.000.000; Bộ KH&ĐT BN 1 · 0; An Giang DP 1 · 0)
- Tệp còn đủ các mục: Tổng số chương trình 5 · Tổng ngân sách 100.000.000 ₫
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn — chuyển BA chốt: tệp chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký + chức danh người ký ở cuối trang; tên tệp theo dạng bao-cao-<slug>-YYYY-MM-DD.pdf

**Kết luận:** Không tái hiện lỗi Forbidden; xuất PDF và tải tệp thành công, nội dung khớp màn hình. Phần trình bày văn bản hành chính đang mâu thuẫn trong đặc tả — chuyển BA chốt → **BA confirm**
**Bằng chứng:** [evidence/CTTDVQL_05.log](evidence/CTTDVQL_05.log) · [CTTDVQL_05-bao-cao-ct-theo-don-vi.pdf](evidence/CTTDVQL_05-bao-cao-ct-theo-don-vi.pdf) · [bảng điều kiện](cond/CTTDVQL_05.md)
**Sheet:** tuần 3 dòng 269 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 41. ✅ CTTLV_05 — BC Chương trình theo lĩnh vực — Xuất Excel (T3 dòng 273)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Chương trình theo lĩnh vực ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo lĩnh vực* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: bảng theo lĩnh vực 2 cột, 2 dòng (Chưa phân loại 4 · Đất đai 1)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-linh-vuc-2026-08-03.xlsx (6.606 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo lĩnh vực pháp luật" trong tệp giữ đủ 2 cột như màn hình và 2 dòng số liệu trùng khớp (Chưa phân loại 4 · Đất đai 1)
- Tệp có mục Tổng số chương trình 5 — cộng đúng theo bảng chi tiết (4 + 1)

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CTTLV_05.log](evidence/CTTLV_05.log) · [CTTLV_05-bao-cao-ct-theo-linh-vuc.xlsx](evidence/CTTLV_05-bao-cao-ct-theo-linh-vuc.xlsx) · [bảng điều kiện](cond/CTTLV_05.md)
**Sheet:** tuần 3 dòng 273 → `Verify 2` = `Pass` ✅

### 42. ⚠️ CTTLV_06 — BC Chương trình theo lĩnh vực — Xuất PDF (T3 dòng 274)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất báo cáo ra tệp PDF đúng định dạng văn bản hành chính và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo lĩnh vực* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-linh-vuc-2026-08-03.pdf (21.054 bytes, 1 trang)
- Khổ giấy đúng A4 (595 x 842 pt); phông chữ nhúng trong tệp là Tinos (bộ phông tương đương Times New Roman)
- Đầu tệp có 4 dòng: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo lĩnh vực pháp luật" trong tệp giữ đủ 2 cột như màn hình và 2 dòng trùng khớp (Chưa phân loại 4 · Đất đai 1)
- Tệp có mục Tổng số chương trình 5 — cộng đúng theo bảng chi tiết (4 + 1)
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn — chuyển BA chốt: tệp chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký + chức danh người ký ở cuối trang; tên tệp theo dạng bao-cao-<slug>-YYYY-MM-DD.pdf

**Kết luận:** Không tái hiện lỗi Forbidden; xuất PDF và tải tệp thành công, nội dung khớp màn hình. Phần trình bày văn bản hành chính đang mâu thuẫn trong đặc tả — chuyển BA chốt → **BA confirm**
**Bằng chứng:** [evidence/CTTLV_06.log](evidence/CTTLV_06.log) · [CTTLV_06-bao-cao-ct-theo-linh-vuc.pdf](evidence/CTTLV_06-bao-cao-ct-theo-linh-vuc.pdf) · [bảng điều kiện](cond/CTTLV_06.md)
**Sheet:** tuần 3 dòng 274 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 43. ✅ CTTTG_04 — BC Chương trình theo thời gian — Xuất Excel (T3 dòng 275)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất toàn bộ báo cáo Chương trình theo thời gian ra tệp Excel và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất Excel]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo và Xuất Excel)
- Màn hình hiển thị số liệu thật: bảng theo kỳ 6 cột, 1 dòng (Năm 2026 | 01/01/2026 | 31/12/2026 | 1 | 0 | 0 ₫)
- Thông báo duy nhất khi bấm Xuất Excel là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-thoi-gian-2026-08-03.xlsx (6.752 bytes)
- Nội dung tệp đủ 4 dòng đầu đề: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo kỳ" trong tệp giữ đủ 6 cột như màn hình (Kỳ · Từ ngày · Đến ngày · Số chương trình · Số DN · Tổng ngân sách) và dòng số liệu trùng khớp
- Tệp còn đủ 3 mục tổng: Tổng số chương trình toàn kỳ 1 · Tổng số DN toàn kỳ 0 · Tổng ngân sách toàn kỳ 0 ₫

**Kết luận:** Không tái hiện lỗi Forbidden. Hệ thống xuất toàn bộ báo cáo ra Excel và tự tải tệp về máy, nội dung khớp màn hình → **Pass**
**Bằng chứng:** [evidence/CTTTG_04.log](evidence/CTTTG_04.log) · [CTTTG_04-bao-cao-ct-theo-thoi-gian.xlsx](evidence/CTTTG_04-bao-cao-ct-theo-thoi-gian.xlsx) · [bảng điều kiện](cond/CTTTG_04.md)
**Sheet:** tuần 3 dòng 275 → `Verify 2` = `Pass` ✅

### 44. ⚠️ CTTTG_05 — BC Chương trình theo thời gian — Xuất PDF (T3 dòng 276)

**Claim vòng 2 (TKM):** TKM retest 31/7: Hệ thống hiển thị thông báo "Forbidden"
**KQ mong đợi:** Hệ thống xuất báo cáo ra tệp PDF đúng định dạng văn bản hành chính và tự động tải tệp về máy

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = *BC Chương trình theo thời gian* → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → [Xuất PDF] → [Xuất file]

**Quan sát:**
- Không tái hiện: không xuất hiện thông báo "Forbidden" ở bất kỳ bước nào (Xem báo cáo, Xuất PDF, Xuất file)
- Thông báo duy nhất khi xuất là "Đang tạo file..."; không có thông báo lỗi nào
- Tệp tự động tải về máy thành công: bao-cao-ct-theo-thoi-gian-2026-08-03.pdf (22.075 bytes, 1 trang)
- Khổ giấy đúng A4 (595 x 842 pt); phông chữ nhúng trong tệp là Tinos (bộ phông tương đương Times New Roman)
- Đầu tệp có 4 dòng: tên báo cáo · "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · "Đơn vị: Toàn quốc" · "Ngày tạo: 03/08/2026"
- Đối chiếu từng cột: bảng "Theo kỳ" trong tệp giữ đủ 6 cột như màn hình (Kỳ · Từ ngày · Đến ngày · Số chương trình · Số DN · Tổng ngân sách) và dòng số liệu trùng khớp (Năm 2026 | 01/01/2026 | 31/12/2026 | 1 | 0 | 0)
- Tệp còn đủ 3 mục tổng: Tổng số chương trình toàn kỳ 1 · Tổng số DN toàn kỳ 0 · Tổng ngân sách toàn kỳ 0 ₫
- Lệch so với KQ mong đợi, đặc tả đang mâu thuẫn — chuyển BA chốt: tệp chưa có quốc hiệu/tên cơ quan ở đầu trang, chưa có ngày ký + chức danh người ký ở cuối trang; tên tệp theo dạng bao-cao-<slug>-YYYY-MM-DD.pdf

**Kết luận:** Không tái hiện lỗi Forbidden; xuất PDF và tải tệp thành công, nội dung khớp màn hình. Phần trình bày văn bản hành chính đang mâu thuẫn trong đặc tả — chuyển BA chốt → **BA confirm**
**Bằng chứng:** [evidence/CTTTG_05.log](evidence/CTTTG_05.log) · [CTTTG_05-bao-cao-ct-theo-thoi-gian.pdf](evidence/CTTTG_05-bao-cao-ct-theo-thoi-gian.pdf) · [bảng điều kiện](cond/CTTTG_05.md)
**Sheet:** tuần 3 dòng 276 → `Verify 2` = `BA confirm` · `DEV phản hồi lần 2` = câu hỏi gửi BA (KHÔNG đụng `Trạng thái dev fix 2`) ⚠️

### 45. ✅ VVDTN_04 — BC Vụ việc đã tiếp nhận — thống kê theo lĩnh vực (T3 dòng 195)

**Claim vòng 2 (TKM):** TKM retest 31/7: Không hiển thị biểu đồ tròn theo lĩnh vực (VVDTN_04_v2.jpg)
**KQ mong đợi:** Báo cáo hiển thị đủ mục thống kê theo lĩnh vực pháp luật (bug gốc: thiếu hẳn cả bảng lẫn biểu đồ theo lĩnh vực)

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Báo cáo thống kê → Loại BC = BC Vụ việc đã tiếp nhận → Kỳ = Năm (01/01–31/12/2026) → Đơn vị = Toàn quốc → [Xem báo cáo] → đọc toàn bộ khối tiêu đề, bảng và biểu đồ trên trang

**Quan sát:**
- Mục "Thống kê theo lĩnh vực pháp luật" ĐÃ hiển thị — bug gốc (thiếu hẳn phần theo lĩnh vực) không còn tái hiện
- Bảng "Lĩnh vực PL | Số lượng | Tỷ lệ" đủ 9 dòng: Doanh nghiệp 20 (40%) · Lao động 11 (22%) · Thuế 7 (14%) · Đất đai 4 (8%) · Dân sự 2 · Hành chính 2 · Đầu tư 2 · Thương mại 1 · Sở hữu trí tuệ 1
- Cộng bảng lĩnh vực = 50, khớp chỉ tiêu "Tổng vụ việc 50"; bảng Kênh tiếp nhận (38+6+2+2+1+1) và bảng Đơn vị (26+20+2+1+1) cũng cộng đúng 50
- Biểu đồ trên trang: 1 biểu đồ cột (6 cột) + 1 biểu đồ đường xu hướng; đếm bằng recharts cho kết quả pie=0 trên toàn trang
- Yêu cầu "biểu đồ tròn" nằm ngoài đặc tả UC125: srs-fr-11-bao-cao.md:1065 bảng mapping 23 loại BC ghi UC125 "BC Vụ việc đã tiếp nhận" → Biểu đồ = "Bar + Trend". Donut thuộc UC124 (Hỏi đáp) và UC127 (Vụ việc đã hoàn thành)
- FR-IX-02 §Output đặc thù chỉ yêu cầu theo_linh_vuc[] dạng structured "Luôn" — không quy định phải render bằng biểu đồ tròn; AC ghi "hiển thị tổng VV tiếp nhận, phân theo kênh + lĩnh vực"

**Kết luận:** Bug gốc (thiếu mục theo lĩnh vực) đã được sửa, số liệu khớp chỉ tiêu. Yêu cầu biểu đồ tròn vượt ngoài đặc tả UC125 (Bar + Trend) và đặc tả điểm này rõ ràng, không mâu thuẫn nên không cần BA → **Pass**
**Bằng chứng:** [evidence/VVDTN_04.log](evidence/VVDTN_04.log) · [bảng điều kiện](cond/VVDTN_04.md)
**Sheet:** tuần 3 dòng 195 → `Verify 2` = `Pass` ✅

### 46. ❌ TKTMBMHD_07 — Thư mục biểu mẫu — nút "Xóa bộ lọc" (T3 dòng 91)

**Claim vòng 2 (TKM):** Hệ thống không trả về danh sách mặc định (TKTMBMHD_07_v2.webm)
**KQ mong đợi:** Xóa toàn bộ giá trị lọc + đưa tab về "Tất cả" + hiển thị lại danh sách mặc định (toàn bộ thư mục trong phạm vi phân quyền)

**Luồng đã chạy lại:** Đăng nhập cbnv_tw → Thư viện biểu mẫu (/bieu-mau/thu-muc) → ghi nhận mặc định → gõ từ khóa + chọn Lĩnh vực + chọn Trạng thái + chuyển tab "Nháp" → [Tìm kiếm] → [Xóa bộ lọc] → đọc lại tab / ô lọc / URL / tổng số bản ghi. Lặp lần 2 chỉ với từ khóa "test", rồi bấm thêm [Làm mới]

**Quan sát:**
- Mặc định ban đầu: tab "Tất cả23", "Hiển thị 1-20 / 23 kết quả", mọi ô lọc trống
- ĐÃ SỬA — sau [Xóa bộ lọc] tab tự về "Tất cả" (trước đó đang đứng ở "Nháp"); ô tìm kiếm, 2 ô chọn và 2 ô ngày đều trắng. Đây là ý đối tác nêu ở vòng 1
- CÒN LỖI — danh sách không về mặc định: lần 1 (từ khóa "a" + lĩnh vực Thuế) sau khi xóa còn "1-2 / 2 kết quả", tab hiển thị "Tất cả2"; URL vẫn giữ ?keyword=a&linhVucId=bbbbbbbb-0000-4000-8000-000000000018
- Lần 2 (chỉ từ khóa "test"): sau [Xóa bộ lọc] vẫn "1-9 / 9 kết quả", tab "Tất cả9", URL vẫn ?keyword=test&page=1 — tái hiện 2/2 lần
- Bấm thêm [Làm mới] cũng không đưa về mặc định: vẫn 9 kết quả, URL vẫn giữ keyword=test
- Đặc tả: srs-fr-09-bieu-mau.md:622 (SCR-VII-01 #7) — "click → xóa từ khóa + mọi trường lọc (lĩnh vực, trạng thái, khoảng ngày) + đưa tab về Tất cả + về sắp xếp mặc định"

**Kết luận:** Fix một phần: tab và các ô lọc đã reset đúng, nhưng truy vấn vẫn giữ từ khóa/lĩnh vực cũ nên danh sách không trở về mặc định — đúng như claim vòng 2 → **Reopen**
**Bằng chứng:** [evidence/TKTMBMHD_07.log](evidence/TKTMBMHD_07.log) · [bảng điều kiện](cond/TKTMBMHD_07.md)
**Sheet:** tuần 3 dòng 91 → `Trạng thái dev fix 2` = `Reopen` · `Verify 2` = `Reopen` · `DEV phản hồi lần 2` = mô tả lỗi ❌

### 47. ✅ QLCHTHXLHS_02 — Cấu hình hệ thống — số thẻ trên màn hình (T3 dòng 152)

**Claim vòng 2 (TKM):** TKM retest 31/7: Lỗi chưa được fix (đối tác chờ 4 thẻ: SLA, Phân công mặc định, Mẫu phản hồi, Quy trình hỗ trợ)
**KQ mong đợi:** Màn Cấu hình hệ thống hiển thị đúng bộ thẻ theo đặc tả, mỗi thẻ mở ra nội dung tương ứng

**Luồng đã chạy lại:** Đăng nhập admin (QTHT) → Quản trị hệ thống → Cấu hình hệ thống (/quan-tri/cau-hinh) → đếm và đọc tên từng thẻ → bấm lần lượt cả 3 thẻ, đọc nội dung từng thẻ

**Quan sát:**
- Màn hình hiển thị đúng 3 thẻ: "Thời hạn xử lý (SLA)" · "Mẫu phản hồi" · "Quản lý ngày lễ"
- Bấm từng thẻ đều mở ra nội dung thật, không phải thẻ rỗng: SLA có bảng 10 cột × 6 dòng loại yêu cầu; Mẫu phản hồi có bảng 9 cột × 15 dòng; Quản lý ngày lễ có bảng 6 cột × 7 dòng (dòng đầu 01/01/2026 Tết Dương lịch)
- Đặc tả khớp: srs-fr-10-quan-tri.md:1803 — "Tab navigation (3 tabs) | Tab 1: Thời hạn xử lý / SLA — Tab 2: Mẫu phản hồi — Tab 3: Quản lý ngày lễ (FR-VIII-29)"
- Hai thẻ đối tác mong đợi đã được bỏ có căn cứ: srs-fr-10-quan-tri.md:1788 — "Đã bỏ: Tab 4 Quy trình hỗ trợ (BA chốt 2026-05-07 Hướng A); Tab 2 Phân công mặc định (BA chốt 2026-05-07 Q11)"; nhật ký thay đổi dòng :20 ghi cùng quyết định

**Kết luận:** Phần mềm khớp đúng đặc tả hiện hành (3 thẻ, mỗi thẻ có nội dung). Kỳ vọng 4 thẻ dựa trên bản thiết kế cũ đã được BA bỏ từ 07/05/2026 — đặc tả điểm này rõ ràng, có ngày BA chốt, không mâu thuẫn nên không cần BA xác nhận lại → **Pass**
**Bằng chứng:** [evidence/QLCHTHXLHS_02.log](evidence/QLCHTHXLHS_02.log) · [bảng điều kiện](cond/QLCHTHXLHS_02.md)
**Sheet:** tuần 3 dòng 152 → `Verify 2` = `Pass` ✅

### 48. ✅ QLCHTHXLHS_03 — Cấu hình hệ thống — bảng cấu hình SLA (T3 dòng 153)

**Claim vòng 2 (TKM):** TKM retest 31/7: (a) SRS có 2 cột riêng Cảnh báo mức 1 và mức 2 nhưng hệ thống gộp thành "Vùng cảnh báo" · (b) Thiếu cột Quá hạn (%) · (c) Loại yêu cầu tràn dữ liệu sang cột Tên loại (QLCHTHXLHS_03_v2.png)
**KQ mong đợi:** Bảng cấu hình SLA hiển thị đúng bộ cột theo đặc tả, dữ liệu không tràn/đè lên nhau

**Luồng đã chạy lại:** Đăng nhập admin (QTHT) → Cấu hình hệ thống → thẻ "Thời hạn xử lý (SLA)" → đọc toàn bộ tiêu đề cột + 6 dòng dữ liệu → đo scrollWidth/clientWidth của từng ô cột "Loại yêu cầu" và "Tên loại" để kiểm tràn

**Quan sát:**
- (a) ĐÃ SỬA — bảng nay có 2 cột RIÊNG "CB mức 1 (%)" và "CB mức 2 (%)", không còn cột gộp "Vùng cảnh báo"
- (b) ĐÃ SỬA — cột "Quá hạn (%)" đã có, giá trị 100% ở cả 6 dòng, khớp đặc tả srs-fr-10-quan-tri.md mục 9 Tab 1 ("Luôn = 100%")
- (c) KHÔNG tái hiện tràn — đo trên viewport 1440px: bảng clientWidth 1128 = scrollWidth 1128; mọi ô cột "Loại yêu cầu" (222px) và "Tên loại" (246px) đều có scrollWidth = clientWidth, không ô nào tràn
- Bộ cột đầy đủ: Loại yêu cầu | Tên loại | Thời hạn (ngày LV) | CB mức 1 (%) | CB mức 2 (%) | Quá hạn (%) | Số ngày BS tối đa | Email | Thông báo app | Hành động — khớp đặc tả mục 5-11 Tab 1
- Đủ 6 loại yêu cầu theo đặc tả mục 5: HOI_DAP / HOI_DAP_PHUC_TAP / VU_VIEC / HO_SO_HT / HO_SO_TT / HO_SO_CHI_TRA
- Cột "Số ngày BS tối đa" hiển thị "—" cho dòng HOI_DAP và 5 cho các dòng còn lại, khớp đặc tả mục 10 ("disabled + blank cho HOI_DAP")
- Hai khung cảnh báo đối tác báo thiếu nay đều có trên thẻ: "Giải thích các mức cảnh báo SLA (BR-SLA-02)" đủ 4 mức, và "Ảnh hưởng khi thay đổi cấu hình SLA" (cảnh báo snapshot)
- Không còn trường "Hệ số quá hạn" trên bảng lẫn trong form sửa — khớp srs-fr-10-quan-tri.md:2241 ("bắt buộc lưu, không hiển thị UI")

**Kết luận:** Cả 3 ý của claim vòng 2 đều đã xử lý: 2 cột cảnh báo tách riêng, có cột Quá hạn (%), không tái hiện tràn dữ liệu → **Pass**
**Bằng chứng:** [evidence/QLCHTHXLHS_03.log](evidence/QLCHTHXLHS_03.log) · [bảng điều kiện](cond/QLCHTHXLHS_03.md)
**Sheet:** tuần 3 dòng 153 → `Verify 2` = `Pass` ✅

### 49. ✅ QLCHTHXLHS_07 — Form sửa cấu hình SLA — trường "Số ngày bổ sung tối đa" (T3 dòng 156)

**Claim vòng 2 (TKM):** TKM retest 31/7: Thiếu trường thông tin "Số ngày bổ sung tối đa" (QLCHTHXLHS_07_v2.jpg)
**KQ mong đợi:** Form sửa hiển thị đủ trường theo thiết kế, tự nhập sẵn giá trị hiện tại; không có trường "Hệ số quá hạn"

**Luồng đã chạy lại:** Đăng nhập admin → Cấu hình hệ thống → thẻ SLA → bấm Sửa ở dòng "Vụ việc hỗ trợ pháp lý" → đọc toàn bộ nhãn + giá trị trong form → thử để trống trường → thử ngưỡng CB2 < CB1 → nhập giá trị mới 7 và lưu → đóng, mở lại form và đọc lại bảng để xác nhận giá trị được giữ → khôi phục về 5

**Quan sát:**
- KHÔNG tái hiện: form "Chỉnh sửa cấu hình SLA" CÓ trường "Số ngày bổ sung tối đa", tự điền sẵn giá trị hiện tại = 5
- Đủ nhãn theo đặc tả mục 12 Tab 1: Thời hạn (ngày làm việc) 10 · Ngưỡng cảnh báo 1 (%) 50 · Ngưỡng cảnh báo 2 (%) 100 · Số ngày bổ sung tối đa 5 · 2 công tắc "Gửi email cảnh báo" + "Gửi thông báo in-app" (đều bật) · nút [Hủy] [Đồng ý]
- KHÔNG còn trường "Hệ số quá hạn" trong form — khớp srs-fr-10-quan-tri.md:2241 (qua_han_he_so "bắt buộc lưu, không hiển thị UI", BA chốt 2026-05-07 Q5)
- Ràng buộc bắt buộc đã có: để trống "Số ngày bổ sung tối đa" rồi bấm Đồng ý → bị chặn, form báo "Số ngày bổ sung tối đa phải là số nguyên dương", drawer không đóng
- Ràng buộc thứ tự ngưỡng đã có: nhập Ngưỡng cảnh báo 2 = 40 (nhỏ hơn ngưỡng 1 = 50) → bị chặn, báo "Ngưỡng cảnh báo 2 phải lớn hơn ngưỡng cảnh báo 1"
- LƯU THẬT được và giữ giá trị: đổi Số ngày bổ sung tối đa 5 → 7, bấm Đồng ý → toast "Cập nhật cấu hình SLA thành công", dòng trên bảng đổi thành ...100%|7, mở lại form vẫn đọc ra 7. Đã khôi phục về 5 sau khi kiểm

**Kết luận:** Claim vòng 2 không tái hiện: trường đã có, tự điền giá trị hiện tại, có ràng buộc bắt buộc, lưu và giữ được giá trị mới; trường "Hệ số quá hạn" đã gỡ khỏi giao diện → **Pass**
**Bằng chứng:** [evidence/QLCHTHXLHS_07.log](evidence/QLCHTHXLHS_07.log) · [bảng điều kiện](cond/QLCHTHXLHS_07.md)
**Sheet:** tuần 3 dòng 156 → `Verify 2` = `Pass` ✅

### 50. ❌ QLTKND_03 — Thẻ trạng thái (tab nhanh) — Quản lý tài khoản (T3 dòng 166)

**Claim vòng 2 (TKM):** Thiếu thẻ "Vô hiệu hóa"; thẻ "Chờ kích hoạt" chưa có màu nhấn
**KQ mong đợi:** Thanh thẻ đúng 4 thẻ theo SCR-VIII-03 (bỏ "Chờ phân quyền"); màu trạng thái theo đặc tả

**Luồng đã chạy lại:** Đăng nhập admin (QTHT) -> Quản trị hệ thống -> Tài khoản & phân quyền -> đếm thẻ + bấm lần lượt 4 thẻ -> đo màu badge cột Trạng thái từng trạng thái -> chọn bộ lọc Trạng thái = "Vô hiệu hóa" -> bấm "Tìm kiếm"

**Quan sát:**
- Thanh thẻ có ĐÚNG 4 thẻ: Tất cả 207 / Hoạt động 145 / Chờ kích hoạt 20 / Tạm khóa 2 — KHÔNG còn "Chờ phân quyền" (khớp srs-fr-10-quan-tri.md:1713 + BA chốt 2026-05-07 Q3)
- Bấm từng thẻ lọc đúng: ?trangThai=CHO_KICH_HOAT -> 20 kết quả; HOAT_DONG -> 145; TAM_KHOA -> 2
- Ý "thiếu thẻ Vô hiệu hóa": đặc tả :1713 chỉ liệt kê 4 thẻ; VO_HIEU_HOA thuộc bộ lọc select (:1711). Chọn "Vô hiệu hóa" + bấm Tìm kiếm -> ?trangThai=VO_HIEU_HOA -> 38 kết quả => dev Reject ĐÚNG
- Ý "màu nhấn": tab không được đặc tả quy định màu (dev Reject đúng ở phạm vi tab), NHƯNG :1720 (SCR-VIII-03 item 15) quy định màu cho badge cột Trạng thái — đo thực tế lệch 3/4
- Badge CHO_KICH_HOAT = rgb(191,191,191) xám (class ant-badge-status-default) — đặc tả yêu cầu VÀNG
- Badge TAM_KHOA = rgb(212,136,6) hổ phách (ant-badge-status-warning) — đặc tả yêu cầu ĐỎ
- Badge VO_HIEU_HOA = rgb(245,34,45) đỏ (ant-badge-status-error) — đặc tả yêu cầu ĐEN
- Badge HOAT_DONG = rgb(56,158,13) xanh (ant-badge-status-success) — ĐÚNG đặc tả
- Bảng màu bị dịch: màu vàng đang gán nhầm cho TAM_KHOA, màu đỏ gán nhầm cho VO_HIEU_HOA, CHO_KICH_HOAT bỏ trống về mặc định
- Ảnh: evidence/QLTKND_03-badge-mau.png

**Kết luận:** Lỗi gốc (6 thẻ, dư "Chờ phân quyền") đã hết hoàn toàn và ý "thiếu thẻ Vô hiệu hóa" đúng là ngoài đặc tả; nhưng ý "Chờ kích hoạt chưa có màu nhấn" có cơ sở — đặc tả gán màu cho badge cột Trạng thái và 3/4 màu đang sai → **Reopen**
**Bằng chứng:** [evidence/QLTKND_03.log](evidence/QLTKND_03.log) · [bảng điều kiện](cond/QLTKND_03.md)
**Sheet:** tuần 3 dòng 166 → `Trạng thái dev fix 2` = `Reopen` · `Verify 2` = `Reopen` · `DEV phản hồi lần 2` = mô tả lỗi ❌

### 51. ✅ TLCTCDG_11 — Tiêu chí đánh giá — cảnh báo tổng trọng số ≠ 100% (T3 dòng 58)

**Claim vòng 2 (TKM):** Hệ thống hiện toast thành công, không hiện cảnh báo tổng trọng số (dòng này KHÔNG có claim vòng 2 — cột Verify vòng 1 còn trống, ghi bằng --mode qaverdict)
**KQ mong đợi:** Hiện "Tổng trọng số hiện tại: {X}%. Cần đảm bảo = 100% trước khi trình phê duyệt" (WRN-DG-TC-01), vẫn cho lưu

**Luồng đã chạy lại:** Đăng nhập cbnv_tw -> Đánh giá hiệu quả -> Thêm mới đợt "QA reverify TLCTCDG_11 2026-08-03" (Sơ bộ 6 tháng / Vụ việc / Bộ Công an / 01-08-2026..31-12-2026) -> Lưu & Chuyển tiêu chí -> Thêm tiêu chí trọng số 90, điểm tối đa 100 -> bấm Lưu (MutationObserver cài trước, KHÔNG lọc trùng) -> rời màn qua sidebar rồi mở lại đợt

**Quan sát:**
- Dữ liệu MỚI: đợt tự tạo trong round này (b5f73c4a…), trạng thái "Lập kế hoạch" — không tái dùng đợt cũ
- Vào tab Tiêu chí khi SUM=0%: banner "Tổng trọng số hiện tại: 0%. Cần đảm bảo = 100% trước khi trình phê duyệt" đã hiện
- Thêm tiêu chí trọng số 90: nhãn realtime "Tổng trọng số: 90%" + "(Tổng trọng số phải bằng 100%)" — khớp srs-fr-08-danh-gia.md:861
- Bấm Lưu -> observer bắt ĐỒNG THỜI: "Đã lưu tiêu chí đánh giá" VÀ "Tổng trọng số hiện tại: 90%. Cần đảm bảo = 100% trước khi trình phê duyệt" — đúng nguyên văn WRN-DG-TC-01 tại :862
- Banner còn kèm cảnh báo BR-CALC-08: "Tổng điểm tối đa có trọng số hiện tại: 90. Cần đảm bảo = 100 trước khi trình phê duyệt"
- KHÔNG chặn lưu — khớp :860 "Không chặn lưu" + AC :234 + BA chốt 2026-07-31 ghi đích danh TLCTCDG_11
- Mở lại đợt sau khi rời màn: tiêu chí còn nguyên (trọng số 90 / điểm tối đa 100), đợt vẫn "Lập kế hoạch", cảnh báo vẫn hiện => lưu thật ở máy chủ
- Ảnh: evidence/TLCTCDG_11-canh-bao-90.png

**Kết luận:** Không tái hiện: hệ thống vừa lưu thành công vừa hiện đúng cảnh báo nêu mức trọng số hiện tại và yêu cầu = 100% trước khi trình phê duyệt → **Pass**
**Bằng chứng:** [evidence/TLCTCDG_11.log](evidence/TLCTCDG_11.log) · [bảng điều kiện](cond/TLCTCDG_11.md)
**Sheet:** tuần 3 dòng 58 → `Verify` (vòng 1) = `Pass` · note nối thêm vào `DEV phản hồi lần 1`, GIỮ nguyên phần dev đã viết (`--mode qaverdict`; dòng này không có claim vòng 2 nên KHÔNG đụng `Trạng thái dev fix 2` / `Verify 2`) ✅

### 52. ✅ TDHSTVV_13 — Thẩm định hồ sơ TVV — kết luận Yêu cầu bổ sung (T2 dòng 67)

**Claim vòng 2 (TKM):** TKM retest 25/7: Người hỗ trợ không nhận được thông báo kèm lý do
**KQ mong đợi:** Hồ sơ chuyển "Yêu cầu bổ sung" + gửi thông báo kèm lý do đến Người hỗ trợ + lưu vết thao tác + hiện "Đã gửi yêu cầu bổ sung đến Người hỗ trợ"

**Luồng đã chạy lại:** SEED dữ liệu mới: đặt lại mật khẩu nht_tc001_btp_tw qua hộp thư giả lập -> đăng nhập NHT, ghi mốc chuông = 3 (đều "3 tháng trước") -> NHT tạo hồ sơ TVV mới "TVV RV2 0308 Kiem Thu" (TVV-BTP-TW-0068, email ứng viên rv2tvv0308@htpldn.test, có tệp thẻ hành nghề) => trạng thái Mới đăng ký. VERIFY: đăng nhập cbnv_tw -> mở hồ sơ -> "Bắt đầu thẩm định" -> tab Thẩm định -> Kết luận Pháp lý "Đạt" + Kết luận thẩm định "YÊU CẦU BỔ SUNG" + lý do mốc "RV2-0308-BOSUNG: ..." -> cài MutationObserver (KHÔNG lọc trùng) -> bấm "Gửi KQ" -> kiểm hộp thư -> đăng nhập lại NHT xem chuông + trang Thông báo -> đăng nhập admin xem Nhật ký hệ thống

**Quan sát:**
- Ý 1 — trạng thái: hồ sơ chuyển từ "Đang thẩm định" sang "Yêu cầu bổ sung" ngay sau khi Gửi KQ ✅
- Ý 4 — câu xác nhận trên màn: observer bắt toast "Đã gửi yêu cầu bổ sung đến Người hỗ trợ" — ĐÚNG NGUYÊN VĂN Kết quả mong đợi, không còn là "Đã lưu kết quả thẩm định" như vòng trước ✅
- Ý 2a — thông báo trong phần mềm cho Người hỗ trợ: chuông NHT tăng 3 -> 4; trang Thông báo có mục mới "Yêu cầu bổ sung hồ sơ TVV" lúc 03/08/2026 18:49, nội dung CHỨA NGUYÊN VĂN lý do "RV2-0308-BOSUNG: De nghi bo sung ban sao cong chung bang tot nghiep va the hanh nghe con hieu luc." ✅
- Nhãn nhóm của thông báo là "Thẩm định" — khớp việc vừa xảy ra (lỗi phụ vòng trước gắn nhầm nhóm "Phê duyệt" đã hết)
- Ý 2b — thư điện tử: hộp thư có thư "Yêu cầu bổ sung hồ sơ TVV" gửi nht_tc001_btp_tw@htpldn.test kèm nguyên văn lý do ✅
- Ý 2c — thư cho chủ hồ sơ: thư "Yêu cầu bổ sung hồ sơ" gửi rv2tvv0308@htpldn.test cũng kèm nguyên văn lý do, KHÔNG bị thay thế ✅
- Ý 3 — lưu vết: Nhật ký hệ thống có bản ghi 03/08/2026 18:49:01, Người dùng "Cán bộ NV Trung ương", Module CG-TVV, Entity TU_VAN_VIEN, Mã c19568f0…, Loại thao tác "Thẩm định" ✅
- Ảnh: evidence/TDHSTVV_13-ho-so-yeu-cau-bo-sung.png · TDHSTVV_13-thong-bao-kem-ly-do.png · TDHSTVV_13-nhat-ky-luu-vet.png

**Kết luận:** Không tái hiện claim vòng 2: Người hỗ trợ đã nộp hồ sơ nhận được thông báo trong phần mềm VÀ thư điện tử, đều kèm nguyên văn lý do; đủ cả 4 ý của Kết quả mong đợi → **Pass**
**Bằng chứng:** [evidence/TDHSTVV_13.log](evidence/TDHSTVV_13.log) · [bảng điều kiện](cond/TDHSTVV_13.md)
**Sheet:** tuần 2 dòng 67 → `Verify 2` = `Pass` ✅

### 53. ✅ NHSYC_02 — Form "Nhập thủ công" vụ việc HTPL (T2 dòng 88)

**Claim vòng 2 (TKM):** TKM retest 29/7: Lỗi vẫn chưa được fix (không nêu rõ ý nào)
**KQ mong đợi:** Form hiển thị đủ trường theo thiết kế, đúng định dạng, không tràn/đè, đồng nhất ngôn ngữ

**Luồng đã chạy lại:** Đăng nhập cbnv_tw -> Vụ việc HTPL -> "Nhập thủ công" -> liệt kê toàn bộ nhóm + trường (nhãn / bắt buộc / kiểu) bằng evaluate_script -> đếm giá trị từng danh mục -> chọn DN "Công ty TNHH Mẫu Test" -> điền đủ + Ngày tiếp nhận 02/08/2026 -> bấm "Lưu & Tiếp nhận" (MutationObserver cài trước) -> mở chi tiết vụ việc vừa tạo đọc lại giá trị

**Quan sát:**
- Form có ĐỦ 4 nhóm đúng thiết kế: Thông tin Doanh nghiệp / Nội dung Yêu cầu / Tài liệu Đính kèm / Thông tin Tiếp nhận
- Ý DUY NHẤT dev nhận là bug — nhóm 4 thiếu "Ngày tiếp nhận": ĐÃ CÓ, kiểu chọn ngày, gắn dấu bắt buộc ✅
- Nhóm 4 hiện gồm: Kênh tiếp nhận (bắt buộc) · Ngày tiếp nhận (bắt buộc) · Người tiếp nhận
- Lưu thật (không dừng ở quan sát): tạo được VV-BTP-TW-20260803-002, toast "Đã tiếp nhận — VV-BTP-TW-20260803-002"
- Mở lại chi tiết vụ việc: "Ngày tiếp nhận 02/08/2026 07:00" — đúng giá trị vừa nhập; "Kênh tiếp nhận Điện thoại" đúng => nhập-lưu-hiển thị lại khớp
- Ghi nhận (KHÔNG tính lỗi — BA chốt 16/07: danh mục cấu hình được, không phải lỗi Dev): Lĩnh vực pháp luật 10 giá trị · Loại hình hỗ trợ 8 giá trị · Kênh tiếp nhận 3 giá trị (Trực tiếp/Điện thoại/Bưu chính)
- Ảnh: evidence/NHSYC_02-vu-viec-ngay-tiep-nhan.png

**Kết luận:** Phần dev nhận trách nhiệm đã fix và chạy đúng trọn luồng (có trường, nhập được, lưu được, hiển thị lại đúng); các ý còn lại thuộc danh mục cấu hình / đặc tả đã được BA chốt 16/07 là không phải lỗi Dev → **Pass**
**Bằng chứng:** [evidence/NHSYC_02.log](evidence/NHSYC_02.log) · [bảng điều kiện](cond/NHSYC_02.md)
**Sheet:** tuần 2 dòng 88 → `Verify 2` = `Pass` ✅

### 54. ✅ QLDX_03 — Tự động đăng xuất khi hết phiên (T3 dòng 184)

**Claim vòng 2 (TKM):** TKM retest 31/7: không hiển thị hộp thoại cảnh báo, hệ thống chuyển thẳng màn Đăng nhập kèm "Đăng xuất thành công"
**KQ mong đợi:** Không thao tác 25 phút: hiện hộp thoại cảnh báo sắp hết phiên, cho gia hạn. Không thao tác 30 phút: tự đăng xuất, chuyển về màn đăng nhập

**Luồng đã chạy lại:** Đăng nhập mới lúc 19:02 -> để nguyên màn Tổng quan, KHÔNG thao tác, chỉ đọc DOM định kỳ 5s bằng bộ ghi nhận (MutationObserver + sampler) -> đo mốc hiện hộp thoại và mốc bị đưa về /login

**Quan sát:**
- Lượt đo đồng hồ thật (19:02 -> 19:17): phiên sống liên tục 14.8 phút, KHÔNG hộp thoại, KHÔNG bị đăng xuất, URL giữ /dashboard -> bác bỏ giả thiết phiên chết sớm 7-10 phút
- Lượt đo này bị hỏng ở phút 14.8 do RỚT MẠNG phía máy test (trang rơi vào chrome-error ERR_INTERNET_DISCONNECTED), không phải lỗi ứng dụng -> không lấy làm kết luận
- Lượt đo lại: đặt mốc hoạt động cuối = 19:23:20 rồi để đồng hồ THẬT chạy. Đúng 19:48:21 (= idle 25.0 phút) hộp thoại bật: 'Phiên đăng nhập sắp hết hạn - Bạn không thao tác trong một thời gian. Phiên sẽ tự đăng xuất sau 5:00. Nhấn Tiếp tục đăng nhập để giữ phiên làm việc' + 2 nút [Đăng xuất] [Tiếp tục đăng nhập]
- Đồng hồ đếm ngược chạy thật theo từng giây (5:00 -> 4:11 -> 4:06 -> ... -> 3:42), không phải nhãn tĩnh
- Hết đếm ngược ở mốc 30 phút: hệ thống tự đăng xuất, tải lại và chuyển về /login. Kiểm chứng phiên đã bị hủy thật: trước đó lúc 19:46 gọi /login còn bị đưa về /dashboard, sau khi hết phiên thì /login đứng nguyên
- Đồng hồ canh mạng chạy song song (curl mỗi 25s): **78/78 lần trả HTTP 200** liên tục 19:46:52-20:19:03, phủ kín toàn bộ khoảng đo -> loại trừ khả năng đăng xuất do rớt mạng (log: evidence/QLDX_03-canh-mang.log)
- Đặc tả: srs-fr-10-quan-tri.md:1959 'Dang xuat tu dong: 25 phut idle -> Modal canh bao -> 30 phut -> Auto invalidate -> Redirect MH-10.8b'; SCR-VIII-09 row 12 mô tả modal Session Warning

**Kết luận:** Hộp thoại cảnh báo bật đúng mốc 25 phút và hệ thống tự đăng xuất đúng mốc 30 phút, khớp đặc tả; không tái hiện được triệu chứng đối tác báo → **Pass**
**Bằng chứng:** [evidence/QLDX_03.log](evidence/QLDX_03.log) · [QLDX_03-hop-thoai-canh-bao-25p.png](evidence/QLDX_03-hop-thoai-canh-bao-25p.png) · [QLDX_03-tu-dang-xuat-30p.png](evidence/QLDX_03-tu-dang-xuat-30p.png) · [bảng điều kiện](cond/QLDX_03.md)
**Sheet:** tuần 3 dòng 184 → `Verify 2` = `Pass` ✅
