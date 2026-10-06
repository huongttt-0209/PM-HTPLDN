# QLDMTCTV_05 — Evidence audit (re-verify vòng 1, tuần 3)

**Mã TC:** QLDMTCTV_05 · **Dòng sheet:** 318 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **QA:** QA Automation (Claude Code) · **Tool:** Chrome DevTools MCP
**Môi trường QA:** https://18.143.165.120.nip.io — bản dựng đọc ở chân menu: **`HTPLDN · V1.0.5`**
**Verdict tổng:** `Pass` (cột Q — Verify). Cột P giữ nguyên `dev done`.

## Note dev trước khi QA đè

(cột R rỗng tại 2026-08-03 — dev không để lại note)

---

## 1. Bằng chứng đối tác — đã xem gì, thấy gì

| Mục | Nội dung |
|---|---|
| File | `partner-evidence/QLDMTCTV_05.jpg` (1921×1041) |
| Cách xem | Mở FULL-RES bằng tool Read; cắt + phóng to ×3 riêng 2 vùng: thanh thẻ trạng thái và góc phải trên (vai trò) để đọc chắc chữ |
| URL trong ảnh | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc?trangThai=MOI_DANG_KY&page=1` |
| **Vai trò đọc được trong ảnh** | **"Cán bộ NV Trung ương" · `CB_NV_TW`** — phạm vi **`BTP · TW`** |
| Thời điểm máy đối tác | 2026-07-28 09:00 |
| Bản ghi trong ảnh | 1 dòng — `TC-BTP-TW-0009` "TKM", loại hình "Khác", đơn vị "Cục Bổ trợ tư pháp - Bộ Tư pháp", người đại diện "Tester TKM" |
| Thanh thẻ trong ảnh | 6 thẻ: Đang hoạt động · Chờ phê duyệt · Mới đăng ký (đang chọn) · Đã từ chối · Tạm dừng · Vô hiệu hóa — **không thẻ nào có số đếm, không thẻ nào có dấu đỏ** |

### 🔴 Dữ kiện quyết định về vai trò

Trước khi verify có giả thuyết (mượn từ case QLDMTCTV_02 kề bên) rằng ảnh đối tác có thể chụp ở vai trò **QTHT**, khi đó ý (c) sẽ là **so sai vai trò**. **Đã đọc ảnh và bác bỏ giả thuyết này:** góc phải trên ghi rõ `Cán bộ NV Trung ương` + mã vai trò `CB_NV_TW`. Đối tác chụp **đúng vai trò họ phản ánh**, nên ý (c) là so sánh **hợp lệ** và phải được verify nghiêm túc bằng 2 vai trò, không được gạt đi.

> Ghi chú: ảnh của case QLDMTCTV_02 (chụp 08:54 cùng ngày) là ảnh **khác**, chụp ở vai trò Quản trị viên. Hai case dùng 2 ảnh khác nhau — không suy vai trò của case này từ case kia.

## 2. Ba ý của case — lập luận từng ý

### Ý (a) — "Mỗi thẻ không hiển thị số đếm" → `Pass`

- **SRS:** `srs-fr-04-chuyen-gia-tvv.md` dòng **1625-1630** — cả 6 thẻ đều ghi loại UI **"tab + số đếm"**; dòng **1650** ghi "20 mục/trang; **hiển thị tổng mỗi tab**".
- **Đo được:** số đếm hiện trên thẻ và **khớp số bản ghi thực** — "Đang hoạt động" 3 ↔ bảng 3 dòng; "Mới đăng ký" 1 ↔ bảng 1 dòng; "Chờ phê duyệt" 1 ↔ bảng 1 dòng.
- **Phép thử phân biệt (chứng minh số đếm là động):** trước seed, thẻ "Mới đăng ký" **không có** số đếm và bảng **0 dòng**; sau seed 1 tổ chức + **tải lại trang bỏ qua bộ nhớ đệm**, thẻ hiện **"1"** và bảng **1 dòng**.
- **Kết luận:** triệu chứng đối tác báo (thẻ có dữ liệu mà không có số đếm) **không còn tái hiện**.
- **Sai lệch nhỏ ngoài phản ánh:** thẻ 0 bản ghi không hiện số "0" (ẩn huy hiệu khi bằng 0). Khác bản chất triệu chứng đối tác → không đổi verdict, ghi ở §4.
- **Ảnh:** `image/QLDMTCTV_05-cbnv-tw-04-thanh-the-truoc-khi-seed.png` (trước) · `image/QLDMTCTV_05-cbnv-tw-04-sau-seed-the-moi-dang-ky-so-dem-do.png` (sau).

### Ý (b) — "Thẻ Mới đăng ký không có nhãn đỏ" → `Pass`

- **SRS:** dòng **1627** — thẻ "Mới đăng ký", loại UI **"tab + số đếm + chấm đỏ nếu >0"**, nhãn "Tổ chức tư vấn mới do Cán bộ Nghiệp vụ tạo, chưa trình phê duyệt".
- **Tiền đề ban đầu THIẾU:** đầu phiên thẻ "Mới đăng ký" **rỗng** (bản ghi `TC-BTP-TW-0001` của phiên QA trước đã được trình phê duyệt nên đã rời sang thẻ "Chờ phê duyệt"). Theo §Nguyên tắc 4 → **TỰ SEED**, không lấy làm blocker và không kết luận khi thẻ rỗng.
- **Đã seed:** tạo `TC-BTP-TW-0002` "Trung tam Tu van QA Kiem Cham Do 0803" qua giao diện bằng chính `cbnv_tw_04`, **cố ý KHÔNG trình phê duyệt** để giữ đúng trạng thái "Mới đăng ký" như tình huống đối tác.
- **Đo được sau seed + tải lại trang:** huy hiệu thẻ "Mới đăng ký" = **"1" trên nền ĐỎ** `rgb(245, 34, 45)`; cùng lúc thẻ "Đang hoạt động" = "3" trên nền **xanh** `rgb(9, 88, 217)`. Dấu hiệu đỏ **chỉ bật cho đúng thẻ** và **chỉ khi > 0** (khi = 0 thì không có huy hiệu nào).
- **Cách hiện thực khác đặc tả về hình thức:** dấu đỏ được **gộp vào chính huy hiệu số đếm** (huy hiệu nền đỏ mang số) thay vì vẽ thêm một chấm tròn riêng bên cạnh. Dòng 1627 đòi 2 thứ — số đếm + dấu đỏ khi > 0 — và **cả 2 đều đang được đáp ứng**; chỉ khác cách trình bày. Theo nguyên tắc mô tả yêu cầu chứ không áp đặt cách làm, đây **không** phải lỗi.
- **Kết luận:** triệu chứng đối tác báo **không còn tái hiện** — nay CÓ dấu hiệu đỏ khi tồn tại tổ chức chưa trình duyệt.
- **Ảnh:** `image/QLDMTCTV_05-seed-form-them-moi-truoc-khi-luu.png` · `image/QLDMTCTV_05-cbnv-tw-04-sau-seed-the-moi-dang-ky-so-dem-do.png` · `image/QLDMTCTV_05-the-moi-dang-ky-sau-seed-1-ban-ghi-chua-trinh-duyet.png`.

### Ý (c) — "Thẻ Chờ phê duyệt hiển thị đối với CBNV" → `Pass`

- **SRS:** dòng **1628** — cột "Label / Dữ liệu hiển thị" ghi *"Hiển thị khi vai trò là Cán bộ Phê duyệt"*; dòng **1615** (Quyền truy cập) ghi *"Cán bộ Phê duyệt cùng đơn vị: xem + phê duyệt/từ chối tab 'Chờ phê duyệt'"*.
- **Đo trên 2 vai trò cùng cấp cùng đơn vị, 2 phiên trình duyệt cách ly hoàn toàn:**

| Vai trò / tài khoản | Số thẻ | Danh sách thẻ (nguyên văn `innerText`) | Có "Chờ phê duyệt"? |
|---|:-:|---|:-:|
| CB Nghiệp vụ TW — `cbnv_tw_04` (trùng vai trò ảnh đối tác) | **5** | Đang hoạt động `3` · Mới đăng ký `1` · Đã từ chối · Tạm dừng · Vô hiệu hóa | **KHÔNG** |
| CB Phê duyệt TW — `cbpd_tw_04` (cùng đơn vị `BTP · TW`) | **6** | Đang hoạt động `3` · Chờ phê duyệt `1` · Mới đăng ký `1` · Đã từ chối · Tạm dừng · Vô hiệu hóa | **CÓ** |

- Bấm thẻ "Chờ phê duyệt" ở vai trò CB Phê duyệt → lọc ra đúng `TC-BTP-TW-0001`, cột Trạng thái = "Chờ phê duyệt".
- **Kết luận:** triệu chứng đối tác báo **không còn tái hiện**; hành vi hiện tại khớp dòng 1628 + 1615.
- **Lưu ý phương pháp:** vì đây là kết luận **phân quyền**, mỗi vai trò được chạy trong **một ngữ cảnh trình duyệt cách ly riêng** (kho cookie + bộ nhớ cục bộ tách hẳn), mạnh hơn thao tác đăng xuất thông thường — loại trừ triệt để rủi ro dính phiên cũ gây kết luận phân quyền sai.
- **Ảnh:** `image/QLDMTCTV_05-cbnv-tw-04-sau-seed-the-moi-dang-ky-so-dem-do.png` (5 thẻ) · `image/QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png` (6 thẻ).

### Lọc theo thẻ (vế "Hệ thống lọc danh sách theo trạng thái tương ứng")

Bấm lần lượt cả 6 thẻ: địa chỉ trang đổi thành `?trangThai=<mã trạng thái>` và bảng chỉ còn dòng đúng trạng thái — "Đang hoạt động" 3 dòng đều "Đang hoạt động"; "Mới đăng ký" → `TC-BTP-TW-0002`; "Chờ phê duyệt" → `TC-BTP-TW-0001`; 3 thẻ còn lại không có bản ghi. ✅ Đúng.

## 3. 🔴 Mâu thuẫn nội tại trong SRS (đã tự mở đọc xác minh cả 2 chỗ)

- **Dòng 1610:** "Loại màn hình: Danh sách **6 tab** + thao tác hàng loạt…"
- **Dòng 1617:** "Hiển thị **6 tab** phân loại theo trạng thái lifecycle."
- **Dòng 1625-1630:** liệt kê chi tiết đúng **6 thẻ**.
- **Dòng 1129** (Acceptance Criteria của FR-IV-NEW-01): "**Then** danh sách TC TV thuộc đơn vị, **3 tab** trạng thái."

⇒ Cùng một tài liệu vênh nhau **6 tab vs 3 tab**. Web làm theo phần đặc tả màn hình (6 thẻ, ẩn bớt 1 thẻ theo vai trò). **Không dùng mâu thuẫn này để chấm case** — cả 3 ý đều đo theo mô tả chi tiết từng thẻ (dòng 1625-1630) và đều đạt. Nhưng nên đưa BA chốt lại con số để tài liệu khỏi lệch.

**Về mã tham chiếu:** FR gốc `FR-IV-NEW-01` (dòng **1027**) có dòng **1029** ghi `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])` → **SRS KHÔNG cấp mã UC cho chức năng này**. Note gửi đối tác vì thế không trích mã UC (và vì verdict là `Pass` nên note chỉ dùng tên chức năng + lời văn, không kèm mã FR/số dòng).

## 4. Ngoài phạm vi case — phát hiện thêm (chưa log, chờ user quyết)

1. **Thẻ "Chờ phê duyệt" không chuyển đỏ khi > 0.** Dòng **1628** quy định thẻ này cũng là "tab + số đếm + **chấm đỏ nếu >0**". Thực tế với `cbpd_tw_04`, thẻ đang có 1 bản ghi nhưng huy hiệu vẫn **nền xanh** `rgb(9, 88, 217)`; chỉ thẻ "Mới đăng ký" mới đỏ. Đây là **thẻ khác** với thẻ đối tác phản ánh ở ý (b) nên không tính vào verdict case này. Đáng chú ý vì xét theo vai trò thì "Chờ phê duyệt" mới là việc cần xử lý của Cán bộ Phê duyệt.
2. **Thẻ 0 bản ghi không hiện số "0"** — dòng **1650** ghi "hiển thị tổng mỗi tab". Người dùng không phân biệt được "0 bản ghi" với "chưa làm số đếm".
3. **Thứ tự thẻ khác SRS.** SRS (1625-1630): Đang hoạt động → Tạm dừng → Mới đăng ký → Chờ phê duyệt → Đã từ chối → Vô hiệu hóa. Web: Đang hoạt động → Chờ phê duyệt → Mới đăng ký → Đã từ chối → Tạm dừng → Vô hiệu hóa.
4. **Màn hình rỗng hiện chữ "Trống"**, trong khi dòng **1649** mô tả phải là "Chưa có tổ chức tư vấn nào trong mục này" + nút "+ Thêm tổ chức tư vấn" (chỉ ở thẻ Mới đăng ký).

> Cả 4 mục đều **không** ghi vào sheet đối tác (sheet này chỉ dùng để chấm verdict các case đã có). Chờ user quyết cách chuyển tới dev.

## 5. Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js` — không lọc trùng, đọc bằng `innerText`; **tự kiểm `soObserverDangSong = 1`** trước khi tin số liệu.
- Thao tác seed đo kèm số request: **1 request** `POST /api/v1/to-chuc-tu-vans` ↔ **1 khung thông báo** "Tạo Tổ chức tư vấn thành công" → không có thông báo lặp, không tạo trùng bản ghi.
- **Mọi bước đổi trạng thái (kể cả seed) đều có ảnh và ảnh đã được MỞ RA ĐỌC**, không chỉ lưu.
- Bảng điều khiển trình duyệt: **0 lỗi, 0 cảnh báo**. Các lệnh gọi máy chủ: 200/304 (riêng `GET /api/v1/auth/me` 401 là lần dò trước khi đăng nhập, bình thường).
- **Một phép đo đã nói dối và đã bị bắt:** script đọc ô "Loại hình" trả về **rỗng** sau khi đã chọn giá trị. Kiểm lại bằng mã HTML gốc của ô thì giá trị "Trung tâm Tư vấn Pháp luật" vẫn nằm đúng chỗ — ứng dụng dùng lớp CSS riêng `.ant-select-content-value` chứ không phải lớp mặc định mà script tra. ⇒ **selector của QA sai, không phải lỗi ứng dụng** → không log (đúng bài học §4 của postmortem: đọc HTML thô của ô đó trước khi kết luận).

## 6. Danh sách ảnh đã chụp và đã đọc

| Ảnh | Nội dung đã đọc được trong ảnh |
|---|---|
| `image/QLDMTCTV_05-cbnv-tw-04-thanh-the-truoc-khi-seed.png` | Vai trò `CB_NV_TW`, `BTP · TW`; 5 thẻ; chỉ "Đang hoạt động" có huy hiệu xanh `3`; "Mới đăng ký" trống trơn |
| `image/QLDMTCTV_05-seed-form-them-moi-truoc-khi-luu.png` | Form "Thêm mới Tổ chức tư vấn" đã điền tên/người đại diện/lĩnh vực trước khi bấm Lưu |
| `image/QLDMTCTV_05-cbnv-tw-04-sau-seed-the-moi-dang-ky-so-dem-do.png` | 5 thẻ; "Đang hoạt động" huy hiệu **xanh** `3`; "Mới đăng ký" huy hiệu **ĐỎ** `1`; vẫn không có thẻ "Chờ phê duyệt" |
| `image/QLDMTCTV_05-the-moi-dang-ky-sau-seed-1-ban-ghi-chua-trinh-duyet.png` | Thẻ "Mới đăng ký" đang chọn, huy hiệu đỏ `1`, bảng 1 dòng `TC-BTP-TW-0002` — bố cục đối chiếu trực tiếp được với ảnh đối tác |
| `image/QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png` | Vai trò `CB_PD_TW`; **6 thẻ**, có "Chờ phê duyệt" huy hiệu xanh `1`; "Mới đăng ký" huy hiệu đỏ `1` |
