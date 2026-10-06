# Bug Report — Thông báo & Email (phát hiện thêm khi re-verify R10)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | https://18.143.165.120.nip.io · MailHog http://18.143.165.120:8025 |
| **Người test** | QA Automation (Claude Code) |
| **Ngày** | 2026-07-30 21:05:00 |
| **Loại test** | Bug phát hiện thêm khi re-verify 24 case đối tác (nhóm 7 case thông báo) |
| **Round** | Re-verify tuần 3 — R11 (2026-07-30 21:05; round trước: R10 cùng ngày) |
| **Tài liệu tham chiếu** | SRS v3.5 `srs-v3.5/srs-v3.5.md` §B.6b **BR-NOTIF-01** (dòng 5591 — bản chuẩn; bản cũ là dòng 5520) · `srs-v3.5/srs-fr-08-danh-gia.md:716` · [KET-QUA-reverify-24-case-reopent.md](../../dev-fix-reverify-round-10-2026-07-30/KET-QUA-reverify-24-case-reopent.md) |

---

**Nguồn SRS:** mọi trích dẫn dạng `srs-v3.5/<file>:<dòng>` lấy từ `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chuẩn duy nhất). Bản `input/srs-update-2026-5-5/` lệch số dòng ở chính các mục dưới đây (vd cùng nội dung "Đăng xuất thành công": bản chuẩn dòng 1011 · bản cũ dòng 1002) nên KHÔNG dùng để đối chiếu.

## Tổng hợp

> **Round hiện tại (LATEST) — R11 re-verify 2026-07-30 21:05: cả 2 bug đã fix → 2/2 Closed.** Cả hai đều được thử trên **dữ liệu MỚI sinh qua giao diện** (thông báo/thư cũ đã đóng băng từ trước khi dev sửa nên không dùng làm phép thử được).
> - `BUG-TB-MAIL-01` ✅ — trình rồi phê duyệt vụ việc `VV-BTP-TW-20260730-002` sinh 7 thư thuộc 2 loại tiêu đề từng lỗi; cả 7 mở đầu bằng đúng nội dung nghiệp vụ, không còn đoạn chú thích nội bộ của người soạn mẫu.
> - `BUG-TB-CAT-01` ✅ — từ chối báo cáo đánh giá `DG-20260725-0001` kèm lý do dài 150 ký tự; người nhận đọc thông báo trong hệ thống thấy **đủ lý do** (nội dung 457 ký tự, không còn dừng ở 200).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 2    | 0        | 0     | 1      | 1     | 0       | 2      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-TB-MAIL-01 | Medium | P2 | Data | (ngoài case — phát hiện khi verify PCNTHDG_11 / PDPCDG_01) | `BR-NOTIF-01 §Template` (`srs-v3.5/srs-v3.5.md:5591`) | Email gửi người dùng lọt chú thích nội bộ của mẫu thư ở đầu thân thư (29/120 email, 11 loại) | Closed |
| BUG-TB-CAT-01 | Minor | P3 | Data | (ngoài case — phát hiện khi verify PDPCDG_05 / PDBCDG_04) | `BR-NOTIF-01 §Sự kiện trigger (3) "Từ chối — TB người tạo, kèm lý do"` (`srs-v3.5/srs-v3.5.md:5591`) · `srs-v3.5/srs-fr-08-danh-gia.md:716` | Nội dung thông báo trong hệ thống bị cắt cứng ở 200 ký tự làm mất phần lý do từ chối | Closed |

---

## ~~BUG-TB-MAIL-01~~ [CLOSED] — Email gửi người dùng lọt chú thích nội bộ của mẫu thư

> **Re-test:** 2026-07-30 20:53 R11 — ✅ PASS (Closed-verified). Thư cũ trong hộp thư đã đóng băng từ trước khi dev sửa (thư nghiệp vụ gần nhất cách 5 tiếng) nên **sinh thư MỚI qua giao diện** để làm phép thử: `qa_tvvseed28` trình phê duyệt vụ việc `VV-BTP-TW-20260730-002` → 6 thư "Vụ việc chờ phê duyệt"; rồi `cbpd_tw_01` phê duyệt → 1 thư "Vụ việc đã được phê duyệt". **7/7 thư mới sạch**: thân thư mở đầu ngay bằng tiêu đề nghiệp vụ + dữ liệu vụ việc, không còn đoạn *"đã tự mô tả sự kiện … bỏ prefix cứng, hiển thị trung tính … }}"*. Kiểm cả bản thô của thư (giải mã quoted-printable) — 0/7 thư khớp mẫu chú thích hoặc cú pháp `{{`/`}}`. Hai loại tiêu đề này đều nằm trong 11 loại từng lỗi ở R10 (6 + 1 = 7/29 thư lỗi cũ). Ảnh: [image/TB-MAIL-01-r11-than-thu-sach-khong-con-chu-thich.png](image/TB-MAIL-01-r11-than-thu-sach-khong-con-chu-thich.png).

### Mô tả

Theo `srs-v3.5/srs-v3.5.md:5591` (Phụ lục B.6b, **BR-NOTIF-01**), khi entity workflow chuyển trạng thái có ý nghĩa với bên liên quan, hệ thống phải gửi thông báo **in-app + email** cho các đối tượng tương ứng, với **Template** quản lý tại entity `MAU_PHAN_HOI` hoặc cấu hình tại UC108; yêu cầu kiểm thử ghi trong chính dòng BR này là *"test template render đúng dữ liệu entity"*.

Thực tế, thân email gửi cho người dùng **mở đầu bằng một đoạn chú thích nội bộ của người soạn mẫu thư** (kèm cả dấu đóng biến `}}` của cú pháp template), trước cả tiêu đề nghiệp vụ. Người nhận đọc được nguyên văn ghi chú kỹ thuật này.

### Các bước tái hiện

1. Thực hiện bất kỳ thao tác workflow có gửi email theo BR-NOTIF-01 — ví dụ: `cbnv_tw` trình phê duyệt phân công đợt đánh giá `DG-20260730-0001`, hoặc `cbpd_tw_01` phê duyệt/từ chối phân công, hoặc trình phê duyệt vụ việc.
2. Mở hộp thư giả lập MailHog http://18.143.165.120:8025 (môi trường chưa tích hợp email thật), tìm thư vừa gửi.
3. Đọc **phần đầu thân thư**.

### Kết quả mong đợi

- Theo `srs-v3.5/srs-v3.5.md:5591` (BR-NOTIF-01 §Template): thân thư gửi người dùng chỉ chứa **nội dung nghiệp vụ đã render** từ mẫu thư (tiêu đề sự kiện + dữ liệu entity). Không được lọt chú thích của người soạn mẫu, cũng không được lọt cú pháp template chưa xử lý.

### Kết quả thực tế

- Thân thư mở đầu bằng đoạn: *"đã tự mô tả sự kiện (vd "Hồ sơ bị từ chối", "Hồ sơ chờ phê duyệt") nên bỏ prefix cứng, hiển thị trung tính đúng cho cả 3 nhánh. **}}**"* — rồi mới đến nội dung thật *"Phân công đánh giá đã được duyệt - DG-20260730-0001…"*.
- Quét **120 email gần nhất** trên MailHog: **29 email** lọt đoạn này, thuộc **11 loại tiêu đề**:

  | Số thư | Loại tiêu đề |
  |---|---|
  | 12 | Phân công đánh giá chờ phê duyệt |
  | 6 | Vụ việc chờ phê duyệt |
  | 3 | Đăng ký khóa học |
  | 1 | Phân công đánh giá đã được duyệt |
  | 1 | Phân công đánh giá bị từ chối |
  | 1 | Báo cáo đánh giá đã được phê duyệt |
  | 1 | Báo cáo đánh giá bị từ chối |
  | 1 | Vụ việc đã được phê duyệt |
  | 1 | Khóa học bị từ chối |
  | 2 | Câu hỏi đã được phê duyệt |

- Lỗi **không phụ thuộc entity** (đánh giá / vụ việc / đào tạo / hỏi đáp đều bị) ⇒ nằm ở mẫu thư dùng chung, không phải ở luồng của một module.

### Bằng chứng

- Nguyên văn đầu thư (giải mã quoted-printable, gỡ thẻ HTML), thư `2026-07-30T08:23:28` — *Phân công đánh giá đã được duyệt - DG-20260730-0001*:
  ```
  đã tự mô tả sự kiện (vd "Hồ sơ bị từ chối", "Hồ sơ chờ phê duyệt") nên bỏ prefix cứng,
  hiển thị trung tính đúng cho cả 3 nhánh. }} Phân công đánh giá đã được duyệt -
  DG-20260730-0001 Phân công đánh giá do bạn trình đã được phê duyệt: - Mã kế hoạch:
  DG-20260730-0001 - Đợt đánh giá: QA reverify R10 30-07 …
  ```
- Cách đo: `GET http://18.143.165.120:8025/api/v2/messages?limit=120` → giải mã `Content-Transfer-Encoding: quoted-printable` → khớp mẫu `(bỏ prefix cứng|hiển thị trung tính|\{\{|\}\}|đã tự mô tả sự kiện)` → 29/120 thư, đếm theo tiêu đề đã giải mã UTF-8.

---

## ~~BUG-TB-CAT-01~~ [CLOSED] — Nội dung thông báo trong hệ thống bị cắt ở 200 ký tự làm mất lý do từ chối

> **Re-test:** 2026-07-30 21:05 R11 — ✅ PASS (Closed-verified). Chạy lại đúng luồng gốc trên giao diện, dữ liệu MỚI (thông báo cũ đã đóng băng trước khi dev sửa): `cbpd_tw_01` **từ chối báo cáo đánh giá** đợt `DG-20260725-0001` với lý do dài **150 ký tự** → đăng nhập bằng **đúng người nhận** `cbnv_tw_04` (người trình báo cáo) mở hộp thông báo. Thông báo *"Báo cáo đánh giá bị từ chối - DG-20260725-0001"* (30/07/2026 20:59) hiển thị **trọn nội dung 457 ký tự**, đọc được **đủ lý do từ chối** tới chữ cuối *"…hay bi cat bot khi noi dung dai"*, kèm cả dòng trạng thái đợt sau khi từ chối — không còn dừng ở 200 ký tự. Danh sách thông báo còn có nút **Xem thêm / Thu gọn** để mở rộng nội dung dài. Đối chiếu chéo kênh thư điện tử: nội dung hai kênh trùng khớp, đều đủ lý do. Ảnh: [image/TB-CAT-01-r11-thong-bao-hien-du-ly-do-tu-choi.png](image/TB-CAT-01-r11-thong-bao-hien-du-ly-do-tu-choi.png).

### Mô tả

Theo `srs-v3.5/srs-v3.5.md:5591` (BR-NOTIF-01, §Sự kiện trigger mục **(3) Từ chối**): *"Từ chối — TB người tạo, **kèm lý do**"*, kênh gửi là **in-app + email**. Với module đánh giá, `srs-v3.5/srs-fr-08-danh-gia.md:716` gắn BR-NOTIF-01 vào bước *"Gửi thông báo CB NV kết quả phê duyệt"*.

Thực tế, thông báo **trong hệ thống** (in-app) bị cắt cứng ở **đúng 200 ký tự**, mà phần lý do từ chối lại nằm ở cuối nội dung ⇒ người nhận thông báo in-app **không đọc được lý do**, phải mở email mới biết. Kênh email và dữ liệu lưu trong hệ thống vẫn đủ, nên đây là lỗi riêng của kênh in-app.

### Các bước tái hiện

1. Đăng nhập `cbpd_tw_01` / `Test@1234` (CB Phê duyệt Trung ương) → từ chối **phân công đánh giá** của đợt `DG-20260730-0001` kèm lý do dài (~90 ký tự). Lặp tương tự với **từ chối báo cáo đánh giá** đợt `DG-20260722-0001`.
2. Đăng nhập bằng chính người nhận — `cbnv_tw` (CB Nghiệp vụ đã trình, có quyền xem hộp thông báo của mình) → mở hộp thông báo, hoặc gọi `GET /api/v1/thong-baos?page=1&pageSize=40`.
3. Đọc trọn nội dung thông báo tương ứng và đếm độ dài.

### Kết quả mong đợi

- Theo `srs-v3.5/srs-v3.5.md:5591` (BR-NOTIF-01 mục 3): thông báo từ chối gửi cho người tạo phải **kèm lý do từ chối**, ở **cả 2 kênh** in-app và email — người nhận đọc thông báo trong hệ thống là biết được vì sao bị từ chối.

### Kết quả thực tế

Đo trên hộp thông báo của **đúng người nhận** (`cbnv_tw`, phiên API riêng):

| Thông báo | Độ dài `noiDung` | Phần cuối nhận được |
|---|---|---|
| Phân công đánh giá bị từ chối — `DG-20260730-0001` | **200** (cắt) | `… - Lý do từ c` → **mất hẳn lý do** |
| Báo cáo đánh giá bị từ chối — `DG-20260722-0001` | **200** (cắt) | `… - Lý do từ chối: QA reverify R10 - tu choi de kiem` → mất phần sau |
| Phân công đánh giá đã được duyệt — `DG-20260730-0001` | **200** (cắt) | `… Đợt đánh giá đã chuyển sang trạng t` |
| Khóa học bị từ chối — `KH-20260730-001` | 93 (nguyên) | `… Lý do: QA seed: bo sung doi tuong, dia diem, so buoi hoc truoc khi duyet` ✅ |

→ Mọi nội dung dài hơn ngưỡng đều dừng ở **đúng 200 ký tự**, nội dung ngắn thì nguyên vẹn ⇒ giới hạn cứng 200 ký tự, không phải lỗi nội dung cụ thể.

### Bằng chứng

- Kiểm chứng bằng phương pháp thứ hai (so cùng nội dung ở kênh email — MailHog), lý do **đầy đủ**:
  ```
  2026-07-30T08:22:22 | Phân công đánh giá bị từ chối - DG-20260730-0001
     Lý do từ chối: QA reverify R10 - tu choi phan cong de kiem tra thong bao kem ly do
  2026-07-30T08:19:29 | Báo cáo đánh giá bị từ chối - DG-20260722-0001
     Lý do từ chối: QA reverify R10 - tu choi de kiem tra thong bao kem ly do cho CB nghiep vu
  ```
  ⇒ dữ liệu nguồn có đủ lý do; chỉ bản in-app bị cắt.
- Trích `GET /api/v1/thong-baos?page=1&pageSize=40` (người nhận `cbnv_tw`):
  ```
  2026-07-30T08:22:22 | Phân công đánh giá bị từ chối - DG-20260730-0001
      len(noiDung) = 200 · …'- Lý do từ c'
  2026-07-30T08:19:29 | Báo cáo đánh giá bị từ chối - DG-20260722-0001
      len(noiDung) = 200 · …'- Lý do từ chối: QA reverify R10 - tu choi de kiem'
  ```
