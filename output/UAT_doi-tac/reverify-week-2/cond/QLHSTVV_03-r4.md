# Bảng đối chiếu điều kiện — re-verify QLHSTVV_03 (row 58, mode reverify2, 30/07/2026)

Bug gốc (vòng 2): màn chi tiết hồ sơ tư vấn viên không tra được "Số quyết định công nhận", và còn
mục "Địa bàn" đã bị bỏ. BA chốt 30/07/2026: đưa "Số quyết định công nhận" lên THẺ ĐẦU TRANG cạnh
"Ngày công nhận" (SCR-IV-03 mục 3), KHÔNG đưa vào thẻ "Hồ sơ"; thẻ "Hồ sơ" 6 nhóm là đúng; bỏ "Địa bàn".

| Điều kiện | Bug gốc / CÁCH VERIFY yêu cầu | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản | `cbnv_tw` / Test@1234 | Đúng `cbnv_tw`. Phiên nhận việc đang là `nht_qa_tw` nên đã thoát phiên đúng cách rồi đăng nhập lại bằng `cbnv_tw` | Không |
| Màn hình | Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia → xem chi tiết | Đúng màn chi tiết hồ sơ | Không |
| Hồ sơ (A): đã phê duyệt/công nhận, có số QĐ thật, ĐÃ công khai | 1 hồ sơ | `TVV-BTP-TW-0002` "QA TVV Seed28 Active" — Đang hoạt động + cờ Công khai bật (danh sách hiện nhãn "Công khai", thẻ đầu trang có nút "Hủy công khai") + ngày công nhận 12/07/2026 + số quyết định `QD-SEED28-2026` | Không |
| Số QĐ của (A) phải là số THẬT của chính hồ sơ đó | CÁCH VERIFY mô tả dạng "QĐ-…/QĐ-BTP" | Số thật của bản ghi là `QD-SEED28-2026`; đã đối chiếu màn hình với dữ liệu gốc của chính bản ghi, khớp tuyệt đối. Không hạ FAIL vì lệch định dạng chữ — tiêu chí là "đúng số của chính hồ sơ đó" | Không |
| Hồ sơ (B): CHƯA qua phê duyệt | Mới đăng ký / Đang thẩm định | `TVV-BTP-TW-0023` — trạng thái "Mới đăng ký", chưa công khai, chưa có ngày công nhận | Không |
| Phải kiểm nhóm thứ 6 trên hồ sơ ĐÃ công khai (bẫy b) | Không kết luận tiêu chí (2) trên hồ sơ chưa công khai | Cố ý dùng (A) đã công khai để kết luận tiêu chí 6 nhóm; 5 nhóm ở (B) chưa công khai tính là ĐẠT tiêu chí (4b), không tính FAIL | Không |
| Cách đếm nhóm và tìm "Địa bàn" | Bung hết nhóm thu gọn rồi đếm | Đếm bằng truy vấn DOM, cả 6 nhóm của (A) đều bung sẵn; tìm chuỗi "Địa bàn" quét TOÀN trang chi tiết (không chỉ nhóm Tổ chức) để không bỏ sót nếu mục bị đẩy sang nhóm khác — 0 lần khớp trên cả 2 hồ sơ | Không |
| Phân biệt trường na ná (bẫy c) | Nhãn đúng ý nghĩa là đạt | Không quy kết "Số QĐ công bố" thành "Số quyết định (công nhận)" chỉ vì tên gần giống; đã chứng minh là 2 trường khác nhau bằng giá trị thực (một bên trống "—", một bên `QD-SEED28-2026`) | Không |
| Dữ liệu bị đụng | Chỉ đọc | Không seed, không sửa, không xóa; không bấm "Sửa hồ sơ" / "Cập nhật trạng thái" / "Hủy công khai" / "Bắt đầu thẩm định" | Không |
