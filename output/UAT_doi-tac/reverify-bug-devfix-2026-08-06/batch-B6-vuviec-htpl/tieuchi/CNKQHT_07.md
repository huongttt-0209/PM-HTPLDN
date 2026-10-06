Mã case: CNKQHT_07 (dòng 62, tab `bug`)          Thời điểm viết: 2026-08-06 13:07
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** — dấu vân tay tự đo lúc 15:26 và đo lại lúc 16:05 ngày 06/08/2026: tệp bó mã `assets/index-DIABnbIr.js` · `GET /` trả `last-modified: Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · `etag: "6a74340b-428"` · `/api/docs-json` → `info.version 1.0.0`. Trùng bản dựng của case 51 cùng đợt; **khác** bản dựng case 45 + 50 (`assets/index-CNwX9JjX.js`, last-modified 06/08 02:51:16 GMT, etag `"6a73f6a4-428"`) vì bản dựng được thay giữa đợt.

> **Phạm vi verdict (đọc TRƯỚC khi chấm).** Đối tác chỉ phản ánh **vế (c)** ("CBNV không nhận được thông báo").
> Theo flow §Ca biên, verdict của case **chỉ do vế (c)** quyết định. Nếu giai đoạn B thấy (a)/(b)/(d) cũng lệch
> thì đó là **PHÁT HIỆN MỚI**, xử riêng — trái đặc tả nói rõ → log lỗi mới; đặc tả im lặng → thêm 1 mục hỏi BA.
> **Không kéo verdict của case.** Ngoại lệ duy nhất: phát hiện mới làm sai lệch chính phép đo của vế (c)
> (ví dụ (b) hỏng tới mức bản ghi kết quả không được tạo → sự kiện sinh thông báo không xảy ra) ⇒ chưa chốt được, đo lại.

> **Khai báo hồ sơ QA đợt trước đã đọc** (bắt buộc theo flow, dòng 88-90): đã đọc
> `reverify-week-3/uat-luong3-2026-08-04/cond/CNKQHT_07.md`, `.../cases/CNKQHT_07.md`,
> `.../reverify-audit/CNKQHT_07-vong2.md`. Các file đó chứa **số đo cũ** (bản dựng `index-DpIXRGaI.js` · V1.0.5,
> ngày 04/08/2026, bản ghi `VV-BTP-TW-20260525-001`, đếm 453→455 mục). **Mục 4 dưới đây suy từ ĐẶC TẢ, không lấy
> số đo cũ làm ngưỡng.** Riêng 2 điểm từ hồ sơ cũ chỉ dùng làm *cảnh báo bẫy*, không dùng làm tiêu chí:
> ① đợt trước xác định người nhận bằng `nguoiTiepNhanId` — đó là **giả thuyết**, giai đoạn B phải tự dựng để xác minh;
> ② đợt trước **không có bằng chứng kênh email** (chỉ đo in-app + đếm API) ⇒ kênh email lần này bắt buộc đo thật.

---

## 1. Đối tác phản ánh

Kết quả mong đợi của đối tác gồm **4 vế**; cột "Đối tác thực sự nêu" quyết định phạm vi verdict:

| Vế | Nội dung kỳ vọng của đối tác | Đối tác thực sự nêu? |
|:--:|---|:--:|
| (a) | Hệ thống hiển thị thông báo "Đã cập nhật kết quả hỗ trợ" và làm mới Nhóm 6 | ❌ Không nêu |
| (b) | Lưu nội dung, tệp và ghi chú vào hồ sơ | ❌ Không nêu |
| **(c)** | **Gửi thông báo cho cán bộ nghiệp vụ phụ trách để xem xét và chuẩn bị trình phê duyệt** | ✅ **CÓ — vế duy nhất** |
| (d) | Lưu vết thao tác theo quy định | ❌ Không nêu |

**Ô "Kết quả thực tế" của đối tác:** *"CBNV không nhận được thông báo"* → khớp duy nhất vế (c).
**Trạng thái trên bảng:** Fail · Dopai `dev done` · Trạng thái dev fix `Fixed` · ô "Kết quả verify" đang TRỐNG (chưa qua vòng verify nào trên tab `bug`).

### Bằng chứng — tệp + frame ĐÃ MỞ XEM

Tệp: `partner-evidence/CNKQHT_07.webm` (13.831.283 byte, ~57 giây).
Frame đã trích + đã mở xem: `partner-evidence/frames-CNKQHT_07/` (19 frame mỗi 3 giây + 26 frame mỗi 0,5 giây ở 2 khoảng 13-18s và 31-39s).

| Mốc giây | Frame | Thấy gì |
|---|---|---|
| 00:00 | `t000.00s.jpg` | Hộp thoại **"Cập nhật kết quả hỗ trợ"** (Nội dung kết quả 0/10000 · vùng "Tệp kết quả hỗ trợ" · Ghi chú) trên `htpldn-uat.ospgroup.vn/vu-viec/fa942aa3-e2a4-4608-be31-ec55a1f1cef9`. Góc phải: `huongcg` · **TVV · CG** · BTP·TW, chuông badge 23. Sidebar ghi bản dựng **HTPLDN · V1.0.2**. |
| 00:12 | `t012.10s.jpg` | Đã gõ nội dung `TVV cập nhật kết quả` (20/10000). **Vùng "Tệp kết quả hỗ trợ" VẪN TRỐNG** (chưa đính kèm tệp nào), ô Ghi chú vẫn trống. |
| **00:14,56** | `t014.56s.jpg` | Toast xanh **"Đã cập nhật kết quả"** ở đầu màn. Hộp thoại đóng. Tiêu đề: **VV-BTP-TW-20260511-001** — "INVESTIGATE-NOTIF-01-170214", nhãn **Đang xử lý**, stepper đang ở bước **6 Đang xử lý**, badge "Quá hạn nghiêm trọng · 41 ngày LV". Nội dung yêu cầu: *"Probe NOTIF-01 listener at 170214 UTC for hypothesis test on UC62"*. Lĩnh vực Thuế · Ngày tiếp nhận 11/05/2026. |
| 00:16-00:17 | `t016.72s.jpg`, `t018.12s.jpg` | Mở menu tài khoản → **Đăng xuất** → hộp xác nhận đăng xuất. |
| 00:24 | `t024.14s.jpg` | MailHog của env đối tác (`htpldn-uat.ospgroup.vn/mailhog/`, Inbox 205). Đầu danh sách: "Mã xác thực đăng nhập" → `cbnv_tw@htpldn.gov.vn` (a few seconds ago) — tức đang lấy OTP để đăng nhập, **không phải** đang kiểm thư thông báo. Đáng chú ý: thư cũ **"Người hỗ trợ đã xác nhận tham gia vụ việc - VV-BTP-TW-20260511-001"** (cùng vụ việc) gửi tới **`cb_nv_tw_03@htpldn.test`**, 14 phút trước. |
| 00:30 | `t030.17s.jpg` | Màn nhập mã xác thực: *"Mã 6 chữ số đã gửi đến email **cbn\*\*\*@htpldn.gov.vn**"* → tài khoản đang đăng nhập dùng hộp thư `@htpldn.gov.vn`. |
| **00:36,20** | **`t036.20s.jpg` — KHOẢNH KHẮC QUYẾT ĐỊNH** | Đã vào `/dashboard` với tài khoản **"Cán bộ NV Trung ương · CB_NV_TW"**, chuông badge **99+**, **hộp thả xuống "Thông báo" đang mở**. Toàn bộ 5 mục nhìn thấy: 4× *"Tài khoản vừa đăng nhập ở nơi khác"* (vài giây trước / một giờ trước / 15 giờ trước / 18 giờ trước) + 1× *CT HTPL "Chương trình kế hoạch có file đí…"* (2 ngày trước). **KHÔNG có mục nào nhắc VV-BTP-TW-20260511-001 hay việc cập nhật kết quả** — trong khi mục đầu danh sách là "vài giây trước" ⇒ danh sách đang xếp mới-nhất-trước và mục kỳ vọng lẽ ra phải nằm ngay đầu. |
| 00:39-00:54 | `t039.20s.jpg`, `t045.23s.jpg`, `t054.43s.jpg` | Đuôi video: về danh sách Vụ việc HTPL rồi mở một vụ việc **khác** (VV-BTP-TW-20260514-002, "Đã tiếp nhận"). Không liên quan vế (c). |

**Bằng chứng ĐÚNG case này** — hộp thoại đúng tên "Cập nhật kết quả hỗ trợ", vụ việc đúng trạng thái "Đang xử lý", và khoảnh khắc lỗi (mở chuông thấy không có thông báo) đều khớp mô tả + bước của CNKQHT_07. Không phải case khác.

**Hai điều bằng chứng KHÔNG cho biết → thành GAP phải đóng ở giai đoạn B:**
1. **Ai là "CBNV phụ trách" của VV-BTP-TW-20260511-001.** Video không mở Nhóm 5 (Phân công) / Dòng thời gian nên không thấy ai tiếp nhận, ai phân công, ai tạo vụ việc. ⇒ **không chứng minh được** tài khoản mở chuông (hộp thư `@htpldn.gov.vn`) chính là người kỳ vọng nhận. Dấu hiệu ngược chiều: thư hệ thống trước đó **của cùng vụ việc này** lại gửi tới `cb_nv_tw_03@htpldn.test` (mốc 00:24) — hai hộp thư khác nhau ⇒ **có khả năng đối tác mở nhầm hộp thông báo**. Đây đúng là bẫy flow cảnh báo ("X phải nhận thông báo" → kiểm nhầm người).
2. **Kênh email sau thao tác.** Đối tác mở MailHog ở 00:24 là để lấy OTP, **không** quay lại kiểm thư sau khi cập nhật ⇒ kênh email chưa được đối tác kiểm có chủ đích.

**Ghi nhận thêm (không kéo verdict, chỉ để giai đoạn B không hiểu nhầm bước):** bước 3 của đối tác ghi *"Nhập nội dung và tải tệp"* nhưng frame 00:12 cho thấy **không đính kèm tệp nào**. Giai đoạn B vẫn phải chạy đúng bước có tệp (xem mục 4).

---

## 2. Đặc tả nói gì

**Nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
FR chi phối: **FR-V.I-15 (UC65) — Người được phân công cập nhật kết quả hỗ trợ**, `srs-fr-05-vu-viec.md:1075`.

### Vế (c) — đặc tả NÓI RÕ và KHỚP kỳ vọng đối tác

| Trích | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1087` | `| PRE-02 | VV ở trạng thái DANG_XU_LY, tài khoản hiện tại là `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id` của phân công đã chấp nhận |` |
| **`srs-fr-05-vu-viec.md:1106`** | `| 5 | Gửi thông báo CB NV | — |` (Processing bước 5) |
| **`srs-fr-05-vu-viec.md:1114`** | `- CB NV nhận thông báo để review` (Postconditions) |
| **`srs-fr-05-vu-viec.md:1125`** | `- **Given** người được phân công nhập nội dung + upload tài liệu **When** lưu **Then** cập nhật, thông báo CB NV` (AC) |
| `srs-fr-05-vu-viec.md:1110` | `**Outputs:** Không có output riêng (KET_QUA_VU_VIEC được cập nhật, thông báo gửi CB NV).` |

**Kênh — đặc tả CHỐT 2 kênh:**

| Trích | Nguyên văn |
|---|---|
| **`srs-fr-05-vu-viec.md:2480`** | `Mọi sự kiện workflow (phân công, xác nhận, từ chối, phê duyệt, hoàn thành, công khai, bổ sung hồ sơ, cảnh báo SLA) đều gửi thông báo cho người liên quan qua 2 kênh: in-app (THONG_BAO) + email. Người nhận xác định theo loại sự kiện.` (BR-NOTIF-01) |
| **`srs-fr-05-vu-viec.md:2482`** | `**Applied in (nhóm V.I):** FR-V.I-04, FR-V.I-09, FR-V.I-10, FR-V.I-12, FR-V.I-13, **FR-V.I-15**, FR-V.I-16, FR-V.I-NEW-02, FR-V.I-NEW-05, FR-V.I-CROSS-01` |
| `srs-fr-05-vu-viec.md:2337` | `| BR-NOTIF-01 | Quy tắc gửi thông báo | FR-V.I-04, 09, 10, 12, 13, **15**, 16, NEW-02, NEW-05, CROSS-01 |` |
| **`srs-v3.5.md:739`** | `| INT-06 | Email Server (SMTP) | Gửi email thông báo: phê duyệt, phân công, cảnh báo SLA, kích hoạt TK, đặt lại MK. SLA: gửi trong ≤ 5 phút | Email HTML (To, Subject, Body, Attachments optional) | Cross-cutting (mọi UC có notification) |` |

**Nơi đọc thông báo in-app (để mục 4 đo đúng chỗ):**

| Trích | Nguyên văn |
|---|---|
| `srs-v3.5.md:618` | `| Chuông thông báo (🔔) | Phải | Số đếm + danh sách thông báo thả xuống. Có link "Xem tất cả thông báo" → Trang Danh sách Thông báo (§3.1.1.3) |` |
| `srs-v3.5.md:704` | `**Đường dẫn:** `/thong-baos` — truy cập từ Chuông thông báo (🔔) trên thanh trên → "Xem tất cả thông báo".` |
| `srs-v3.5.md:706` | `**Nguồn dữ liệu:** entity `THONG_BAO` (§3.4.3.15), lọc theo người dùng đăng nhập (BR-AUTH-01). Mỗi vai trò chỉ thấy thông báo của chính mình.` |
| `srs-v3.5.md:716` | Thẻ thông báo gồm: chấm đỏ (chưa đọc), `tieu_de` in đậm, nhãn `loai`, thời điểm tuyệt đối + tương đối, `noi_dung` |
| `srs-v3.5.md:721` | `- Danh sách sắp xếp **mới nhất trước** theo thời điểm tạo (BR-DATA-07).` |
| `srs-v3.5.md:718` | Phân trang **20 bản ghi/trang** khi tổng > 20 |

### Các vế đối tác KHÔNG nêu — chỉ ghi để giai đoạn B nhận diện, không chấm

- Vế (b): `srs-fr-05-vu-viec.md:1094-1096` (Inputs `noi_dung_ket_qua` ≤10.000 ký tự bắt buộc · `file_ket_qua` tùy chọn · `ghi_chu` tùy chọn) và `:1104-1105` (bước 3 "Tạo/cập nhật KET_QUA_VU_VIEC", bước 4 "Lưu tài liệu kết quả"); thành phần Accordion 6 tại `:1732`.
- Vế (d): `srs-fr-05-vu-viec.md:1107` (`| 6 | Ghi lịch sử | — |`) + `:1108` (`| 7 | Ghi nhật ký thao tác | BR-DATA-05 |`); định nghĩa BR-DATA-05 tại `:2386-2388` — *"Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Log là immutable, không sửa/xóa."*
- Nút thao tác: `srs-fr-05-vu-viec.md:1747` — `| DANG_XU_LY | [Cập nhật Kết quả] | Người được phân công/CB NV | Mở Accordion 6 để cập nhật |`.

### IM LẶNG về — CẤM chấm Fail vì những điều này

1. **Ai chính xác là "CB NV" nhận thông báo.** FR-V.I-15 (`:1106`, `:1114`, `:1125`) chỉ ghi **"CB NV"** trơn. Các FR khác dùng cụm **"CB NV phụ trách"** (`:419`, `:997`, `:1293`, `:2444`) nhưng **không nơi nào trong SRS định nghĩa "phụ trách" = người tiếp nhận (`nguoi_tiep_nhan_id`, `:2022`) hay người phân công hay người tạo hay mọi CB NV cùng đơn vị**. ⇒ Mục 5 phải phủ nhiều dạng để phân biệt; và nếu đo xong thấy thông báo đến **một** CB NV có liên quan thật sự tới vụ việc thì **không được** chấm Fail chỉ vì "không đúng người mình đoán".
2. **Câu chữ tiêu đề/nội dung thông báo của FR-V.I-15.** Bảng "Thông báo riêng SCR-V.I-03" (`:1773-1785`) **không có dòng nào** cho "Cập nhật kết quả hỗ trợ" — chỉ có dòng "Cập nhật kết quả cuối → Hoàn thành" (`:1782`, thuộc FR-V.I-16, khác FR).
3. **Chữ toast của vế (a).** Đặc tả im lặng ⇒ toast trên video ghi "Đã cập nhật kết quả" (thiếu chữ "hỗ trợ" so với ô Kết quả mong đợi) **không phải bug**; nếu muốn chốt thì là mục hỏi BA.
4. **"Làm mới Nhóm 6"** (vế a) — `:1732` chỉ liệt kê thành phần Accordion 6, không quy định hành vi tự làm mới.
5. **Độ trễ kênh in-app.** Chỉ email có mốc ≤ 5 phút (`srs-v3.5.md:739`); in-app không có mốc.
6. **File đính kèm trong thông báo.** `srs-v3.5.md:723` nói rõ `THONG_BAO` **không có trường file** ⇒ thông báo không kèm tệp là ĐÚNG đặc tả.
7. **Thông báo có dẫn sang màn chi tiết VV hay không** — `srs-v3.5.md:724` để ngỏ, phụ thuộc quyền của vai trò.
8. **Lấn cấn nhỏ đã rà, KHÔNG coi là mâu thuẫn:** danh sách sự kiện liệt kê trong BR-NOTIF-01 (`:2480`) không có chữ "cập nhật kết quả", nhưng dòng **Applied in** của chính BR đó (`:2482`) và bảng ánh xạ (`:2337`) đều **có FR-V.I-15**, cộng với FR-V.I-15 bước 5 (`:1106`) tự nó đã đòi gửi thông báo. ⇒ Coi FR bước 5 + Applied-in là chi phối, **2 kênh in-app + email đều bắt buộc**. Ghi ra đây để giai đoạn B không sa vào tranh cãi này.

### → Rẽ nhánh (flow dòng 118-134)

Vế (c): đặc tả **nói rõ** (`:1106` / `:1114` / `:1125`) và **khớp** kỳ vọng đối tác ⇒ **KHÔNG phải nhánh cần BA — đo được**. Viết mục 4 + 5 + 6 rồi sang giai đoạn B.
Vế (a) (b) (d): không thuộc phạm vi verdict; nếu phát hiện lệch thì xử theo khung "phát hiện mới" ở đầu file.

---

## 3. Precondition

**Môi trường:** https://18.143.165.120.nip.io (env verify nội bộ). Hộp thư kiểm email: **http://18.143.165.120:8025/** (MailHog, cổng 8025 trên IP thô, KHÔNG qua nip.io — `input/input.md:2,9`).
⚠️ Env này **khác** env trong bằng chứng đối tác (`htpldn-uat.ospgroup.vn`) ⇒ Pass ở đây chỉ là **Pass tạm** cho tới khi bản dựng lên env đối tác. Ghi rõ ở mục 6 và trong báo cáo.

**Tài khoản (bộ `_01`, mật khẩu `Test@1234` — `input/input.md:37-43`, `:77-78`, `:88`, `:103`):**

| Vai trò trong phép đo | Tài khoản | Ghi chú |
|---|---|---|
| **Người bấm "Cập nhật kết quả"** (= `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id`) | `qa_tvvseed28` / `Test@1234` — TVV + CG, Cục Bổ trợ tư pháp (BTP), cấp TW | Trùng vai trò đối tác trong video (TVV · CG). Dự phòng cùng vai trò-cấp: `nht_qa_tw` (NHT, TW). |
| **CB NV #1 — người kỳ vọng nhận** | `cbnv_tw_01` / `Test@1234` — CB_NV_TW | ⚠️ Hồ sơ đợt trước ghi tên khác (`cb_nv_tw_01`) + mật khẩu khác (`Secret@123`). **Thử theo `input.md` trước; ghi rõ tài khoản THỰC đăng nhập được vào mục 6 + báo cáo.** |
| **CB NV #2 — đối chứng "không phải người kỳ vọng"** | `cbnv_tw_02` / `Test@1234` — CB_NV_TW | Dùng để tách vai người tạo ≠ người phân công (dạng 2) và làm nhóm chứng âm. |
| DN (chỉ cho dạng 3) | `0109998887` / `Test@1234` — DN-HNI-0001, Hà Nội | VV do DN gửi sẽ về đơn vị theo `tinh_thanh_id` ⇒ CB NV nhận là của Sở Tư pháp Hà Nội: `cbnv_hn` / `Test@1234`. **Đây là nới đơn vị có chủ đích — bắt buộc khai ở mục 6.** |
| Chỉ để dựng dữ liệu / tra cứu, **KHÔNG ra verdict** | `admin` / `Secret@123` | Quyền rộng che lỗi phân quyền (flow §Chuẩn bị bước 1). |

**Màn / URL:**
- Thao tác: `SCR-V.I-03` — `/vu-viec/{id}` → **Nhóm 6 — Kết quả hỗ trợ** → nút **[Cập nhật kết quả]** (chỉ hiện khi VV ở `DANG_XU_LY`, `srs-fr-05-vu-viec.md:1747`).
- Đo in-app: chuông 🔔 trên thanh trên **và** trang **`/thong-baos`** (`srs-v3.5.md:704`) — đo ở `/thong-baos`, **không** kết luận từ dropdown chuông (dropdown chỉ hiện vài mục gần nhất, dễ false negative).
- Đo email: MailHog `http://18.143.165.120:8025/`.

**Dữ liệu tiền đề cho MỖI dạng (dựng bằng chính luồng chuẩn, trên dữ liệu QA — không đụng dữ liệu đối tác):**
vụ việc phải đi trọn chuỗi **Tiếp nhận → Kiểm tra hồ sơ (Đạt) → Phân công (cho `qa_tvvseed28`) → người được phân công Chấp nhận** để tới trạng thái **Đang xử lý**; xem bảng nút `srs-fr-05-vu-viec.md:1742-1747`.
🔴 **Bắt buộc tự dựng, không dùng vụ việc có sẵn** — vì bằng chứng đối tác không cho biết ai là người kỳ vọng nhận (GAP #1 ở mục 1); chỉ khi tự dựng mới biết chắc "đúng người" (flow §Chuẩn bị bước 3, gạch đầu dòng 3).

**Trước khi đo, ghi lại 2 thứ (không có thì không chấm được "đúng người"):**
- Địa chỉ email thật của từng tài khoản CB NV dùng trong phép đo — **đọc từ hồ sơ tài khoản trong phần mềm**, không suy từ tên đăng nhập (bằng chứng đối tác cho thấy `cbnv_tw` ↔ `@htpldn.gov.vn` còn `cb_nv_tw_03` ↔ `@htpldn.test` — quy ước tên hộp thư không thống nhất).
- Ai là người tạo / người tiếp nhận / người phân công của từng vụ việc vừa dựng.

---

## 4. Tiêu chí chấm — CHỈ cho vế (c) (vế đối tác nêu)

> Đo trên **từng dạng** của mục 5. Mỗi dạng chạy độc lập, có ảnh riêng.
> Toàn bộ đo bằng **thao tác UI thật**; đường máy chủ chỉ dùng để **đối chứng** (flow §Chạy bước 5, bước 8).

**Chuẩn bị phép đo (làm trước khi bấm, nếu thiếu thì phép đo không có giá trị):**
- P1. Nội dung kết quả phải chứa **chuỗi nhận dạng duy nhất** dạng `QA-CNKQHT07-<dạng>-<HHMMSS>` — để sau này phân biệt thông báo của lần bấm này với lần bấm khác.
- P2. Thao tác phải có **đủ 3 thành phần**: nội dung + **≥1 tệp đính kèm** + ghi chú (đúng bước 3 của đối tác; video đối tác thiếu tệp).
- P3. **Đếm thô, không lọc**: mở `/thong-baos` bằng **chính tài khoản CB NV kỳ vọng**, ghi số mục tổng `N_trước` và xác nhận **không** có mục nào nhắc mã vụ việc sắp thao tác.
- P4. Ghi **thời điểm bấm** tới giây.
- P5. Cài bộ bắt thông báo trước khi bấm (không lọc trùng · đọc bằng `innerText` · đếm request song song), đếm thông báo **theo mốc giờ khác nhau** chứ không theo số phần tử.

### ✅ PASS khi — đủ CẢ 6 điều, trên MỌI dạng của mục 5

1. **Thao tác chạy được tới cùng:** sau khi bấm, mở lại màn chi tiết thấy Nhóm 6 hiện đúng chuỗi nhận dạng ở P1 (chứng minh sự kiện sinh thông báo **đã thực sự xảy ra**; nếu bước này hỏng thì phép đo vế (c) vô nghĩa — xem ngoại lệ ở đầu file).
2. **Kênh trong ứng dụng — có mục mới:** đăng nhập **bằng chính tài khoản CB NV kỳ vọng** (không dùng `admin`, không dùng tài khoản vừa bấm), mở `/thong-baos` → `N_sau > N_trước`, và **≥1 mục mới** thoả cả 3: (i) nhắc **đúng mã vụ việc** vừa thao tác; (ii) nội dung cho biết **người được phân công đã cập nhật kết quả hỗ trợ** (mô tả nghiệp vụ — **không** đòi trùng câu chữ nào, xem mục 2 §IM LẶNG #2); (iii) thời điểm trên thẻ nằm **trong cùng phút** với thời điểm bấm ở P4.
3. **Vị trí đúng thứ tự:** mục mới đó nằm ở **đầu** danh sách `/thong-baos` (đặc tả xếp mới-nhất-trước, `srs-v3.5.md:721`) — nếu nó tồn tại nhưng nằm sai chỗ thì ghi nhận riêng, không kéo vế (c).
4. **Kênh email — có thư mới:** trong MailHog env verify xuất hiện thư gửi tới **đúng địa chỉ email của chính tài khoản CB NV kỳ vọng** (địa chỉ lấy từ hồ sơ tài khoản như mục 3 dặn), phát sinh **trong vòng 5 phút** kể từ P4 (`srs-v3.5.md:739`), tiêu đề hoặc nội dung nhắc **đúng mã vụ việc** + việc cập nhật kết quả.
5. **Đối chứng bằng đường thứ hai:** đọc lại danh sách thông báo của **chính tài khoản đó** qua đường máy chủ (phiên của chính tài khoản đó, không phải phiên admin) → ra **cùng** mục mới ấy; số đếm hai đường **khớp nhau**. Lệch nhau ⇒ chưa được chốt, ghi cả hai, hỏi user.
6. **Gửi có địa chỉ, không phát tán:** hai tài khoản **không** kỳ vọng nhận — (i) chính tài khoản vừa bấm cập nhật, (ii) một CB NV cùng cấp **không** liên quan vụ việc đó — **không** có mục thông báo tương ứng với chuỗi nhận dạng P1.

### ❌ FAIL nếu — bất kỳ điều nào

- **F1 (tái hiện đúng lời đối tác):** sau khi bấm và chờ **≥ 5 phút**, tài khoản CB NV kỳ vọng **không** có mục thông báo mới nào nhắc mã vụ việc đó ở **cả hai** kênh (in-app `/thong-baos` **và** MailHog) — xảy ra trên ≥1 dạng mà dạng đó đã xác định chắc chắn được người kỳ vọng.
- **F2 (fix một phần):** chỉ **một** trong hai kênh có (in-app có / email không, hoặc ngược lại). Đặc tả đòi đủ 2 kênh (`srs-fr-05-vu-viec.md:2480` + `:2482`).
- **F3 (sai người):** thông báo có sinh ra nhưng gửi cho người khác (người vừa bấm cập nhật, doanh nghiệp, hoặc một CB NV không liên quan) **trong khi** mọi tài khoản CB NV có liên quan tới vụ việc (người tạo · người tiếp nhận · người phân công) đều **không** có.
- **F4 (không truy được về bản ghi):** thông báo có nhưng **không** nhắc mã vụ việc nào, khiến CB NV không biết phải "xem xét, chuẩn bị trình phê duyệt" cho hồ sơ nào.
- **F5 (nói sai hành động):** nội dung thông báo mô tả **một thao tác khác** với thao tác vừa làm (vd báo "đã phê duyệt" / "đã hoàn thành").

### 🚫 KHÔNG được chấm Fail vì (đặc tả im lặng — chi tiết ở mục 2)

- Tiêu đề/nội dung thông báo khác câu chữ người test hình dung.
- Thông báo không kèm tệp (`srs-v3.5.md:723` — entity không có trường file).
- Thông báo không bấm dẫn được sang màn chi tiết vụ việc (`srs-v3.5.md:724`).
- Kênh in-app xuất hiện chậm vài chục giây (chỉ **email** có mốc ≤ 5 phút).
- Chuông (dropdown) không thấy mục trong khi `/thong-baos` **có** — dropdown chỉ hiện vài mục gần nhất; chốt theo `/thong-baos`.
- Toast của vế (a) ghi "Đã cập nhật kết quả" thay vì "Đã cập nhật kết quả hỗ trợ".
- Người nhận là một CB NV **có liên quan** vụ việc nhưng không phải người test đoán trước (đặc tả không định nghĩa "phụ trách").

### ⚠️ Bẫy PASS-oan phải né

- **Đo nhầm người** — bẫy chính của case này. Chỉ được kết luận "có/không nhận" sau khi đã tự dựng vụ việc và biết chắc ai là người tạo / tiếp nhận / phân công.
- **Không có nhóm chứng dương ⇒ không phân biệt được "FR-V.I-15 không gửi" với "thông báo hỏng cho tài khoản này".** Bắt buộc chạy thêm **1 phép chứng dương** trên cùng tài khoản CB NV kỳ vọng: kích hoạt một sự kiện khác mà đặc tả cũng đòi gửi cho CB NV — sẵn có ngay trong chuỗi dựng tiền đề: **FR-V.I-10 (UC60) Xác nhận tham gia hỗ trợ**, `srs-fr-05-vu-viec.md:795` (tiêu đề FR) · `:825` (`| 5 | Gửi thông báo CB NV | — |`) · `:834` (`- CB NV nhận thông báo`) — tức bước "người được phân công **Chấp nhận** phân công", rồi kiểm chính hộp đó. Chứng dương ra thông báo mà FR-V.I-15 không ra ⇒ khoanh đúng lỗi ở FR-V.I-15. Cả hai đều không ra ⇒ ghi rõ là nghi vấn hạ tầng thông báo, **không** vội chốt vế (c).
- **Kết luận từ script trong trang mà không có ảnh** — phải có ảnh mở đọc được của `/thong-baos` và của MailHog.
- **Tab mở lâu chạy bản dựng cũ** — tải lại trang trước khi đo, ghi dấu vân tay bản dựng (tên tệp bó mã / mã commit / thời điểm deploy), không chỉ chuỗi "V1.0.x".

---

## 5. Dạng dữ liệu phải phủ — **M = 3**

**Vì sao phải nhiều dạng:** đặc tả im lặng về "CB NV" là ai (mục 2 §IM LẶNG #1), nên chỉ 1 bản ghi thì không phân biệt được 4 giả thuyết người nhận: **người TẠO vụ việc · người TIẾP NHẬN · người PHÂN CÔNG · mọi CB NV cùng đơn vị**. Đây đúng là chỗ đối tác có thể đã kiểm nhầm hộp.

| # | Tên dạng | Cách dựng | Dạng này trả lời điều gì |
|:--:|---|---|---|
| **1** | **Người kỳ vọng nhận TỰ TẠO trọn vụ việc** — tạo = tiếp nhận = phân công đều là `cbnv_tw_01` | `cbnv_tw_01` nhập thủ công vụ việc (`srs-fr-05-vu-viec.md:1707` — nhập thủ công UC54 vào thẳng `DA_TIEP_NHAN`) → tự kiểm tra hồ sơ → tự phân công cho `qa_tvvseed28` → `qa_tvvseed28` chấp nhận → cập nhật kết quả | **Quyết định khi FAIL.** Mọi giả thuyết người nhận đều trỏ về `cbnv_tw_01`. Không có thông báo ở đây ⇒ không giả thuyết nào cứu được ⇒ lỗi thật. |
| **2** | **Người khác TẠO, người kỳ vọng nhận chỉ PHÂN CÔNG** — tạo + tiếp nhận = `cbnv_tw_02`; phân công = `cbnv_tw_01` | `cbnv_tw_02` nhập thủ công + kiểm tra hồ sơ → **`cbnv_tw_01`** thực hiện Phân công cho `qa_tvvseed28` → chấp nhận → cập nhật kết quả | **Quyết định khi PASS.** Tách "người tạo/tiếp nhận" khỏi "người phân công" ⇒ biết hệ thống gửi theo trục nào. |
| **3** | **KHÔNG CB NV nào là người tạo** — doanh nghiệp tự gửi hồ sơ | DN `0109998887` gửi yêu cầu từ chuyên trang (`srs-fr-05-vu-viec.md:1708` — từ chuyên trang UC52, `trang_thai = MOI_TAO`; `:200` — gửi thông báo CB NV đơn vị theo `tinh_thanh_id`) → CB NV đơn vị đó tiếp nhận + kiểm tra + phân công → người được phân công chấp nhận → cập nhật kết quả | Đây là **đường vào mặc định ở thực tế**. Loại bỏ giả thuyết "hệ thống chỉ gửi cho người tạo bản ghi" — bài học đã có ở dự án này. |

**Nguồn xác định M (theo flow dòng 189-193, dừng ở bước ①):** ① mục đặc tả nói về **cách bản ghi được tạo** — `srs-fr-05-vu-viec.md:1707-1708` liệt kê các đường tạo VU_VIEC: *"Nhập thủ công (UC54): trang_thai mặc định = DA_TIEP_NHAN"* và *"Từ chuyên trang (UC52): trang_thai = MOI_TAO"*; cộng với các vai CB NV gắn vào vụ việc ở `:1742` (người tiếp nhận, `nguoi_tiep_nhan`), `:1745` (người phân công), `:2022` (`nguoi_tiep_nhan_id`).

**Dạng thứ 4 đã tra nhưng KHÔNG seed được — khai để khỏi coi là bỏ sót:** vụ việc vào qua **API/Hệ thống khác** (`srs-fr-05-vu-viec.md:459`, `:493` — UC55, THONG_BAO gửi CB NV). Đường này đòi mTLS mà env UAT không cấp chứng thư (đã tra, không vào được). Dạng này **không** đổi câu trả lời cho vế (c) vì nó chỉ là một biến thể nữa của "không CB NV nào là người tạo" — đã được dạng 3 phủ. Ghi rõ trong báo cáo.

**Ghi chú thực thi cho dạng 3:** vụ việc của DN Hà Nội sẽ về Sở Tư pháp Hà Nội ⇒ người kỳ vọng nhận là CB NV của đơn vị đó (`cbnv_hn`), không phải cấp TW. Đây là **nới cấp/đơn vị có chủ đích** (giữ nguyên **vai trò** CB_NV — thứ quyết định bộ quyền; chỉ nới **cấp/đơn vị** — thứ quyết định phạm vi dữ liệu, theo flow §Đóng GAP gạch đầu dòng cuối). **Bắt buộc khai vào mục 6: đã nới chiều nào + vì sao.** Nếu đơn vị đó không có người hỗ trợ/TVV đang hoạt động để phân công (đã có tiền lệ với An Giang — `input/input.md:84-86`) thì đổi sang DN thuộc đơn vị có sẵn nguồn lực, và ghi rõ đã đổi gì.

---

## 6. Bảng điều kiện

Cột **"Đối tác"** điền NGAY từ bằng chứng. Hai cột sau điền ở giai đoạn B. **Điền đủ 5 dòng, không bỏ trống dòng nào** — dòng cho là không ảnh hưởng vẫn ghi `Không — <căn cứ>`.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Người bấm:** `huongcg` — **TVV · CG**, đơn vị BTP · TW, là người được phân công của vụ việc. **Người kiểm thông báo:** tài khoản hiển thị **"Cán bộ NV Trung ương · CB_NV_TW"**, hộp thư OTP `cbn***@htpldn.gov.vn` (MailHog cho thấy `cbnv_tw@htpldn.gov.vn`). ⚠️ **Video KHÔNG cho biết tài khoản này có phải CB NV phụ trách của chính vụ việc đó không** — thư hệ thống trước đó của **cùng vụ việc** lại gửi tới `cb_nv_tw_03@htpldn.test` (mốc 00:24) ⇒ **nghi kiểm nhầm hộp**. | **Người bấm cập nhật:** `qa_tvvseed28` / `Test@1234` (TVV · CG, Cục Bổ trợ tư pháp, cấp TW) cho dạng 1 + 1B + 2 — trùng vai trò người bấm trong video; `nht_ag_uat2` / `Test@1234` (Người hỗ trợ, Sở Tư pháp An Giang) cho dạng 3. **Người kỳ vọng nhận:** `cbnv_tw_01` (dạng 1, 1B) · `cbnv_tw_02` (dạng 2) · `cbnv_dp_01` (dạng 3) — đều `Test@1234`, đăng nhập được đúng tên trong `input/input.md`; **KHÔNG** dùng cặp `cb_nv_tw_01` / `Secret@123` của hồ sơ đợt trước. **Địa chỉ hộp thư đọc từ hồ sơ tài khoản trong phần mềm** (không suy từ tên đăng nhập): `cbnv_tw_01@htpldn.test` · `cbnv_tw_02@htpldn.test` · `cbnv_dp_01@htpldn.test` — miền `@htpldn.test`, **khác** miền `@htpldn.gov.vn` mà tài khoản trong video dùng. `admin` chỉ dùng tra cứu định danh + dựng dữ liệu, **không** dùng để chấm. | **Không** — vai trò CB_NV giữ nguyên ở cả 3 dạng. Có **nới cấp/đơn vị có chủ đích** ở dạng 3 (CB NV cấp Sở thay vì TW) vì vụ việc do DN gửi về đơn vị theo tỉnh/thành; nới cấp chỉ đổi phạm vi dữ liệu, không đổi bộ quyền, và dạng 1 + 2 vẫn giữ đúng cấp TW như đối tác. Đã tự dựng nên biết chắc ai là người tạo · tiếp nhận · phân công — đóng được GAP #1 của mục 1. |
| Entity + trạng thái | Vụ việc **VV-BTP-TW-20260511-001** (`/vu-viec/fa942aa3-e2a4-4608-be31-ec55a1f1cef9`), tiêu đề "INVESTIGATE-NOTIF-01-170214", trạng thái **Đang xử lý** (stepper bước 6), badge "Quá hạn nghiêm trọng · 41 ngày LV", lĩnh vực Thuế, ngày tiếp nhận 11/05/2026. | 3 vụ việc **mới dựng trong env verify**, đều ở đúng trạng thái **Đang xử lý** và đều bấm đúng nút **[Cập nhật kết quả]** trong **Nhóm 6 — Kết quả hỗ trợ**: **D1/D1B** `VV-BTP-TW-20260806-003` (`/vu-viec/fbf936fb-b605-4286-946b-f68ba1fd6e89`, lĩnh vực Thuế) · **D2** `VV-BTP-TW-20260806-004` (`/vu-viec/45501596-4a60-4e9b-8321-632fa6efd682`) · **D3** `VV-STP-AG-20260806-005` (`/vu-viec/0dfb2b25-efa3-4fb4-86b7-31b4bfe78c86`). Không đụng vụ việc của đối tác (khác env). | **Không** — cùng entity `VU_VIEC`, cùng trạng thái `DANG_XU_LY`, cùng màn `SCR-V.I-03` và cùng nút như video. Khác duy nhất: vụ việc của đối tác quá hạn nghiêm trọng còn của mình trong hạn — mốc hạn không nằm trong nhánh xử lý nào của FR-V.I-15 nên không đổi kết quả. |
| Dữ liệu tiền đề | Đã đi trọn chuỗi tới "Đang xử lý" (mốc 00:24 có thư "Người hỗ trợ đã xác nhận tham gia vụ việc - VV-BTP-TW-20260511-001", 14 phút trước ⇒ đã có phân công + chấp nhận). **Không thấy** ai tạo / ai tiếp nhận / ai phân công — video không mở Nhóm 5 lẫn Dòng thời gian. Vụ việc là bản ghi thăm dò do chính đối tác dựng ("Probe NOTIF-01 listener … for hypothesis test on UC62"). | Cả 3 dạng đi **trọn luồng chuẩn** Tiếp nhận → Kiểm tra hồ sơ (Đạt) → Phân công → người được phân công **Chấp nhận** → Đang xử lý, nên biết chắc từng vai: **D1/D1B** tạo = tiếp nhận = kiểm tra = phân công đều là `cbnv_tw_01`, người được phân công `qa_tvvseed28`. **D2** tạo + tiếp nhận + kiểm tra = `cbnv_tw_02`, **phân công = `cbnv_tw_01`**, người được phân công `qa_tvvseed28`. **D3** người tạo là **doanh nghiệp** (`0209888006`), tiếp nhận + kiểm tra + phân công = `cbnv_dp_01`, người được phân công `nht_ag_uat2`. Bước **Chấp nhận phân công** của cả 3 dạng đồng thời là **nhóm chứng dương** (FR-V.I-10). | **Không** — dựng đủ 3 dạng để tách 4 giả thuyết người nhận (người tạo · người tiếp nhận · người phân công · mọi CB NV cùng đơn vị) mà bằng chứng đối tác không tách được. |
| Input / filter / giá trị nhập | Nội dung kết quả = `TVV cập nhật kết quả` (20/10000). **Không đính kèm tệp** (vùng "Tệp kết quả hỗ trợ" trống ở 00:12) · **Ghi chú để trống** — dù bước 3 của phiếu ghi "Nhập nội dung và tải tệp". Kiểm thông báo: mở **dropdown chuông** trên `/dashboard` (badge 99+), **không** mở trang `/thong-baos`; **không** kiểm hộp thư sau thao tác (lần mở MailHog ở 00:24 là để lấy OTP đăng nhập). | **Giá trị nhập:** mỗi lần bấm có chuỗi nhận dạng riêng `QA-CNKQHT07-<dạng>-<HHMMSS>`. Dạng 1 · 2 · 3 nhập **đủ 3 thành phần** (nội dung + 1 tệp `.pdf` + ghi chú) đúng bước 3 của phiếu. **Dạng 1B nhập ĐÚNG như đối tác: chỉ nội dung, KHÔNG tệp, KHÔNG ghi chú** (`QA-CNKQHT07-D1B-160609`, ô đếm 107/10000, danh sách tệp đính kèm rỗng — ảnh `cnkqht07-15-d1b-form-khong-tep-khong-ghichu-truoc-khi-bam.png`). **Cách kiểm thông báo:** đo ở **trang `/thong-baos`** của chính người kỳ vọng nhận (không chốt bằng dropdown chuông) + **hộp thư MailHog** của đúng địa chỉ đó + đối chứng bằng đường máy chủ trong **phiên của chính tài khoản đó**. | **Không** — dạng 1B lặp đúng bộ nhập của đối tác (không tệp, không ghi chú) và vẫn ra thông báo ở cả 2 kênh, nên chênh lệch "có tệp / không tệp" không còn là biến chưa kiểm. Cách kiểm của mình **rộng hơn** đối tác (thêm `/thong-baos` + hộp thư), không hẹp hơn. |
| Độ phủ biến thể (N bản ghi, M dạng) | **N = 1** bản ghi · **M = 1** dạng (đúng 1 vụ việc, 1 lần bấm, 1 hộp thông báo, 1 kênh). Không có bản ghi đối chứng nào để biết hệ thống gửi cho người tạo hay người tiếp nhận hay người phân công. | **N = 3 bản ghi · 4 lần bấm · M = 3 dạng** (dạng 1 chạy 2 lần: 1 lần đủ thành phần, 1 lần không tệp/không ghi chú). Mỗi lần bấm đo **2 kênh** (in-app + hộp thư) trên **3 hộp thông báo khác nhau**, kèm **1 nhóm chứng dương** (FR-V.I-10) trên chính từng hộp và **2 nhóm chứng âm** (người vừa bấm; CB NV không liên quan / người chỉ phân công). | **Không** — phủ vượt đối tác (N=1 · M=1 · 1 kênh · 1 hộp). Dạng thứ 4 (vụ việc vào qua API hệ thống khác, UC55) **không seed được** vì env không cấp chứng thư mTLS; dạng này chỉ là biến thể khác của "không CB NV nào là người tạo" mà dạng 3 đã phủ ⇒ khai ra, không tính là GAP. |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** `https://htpldn-uat.ospgroup.vn/vu-viec/fa942aa3-e2a4-4608-be31-ec55a1f1cef9` — mã **VV-BTP-TW-20260511-001**.
- **Trạng thái entity:** **Đang xử lý** (`DANG_XU_LY`, stepper bước 6/9), quá hạn nghiêm trọng 41 ngày LV.
- **Vai trò + env + bản dựng:** người bấm `huongcg` (TVV · CG, BTP · TW) / người kiểm thông báo "Cán bộ NV Trung ương" (CB_NV_TW) · env **`htpldn-uat.ospgroup.vn`** (env nghiệm thu của đối tác) · bản dựng ghi ở thanh bên **"HTPLDN · V1.0.2"** · đồng hồ máy quay **30/07/2026, 09:54-09:55**.

**Giới hạn hiệu lực của verdict (không phải GAP):** giai đoạn B đo trên **`18.143.165.120.nip.io`**, khác env đối tác `htpldn-uat.ospgroup.vn`, và bản dựng gần như chắc chắn mới hơn V1.0.2 của video. ⇒ Kết quả Pass ở đây là **Pass tạm**, chỉ có hiệu lực cho env + bản dựng ghi ở đầu file, cho tới khi bản dựng đó lên env đối tác. Phải nói rõ điều này trong báo cáo, đừng để người đọc tưởng đối tác mở lên là hết lỗi.

---

## Việc bắt buộc của giai đoạn B trước khi chốt

1. Điền `Bản dựng:` ở đầu file — kèm **dấu vân tay** (tên tệp bó mã / mã commit / thời điểm deploy), không chỉ chuỗi "V1.0.x".
2. Điền đủ **2 cột còn lại × 5 dòng** mục 6. Còn ≥1 GAP ⇒ **cấm mọi verdict trừ ô trống**, và ô trống phải ghi rõ GAP nào chưa đóng + vì sao.
3. Ghi rõ **tài khoản THỰC** đã đăng nhập cho từng vai (mục 3 có 2 nguồn tên/mật khẩu mâu thuẫn nhau).
4. Khai **dữ liệu đã seed / thay đổi**: bản ghi nào · đổi gì · env nào.
5. Nếu sửa tiêu chí giữa chừng ⇒ thêm một mục sửa đổi có mốc giờ, nêu rõ sửa gì và vì sao. **Cấm sửa âm thầm mục 4 và mục 5 cho khớp kết quả đo.**

---

## 7. Sửa đổi trong lúc chạy (giai đoạn B)

**Nguyên tắc đã giữ:** mục 4 (tiêu chí PASS/FAIL) và bộ 3 dạng ở mục 5 **không bị sửa** sau khi có số đo. Hai thay đổi dưới đây đều là thay đổi **cách dựng dữ liệu**, đã được mục 5 cho phép trước, và đều làm phép đo **chặt hơn**, không nới lỏng.

### 7.1 — 2026-08-06 15:47 · Đổi đơn vị của dạng 3: Hà Nội → An Giang

- **Sửa gì:** dạng 3 dự kiến dùng DN `0109998887` (Hà Nội) → CB NV `cbnv_hn`. Thực tế chạy bằng DN `0209888006` (An Giang) → CB NV `cbnv_dp_01`, người được phân công `nht_ag_uat2`.
- **Vì sao:** dựng tới bước Phân công ở Hà Nội thì **nguồn phân công rỗng** — gợi ý tự động không trả người nào cho lĩnh vực Thuế, "Tìm thủ công" chỉ có `[TVV] Nguyễn Văn Seed (DDD-TVV-022)` mà bản ghi này **không gắn tài khoản đăng nhập** (`taiKhoanId` rỗng) nên không thể thực hiện bước "Chấp nhận phân công" để đưa vụ việc lên *Đang xử lý*. Không tới được *Đang xử lý* thì **không bấm được** nút [Cập nhật kết quả] ⇒ không đo được vế (c).
- **Căn cứ được phép:** mục 5 §"Ghi chú thực thi cho dạng 3" đã cho sẵn phương án này ("nếu đơn vị đó không có người hỗ trợ/TVV đang hoạt động để phân công thì đổi sang DN thuộc đơn vị có sẵn nguồn lực, và ghi rõ đã đổi gì").
- **Hệ quả:** vai trò người kỳ vọng nhận vẫn là **CB_NV** (không đổi bộ quyền), chỉ đổi **cấp/đơn vị** từ Sở Tư pháp Hà Nội sang Sở Tư pháp An Giang. Đã khai ở mục 6 dòng 1.
- **Dữ liệu còn lại ở Hà Nội:** `VV-STP-HN-20260806-002` dừng ở trạng thái **Đang kiểm tra**, không đi tiếp. Khai ở §7.3.

### 7.2 — 2026-08-06 16:06 · Thêm lần đo 1B (không tệp, không ghi chú) để đóng một chiều còn hở

- **Thêm gì:** một lần bấm nữa trên chính vụ việc dạng 1, nhập **chỉ nội dung** — **không** đính tệp, **không** ghi chú.
- **Vì sao:** chuẩn bị phép đo P2 của mục 4 bắt buộc "nội dung + ≥1 tệp + ghi chú", nên cả 3 dạng đầu đều chạy **có tệp**, trong khi thao tác của đối tác trong video **không đính tệp nào** (mục 1, mốc 00:12). Nếu việc gửi thông báo lệ thuộc nhánh có tải tệp thì kết quả 3 dạng đầu sẽ Pass mà lỗi của đối tác vẫn còn ⇒ đây là một chiều chưa kiểm, phải đóng trước khi chốt.
- **Đây KHÔNG phải nới tiêu chí:** P2 vẫn giữ nguyên và vẫn được thoả ở dạng 1/2/3; lần 1B là **phép đo bổ sung nghiêm hơn**, không thay thế phép đo nào.
- **Kết quả:** vẫn ra thông báo ở **cả 2 kênh**, cách lúc bấm dưới 1 giây. Chi tiết ở bug-report.

### 7.3 — Dữ liệu đã dựng / đã thay đổi trên env verify `18.143.165.120.nip.io`

| Bản ghi | Thao tác đã làm | Trạng thái để lại |
|---|---|---|
| `VV-BTP-TW-20260806-003` (`fbf936fb-…`) | Tạo thủ công bởi `cbnv_tw_01` → kiểm tra Đạt → phân công `qa_tvvseed28` → chấp nhận → cập nhật kết quả **2 lần** (15:45 có tệp · 16:06 không tệp) | Đang xử lý · Nhóm 6 giữ nội dung của lần 16:06 và tệp `qa-cnkqht07-ket-qua.pdf` của lần 15:45 |
| `VV-BTP-TW-20260806-004` (`45501596-…`) | Tạo + tiếp nhận + kiểm tra bởi `cbnv_tw_02`, phân công bởi `cbnv_tw_01`, chấp nhận bởi `qa_tvvseed28`, cập nhật kết quả 15:46 | Đang xử lý |
| `VV-STP-AG-20260806-005` (`0dfb2b25-…`) | DN `0209888006` gửi yêu cầu → `cbnv_dp_01` tiếp nhận + kiểm tra + phân công `nht_ag_uat2` → chấp nhận → cập nhật kết quả 15:49 | Đang xử lý |
| `VV-STP-HN-20260806-002` | DN `0109998887` gửi yêu cầu → `cbnv_hn` tiếp nhận + kiểm tra; **dừng** vì không có người để phân công (§7.1) | Đang kiểm tra — bỏ dở có chủ ý |
| Tệp dùng để đính kèm | Tự tạo `qa-cnkqht07-ket-qua.pdf` (641 byte) vì ô tải tệp chỉ nhận .pdf/.doc/.docx/.xls/.xlsx/.jpg/.png | Đã đính vào vụ việc `-003` |

Không đổi mật khẩu, không đổi trạng thái tài khoản nào. Không đụng bất kỳ bản ghi nào của đối tác (khác env).
