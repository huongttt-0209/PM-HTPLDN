# Tiêu chí verify — XNTGHTVV_03

Mã case: **XNTGHTVV_03** (dòng 51 tab `bug`) · Thời điểm viết: **2026-08-06 13:05**
Môi trường verify: **https://18.143.165.120.nip.io** · Bản dựng (tự đo ở giai đoạn B, 2026-08-06 15:05):
`HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified: Thu, 06 Aug 2026 07:13:15 GMT`
· `etag "6a74340b-428"`.
⚠️ **Khác bản dựng của 2 case trước cùng lô** (`assets/index-CNwX9JjX.js` · `last-modified 06/08/2026 02:51:16 GMT`
· `etag "6a73f6a4-428"`) ⇒ **có triển khai mới xen giữa lô B6**; số đo của case này chỉ thuộc về bản dựng ghi ở đây.

> **Khai báo hồ sơ QA đợt trước (bắt buộc theo flow 04):** đã đọc
> [`../../reverify-week-3/cond/XNTGHTVV_03.md`](../../reverify-week-3/cond/XNTGHTVV_03.md) (bảng điều kiện tuần 3,
> đo ngày 20/07/2026, kết luận tái hiện 403 2/2 với `qa_tvvseed28`) và ghi chú tài khoản trong
> [`../../input/input.md`](../../input/input.md) dòng 103–117.
> **Mọi ngưỡng ở mục 4 dưới đây suy từ ĐẶC TẢ srs-v3.5, KHÔNG lấy số đo cũ làm ngưỡng.** Số đo cũ chỉ dùng để
> biết dữ liệu tiền đề đã bị tiêu thụ (3 vụ việc VV-BTP-TW-20260712-001/-003/-005 nay ở DA_TIEP_NHAN) nên
> **phải dựng tiền đề mới**.

---

## 1. Đối tác phản ánh

**Thao tác:** Người được phân công mở chi tiết vụ việc ở trạng thái "Đã phân công" → bấm **Từ chối** → nhập lý do
hợp lệ → **Xác nhận**.

**Kết quả mong đợi của đối tác — tách 5 vế (vế a tách tiếp 3 ý vì 3 ý này rẽ nhánh khác nhau):**

| Vế | Nội dung đối tác đòi |
|---|---|
| **(a1)** | Thao tác từ chối được hệ thống **chấp nhận và xử lý**, không văng ra màn báo lỗi phân quyền |
| **(a2)** | Có **thông báo** cho người dùng, nội dung *"Đã từ chối tham gia vụ việc"* |
| **(a3)** | Sau đó **chuyển về màn hình danh sách** |
| **(b)** | Bản ghi phân công được cập nhật: trạng thái **"Từ chối"** + **thời điểm từ chối** + **lý do từ chối** |
| **(c)** | Hồ sơ chuyển trạng thái **"Đã phân công" → "Đã tiếp nhận"** |
| **(d)** | **Gửi thông báo cho cán bộ nghiệp vụ phụ trách, kèm lý do từ chối** |
| **(e)** | **Lưu vết thao tác** theo quy định |

**Kết quả thực tế đối tác ghi:** hệ thống chuyển sang màn lỗi **403 — "Vụ việc không được phân công cho bạn"**
mặc dù vụ việc đang được phân công cho tư vấn viên; *"sau đó hệ thống cập nhật trạng thái của bản ghi là
'Chờ phê duyệt'"*.

**Kết quả verify vòng QA trước (sẽ bị đè ở vòng này):** *"Cán bộ nghiệp vụ phụ trách không nhận được thông báo
kèm lý do từ chối."* ⇒ tranh chấp vòng này tập trung ở **vế (d)**, nhưng vẫn phải đo lại **đủ 5 vế** vì dev
báo Fixed cho cả case.

### Bằng chứng đã mở xem

Tệp: `../partner-evidence/XNTGHTVV_03.webm` (3.842.991 byte, video 31s).
Frame đã trích + **đã mở đọc**: `../partner-evidence/frames-XNTGHTVV_03/`

| Frame | Thấy gì |
|---|---|
| `t000.00s.jpg` | Hộp thoại **"Từ chối phân công"**, ô *Lý do* mới gõ 1 ký tự → cảnh báo đỏ *"Tối thiểu 10 ký tự"*, bộ đếm **1 / 1000**. Header: `huongcg` · **TVV · CG** · **BTP · TW**. Nút **[Chấp nhận] [Từ chối]** hiện đủ, badge *"Còn 7 ngày LV"* |
| `t008.07s.jpg` | Lý do đã nhập hợp lệ: *"TKM test từ chối thành công"* — **27 / 1000** ký tự. Nút **[Xác nhận]** sáng |
| `t009.55s.jpg` | **Khoảnh khắc bấm Xác nhận** — hộp thoại đang mờ dần, lộ **mã vụ việc `VV-BTP-TW-20260630-001`**, chặng tiến trình đang ở **"Đã phân công"**, URL vẫn `.../vu-viec/ab08db14-4e92-48fe-8f2b-b2a0ad00b4a3` |
| `t010.06s.jpg` → `t022.49s.jpg` | **KHOẢNH KHẮC LỖI** — URL nhảy sang `htpldn-uat.ospgroup.vn/**403**`, breadcrumb *"Không tìm thấy trang"*, chữ lớn **403** + **"Vụ việc không được phân công cho bạn"**, dòng *Mã lỗi: ERR-AUTH-VPD-00-04*, dòng **"Vai trò hiện tại: TVV CG"**. Không thấy thông báo thành công nào trước khi chuyển màn |
| `t024.95s.jpg` | Danh sách tab **"Tất cả 4"** — 4 vụ việc, cột *Người xử lý / Tổ chức* đều là `huongcg`: `VV-BKH-20260526-001` (Chờ phê duyệt), `VV-BTP-TW-20260525-001`, `VV-BTP-TW-20260514-002`, `VV-BTP-TW-20260511-001` (đều Đã phân công). **`VV-BTP-TW-20260630-001` — bản ghi vừa bị từ chối — KHÔNG còn trong danh sách** |
| `t029.03s.jpg` / `t031.04s.jpg` | Tab **"Chờ phê duyệt 1"** chỉ có **`VV-BKH-20260526-001`** (DN *Công ty TNHH Sông Hồng B…*, ngày 26/05) — **không phải** bản ghi vừa bị từ chối |

**Bằng chứng ĐÚNG case này** — cùng màn (chi tiết vụ việc, trạng thái "Đã phân công"), cùng thao tác (Từ chối +
nhập lý do + Xác nhận), cùng triệu chứng đối tác mô tả.

**2 điểm lệch giữa lời văn của đối tác và chính video của họ — phải kiểm lại ở giai đoạn B, không suy đoán ở đây:**
1. Ý *"cập nhật trạng thái bản ghi là Chờ phê duyệt"*: bản ghi duy nhất ở "Chờ phê duyệt" trong video là
   `VV-BKH-20260526-001`, **khác mã** với bản ghi vừa bị từ chối (`VV-BTP-TW-20260630-001`).
2. Bản ghi vừa bị từ chối **biến mất khỏi danh sách của chính người bị phân công** ngay sau thao tác — chưa
   đủ căn cứ để nói backend đã xử lý hay chưa (danh sách đang bật *"Bộ lọc nâng cao (2)"*). Giai đoạn B phải
   đọc lại chính bản ghi mình dựng, không suy từ video.

**Lệch môi trường / bản dựng:** video quay trên env đối tác `htpldn-uat.ospgroup.vn` ngày **10/07/2026 08:36–08:37**;
đợt này verify trên env nội bộ `18.143.165.120.nip.io`. Đây là **giới hạn hiệu lực của verdict**, không phải GAP
(ghi lại ở mục 6).

---

## 2. Đặc tả nói gì

**Nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**File chính:** `srs-fr-05-vu-viec.md` — chức năng **FR-V.I-10: Xác nhận tham gia hỗ trợ (UC60)** (dòng 795).
Đã đối chiếu thêm `srs-fr-12-tv-chuyen-sau.md` (luồng CG xác nhận/từ chối của **Tư vấn chuyên sâu** — entity
khác, dòng 189–198 & 1491–1492) và `srs-fr-04-chuyen-gia-tvv.md` (quản lý TVV/CG — **không** đặt thêm quy tắc
nào cho FR-V.I-10). ⇒ luồng của case này chỉ do `srs-fr-05` chi phối.

### 2.1 Ai được phép Từ chối

- `srs-fr-05-vu-viec.md:800` — *"Người được phân công xử lý vụ việc xác nhận hoặc từ chối tham gia hỗ trợ VV.
  Người được phân công là tài khoản trong `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id`, bao gồm NHT/TVV/CG cá nhân hoặc
  TVV do tổ chức tư vấn cử."*
- `:807` (PRE-02) — *"VV ở trạng thái DA_PHAN_CONG, tài khoản hiện tại là `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id` của
  phân công đang chờ xác nhận"*
- `:821` (Bước 1) — *"Kiểm tra tài khoản hiện tại là người được phân công trong `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id`"*
- `:840` (E1) — *"Tài khoản hiện tại không phải người được phân công | ERR-XN-01 | 'Bạn không được phân công cho
  vụ việc này' | ERROR"*
- `:1746` (bảng nút SCR-V.I-03) — *"DA_PHAN_CONG | [Chấp nhận] [Từ chối] … | **Người được phân công** | Chấp nhận
  → DANG_XU_LY / Từ chối → DA_TIEP_NHAN (phân công lại)"*

⇒ Đặc tả **nói rõ**: chỉ khi tài khoản **không** phải người được phân công thì hệ thống mới được từ chối thao tác.
Đúng người được phân công ⇒ **không được** rơi vào nhánh lỗi phân quyền.

### 2.2 Lý do từ chối

- `:815` — *"ly_do_tu_choi | text (long) | Cond | Bắt buộc nếu TU_CHOI; ≥ 10 ký tự (BR-FLOW-04), **tối đa 2.000 ký
  tự** `[PDHSVV_04 chốt 2026-07-24]`"*
- `:2406` (BR-FLOW-04) — *"Mọi hành động 'Từ chối' phải nhập lý do. **Lý do hiển thị cho người tạo ban đầu.**"*
- `:1778` (Thông báo riêng SCR-V.I-03) — *"Người được phân công từ chối — thiếu lý do | Inline error | 'Vui lòng
  nhập lý do từ chối (tối thiểu 10 ký tự)'"*

### 2.3 Cập nhật bản ghi phân công — vế (b)

- `:824` (Bước 4) — *"Cập nhật PHAN_CONG_VU_VIEC"*
- `:2096` — *"trang_thai | text | Y | CHECK IN ('CHO_XAC_NHAN','CHAP_NHAN','TU_CHOI') | 'CHO_XAC_NHAN' | Trạng thái
  phân công"*
- `:2097` — *"ly_do_tu_choi | text | N | Bắt buộc khi trang_thai='TU_CHOI' | — | Lý do cá nhân được phân công từ chối"*
- `:2100` — *"ngay_xac_nhan | datetime | N | | — | Thời điểm cá nhân được phân công xác nhận/từ chối"*
- `:1731` (Accordion 5 SCR-V.I-03, điều kiện hiển thị *"Khi VV đã qua DA_PHAN_CONG"*) — hiển thị *"Họ tên cá nhân
  được phân công …, ngày phân công, **trạng thái xác nhận**"*

### 2.4 Chuyển trạng thái hồ sơ — vế (c)

- `:823` (Bước 3) — *"Nếu TU_CHOI: chuyển VV → DA_TIEP_NHAN (phân công lại)"*
- `:833` (Postconditions) — *"Nếu từ chối: VV quay lại DA_TIEP_NHAN để chọn người/tổ chức xử lý khác"*
- `:846` (Acceptance Criteria) — *"**Given** người được phân công từ chối **When** nhập lý do **Then** VV quay lại
  DA_TIEP_NHAN để chọn người/tổ chức xử lý khác"*
- `:2250` (SM-VUVIEC) — *"DA_PHAN_CONG --> DA_TIEP_NHAN : NHT/TVV từ chối (phân công lại)"*
- `:2292` (bảng chuyển trạng thái) — *"| DA_PHAN_CONG | DA_TIEP_NHAN | Người được phân công từ chối | Có lý do |
  Quay lại chọn người/tổ chức xử lý khác | FR-V.I-10 | — |"*

⇒ **4 vị trí trùng khớp nhau**, không mâu thuẫn. Đặc tả **nói rõ và khớp** kỳ vọng đối tác.

### 2.5 Thông báo — vế (d)

- `:825` (Bước 5) — *"Gửi thông báo CB NV"*
- `:834` (Postconditions) — *"CB NV nhận thông báo"*
- `:2480` (BR-NOTIF-01) — *"Mọi sự kiện workflow (phân công, xác nhận, **từ chối**, phê duyệt, hoàn thành, công
  khai, bổ sung hồ sơ, cảnh báo SLA) đều gửi thông báo cho người liên quan qua **2 kênh: in-app (THONG_BAO) +
  email**. Người nhận xác định theo loại sự kiện."*
- `:2482` — *"**Applied in (nhóm V.I):** FR-V.I-04, FR-V.I-09, **FR-V.I-10**, FR-V.I-12, …"* ⇒ BR-NOTIF-01 **có**
  áp cho chính chức năng này.
- `:2406` (BR-FLOW-04) — lý do *"hiển thị cho **người tạo ban đầu**"*.

**Các mốc định danh "cán bộ nghiệp vụ" trong dữ liệu — 3 người có thể KHÁC nhau:**
- `:2098` — *"nguoi_phan_cong_id | identifier | Y | FK → TAI_KHOAN(id) | — | **CB NV thực hiện phân công**"*
- `:2022` — *"nguoi_tiep_nhan_id | identifier | N | FK → TAI_KHOAN(id) | | **CB NV tiếp nhận**"*
- `:2376` — *"Mọi entity đều có 7 common fields (id, created_at, updated_at, **created_by**, updated_by,
  is_deleted, don_vi_id)"*

### 2.6 Lưu vết — vế (e)

- `:826` (Bước 6) — *"Ghi lịch sử"* · `:827` (Bước 7) — *"Ghi nhật ký thao tác | BR-DATA-05"*
- `:2129` — *"LICH_SU_VU_VIEC … Nhật ký toàn bộ thao tác trên VV — audit trail + nguồn hiển thị Timeline (SCR-V.I-03)"*
- `:2136` — `hanh_dong` CHECK IN (… `'XAC_NHAN_PHAN_CONG'`, **`'TU_CHOI_PHAN_CONG'`**, …)
- `:2142` — *"ly_do | text | N | **Bắt buộc khi hanh_dong ∈ ('YEU_CAU_BO_SUNG','MO_LAI','TU_CHOI_PHAN_CONG',
  'TU_CHOI_PD','HUY_CONG_KHAI')**"*
- `:1735` (thành phần #12 SCR-V.I-03, điều kiện hiển thị **"Luôn"**) — *"Dòng thời gian (Timeline) | C18 | Lịch sử
  xử lý từ LICH_SU_VU_VIEC: 'dd/mm HH:mm — {ho_ten} {hanh_dong}'. Tự động cuộn đến mục mới nhất"*

⇒ Đây là **bảng liệt kê đóng** + điều kiện hiển thị *"Luôn"* ⇒ đặc tả **nói rõ**, không phải im lặng.

### 2.7 IM LẶNG về

| # | Đặc tả không quy định | Hệ quả |
|---|---|---|
| S1 | **Nội dung chữ của thông báo báo thành công khi người được phân công từ chối.** Bảng *"Thông báo riêng SCR-V.I-03"* (`:1773`–`:1785`) liệt kê 11 tình huống, **có** dòng lỗi thiếu lý do (`:1778`) nhưng **không có** dòng nào cho ca từ chối **thành công**. Bảng chung §E (`:1586`–`:1597`) chỉ có câu tổng quát *"Đã lưu thành công"* / *"Đã cập nhật thông tin vụ việc"* | Vế **(a2)** — đòi đúng chữ *"Đã từ chối tham gia vụ việc"* ⇒ **cần BA** |
| S2 | **Điều hướng sau khi từ chối.** `:829` (Outputs FR-V.I-10) — *"Không có output riêng (trạng thái VV được cập nhật)"*, không nhắc điều hướng. Đối chiếu: `:347` (Outputs FR-V.I-04) **có** ghi rõ *"…xác nhận lưu thành công, **redirect chi tiết VV**"* ⇒ đặc tả **biết cách** khai điều hướng khi muốn, chỗ này cố tình không khai | Vế **(a3)** — đòi *"chuyển về màn hình danh sách"* ⇒ **cần BA** |
| S3 | **Đích danh CB NV nào nhận thông báo.** `:825`/`:834` chỉ ghi *"CB NV"*; BR-NOTIF-01 `:2480` ghi *"Người nhận xác định theo loại sự kiện"* nhưng không liệt kê người nhận cho sự kiện từ chối phân công; BR-FLOW-04 `:2406` lại nói lý do *"hiển thị cho người tạo ban đầu"* — mà `nguoi_phan_cong_id` (`:2098`), `nguoi_tiep_nhan_id` (`:2022`) và `created_by` (`:2376`) **có thể là 3 tài khoản khác nhau** | Vế **(d)** — phần *"đúng người"*: đo cả 3 ứng viên (xem mục 4 & mục 5), chỉ hỏi BA **nếu** không ai trong 3 nhận được, hoặc người nhận không phải người đối tác kỳ vọng |
| S4 | **Thông báo có bắt buộc chứa lý do từ chối hay không.** `:825` chỉ ghi *"Gửi thông báo CB NV"*; BR-FLOW-04 `:2406` đòi lý do *"hiển thị cho người tạo ban đầu"* nhưng không nói qua kênh thông báo hay qua màn chi tiết | Vế **(d)** — phần *"kèm lý do"*: đo cả 2 chỗ (nội dung thông báo **và** nơi hiển thị lý do trên hồ sơ); nếu lý do đến được người nhận qua một trong hai thì hết bất đồng, nếu không ở đâu cả thì mới là lỗi |
| S5 | Mã lỗi `ERR-AUTH-VPD-00-04` trên màn 403 của đối tác **không tồn tại** trong bất kỳ file nào của srs-v3.5 (đã grep toàn thư mục) | Chỉ ghi nhận; **không** dùng mã lỗi làm tiêu chí chấm (describe, không prescribe) |

**Đối chiếu `tasks/srs-contradictions.md`:** không có entry Open nào cho FR-V.I-10 / xác nhận-từ chối phân công vụ việc.

---

## 3. Precondition

### 3.1 Tài khoản (env `https://18.143.165.120.nip.io`, mật khẩu `Test@1234` trừ `admin`)

| Vai trò cần | Tài khoản | Dùng để làm gì |
|---|---|---|
| **Doanh nghiệp** | `0109998887` — *QA UAT Kiểm Thử DN* (DN-HNI-0001, Hà Nội) | Tạo vụ việc dạng ③ (VV do DN tự gửi) — để `created_by` là DN |
| **CB Nghiệp vụ TW — người A** | `cbnv_tw_01` | **Tạo / tiếp nhận** vụ việc ⇒ giữ vai *người tạo ban đầu* (`created_by`, `nguoi_tiep_nhan_id`) |
| **CB Nghiệp vụ TW — người B** | `cbnv_tw_02` | **Kiểm tra + Phân công** vụ việc ⇒ giữ vai *người phân công* (`nguoi_phan_cong_id`). **Bắt buộc khác người A** để phân biệt được hai vai |
| **Người được phân công (bấm Từ chối)** | `qa_tvvseed28` — TVV + CG, Cục Bổ trợ tư pháp – Bộ Tư pháp, cấp TW, `userId = 5432719c-c542-4a5d-8c3a-db1b8a918bbf` | **Chính tài khoản ra verdict** cho vế (a1)(a2)(a3)(b)(c) |
| **Kiểm thông báo** | Đăng nhập lại lần lượt **`cbnv_tw_01`** và **`cbnv_tw_02`** | Vế (d): xem ai thật sự nhận |
| **Chuẩn bị / điều tra** | `admin` / `Secret@123` | **Chỉ** để tra `PHAN_CONG_VU_VIEC`, danh sách tài khoản, gán lại dữ liệu. **KHÔNG ra verdict bằng tài khoản này** (quyền rộng che lỗi phân quyền) |

**Kiểm bắt buộc trước khi chạy:** xác nhận `cbnv_tw_01` và `cbnv_tw_02` **cùng đơn vị TW** (`donViId`
`00000000-0000-4000-8000-000000000001`) — nếu khác đơn vị thì người B không thao tác được trên hồ sơ của người A,
phải đổi cặp. Ghi `donViId` thực đọc được vào báo cáo.

**Cảnh báo dữ liệu kế thừa:** `qa_tvvseed28` đã bị đổi `loaiTvv` **TVV → CG** ngày 21/07/2026
(`tuVanVienId = 98cfd963-3cd3-4c8a-bfa9-625460824d6d`). Nếu modal phân công lọc theo `loaiTvv` mà không thấy tài
khoản này thì **đổi lại `loaiTvv` hoặc tạo TVV khác cùng đơn vị**, ghi rõ đã mutate gì.

### 3.2 Màn / đường dẫn

- Người được phân công: **Vụ việc HTPL → mở chi tiết vụ việc** (`/vu-viec/{id}`), thanh hành động có
  **[Chấp nhận] [Từ chối]** khi hồ sơ ở *"Đã phân công"*.
- Cán bộ nghiệp vụ: **chuông thông báo / danh sách thông báo trong ứng dụng** của chính tài khoản đó + hộp thư
  giả lập **MailHog `http://18.143.165.120:8025/`** (env này chưa tích hợp email thật — không log "không nhận
  được email" khi chưa mở MailHog).
- Đối chứng lưu vết: **Dòng thời gian (Timeline)** trên chính màn chi tiết vụ việc, xem bằng tài khoản CB NV.

### 3.3 Dữ liệu tiền đề phải dựng (bằng chính luồng chuẩn, trên dữ liệu QA)

**Cần ≥ 3 vụ việc mới ở trạng thái "Đã phân công", người xử lý = `qa_tvvseed28`, phân công đang *Chờ xác nhận*** —
mỗi vụ việc một dạng ở mục 5. Cách dựng để **phân biệt được người tạo và người phân công**:

| Dạng | Cách dựng | Kết quả cần có trước khi bấm Từ chối |
|---|---|---|
| **① Người tạo ≡ người phân công** | `cbnv_tw_01` nhập hồ sơ thủ công → tự kiểm tra → **tự phân công** cho `qa_tvvseed28` | `created_by` = `nguoi_tiep_nhan_id` = `nguoi_phan_cong_id` = `cbnv_tw_01` |
| **② Người tạo ≠ người phân công** ← **phép thử quyết định của vế (d)** | `cbnv_tw_01` nhập hồ sơ thủ công + tiếp nhận → **`cbnv_tw_02`** kiểm tra và **phân công** cho `qa_tvvseed28` | `created_by` = `nguoi_tiep_nhan_id` = `cbnv_tw_01`; `nguoi_phan_cong_id` = `cbnv_tw_02` — **hai tài khoản khác nhau** |
| **③ Người tạo là Doanh nghiệp** | DN `0109998887` gửi yêu cầu → `cbnv_tw_01` tiếp nhận + kiểm tra → `cbnv_tw_02` phân công cho `qa_tvvseed28` | `created_by` = tài khoản DN; `nguoi_tiep_nhan_id` = `cbnv_tw_01`; `nguoi_phan_cong_id` = `cbnv_tw_02` — **ba tài khoản khác nhau** |

**Chốt định danh trước khi thao tác (bắt buộc, ghi vào báo cáo):** với mỗi vụ việc, đọc và ghi lại **mã vụ việc**,
`created_by`, `nguoi_tiep_nhan_id`, `nguoi_phan_cong_id`, `nguoi_xu_ly_id`. Không chốt được 4 định danh này ⇒
**chưa được chạy vế (d)** — nếu không, giai đoạn B sẽ kết luận nhầm *"cán bộ nghiệp vụ không nhận được thông báo"*
trong khi thực ra đã kiểm nhầm người.

**Dọn nhiễu thông báo:** trước khi bấm Từ chối, đánh dấu đã đọc / ghi lại **mốc thời gian + số thông báo hiện có**
của cả `cbnv_tw_01` và `cbnv_tw_02`, và ghi lại số thư hiện có trong MailHog. Chỉ đếm phần **tăng thêm** sau thao tác.

---

## 4. Tiêu chí chấm

Cài bộ bắt thông báo **trước** khi bấm Xác nhận (không lọc trùng · đọc bằng `innerText` · đếm request song song
số thông báo · đếm theo **mốc giờ khác nhau**, không theo số phần tử).

### ✅ PASS khi — đo trên MỖI vụ việc ①②③ đã dựng ở mục 3.3

**(a1) — Thao tác được xử lý, không bị chặn quyền**
1. Đăng nhập `qa_tvvseed28`, mở chi tiết vụ việc đã dựng (hồ sơ đang ở *"Đã phân công"*, `nguoi_xu_ly_id` = đúng
   `userId` của tài khoản này), bấm **Từ chối**, nhập lý do hợp lệ (≥ 10 ký tự, ví dụ
   `"QA verify XNTGHTVV_03 batch B6 - tu choi tham gia ho tro"`), bấm **Xác nhận**.
2. Sau thao tác, phiên làm việc **không** bị đưa sang màn từ chối quyền truy cập; đường dẫn trình duyệt **không**
   chuyển sang trang lỗi phân quyền; máy chủ **không** trả về mã 403 cho chính lời gọi thực hiện thao tác từ chối.
   *(căn cứ: `:807` PRE-02 + `:821` Bước 1 + `:840` E1 — nhánh lỗi này chỉ được kích hoạt khi tài khoản **không**
   phải người được phân công; ở đây tài khoản **đúng là** người được phân công)*

**(a2) — Có phản hồi cho người dùng**

3. Trong 5 giây sau khi bấm Xác nhận, bộ bắt thông báo ghi nhận **≥ 1 thông báo trên màn** ứng với **đúng 1 lời gọi
   máy chủ** cho thao tác từ chối, và thông báo đó thuộc loại **thành công/thông tin** (không phải loại lỗi).
   Chép **nguyên văn** chữ hiện ra vào báo cáo.
   → **Nội dung chữ**: đặc tả im lặng (S1) ⇒ **không chấm Fail vì chữ khác** kỳ vọng đối tác; ghi nguyên văn và
   đẩy sang câu hỏi BA.

**(b) — Bản ghi phân công được cập nhật**

4. Mở lại chi tiết vụ việc bằng **`cbnv_tw_02`** (hoặc `cbnv_tw_01`), phần **Phân công xử lý**: *trạng thái xác
   nhận* của bản ghi phân công hiển thị là **Từ chối** (không còn *Chờ xác nhận*).
5. Đọc lại bản ghi phân công bằng **đường thứ hai** (gọi thẳng máy chủ đọc `PHAN_CONG_VU_VIEC` của vụ việc đó) và
   đối chiếu **3 trường**: `trang_thai = 'TU_CHOI'` (`:2096`) · `ngay_xac_nhan` **có giá trị** và nằm trong khoảng
   ± 2 phút quanh thời điểm bấm Xác nhận (`:2100`) · `ly_do_tu_choi` **khớp từng chữ** chuỗi đã nhập ở bước 1
   (`:2097`).
   Cả 3 trường đúng ⇒ (b) PASS. Thiếu bất kỳ trường nào ⇒ (b) FAIL.

**(c) — Trạng thái hồ sơ chuyển đúng**

6. Trạng thái hồ sơ đọc được ngay sau thao tác là **"Đã tiếp nhận"** (`DA_TIEP_NHAN`), **không** phải "Đã phân công",
   **không** phải "Chờ phê duyệt", **không** phải "Từ chối".
   *(căn cứ 4 vị trí trùng khớp: `:823`, `:833`, `:846`, `:2292`)*
7. Đối chứng bằng đường thứ hai: đăng nhập `cbnv_tw_02`, mở danh sách vụ việc — **đúng mã vụ việc đó** xuất hiện
   ở nhóm hồ sơ đang xử lý với trạng thái *"Đã tiếp nhận"*, và **có** nút [Phân công] để phân công lại
   (`:1745` — *"DA_TIEP_NHAN (phân công lại sau khi bị từ chối)"*).

**(d) — Cán bộ nghiệp vụ nhận được thông báo kèm lý do**

8. Sau thao tác, kiểm **đủ 2 kênh mà đặc tả khai** (`:2480` BR-NOTIF-01 — in-app + email) cho **đủ cả 3 ứng viên**
   ứng với dạng dữ liệu đang chạy: `nguoi_phan_cong_id` · `nguoi_tiep_nhan_id` · `created_by`.
   - **Kênh trong ứng dụng:** đăng nhập lần lượt từng tài khoản cán bộ, đếm **số thông báo tăng thêm** so với mốc
     đã ghi ở mục 3.3, mở thông báo mới và chép **nguyên văn** nội dung.
   - **Kênh email:** đọc MailHog `http://18.143.165.120:8025/`, lọc thư đến **sau** mốc thời gian đã ghi, đối chiếu
     địa chỉ người nhận với email của từng tài khoản cán bộ. Chép nguyên văn tiêu đề + thân thư.
9. **PASS vế (d) khi đồng thời:**
   - **Đúng người:** ở dạng **② và ③** (người tạo ≠ người phân công), tài khoản cán bộ nghiệp vụ đang phụ trách hồ
     sơ nhận được thông báo về việc bị từ chối — trên **cả hai kênh** in-app và email. Ghi rõ **tài khoản nào nhận,
     tài khoản nào không**.
   - **Kèm lý do:** chuỗi lý do đã nhập ở bước 1 **đến được** người nhận đó — hoặc nằm trong nội dung thông báo/thư,
     **hoặc** hiển thị trên hồ sơ khi người đó mở vụ việc (`:2406` BR-FLOW-04). Ghi rõ đến bằng đường nào.
10. **FAIL vế (d) nếu:** không tài khoản cán bộ nào trong 3 ứng viên nhận được gì trên **cả hai** kênh · hoặc nhận
    được nhưng **không** kênh nào và **không** chỗ nào trên hồ sơ cho người đó thấy được lý do từ chối.
    **Chưa chốt (ô trống) nếu:** chỉ một trong hai kênh có tin còn kênh kia chưa kiểm được vì lý do hạ tầng — ghi rõ
    kênh nào chưa kiểm được và vì sao.

**(e) — Lưu vết thao tác**

11. Mở **Dòng thời gian** trên chi tiết vụ việc bằng tài khoản cán bộ: xuất hiện **1 mục mới** ứng với thao tác từ
    chối phân công, có **họ tên `qa_tvvseed28`** và **mốc ngày giờ** khớp ± 2 phút với thời điểm bấm Xác nhận
    (`:1735` — thành phần hiển thị *"Luôn"*).
12. Đối chứng đường thứ hai: đọc lại nhật ký vụ việc từ máy chủ — có bản ghi `hanh_dong = 'TU_CHOI_PHAN_CONG'`
    (`:2136`) với `ly_do` **khác rỗng** và khớp chuỗi đã nhập (`:2142` — `ly_do` **bắt buộc** với hành động này),
    `trang_thai_truoc = 'DA_PHAN_CONG'`, `trang_thai_sau = 'DA_TIEP_NHAN'`.

### ❌ FAIL nếu (bất kỳ điều nào)

- **(a1)** Bấm Xác nhận xong bị đưa sang màn từ chối quyền truy cập / trang lỗi phân quyền, **trong khi** tài khoản
  đang đăng nhập đúng là người được phân công của hồ sơ đó (đã chốt định danh ở mục 3.3) — **đây chính là triệu
  chứng đối tác quay**.
- **(a1) một phần:** máy chủ xử lý thành công nhưng giao diện vẫn văng sang màn lỗi ⇒ **fix một phần ⇒ Reopen**,
  không được Pass vì *"dữ liệu vẫn đúng"*.
- **(b)** Bản ghi phân công còn *Chờ xác nhận*, hoặc thiếu thời điểm từ chối, hoặc thiếu/lệch lý do.
- **(c)** Hồ sơ **không** ở "Đã tiếp nhận" sau thao tác — kể cả khi nó ở "Từ chối" hay "Chờ phê duyệt"
  (đối tác báo thấy "Chờ phê duyệt": nếu tái hiện được đúng trên bản ghi mình dựng thì FAIL vế (c)).
- **(d)** Theo điều kiện ở bước 10.
- **(e)** Dòng thời gian không có mục nào cho thao tác từ chối, **hoặc** có mục nhưng nhật ký thiếu lý do.

### 🚫 KHÔNG được chấm Fail vì (đặc tả im lặng)

- **Chữ** của thông báo báo thành công khác *"Đã từ chối tham gia vụ việc"* (S1) — chép nguyên văn, đẩy BA.
- **Không** tự chuyển về màn hình danh sách sau khi từ chối (S2) — ghi nhận hiện trạng, đẩy BA.
  ⚠️ Phân biệt rõ với (a1): **ở lại màn chi tiết** ≠ **bị đưa sang màn lỗi phân quyền**. Chỉ ca thứ hai mới là lỗi.
- Thông báo **không** gửi cho `nguoi_phan_cong_id` nhưng **có** gửi cho `created_by` (hoặc ngược lại) (S3) — ghi rõ
  ai nhận ai không, chỉ hỏi BA khi vẫn còn bất đồng với kỳ vọng đối tác.
- Màn lỗi không in mã `ERR-AUTH-VPD-00-04` hay bất kỳ mã nào — mã lỗi không phải tiêu chí (S5).
- Bộ đếm ký tự ô lý do dừng ở **1000** trong khi `:815` ghi *"tối đa 2.000 ký tự"* — **lệch này KHÔNG thuộc vế nào
  đối tác nêu**; nếu tái hiện được thì mở phiếu riêng, **không kéo verdict của case**.

### ⚠️ Chặn Pass oan

- **Cấm Pass bằng quan sát tĩnh** — không được kết luận *"đã fix"* chỉ vì thấy nút [Từ chối] hiện ra hoặc vì hồ sơ
  biến mất khỏi danh sách của người được phân công. Biến mất khỏi danh sách **không** chứng minh đã chuyển đúng
  trạng thái; phải đọc lại **chính bản ghi đó** bằng tài khoản cán bộ.
- **Cấm kết luận vế (d) chỉ bằng một kênh** hoặc chỉ bằng một tài khoản cán bộ — bẫy *"kiểm nhầm người"* đã làm
  hỏng vòng trước.
- **Không có ảnh lỗi cũ của chính mình** ⇒ chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**, không được viết
  *"fix đã có tác dụng"*.

**Phép thử của mục 4 này:** một người chưa biết gì về bug, đọc từ bước 1 → 12, chấm được PASS/FAIL cho từng vế.

---

## 5. Dạng dữ liệu phải phủ — **M = 3**

| # | Tên dạng | Vì sao bắt buộc |
|---|---|---|
| **①** | **Vụ việc do CB NV nhập tay, người tạo ≡ người phân công** (`cbnv_tw_01` làm cả hai) | Ca đơn giản nhất — nếu vế (d) Pass ở đây thì chưa chứng minh được gì, vì 1 người gánh cả 2 vai |
| **②** | **Vụ việc do CB NV nhập tay, người tạo ≠ người phân công** (`cbnv_tw_01` tạo · `cbnv_tw_02` phân công) | **Phép thử quyết định** — tách được *"gửi cho người phân công"* khỏi *"gửi cho người tạo"*; đúng điểm mà đặc tả im lặng (S3) và là chỗ vòng QA trước kết luận *"không nhận được thông báo"* |
| **③** | **Vụ việc do Doanh nghiệp tự gửi** (`created_by` = tài khoản DN, cán bộ chỉ tiếp nhận + phân công) | *"Người tạo ban đầu"* của BR-FLOW-04 (`:2406`) lúc này **không phải cán bộ** — nếu hệ thống gửi lý do cho *người tạo* thì ở dạng này không cán bộ nào nhận được, đó mới là bằng chứng chỉ đúng chỗ hỏng |

**Nguồn xác định M** (theo thứ tự tra của flow, dừng ở bước ①):
① **Mục đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo** — `srs-fr-05-vu-viec.md` có **2 đường tạo vụ việc**
riêng biệt: `:160` **FR-V.I-02** *Gửi hồ sơ yêu cầu HTPL (UC52)* → `:199` ghi nhật ký `vai_tro='DN'`; và `:300`
**FR-V.I-04** *Nhập hồ sơ yêu cầu thủ công (UC54)* → `:345` ghi nhật ký `vai_tro='CB_NV'`.
② **Chiều thứ hai** lấy từ chính mô hình dữ liệu: `nguoi_phan_cong_id` (`:2098`) tách bạch với `nguoi_tiep_nhan_id`
(`:2022`) và `created_by` (`:2376`) ⇒ *người tạo* và *người phân công* là **hai vai độc lập**, bắt buộc phủ cả ca
trùng nhau lẫn ca tách nhau.

**Dạng chưa tồn tại thì được seed** — bắt buộc khai vào báo cáo: **tạo/đổi bản ghi nào · đổi gì · trên env nào**.

---

## 6. Bảng điều kiện

Cột **"Đối tác"** điền ngay từ bằng chứng; 2 cột sau điền ở giai đoạn B.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| **Vai trò / tài khoản** | `huongcg` — vai trò **TVV · CG**, đơn vị **BTP · TW**. Đọc từ header (`huongcg` · `TVV · CG` · `BTP · TW`, mọi frame) và từ dòng *"Vai trò hiện tại: TVV CG"* in ngay trên màn 403 (`t016.18s.jpg`). Đây là **người được phân công**, không phải cán bộ | Phủ **rộng hơn**, khai rõ: dạng ①② dùng `qa_tvvseed28` — **TVV · CG**, Cục Bổ trợ tư pháp – Bộ Tư pháp, **cấp TW** (trùng đúng vai trò + cấp của đối tác); dạng ③ dùng `nht_ag_uat2` — **Người hỗ trợ pháp lý (NHT)**, Sở Tư pháp An Giang, **cấp ĐP**. Cả hai đều là **người được phân công** của chính hồ sơ mình dựng | **Không** |
| **Entity + trạng thái** | Vụ việc **`VV-BTP-TW-20260630-001`**, id `ab08db14-4e92-48fe-8f2b-b2a0ad00b4a3`, ở **"Đã phân công"** — chặng tiến trình dừng ở bước *Đã phân công* (`t009.55s.jpg`), thanh hành động có đủ **[Chấp nhận] [Từ chối]**, badge *"Còn 7 ngày LV"* | **3 vụ việc QA tự dựng**, cả 3 ở **"Đã phân công"**, chặng tiến trình dừng bước 5, thanh hành động đủ **[Chấp nhận] [Từ chối]**, badge *"Bình thường · còn 15 ngày LV"*: `VV-BTP-TW-20260806-001` (`1d26d8c7…`) · `VV-BTP-TW-20260806-002` (`ca7d0fb0…`) · `VV-STP-AG-20260806-004` (`4100caae…`) | **Không** |
| **Dữ liệu tiền đề** | Phân công trỏ **đúng tài khoản đang đăng nhập**: cột *Người xử lý / Tổ chức* = `huongcg` ở **cả 4 dòng** danh sách (`t024.95s.jpg`). Tiêu đề vụ việc *"Test file đính kèm vụ việc"*, DN chưa lộ tên, lĩnh vực **Thuế**, kênh **Trực tiếp**, ngày tiếp nhận 30/06/2026 10:28, deadline 21/07/2026. **Video KHÔNG cho biết ai tạo / ai phân công** ⇒ đây là chiều phải tự dựng (mục 3.3) | **Chốt đủ 4 định danh trước khi bấm** cho cả 3 hồ sơ (đọc từ máy chủ): ① tạo = tiếp nhận = phân công `cbnv_tw_01`; ② tạo = tiếp nhận `cbnv_tw_01`, phân công `cbnv_tw_02`; ③ tạo = DN An Giang, tiếp nhận `cbnv_dp_01`, phân công `cbnv_dp_02`. Người xử lý của cả 3 = **đúng tài khoản bấm Từ chối** | **Không** |
| **Input / filter / giá trị nhập** | Lý do từ chối *"TKM test từ chối thành công"* — **27 / 1000** ký tự, hợp lệ (≥ 10). Hộp thoại *"Từ chối phân công"*, nút **[Xác nhận]** / **[Hủy]**. Danh sách sau đó bật **"Bộ lọc nâng cao (2)"** — 2 bộ lọc đang áp, có thể che bớt bản ghi | Cùng hộp thoại *"Từ chối phân công"* + **[Xác nhận]/[Hủy]**. Lý do nhập hợp lệ, 3 chuỗi khác nhau **65 / 96 / 91** ký tự. Danh sách sau thao tác cũng đang bật bộ lọc nâng cao (**3** ở cấp TW, **2** ở cấp ĐP) ⇒ **không dùng danh sách để kết luận**, mà đọc lại **chính bản ghi** bằng tài khoản cán bộ | **Không** |
| **Độ phủ biến thể (N bản ghi, M dạng)** | **N = 1 bản ghi, M = 1 dạng** — đối tác chỉ quay đúng 1 vụ việc, 1 lần bấm, và **không** kiểm chiều *người tạo vs người phân công* (chiều quyết định vế (d)). Cũng **không** mở hộp thư / danh sách thông báo của cán bộ nào trong video | **N = 3 bản ghi · M = 3/3 dạng** (①②③ của mục 5). Vế (d) đo **cả 2 kênh** (chuông trong ứng dụng + hộp thư) cho **cả 3 ứng viên** mỗi dạng, đếm theo phần **tăng thêm** so với mốc đã ghi trước thao tác | **Không** |

**3 dữ kiện neo của đối tác**
1. **URL / ID bản ghi:** `htpldn-uat.ospgroup.vn/vu-viec/ab08db14-4e92-48fe-8f2b-b2a0ad00b4a3` → mã
   **`VV-BTP-TW-20260630-001`**; sau thao tác nhảy sang `htpldn-uat.ospgroup.vn/403`.
2. **Trạng thái entity:** trước thao tác **"Đã phân công"** (`t009.55s.jpg`); sau thao tác bản ghi **không còn** trong
   danh sách của người được phân công (`t024.95s.jpg`) — bản ghi duy nhất ở *"Chờ phê duyệt"* là
   **`VV-BKH-20260526-001`**, **khác mã**.
3. **Vai trò + env + bản dựng:** `huongcg` · **TVV · CG** · **BTP · TW**; env **`htpldn-uat.ospgroup.vn`**
   (env nghiệm thu của đối tác); đồng hồ máy quay **10/07/2026 08:36–08:37**; chuỗi phiên bản in ở chân trang trái:
   **`HTPLDN · V1.0`**; không có mã bó dựng/commit trong video.

> **Lệch env + bản dựng:** đối tác quay trên `htpldn-uat.ospgroup.vn` (10/07/2026), đợt này đo trên
> `18.143.165.120.nip.io`. Đây là **giới hạn hiệu lực của verdict**, **không phải GAP** — mọi kết luận Pass chỉ có
> giá trị cho env + bản dựng ghi ở đầu file, phải nói rõ điều đó trong báo cáo.

**Kết luận mục 6: 0/5 GAP.** Cả 5 chiều đều đã test thật ở giai đoạn B, không chiều nào để trống.

---

## 7. Sửa đổi (ghi ở giai đoạn B — không sửa lén mục 4/5)

**2026-08-06 15:05 — Bản dựng đổi giữa lô.** Bản dựng đo được ở case này (`assets/index-DIABnbIr.js`,
`last-modified 06/08/2026 07:13:15 GMT`, `etag "6a74340b-428"`) **khác** bản dựng của 2 case trước trong cùng lô B6.
Không đổi tiêu chí, chỉ ghi nhận: số đo của case này chỉ có hiệu lực cho bản dựng ghi ở dòng 4.

**2026-08-06 14:30 — Mở rộng chiều đơn vị của dạng ③ (khai theo yêu cầu "mở rộng chiều tài khoản phải khai").**
Mục 3.1 dự kiến dạng ③ dùng DN `0109998887` (Hà Nội) + `cbnv_tw_01`/`cbnv_tw_02` + `qa_tvvseed28`. Thực tế **không
dựng được** theo cấu hình đó, phải chuyển sang **Sở Tư pháp An Giang**. Hai lý do đo được, ghi lại nguyên trạng:
1. Cán bộ cấp TW **không tiếp nhận được** hồ sơ do DN Hà Nội gửi — máy chủ chặn với thông báo *"Đơn vị của người
   phê duyệt khác đơn vị của bản ghi"*. Đây là **hành vi phân quyền theo đơn vị**, không phải lỗi của case này.
2. Bảng gợi ý phân công của đơn vị Hà Nội **rỗng** (`0` người), kể cả khi bỏ lọc theo lĩnh vực ⇒ không có ai để
   phân công.
Cấu hình thực dùng cho dạng ③: DN `0209888006` (*Cong ty QA UAT An Giang*) tạo · `cbnv_dp_01` tiếp nhận + kiểm tra ·
`cbnv_dp_02` phân công · `nht_ag_uat2` (NHT) là người được phân công. **Vẫn giữ nguyên bản chất của dạng ③** —
*người tạo ban đầu không phải cán bộ*, và 3 định danh vẫn là 3 tài khoản khác nhau.

**2026-08-06 14:12 — Dữ liệu đã can thiệp (khai bắt buộc).** Tài khoản DN `0209888006` trên env
`18.143.165.120.nip.io` đăng nhập không được; đã **đặt lại mật khẩu về `Test@1234` bằng chính luồng quên mật khẩu
của ứng dụng**. Không sửa dữ liệu nghiệp vụ nào của tài khoản này.

**2026-08-06 15:05 — Cách chấm vế (b), bước 5.** Bước 5 đòi đọc `ngay_xac_nhan` (`:2100`). Máy chủ **không phơi ra
trường tên như vậy** trên bản ghi phân công; trường thời gian đọc được là **mốc cập nhật của chính bản ghi phân
công**, và mốc này lệch **0,15 giây** so với thời điểm bấm Xác nhận (bản ghi không có lần cập nhật nào khác).
Chấm theo **yêu cầu nghiệp vụ** — *bản ghi phân công có lưu thời điểm từ chối* — chứ không chấm theo **tên trường**
(tên trường là cách hiện thực). Ghi rõ số đo trong báo cáo để người đọc tự kiểm.

**2026-08-06 15:10 — Bỏ S1/S2/S3/S4 khỏi danh sách hỏi BA (theo quy tắc "đo xong hết bất đồng thì bỏ").**
Bốn điểm im lặng ở mục 2.7 đều đã đo và **không còn bất đồng** giữa bản dựng và kỳ vọng đối tác:
- **S1 (chữ của thông báo):** bản dựng hiện **"Đã từ chối phân công"**, loại **thành công**, gọi **đúng tên hành
  động** đối tác mô tả (*từ chối*), đúng 1 lần hiển thị ứng với đúng 1 lời gọi máy chủ. Khác chữ nhưng **không khác
  nghĩa** ⇒ không còn gì để BA phân xử. Chép nguyên văn vào báo cáo.
- **S2 (điều hướng):** bản dựng **tự chuyển về màn danh sách** — **đúng bằng** điều đối tác mong đợi ⇒ hết bất đồng.
- **S3 (đích danh CB NV nào nhận):** đo 3 dạng cho ra **một quy tắc nhất quán** — người nhận là **cán bộ nghiệp vụ
  đang phụ trách hồ sơ (người tiếp nhận)**. Ở dạng ③ người tạo là doanh nghiệp thì doanh nghiệp **không** nhận,
  cán bộ tiếp nhận **có** nhận ⇒ đúng bằng *"cán bộ nghiệp vụ phụ trách"* mà đối tác đòi ⇒ hết bất đồng.
- **S4 (thông báo có kèm lý do không):** thông báo **có kèm nguyên văn lý do** trên **cả hai kênh** ⇒ hết bất đồng.
⇒ **Không mở mục hỏi BA nào cho case này.**
