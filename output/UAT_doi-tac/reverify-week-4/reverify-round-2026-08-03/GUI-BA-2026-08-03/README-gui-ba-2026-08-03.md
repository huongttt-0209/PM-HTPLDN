# 📤 GỬI BA — 2026-08-03

> **Đọc file này trước.** Thư mục này là **gói gửi BA** của đợt re-verify vòng 2 (54 case dev báo đã fix, chạy ngày 03/08/2026). Gửi **nguyên thư mục** `GUI-BA-2026-08-03/` là đủ, không cần kèm gì thêm.

## Gửi cái gì

| # | File | Nội dung | Gửi BA? |
|---|---|---|---|
| 1 | [`ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md`](ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md) | **Tài liệu chính** — 21 phiếu chờ BA, đối chiếu SRS + 4 câu hỏi + bảng để BA điền quyết định | ✅ **Gửi** |
| 2 | `evidence/SLHDVM_07-bao-cao-hoi-dap.pdf` | Tệp PDF thật hệ thống xuất ra ngày 03/08 (BC Số lượng hỏi đáp) — để BA xem tận mắt phần đầu/cuối trang | ✅ **Gửi** |
| 3 | `evidence/CGTVPL_07-bao-cao-so-luong-cg-tvv.pdf` | Tệp PDF thật thứ hai (BC Số lượng CG/TVV) — đối chứng cho thấy mọi báo cáo nhóm IX đều cùng khuôn | ✅ **Gửi** |
| 4 | Thư mục này (README) | Bản đồ gói gửi | tùy |

## Hỏi BA cái gì (tóm tắt 1 đoạn)

Tệp **PDF của màn Báo cáo thống kê** hiện đã xuất được bình thường (hết lỗi "Forbidden"), đúng A4 + Times New Roman + đủ 4 mục đầu tệp, số liệu khớp màn hình. Nhưng tệp **không có quốc hiệu / tên cơ quan ở đầu trang và không có ngày ký / chức danh ở cuối trang** như câu chữ trong phiếu UAT yêu cầu.

Chỗ này **vướng ở đặc tả chứ không phải ở phiếu**: đặc tả vừa nói tệp PDF phải "theo Thông tư 17/2025" (kéo theo cả khung văn bản hành chính), vừa mô tả riêng phần đầu tệp của báo cáo thống kê chỉ gồm 4 mục — và chính đặc tả cũng đang ghi chú là phần trích dẫn Thông tư 17/2025 chưa được tra cứu lại. Vì vậy QA **không tự chốt** được, xin BA quyết.

**4 câu hỏi** (chi tiết + căn cứ trong file số 1): ① PDF nhóm IX có bắt buộc khung hành chính không · ② dọn câu chữ đặc tả theo hướng nào · ③ quy ước đặt tên tệp xuất · ④ có cần ký số điện tử không.

## Quyết định của BA ảnh hưởng bao nhiêu phiếu

| Kịch bản | Số phiếu đổi kết quả | Ai xử lý tiếp |
|---|---|---|
| Câu ① chốt **"có bắt buộc"** | **21** phiếu PDF → `Reopen` | Dev BE bổ sung quốc hiệu + khối ký |
| Câu ① chốt **"không bắt buộc"** | **21** phiếu PDF → `Pass` | BA cập nhật lại "Kết quả mong đợi" của 21 phiếu + dọn câu chữ đặc tả |
| Câu ③ chốt **"có quy ước tên tệp"** | thêm **17** phiếu Excel đang `Pass` phải mở lại | Dev BE đổi quy ước đặt tên |

> QA nghiêng về **"không bắt buộc"** — lý do và căn cứ ghi trong file số 1, mục *Đề xuất QA tạm thời*.

## Bối cảnh (không cần gửi BA, để tra khi cần)

- Kết quả đầy đủ 54 case: [`../KET-QUA-REVERIFY-VONG-2.md`](../KET-QUA-REVERIFY-VONG-2.md) — 30 Pass · 3 Reopen · 21 BA confirm.
- Hồ sơ mâu thuẫn đặc tả gốc: `tasks/srs-contradictions.md` → **SRS-C-010** (Open).
- Sheet đã ghi: tab `UAT_TGPL Doanh Nghiệp-tuần 3`, cột `Verify 2` = `BA confirm` cho 21 dòng; cột `Trạng thái dev fix 2` **giữ nguyên** của dev.

---

*Gói gửi BA lập ngày 2026-08-03 · QA Automation via Claude Code*
