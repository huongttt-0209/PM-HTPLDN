# KTDGKQHT_20 — evidence audit (bug do QA phát hiện ngoài phạm vi case)

- Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` **row 130** · mở ngày 2026-08-03 khi verify KTDGKQHT_02.
- Verdict QA: **Open** (cột Verify). Cột `Trạng thái dev fix 1` giữ `dev done` của dev — QA **chưa** re-verify bản fix.

## Note dev trước khi QA đè (2026-08-03)

> Dev phản hồi SAU khi QA mở dòng bug này. Lưu nguyên văn trước khi cột R bị ghi đè bằng note QA:

```
Đã fix (BUG thật BR-KQ-08/BR-KQ-02): mẫu số tỷ lệ chuyên cần = COUNT(lịch học) của khóa, không phải so_buoi_hoc/buổi đã điểm danh (write-path recalculateAttendance). Commit 94bf3820. Verify local + 120: điểm danh lại → tong_buoi=3, 33.33% (UI+DOCX). ⚠️ giá trị stored — khóa cũ tự đúng khi điểm danh lần kế.
```

**Đọc note dev:** dev **xác nhận đây là bug thật** (khớp verdict `Open` của QA), khai đã sửa ở commit `94bf3820` và cảnh báo giá trị là **stored** — khóa cũ chỉ tự đúng khi điểm danh lần kế tiếp.

## Việc cần làm vòng sau

Re-verify trên **dữ liệu MỚI**, không dùng lại khóa `KH-QAW7-HOINGHI` cũ: vì đây là trường lưu trong CSDL, bản ghi tạo trước bản fix vẫn giữ giá trị sai → re-test bản ghi cũ dễ ra kết luận Reopen oan. Tạo khóa mới, thêm nhiều buổi, điểm danh một phần rồi mới đo.
