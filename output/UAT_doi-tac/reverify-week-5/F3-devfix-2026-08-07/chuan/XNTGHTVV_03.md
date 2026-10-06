# Chuẩn chấm đã khóa — XNTGHTVV_03 (dòng 51)

> **Nguồn khóa chuẩn:** khối `── CÁCH VERIFY sau Dev fix ──` trong
> [`../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md`](../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md)
> entry `BUG-VV-XNTGHTVV-03`, dòng **731–742**.
> Ô "Kết quả verify" đang nằm trên bảng: [`../audit/XNTGHTVV_03-ketqua-verify-CU.md`](../audit/XNTGHTVV_03-ketqua-verify-CU.md).
> Tiêu chí vòng trước (ngữ cảnh): [`../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/tieuchi/XNTGHTVV_03.md`](../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/tieuchi/XNTGHTVV_03.md).
>
> **Đặc tả — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md`
> (2.506 dòng, mtime **04/08/2026 17:17** — **KHÔNG** bị sửa ngày 06/08).
> Mọi số dòng dưới đây do agent này **tự mở file đếm lại ngày 2026-08-07**.

---

## 1. Lỗi gốc (Expected/Actual của phiếu)

**Thao tác:** người được phân công mở chi tiết vụ việc ở **"Đã phân công"** → bấm **[Từ chối]** → nhập lý do hợp lệ (≥ 10 ký tự) → **Xác nhận**.

| | Nội dung |
|---|---|
| **Expected (phiếu, vế còn tranh chấp)** | Lý do từ chối là thông tin **bắt buộc** ⇒ phải được **lưu vào nhật ký vụ việc**, và cán bộ phụ trách phải **đọc lại được trên màn chi tiết vụ việc**, kể cả sau khi hồ sơ đã quay về "Đã tiếp nhận". |
| **Actual đo được 06/08/2026 (bản dựng V1.0.8 · `assets/index-DIABnbIr.js`)** | Nhật ký **có** sinh mục cho thao tác từ chối (đúng hành động `TU_CHOI_PHAN_CONG`, đúng người, đúng giờ) nhưng mục đó **không mang trường lý do**. Đo trên **3/3 hồ sơ**, cả UI lẫn đọc thẳng máy chủ — hai đường **khớp nhau**. Sau khi hồ sơ về "Đã tiếp nhận", nhóm "Phân công Người hỗ trợ / Tư vấn viên" (nơi có cột *Lý do từ chối*) **không còn hiển thị** ⇒ trên toàn màn chi tiết **không còn chỗ nào** cho cán bộ đọc lý do. |
| **6/7 vế ĐÃ HẾT LỖI — không đo lại để ra verdict** | (a1) không còn văng màn chặn quyền · (a2) có thông báo thành công "Đã từ chối phân công" · (a3) tự quay về màn danh sách · (b) bản ghi phân công `trangThai=TU_CHOI` + `lyDoTuChoi` khớp từng chữ + có mốc thời gian · (c) hồ sơ về đúng `DA_TIEP_NHAN` (không phải "Chờ phê duyệt") và phân công lại được · (d) cán bộ phụ trách nhận thông báo **kèm nguyên văn lý do** trên **cả 2 kênh** (chuông + thư). |

**Vế duy nhất quyết định verdict vòng này: (e) lưu vết — lý do trong NHẬT KÝ VỤ VIỆC + đọc lại được trên hồ sơ.**

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

**Kết quả đối chiếu: 0/3 trích dẫn bị lệch.** Ba số dòng ghi trong ô "Kết quả verify" cũ (`:2142` · `:826-827` · `:1735`) **vẫn đúng nguyên** trên bản chốt hiện tại.

| Trích dẫn cũ | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng |
|---|---|---|
| `srs-fr-05-vu-viec.md:2142` | **:2142 — KHÔNG lệch** | `| 9 | ly_do | text | N | Bắt buộc khi hanh_dong ∈ ('YEU_CAU_BO_SUNG','MO_LAI','TU_CHOI_PHAN_CONG','TU_CHOI_PD','HUY_CONG_KHAI') | — | Lý do |` |
| `srs-fr-05-vu-viec.md:826-827` | **:826-827 — KHÔNG lệch** | `:826` = `| 6 | Ghi lịch sử | — |` · `:827` = `| 7 | Ghi nhật ký thao tác | BR-DATA-05 |` |
| `srs-fr-05-vu-viec.md:1735` | **:1735 — KHÔNG lệch** | `| 12 | sidebar | Dòng thời gian (Timeline) | C18 | Lịch sử xử lý từ LICH_SU_VU_VIEC: "dd/mm HH:mm — {ho_ten} {hanh_dong}". Tự động cuộn đến mục mới nhất | — | Luôn |` |

**Dòng nền bổ sung (agent này tự mở kiểm, dùng để chống Pass/Fail oan — cũng không lệch):**

| Dòng | Nguyên văn (rút gọn ≤200 ký tự) | Dùng để |
|---|---|---|
| `:795` | `### FR-V.I-10: Xác nhận tham gia hỗ trợ (UC60)` | Định vị chức năng |
| `:807` | `| PRE-02 | VV ở trạng thái DA_PHAN_CONG, tài khoản hiện tại là PHAN_CONG_VU_VIEC.nguoi_xu_ly_id của phân công đang chờ xác nhận |` | Tiền đề |
| `:815` | `| 3 | ly_do_tu_choi | text (long) | Cond | Bắt buộc nếu TU_CHOI; ≥ 10 ký tự (BR-FLOW-04), **tối đa 2.000 ký tự** [PDHSVV_04 chốt 2026-07-24] |` | Ràng buộc input |
| `:823` | `| 3 | Nếu TU_CHOI: chuyển VV → DA_TIEP_NHAN (phân công lại) | SM-VUVIEC |` | Vế (c) đã hết lỗi |
| `:2129` | `**Mô tả:** Nhật ký toàn bộ thao tác trên VV — audit trail + nguồn hiển thị Timeline (SCR-V.I-03).` | Nhật ký = nguồn của Timeline |
| `:2130` | `**Tham chiếu FR:** FR-V.I-06, FR-V.I-07, **FR-V.I-10**, FR-V.I-11, FR-V.I-13, FR-V.I-15, FR-V.I-16, FR-V.I-17, FR-V.I-CROSS-01` | FR-V.I-10 nằm trong nhóm ghi nhật ký |
| `:2136` | `| 3 | hanh_dong | text | Y | CHECK IN ('TAO_VV','TIEP_NHAN','KIEM_TRA','YEU_CAU_BO_SUNG','BO_SUNG_HS','PHAN_CONG','XAC_NHAN_PHAN_CONG','TU_CHOI_PHAN_CONG','CAP_NHAT_KQ','TRINH…` | Tên hành động phải tìm |
| `:2406` | `Mọi hành động "Từ chối" phải nhập lý do. Lý do hiển thị cho người tạo ban đầu.` | **Căn cứ của vế "đọc lại được trên hồ sơ"** |
| `:1745` | `| DANG_KIEM_TRA (kết luận Đạt) / DA_TIEP_NHAN (phân công lại sau khi bị từ chối) | [Phân công] (modal 2 thẻ, gộp MH-05.5) | CB NV | …` | Công thức dựng lại tiền đề |
| `:1746` | `| DA_PHAN_CONG | [Chấp nhận] [Từ chối] (gộp MH-05.6) | Người được phân công | Chấp nhận → DANG_XU_LY / Từ chối → DA_TIEP_NHAN (phân công lại) |` | Nút cần thấy trước khi bấm |

> ⚠️ **Điểm phải hiểu đúng để không prescribe:** `:1735` khai chuỗi hiển thị Timeline là `"dd/mm HH:mm — {ho_ten} {hanh_dong}"` — **không** có chỗ đặt `ly_do` trong chính chuỗi đó. Yêu cầu "cán bộ đọc được lý do trên hồ sơ" đứng trên **`:2406` (BR-FLOW-04)**, không đứng trên định dạng dòng của `:1735`. ⇒ Lý do hiện **ở bất kỳ đâu trên màn chi tiết** (mở rộng mục nhật ký, tooltip, accordion, cột riêng…) đều tính là đạt. Chỉ FAIL khi **không chỗ nào trên màn chi tiết** đọc được.

---

## 3. Precondition + dữ liệu + công thức dựng

### 3.1 Vai trò / tài khoản (env `https://18.143.165.120.nip.io`, MailHog `http://18.143.165.120:8025/`)

| Vai trò | Tài khoản | Mật khẩu | Dùng để |
|---|---|---|---|
| **Người ra verdict** — cán bộ nghiệp vụ **đang phụ trách hồ sơ** | `cbnv_tw_01` (cấp TW, `donViId 00000000-0000-4000-8000-000000000001`) | `Test@1234` | **Mở chi tiết vụ việc đọc Dòng thời gian** — đây là tài khoản chốt PASS/FAIL |
| Cán bộ nghiệp vụ TW thứ hai (dựng dạng ②) | `cbnv_tw_02` | `Test@1234` | Kiểm tra hồ sơ + Phân công (để `nguoi_phan_cong_id` ≠ người tạo) |
| **Người bấm [Từ chối]** cấp TW | `qa_tvvseed28` (TVV + CG, Cục Bổ trợ tư pháp – BTP, `userId 5432719c-c542-4a5d-8c3a-db1b8a918bbf`) | `Test@1234` | Thao tác từ chối dạng ①② |
| **Người bấm [Từ chối]** cấp ĐP (dạng ③) | `nht_ag_uat2` (NHT, Sở Tư pháp An Giang) | `Test@1234` | Thao tác từ chối dạng ③ |
| Cán bộ ĐP dựng dạng ③ | `cbnv_dp_01` (tiếp nhận + kiểm tra) · `cbnv_dp_02` (phân công) | `Test@1234` | Chỉ dựng tiền đề |
| Doanh nghiệp gửi hồ sơ dạng ③ | `0209888006` (*Cong ty QA UAT An Giang*) | `Test@1234` | Chỉ dựng tiền đề (`created_by` = DN) |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Chỉ tra định danh khi bí; quyền rộng che lỗi phân quyền |

### 3.2 Màn / đường dẫn

- Người được phân công: **Vụ việc HTPL → chi tiết vụ việc** `/vu-viec/{id}` — thanh hành động có **[Chấp nhận] [Từ chối]** khi hồ sơ ở "Đã phân công" (`:1746`).
- Cán bộ ra verdict: **cùng màn `/vu-viec/{id}`**, cuộn tới khối **"Dòng thời gian"** (`:1735`, điều kiện hiển thị **"Luôn"**).

### 3.3 Trạng thái dữ liệu hiện tại + công thức dựng lại (BẮT BUỘC — kho tiền đề đã cạn)

**Đã bị tiêu thụ, KHÔNG còn dùng được:**
- `input/input.md:111-113` — `VV-BTP-TW-20260712-001 / -003 / -005` đã bị từ chối ở vòng 20/07 → nay ở `DA_TIEP_NHAN`, không còn người xử lý.
- Vòng 06/08 tiêu thêm 3 hồ sơ: `VV-BTP-TW-20260806-001`, `VV-BTP-TW-20260806-002`, `VV-STP-AG-20260806-004` → cả 3 nay ở **`DA_TIEP_NHAN`**, `nguoiXuLyId = null`, `coPhanCongBiTuChoi = true`.

⇒ **Không có sẵn hồ sơ nào ở "Đã phân công". Phải dựng trước khi đo.**

**Công thức A — TÁI SỬ DỤNG (nhanh nhất, ưu tiên).** 6 hồ sơ trên đang ở `DA_TIEP_NHAN` và theo `:1745` trạng thái này **có nút [Phân công]** ("phân công lại sau khi bị từ chối"):

```
Đăng nhập cbnv_tw_01 (hoặc cbnv_tw_02 cho dạng ②)
  → mở /vu-viec/{id} của VV-BTP-TW-20260806-001 (hoặc -002)
  → [Phân công] → thẻ "Cá nhân" → chọn qa_tvvseed28 → Xác nhận
  → hồ sơ về "Đã phân công", bản ghi phân công ở "Chờ xác nhận"
Đăng nhập qa_tvvseed28 → mở chính hồ sơ đó → [Từ chối]
  → nhập lý do ≥10 ký tự, CHUỖI MỐC-GIỜ DUY NHẤT dạng
     QA-XNTG-<YYYYMMDD-HHMM>-tu-choi-tham-gia-ho-tro   (ghi lại nguyên văn)
  → Xác nhận. Ghi lại thời điểm bấm.
```
Dạng ③ làm y hệt trên `VV-STP-AG-20260806-004` với `cbnv_dp_02` phân công cho `nht_ag_uat2`.

**Công thức B — DỰNG MỚI (nếu A hỏng, đúng khối CÁCH VERIFY dòng 734):**
```
cán bộ nhập hồ sơ thủ công -> tiếp nhận -> kiểm tra hồ sơ kết luận Đạt
  -> Phân công cho một tư vấn viên / người hỗ trợ
  -> đăng nhập chính người đó -> [Từ chối] -> nhập lý do >= 10 ký tự
     (ghi lại nguyên văn chuỗi đã nhập) -> Xác nhận
```

**Chốt định danh TRƯỚC khi bấm (bắt buộc ghi vào báo cáo):** với mỗi hồ sơ đọc và ghi `mã VV` · `created_by` · `nguoi_tiep_nhan_id` · `nguoi_phan_cong_id` · `nguoi_xu_ly_id`. Không chốt được ⇒ chưa được đo, vì "cán bộ phụ trách" phải là **đúng người**.

> ⚠️ `qa_tvvseed28` đã bị đổi `loaiTvv` **TVV → CG** ngày 21/07/2026 (`tuVanVienId 98cfd963-3cd3-4c8a-bfa9-625460824d6d`). Nếu modal [Phân công] lọc theo `loaiTvv` mà không thấy tài khoản này → đổi lại hoặc chọn TVV/NHT khác **cùng đơn vị**, và **khai rõ đã mutate gì**.

---

## 4. Các bước đo (thao tác UI thật)

> Bước 1–3 chép nguyên ý khối CÁCH VERIFY dòng **735–737**; bước 0 và 4 là thao tác bắt buộc để bước 1–3 chạy được.

0. **Dựng tiền đề** theo §3.3 trên **≥ 2 hồ sơ** (khuyến nghị 3 — xem §7). Ghi lại **nguyên văn chuỗi lý do** và **thời điểm bấm Xác nhận** của từng hồ sơ.
1. **Đăng nhập cán bộ nghiệp vụ phụ trách hồ sơ đó** (`cbnv_tw_01` cho dạng ①②, `cbnv_dp_01` cho dạng ③), mở chi tiết vụ việc, **cuộn tới khối "Dòng thời gian"**.
2. **Đọc mục ứng với thao tác từ chối phân công**: phải thấy được **lý do từ chối** đã nhập ở bước dựng tiền đề. Nếu dòng nhật ký hiển thị rút gọn → **mở rộng / bấm vào mục đó** trước khi kết luận là "không có".
3. **Đo bằng đường thứ hai** — xem §5.
4. **Lặp bước 1–3** cho từng hồ sơ còn lại. Ghi bảng: `mã VV | chuỗi lý do đã nhập | lý do đọc được trên màn | lý do đọc được từ máy chủ | khớp từng chữ?`.

**Chống bỏ sót (không phải tiêu chí chấm):** trước khi kết luận "màn không cho đọc", quét toàn màn chi tiết bằng `evaluate_script` tìm chuỗi lý do trong `document.body.innerText` — lý do có thể nằm ngoài khối Dòng thời gian (accordion, tooltip, cột riêng) và **vẫn tính là đạt** theo `:2406`.

---

## 5. Đường đo thứ hai (đối chứng độc lập)

Nguyên văn khối CÁCH VERIFY dòng **737**:

> `3) Đo bằng đường thứ hai: đọc lại nhật ký của chính vụ việc đó từ máy chủ (GET /api/v1/vu-viecs/{id}/lich-su) và đối chiếu mục có hành động từ chối phân công.`

- Gọi **bằng chính phiên đăng nhập của cán bộ phụ trách** (cookie-auth), không dùng `admin` để ra verdict.
- Tìm mục có `hanhDong = "TU_CHOI_PHAN_CONG"` (`:2136`), đối chiếu:
  - có trường lý do, **khác rỗng**;
  - nội dung **khớp từng chữ** chuỗi đã nhập;
  - `thoiGian` lệch ≤ vài giây so với thời điểm bấm.
- Vòng trước bản ghi này chỉ có `id · entityType · hanhDong · nguoiThucHienId · nguoiThucHien · thoiGian · duLieuCu · duLieuMoi` — **không có trường lý do**. Nếu lý do được ghi vào `duLieuMoi` thay vì một trường riêng thì **vẫn tính là đạt** (yêu cầu là *lưu vào nhật ký*, không phải *tên trường nào*).
- **Mâu thuẫn 2 đường** (máy chủ có / màn không, hoặc ngược lại) ⇒ ghi cả hai vào bug entry, xem §6 FAIL.

---

## 6. ✅ PASS khi / ❌ FAIL nếu — **chép nguyên văn từ khối CÁCH VERIFY** (bug-report.md:738–741)

```
✅ PASS khi: mục nhật ký của thao tác từ chối phân công mang lý do khác rỗng và khớp từng chữ chuỗi đã nhập, ĐỒNG THỜI cán bộ đọc được lý do đó ngay trên hồ sơ. Đúng ở cả hai đường đo, và lặp lại được trên ít nhất 2 hồ sơ khác nhau.
❌ FAIL nếu: nhật ký vẫn không có lý do; hoặc máy chủ đã có lý do nhưng màn hình không cho cán bộ đọc được (fix một phần vẫn là FAIL); hoặc lý do lệch so với chuỗi đã nhập.
⚠️ Đừng chấm FAIL vì cách trình bày dòng nhật ký (thứ tự, định dạng ngày giờ, chỗ đặt lý do) — đặc tả không quy định phần này.
⚠️ Đừng chấm PASS vì thấy lý do hiện trong thông báo gửi cán bộ hoặc trong bản ghi phân công — hai chỗ đó đã có sẵn từ trước và không thay cho nhật ký; phải đọc đúng mục nhật ký của vụ việc.
```

---

## 7. Độ phủ biến thể bắt buộc

**Sàn cứng của khối PASS: N ≥ 2 hồ sơ khác nhau.**
**Chuẩn đã khóa ở mục 5 file tiêu chí vòng trước: M = 3 dạng, mỗi dạng một bản ghi riêng ⇒ N ≥ 3.**

| # | Dạng | Cách dựng | Vì sao bắt buộc |
|---|---|---|---|
| **①** | Người tạo **≡** người phân công | `cbnv_tw_01` tạo + tiếp nhận + **tự phân công** cho `qa_tvvseed28` | Ca đơn giản nhất; 1 người gánh 2 vai |
| **②** | Người tạo **≠** người phân công | `cbnv_tw_01` tạo + tiếp nhận · **`cbnv_tw_02`** kiểm tra + phân công | Tách được *"gửi/hiện cho người phân công"* khỏi *"cho người tạo"* — đúng chỗ `:2406` nói "người tạo ban đầu" |
| **③** | Người tạo là **Doanh nghiệp** | DN `0209888006` gửi · `cbnv_dp_01` tiếp nhận + kiểm tra · `cbnv_dp_02` phân công · `nht_ag_uat2` từ chối | `created_by` **không phải cán bộ** ⇒ nếu hệ thống chỉ hiện lý do cho *người tạo* thì dạng này lộ ngay |

**Đã tra 3 nguồn để chốt M (nói rõ đã tra gì):**
1. **Chuẩn PASS đã khóa** — bug-report.md:738 chỉ đặt sàn "ít nhất 2 hồ sơ khác nhau", **không** khai dạng ⇒ phải lấy M từ nguồn 2 + 3.
2. **Mục SRS về nguồn dữ liệu** — `srs-fr-05-vu-viec.md:160` `### FR-V.I-02: Gửi hồ sơ yêu cầu HTPL (UC52)` → `:199` `| 7 | Ghi LICH_SU_VU_VIEC: hanh_dong='TAO_VV', vai_tro='DN' |`; và `:300` `### FR-V.I-04: Nhập hồ sơ yêu cầu thủ công (UC54)` → `:345` `| 10 | Ghi LICH_SU_VU_VIEC: hanh_dong='TAO_VV', vai_tro='CB_NV' |` ⇒ **2 đường tạo vụ việc** (DN gửi / CB nhập tay) ⇒ ra dạng ③ tách khỏi ①②.
3. **Bộ lọc + enum trên màn / mô hình dữ liệu** — `:2098` `nguoi_phan_cong_id … CB NV thực hiện phân công` · `:2022` `nguoi_tiep_nhan_id … CB NV tiếp nhận` · `:2376` `Mọi entity đều có 7 common fields (id, created_at, updated_at, created_by, …)` ⇒ *người tạo* và *người phân công* là **2 vai độc lập** ⇒ bắt buộc phủ cả ca trùng (①) lẫn ca tách (②). Enum liên quan: `:2096` `PHAN_CONG_VU_VIEC.trang_thai CHECK IN ('CHO_XAC_NHAN','CHAP_NHAN','TU_CHOI')` — chỉ 1 nhánh (`TU_CHOI`) thuộc case này.

**Chiều KHÔNG bắt buộc (ghi để agent đo không tự nới):** `:800` nói người được phân công *"bao gồm NHT/TVV/CG cá nhân **hoặc TVV do tổ chức tư vấn cử**"*, và `:1745` khai modal phân công có **2 thẻ "Cá nhân" / "Tổ chức"**. Vòng trước chỉ phủ **Cá nhân** (TVV cấp TW + NHT cấp ĐP). Bug này nằm ở tầng ghi nhật ký, **không rẽ nhánh theo cá nhân/tổ chức** ⇒ **không** thêm vào M. Nếu dựng được thì đo thêm và ghi nhận, **không** dùng để kéo verdict.

**Nếu chỉ dựng được 2 hồ sơ:** ưu tiên **dạng ② và ③** (bỏ ①), và **khai rõ dạng nào chưa dựng + vì sao** trong báo cáo.

---

## 8. ⚠️ Bẫy / rule chống kết luận oan

1. **Bẫy "thấy lý do là Pass"** — vòng trước lý do **vẫn còn nguyên vẹn ở 2 chỗ khác**: bản ghi phân công (`lyDoTuChoi`, `:2097`) và **thông báo + email gửi cán bộ** (nguyên văn có dòng `- Lý do từ chối: …`). Hai chỗ đó **đã đúng từ trước**, **không** thay cho nhật ký. Nhìn thấy lý do trong chuông/thư/bản ghi phân công mà chấm PASS = **Pass oan**.
2. **Bẫy "fix nửa đường"** — máy chủ đã có lý do trong nhật ký nhưng màn chi tiết không cho cán bộ đọc ⇒ **vẫn FAIL** (nguyên văn khối CÁCH VERIFY). Ngược lại cũng vậy.
3. **Bẫy "không thấy = không có"** — trước khi kết luận màn không cho đọc, phải **mở rộng mục nhật ký** và quét `innerText` toàn màn. Lý do đặt ở chỗ khác trong màn chi tiết **vẫn đạt** (`:2406`; `:1735` không quy định chỗ đặt lý do).
4. **Bẫy dùng `admin`** — `admin` quyền rộng, đọc được thứ cán bộ không đọc được ⇒ **CẤM ra verdict bằng `admin`**; chỉ dùng để điều tra và phải khai.
5. **Bẫy đọc nhầm hồ sơ** — 3 hồ sơ của vòng trước đã ở `DA_TIEP_NHAN` và **không còn** bản ghi phân công "Chờ xác nhận". Mở nhầm hồ sơ cũ sẽ thấy mục nhật ký từ chối **của lần trước** (không có lý do, vì được ghi trước khi fix) ⇒ **false Reopen**. Bắt buộc đo trên **thao tác từ chối MỚI thực hiện sau khi dev fix**.
6. **Bẫy record cũ (dữ liệu đóng băng)** — bug này sửa **trường được lưu lúc ghi nhật ký**. Bản ghi nhật ký sinh **trước** bản fix sẽ mãi mãi không có lý do dù dev đã sửa đúng. **Phép thử quyết định = bản ghi nhật ký sinh MỚI.**
7. **Bẫy bản dựng cũ trong tab** — tab MCP mở lâu vẫn chạy bó mã cũ. **Tải lại trang bằng địa chỉ** và **ghi lại tên bó mã FE + `last-modified` + `etag`** vào báo cáo trước khi đo.
8. **Không kéo verdict bằng thao tác khác** — `YEU_CAU_BO_SUNG` cũng thuộc nhóm bắt buộc có lý do (`:2142`) và vòng trước cũng thiếu. Ghi nhận để dev biết phạm vi, **không** dùng để chấm case này.
9. **Không FAIL vì bộ đếm ký tự ô lý do dừng ở 1000** trong khi `:815` ghi "tối đa 2.000 ký tự" — lệch này **không thuộc vế nào đối tác nêu**; nếu tái hiện thì mở phiếu riêng.
10. **Giới hạn hiệu lực** — verdict chỉ có giá trị cho **env nội bộ `18.143.165.120.nip.io` + bản dựng đo được**. Bằng chứng gốc của đối tác quay trên `htpldn-uat.ospgroup.vn`. Phải ghi câu giới hạn này trong kết quả.

---

## 9. Đối chiếu khối note ↔ bug entry

**Kết luận: GIỐNG về bản chất tiêu chí — LỆCH ở độ chi tiết (ô sheet là bản rút gọn, thiếu 4 thứ). KHÔNG có điểm nào mâu thuẫn nhau.**

| Vế | Bug entry (dòng 731–742) | Ô sheet "CÁCH KIỂM LẠI SAU KHI SỬA" | Đánh giá |
|---|---|---|---|
| Thao tác dựng tiền đề | Có **công thức 7 bước đầy đủ** (nhập tay → tiếp nhận → kiểm tra Đạt → phân công → đăng nhập người được phân công → Từ chối → lý do ≥10 ký tự → Xác nhận) | Chỉ "cho người được phân công từ chối một vụ việc kèm lý do" | **LỆCH — sheet thiếu công thức dựng.** Dùng bug entry. |
| Người đo | "cán bộ nghiệp vụ đang phụ trách hồ sơ (ví dụ `cbnv_tw_01`)" | "tài khoản cán bộ phụ trách" | **GIỐNG** |
| Chỗ đo | "màn chi tiết vụ việc `/vu-viec/{id}`, khối **Dòng thời gian**" | "mở chi tiết vụ việc đó và xem mục từ chối trong nhật ký" | **GIỐNG** |
| Đường đo thứ hai | **Bước 3 bắt buộc**: `GET /api/v1/vu-viecs/{id}/lich-su` | **KHÔNG có** | **LỆCH — sheet thiếu hẳn đường đo 2.** Bug entry chặt hơn ⇒ **theo bug entry**. |
| Số hồ sơ | "ít nhất 2 hồ sơ khác nhau" | "ít nhất 2 vụ việc" | **GIỐNG** |
| PASS | lý do **khác rỗng** + **khớp từng chữ** + cán bộ **đọc được ngay trên hồ sơ** + **đúng ở cả hai đường đo** | "nhật ký có lý do, khớp từng chữ, và cán bộ đọc được ngay trên hồ sơ" | **GIỐNG 3/4 vế** — sheet **thiếu** "đúng ở cả hai đường đo" |
| FAIL | (i) nhật ký không có lý do · (ii) máy chủ có mà màn không cho đọc (**fix một phần vẫn FAIL**) · (iii) **lý do lệch chuỗi đã nhập** | (i) "nhật ký vẫn trống lý do" · (ii) "dữ liệu đã có mà màn hình không cho đọc" | **GIỐNG 2/3** — sheet **thiếu** vế (iii), nhưng "khớp từng chữ" ở vế Đạt đã hàm ý |
| ⚠️ chống FAIL oan | "Đừng chấm FAIL vì cách trình bày dòng nhật ký (thứ tự, định dạng ngày giờ, chỗ đặt lý do)" | **KHÔNG có** | **LỆCH — sheet thiếu.** Giữ theo bug entry. |
| ⚠️ chống PASS oan | "Đừng chấm PASS vì thấy lý do trong thông báo gửi cán bộ hoặc trong bản ghi phân công" | "Lưu ý: thấy lý do trong thông báo gửi cán bộ hoặc trong bản ghi phân công thì chưa tính là đạt — đó là hai chỗ khác, không phải nhật ký vụ việc" | **GIỐNG** (sheet diễn đạt dài hơn, cùng nghĩa) |

**⇒ Chuẩn dùng để đo = KHỐI TRONG BUG ENTRY (bản đầy đủ).** Ô sheet là bản rút gọn cho đối tác; đo theo sheet sẽ **bỏ mất đường đo thứ hai** và **2 lằn ranh chống oan**.

**Đối chiếu với đặc tả hiện hành (mục E):** khối CÁCH VERIFY **vẫn khớp** đặc tả — `:2142` (lý do **bắt buộc** khi `hanh_dong = 'TU_CHOI_PHAN_CONG'`), `:826-827` (bước 6 *Ghi lịch sử* + bước 7 *Ghi nhật ký thao tác*), `:2406` (lý do **hiển thị** cho người tạo ban đầu), `:1735` (Timeline điều kiện hiển thị **"Luôn"**). **Không có điểm nào phải nới hay siết.**

---

## 10. Cảnh báo cho agent đo

1. 🔴 **Phải TỰ DỰNG tiền đề — kho đã cạn sạch.** Không hồ sơ nào đang ở "Đã phân công". Bỏ qua bước dựng ⇒ không có gì để đo ⇒ **cấm mọi verdict, kể cả ô trống**.
2. 🔴 **Chỉ đo trên bản ghi nhật ký sinh MỚI sau bản fix.** Đọc lại 3 hồ sơ cũ (`VV-BTP-TW-20260806-001/-002`, `VV-STP-AG-20260806-004`) sẽ thấy mục từ chối **của 06/08** — vĩnh viễn không có lý do → **Reopen oan**.
3. 🔴 **Ghi lại nguyên văn chuỗi lý do trước khi bấm.** Không có chuỗi gốc thì không chấm được "khớp từng chữ". Dùng chuỗi mốc-giờ duy nhất `QA-XNTG-<YYYYMMDD-HHMM>-…`.
4. **Ghi dấu vân tay bản dựng** (bó mã FE · `last-modified` · `etag`) **trước** khi đo, và **tải lại trang bằng địa chỉ** — vòng 06/08 đã gặp **triển khai mới xen giữa lô**.
5. **Không dùng `admin` ra verdict.** Nếu buộc phải tra định danh bằng `admin` thì khai rõ và đối chứng lại bằng tài khoản cán bộ.
6. **6/7 vế đã hết lỗi — đừng đo lại rồi log lại.** Nếu một trong 6 vế đó **hỏng lại** (vd lại văng màn 403, lại về "Chờ phê duyệt") thì đó là **hồi quy mới**: log thành mục riêng, ghi rõ "hồi quy so với bản 06/08", **không** trộn vào vế lưu vết.
7. **Lý do có thể được ghi vào `duLieuMoi` thay vì trường `ly_do` riêng** — vẫn đạt. Đừng prescribe tên trường.
8. Nếu login fail → **Rule 7**: fallback **cùng vai trò + cùng cấp** (`cbnv_tw_01` → `cbnv_tw_02` → `cbnv_tw_03`), **khai account thực dùng**; tuyệt đối không đổi cấp TW↔ĐP (đổi scope dữ liệu ⇒ verdict vô hiệu).
9. Ảnh chụp lưu đúng `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/<...>/image/`.
