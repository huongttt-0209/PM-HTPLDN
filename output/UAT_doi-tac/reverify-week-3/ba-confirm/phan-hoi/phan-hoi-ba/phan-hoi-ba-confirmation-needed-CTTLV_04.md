# Phản hồi BA — CTTLV_04 (dòng 272) · Báo cáo Chương trình theo lĩnh vực — nhóm "Không xác định"

**Phiếu nguồn:** `ba-confirm-CTTLV_04.md`
**Nguồn đối chiếu:** CSV baseline (UC145 dòng 1287) · SRS v3.5 (`srs-fr-11-bao-cao.md` FR-IX-22, `srs-fr-15-ct-htpldn.md` entity + FR-XI-01).
**Ngày lập:** 23/07/2026.

## CTTLV_04 — Báo cáo Chương trình theo lĩnh vực gom nhóm "Không xác định"

**(1) Phần mềm đúng SRS chưa?** SRS **tự mâu thuẫn** (không phải lỗi code). Báo cáo FR-IX-22 **bắt** gom theo lĩnh vực (`srs-fr-11-bao-cao.md:961`, `:981-982`); CSV UC145 (dòng 1287) cũng ghi "theo lĩnh vực pháp lý". NHƯNG dữ liệu chương trình chỉ 12 trường, **không có ô lĩnh vực** (`srs-fr-15-ct-htpldn.md:1321-1334`); form tạo/sửa cũng không có (`:125-137`); CSV UC160 (dòng 1453) không nêu. Không có chỗ nhập → mọi chương trình rơi "Không xác định". Phần mềm hiển thị **đúng theo dữ liệu**: chương trình đã gán thì hiện tên, chưa gán thì gom "Không xác định" (thử 3 chương trình chưa gán + 1 gán "Thương mại" → ra đúng 2 nhóm).

**(2) Đối tác yêu cầu có khác SRS không? Khác gì?** KHÔNG khác về ý định. Đối tác muốn báo cáo hiện **tên lĩnh vực thật** thay vì "Không xác định" — đúng bằng điều SRS vốn muốn (gom theo lĩnh vực). Vướng mắc chỉ là SRS thiếu **trường lĩnh vực** để nhập.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không?** CÓ. Thiếu trường lĩnh vực thì cả báo cáo "theo lĩnh vực" vô nghĩa. Phải thêm trường **Lĩnh vực pháp lý** (bắt buộc, chọn một) vào entity `CHUONG_TRINH_HTPL` (`srs-fr-15-ct-htpldn.md:1321-1334`) + form FR-XI-01 (`:125-137`) + baseline §3.4.3.46 (`srs-v3.5.md`) + nêu nguồn lĩnh vực & xử lý null ở FR-IX-22 (`srs-fr-11-bao-cao.md:952-990`). Căn cứ pháp lý xem đầy đủ ở `phan-hoi-ba-confirm-CTTLV_01.md` (NĐ 55/2019/NĐ-CP Điều 10.2 / 12 / **14.3b** "trong phạm vi ngành, lĩnh vực do mình quản lý"; TT 17/2025/TT-BTP).

**→ Kết luận: Loại 2 — Cập nhật SRS rồi Dev làm theo SRS mới: thêm trường Lĩnh vực pháp lý (bắt buộc) cho chương trình HTPL.** ✅ Đã chốt (2026-07-23). `CTTLV_04` (dòng 272) và `CTTLV_01` (dòng 270) là **cùng một vấn đề gốc** — chốt cùng phương án, cập nhật SRS một lần. **Kết quả mong đợi hai dòng 270 + 272 giữ nguyên**; sau khi Dev bổ sung trường theo SRS, test chạy lại sẽ Pass.
> **Phương án xử lý (cập nhật SRS):** SRS đã cập nhật — `srs-fr-15-ct-htpldn.md:1330` bổ sung entity `CHUONG_TRINH_HTPL.linh_vuc_id` (bắt buộc, FK→DANH_MUC loai='LINH_VUC_PL') + form FR-XI-01 §Inputs ô #8 `linh_vuc_id` tại `:136` + FR-IX-22 "Nguồn dữ liệu lĩnh vực & xử lý thiếu" tại `srs-fr-11-bao-cao.md:986-988` (baseline §3.4.3.10 đồng bộ). Còn lại Dev triển khai: thêm ô chọn Lĩnh vực pháp lý (bắt buộc) vào form tạo/sửa CT, gom BC theo `linh_vuc_id`; test dòng 270/272 chạy lại Pass, Kết quả mong đợi giữ nguyên.
