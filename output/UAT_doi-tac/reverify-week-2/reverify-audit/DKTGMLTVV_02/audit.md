# Audit verify vòng 2 — DKTGMLTVV_02 (row 52, tab tuần 2)

**Verdict:** `Reject` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/DKTGMLTVV_02-r2.md`](../../cond/DKTGMLTVV_02-r2.md)

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `DKTGMLTVV_02_v2.jpg` (212.005 byte, ảnh tĩnh 1 khung hình) |
| Nội dung thấy trong ảnh | Form Thêm mới TVV, nhóm "Thông tin cá nhân" mở, hiện lần lượt: Loại (Tư vấn viên (TVV)) · Ảnh chân dung · Họ tên · Ngày sinh · Giới tính. **Vùng nhìn dừng tại "Giới tính"** — ảnh cắt ngay trên thanh taskbar Windows |
| **Ảnh KHÔNG chứa vùng có lỗi** | Trường "Đơn vị quản lý" nằm ở **cuối nhóm 1**, sau Số CMND/CCCD → Email → Số điện thoại → Địa chỉ. Tức còn **5 trường nữa** bên dưới mép ảnh. Ảnh không chụp tới đó nên không thể hiện được điều đối tác khẳng định là thiếu |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi` · (b) vai trò NHT, badge **"BTP · DP"** · (c) 2026-07-25 15:18 |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Hiển thị / trường thiếu)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:1494` — SCR-IV-02 mục **2.11**: "Đơn vị quản lý * \| ô văn bản (chỉ đọc) \| Hiển thị tên đơn vị của Người hỗ trợ đang đăng nhập (auto-set, không sửa được). Ghi chú: NHT chỉ đăng ký TVV trong phạm vi đơn vị mình theo BR-AUTH-08" | Trường **CÓ mặt**, đúng vị trí cuối nhóm 1 (mục 2.11, ngay sau "Địa chỉ" = mục 2.10), là ô văn bản **chỉ đọc + khoá** (`readOnly=true`, `disabled=true`), **tự điền đúng đơn vị** của tài khoản đang đăng nhập | **Đủ** |
| `srs-fr-04-chuyen-gia-tvv.md:1474` — SCR-IV-02 §Mô tả: "`don_vi_id` auto-set theo đơn vị NHT đang đăng nhập" | `nht_qa_tw` → "Cục Bổ trợ tư pháp - Bộ Tư pháp"; `nht_qa_01` → "Sở Tư pháp An Giang" ⇒ auto-set chạy đúng theo tài khoản | **Đủ** |

⇒ Web **đúng đặc tả**. Lỗi đối tác báo **không tồn tại** trên bản hiện tại, với đúng vai trò và đúng đơn vị của họ.

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Đăng nhập `nht_qa_tw` (NHT, badge "BTP · TW") → `/chuyen-gia-tvv/tao-moi` → mở hết 6 nhóm thu gọn → đọc **toàn bộ nhãn** bằng DOM (không phụ thuộc vùng nhìn) | 30 nhãn, nhóm 1 gồm 12 nhãn: Loại · Ảnh chân dung · Họ tên · Ngày sinh · Giới tính (Nam/Nữ) · Số CMND/CCCD · Email · Số điện thoại · Địa chỉ · **Đơn vị quản lý** | `DKTGMLTVV_02-r2-nht-tw-co-don-vi-quan-ly.png` |
| 2 | Đo thuộc tính của chính ô "Đơn vị quản lý" | `readOnly = true`, `disabled = true`, giá trị tự điền **"Cục Bổ trợ tư pháp - Bộ Tư pháp"**, vị trí cuối nhóm 1 (cách đỉnh trang 1162 px — dưới mép ảnh của đối tác) | — |
| 3 | **Đối chứng đúng badge đơn vị của đối tác** — đăng nhập `nht_qa_01`, header hiện **"BTP · DP"** (trùng khít ảnh đối tác) | Trường vẫn có mặt, vẫn chỉ đọc, tự điền **"Sở Tư pháp An Giang"**; nhóm 1 vẫn đủ 12 nhãn | `DKTGMLTVV_02-r2-nht-btp-dp-co-don-vi-quan-ly.png` |

**Vì sao là `Reject` chứ không phải `Resolved`:** `Resolved` chỉ dùng khi lỗi không tái hiện **nhưng đối tác có bằng chứng lỗi thật**.
Ở đây ảnh của đối tác **không chứa vùng đang tranh chấp** — khung hình dừng ở "Giới tính", còn "Đơn vị quản lý" nằm dưới đó 5 trường.
Ảnh không chứng minh được sự vắng mặt của trường, nên không có "bằng chứng lỗi thật" để áp `Resolved`. Cộng với việc web đáp ứng đúng
đặc tả ở đúng vai trò + đúng đơn vị của đối tác ⇒ theo QA_VERIFY_PROTOCOL §Verdict, đây là trường hợp "web chạy đúng SRS, lỗi đối tác
báo không có thật / báo cáo vô hiệu" → `Reject`.

**Vì sao KHÔNG phải `BA confirm`:** không có bất đồng về đặc tả — SRS quy định rõ trường này và web làm đúng. Không có mâu thuẫn nguồn nào cần BA chốt.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có 1 điểm nhỏ, KHÔNG log bug:** SRS `:1494` ghi nhãn có dấu sao bắt buộc ("Đơn vị quản lý *") nhưng web hiển thị nhãn **không có dấu sao đỏ**.
Đây là trường chỉ đọc + tự điền, người dùng không thể bỏ trống, nên dấu sao chỉ mang tính trang trí và không ảnh hưởng nghiệp vụ.
Ghi nhận để BA quyết khi rà soát đồng bộ nhãn, không đưa vào note gửi đối tác (tránh làm loãng kết luận chính).

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Không tạo dữ liệu:** chỉ mở form và đọc nhãn, không bấm Lưu — không phát sinh bản ghi TVV nào trên env.
- **Badge "BTP · DP" của `nht_qa_01`:** tài khoản này thuộc Sở Tư pháp An Giang nhưng badge hiển thị "BTP · DP". Trùng với badge trong ảnh đối tác,
  nên dùng làm đối chứng là hợp lệ. Cách app dựng chuỗi badge (mã Bộ + cấp) không thuộc phạm vi case này.
- **Vòng 1 của case này** đã có kết luận BA 15/07/2026 về trường "Loại" (giữ 2 giá trị) — không liên quan claim vòng 2, không đụng tới.
