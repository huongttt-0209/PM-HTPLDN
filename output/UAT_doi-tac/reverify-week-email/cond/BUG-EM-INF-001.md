# Condition table — BUG-EM-INF-001 (R3)

| Điều kiện | Thao tác | Kỳ vọng | Thực tế | Kết quả |
|---|---|---|---|---|
| `cbnv_tw_01`; TVV `TVV-BTP-TW-0049`; bản ghi version 9 | PATCH `moTaCongKhai` với đủ 15 thẻ whitelist của EC-SEC-06a, mỗi thẻ mang hậu tố `-R3` | API chấp nhận và không xóa thẻ whitelist | PATCH 200, version 10 | PASS |
| Sau PATCH thành công | GET lại hồ sơ TVV | Còn đủ `<p>`, `<br>`, `<b>`, `<strong>`, `<i>`, `<em>`, `<u>`, `<ul>`, `<ol>`, `<li>`, `<a>`, `<h3>`, `<h4>`, `<blockquote>`, `<code>` | Giá trị đọc lại còn đủ 15 thẻ; link được bổ sung thuộc tính an toàn | PASS |
| Hoàn tất thu bằng chứng | PATCH trả dữ liệu fixture ban đầu với version mới nhất | Không để lại dữ liệu test R3 | PATCH 200, version 11; nội dung gốc đã được hoàn nguyên | PASS |

**Kết luận:** PASS — lỗi xóa 6 thẻ whitelist không còn tái hiện.

**Evidence:** [API GET sau PATCH](../bug-report/image/bug-em-inf-001-r3-all-whitelist-tags-preserved-2026-08-25.png) — SHA-256 `48224e810322a4ae5277a516f5348828df2411d7ef0a3acad09e4a36f5126cc5`.
