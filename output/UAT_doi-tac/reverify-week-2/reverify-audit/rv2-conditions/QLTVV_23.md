# Bảng đối chiếu điều kiện — QLTVV_23 (re-verify sau dev fix, 2026-07-15)

Re-test đúng vai trò/màn mà bug gốc mô tả (bug-report §Các bước tái hiện).

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Màn hình | Form "Chỉnh sửa Tư vấn viên" (màn Sửa) | `/chuyen-gia-tvv/98cfd963…/chinh-sua`, TVV-BTP-TW-0002 (Đang hoạt động) | Không |
| Nhóm trường | Nhóm "Nghề nghiệp" | Nhóm "Nghề nghiệp" (mở rộng) | Không |
| Thao tác kiểm | Xem có trường "Mô tả kinh nghiệm" không | Field có mặt (ô văn bản dài, 0/5000); nhập 63 ký tự OK | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Nhóm "Nghề nghiệp" của form Sửa nay CÓ trường "Mô tả kinh nghiệm" (ô văn bản dài tối đa 5000 ký tự) — nhập được và lưu được (đã lưu thành công, giá trị hiển thị lại ở màn Chi tiết). Trường "Chứng chỉ hành nghề" cũng đã có mặt.
