# Chuẩn chấm đã khóa — DGKQHTVV_01 (dòng 64)

> 🔴 **VÒNG NÀY ĐO NHÁNH DOANH NGHIỆP.** Case Reopen vì **vai trò DOANH NGHIỆP** không vào được chức năng đánh giá.
> **BẮT BUỘC đăng nhập bằng tài khoản doanh nghiệp (tên đăng nhập = mã số thuế). CẤM ra verdict bằng tài khoản cán bộ.**
> Nhánh cán bộ nghiệp vụ **đã hết lỗi từ vòng 06/08** — chỉ chạy lại 1 bản ghi để chắc không hỏng theo, **không** dùng để ra verdict.
>
> **Nguồn khóa chuẩn:** khối `── CÁCH VERIFY sau Dev fix ──` trong
> [`../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md`](../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md)
> entry `BUG-VV-DGKQHTVV-01`, dòng **878–894**.
> Ô "Kết quả verify" đang nằm trên bảng: [`../audit/DGKQHTVV_01-ketqua-verify-CU.md`](../audit/DGKQHTVV_01-ketqua-verify-CU.md).
> Tiêu chí vòng trước: [`../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/tieuchi/DGKQHTVV_01.md`](../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/tieuchi/DGKQHTVV_01.md).
>
> **Đặc tả — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md`
> (2.506 dòng, mtime **04/08/2026 17:17** — **KHÔNG** bị sửa ngày 06/08). Số dòng dưới đây **tự mở file đếm lại ngày 2026-08-07**.
> Chức năng: **FR-V.I-17 — Đánh giá kết quả hỗ trợ vụ việc (UC67)**, heading tại `:1185`.

---

## 1. Lỗi gốc (Expected/Actual của phiếu)

| | Nội dung |
|---|---|
| **Expected** | Doanh nghiệp là **một trong hai** đối tượng được đánh giá vụ việc (cùng cán bộ nghiệp vụ). DN phải **mở được vụ việc của chính mình** và **chấm được** khi vụ việc ở **"Hoàn thành"** hoặc **"Đã đánh giá"**; **mỗi DN chấm 1 lần / 1 vụ việc**. |
| **Actual đo 06/08/2026 (V1.0.8 · `assets/index-DIABnbIr.js`)** | DN đăng nhập, thấy vụ việc của mình trong danh sách với nhãn "Đã hoàn thành", **0 phần tử tương tác** dẫn tới việc đánh giá. Bấm mở chi tiết **chính vụ việc của mình** → bị đẩy sang **trang báo không có quyền truy cập**. Nguyên nhân đọc tại chỗ: **3 lời gọi dữ liệu của màn chi tiết bị từ chối vì vai trò** (thông tin phân công · kết quả · kết quả kiểm tra), mỗi lời gọi **403**; FE bắt lỗi rồi chuyển thẳng sang trang không có quyền. Đường đo thứ hai: gọi thẳng thao tác đánh giá **bằng chính phiên của DN** → **403 · `ERR-AUTH-DN-00-01` · "Role không được phép truy cập endpoint CMS này"** ⇒ **không** phải lỗi bề mặt giao diện. Lặp **giống hệt trên 2 doanh nghiệp** khác nhau. Địa chỉ chế độ xem dành cho DN (`:1792`) **không tồn tại** trên bản dựng — mở ra trang "không tìm thấy". |
| **ĐÃ HẾT LỖI — không dùng ra verdict** | Nhánh **cán bộ nghiệp vụ**: chấm 9·8·10 + nhận xét → **tải lại trang** → Nhóm 8 đọc đủ 3 điểm, điểm tổng **9/10**, nhận xét đúng nguyên văn, người + thời điểm đúng; trạng thái chuyển "Đã đánh giá"; đường đo 2 trùng khít. Đo trên 2 bản ghi riêng. **Ca biên đạt:** điểm ngoài 0–10 bị chặn (0 lời gọi gửi đi); đánh giá **lần 2 cùng loại** bị chặn, không ghi đè. |

**Vế duy nhất quyết định verdict vòng này: DOANH NGHIỆP mở được vụ việc của mình + có đường vào đánh giá + gửi xong đọc lại được sau khi tải lại trang.**

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

**Kết quả đối chiếu: 0/6 trích dẫn bị lệch.** Sáu số dòng ghi trong ô "Kết quả verify" cũ (`:1190` · `:1198` · `:1215` · `:2116` · `:1809` · `:1811`) **vẫn đúng nguyên**.
*(Ghi chú: ô sheet chỉ liệt kê 5 mã — `:1190 · :1198 · :2116 · :1809 · :1811`; `:1215` nằm ở bảng "Kết quả mong đợi" của bug entry. Cả 6 đều đã kiểm.)*

| Trích dẫn cũ | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng |
|---|---|---|
| `:1190` | **:1190 — KHÔNG lệch** | `**Mô tả:** CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc.` |
| `:1198` | **:1198 — KHÔNG lệch** | `| PRE-03 | Role ∈ {CB_NV, DN} (theo CSV UC67) |` |
| `:1215` | **:1215 — KHÔNG lệch** | `| 1 | Kiểm tra quyền: role ∈ {CB_NV, DN} | BR-AUTH-01 |` |
| `:2116` | **:2116 — KHÔNG lệch** | `| 4 | loai_nguoi_danh_gia | text | Y | CHECK IN ('CB_NV','DN') | — | Loại người đánh giá (theo CSV UC67: chỉ CB Nghiệp vụ và Doanh nghiệp) |` |
| `:1809` | **:1809 — KHÔNG lệch** | `| Nhóm 8 — Đánh giá | Cho phép nhập khi vụ việc ở "Hoàn thành" / "Đã đánh giá" + DN chưa đánh giá. Sau khi đánh giá → chuyển sang chế độ chỉ đọc |` |
| `:1811` | **:1811 — KHÔNG lệch** | `| Thanh thao tác | Chỉ 2 nút DN được phép: **[Bổ sung hồ sơ]** (khi trạng thái = "Yêu cầu bổ sung" — gọi FR-V.I-NEW-02); **[Đánh giá]** (khi trạng thái = "Hoàn thành" / "Đã đánh giá" + chưa đánh giá)…` |

**Dòng nền bổ sung (agent này tự mở kiểm — cũng không lệch):**

| Dòng | Nguyên văn (≤200 ký tự) |
|---|---|
| `:1185` | `### FR-V.I-17: Đánh giá kết quả hỗ trợ vụ việc (UC67)` |
| `:1197` | `| PRE-02 | VV ở trạng thái HOAN_THANH hoặc DA_DANH_GIA |` |
| `:1216` | `| 2 | Validate scope theo role: nếu role='DN' → VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id; nếu role='CB_NV' → VU_VIEC.don_vi_id = current_user.don_vi_id | BR-AUTH-03/04, BR-…` |
| `:1219` | `| 5 | Check duplicate: nếu đã tồn tại bản ghi DANH_GIA_VU_VIEC cho cùng VV và cùng loại người đánh giá → ERR-DG-VV-03 | — |` |
| `:1220` | `| 6 | Xác nhận điểm 0-10; tính điểm tổng = trung bình 3 điểm | — |` |
| `:1222` | `| 8 | Chuyển VV → DA_DANH_GIA (chỉ lần đánh giá đầu tiên; nếu VV đã DA_DANH_GIA thì giữ nguyên) | SM-VUVIEC |` |
| `:1241` | `| E3 | Đã đánh giá | ERR-DG-VV-03 | "Bạn đã đánh giá vụ việc này rồi" | ERROR |` |
| `:1242` | `| E4 | Không có quyền đánh giá VV | ERR-DG-VV-04 | "Bạn không có quyền đánh giá vụ việc này (DN khác/đơn vị khác)" |` |
| `:1734` | `| 11 | content | Accordion 8 — Đánh giá (gộp MH-05.9) | C23 | diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet | CB NV/DN nhập trực tiếp | K…` |
| `:1751` | `| HOAN_THANH | [Đánh giá] (gộp MH-05.9) | CB NV/DN | Mở Accordion 8. Gửi → DA_DANH_GIA |` |
| `:1789` | `### SCR-V.I-03 — Chế độ doanh nghiệp` |
| `:1792` | `**URL:** /ho-so-cua-toi/vu-viec/{id} (backend tự định tuyến theo phiên)` |
| `:1793` | `**Quyền truy cập:** DN chỉ thấy vụ việc của DN mình (backend tự kiểm tra; truy cập trái phép → trả lỗi 403 + chuyển về SCR-V.I-04).` |
| `:1805` | `| Nhóm 4 — Kết quả kiểm tra | **Ẩn hoàn toàn** (thông tin nội bộ) |` |
| `:1806` | `| Nhóm 5 — Phân công xử lý | **Ẩn hoàn toàn** (thông tin nội bộ — bảo mật cán bộ theo NĐ 13/2023)… |` |
| `:1807` | `| Nhóm 6 — Kết quả hỗ trợ | Chỉ đọc. Chỉ hiển thị khi vụ việc ở "Đã duyệt" / "Hoàn thành" / "Đã đánh giá" |` |
| `:1808` | `| Nhóm 7 — Phê duyệt | **Ẩn hoàn toàn** (thông tin nội bộ) |` |
| `:1810` | `| Dòng thời gian | Chỉ hiển thị các sự kiện liên quan đến DN: tiếp nhận, kết luận kiểm tra, kết quả phê duyệt, hoàn thành, từ chối, công khai/hủy công khai. Ẩn sự kiện nội bộ (phân…` |
| `:1815` / `:1819` | `### SCR-V.I-04: Danh sách Vụ việc của tôi (doanh nghiệp)` · `**URL:** /ho-so-cua-toi/vu-viec` |
| `:1830` | `| 3 | tab | 3 tab trạng thái | C19 | "Tất cả" / "Đang xử lý" (chưa hoàn thành) / "Đã kết thúc" (đã hoàn thành / đã đánh giá / bị từ chối). Mỗi tab có badge số đếm |` |
| `:1834` | `| 7 | table | Mã vụ việc | text (link) | VV-{Tỉnh}-YYYYMMDD-{số thứ tự}, độ rộng 160px | click → mở chi tiết (chế độ DN) | Luôn |` |
| `:1846` | `- Phạm vi truy cập: backend cố định lọc theo DN đăng nhập — DN không thể xem vụ việc của DN khác kể cả khi sửa URL` |
| `:2108` | `**Mô tả:** Đánh giá chất lượng hỗ trợ VV. Mỗi VV có tối đa 1 đánh giá từ CB NV và 1 từ DN — UNIQUE (vu_viec_id, loai_nguoi_danh_gia).` |
| `:2114` | `| 2 | vu_viec_id | identifier | Y | FK → VU_VIEC(id); UNIQUE(vu_viec_id, loai_nguoi_danh_gia) | — | VV được đánh giá |` |
| `:2120` | `| 8 | diem_tong | number | Y | Auto = AVG(diem_chat_luong, diem_thoi_gian, diem_thai_do) | — | Điểm tổng hợp |` |
| `:2297` | `| HOAN_THANH | DA_DANH_GIA | CB NV đánh giá (UC67) | VV đã hoàn thành | Lưu đánh giá, audit | FR-V.I-17 | — |` |

### 2-bis. Ba câu hỏi của điều phối — trả lời bằng dòng đặc tả

| Câu hỏi | Trả lời | Dòng dẫn |
|---|---|---|
| **DN được đánh giá ở những trạng thái vụ việc nào?** | **"Hoàn thành" (`HOAN_THANH`) và "Đã đánh giá" (`DA_DANH_GIA`)** — với điều kiện **DN chưa đánh giá**. Bảng quy tắc **chế độ doanh nghiệp** khai cả 2 trạng thái ở **cả 2 chỗ**: Nhóm 8 và Thanh thao tác. | `:1197` (PRE-02) · `:1734` (điều kiện hiển thị Nhóm 8) · **`:1809`** · **`:1811`** |
| **Mỗi DN chấm mấy lần?** | **Đúng 1 lần cho mỗi vụ việc.** Ràng buộc ở 4 tầng: mô tả, ràng buộc dữ liệu `UNIQUE(vu_viec_id, loai_nguoi_danh_gia)`, bước xử lý check duplicate, và mã lỗi. Cả vụ việc tối đa **2** đánh giá (1 CB_NV + 1 DN). | `:1190` · `:2108` · `:2114` · `:2116` · `:1219` · `:1241` |
| **DN có được xem chi tiết vụ việc của chính mình không?** | **CÓ — đặc tả có hẳn một chế độ xem riêng cho DN.** `SCR-V.I-03 — Chế độ doanh nghiệp` với URL riêng; **403 chỉ dành cho truy cập TRÁI PHÉP** (vụ việc của DN khác), không dành cho vụ việc của chính mình. Ở danh sách, click mã vụ việc **mở chi tiết (chế độ DN)**; nút 👁 Xem **luôn hiển thị**. | `:1789` · **`:1792`** · **`:1793`** · `:1807` · `:1834` · `:1841` |

> 🔴 **Điểm mấu chốt của `:1793`:** *"DN chỉ thấy vụ việc của DN mình (backend tự kiểm tra; **truy cập trái phép → trả lỗi 403 + chuyển về SCR-V.I-04**)"*. ⇒ Màn 403 là **hành vi ĐÚNG** khi DN mở vụ việc **của DN khác**, và là **hành vi SAI** khi DN mở vụ việc **của chính mình**. Agent đo phải phân biệt tuyệt đối 2 ca này.

---

## 3. Precondition + dữ liệu + công thức dựng

### 3.1 Vai trò / tài khoản (env `https://18.143.165.120.nip.io`, MailHog `http://18.143.165.120:8025/`)

🔴 **Tài khoản ra verdict = DOANH NGHIỆP. Tên đăng nhập của DN chính là MÃ SỐ THUẾ, không phải dạng chữ** (`input/input.md:93`).

| Vai trò | Tài khoản (tên đăng nhập) | Mật khẩu | Ghi chú |
|---|---|---|---|
| **DN #1 — ra verdict** | **`0209888006`** — *Cong ty QA UAT An Giang* (`DN-AGG-0001`) | `Test@1234` | **Đã dùng thành công vòng 06/08**, đang sở hữu `VV-STP-AG-20260806-005` ở "Hoàn thành" chưa có đánh giá. Mật khẩu đã được QA đặt lại về `Test@1234` ngày 06/08 qua luồng "Quên mật khẩu?" |
| **DN #2 — ra verdict** | **`0109998887`** — *QA UAT Kiểm Thử DN* (`DN-HNI-0001`, Hà Nội) | `Test@1234` | Đã dùng vòng 06/08, sở hữu vụ việc `ac866cde-…` |
| DN dự phòng (cùng vai trò DN) | `2323232323` | `Test@1234` | Chỉ dùng khi #1 hoặc #2 lock; **khai account thực dùng** |
| Cán bộ dựng tiền đề (**KHÔNG ra verdict**) | `cbnv_dp_01` · `cbpd_dp_01` (An Giang) · `cbnv_tw_01` · `cbnv_tw_02` · `cbpd_tw_01` (TW) · `cbnv_hn` / `cbpd_hn` (Hà Nội) · `qa_tvvseed28` (TVV TW) · `nht_ag_uat2` (NHT An Giang) | `Test@1234` | Đẩy vụ việc lên "Hoàn thành"; chạy lại 1 bản ghi nhánh cán bộ để kiểm hồi quy |
| **CẤM dùng** | `admin` | — | Vòng 06/08 **không dùng `admin`** — giữ nguyên. Quyền rộng che đúng loại lỗi đang đo (phân quyền) |

**OTP:** lấy ở MailHog `http://18.143.165.120:8025/` (env chưa tích hợp email thật — không log "không nhận được OTP" thành bug).

### 3.2 Màn / đường dẫn — **cách biết vụ việc nào thuộc DN đó**

- **Danh sách:** `SCR-V.I-04` — `/ho-so-cua-toi/vu-viec` (`:1815`, `:1819`), tiêu đề **"Vụ việc của tôi"**.
  **Backend cố định lọc theo DN đăng nhập — DN không thể xem vụ việc của DN khác kể cả khi sửa URL (`:1846`).**
  ⇒ **Mọi dòng trong danh sách này đều là vụ việc của chính DN đang đăng nhập.** Đây là cách xác định quyền sở hữu **không cần hỏi ai**.
- **Lọc nhanh:** tab **"Đã kết thúc"** = *đã hoàn thành / đã đánh giá / bị từ chối* (`:1830`); cột **Trạng thái** badge (`:1837`); ô tìm theo mã vụ việc hoặc tiêu đề (`:1831`).
- **Mở chi tiết:** click **mã vụ việc** → mở chi tiết **chế độ DN** (`:1834`), hoặc icon 👁 **Xem** (`:1841`). URL kỳ vọng `/ho-so-cua-toi/vu-viec/{id}` (`:1792`).
- **Chỗ đánh giá:** **Nhóm 8 — Đánh giá** (`:1809`) và/hoặc nút **[Đánh giá]** trên **Thanh thao tác** (`:1811`).

### 3.3 Dữ liệu tiền đề — có sẵn gì, thiếu gì, dựng thế nào

**Cần: ≥ 2 vụ việc DO CHÍNH DN đó gửi/sở hữu, ở "Hoàn thành", CHƯA có đánh giá loại DN — trên ≥ 2 doanh nghiệp khác nhau.**

| Bản ghi | Chủ sở hữu | Trạng thái sau vòng 06/08 | Dùng được cho |
|---|---|---|---|
| `VV-STP-AG-20260806-005` (`0dfb2b25-…`) | DN **`0209888006`** | **"Hoàn thành"**, **chưa có đánh giá nào** | ✅ **D2 — bản ghi #1 của DN #1**, dùng ngay |
| vụ việc `ac866cde-…` | DN **`0109998887`** | Đã chạm vòng 06/08 (bị 403) — **phải xác minh lại trạng thái + chưa có đánh giá DN** | ✅ **D2 — bản ghi của DN #2** nếu đúng "Hoàn thành" |
| `VV-BTP-TW-20260806-003` (`fbf936fb-…`) | Vụ việc nhập tay trên DN *Cong ty TNHH QA UAT Kiem Thu* | **"Đã đánh giá"**, đã có **1 đánh giá loại CB_NV** (9·8·10, nhận xét `QA-DGKQ-20260806-1634`) | ✅ **D3** (xem dưới) + kiểm hồi quy nhánh cán bộ |
| `VV-BTP-TW-20260806-004` (`45501596-…`) | như trên | **"Đã đánh giá"**, đã có 1 đánh giá loại CB_NV (`QA-DGKQ-20260806-1701`) | ✅ **D3** dự phòng |
| `VV-QA-008` | — | "Đã đánh giá" nhưng **không kèm bản ghi đánh giá nào** (dữ liệu lạ) | ⚠️ **KHÔNG dùng làm tiền đề** — xem §8 bẫy 6 |

**⇒ THIẾU: bản ghi thứ hai của cùng DN #1 (và của DN #2).** Công thức dựng — nguyên văn khối CÁCH VERIFY dòng **881**:

```
doanh nghiệp gửi hồ sơ -> cán bộ nghiệp vụ cùng địa bàn tiếp nhận
  -> kiểm tra hồ sơ kết luận Đạt -> phân công người xử lý
  -> cập nhật kết quả -> trình phê duyệt -> cán bộ phê duyệt duyệt
  -> cập nhật kết quả cuối -> "Hoàn thành"
```
Cặp tài khoản chạy được đã kiểm chứng: **DN `0209888006` gửi → `cbnv_dp_01` tiếp nhận + kiểm tra → phân công `nht_ag_uat2` → `nht_ag_uat2` chấp nhận + cập nhật kết quả → trình phê duyệt → `cbpd_dp_01` duyệt → `cbnv_dp_01` cập nhật KQ cuối → "Hoàn thành".**

> ⚠️ **Đơn vị Hà Nội đã hỏng 2 lần khi dựng** (khai ở tiêu chí vòng trước): (a) cán bộ **cấp TW không tiếp nhận được** hồ sơ do DN Hà Nội gửi — máy chủ chặn *"Đơn vị của người phê duyệt khác đơn vị của bản ghi"*; (b) bảng gợi ý phân công của Sở Tư pháp Hà Nội **rỗng** (TVV `DDD-TVV-022` có `taiKhoanId` rỗng) ⇒ không đẩy được lên "Hoàn thành". **Muốn có bản ghi #2 cho DN `0109998887` (Hà Nội) thì phải tạo/kích hoạt được một người xử lý thuộc Sở Tư pháp Hà Nội trước** (dùng cặp `cbnv_hn` / `cbpd_hn`), hoặc **thay DN #2 bằng `2323232323`** và khai rõ việc thay.

**Tiền đề tạo được mà không tạo ⇒ CẤM mọi verdict, kể cả ô trống.**

---

## 4. Các bước đo — **chép nguyên văn khối CÁCH VERIFY** (bug-report.md:879–889)

```
Precondition: tài khoản doanh nghiệp (ví dụ 0209888006 / Test@1234, tên đăng nhập là mã số thuế) + màn danh sách vụ việc của doanh nghiệp đó và màn chi tiết vụ việc.
  Cần >= 2 vụ việc DO CHÍNH doanh nghiệp đó gửi, đang ở "Hoàn thành" và chưa có đánh giá của loại doanh nghiệp.
  Chưa có thì tạo mới bằng luồng chuẩn: doanh nghiệp gửi hồ sơ -> cán bộ nghiệp vụ cùng địa bàn tiếp nhận -> kiểm tra hồ sơ kết luận Đạt -> phân công người xử lý -> cập nhật kết quả -> trình phê duyệt -> cán bộ phê duyệt duyệt -> cập nhật kết quả cuối -> "Hoàn thành".
  Sẵn sàng thêm 1 vụ việc "Hoàn thành" đã có đánh giá của cán bộ nghiệp vụ (để kiểm ca doanh nghiệp chấm sau).
1) Đăng nhập bằng chính tài khoản doanh nghiệp đó, mở danh sách vụ việc, bấm mở chi tiết vụ việc "Hoàn thành" của chính mình. Phải xem được nội dung hồ sơ, không bị đẩy sang trang báo không có quyền.
2) Đếm số phần tử tương tác dẫn tới việc đánh giá (nhìn thấy bằng mắt trong khung nhìn, không moi bằng công cụ nhà phát triển). Kích hoạt nó, nhập 9 · 8 · 10 và một chuỗi nhận xét mốc giờ duy nhất dạng QA-DGKQ-<YYYYMMDD-HHMM>, rồi gửi. Cài bộ bắt thông báo TRƯỚC khi bấm, đếm theo mốc giờ khác nhau và đếm số lời gọi song song.
3) Tải lại trang bằng địa chỉ (không dùng lại màn cũ), mở lại Nhóm 8 — Đánh giá và đọc nội dung.
4) Đo bằng đường thứ hai: bằng chính phiên đăng nhập của doanh nghiệp, đọc lại bản ghi đánh giá của vụ việc đó từ máy chủ và đối chiếu từng trường với những gì màn hình hiển thị ở bước 3.
5) Lặp bước 1-4 trên vụ việc thứ hai của cùng doanh nghiệp, và trên 1 doanh nghiệp KHÁC với vụ việc của chính doanh nghiệp đó.
6) Kiểm phạm vi (chứng âm): cùng tài khoản doanh nghiệp đó, thử đánh giá một vụ việc CỦA DOANH NGHIỆP KHÁC -> phải bị từ chối.
7) Kiểm trùng: doanh nghiệp đánh giá lần thứ hai cùng vụ việc -> phải bị từ chối, đọc lại vẫn đúng 1 bộ điểm của loại doanh nghiệp.
```

**Ghi chú thao tác UI thật (không đổi tiêu chí):**
- Bộ bắt thông báo: `output/UAT_doi-tac/tools/toast-capture.js` — **cài TRƯỚC khi bấm**, tự kiểm `soObserverDangSong = 1`, **CẤM lọc trùng**, đọc `innerText`, đếm theo **mốc giờ khác nhau** (không đếm theo số phần tử). SPA-navigate wipe observer ⇒ **cài lại sau mỗi lần chuyển màn**.
- Bước 2 "đếm bằng mắt trong khung nhìn": chụp `take_screenshot` làm bằng chứng số phần tử, **không** dùng querySelector để moi phần tử ẩn rồi tính là "có".
- Bước 8 (thêm, chỉ để kiểm hồi quy — **không** ra verdict): đăng nhập `cbnv_tw_01`, mở 1 vụ việc "Đã đánh giá" (`VV-BTP-TW-20260806-003`), xác nhận Nhóm 8 vẫn đọc được đủ 3 điểm + điểm tổng + nhận xét cũ.

---

## 5. Đường đo thứ hai (đối chứng độc lập)

**Bắt buộc — bước 4 của khối CÁCH VERIFY.**

- Gọi **bằng chính phiên đăng nhập của DN** (cookie-auth, JWT là cookie), **không** dùng `admin`, **không** dùng phiên cán bộ.
- Đọc lại bản ghi đánh giá của đúng vụ việc đó, đối chiếu **từng trường** với màn hình ở bước 3:
  `diem_chat_luong = 9` · `diem_thoi_gian = 8` · `diem_thai_do = 10` · `diem_tong = AVG = 9` (`:2120`) · `nhan_xet` = đúng chuỗi mốc-giờ · **`loai_nguoi_danh_gia = 'DN'`** (`:2116`) · `nguoi_danh_gia_id` = tài khoản DN đang đăng nhập.
- **Chứng âm bước 6:** thao tác đánh giá lên vụ việc của DN khác phải bị từ chối. Theo `:1242` mã kỳ vọng là `ERR-DG-VV-04` *"Bạn không có quyền đánh giá vụ việc này (DN khác/đơn vị khác)"*, theo `:1793` mở chi tiết trái phép thì **403 + chuyển về SCR-V.I-04**. **Chỉ chấm "bị từ chối hay không", KHÔNG chấm theo mã lỗi cụ thể** (describe, không prescribe).
- **Kiểm trùng bước 7:** lần 2 cùng loại DN phải bị từ chối (`:1219`, `:1241`), đọc lại **vẫn đúng 1 bộ điểm**, không ghi đè, không sinh bản ghi thứ hai.
- **Hai đường mâu thuẫn ⇒ CHƯA chốt được** — ghi cả hai vào bug entry, xem §6 FAIL ("fix một phần vẫn là FAIL").

---

## 6. ✅ PASS khi / ❌ FAIL nếu — **chép nguyên văn từ khối CÁCH VERIFY** (bug-report.md:890–893)

```
✅ PASS khi: doanh nghiệp mở được chi tiết vụ việc của chính mình; đếm được >= 1 phần tử dẫn tới việc đánh giá; gửi xong thì SAU KHI TẢI LẠI TRANG Nhóm 8 đọc được đúng 3 điểm đã nhập + đúng chuỗi nhận xét + điểm tổng bằng trung bình 3 điểm; đường đo thứ hai trùng khít và ghi loại người đánh giá là doanh nghiệp; đúng trên >= 2 vụ việc và >= 2 doanh nghiệp; chứng âm bước 6 và kiểm trùng bước 7 đều bị từ chối.
❌ FAIL nếu: doanh nghiệp vẫn không mở được chi tiết vụ việc của chính mình; hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá; hoặc gửi được và báo thành công nhưng sau khi tải lại trang Nhóm 8 vẫn rỗng / thiếu >= 1 trong 3 điểm / nhận xét khác chuỗi đã nhập / điểm tổng khác trung bình 3 điểm; hoặc hai đường đo lệch nhau (fix một phần vẫn là FAIL); hoặc doanh nghiệp đánh giá được vụ việc của doanh nghiệp khác.
⚠️ Đừng chấm FAIL vì: nhãn / vị trí / kiểu hiển thị của đường vào đánh giá (nút trên thanh hành động hay điều khiển ngay trong Nhóm 8; hộp thoại hay mở tại chỗ); nguyên văn chữ thông báo thành công; cách làm tròn / định dạng điểm tổng (9 vs 9.0 vs 9,0); không có chức năng sửa/xoá đánh giá đã gửi; thứ tự - màu - bố cục trình bày lại 3 điểm; điểm tư vấn viên không đổi (đặc tả tự mâu thuẫn ở chỗ này, đã gửi BA); không ai nhận được thông báo sau khi đánh giá (đặc tả không xếp chức năng này vào nhóm phải gửi thông báo).
⚠️ Đừng chấm PASS vì: thấy nhãn trạng thái đã đổi sang "Đã đánh giá", thấy nhật ký đã có mục đánh giá, hay thấy thông báo báo thành công — cả ba dấu hiệu này ĐÃ từng đúng trong khi lỗi còn nguyên. Chỉ bước 3 (đọc lại Nhóm 8 sau khi tải lại trang) và bước 4 (đường đo thứ hai) mới chốt được. Cũng đừng chấm PASS vì nhánh cán bộ nghiệp vụ đã chạy được — nhánh đó đã đạt từ vòng này, phải đo lại ĐÚNG nhánh doanh nghiệp.
```

---

## 7. Độ phủ biến thể bắt buộc — **N ≥ 3 bản ghi × M = 4 dạng (D2 là dạng quyết định)**

Sàn cứng của khối PASS: **≥ 2 vụ việc VÀ ≥ 2 doanh nghiệp** + chứng âm (bước 6) + kiểm trùng (bước 7).

| # | Dạng | Nội dung | Trạng thái vòng 06/08 | Vòng này |
|---|---|---|---|---|
| **D1** | CB Nghiệp vụ × "Hoàn thành" | `cbnv_tw_01` chấm vụ việc BTP·TW ở "Hoàn thành" | ✅ **ĐẠT** trên 2 bản ghi riêng | Chỉ **kiểm hồi quy 1 bản ghi**, không ra verdict |
| **D2** | **Doanh nghiệp × "Hoàn thành"** | DN chấm vụ việc **của chính mình** ở "Hoàn thành", chưa có đánh giá loại DN | ❌ **HỎNG ngay ở điểm vào** (403 khi mở chi tiết) | 🔴 **DẠNG QUYẾT ĐỊNH** — ≥ 2 vụ việc × ≥ 2 DN |
| **D3** | Loại người còn lại × **"Đã đánh giá"** | Vụ việc đã ở "Đã đánh giá" do CB NV chấm trước → **DN vào chấm tiếp** | 🚫 **KHÔNG dựng được** (DN bị chặn hoàn toàn) | ✅ **NAY DỰNG ĐƯỢC** — xem dưới |
| **D4** | Trùng — cùng loại người chấm lần 2 | DN đã chấm, vào chấm lại cùng vụ việc → phải bị từ chối | ✅ đạt **ở phía CB_NV**; **chưa** đo phía DN | Đo lại **ở phía DN** = bước 7 |

### D3 — dạng vòng trước ghi "CHƯA KIỂM ĐƯỢC": nay dựng được chưa và dựng thế nào

**Lý do vòng trước không dựng được (nguyên văn ô sheet):** *"Muốn dựng được trường hợp này thì phía doanh nghiệp phải chấm được trước, nên phải đợi sửa xong mới kiểm."*
👉 **Lý do đó chỉ đúng cho chiều DN-chấm-trước.** Chiều **CB-chấm-trước** đã có sẵn dữ liệu.

**NAY DỰNG ĐƯỢC — 2 đường, ưu tiên đường A:**

- **Đường A (dùng dữ liệu tồn, 0 công dựng):** `VV-BTP-TW-20260806-003` và `-004` đang ở **"Đã đánh giá"** với **đúng 1 đánh giá loại `CB_NV`** (9·8·10 + nhận xét `QA-DGKQ-20260806-1634` / `-1701`). Sau khi dev mở quyền DN, chỉ cần **đăng nhập DN chủ của 2 vụ việc đó** rồi vào chấm ⇒ đúng bài "một bên đã chấm, bên còn lại vào chấm".
  🔴 **Việc phải làm trước:** 2 vụ việc này do `cbnv_tw_01`/`cbnv_tw_02` **nhập thủ công** trên doanh nghiệp **`Cong ty TNHH QA UAT Kiem Thu`** (cấp TW). Tên này **gần giống nhưng chưa chắc trùng** tài khoản `0109998887` (*QA UAT Kiểm Thử DN*, `DN-HNI-0001`). **Phải xác minh quyền sở hữu trước:** đăng nhập `0109998887` → mở `/ho-so-cua-toi/vu-viec` → tìm mã `VV-BTP-TW-20260806-003`. Có trong danh sách ⇒ đúng chủ (theo `:1846` danh sách này backend cố định lọc theo DN đăng nhập). Không có ⇒ chuyển đường B.
- **Đường B (dựng mới, chắc chắn):** trên **DN `0209888006`** — lấy 1 vụ việc "Hoàn thành" của DN đó (dựng theo §3.3), **cho `cbnv_dp_01` chấm trước** (đẩy vụ việc sang "Đã đánh giá"), rồi **đăng nhập DN `0209888006` vào chấm tiếp**. Đây chính là câu *"Sẵn sàng thêm 1 vụ việc 'Hoàn thành' đã có đánh giá của cán bộ nghiệp vụ (để kiểm ca doanh nghiệp chấm sau)"* trong Precondition của khối CÁCH VERIFY.

**Cách chấm D3 — GIỮ NGUYÊN ràng buộc đã khóa, không tự nới:** D3 chạm **điểm đặc tả chưa thống nhất** đã gửi BA
(`cau-hoi-BA.md` §"Vụ việc đã ở 'Đã đánh giá' thì bên còn lại có được vào đánh giá không?"): `:1751` (bảng nút **chế độ cán bộ**, chỉ có dòng `HOAN_THANH`) **lệch** với `:1197` / `:1734` / `:1811` (đều gồm "Đã đánh giá").
⇒ **D3 hỏng thì GHI NHẬN + gửi BA, KHÔNG chấm Fail, KHÔNG kéo verdict case.** Verdict do **D2** quyết định.
📌 **Dữ kiện mới cần ghi vào ô BA (không tự kết luận):** mâu thuẫn nằm ở **bảng nút chế độ CÁN BỘ** (`:1751`); còn **bảng quy tắc chế độ DOANH NGHIỆP** khai *"Hoàn thành" / "Đã đánh giá"* **thống nhất ở cả 2 dòng** (`:1809` Nhóm 8 và `:1811` Thanh thao tác) ⇒ ở **nhánh DN**, đặc tả **không** tự mâu thuẫn. Ghi quan sát này vào báo cáo để BA chốt nhanh hơn; **vẫn không** dùng để kéo verdict.

### Đã tra 3 nguồn để chốt M (nói rõ đã tra gì)

1. **Chuẩn PASS đã khóa** (bug-report.md:890) — ấn định **≥ 2 vụ việc × ≥ 2 doanh nghiệp** + chứng âm phạm vi (bước 6) + kiểm trùng (bước 7) ⇒ ra **D2** và **D4**.
2. **Mục SRS về nguồn dữ liệu** — `:2116` `loai_nguoi_danh_gia … CHECK IN ('CB_NV','DN')` là **tập enum ĐÓNG 2 giá trị**; `:2108` + `:2114` `UNIQUE(vu_viec_id, loai_nguoi_danh_gia)` ⇒ mỗi vụ việc có **2 đường** sinh bản ghi đánh giá, mỗi đường **1 lần** ⇒ ra **D1, D2, D4**.
3. **Bộ lọc + enum trên màn** — trạng thái tiền đề là enum **2 giá trị** `HOAN_THANH` / `DA_DANH_GIA` (`:1197` PRE-02 · `:1734` điều kiện hiển thị Nhóm 8 · `:1809` + `:1811` chế độ DN) ⇒ ra **D3**. Bộ lọc trên màn DN: 3 tab `Tất cả / Đang xử lý / Đã kết thúc` (`:1830`) — tab **"Đã kết thúc"** gộp *đã hoàn thành / đã đánh giá / bị từ chối*, dùng để tìm nhanh cả D2 lẫn D3.

**M = 4 giữ nguyên. Mỗi dạng đo trên bản ghi riêng — CẤM suy kết quả dạng này từ dạng khác.**

---

## 8. ⚠️ Bẫy / rule chống kết luận oan

1. 🔴 **Bẫy Pass oan đã ghi thành lịch sử** — video vòng 2 của đối tác chứng minh **thông báo "Đã đánh giá vụ việc" + nhãn trạng thái đổi sang "Đã đánh giá" + Dòng thời gian có mục *Đánh giá*** vẫn **ĐÚNG HẾT** trong khi Nhóm 8 vẫn *"Chưa có thông tin"*. **Ba dấu hiệu này KHÔNG có quyền chốt.** Chỉ **bước 3** (đọc lại Nhóm 8 **sau khi tải lại trang**) và **bước 4** (đường đo thứ hai) mới chốt được.
2. 🔴 **Bẫy đo nhầm nhánh** — nhánh **cán bộ nghiệp vụ đã đạt từ vòng 06/08**. Chạy lại nhánh đó rồi kết luận "đã fix" = **Pass oan trắng trợn**. **Verdict chỉ được ra từ phiên đăng nhập DOANH NGHIỆP.**
3. 🔴 **Bẫy 403 đúng/sai** — theo `:1793`, **403 + chuyển về danh sách là hành vi ĐÚNG** khi DN mở vụ việc **của DN khác** (bước 6 chứng âm). Chỉ **403 trên vụ việc CỦA CHÍNH MÌNH** mới là lỗi. Log nhầm chiều = **bug invalid**.
4. 🔴 **Bẫy "thiếu nhóm thông tin = lỗi"** — ở chế độ DN, đặc tả **cố ý ẩn**: `:1805` Nhóm 4 Kết quả kiểm tra **Ẩn hoàn toàn** · `:1806` Nhóm 5 Phân công xử lý **Ẩn hoàn toàn** (bảo mật cán bộ, NĐ 13/2023) · `:1808` Nhóm 7 Phê duyệt **Ẩn hoàn toàn**. Vòng trước FE **gọi đúng 3 nguồn dữ liệu này rồi ăn 403** → đẩy sang trang không có quyền. ⇒ Sau khi fix, DN mở chi tiết mà **không thấy Nhóm 4 / 5 / 7 là ĐÚNG ĐẶC TẢ** — **CẤM log thành "thiếu thông tin"**.
5. 🔴 **Bẫy Dòng thời gian thiếu mục "Đánh giá"** — `:1810` khai Dòng thời gian **chế độ DN** chỉ hiển thị: *tiếp nhận, kết luận kiểm tra, kết quả phê duyệt, hoàn thành, từ chối, công khai/hủy công khai*. **"Đánh giá" KHÔNG nằm trong danh sách này.** ⇒ DN không thấy mục *Đánh giá* trên Dòng thời gian **không phải lỗi**. (Ở chế độ cán bộ thì phải có, theo `:1224` + `:1735`.)
6. ⚠️ **Không dùng `VV-QA-008` làm tiền đề** — vụ việc này đang mang nhãn "Đã đánh giá" **nhưng không kèm bản ghi đánh giá nào**; đây là dữ liệu bất thường tồn đọng, đo trên nó cho kết quả không diễn giải được.
7. ⚠️ **Không FAIL vì điểm trung bình của tư vấn viên không đổi** — `:1233` (Postconditions) *"Điểm TVV được cập nhật"* **ngược** với `:1223` (Processing bước 9) *"UC67 chỉ tạo DANH_GIA_VU_VIEC; trigger cập nhật điểm TVV nằm ở module FR-IV"*. **Đã gửi BA**, cố ý bỏ trống tiêu chí.
8. ⚠️ **Không FAIL vì không ai nhận thông báo sau khi đánh giá** — bảng "Thông báo riêng SCR-V.I-03" (`:1773`–`:1785`, 11 tình huống) **không có dòng nào cho thao tác đánh giá**.
9. ⚠️ **Bộ bắt thông báo CẤM lọc trùng và CẤM dùng `textContent`** — lọc trùng che double-toast (Pass oan), `textContent` đọc cả node ẩn AntD (bug ma). Dùng `innerText`, đếm theo **mốc giờ**, **luôn đếm kèm số lời gọi**. Cài **TRƯỚC** khi bấm; **cài lại sau mỗi SPA-navigate**.
10. ⚠️ **Bẫy bản dựng cũ trong tab** — tab MCP mở lâu vẫn chạy bó mã cũ. **Tải lại trang bằng địa chỉ**, ghi lại **bó mã FE + `last-modified` + `etag`** trước khi đo. Vòng 06/08 đã có **triển khai mới xen giữa lô**.
11. ⚠️ **Địa chỉ `/ho-so-cua-toi/vu-viec/{id}` vòng trước trả trang "không tìm thấy"** và bảng định tuyến FE chỉ có danh sách / tạo mới / chi tiết dùng chung. **Không prescribe URL** — nếu dev cho DN xem chi tiết qua đường dẫn khác mà **xem được đúng nội dung + đánh giá được** thì **vẫn PASS** (`:1792` là cách hiện thực, yêu cầu nghiệp vụ là DN mở được vụ việc của mình).
12. ⚠️ **Giới hạn hiệu lực** — verdict chỉ có giá trị cho **env nội bộ `18.143.165.120.nip.io` + bản dựng đo được**. Bằng chứng đối tác quay trên `htpldn-uat.ospgroup.vn` (V1.0 và V1.0.5). Ghi câu giới hạn này vào kết quả.

---

## 9. Đối chiếu khối note ↔ bug entry

**Kết luận: GIỐNG về hướng và về vế quyết định — LỆCH ĐÁNG KỂ về độ chặt (ô sheet là bản rút gọn, thiếu 6 thứ, trong đó có ĐƯỜNG ĐO THỨ HAI và 2 khối chống oan). KHÔNG có điểm nào mâu thuẫn nhau.**

| Vế | Bug entry (dòng 878–894) | Ô sheet "CÁCH KIỂM LẠI SAU KHI SỬA" | Đánh giá |
|---|---|---|---|
| Vai trò ra verdict | "tài khoản doanh nghiệp (ví dụ `0209888006` / `Test@1234`, **tên đăng nhập là mã số thuế**)" | "Đăng nhập bằng tài khoản doanh nghiệp" | **GIỐNG** — bug entry chỉ đích danh account + nhắc quy ước mã số thuế |
| Tiền đề | "**≥ 2 vụ việc DO CHÍNH doanh nghiệp đó gửi**, ở 'Hoàn thành', **chưa có đánh giá loại doanh nghiệp**" + **công thức dựng 8 bước** + "**sẵn sàng thêm 1 vụ việc đã có đánh giá của cán bộ**" | "một vụ việc 'Hoàn thành' của chính doanh nghiệp đó" | **LỆCH — sheet thiếu công thức dựng + thiếu điều kiện "chưa có đánh giá loại DN" + thiếu vụ việc dự phòng cho D3** |
| Bước mở chi tiết | Bước 1 — "Phải **xem được nội dung hồ sơ**, không bị đẩy sang trang báo không có quyền" | "mở một vụ việc 'Hoàn thành' của chính doanh nghiệp đó" | **GIỐNG** (sheet ngầm định, bug entry ghi rõ tiêu chí) |
| Đếm điểm vào | Bước 2 — "**đếm số phần tử tương tác** dẫn tới việc đánh giá, **nhìn thấy bằng mắt trong khung nhìn, không moi bằng công cụ nhà phát triển**" | **KHÔNG có** | **LỆCH — sheet thiếu.** Đây là tiêu chí đếm được của vế (a) |
| Giá trị nhập | "**9 · 8 · 10**" + "chuỗi nhận xét mốc giờ duy nhất dạng **`QA-DGKQ-<YYYYMMDD-HHMM>`**" | "chấm 3 điểm kèm nhận xét" | **LỆCH — sheet thiếu bộ giá trị chuẩn + quy ước chuỗi mốc-giờ** (không có chuỗi duy nhất thì không phân biệt được với dữ liệu cũ) |
| Bắt thông báo | "Cài bộ bắt thông báo **TRƯỚC khi bấm**, đếm theo mốc giờ khác nhau và **đếm số lời gọi song song**" | **KHÔNG có** | **LỆCH — sheet thiếu** |
| Tải lại trang | Bước 3 — "**Tải lại trang bằng địa chỉ (không dùng lại màn cũ)**", mở lại Nhóm 8 | "sau đó **TẢI LẠI TRANG** rồi xem Nhóm 8" | **GIỐNG** — cả hai đều nhấn mạnh vế quyết định |
| **Đường đo thứ hai** | **Bước 4 bắt buộc** — đọc lại bản ghi đánh giá từ máy chủ **bằng chính phiên DN**, đối chiếu **từng trường** | **KHÔNG có** | 🔴 **LỆCH NẶNG — sheet thiếu hẳn.** Theo bug entry |
| Độ phủ | Bước 5 — "≥ 2 vụ việc của **cùng** doanh nghiệp **VÀ** 1 doanh nghiệp **KHÁC**" | "ít nhất 2 vụ việc và 2 doanh nghiệp khác nhau" | **GIỐNG về số**, sheet không nói rõ "2 vụ việc của cùng 1 DN" |
| Chứng âm phạm vi | **Bước 6 — thao tác chủ động**: thử đánh giá vụ việc của DN khác → phải bị từ chối | Chỉ nằm ở vế FAIL: "hoặc doanh nghiệp chấm được vụ việc của doanh nghiệp khác" | **LỆCH — sheet biến bước đo chủ động thành điều kiện thụ động.** Vẫn phải **chủ động chạy** bước 6 |
| Kiểm trùng | **Bước 7** — DN đánh giá lần 2 cùng vụ việc → phải bị từ chối, vẫn đúng 1 bộ điểm | **KHÔNG có** | **LỆCH — sheet thiếu** |
| PASS | 8 vế (mở được · đếm ≥1 phần tử · 3 điểm sau reload · nhận xét · điểm tổng = TB · đường đo 2 trùng khít **+ ghi loại người đánh giá là DN** · ≥2 VV & ≥2 DN · bước 6 + 7 bị từ chối) | 3 vế (mở được · chấm được · sau reload đọc lại đủ 3 điểm + điểm tổng + nhận xét) | **GIỐNG phần lõi**, sheet **thiếu 5 vế** |
| FAIL | 6 vế, có **"hai đường đo lệch nhau (fix một phần vẫn là FAIL)"** | 3 vế (vẫn 403 · Nhóm 8 trống sau reload · chấm được VV của DN khác) | **GIỐNG 3/6**, sheet **thiếu** vế thiếu điểm/lệch nhận xét/điểm tổng sai và vế 2 đường lệch |
| ⚠️ chống FAIL oan | **Khối 7 hạng mục** (nhãn/vị trí, chữ thông báo, làm tròn điểm tổng, không có sửa/xoá, bố cục, điểm TVV, không ai nhận thông báo) | **KHÔNG có** | 🔴 **LỆCH NẶNG — sheet thiếu.** Thiếu khối này rất dễ **FAIL oan** |
| ⚠️ chống PASS oan | **Khối đầy đủ**: nhãn "Đã đánh giá" / nhật ký / thông báo **đều từng đúng trong khi lỗi còn nguyên**; và "đừng Pass vì nhánh cán bộ đã chạy được" | **KHÔNG có** | 🔴 **LỆCH NẶNG — sheet thiếu.** Đây là bẫy đã làm hỏng vòng trước |
| D3 | Nằm ở **Precondition** ("sẵn sàng thêm 1 vụ việc 'Hoàn thành' đã có đánh giá của cán bộ nghiệp vụ") | Nằm ở mục riêng **"CHƯA KIỂM ĐƯỢC"** | **GIỐNG bản chất** — bug entry đã dự phòng sẵn tiền đề cho D3; sheet chỉ khai là chưa kiểm được |

**⇒ Chuẩn dùng để đo = KHỐI TRONG BUG ENTRY (bản đầy đủ).** Đo theo ô sheet sẽ mất **đường đo thứ hai**, **bước 6**, **bước 7**, **bộ giá trị chuẩn**, và **cả 2 khối chống oan**.

**Đối chiếu với đặc tả hiện hành (mục E):** khối CÁCH VERIFY **vẫn khớp** đặc tả, **không có điểm nào phải nới hay siết**:
- "DN mở được chi tiết vụ việc của chính mình" ← `:1789` + `:1792` + `:1793` (403 **chỉ** cho truy cập trái phép).
- "có phần tử dẫn tới việc đánh giá khi VV ở Hoàn thành + DN chưa đánh giá" ← `:1809` + `:1811` + `:1197` + `:1734`.
- "Nhóm 8 đọc lại được 3 điểm + nhận xét + điểm tổng = trung bình" ← `:1734` + `:1220` + `:2120` + `:1809` ("sau khi đánh giá → chuyển sang chế độ chỉ đọc", tức phải **có nội dung để đọc**).
- "đường đo 2 ghi loại người đánh giá là doanh nghiệp" ← `:2116`.
- "bước 6 chứng âm phạm vi" ← `:1216` + `:1242` + `:1793` + `:1846`.
- "bước 7 kiểm trùng" ← `:1190` + `:2108` + `:2114` + `:1219` + `:1241`.

---

## 10. Cảnh báo cho agent đo

1. 🔴 **ĐĂNG NHẬP BẰNG TÀI KHOẢN DOANH NGHIỆP — `0209888006` và `0109998887`, mật khẩu `Test@1234`, tên đăng nhập là MÃ SỐ THUẾ.** Verdict ra bằng tài khoản cán bộ = **vô hiệu**. Nhánh cán bộ chỉ chạy 1 bản ghi để kiểm hồi quy.
2. 🔴 **CẤM `admin`.** Vòng 06/08 không dùng `admin` — giữ nguyên. Lỗi đang đo là lỗi **phân quyền**; `admin` che đúng loại lỗi đó.
3. 🔴 **Ba dấu hiệu CẤM dùng để Pass:** nhãn trạng thái "Đã đánh giá" · Dòng thời gian có mục Đánh giá · thông báo "Đã đánh giá vụ việc". Cả ba **đã từng đúng trong khi lỗi còn nguyên**. Chỉ **bước 3 + bước 4** chốt được.
4. 🔴 **Phân biệt 403 đúng và 403 sai.** VV của chính mình → 403 = **lỗi**. VV của DN khác → 403 + về danh sách = **đúng đặc tả `:1793`**, cấm log.
5. 🔴 **Không log "thiếu Nhóm 4 / 5 / 7" và "Dòng thời gian không có mục Đánh giá" thành bug** — đặc tả **cố ý ẩn** ở chế độ DN (`:1805`, `:1806`, `:1808`, `:1810`).
6. **Dữ liệu sẵn dùng ngay:** `VV-STP-AG-20260806-005` (DN `0209888006`, "Hoàn thành", chưa có đánh giá). **Còn thiếu bản ghi thứ hai của cùng DN** → dựng theo §3.3. **Xác minh lại** trạng thái vụ việc `ac866cde-…` của DN `0109998887` trước khi tính là tiền đề.
7. **D3 nay dựng được** (đường A: `VV-BTP-TW-20260806-003`/`-004` đã ở "Đã đánh giá" với 1 đánh giá CB_NV — **phải xác minh DN chủ trước** bằng cách tìm mã VV trong `/ho-so-cua-toi/vu-viec` của DN; đường B: cho `cbnv_dp_01` chấm trước trên vụ việc của DN `0209888006`). **D3 hỏng ⇒ gửi BA, KHÔNG chấm Fail, KHÔNG kéo verdict.**
8. **Đơn vị Hà Nội đã hỏng 2 lần khi dựng tiền đề** (cấp TW không tiếp nhận được hồ sơ DN Hà Nội; pool phân công Sở Tư pháp Hà Nội rỗng). Nếu kẹt → dùng **`2323232323`** làm DN #2 và **khai rõ việc thay**.
9. **Cài `toast-capture.js` TRƯỚC khi bấm**, tự kiểm `soObserverDangSong = 1`, **không lọc trùng**, `innerText`, đếm theo mốc giờ + đếm lời gọi; **cài lại sau mỗi SPA-navigate**.
10. **Ghi dấu vân tay bản dựng** (bó mã FE · `last-modified` · `etag`) và **tải lại trang bằng địa chỉ** trước khi đo.
11. Login fail → **Rule 7**: fallback **cùng vai trò DN** (`0209888006` → `0109998887` → `2323232323`), **khai account thực dùng**; không đổi sang vai trò cán bộ.
12. Ảnh chụp lưu đúng `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/<...>/image/`.
