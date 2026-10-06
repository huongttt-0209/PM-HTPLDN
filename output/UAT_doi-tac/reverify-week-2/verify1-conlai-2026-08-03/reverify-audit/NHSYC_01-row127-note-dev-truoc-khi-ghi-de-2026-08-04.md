# Bản sao cột P / Q / R dòng 127 (tab tuần 2) TRƯỚC khi QA ghi đè
Thời điểm sao lưu: 2026-08-04T11:58:17
Mã TC: NHSYC_01

## P — Trạng thái dev fix 1
BA confirm

## Q — Verify
Reopen

## R — DEV phản hồi lần 1 (nguyên văn, đây là phần sẽ bị ghi đè)
REOPEN đã fix: (A) tạo hồ sơ CÓ tệp không còn 500 — ghi ho_so qua RLS-pinned manager (trước dùng pool repo không mang GUC RLS → policy fail). (B) điểm ưu tiên auto-calc BR-CALC-07 (DN thường→1) + nhãn sạch mã. Commit f50e96666. Verify local PASS; 120 A đang confirm. ⚠️ B còn 3 điểm CHỜ BA: thang điểm SRS mâu thuẫn (1=Rất cao vs cộng dồn), ngưỡng LĐ nữ chưa định lượng, createForDn ngoài phạm vi — sẽ có phiếu BA riêng.
