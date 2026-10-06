# Phản hồi BA — CTTLV_01 (dòng 270) · Báo cáo Chương trình theo lĩnh vực

**Phiếu nguồn:** `ba-confirm-CTTLV_01.md`
**Nguồn đối chiếu:** CSV baseline (`docs/Input/Danh sách transaction_v1.1_2026-03-27.csv`, UC145 dòng 1287, UC160 dòng 1453) · SRS v3.5 (`srs-fr-11-bao-cao.md` FR-IX-22, `srs-fr-15-ct-htpldn.md` entity + FR-XI-01).
**Ngày lập:** 23/07/2026.

## CTTLV_01 — Báo cáo Chương trình theo lĩnh vực gom nhóm "Không xác định"

**(1) Phần mềm đúng SRS chưa?** SRS **tự mâu thuẫn** (không phải lỗi code). Báo cáo FR-IX-22 **bắt** gom theo lĩnh vực — mỗi hàng một lĩnh vực (`srs-fr-11-bao-cao.md:961`, `:981-982`); CSV UC145 (dòng 1287) cũng ghi "thống kê theo lĩnh vực pháp lý". NHƯNG dữ liệu chương trình **không có trường lĩnh vực** để nhập (12 trường, không có lĩnh vực — `srs-fr-15-ct-htpldn.md:1321-1334`; form tạo/sửa cũng không có ô — `:125-137`; CSV UC160 dòng 1453 không nêu). Không có chỗ nhập → mọi chương trình rơi "Không xác định". Phần mềm hiển thị **đúng theo dữ liệu**: chương trình đã gán lĩnh vực thì hiện tên, chưa gán thì gom "Không xác định".

**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG khác về ý định. Đối tác muốn báo cáo hiện **tên lĩnh vực thật** thay vì "Không xác định" — đúng bằng điều SRS vốn muốn (gom theo lĩnh vực). Vướng mắc chỉ là SRS thiếu **trường lĩnh vực** để nhập, nên không có dữ liệu mà gom.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ. Thiếu trường lĩnh vực thì cả báo cáo "theo lĩnh vực" vô nghĩa (mọi chương trình rơi "Không xác định"). Phải thêm trường **Lĩnh vực pháp lý** (bắt buộc, chọn một) vào entity `CHUONG_TRINH_HTPL` (`srs-fr-15-ct-htpldn.md:1321-1334`) + form FR-XI-01 §Inputs (`:125-137`) + baseline §3.4.3.46 (`srs-v3.5.md`) + nêu nguồn lĩnh vực & xử lý null ở FR-IX-22 (`srs-fr-11-bao-cao.md`). Căn cứ: NĐ 55/2019/NĐ-CP — chương trình HTPL thực hiện "trong phạm vi ngành, lĩnh vực do mình quản lý" (Điều 14 khoản 3b; hoạt động Điều 10 khoản 2; lập theo cấp Điều 12) nên vốn đã gắn một lĩnh vực; TT 17/2025/TT-BTP (chế độ báo cáo thống kê ngành Tư pháp) cần chương trình có trường lĩnh vực mới gom được.

**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: thêm trường Lĩnh vực pháp lý (bắt buộc) cho chương trình HTPL.** ✅ Đã chốt (2026-07-23). BA đã cập nhật SRS; Dev triển khai; test dòng 270/272 chạy lại sẽ Pass (Kết quả mong đợi **giữ nguyên**). `CTTLV_01` (dòng 270) và `CTTLV_04` (dòng 272) là **cùng một vấn đề gốc** — chốt cùng phương án.
> **Phương án xử lý (cập nhật SRS):** SRS đã cập nhật — `srs-fr-15-ct-htpldn.md:1330` bổ sung entity `CHUONG_TRINH_HTPL.linh_vuc_id` (bắt buộc, FK→DANH_MUC loai='LINH_VUC_PL') + form FR-XI-01 §Inputs ô #8 `linh_vuc_id` tại `:136` + FR-IX-22 "Nguồn dữ liệu lĩnh vực & xử lý thiếu" tại `srs-fr-11-bao-cao.md:986-988` (baseline §3.4.3.10 đồng bộ). Còn lại Dev triển khai: thêm ô chọn Lĩnh vực pháp lý (bắt buộc) vào form tạo/sửa CT, gom BC theo `linh_vuc_id`; test dòng 270/272 chạy lại Pass, Kết quả mong đợi giữ nguyên.
