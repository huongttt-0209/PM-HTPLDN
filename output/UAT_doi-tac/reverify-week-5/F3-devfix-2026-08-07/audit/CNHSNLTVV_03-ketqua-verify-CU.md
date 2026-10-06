# Nội dung CŨ của ô 'Kết quả verify' — dòng 36 · CNHSNLTVV_03

Chụp lại lúc bắt đầu lô F3-devfix-2026-08-07, TRƯỚC khi đè (prompt mục 6 cho phép đè `--cho-phep-de-ketqua`).

- Trạng thái dev fix (lúc chụp): `Fixed`
- Dopai (lúc chụp): `dev done`
- DEV phản hồi lần 1 (lúc chụp): ĐÃ VERIFY E2E PASS local + server 120 V1.0.6 (04/08/2026). Actor 120 nht_qa_tw, hồ sơ TVV-BTP-TW-0002: Cập nhật năng lực lưu thành công, PATCH /nang-luc HTTP 200; reload GET HTTP 200 và dữ liệu hiển thị đúng. Đã khôi phục dữ liệu test sau verify. Không cần code/commit mới: happy-path đã được khắc phục bởi nhóm CNHSNLTVV_02 (3735fa1b9, f5c87089d, 77857dd16, b296b5529). Evidence: CNHSNLTVV_03-120-v106-save-pass.png.

---

## Nguyên văn ô 'Kết quả verify'

```text
🔁 CÒN LỖI Ở ĐÂU: Màn Cập nhật năng lực tư vấn viên — lượt lưu có đính tệp ở khối "Thêm chứng chỉ mới" vẫn báo "Lỗi hệ thống, vui lòng thử lại sau." và không lưu được gì. Tái hiện 3/3 lượt.
VÌ SAO LÀ LỖI: srs-fr-04-chuyen-gia-tvv.md:433 đòi lưu thành công khi cập nhật thông tin/chứng chỉ có kèm tệp tải lên; :425-:429 chỉ cho phép từ chối trong 5 tình huống dữ liệu/quyền cụ thể, không có tình huống này.
ĐÃ HẾT LỖI: 4/4 lượt lưu không đính tệp đều thành công, dữ liệu còn nguyên sau khi tải lại trang (trường chữ/số, lĩnh vực, bằng cấp và chứng chỉ chi tiết).
AI SỬA: Dev BE.
ĐÃ ĐO: nht_qa_tw (NHT). 2 hồ sơ × 5 dạng = 7 lượt bấm Lưu, mỗi lượt 1 request/1 thông báo. Lỗi không phụ thuộc tên tệp hay hồ sơ; bỏ trường tệp thì lưu được.
CÁCH VERIFY SAU DEV FIX: Vai trò NHT, tab Năng lực trên 2 hồ sơ (1 Đang hoạt động, 1 Mới đăng ký), bấm Lưu 6 lượt (2 lượt không tệp, 4 lượt có tệp, đủ 2 kiểu tên tệp); tải lại trang, tệp phải hiện ở "Chứng chỉ hiện có". Chỉ lượt không tệp chạy được thì chưa đạt.
```
