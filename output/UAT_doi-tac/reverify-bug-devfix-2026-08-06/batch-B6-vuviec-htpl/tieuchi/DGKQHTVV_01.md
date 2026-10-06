# Tiêu chí verify — DGKQHTVV_01

```
Mã case: DGKQHTVV_01 (dòng 64, tab `bug`)      Thời điểm viết: 2026-08-06 13:04
Chức năng: Đánh giá kết quả hỗ trợ vụ việc (Nhóm 8 — Đánh giá, màn chi tiết vụ việc)
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: HTPLDN · V1.0.8 (tự đo 2026-08-06 16:20)
  Dấu vân tay tự đo: assets/index-DIABnbIr.js · assets/index-DVlgOkLg.css ·
  GET / last-modified Thu, 06 Aug 2026 07:13:15 GMT (14:13:15 giờ VN) · etag W/"6a74340b-428" · nginx/1.27.5
```

> **Khai theo flow 04 (dòng 88-90) — đã đọc hồ sơ QA nội bộ đợt trước, chứa SỐ ĐO CŨ:**
> `output/UAT_doi-tac/reverify-week-3/cond/DGKQHTVV_01.md` ·
> `output/UAT_doi-tac/reverify-week-3/reverify-audit/DGKQHTVV_01/audit.md` ·
> entry `BUG-DGKQHTVV_01 [CLOSED]` trong `reverify-week-3/bug-reports/vu-viec/Pass-bug-report-UAT-tuan-3.md` ·
> dòng kết quả round 10 trong `reverify-week-3/dev-fix-reverify-round-10-2026-07-30/KET-QUA-reverify-24-case-reopent.md`.
> **Mục 4 dưới đây suy từ ĐẶC TẢ, không lấy số đo/ngưỡng của các hồ sơ trên.**
> ⚠️ Số dòng SRS trong hồ sơ cũ (1186-1187 / 1204-1205 / 1723 / 1740 / 1747) **đã lệch** — file
> `srs-fr-05-vu-viec.md` được cập nhật 2026-08-04. Số dòng trong file này lấy bằng cách **mở file đọc lại
> ngày 2026-08-06**.

---

## 1. Đối tác phản ánh

Case đã **đổi triệu chứng qua các vòng** — tách 2 vế, verdict phải xét cả hai:

| Vế | Nguồn | Nội dung |
|---|---|---|
| **(a) Không có điểm vào thao tác đánh giá** | Đối tác vòng 1 (ô *Kết quả thực tế*) + TKM retest 27/7 | "Hệ thống không hiển thị nút chức năng mặc dù bản ghi ở trạng thái phù hợp" → TKM retest 27/7: *"Hệ thống vẫn chưa có nút chức năng"*. Vụ việc đã "Hoàn thành", mở Nhóm 8 — Đánh giá chỉ thấy trạng thái rỗng, không có gì bấm được để đánh giá. **⚠️ Video vòng 2 (05/08/2026, bản "HTPLDN · V1.0.5" env đối tác) cho thấy vế này ĐÃ HẾT ở phía đối tác**: nút **[⭐ Đánh giá]** hiện rõ ở góc trên phải + mở được hộp thoại "Đánh giá chất lượng" đủ 3 tiêu chí + nhận xét (frame `t000.00s`, `t001.55s`). |
| **(b) Gửi được nhưng đánh giá KHÔNG lưu** | QA vòng trước (ô *Kết quả verify*) **+ nay có bằng chứng ĐỐI TÁC** (video vòng 2) | "Hệ thống hiển thị thông báo thành công nhưng Đánh giá không được lưu vào Nhóm 8". Video vòng 2 tái hiện đúng: gửi → thông báo xanh **"Đã đánh giá vụ việc"** (`t002.58s`) → trạng thái đổi sang **"Đã đánh giá"** + Dòng thời gian có thêm mục *Đánh giá 05/08/2026 09:10* (`t010.09s`) — **nhưng Nhóm 8 "Đánh giá" vẫn là "Chưa có thông tin"** (`t006.05s`, `t008.07s`, `t010.09s`). ⇒ Triệu chứng chính xác **không phải** "không lưu gì cả", mà là **đánh giá không đọc lại được ở Nhóm 8** dù trạng thái + nhật ký đã ghi nhận. |

**Quan hệ 2 vế:** (b) là **vế quyết định**. "Có nút" mà "không lưu" = fix mới nửa đường → theo flow 04 §Ca biên
(dòng 320-321) còn ≥1 vế lỗi ⇒ **Reopen**, KHÔNG được Pass. Cấm Pass bằng quan sát tĩnh *"thấy nút đã có rồi"*
(flow dòng 219) — bắt buộc chạy tới bước gửi và **đọc lại sau khi tải lại trang**.

### Bằng chứng đã xem

**① Ảnh vòng 1 — `partner-evidence/DGKQHTVV_01.jpg`** (218.486 byte, ảnh tĩnh, đọc full-res).

**Có đúng case này không → CÓ, khớp.** Màn *Vụ việc hỗ trợ pháp lý / Chi tiết* trên env đối tác, nhóm
**"Đánh giá"** đang mở, hiển thị hình "trống" + chữ **"Chưa có thông tin"**, không có phần tử bấm được nào
trong nhóm. Khớp mô tả case ("Mở Nhóm 8 – Đánh giá") + khớp ô *Kết quả thực tế*.

**② Video vòng 2 — `partner-evidence/DGKQHTVV_01_v2.webm`** (3.006.561 byte, 1920×1080, ~15 giây).
Trích frame: `partner-evidence/frames-DGKQHTVV_01-v2/` (quét `--every 2`, soi kỹ `--from 0 --to 8 --every 0.5`).
**Frame đã MỞ XEM:** `t000.00s` · `t001.55s` · `t002.07s` · `t002.58s` · `t003.10s` · `t004.13s` · `t006.05s` ·
`t008.07s` · `t010.09s` · `t014.14s`.

**Có đúng case này không → CÓ, khớp** (cùng chức năng, cùng màn, cùng vai trò). Diễn biến đọc được:

| Mốc | Thấy gì |
|---|---|
| `t000.00s` – `t001.55s` | Hộp thoại **"Đánh giá chất lượng"** đang mở, đủ 3 ô bắt buộc *Điểm chất lượng (0-10)* = **5.0** · *Điểm thời gian (0-10)* = **5.5** · *Điểm thái độ (0-10)* = **7.5** + ô *Nhận xét* = **"abc"** (bộ đếm `3 / 2000`) + 2 nút [Hủy] [Xác nhận]. Nền sau: mã **VV-BTP-TW-2…**, nhãn **"Đã hoàn thành"** + nút **[⭐ Đánh giá]** góc trên phải, thanh tiến trình đang ở bước 9 **"Hoàn thành"** |
| `t002.07s` | Con trỏ trên [Xác nhận], hộp thoại bắt đầu đóng |
| **`t002.58s` – `t004.13s`** | **Thông báo xanh có dấu ✓ — nguyên văn: "Đã đánh giá vụ việc"** (đúng **1** thông báo, 1 mốc giờ). Tiêu đề đổi thành **VV-BTP-TW-20260713-001 — TKM test** + nhãn **"Đã đánh giá"**; góc phải còn **"Đã hoàn thành"**, **nút [Đánh giá] đã biến mất**; thanh tiến trình 10/10 bước đều ✓ |
| **`t006.05s` · `t008.07s`** | Cuộn xuống nhóm **"Đánh giá"** (đang mở): vẫn hình "trống" + **"Chưa có thông tin"**. Ở `t008.07s` đối tác **bôi xanh chính chữ "Chưa có thông tin"** để nhấn mạnh |
| **`t010.09s` — KHOẢNH KHẮC QUYẾT ĐỊNH** | Nhóm "Đánh giá" = **"Chưa có thông tin"**, trong khi **Dòng thời gian ngay bên dưới ĐÃ có mục *"Đánh giá — 05/08/2026 09:10 — Cán bộ NV Trung ương"*** (các mục cũ: Hoàn thành 27/07/2026 15:11 · Phê duyệt 27/07/2026 14:44 · Trình phê duyệt / Cập nhật kết quả 27/07/2026 14:43 — `huongcg`) |
| `t014.14s` | Cuộn lại đầu trang: **VV-BTP-TW-20260713-001** · nhãn **"Đã đánh giá"** · **"Đã hoàn thành"** · không còn nút [Đánh giá] |

**Đọc thêm được từ video (ảnh vòng 1 không có):** Tiêu đề *TKM test* · Loại hình *LHHT_TKM* · Kênh tiếp nhận
*Trực tiếp* · Lĩnh vực *Thuế* · Ưu tiên *Trung bình* · Ngày tiếp nhận *13/07/2026 16:47* · Thời hạn xử lý
*03/08/2026*.
**Đối tác KHÔNG tải lại trang** trong suốt 15 giây (địa chỉ không đổi, không có nhịp tải lại) — nhãn trạng thái
và Dòng thời gian **tự cập nhật**, chứng tỏ màn **đã lấy lại dữ liệu** sau khi gửi mà Nhóm 8 vẫn rỗng.
⇒ Video **chưa** chứng minh trạng thái sau khi **tải lại trang** — tiêu chí `b2` mục 4 vẫn là phép thử bắt buộc
của giai đoạn B.

### ⚠️ Ảnh vòng 1 và video vòng 2 KHÔNG cùng bản ghi / không cùng bản dựng (flow dòng 105)

| Chiều | Ảnh vòng 1 | Video vòng 2 | Lệch? |
|---|---|---|:-:|
| Bản ghi | `/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — **không lộ mã VV** | `/vu-viec/43ec038d-36a0-44c0-ad6d-f21bec32a207` — **VV-BTP-TW-20260713-001** ("TKM test") | **LỆCH — 2 vụ việc khác nhau** |
| Vai trò | Cán bộ NV Trung ương · `CB_NV_TW` · BTP·TW | Cán bộ NV Trung ương · `CB_NV_TW` · BTP·TW | Không |
| Bản dựng | **HTPLDN · V1.0** | **HTPLDN · V1.0.5** | **LỆCH** |
| Thời điểm | 2026-07-10 09:57 | 2026-08-05 09:10 | **LỆCH ~26 ngày** |
| Môi trường | `htpldn-uat.ospgroup.vn` | `htpldn-uat.ospgroup.vn` | Không |

⇒ Hai vòng bằng chứng **không so trực tiếp với nhau được**; chúng là **2 lát cắt thời gian của cùng một chức
năng**. Cách đọc đúng: trên bản **V1.0** (10/07) vế (a) đúng như đối tác báo; tới bản **V1.0.5** (05/08) vế (a)
đã hết nhưng **vế (b) lộ ra**. Đây chính là lý do case đổi triệu chứng qua các vòng.

### 3 thiếu sót của ảnh vòng 1 — video vòng 2 lấp được CẢ 3

1. ~~Không thấy mã vụ việc~~ → **đã lấp**: `VV-BTP-TW-20260713-001` (lưu ý: là **bản ghi khác** với ảnh vòng 1).
2. ~~Không thấy vùng thanh hành động~~ → **đã lấp**: nút **[⭐ Đánh giá]** nằm ở **góc trên phải**, cạnh nhãn
   "Đã hoàn thành" (**không** phải thanh cố định ở đáy như suy đoán ban đầu). Sau khi gửi thì nút biến mất.
3. ~~Trạng thái chỉ là suy ra~~ → **đã lấp**: đọc trực tiếp nhãn **"Đã hoàn thành"** → sau khi gửi đổi thành
   **"Đã đánh giá"**; thanh tiến trình 10 bước đều ✓.

**Lệch env giữa đối tác và vòng verify:** cả 2 bằng chứng đều chụp trên `htpldn-uat.ospgroup.vn` (env nghiệm
thu đối tác), vòng này đo trên `18.143.165.120.nip.io` (env nội bộ) → đây là **giới hạn hiệu lực** của verdict,
ghi ở mục 6, **không phải GAP**.

---

## 2. Đặc tả nói gì

**Nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md`
(đã mở file đọc ngày 2026-08-06; số dòng trích dưới đây là số dòng thật của bản này).

> **Lưu ý chọn file:** `srs-fr-08-danh-gia.md` là module **"Theo dõi Đánh giá Hiệu quả HTPL"** (đợt đánh giá,
> kế hoạch, người đánh giá, báo cáo — FR-VI-01…10) — **KHÁC** case này. Chức năng "Đánh giá kết quả hỗ trợ vụ
> việc" (Nhóm 8 trên màn chi tiết vụ việc) nằm ở **FR-V.I-17 / UC67** trong `srs-fr-05-vu-viec.md`. Đặc tả nói
> rõ hai thứ này không trộn: dòng 1226 — *"UC67 đánh giá từng VV cụ thể, KHÔNG tự tổng hợp lên nhóm VI."*

### 2.1 AI được đánh giá (vế "tác nhân")

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1190` | "**Mô tả:** CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc." |
| `srs-fr-05-vu-viec.md:1198` | "\| PRE-03 \| Role ∈ {CB_NV, DN} (theo CSV UC67) \|" |
| `srs-fr-05-vu-viec.md:1215` | "\| 1 \| Kiểm tra quyền: role ∈ {CB_NV, DN} \| BR-AUTH-01 \|" |
| `srs-fr-05-vu-viec.md:1216` | "\| 2 \| Validate scope theo role: nếu role='DN' → `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id`; nếu role='CB_NV' → `VU_VIEC.don_vi_id = current_user.don_vi_id` \| BR-AUTH-03/04, BR-AUTH-08 \|" |
| `srs-fr-05-vu-viec.md:2116` | "\| 4 \| loai_nguoi_danh_gia \| text \| Y \| CHECK IN ('CB_NV','DN') \| — \| Loại người đánh giá (theo CSV UC67: chỉ CB Nghiệp vụ và Doanh nghiệp) \|" |
| `srs-fr-05-vu-viec.md:2108` | "Mỗi VV có tối đa 1 đánh giá từ CB NV và 1 từ DN — UNIQUE (vu_viec_id, loai_nguoi_danh_gia)." |

⇒ **CẢ HAI** vai trò đều được đánh giá, độc lập nhau, mỗi loại **đúng 1 lần**/vụ việc. Đây là **tập enum ĐÓNG
2 giá trị** → đặc tả **nói rõ** (không im lặng): vai trò khác (Người hỗ trợ, TVV, CB Phê duyệt, QTHT) **không**
thuộc tác nhân đánh giá. Ô *Tác nhân* của đối tác ("CB Nghiệp vụ TW/BN/ĐP **hoặc** Doanh nghiệp") **khớp** đặc tả.
Ràng buộc phạm vi: CB NV phải **cùng đơn vị** vụ việc (`don_vi_id`), DN phải là **chủ** vụ việc
(`doanh_nghiep_id`). Ngoại lệ cấp TW xem toàn quốc: `srs-fr-05-vu-viec.md:2358` — *"Không có exception ngoại trừ
QTHT và Cán bộ Trung ương (TW xem toàn quốc theo BR-AUTH-03/04…)"*.

### 2.2 Trạng thái nào thì có chức năng · điểm vào ở đâu

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1197` | "\| PRE-02 \| VV ở trạng thái HOAN_THANH hoặc DA_DANH_GIA \|" |
| `srs-fr-05-vu-viec.md:1734` | "\| 11 \| content \| Accordion 8 — Đánh giá (gộp MH-05.9) \| C23 \| diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet \| **CB NV/DN nhập trực tiếp** \| **Khi VV ở HOAN_THANH hoặc DA_DANH_GIA** \|" |
| `srs-fr-05-vu-viec.md:1751` | "\| HOAN_THANH \| [Đánh giá] (gộp MH-05.9) \| CB NV/DN \| Mở Accordion 8. Gửi → DA_DANH_GIA \|" |
| `srs-fr-05-vu-viec.md:1758` | "- Nếu user **không thuộc vai trò yêu cầu** → nút **không hiển thị** (không phải mờ đi)" |
| `srs-fr-05-vu-viec.md:1759` | "- Nếu vai trò đúng nhưng **trạng thái / phạm vi không khớp** → nút **hiển thị nhưng mờ đi + tooltip** giải thích điều kiện chưa đạt" |
| `srs-fr-05-vu-viec.md:1809` (chế độ DN) | "\| Nhóm 8 — Đánh giá \| Cho phép nhập khi vụ việc ở "Hoàn thành" / "Đã đánh giá" + DN chưa đánh giá. Sau khi đánh giá → chuyển sang chế độ chỉ đọc \|" |
| `srs-fr-05-vu-viec.md:1811` (chế độ DN) | "\| Thanh thao tác \| Chỉ 2 nút DN được phép: **[Bổ sung hồ sơ]** (khi trạng thái = "Yêu cầu bổ sung"…); **[Đánh giá]** (khi trạng thái = "Hoàn thành" / "Đã đánh giá" + chưa đánh giá). Ẩn toàn bộ nút nội bộ \|" |

⇒ Bảng thành phần màn hình (dòng 1722-1736) và bảng nút theo trạng thái (dòng 1740-1754) là **bảng liệt kê
đóng có cột "Điều kiện hiển thị"** → theo flow dòng 326-327 đây là đặc tả **NÓI RÕ**, không phải im lặng.
Kỳ vọng đối tác ("phải có chức năng đánh giá khi bản ghi ở trạng thái phù hợp") **khớp** đặc tả ⇒ theo bảng rẽ
nhánh flow (dòng 125): **đo được, không phải cần BA**.

### 2.3 Biểu mẫu gồm gì · gửi xong lưu gì · hiển thị lại ở đâu

| Dòng | Nguyên văn / nội dung |
|---|---|
| `srs-fr-05-vu-viec.md:1205-1209` | Inputs: `diem_chat_luong` 0-10 (Y) · `diem_thoi_gian` 0-10 (Y) · `diem_thai_do` 0-10 (Y) · `diem_tong` "Y (auto)" = "AVG(3 điểm)" · `nhan_xet` text long (N) |
| `srs-fr-05-vu-viec.md:1220` | "\| 6 \| Xác nhận điểm 0-10; tính điểm tổng = trung bình 3 điểm \|" |
| `srs-fr-05-vu-viec.md:1221` | "\| 7 \| Tạo bản ghi DANH_GIA_VU_VIEC \|" |
| `srs-fr-05-vu-viec.md:1222` | "\| 8 \| Chuyển VV → DA_DANH_GIA (chỉ lần đánh giá đầu tiên; nếu VV đã DA_DANH_GIA thì giữ nguyên) \| SM-VUVIEC \|" |
| `srs-fr-05-vu-viec.md:1224` | "\| 10 \| Ghi LICH_SU_VU_VIEC: hanh_dong='DANH_GIA', vai_tro=role \| BR-DATA-05 \|" |
| `srs-fr-05-vu-viec.md:1230-1233` | "**Postconditions:** - Đánh giá VV được ghi nhận - VV chuyển trạng thái DA_DANH_GIA - Điểm TVV được cập nhật" |
| `srs-fr-05-vu-viec.md:1245` | "**Given** CB NV/DN đánh giá VV **When** nhập điểm + nhận xét **Then** lưu đánh giá, VV → DA_DANH_GIA" |
| `srs-fr-05-vu-viec.md:2113-2123` | Entity `DANH_GIA_VU_VIEC` 11 cột: `vu_viec_id` (UNIQUE cùng `loai_nguoi_danh_gia`) · `nguoi_danh_gia_id` · `loai_nguoi_danh_gia` · 3 điểm CHECK BETWEEN 0 AND 10 · `diem_tong` "Auto = AVG(…)" · `nhan_xet` max 2000 · `ngay_danh_gia` · `don_vi_id` |
| `srs-fr-05-vu-viec.md:1735` | "\| 12 \| sidebar \| Dòng thời gian (Timeline) \| C18 \| Lịch sử xử lý từ LICH_SU_VU_VIEC: "dd/mm HH:mm — {ho_ten} {hanh_dong}"… \| — \| **Luôn** \|" |
| `srs-fr-05-vu-viec.md:1726` | Thanh tiến trình 10 bước "… → Hoàn thành → **Đã đánh giá**", điều kiện hiển thị "Luôn" |
| `srs-fr-05-vu-viec.md:2277` | "\| Đã đánh giá \| DA_DANH_GIA \| CB NV đã đánh giá chất lượng HTPL \| Tím \|" |
| `srs-fr-05-vu-viec.md:2297` | "\| HOAN_THANH \| DA_DANH_GIA \| CB NV đánh giá (UC67) \| VV đã hoàn thành \| **Lưu đánh giá, audit** \| FR-V.I-17 \|" |

⇒ **Vế (b) có đặc tả rõ:** đánh giá phải **được ghi nhận** (bản ghi có đủ 3 điểm + điểm tổng = trung bình +
nhận xét), Nhóm 8 là nơi **hiển thị lại** (dòng 1734 + chế độ DN dòng 1809 "sau khi đánh giá → chuyển sang chế
độ chỉ đọc"), trạng thái vụ việc chuyển **"Đã đánh giá"**, Dòng thời gian ghi thêm sự kiện đánh giá.

### 2.4 Mỗi hồ sơ được đánh giá mấy lần

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1219` | "\| 5 \| Check duplicate: nếu đã tồn tại bản ghi DANH_GIA_VU_VIEC cho cùng VV và cùng loại người đánh giá → ERR-DG-VV-03 \|" |
| `srs-fr-05-vu-viec.md:1241` | "\| E3 \| Đã đánh giá \| ERR-DG-VV-03 \| "Bạn đã đánh giá vụ việc này rồi" \| ERROR \|" |
| `srs-fr-05-vu-viec.md:1239-1240` | E1 `ERR-DG-VV-01` "Vụ việc chưa hoàn thành" · E2 `ERR-DG-VV-02` "Điểm phải từ 0 đến 10" |
| `srs-fr-05-vu-viec.md:1242` | "\| E4 \| Không có quyền đánh giá VV \| ERR-DG-VV-04 \| "Bạn không có quyền đánh giá vụ việc này (DN khác/đơn vị khác)" \|" |

⇒ Tối đa **2 đánh giá/vụ việc** (1 của CB NV + 1 của DN); lần thứ 2 **cùng loại** phải bị từ chối.

### IM LẶNG về (KHÔNG được chấm Fail vì những điểm này)

1. **Nguyên văn chữ thông báo khi gửi đánh giá THÀNH CÔNG.** Bảng "Thông báo riêng SCR-V.I-03"
   (`srs-fr-05-vu-viec.md:1773-1786`) liệt kê 11 tình huống (phân công, trình phê duyệt, phê duyệt, hoàn thành,
   công khai, mở lại hồ sơ…) — **không có dòng nào cho thao tác đánh giá**.
2. **Nhãn · vị trí · kiểu hiển thị** của điểm vào thao tác đánh giá (nút trên thanh hành động hay điều khiển
   ngay trong Nhóm 8; mở hộp thoại hay mở tại chỗ). Dòng 1751 chỉ nói "Mở Accordion 8".
3. **Số chữ số thập phân** khi hiển thị điểm tổng (dòng 1208 và 2120 chỉ nói "AVG").
4. **Sửa / xoá / gửi lại** một đánh giá đã lưu — đặc tả chỉ chặn tạo trùng, không nói người dùng có được sửa.
5. **Thứ tự · màu · cách trình bày lại** 3 điểm trong Nhóm 8 sau khi đã đánh giá.

### ⚠️ ĐIỂM ĐẶC TẢ CHƯA THỐNG NHẤT (chỉ chạm dạng D3, xử riêng — không kéo verdict case)

`srs-fr-05-vu-viec.md:1740-1754` (bảng nút hành động **chế độ cán bộ**) chỉ có **một** dòng cho chức năng đánh
giá — dòng 1751, trạng thái `HOAN_THANH`; **không có** dòng cho `DA_DANH_GIA`. Trong khi đó `:1197` (PRE-02),
`:1734` (điều kiện hiển thị Nhóm 8) và `:1811` (chế độ DN) đều bao gồm **"Đã đánh giá"**.
⇒ Tình huống "vụ việc đã ở **Đã đánh giá** do một bên chấm trước, bên còn lại vào chấm" bị **2 vị trí đặc tả
nói lệch nhau**. Theo flow dòng 123: **cần BA** — nhưng **chỉ cho dạng D3**. Nếu D3 hỏng đúng vì điểm này thì
ghi vào file gửi BA, **không** kéo verdict của case; verdict của case do vế (a) + (b) trên D1/D2 quyết định
(flow dòng 322-324).

---

## 3. Precondition

**Env verify:** `https://18.143.165.120.nip.io` (KHÔNG phải env đối tác).

| Dạng | Tài khoản CỤ THỂ | Màn / URL | Dữ liệu tiền đề |
|---|---|---|---|
| CB Nghiệp vụ | **`cbnv_tw_01` / `Test@1234`** (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, đơn vị BTP·TW — `input/input.md:38`). Dự phòng cùng vai trò + cùng cấp: `cbnv_tw` (`input.md:19,130`) → `cbnv_tw_02` (`input.md:46`) | Vụ việc HTPL → chi tiết vụ việc `/vu-viec/{id}` | ≥1 vụ việc thuộc đơn vị BTP·TW ở **"Hoàn thành"** và **chưa có** đánh giá loại CB NV |
| Doanh nghiệp | **`0109998887` / `Test@1234`** (QA UAT Kiểm Thử DN, DN-HNI-0001, Hà Nội — `input/input.md:88`; **tên đăng nhập của DN là mã số thuế**, `input.md:93`). Dự phòng cùng vai trò DN: `0209888006` · `2323232323` (`input.md:89-90`) | Hồ sơ của tôi → chi tiết vụ việc `/ho-so-cua-toi/vu-viec/{id}` (`srs-fr-05-vu-viec.md:1792`) | ≥1 vụ việc **của chính DN đó** ở "Hoàn thành" và **chưa có** đánh giá loại DN |
| Phụ trợ (chỉ để dựng tiền đề, KHÔNG ra verdict) | `cbpd_tw_01` (phê duyệt cấp TW, `input.md:41`) · `qa_tvvseed28` (nhận phân công cấp TW, `input.md:103`) · với vụ việc của DN Hà Nội: `cbnv_hn` / `cbpd_hn` (`input.md:96-97`) | — | — |

**Cách dựng tiền đề (luồng chuẩn, trên dữ liệu QA — không đụng dữ liệu đối tác):**
Tạo/chọn vụ việc → Tiếp nhận → Kiểm tra hồ sơ (kết luận Đạt) → Phân công người xử lý → người đó Chấp nhận →
Cập nhật kết quả → Trình phê duyệt → `cbpd_tw_01` Phê duyệt → CB NV Cập nhật KQ cuối → **"Hoàn thành"**.
Tiền đề **tạo được mà không tạo ⇒ CẤM mọi verdict, kể cả ô trống** (flow dòng 209).

⚠️ `input/input.md:111-113`: sau case XNTGHTVV_03, VV-BTP-TW-20260712-001/-003/-005 đã bị từ chối phân công →
đang ở "Đã tiếp nhận"; phải phân công lại trước khi đẩy tiếp.

---

## 4. Tiêu chí chấm

### ✅ PASS khi — CẢ hai vế cùng đạt

**Vế (a) — chức năng đánh giá tiếp cận được từ giao diện:**

- **a1.** Đăng nhập đúng vai trò (CB NV cùng đơn vị / DN chủ vụ việc), mở chi tiết một vụ việc ở **"Hoàn thành"**
  chưa có đánh giá của loại người đó: **đếm được ≥1 phần tử tương tác dẫn tới việc đánh giá**, nhìn thấy được
  bằng mắt trong khung nhìn (không phải moi ra bằng công cụ nhà phát triển). Ghi lại **nhãn nguyên văn + vị trí
  + kích thước** của phần tử đó. *(Nhãn/vị trí do dự án chọn — xem mục 2 §IM LẶNG điểm 2.)*
- **a2.** Kích hoạt phần tử đó → mở ra chỗ nhập gồm **đúng 3 ô điểm** (chất lượng · thời gian · thái độ) nhận
  giá trị **0-10** + **1 ô nhận xét**; **đếm** đủ 3+1.
- **a3.** Nhập một điểm **ngoài khoảng 0-10** (ví dụ 11) → hệ thống **từ chối** và nêu được khoảng giá trị hợp
  lệ; **không** tạo bản ghi đánh giá (kiểm bằng a4/b2 sau đó).

**Vế (b) — gửi xong dữ liệu THỰC SỰ lưu và đọc lại được:**

- **b1.** Nhập bộ giá trị cụ thể **9 · 8 · 10** + nhận xét là chuỗi mốc-giờ duy nhất
  `QA-DGKQ-<YYYYMMDD-HHMM>` (để phân biệt với mọi dữ liệu cũ) → gửi. **Cài bộ bắt thông báo TRƯỚC khi bấm**;
  đếm **số thông báo theo MỐC GIỜ KHÁC NHAU** (không đếm theo số phần tử) và **đếm số request** song song.
- **b2. (tiêu chí quyết định — đọc lại sau khi TẢI LẠI TRANG)** Tải lại màn chi tiết đúng vụ việc đó bằng địa
  chỉ trang (không dùng lại DOM cũ), mở lại **Nhóm 8 — Đánh giá**: đọc được **đúng 3 số vừa nhập (9 · 8 · 10)**
  + **đúng chuỗi nhận xét mốc-giờ** đã nhập + **điểm tổng = trung bình 3 điểm = 9** (`:1220`, `:2120` — chấp nhận
  mọi cách làm tròn hiển thị). Nhóm 8 **không còn** ở trạng thái rỗng "Chưa có thông tin".
- **b3.** Sau khi tải lại, trạng thái vụ việc đọc trên màn = **"Đã đánh giá"** (`:1222`, `:2297`) — áp dụng cho
  lần đánh giá **đầu tiên**; vụ việc vốn đã ở "Đã đánh giá" thì **giữ nguyên** trạng thái đó.
- **b4.** Sau khi tải lại, **Dòng thời gian có thêm đúng 1 mục** ghi sự kiện đánh giá, kèm **người thực hiện** +
  **mốc giờ khớp** thao tác vừa làm (`:1224`, `:1735`).
- **b5. (đường đo thứ hai — bắt buộc)** Đọc lại chính vụ việc đó qua máy chủ (không qua giao diện): 3 điểm +
  điểm tổng + nhận xét + loại người đánh giá **trùng khít** với những gì màn hình hiển thị ở b2.
  **Hai đường mâu thuẫn ⇒ CHƯA chốt được**, ghi cả hai và hỏi user (flow dòng 249).
- **b6.** Thực hiện đánh giá **lần 2 bằng CÙNG loại người đánh giá** trên cùng vụ việc → hệ thống **từ chối** và
  nêu được lý do "đã đánh giá rồi" (`:1219`, `:1241`); đọc lại b2/b5 thấy **vẫn đúng 1 bộ điểm** của loại đó,
  không bị ghi đè, không sinh bản ghi thứ hai.

**Phủ đủ M dạng ở mục 5** (dạng nào chưa dựng được → ghi rõ ở mục 6, không được suy từ dạng khác).

> 🔴 **BẪY PASS-OAN — bắt buộc đọc trước khi chấm (bổ sung sau khi xem video vòng 2).**
> Video `t002.58s`/`t010.09s` chứng minh **b1 + b3 + b4 vẫn ĐẠT trong khi lỗi còn nguyên**: thông báo báo
> *"Đã đánh giá vụ việc"*, nhãn trạng thái đổi sang **"Đã đánh giá"**, Dòng thời gian **có** mục *Đánh giá* —
> nhưng Nhóm 8 vẫn **"Chưa có thông tin"**.
> ⇒ **b1/b3/b4 đạt KHÔNG đủ để Pass.** Chỉ **b2** (đọc lại đủ 3 điểm + nhận xét trong Nhóm 8 **sau khi tải lại
> trang**) và **b5** (đường đo thứ hai) mới có quyền chốt vế (b). Thấy nhãn "Đã đánh giá" mà kết luận
> *"đã lưu rồi"* là **Pass oan**.

### ❌ FAIL nếu (bất kỳ điều nào)

- **F1 (vế a còn nguyên):** vai trò đúng + vụ việc ở "Hoàn thành" + đúng phạm vi đơn vị/DN, nhưng **không có
  bất kỳ phần tử nào** trên màn cho phép bắt đầu đánh giá.
- **F2 (vai trò đúng mà nút biến mất):** vai trò đúng nhưng trạng thái/phạm vi chưa khớp → phần tử **biến mất
  hoàn toàn** thay vì hiển thị mờ kèm giải thích điều kiện (`:1759`).
- **F3 (vế b — fix nửa đường; đúng triệu chứng QA vòng trước VÀ video vòng 2 của đối tác):** gửi được và **báo
  thành công**, nhưng sau khi **tải lại trang**, Nhóm 8 vẫn rỗng / thiếu ≥1 trong 3 điểm / nhận xét khác chuỗi
  đã nhập / điểm tổng ≠ trung bình 3 điểm.
  - **F3-bis (dạng đã quan sát được trên bản V1.0.5 env đối tác):** nhãn trạng thái **đã** đổi sang
    "Đã đánh giá" **và** Dòng thời gian **đã** có mục đánh giá, **nhưng** Nhóm 8 vẫn "Chưa có thông tin"
    ⇒ **vẫn FAIL**. Trái `srs-fr-05-vu-viec.md:1734` (Nhóm 8 hiển thị 3 điểm + điểm tổng + nhận xét khi VV ở
    HOAN_THANH/DA_DANH_GIA) và `:1809` (sau khi đánh giá → chuyển sang chế độ chỉ đọc, tức phải có nội dung để
    đọc). Trạng thái đổi + có nhật ký **không thay thế được** yêu cầu hiển thị lại nội dung đánh giá.
- **F4:** giao diện báo thành công nhưng đường đo thứ hai (b5) **không** có bản ghi đánh giá tương ứng — hoặc
  ngược lại, máy chủ đã lưu mà giao diện không đọc lại được.
- **F5:** lần đánh giá đầu tiên xong mà trạng thái vụ việc **không** chuyển "Đã đánh giá".
- **F6:** đánh giá lần 2 **cùng loại người** vẫn được chấp nhận (sinh bản ghi thứ hai hoặc ghi đè âm thầm).
- **F7:** chữ thông báo **sai loại hoặc sai hành động** — báo thành công trong khi thao tác thất bại, hoặc báo
  lỗi trong khi dữ liệu đã lưu (flow dòng 234-236).
- **F8:** điểm ngoài 0-10 vẫn lưu được.
- **F9 (chỉ tính khi chạm dạng D2):** DN được đánh giá **vụ việc của DN khác**, hoặc CB NV đánh giá được vụ việc
  **ngoài phạm vi đơn vị** (trừ ngoại lệ cấp TW theo `:2358`).

### KHÔNG được chấm Fail vì (đặc tả im lặng — xem mục 2)

- Nguyên văn chữ thông báo thành công (chỉ chấm khi **sai loại/sai hành động** theo F7).
- Nhãn cụ thể · vị trí (thanh hành động trên/dưới, hay ngay trong Nhóm 8) · kiểu hiển thị (hộp thoại hay mở tại
  chỗ) của điểm vào thao tác.
- Cách làm tròn/định dạng hiển thị điểm tổng (9 vs 9.0 vs 9,0).
- Không có chức năng sửa/xoá đánh giá đã gửi.
- Thứ tự · màu sắc · bố cục trình bày lại 3 điểm trong Nhóm 8.
- **Riêng dạng D3** (vụ việc đã ở "Đã đánh giá", bên còn lại vào chấm): nếu hỏng đúng vì mâu thuẫn `:1751` vs
  `:1197`/`:1734`/`:1811` → **cần BA**, không chấm Fail, không kéo verdict case.

> **Phép thử mục 4:** người không biết gì về bug này, chỉ đọc từ a1 đến b6, vẫn chấm được PASS/FAIL — mọi tiêu
> chí đều đếm được (số phần tử, số ô, số thông báo theo mốc giờ) hoặc so được (3 số đã nhập, chuỗi mốc-giờ,
> điểm tổng, tên trạng thái).

---

## 5. Dạng dữ liệu phải phủ — M = 4

| # | Tên dạng | Nội dung |
|---|---|---|
| **D1** | **CB Nghiệp vụ × "Hoàn thành"** | `cbnv_tw_01` đánh giá vụ việc BTP·TW ở "Hoàn thành", chưa có đánh giá nào. **Đây là dạng đối tác chụp** |
| **D2** | **Doanh nghiệp × "Hoàn thành"** | `0109998887` đánh giá vụ việc **của chính DN đó** ở "Hoàn thành", chưa có đánh giá loại DN |
| **D3** | **Loại người còn lại × "Đã đánh giá"** | Vụ việc đã ở "Đã đánh giá" do một bên chấm trước → bên còn lại vào chấm (kiểm điều kiện hiển thị ở trạng thái `DA_DANH_GIA`). ⚠️ Dạng này chạm điểm đặc tả chưa thống nhất ở mục 2 |
| **D4** | **Trùng — cùng loại người đánh giá lần 2** | Cùng loại người đã chấm, vào chấm lại cùng vụ việc → phải bị từ chối, không sinh bản ghi thứ hai |

**Nguồn xác định M** (theo flow dòng 189-193, tra tới bước ② là đủ, không cần bước ③ hỏi dev/BA):

- **① Đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo:** `srs-fr-05-vu-viec.md:2116` — cột
  `loai_nguoi_danh_gia` `CHECK IN ('CB_NV','DN')` là **tập enum ĐÓNG 2 giá trị**; `:2108` + `:2114` —
  `UNIQUE(vu_viec_id, loai_nguoi_danh_gia)` ⇒ mỗi vụ việc có **2 đường** sinh bản ghi đánh giá, mỗi đường **1
  lần** ⇒ ra **D1, D2, D4**.
- **② Bộ lọc + giá trị enum ngay trên màn:** `:1197` (PRE-02) + `:1734` (điều kiện hiển thị Nhóm 8) — trạng
  thái tiền đề là enum **2 giá trị** `HOAN_THANH` / `DA_DANH_GIA` ⇒ ra **D3**.
- Vì bug thuộc loại **trường hiển thị lại dữ liệu** (3 điểm + nhận xét ở Nhóm 8), flow dòng 181 cấm để `M = 1`
  — ở đây M = 4, mỗi dạng phải đo trên **bản ghi riêng**, cấm suy từ dạng khác.

---

## 6. Bảng điều kiện

Cột "Đối tác" điền NGAY từ bằng chứng; 2 cột sau điền ở **giai đoạn B**.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Cả 2 vòng đều là Cán bộ NV Trung ương · `CB_NV_TW`**, đơn vị **"BTP · TW"** (góc phải màn). Vòng 1: Dòng thời gian ghi người thực hiện *"CB Nghiệp vụ TW 01"*. Vòng 2: Dòng thời gian ghi *"Cán bộ NV Trung ương"* (mục Đánh giá) và `huongcg` (các mục cập nhật KQ / trình PD). **Không vòng nào có bằng chứng cho vai trò Doanh nghiệp** | **Ra verdict:** `cbnv_tw_01` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, BTP·TW — **trùng vai trò + trùng cấp với đối tác**) · DN `0209888006` · DN `0109998887`. **Chỉ dựng tiền đề, không ra verdict:** `cbpd_tw_01` · `cbnv_dp_01` · `cbpd_dp_01` · `cbnv_hn`. Mật khẩu `Test@1234` cho tất cả, OTP lấy qua MailHog. **Không dùng `admin`**; không phải dùng tài khoản dự phòng Rule 7 | **Không** — phủ đúng vai trò đối tác đã chụp, đồng thời **mở rộng** sang vai trò Doanh nghiệp mà đối tác chưa có bằng chứng nào |
| Entity + trạng thái | **Vòng 1:** vụ việc ở "Hoàn thành" (suy từ Dòng thời gian *Hoàn thành 10/07/2026 09:54* ×2; nhãn trạng thái ngoài khung). **Vòng 2 (đọc trực tiếp nhãn):** trước khi gửi = **"Đã hoàn thành"** (thanh tiến trình đang ở bước 9 *Hoàn thành*) → sau khi gửi = **"Đã đánh giá"**, 10/10 bước ✓ | Cùng entity (vụ việc HTPL), cùng trạng thái tiền đề **"Hoàn thành"** như đối tác: `VV-BTP-TW-20260806-003` và `-004` (BTP·TW) tự đẩy `DANG_XU_LY → HOAN_THANH` rồi đánh giá → nhãn đổi **"Đã đánh giá"** (`DA_DANH_GIA`), thanh tiến trình 10/10 ✓. Nhánh DN: `VV-STP-AG-20260806-005` đẩy tới **"Hoàn thành"**. Thêm 1 bản ghi **sẵn ở "Đã đánh giá"** (`VV-QA-008`) để soi dạng D3 | **Không** — trạng thái tiền đề trùng khít đối tác ("Hoàn thành"), còn phủ thêm trạng thái "Đã đánh giá" mà đối tác không chạm |
| Dữ liệu tiền đề | **Vòng 1:** vụ việc đã qua phê duyệt (*Ngày duyệt 10/07/2026 09:24*) + hoàn thành, Nhóm 8 rỗng ⇒ chưa từng đánh giá; ID `9ed9d021-f308-40cc-b4d7-b60b80fbc1dd`, **không lộ mã VV**. **Vòng 2:** **VV-BTP-TW-20260713-001** — *TKM test* · LHHT_TKM · Kênh *Trực tiếp* · Lĩnh vực *Thuế* · Ưu tiên *Trung bình* · tiếp nhận 13/07/2026 16:47 · hạn xử lý 03/08/2026 · Hoàn thành 27/07/2026 15:11 · Nhóm 8 rỗng trước khi gửi ⇒ chưa từng đánh giá | **Tự dựng bằng luồng chuẩn trên dữ liệu QA của env nội bộ, không đo trên bản ghi đối tác.** `VV-BTP-TW-20260806-003` (`fbf936fb-…`) và `-004` (`45501596-…`): Cập nhật kết quả → Trình phê duyệt → `cbpd_tw_01` Phê duyệt → CB NV cập nhật KQ cuối → **"Hoàn thành"**, Nhóm 8 rỗng trước khi gửi (ảnh 01). Nhánh DN: `VV-STP-AG-20260806-005` (`0dfb2b25-…`) do chính DN `0209888006` nộp, `cbnv_dp_01` + `cbpd_dp_01` đẩy tới "Hoàn thành", chưa có đánh giá loại DN. **Nới 1 chiều so với kế hoạch mục 3 — khai công khai:** dự kiến dùng DN `0109998887` (Hà Nội) nhưng Sở Tư pháp Hà Nội **không có người xử lý nào đăng nhập được** (TVV `DDD-TVV-022` có `taiKhoanId` rỗng) nên không đẩy được vụ việc của DN đó lên "Hoàn thành" → chuyển sang DN `0209888006` (An Giang), **cùng vai trò DN, cùng quan hệ "DN là chủ vụ việc"**. Vẫn tái hiện lại triệu chứng trên DN `0109998887` với vụ việc của chính DN đó (`ac866cde-…`, ảnh 09) để chắc không phải đặc thù 1 doanh nghiệp | **Không** — chiều bị nới (đơn vị chủ quản của vụ việc: Hà Nội → An Giang) **đã khai ở ô bên trái** kèm lý do và đã đo lại trên cả 2 doanh nghiệp cho ra cùng kết quả; đặc tả `:1216` ràng buộc DN theo `doanh_nghiep_id` **của chính DN**, không ràng buộc theo tỉnh |
| Input / filter / giá trị nhập | **Vòng 1: không có** (đối tác dừng ở bước quan sát, không tìm thấy điểm vào). **Vòng 2 có giá trị thật:** Điểm chất lượng **5.0** · Điểm thời gian **5.5** · Điểm thái độ **7.5** · Nhận xét **"abc"** (3/2000) → bấm **[Xác nhận]** → **1 thông báo**, nguyên văn **"Đã đánh giá vụ việc"** | Bộ giá trị mục 4 ấn định: **9 · 8 · 10** + nhận xét mốc-giờ duy nhất `QA-DGKQ-20260806-1634` (VV-003) và `QA-DGKQ-20260806-1701` (VV-004) → điểm tổng đọc lại **9/10**. Thông báo nguyên văn **"Đã đánh giá vụ việc"**, **1 khung · 1 mốc giờ · 1 request** (bộ bắt cài trước khi bấm, không lọc trùng, đọc `innerText`). Thêm 2 ca đối tác không chạy: **điểm ngoài khoảng = 11** (a3) và **đánh giá lần 2 cùng loại người** (D4/b6) | **Không** — 3 ô điểm + 1 ô nhận xét giống hệt đối tác, còn thêm 2 ca biên. Chưa đo **điểm thập phân** (đối tác nhập 5.5): căn cứ không tính GAP — mục 4 §"KHÔNG được chấm Fail vì" đã loại bỏ cách làm tròn/định dạng điểm tổng, và vế (b) đo **khả năng đọc lại nội dung đánh giá**, không phụ thuộc kiểu số |
| Độ phủ biến thể (N bản ghi, M dạng) | **N = 2 bản ghi** (mỗi vòng 1, **khác nhau**) · **vẫn chỉ 1 dạng — D1 (CB NV × "Hoàn thành")**. Không vòng nào phủ **D2 / D3 / D4** | **N = 5 bản ghi chạm tay** (`VV-BTP-TW-20260806-003` · `-004` · `VV-STP-AG-20260806-005` · `VV-QA-008` · vụ việc `ac866cde-…` của DN `0109998887`). **M phủ 3/4:** **D1 đạt** — 2 bản ghi riêng, cùng cho kết quả đọc lại đủ; **D4 đạt** — trên VV-003; **D2 CHẠM và HỎNG ngay ở điểm vào** (đó chính là chỗ quyết định verdict); **D3 KHÔNG dựng được** — muốn có "một bên chấm trước, bên còn lại vào chấm" thì phải có đánh giá của phía DN, mà phía DN bị chặn hoàn toàn ⇒ chỉ quan sát được gần đúng trên `VV-QA-008` (đang ở "Đã đánh giá" nhưng **không** kèm bản ghi đánh giá nào) | **Không** — đối tác mới phủ D1, vòng này phủ **rộng hơn** (D1 ×2 bản ghi + D4 + chạm D2). **D3 còn thiếu, khai thẳng ở ô bên trái**: dạng này chạm điểm đặc tả chưa thống nhất (`:1751` vs `:1197`/`:1734`/`:1811`) nên theo mục 4 §D3 → **gửi BA, không kéo verdict case**; verdict do (a)+(b) trên D1/D2 quyết định. **Không suy** kết quả D3 từ dạng khác |

**3 dữ kiện neo của đối tác** (ghi cho **cả 2 vòng** vì lệch bản ghi + lệch bản dựng — xem bảng đối chiếu mục 1):

| # | Dữ kiện | Vòng 1 — `DGKQHTVV_01.jpg` | Vòng 2 — `DGKQHTVV_01_v2.webm` |
|---|---|---|---|
| 1 | **URL / ID / mã bản ghi** | `https://htpldn-uat.ospgroup.vn/vu-viec/9ed9d021-f308-40cc-b4d7-b60b80fbc1dd` — **không có mã `VV-...`** | `https://htpldn-uat.ospgroup.vn/vu-viec/43ec038d-36a0-44c0-ad6d-f21bec32a207` — **VV-BTP-TW-20260713-001** ("TKM test") |
| 2 | **Trạng thái entity** | "Hoàn thành" (suy từ Dòng thời gian); Nhóm 8 rỗng | **"Đã hoàn thành"** đọc trực tiếp trên nhãn → sau khi gửi đổi **"Đã đánh giá"**; Nhóm 8 **vẫn rỗng** |
| 3 | **Vai trò + env + bản dựng** | CB NV Trung ương (`CB_NV_TW`, BTP·TW) · `htpldn-uat.ospgroup.vn` · **HTPLDN · V1.0** · đồng hồ máy **09:57 · 2026-07-10** | CB NV Trung ương (`CB_NV_TW`, BTP·TW) · `htpldn-uat.ospgroup.vn` · **HTPLDN · V1.0.5** · đồng hồ máy **09:10 · 2026-08-05** |

**Đã lấp được 3 thiếu sót của ảnh vòng 1** (mã VV · vùng thanh hành động · nhãn trạng thái đọc trực tiếp) — chi
tiết ở mục 1 §"3 thiếu sót". Nhưng **lấp bằng bản ghi khác + bản dựng khác**, nên không dùng để khẳng định điều
gì về chính bản ghi của vòng 1.

**Giới hạn hiệu lực (không phải GAP):** bằng chứng chụp trên env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`
bản **V1.0** (10/07/2026) và **V1.0.5** (05/08/2026); vòng này đo trên env nội bộ
`https://18.143.165.120.nip.io` với bản dựng **HTPLDN · V1.0.8** (`assets/index-DIABnbIr.js`, trang gốc sửa lần
cuối 06/08/2026 14:13:15 giờ VN). Verdict chỉ có hiệu lực cho env + bản dựng
đã ghi; Pass ở đây là **Pass tạm** cho tới khi bản dựng đó lên env đối tác. **Ngược lại cũng đúng:** vế (a) hết
lỗi trên V1.0.5 của env đối tác **không** chứng minh nó hết trên bản dựng env verify — vẫn phải đo lại từ a1.

**Giai đoạn B vẫn tự dựng tiền đề** trên dữ liệu QA (flow dòng 208-211) — không đo trên bản ghi của đối tác.

---

## Sửa đổi

### 2026-08-06 13:22 — bổ sung bằng chứng vòng 2 (video), chỉnh mục 1 · 4 · 6

**Vì sao:** phiên chính quyết định tải `DGKQHTVV_01_v2.webm` (cột *Ảnh/video 2*) sau khi mục 1 bản đầu ghi
"ảnh vòng 1 không đủ chốt 3 điểm". Video đã xem đủ tới khoảnh khắc quyết định.

**Sửa gì:**

| Mục | Trước | Sau | Lý do |
|---|---|---|---|
| 1 — vế (a) | Chỉ có lời đối tác + TKM retest 27/7 | Thêm: video vòng 2 cho thấy **nút [⭐ Đánh giá] + hộp thoại 3 tiêu chí ĐÃ CÓ** trên bản V1.0.5 env đối tác | Bằng chứng mới của chính đối tác |
| 1 — vế (b) | Chỉ có ô *Kết quả verify* của QA vòng trước | Thêm bằng chứng **của đối tác**; đồng thời **chỉnh cách mô tả triệu chứng**: không phải "không lưu gì cả" mà là **"đánh giá không đọc lại được ở Nhóm 8"** — vì trạng thái đã đổi "Đã đánh giá" và Dòng thời gian đã ghi mục *Đánh giá* | Video `t010.09s` cho thấy dữ liệu đã được ghi nhận ở 2 nơi khác; mô tả cũ sẽ dẫn giai đoạn B đo sai chỗ |
| 1 — bằng chứng | 1 mục (ảnh) | 2 mục (ảnh + video) + bảng diễn biến theo mốc giây + bảng đối chiếu **lệch bản ghi / lệch bản dựng** (flow dòng 105) + mục "3 thiếu sót đã lấp" | Bắt buộc theo flow khi có bằng chứng nhiều vòng |
| 4 — sau b6 | *(không có)* | Thêm khối **BẪY PASS-OAN**: b1/b3/b4 đạt **không đủ** để Pass; chỉ b2 + b5 mới chốt được vế (b) | Video chứng minh 3 tiêu chí này **vẫn đạt trong khi lỗi còn nguyên** — nếu để nguyên, người chấm rất dễ Pass oan |
| 4 — F3 | 1 điều kiện | Thêm **F3-bis**: trạng thái đã đổi + có nhật ký nhưng Nhóm 8 vẫn rỗng ⇒ **vẫn FAIL** (trái `:1734` + `:1809`) | Ghi thẳng dạng lỗi đã quan sát được để không ai lập luận "đã lưu rồi nên Pass" |
| 6 | Cột "Đối tác" chỉ có dữ kiện vòng 1; 3 dữ kiện neo dạng danh sách | Cột "Đối tác" gộp cả 2 vòng; 3 dữ kiện neo chuyển thành **bảng 2 cột theo vòng**; ghi rõ đã lấp thiếu sót nào và **lấp bằng bản ghi/bản dựng khác** | Dữ kiện mới: mã VV, nhãn trạng thái, vị trí nút, giá trị nhập thật |

**KHÔNG sửa:** tiêu chí a1–a3 · b1–b6 (nội dung từng tiêu chí giữ nguyên) · danh sách "KHÔNG được chấm Fail vì"
· **mục 5 M = 4 và 4 dạng D1-D4 giữ nguyên** — video chỉ thêm 1 bản ghi nữa của **cùng dạng D1**, không sinh
dạng mới, không đổi nguồn xác định M.

### 2026-08-06 17:05 — điền số đo giai đoạn B (bản dựng + mục 6), khai 2 việc lệch kế hoạch

**Vì sao:** hoàn tất đo thật; mục 3 và mục 6 còn ô để trống, để trống là cấm ra verdict.

**Sửa gì:**

| Mục | Trước | Sau | Lý do |
|---|---|---|---|
| Đầu file + mục 6 §Giới hạn hiệu lực | `Bản dựng: <điền ở giai đoạn B>` | **HTPLDN · V1.0.8** + dấu vân tay tự đo (`index-DIABnbIr.js`, `index-DVlgOkLg.css`, ngày sửa trang gốc, thẻ etag, máy chủ) | Bắt buộc theo flow — verdict chỉ có hiệu lực cho bản dựng đã ghi |
| 6 — cột "Mình test lần này" + "GAP?" | Trống cả 5 dòng | Điền đủ 5/5 dòng, mỗi dòng kèm căn cứ | Còn ô trống ⇒ cấm ra verdict |
| 6 — dòng "Dữ liệu tiền đề" | Kế hoạch mục 3 ghi DN `0109998887` (Hà Nội) | **Nới sang DN `0209888006` (An Giang)** — khai lý do: Sở Tư pháp Hà Nội không có người xử lý nào đăng nhập được nên không đẩy được vụ việc lên "Hoàn thành"; đã đo lại trên **cả hai** doanh nghiệp cho cùng kết quả | Nới chiều mà không khai = GAP chưa đóng |
| 6 — dòng "Độ phủ biến thể" | — | Khai thẳng **D3 không dựng được** (phải có đánh giá phía DN mới có bản ghi "Đã đánh giá do một bên chấm", mà phía DN bị chặn) → gửi BA theo mục 4 §D3, **không** kéo verdict case | Cấm suy dạng chưa dựng từ dạng đã dựng |

**KHÔNG sửa:** mục 1 · mục 2 · tiêu chí a1–a3 / b1–b6 · F1–F9 · danh sách "KHÔNG được chấm Fail vì" · mục 5.
Kết quả đo **không** được dùng để chỉnh lại thước đo.
