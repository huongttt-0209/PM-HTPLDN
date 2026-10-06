# Phản hồi BA — CTTLV_01 (dòng 270) · Báo cáo Chương trình theo lĩnh vực

**Phiếu nguồn:** `ba-confirm-CTTLV_01.md`
**Nguồn đối chiếu:** CSV baseline (`docs/Input/Danh sách transaction_v1.1_2026-03-27.csv`, UC145 dòng 1287, UC160 dòng 1453) · SRS v3.5 (`srs-fr-11-bao-cao.md` FR-IX-22, `srs-fr-15-ct-htpldn.md` entity + FR-XI-01).
**Ngày lập:** 23/07/2026.

---

## CTTLV_01 — Báo cáo Chương trình theo lĩnh vực gom nhóm "Không xác định"

**Loại quyết định:** **Loại 2 — Update SRS + Dev update theo SRS mới.** ✅ Đã chốt (2026-07-23): bổ sung trường "Lĩnh vực pháp lý" (bắt buộc, chọn một) cho chương trình HTPL.

**Bối cảnh nghiệp vụ.** Báo cáo UC145 ("Báo cáo thống kê chương trình hỗ trợ theo lĩnh vực pháp lý") phục vụ cán bộ nghiệp vụ/phê duyệt tổng hợp xem mỗi lĩnh vực pháp lý có bao nhiêu chương trình và bao nhiêu doanh nghiệp tham gia. Muốn thống kê "theo lĩnh vực", mỗi chương trình phải mang một lĩnh vực pháp lý — đây là dữ liệu đầu vào, không phải thứ báo cáo tự suy ra.

**Đối tác phản ánh.** Báo cáo hiển thị nhóm **"Không xác định"** và cho là dữ liệu sai; kỳ vọng mọi chương trình đều hiện đúng tên lĩnh vực. Hiện tượng tái hiện đúng: phần mềm hiển thị trung thực dữ liệu (chương trình có lĩnh vực → hiện tên; chưa có → gom "Không xác định"). Gốc rễ nằm ở đặc tả, không ở code.

**Đối chiếu SRS/CSV.** Mâu thuẫn nội bộ SRS:
1. Báo cáo YÊU CẦU gom theo lĩnh vực — FR-IX-22 (`srs-fr-11-bao-cao.md:961` §Mô tả "hàng = lĩnh vực"; `:981-982` §Output `linh_vuc_id`+`ten_linh_vuc` "Luôn"); CSV UC145 (dòng 1287) "thống kê theo lĩnh vực pháp lý".
2. NHƯNG chương trình không có nơi gán lĩnh vực — entity `CHUONG_TRINH_HTPL` (`srs-fr-15-ct-htpldn.md:1321-1334`, 12 trường) không có trường lĩnh vực; form FR-XI-01 §Inputs (`:125-137`) cũng không; CSV UC160 (dòng 1453) không nêu.
3. SRS im lặng về xử lý chương trình null lĩnh vực (gom "Không xác định" / ẩn / bắt buộc gán) — không có quy ước dùng chung.
→ Theo SRS hiện tại, không có cách gán lĩnh vực cho chương trình → mọi chương trình rơi vào "Không xác định".

**Căn cứ pháp lý & nghiệp vụ.**
- **NĐ 55/2019/NĐ-CP** Điều 10 khoản 2 (chương trình HTPL gồm 3 hoạt động), Điều 12 (chương trình 3 cấp), **Điều 14 khoản 3b** — chương trình thực hiện *"trong phạm vi ngành, lĩnh vực do mình quản lý"* → chương trình vốn gắn một lĩnh vực quản lý, gắn trường lĩnh vực là phù hợp tinh thần NĐ55.
- **TT 17/2025/TT-BTP** (báo cáo thống kê ngành Tư pháp, hiệu lực 01/11/2025) — báo cáo theo lĩnh vực nằm trong chế độ báo cáo, cần chương trình có trường lĩnh vực để gom số liệu.

**Nội dung xử lý.** BA cập nhật SRS rồi Dev làm theo bản mới:
- Thêm trường **Lĩnh vực pháp lý** (tham chiếu danh mục Lĩnh vực pháp lý dùng chung), **bắt buộc, chọn một lĩnh vực chính**, vào: entity `CHUONG_TRINH_HTPL` (`srs-fr-15-ct-htpldn.md:1321-1334`); form FR-XI-01 §Inputs (`:125-137`); baseline §3.4.3.46 (`srs-v3.5.md`); nêu rõ nguồn lĩnh vực + xử lý null ở báo cáo FR-IX-22 (`srs-fr-11-bao-cao.md`).
- Sau khi SRS cập nhật → Dev bổ sung trường; báo cáo gom theo lĩnh vực thật, nhóm "Không xác định" không còn.
