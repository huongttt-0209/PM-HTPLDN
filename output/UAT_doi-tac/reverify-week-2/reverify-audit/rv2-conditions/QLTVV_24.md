# Bảng đối chiếu điều kiện — QLTVV_24 (re-verify sau dev fix, 2026-07-15)

Re-test đúng vai trò/màn/data mà bug gốc mô tả (bug-report §Các bước tái hiện).

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Màn hình | Form "Chỉnh sửa Tư vấn viên" (màn Sửa) | `/chuyen-gia-tvv/98cfd963…/chinh-sua`, TVV-BTP-TW-0002 | Không |
| Data / input | Ảnh chân dung định dạng `.png` hợp lệ | PNG hợp lệ 120×160, 429 B (`anh-chan-dung-qa.png`) | Không |
| Thao tác | Tải `.png` vào Ảnh chân dung → bấm Lưu → quan sát thông báo + kết quả lưu | Tải `.png` (chấp nhận, POST `/files?kind=avatar` → 201) → Lưu (PATCH TVV → 200) → điều hướng về Chi tiết; hồ sơ cập nhật thành công; NHƯNG ảnh chân dung không hiển thị: avatar là chữ "Q", GET `.../files/71bcd8f1…/download` → 404 (lặp lại sau khi tải lại trang) | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Reopen (fix một phần)**.
- ✅ Đã fix phần lỗi gốc: `.png` được chấp nhận, không còn báo "Chỉ chấp nhận file PDF"; bấm Lưu thành công, hồ sơ cập nhật (Mô tả kinh nghiệm + các trường đã lưu và hiển thị lại).
- ❌ Phát sinh cùng luồng: ảnh chân dung đã tải + lưu KHÔNG hiển thị sau khi lưu — màn Chi tiết vẫn hiện chữ viết tắt; endpoint tải ảnh vừa lưu trả 404 (tái hiện sau reload). ⇒ Người dùng tải ảnh, lưu được nhưng ảnh không bao giờ hiện.
