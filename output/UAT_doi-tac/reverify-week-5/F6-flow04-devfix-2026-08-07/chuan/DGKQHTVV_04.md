# Chuẩn chấm đã khóa — DGKQHTVV_04 (dòng 68) — GIAI ĐOẠN A, CHƯA CÓ VERDICT

> **FLOW 04** — verify bug dev báo đã fix, **không có hồ sơ nội bộ** (không có bug entry, không có khối `CÁCH VERIFY` cũ cho mã này).
> **Nguồn chuẩn đặc tả — DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> Mọi số dòng dưới đây **tự mở file đọc lại ngày 2026-08-07 trong lượt này**. Không mượn số dòng từ phiếu UAT, thư BA hay báo cáo đợt cũ.
> Chức năng: **FR-V.I-17 — Đánh giá kết quả hỗ trợ vụ việc (UC67)**, heading tại `srs-fr-05-vu-viec.md:1185`.
>
> 🔴 **Không có bằng chứng đối tác cho mã này** (đã tìm toàn bộ `reverify-week-5/**/partner-evidence/`). ⇒ Tiền đề tái hiện suy từ chính bước + điều kiện ghi trên phiếu; phải khai rõ điều kiện đã tái hiện.
>
> 🔴 **Cảnh báo lệch mã TC — ghi thẳng trên nguồn case:** *"đối tác xóa và đánh lệch ID, chuyển lại ID 4 và 5 cho map với đối tác"*. ⇒ Khi ghi kết quả phải neo vào **đúng dòng 68 của nguồn case**, không neo vào mã `DGKQHTVV_04` một mình. Trước khi chốt, **đọc lại đầy đủ dòng 68** ở nguồn case (nguồn có thể đổi trong lúc chạy).

---

## 1. Lỗi gốc — nguyên văn phiếu

| | Nội dung |
|---|---|
| **Mã TC / dòng** | `DGKQHTVV_04` — dòng **68** |
| **Mô tả** | Tự động tính điểm tổng bằng trung bình cộng 3 điểm |
| **Điều kiện** | 1. Đăng nhập tài khoản; 2. Hồ sơ vụ việc ở trạng thái "Hoàn thành" hoặc "Đã đánh giá" |
| **Các bước** | 1. Chọn menu "Vụ việc HTPL"; 2. Tìm kiếm và nhấn Xem chi tiết; 3. Mở Nhóm 8 – Đánh giá; 4. Bấm nút "Đánh giá" và nhấn "Lưu đánh giá" |
| **Kết quả mong đợi (nguyên văn)** | Tự động tính điểm tổng bằng trung bình cộng 3 điểm |
| **Trạng thái** | Fail · **Dopai:** Open · **Loại vấn đề:** đối tác xóa và đánh lệch ID, chuyển lại ID 4 và 5 cho map với đối tác · **Trạng thái dev fix:** Fixed |

**Vai trò suy ra từ bước 1:** menu **"Vụ việc HTPL"** = menu CMS phía cán bộ (`srs-v3.5.md:641` — `📋 Quản lý vụ việc hỗ trợ pháp lý [click thẳng] → FR-V.I (UC51-67)`; tiêu đề màn `srs-fr-05-vu-viec.md:1637` — `"Quản lý Vụ việc HTPL"`). ⇒ **Đo ở chế độ CÁN BỘ (CB_NV)**. Nhánh doanh nghiệp là `DGKQHTVV_01`, không gộp.

---

## 2. Đặc tả đối chiếu — trích dẫn nguyên văn, tự mở file đếm lại

### 2.1 Công thức điểm tổng — SRS quy định ở **4 chỗ, thống nhất nhau**

| `file:dòng` | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1208` | `\| 5 \| diem_tong \| number \| Y (auto) \| AVG(3 điểm) \|` *(bảng **Inputs** của FR-V.I-17)* |
| `srs-fr-05-vu-viec.md:1220` | `\| 6 \| Xác nhận điểm 0-10; tính điểm tổng = trung bình 3 điểm \| — \|` *(bảng **Processing**, bước 6)* |
| `srs-fr-05-vu-viec.md:1734` | `\| 11 \| content \| Accordion 8 — Đánh giá (gộp MH-05.9) \| C23 \| diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet \| CB NV/DN nhập trực tiếp \| Khi VV ở HOAN_THANH hoặc DA_DANH_GIA \|` |
| `srs-fr-05-vu-viec.md:2120` | `\| 8 \| diem_tong \| number \| Y \| Auto = AVG(diem_chat_luong, diem_thoi_gian, diem_thai_do) \| — \| Điểm tổng hợp \|` *(entity `DANH_GIA_VU_VIEC`)* |

> ⇒ **Expected đối tác *"trung bình cộng 3 điểm"* KHỚP NGUYÊN với SRS.** Không có DIFF ở công thức.

### 2.2 **3 tiêu chí là 3 tiêu chí nào** — SRS nêu đích danh

| `file:dòng` | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1190` | `**Mô tả:** CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc.` |
| `srs-fr-05-vu-viec.md:1205` | `\| 2 \| diem_chat_luong \| number \| Y \| 0-10 \|` |
| `srs-fr-05-vu-viec.md:1206` | `\| 3 \| diem_thoi_gian \| number \| Y \| 0-10 \|` |
| `srs-fr-05-vu-viec.md:1207` | `\| 4 \| diem_thai_do \| number \| Y \| 0-10 \|` |
| `srs-fr-05-vu-viec.md:2117` | `\| 5 \| diem_chat_luong \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm chất lượng tư vấn \|` |
| `srs-fr-05-vu-viec.md:2118` | `\| 6 \| diem_thoi_gian \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm đúng thời hạn \|` |
| `srs-fr-05-vu-viec.md:2119` | `\| 7 \| diem_thai_do \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm thái độ phục vụ \|` |

**⇒ 3 tiêu chí = chất lượng tư vấn · đúng thời hạn · thái độ phục vụ.** Cả 3 đều **bắt buộc**, thang **0–10**.

### 2.3 Điều kiện để thao tác có hiệu lực (tiền đề, KHÔNG tách thành bug mới)

| `file:dòng` | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1197` | `\| PRE-02 \| VV ở trạng thái HOAN_THANH hoặc DA_DANH_GIA \|` |
| `srs-fr-05-vu-viec.md:1198` | `\| PRE-03 \| Role ∈ {CB_NV, DN} (theo CSV UC67) \|` |
| `srs-fr-05-vu-viec.md:1215` | `\| 1 \| Kiểm tra quyền: role ∈ {CB_NV, DN} \| BR-AUTH-01 \|` |
| `srs-fr-05-vu-viec.md:1216` | `\| 2 \| Validate scope theo role: nếu role='DN' → \`VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id\`; nếu role='CB_NV' → \`VU_VIEC.don_vi_id = current_user.don_vi_id\` \| BR-AUTH-03/04, BR-AUTH-08 \|` |
| `srs-fr-05-vu-viec.md:1219` | `\| 5 \| Check duplicate: nếu đã tồn tại bản ghi DANH_GIA_VU_VIEC cho cùng VV và cùng loại người đánh giá → ERR-DG-VV-03 \| — \|` |
| `srs-fr-05-vu-viec.md:1222` | `\| 8 \| Chuyển VV → DA_DANH_GIA (chỉ lần đánh giá đầu tiên; nếu VV đã DA_DANH_GIA thì giữ nguyên) \| SM-VUVIEC \|` |
| `srs-fr-05-vu-viec.md:1751` | `\| HOAN_THANH \| [Đánh giá] (gộp MH-05.9) \| CB NV/DN \| Mở Accordion 8. Gửi → DA_DANH_GIA \|` |
| `srs-fr-05-vu-viec.md:2114` | `\| 2 \| vu_viec_id \| identifier \| Y \| FK → VU_VIEC(id); UNIQUE(vu_viec_id, loai_nguoi_danh_gia) \| — \| VV được đánh giá \|` |

### 2.4 Chỗ SRS IM LẶNG hoặc TỰ MÂU THUẪN — đã đọc trọn đoạn, không phải grep rỗng

| Vấn đề | Kết luận | Dòng đã đọc để truy phạm vi |
|---|---|---|
| **Làm tròn / số chữ số thập phân của `diem_tong` khi 3 điểm không chia hết cho 3** | **IM LẶNG cho UC67.** Quy tắc làm tròn duy nhất trong file **loại trừ UC67 bằng chữ**: `srs-fr-05-vu-viec.md:2462` — `Trigger cập nhật \`TU_VAN_VIEN.diem_danh_gia_tb = AVG(diem_trung_binh)\` từ DANH_GIA_SAU_VU_VIEC (đối tượng do FR-IV quản lý). Thang điểm 1–5, làm tròn 1 chữ số thập phân (round-half-up). **UC67 chỉ tạo DANH_GIA_VU_VIEC (thang 0–10)**, trigger cập nhật điểm TVV nằm ở **FR-IV-CROSS-01**.` Đã đọc trọn bảng Inputs (`:1202`–`:1209`), Processing (`:1213`–`:1224`), entity (`:2111`–`:2123`) — không dòng nào nói làm tròn cho `diem_tong` | `:1208`, `:1220`, `:2120`, `:2462` |
| **"Tự động" nghĩa là tính lúc nào / ở đâu** (cập nhật ngay khi gõ trên form, hay tính khi gửi ở phía máy chủ) | **IM LẶNG.** SRS chỉ khẳng định **kết quả** là auto: `:1208` `Y (auto)`, `:1734` `diem_tong (AVG auto)`, `:2120` `Auto = AVG(...)`; và đặt phép tính ở **bước xử lý số 6 khi gửi** (`:1220`). Không có dòng nào bắt cập nhật realtime trên form | `:1208`, `:1220`, `:1734`, `:2120` |
| **Nhãn nút gửi trong Accordion 8** ("Lưu đánh giá" theo phiếu) | **IM LẶNG.** `:1751` chỉ ghi `[Đánh giá] … Mở Accordion 8. Gửi → DA_DANH_GIA`. Bảng "Thông báo riêng SCR-V.I-03" (`:1773`–`:1785`, 11 tình huống) **không có dòng nào cho thao tác đánh giá** | `:1751`, `:1773`–`:1785` |
| **VV đang ở `DA_DANH_GIA` thì phía cán bộ còn thấy nút [Đánh giá] không** | **TỰ MÂU THUẪN.** Bảng nút hành động **chế độ cán bộ** (`:1751`) chỉ có dòng `HOAN_THANH`, **không có** dòng `DA_DANH_GIA`; trong khi `:1197` (PRE-02), `:1734` (điều kiện hiển thị Accordion 8) và `:1811` (thanh thao tác **chế độ DN**) đều gồm cả `DA_DANH_GIA`. **Mâu thuẫn này đã ở tay BA từ đợt trước** | `:1197`, `:1734`, `:1751`, `:1811` |
| **Điểm trung bình của tư vấn viên có phải đổi sau khi đánh giá không** | **TỰ MÂU THUẪN.** `:1233` (Postconditions) — `- Điểm TVV được cập nhật` **ngược** với `:1223` (Processing bước 9) — `… **UC67 chỉ tạo DANH_GIA_VU_VIEC; trigger cập nhật điểm TVV nằm ở module FR-IV**` và `:2462`. **Đã gửi BA** | `:1223`, `:1233`, `:2462` |

---

## 3. BUG SCOPE LOCK — các dòng `Cn`

> Expected chỉ có **một câu**. Tách đúng câu đó, **không** kéo theo chức năng kế bên (không đo chặn điểm ngoài 0–10 `:1240`, không đo chặn đánh giá lần 2 `:1219`/`:1241`, không đo chuyển trạng thái `:1222`, không đo thông báo). Sau khi mở màn, **cấm đổi quan hệ** để khớp kết quả (Flow 04, luật khóa 5).

```
C1 · "…tính điểm tổng bằng trung bình cộng 3 điểm" — điểm tổng lưu và hiển thị = (điểm chất lượng tư vấn
     + điểm đúng thời hạn + điểm thái độ phục vụ) / 3
   · srs-fr-05-vu-viec.md:1208 · :1220 · :1734 · :2120 (4 chỗ thống nhất) · MATCH · route TEST
   · Đường đo: CB NV mở Nhóm 8 của 1 VV "Hoàn thành" chưa có đánh giá CB_NV, nhập bộ điểm PHÂN BIỆT
     4 · 8 · 9 (trung bình = 7, khác median 8, khác min 4, khác max 9, khác tổng 21) + chuỗi nhận xét mốc-giờ
     duy nhất, gửi → TẢI LẠI TRANG BẰNG ĐỊA CHỈ → đọc lại điểm tổng ở Nhóm 8

C2 · "TỰ ĐỘNG tính" — người dùng KHÔNG phải tự nhập điểm tổng; hệ thống tự sinh giá trị đó
   · srs-fr-05-vu-viec.md:1208 ("Y (auto)") · :1734 ("diem_tong (AVG auto)") · :2120 ("Auto = AVG(...)")
     + srs-v3.5.md:585 (UI-13: trường hệ thống tự gán KHÔNG gắn dấu sao) · MATCH · route TEST
   · Đường đo: cùng lượt với C1 — quan sát ô điểm tổng không nhận nhập tay / không bắt buộc người dùng điền,
     và giá trị lưu được sinh ra dù người dùng không chạm vào ô đó
   · ⚠️ Đã khóa: THỜI ĐIỂM tính (realtime khi gõ vs khi gửi) SRS IM LẶNG ⇒ KHÔNG thuộc tiêu chí chấm của C2

C3 · Làm tròn / số chữ số thập phân của điểm tổng khi 3 điểm không chia hết cho 3
   · IM LẶNG cho UC67 (:2462 loại trừ UC67 khỏi quy tắc làm tròn duy nhất) · GAP · route BA
   · Đường đo: KHÔNG bắt buộc. Nếu chạy thì CHỈ để cấp dữ kiện cho câu hỏi BA, phải ghi nhãn
     "dữ liệu cho câu hỏi BA — KHÔNG ra verdict", và CẤM dùng kết quả này đổi verdict C1/C2
```

**Ánh xạ bắt buộc:** mọi thao tác / seed / ảnh phải trả lời được `đang kiểm Cn nào?`. Không ánh xạ được ⇒ **CẤM chạy**.

**Số bản ghi:** `C1` + `C2` là **một mệnh đề công thức**, đo bằng **một bộ điểm phân biệt trên một bản ghi** là đủ kết luận (luật khóa 3 + 4: chỉ thêm biến thể khi chính vế expected áp cho nhiều biến thể **và** SRS quy định kết quả khác nhau — ở đây SRS không quy định kết quả khác nhau theo bộ điểm). **Cấm biến thành regression nhiều bộ điểm / nhiều bản ghi / nhiều trạng thái.**

---

## 4. Tiền đề tối thiểu + tài khoản / vai trò

### 4.1 Môi trường

| Hạng mục | Giá trị |
|---|---|
| Env đo | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn` |
| Mã xác thực 6 số | MailHog `http://18.143.165.120:8025/` (env chưa tích hợp email thật — cấm log "không nhận được mã" thành bug) |
| Vân tay bản dựng | **Đo lại đầu phiên** (bó mã FE + `last-modified` + `etag`). Mốc 2026-08-06 18:44: `HTPLDN · V1.0.8`, `assets/index-DIABnbIr.js`, `last-modified Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"` |
| Giới hạn hiệu lực | Verdict chỉ có giá trị cho env + bản dựng đã đo; phải ghi câu giới hạn vào kết quả |

### 4.2 Vai trò được đánh giá theo SRS

`:1198` PRE-03 `Role ∈ {CB_NV, DN}` · `:1216` scope `role='CB_NV' → VU_VIEC.don_vi_id = current_user.don_vi_id`.

| Vai trò | Tài khoản | Mật khẩu | Ghi chú |
|---|---|---|---|
| **CB NV Trung ương — ưu tiên ra verdict** | `cbnv_tw` | `Test@1234` | Tài khoản đã dùng đo lô 06/08 (`BAN-DUNG.md:19`) |
| Dự phòng cùng vai trò + cùng cấp (Rule 7) | `cbnv_tw_01` → `cbnv_tw_02` → `cbnv_tw_03` | `Test@1234` | **Chỉ fallback CÙNG vai trò + CÙNG cấp**; khai account thực dùng |
| CB NV Địa phương (nếu bản ghi tiền đề thuộc ĐP) | `cbnv_dp_01` (`cbnv_dp` FAIL login từ 03/08) | `Test@1234` | Bắt buộc dùng đúng đơn vị để thoả `:1216` |
| Dựng tiền đề (KHÔNG ra verdict) | `cbpd_tw_01` / `cbpd_dp_01` (phê duyệt) · tài khoản DN gửi hồ sơ · người được phân công | `Test@1234` | Chỉ dùng đẩy VV lên "Hoàn thành" |
| **CẤM ra verdict** | `admin` | — | Quyền rộng che lỗi phân quyền/scope |

### 4.3 Dữ liệu tiền đề — điều kiện cứng

**Cần đúng 1 vụ việc: thuộc đơn vị của tài khoản đo · đang ở `HOAN_THANH` ("Hoàn thành") · CHƯA có bản ghi đánh giá loại `CB_NV`.**

🔴 **Vì sao bắt buộc `HOAN_THANH`, không dùng `DA_DANH_GIA`:** ở chế độ **cán bộ**, bảng nút hành động `:1751` chỉ khai `[Đánh giá]` cho `HOAN_THANH` và **không có** dòng `DA_DANH_GIA`, trong khi `:1197`/`:1734` lại gồm cả `DA_DANH_GIA` (§2.4 — mâu thuẫn đang ở tay BA). Đo trên `DA_DANH_GIA` sẽ **rơi thẳng vào vùng mâu thuẫn** ⇒ không kết luận được `C1`. **Phiếu ghi "Hoàn thành **hoặc** Đã đánh giá" là *hoặc*** ⇒ chọn nhánh không tranh chấp.

🔴 **Bản ghi bị tiêu hao sau 1 lần đo:** `:1219` chặn đánh giá lần 2 cùng loại người, `:2114` `UNIQUE(vu_viec_id, loai_nguoi_danh_gia)`, `:1222` chuyển VV sang `DA_DANH_GIA`. ⇒ **Mỗi bản ghi chỉ chạy được `C1`/`C2` đúng một lần.** Nếu phải chạy lại (đo hỏng, phép đo mâu thuẫn) thì **phải có bản ghi thứ hai đã dựng sẵn** — chuẩn bị trước, đừng để kẹt giữa chừng.

| Ứng viên tái dùng (ưu tiên — Flow 04 §Giai đoạn B bước 3) | Việc phải xác minh TRƯỚC khi tính là tiền đề |
|---|---|
| `VV-STP-AG-20260806-005` (`0dfb2b25-…`) — DN An Giang, ghi nhận 06/08 là **"Hoàn thành", chưa có đánh giá nào** | 🔴 **Phải kiểm lại trạng thái ngay đầu phiên.** Lô F3 ngày 07/08 đo **nhánh doanh nghiệp** trên đúng bản ghi này; nếu DN đã chấm thì VV **đã chuyển `DA_DANH_GIA`** (`:1222`) ⇒ **không dùng được** cho `C1` (rơi vào vùng mâu thuẫn `:1751`). Ngoài ra bản ghi thuộc **An Giang** ⇒ phải đo bằng `cbnv_dp_01`, không phải `cbnv_tw` |
| `VV-BTP-TW-20260806-003` / `-004` | ❌ **KHÔNG dùng** — đã ở "Đã đánh giá" và **đã có** đánh giá loại `CB_NV` ⇒ `:1219` chặn |

**Nếu không có bản ghi hợp lệ → dựng mới theo luồng chuẩn 8 bước:**
`DN gửi hồ sơ → CB NV cùng địa bàn tiếp nhận → kiểm tra hồ sơ kết luận Đạt → phân công người xử lý → cập nhật kết quả → trình phê duyệt → CB PD duyệt → cập nhật kết quả cuối → "Hoàn thành"`.
Cặp đã chạy được: DN `0209888006` gửi → `cbnv_dp_01` tiếp nhận + kiểm tra → phân công `nht_ag_uat2` → `nht_ag_uat2` chấp nhận + cập nhật kết quả → trình phê duyệt → `cbpd_dp_01` duyệt → `cbnv_dp_01` cập nhật KQ cuối → "Hoàn thành".
⚠️ **Đơn vị Hà Nội đã hỏng 2 lần khi dựng** (cấp TW không tiếp nhận được hồ sơ DN Hà Nội; bảng gợi ý phân công Sở Tư pháp Hà Nội rỗng) — đừng chọn địa bàn đó.
**Cấm ghi thẳng DB, cấm đoán endpoint seed.** Có seed thì khai: **đổi bản ghi nào · đổi gì · trên env nào**.

> ⚠️ **Tiền đề tạo được mà không chuẩn bị ⇒ CẤM chốt** (kể cả chốt bằng ô trống).

---

## 5. Đường đo + đối chứng độc lập

### 5.1 Đường UI ngắn nhất (một đường duy nhất cho `C1` + `C2`)

1. Tải lại trang bằng địa chỉ (không tái dùng tab cũ chạy bó mã cũ), ghi vân tay bản dựng.
2. Đăng nhập **UI thật** bằng tài khoản CB NV đúng đơn vị của bản ghi tiền đề. Ghi account thực dùng.
3. Click menu **"Quản lý vụ việc hỗ trợ pháp lý"** (`srs-v3.5.md:641`) → `SCR-V.I-01` (`srs-fr-05-vu-viec.md:1626`).
4. Tìm theo **mã vụ việc** tiền đề → **Xem chi tiết** (`SCR-V.I-03`, `:1715`) → mở **Nhóm 8 — Đánh giá** / bấm nút mở đánh giá.
5. **Trước khi nhập:** chụp ảnh ô điểm tổng ở trạng thái chưa nhập gì (bằng chứng cho `C2` — người dùng không phải tự điền).
6. Nhập **4 · 8 · 9** (chất lượng tư vấn · đúng thời hạn · thái độ phục vụ) + chuỗi nhận xét mốc-giờ duy nhất dạng `QA-DGKQ-<YYYYMMDD-HHMM>`. **Không chạm vào ô điểm tổng.**
7. **Gửi bằng UI thật** (nút gửi của form đánh giá — phiếu gọi là "Lưu đánh giá"; **không prescribe nhãn nút**). Hành động đang tranh chấp **phải** thực hiện bằng UI, không thay bằng gọi máy chủ.
8. **Tải lại trang bằng địa chỉ** (không dùng lại màn cũ) → mở lại Nhóm 8 → **đọc điểm tổng bằng `innerText`**.
   - **Kỳ vọng số học của `C1`: điểm tổng = 7** (= (4+8+9)/3). Chuỗi hiển thị có thể là `7` / `7.0` / `7,0` — cả ba đều thoả `C1` (định dạng thuộc `C3` = GAP).

> **Không bấm gửi lặp** để dò double-submit — `Cn` và SRS không yêu cầu hành vi khi bấm lặp.
> **Không cài bộ bắt thông báo** trừ khi cần chính chuỗi thông báo làm bằng chứng thao tác đã chạy; nếu cài thì cài **TRƯỚC** khi bấm, dùng `innerText`, **CẤM lọc trùng**, đếm theo **mốc giờ khác nhau** (không đếm theo độ dài mảng), và **đếm kèm số lời gọi song song**. Nội dung thông báo **KHÔNG** là tiêu chí chấm của `Cn` nào (bảng `:1773`–`:1785` không có dòng cho thao tác đánh giá).

### 5.2 Đối chứng độc lập (bắt buộc — đúng 1 đường thứ hai)

- Bằng **chính phiên đăng nhập CB NV vừa dùng** (JWT là cookie), đọc lại **bản ghi đánh giá của đúng vụ việc đó** từ máy chủ, đối chiếu **từng trường** với chữ trên màn ở bước 8: `diem_chat_luong = 4` · `diem_thoi_gian = 8` · `diem_thai_do = 9` · **`diem_tong = 7`** · `nhan_xet` = đúng chuỗi mốc-giờ đã nhập · `loai_nguoi_danh_gia = 'CB_NV'` (`:2116`).
- 🔴 **CHƯA BIẾT ĐƯỜNG DẪN API — phải tra danh sách endpoint TRƯỚC khi dùng.** Cấm đoán khóa JSON / ID / endpoint. Đọc bản mô tả API mà hệ thống công bố (`/api/docs-json`, đọc được không cần đăng nhập) để lấy **đúng** đường dẫn đọc chi tiết vụ việc / đọc đánh giá, rồi mới gọi.
- **Không** gọi bằng `admin`, không gọi bằng vai trò khác.
- **Bấm lại cùng một nút KHÔNG tính là đường thứ hai.** Hai đường khớp thì **dừng**, không mở đường thứ ba.
- 🔴 **Hai đường mâu thuẫn ⇒ CHƯA ĐƯỢC CHỐT** — ghi cả hai, hỏi user.

### 5.3 Những gì CẤM chạy trong case này

- Không đo chặn điểm ngoài 0–10 (`:1240` E2), không đo chặn đánh giá lần 2 (`:1219`/`:1241` E3), không đo chứng âm phạm vi DN/đơn vị khác (`:1242` E4) — **expected không nhắc**, thuộc case khác.
- Không đo chuyển trạng thái sang "Đã đánh giá" (`:1222`) như một tiêu chí — đó là **hệ quả**, không phải vế expected.
- Không đo điểm trung bình tư vấn viên (vùng mâu thuẫn `:1223` ↔ `:1233`, đã gửi BA).
- Không đo nhánh doanh nghiệp (đó là `DGKQHTVV_01`).
- Không lặp bộ điểm khác / bản ghi khác để "chắc" — trừ khi phép đo đầu hỏng và phải chạy lại (khi đó phải khai rõ lý do chạy lại).

---

## 6. Bẫy chấm sai

### 6.1 Bẫy **PASS oan**

1. 🔴 **Bộ điểm không phân biệt được công thức.** Vòng trước dùng **9 · 8 · 10** → trung bình = **9**, mà **median cũng = 9** ⇒ một cách tính sai (lấy trung vị) vẫn ra đúng số. Tương tự mọi bộ 3 số bằng nhau (8·8·8) hay đối xứng. **Bắt buộc dùng bộ phân biệt — 4 · 8 · 9 → trung bình 7 ≠ median 8 ≠ min 4 ≠ max 9 ≠ tổng 21.**
2. 🔴 **Chỉ nhìn ô "Điểm tổng" trên form TRƯỚC khi lưu rồi Pass.** Số trên form có thể do FE tính tạm mà máy chủ lưu số khác. **Chỉ số đọc lại SAU KHI TẢI LẠI TRANG + đối chứng bản ghi mới chốt được.**
3. 🔴 **Pass vì thấy thông báo "thành công" / nhãn trạng thái đổi sang "Đã đánh giá" / dòng thời gian có mục đánh giá.** Cả ba dấu hiệu này **đã từng đúng trong khi dữ liệu vẫn sai** ở các vòng trước. Không có quyền chốt.
4. 🔴 **Tab mở lâu vẫn chạy bó mã FE cũ** ⇒ đo bản cũ, Pass oan. **Tải lại trang bằng địa chỉ + ghi vân tay bản dựng.**
5. ⚠️ **Bộ bắt thông báo lọc trùng** che double-submit (2 lần gửi) ⇒ Pass oan. **CẤM lọc trùng**, đếm theo mốc giờ + đếm số lời gọi.
6. ⚠️ **`textContent` thay vì `innerText`** ⇒ gom node ẩn, đọc nhầm số cũ còn nằm trong DOM.
7. ⚠️ **Pass bằng quan sát tĩnh** ("thấy ô điểm tổng có sẵn công thức rồi"). Vế bug là **hành động** ⇒ bắt buộc nhập + gửi thật bằng UI.

### 6.2 Bẫy **FAIL oan**

1. 🔴 **FAIL vì ô điểm tổng không tự đổi số ngay khi đang gõ 3 điểm.** SRS **im lặng** về thời điểm tính; `:1220` đặt phép tính ở **bước xử lý khi gửi**. Chỉ cần **giá trị lưu và đọc lại** đúng trung bình là đạt `C1`/`C2`.
2. 🔴 **FAIL vì điểm tổng hiện `7` thay vì `7.0` / `7,0`** (hoặc ngược lại). Thuộc `C3` = **GAP**, SRS im lặng cho UC67 (`:2462` loại trừ UC67).
3. 🔴 **FAIL vì nút gửi không mang chữ "Lưu đánh giá".** SRS **không quy định** nhãn nút trong Accordion 8 (`:1751` chỉ nói `[Đánh giá] … Mở Accordion 8. Gửi → DA_DANH_GIA`). Describe, không prescribe.
4. 🔴 **FAIL vì VV đang ở "Đã đánh giá" mà chế độ cán bộ không cho đánh giá tiếp.** Vùng **mâu thuẫn SRS** `:1751` ↔ `:1197`/`:1734` (§2.4) ⇒ **CẤM chấm Fail**, ghi câu hỏi BA. Đây chính là lý do tiền đề khóa cứng ở `HOAN_THANH`.
5. 🔴 **FAIL vì điểm trung bình tư vấn viên không đổi.** `:1233` (Postconditions *"Điểm TVV được cập nhật"*) **ngược** `:1223` + `:2462` (UC67 không trigger; trigger nằm ở FR-IV). **Đã gửi BA**, cố ý bỏ trống tiêu chí.
6. 🔴 **FAIL vì không ai nhận được thông báo sau khi đánh giá.** Bảng "Thông báo riêng SCR-V.I-03" (`:1773`–`:1785`, 11 tình huống) **không có dòng nào** cho thao tác đánh giá.
7. ⚠️ **FAIL vì ô điểm tổng không có dấu sao `*`.** `srs-v3.5.md:585` (UI-13): trường **hệ thống tự gán không** gắn dấu sao dù bắt buộc. `diem_tong` là `Y (auto)` (`:1208`) ⇒ **không có dấu sao là ĐÚNG**.
8. ⚠️ **FAIL vì bị chặn khi bấm đánh giá lần 2.** `:1219` + `:1241` (`ERR-DG-VV-03` *"Bạn đã đánh giá vụ việc này rồi"*) quy định phải chặn ⇒ **đúng đặc tả**, và cũng **ngoài phạm vi** `Cn` của case này.
9. ⚠️ **FAIL vì đo bằng tài khoản sai đơn vị** rồi không thấy vụ việc / bị từ chối. `:1216` bắt `VU_VIEC.don_vi_id = current_user.don_vi_id` ⇒ đó là **tiền đề sai**, không phải lỗi.

### 6.3 Bug mới phát sinh trong lúc verify

- Bug **tự lộ** trong bước bắt buộc của `C1`/`C2` (nhập → gửi → đọc lại), SRS nói rõ, xác nhận được bằng artifact đang có ⇒ **tra trùng rồi log riêng**; chỉ kéo verdict `C1`/`C2` về Reopen nếu nó làm vế đó không đạt hoặc chặn phép đo.
- Hiện tượng chỉ thấy sau khi **đổi màn / role / bộ lọc / seed** hoặc trên bản ghi do QA tự tạo ngoài vế `Cn` ⇒ **ghi candidate một dòng**, **không điều tra**, **không kết luận** (kể cả kết luận "không phải lỗi").

---

## 7. Kết luận sơ bộ — route (CHƯA CÓ VERDICT)

| Vế | Quan hệ | Route | Được chấm Pass/Reopen? |
|---|---|---|---|
| `C1` — điểm tổng = trung bình cộng 3 điểm | **MATCH** — SRS khớp expected ở **4 chỗ** (`:1208`, `:1220`, `:1734`, `:2120`) | **TEST** | ✅ Có |
| `C2` — hệ thống **tự** sinh điểm tổng, người dùng không nhập | **MATCH** (`:1208` `Y (auto)`, `:1734` `AVG auto`, `:2120` `Auto = AVG(...)`, + `srs-v3.5.md:585`) | **TEST** | ✅ Có |
| `C3` — làm tròn / chữ số thập phân | **GAP** — SRS im lặng cho UC67; `:2462` loại trừ UC67 khỏi quy tắc làm tròn duy nhất | **BA** | ❌ Cấm Pass, cấm Reopen |

**⇒ Phải sang Giai đoạn B** để verify `C1` + `C2`. **Không có DIFF nào** giữa SRS và expected ở công thức ⇒ nếu web tính đúng trung bình cộng thì `C1`/`C2` đạt.

**Hệ quả logic đã thấy trước (Flow 04 §Ca biên):** vì còn `C3` = `GAP`, verdict trần của case là **Cần BA** chứ không phải "Pass" thuần — trừ khi người điều phối quyết định `C3` nằm **ngoài** expected (expected chỉ nói *"trung bình cộng 3 điểm"*, không nói gì về làm tròn). **Quyết định này phải do người điều phối chốt trước khi ra verdict, và phải ghi rõ lý do** — agent đo **không được tự nới**.

**Câu hỏi BA phải nêu (soạn sẵn, chờ số đo điền vào `…`):**

1. **Điểm tổng của đánh giá vụ việc (UC67, thang 0–10) hiển thị và lưu với mấy chữ số thập phân, làm tròn theo quy tắc nào?** Quy tắc làm tròn duy nhất trong SRS (`srs-fr-05-vu-viec.md:2462`) chỉ áp cho thang tư vấn viên 1–5 và **loại trừ UC67 bằng chữ**. *(Web hiện tại khi 3 điểm chia hết cho 3: `…`; khi không chia hết: `…`)*
2. **Vụ việc đang ở "Đã đánh giá" thì phía CÁN BỘ còn được vào đánh giá không?** Bảng nút hành động chế độ cán bộ (`:1751`) chỉ khai `[Đánh giá]` cho `HOAN_THANH`, trong khi `:1197` (PRE-02) và `:1734` (điều kiện hiển thị Accordion 8) đều gồm cả `DA_DANH_GIA`. *(Đã né bằng cách khóa tiền đề ở "Hoàn thành" — nhưng mâu thuẫn vẫn cần chốt.)*

> Nếu đo xong `C1`/`C2` đạt và `C3` chỉ là chuyện định dạng: `WEB HIỆN TẠI` ghi **"đúng kỳ vọng đối tác"**, câu hỏi BA nêu rõ mục đích là **bổ sung điều này vào đặc tả — KHÔNG phải chặn bàn giao** (Flow 04 §Nội dung kết quả tối thiểu, vế `GAP`).
