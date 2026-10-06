# DKTGMLTVV_OOS_02 — lưu note DEV trước khi QA ghi đè (2026-08-03)

- Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` **row 139**, mở 03/08/2026 17:33 khi verify luồng Mạng lưới TVV.
- Dev phản hồi + tự đặt `P = dev done`, ai đó đặt `Q = Pass` trong khoảng 20:20–21:10, **sau** khi QA đọc dòng này lúc ~21:00.

## Nguyên văn phần dev nối vào cột R

```
[DEV 03/08] Nhãn "Số CMND/CCCD" → đã đổi "Số Căn cước công dân" theo SCR-IV-02 :1495 (commit 16a54e26a). Đủ 3 nhãn đúng SRS → dev done.
```

**Đọc note dev:** dev chỉ nêu đã đổi 1 nhãn ("Số CMND/CCCD" → "Số Căn cước công dân", commit `16a54e26a`) nhưng khẳng định đủ cả 3 nhãn đúng đặc tả. QA đo độc lập lúc 21:05 trên gói `index-B1e0L2GY.js`: **đúng cả 3** — khớp lời dev. Giữ `Pass`.

## Vì sao QA vẫn ghi đè cột R

Note QA cũ còn câu "Đề nghị BA xác nhận riêng điểm 2" — nay đã xác định KHÔNG cần BA (đặc tả nhất quán dùng "Căn cước công dân" ở `:1495`, `:202`, `:337`, `:1438`, `:1527`). Để nguyên sẽ đẩy sang BA một câu hỏi không cần thiết. Note mới rút lại đề nghị đó và **giữ lại nguyên văn dòng dev** ở cuối.
