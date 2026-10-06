# Tiêu chí chấm — CNDSMLTVV_01

```
Mã case: CNDSMLTVV_01 (tab `bug`, dòng 37 · Tuần 2 · STT 46)
Thời điểm viết: 2026-08-06 17:50   (viết TRƯỚC khi mở màn đang tranh chấp)
Môi trường verify: https://18.143.165.120.nip.io   (env NỘI BỘ, không phải env nghiệm thu của đối tác)
Bản dựng: HTPLDN · V1.0.8 · bó mã FE `assets/index-DIABnbIr.js` (+ `assets/index-DVlgOkLg.css`)
          · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · etag `W/"6a74340b-428"`
          (số đo của 4 case trước cùng lô; ĐỌC LẠI sau khi tải lại trang ở đầu giai đoạn B —
           nếu lệch thì ghi bổ sung ở mục 7. KHÁC bản dựng `HTPLDN · V1.0` trong ảnh của đối tác)
```

> **Hồ sơ QA nội bộ đã đọc trước khi viết file này (khai theo flow 04 §Giai đoạn A):**
> `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/bug-report.md` (4 entry đã có của lô B7) ·
> `output/UAT_doi-tac/input/input.md` (danh sách tài khoản) ·
> `output/UAT_doi-tac/batch-B7-tuvan-mangluoi-2026-08-06/tieuchi/QLTVV_02.md` (case cùng màn SCR-IV-01,
> đo 06/08 — **chỉ dùng để biết màn đó có gì**, KHÔNG lấy số đo cũ làm ngưỡng).
> Ngưỡng ở mục 4 dưới đây suy từ **đặc tả `srs-v3.5`**, không lấy từ số vừa nhìn thấy trên màn.

---

## 1. Đối tác phản ánh

**Case gộp 2 vế** (ô *Kết quả mong đợi* của phiếu có 2 gạch đầu dòng ⇒ rẽ nhánh TỪNG vế theo flow 04 §Ca biên):

- **Vế (1) — giao diện nhập.** *"Hệ thống hiển thị cửa sổ nhập mô tả công khai (bắt buộc) áp cho các tư vấn
  viên đã chọn và xác nhận `Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?`"*
  Ô *Kết quả thực tế*: *"Hệ thống **không mở cửa sổ nhập** mà hiển thị thông báo `Mô tả công khai là bắt buộc
  trước khi đẩy lên Cổng pháp luật quốc gia`"*.
- **Vế (2) — kết quả nghiệp vụ.** *"Lưu mô tả công khai, đặt cờ công khai, chuyển trạng thái công khai,
  ghi thời điểm."* — 4 kết cục phải kiểm riêng, **sau khi tải lại trang**, không dừng ở thông báo thành công.

Ô *Các bước thực hiện* của phiếu: 1. Chọn menu "Mạng lướt tư vấn viên" → "Tư vấn viên/Chuyên gia";
2. **Tích chọn các ứng viên hợp lệ**; 3. Nhấn **"Công khai hàng loạt"** và Xác nhận.
Ô *Điều kiện*: 1. Đăng nhập tài khoản; 2. **Hồ sơ đang ở trạng thái "Đang hoạt động" và CHƯA được công khai**.
Ô *Tác nhân*: **Cán bộ nghiệp vụ TW, BN, ĐP**.

**Bằng chứng đã mở XEM full-res:** [`partner-evidence/CNDSMLTVV_01.jpg`](../partner-evidence/CNDSMLTVV_01.jpg)
(1 ảnh tĩnh 1906×1031, không phải video). Đọc được trên ảnh:

| Vị trí trên ảnh | Nội dung đọc được |
|---|---|
| Thanh địa chỉ | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach` |
| Thanh điều hướng | `Trang chủ / Mạng lưới Tư v…` (phần sau bị thông báo che) |
| Thông báo (đỏ, giữa trên, có dấu ✕ tròn) | **"Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia"** — nổi một mình, **không kèm cửa sổ nhập nào phía sau** |
| Hàng tab | `Đang hoạt động` (**đang chọn**) · Tạm dừng · Mới đăng ký `26` · Chờ thẩm định · Yêu cầu bổ sung `3` · Đang thẩm định · Chờ phê duyệt · Chờ kích hoạt tài khoản · Từ chối · `…` |
| Thanh công cụ (phần không bị che) | `Xóa bộ lọc` · `Tìm kiếm`. **Không nhìn thấy nút "Công khai hàng loạt"** trong vùng hiện ra — vùng phía trên bị thông báo che |
| Tiêu đề bảng | (ô chọn) · Ảnh · Mã TVV · Họ tên · Loại · Lĩnh vực · Tổ chức · Điểm ĐG · Trạng thái · `Ngày công nh…` |
| **Ô chọn** | Ô chọn ở tiêu đề **RỖNG** (không phải dấu gạch "chọn một phần") và **5/5 hàng nhìn thấy đều rỗng** ⇒ tại khoảnh khắc chụp **0 dòng đang được chọn**. Thân bảng có cuộn dọc riêng nên 5 hàng phía trên không nhìn thấy |
| 5 hàng nhìn thấy | `TVV-BTP-TW-0030` huongcg · Chuyên gia · Đoàn Luật sư Hà Nội · `—/5` · **Đang hoạt động** · 08/05/2026 — `TW-0029` hương tvv1 · Tư vấn viên · 09/05/2026 — `TW-0006` Hồ Văn Mười Tám · 06/05/2026 — `TW-0004` Trương Văn Mười Sáu · 06/05/2026 — `TW-0002` Đinh Văn Mười Bốn · 06/05/2026. **Cả 5 đều "Đang hoạt động"** |
| Chân bảng | `1-10 / 10 mục` · trang `1` · `20 / trang` |
| Góc phải trên | `BTP · TW` · chuông `99+` · `Cán bộ NV Trung ương` · huy hiệu **`CB_NV_TW`** |
| Sidebar (chân logo) | `HTPLDN · V1.0`; menu đang ở `Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia` |
| Đồng hồ máy | `05:41 PM · 2026-07-25` |

⇒ **Màn tranh chấp xác định từ chính ảnh (không chỉ từ mô tả):** `SCR-IV-01` — *Danh sách Tư vấn viên*,
đường dẫn `/chuyen-gia-tvv/danh-sach`, **tab "Đang hoạt động"**, thao tác **hàng loạt "Công khai"**
(`FR-IV-08`). Khớp mã case `CNDSMLTVV` = *Cập nhật danh sách mạng lưới tư vấn viên* ⇒ **bằng chứng đúng case này**.

**3 dữ kiện neo của đối tác:** màn `/chuyen-gia-tvv/danh-sach` tab *Đang hoạt động*, 10 bản ghi, 0 dòng đang
chọn tại khoảnh khắc chụp · vai trò **CB_NV_TW**, đơn vị hiện `BTP · TW` · env **`htpldn-uat.ospgroup.vn`**,
bản dựng **`HTPLDN · V1.0`**, 25/07/2026 17:41.

---

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` và
`…/srs-v3.5.md` (đã **mở file đọc từng dòng**, không lấy số dòng từ trí nhớ).

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-04:641` | `### FR-IV-08: Công khai mạng lưới TVV (UC46)` |
| `:643` | `**Màn hình:** SCR-IV-01 (thao tác hàng loạt "Công khai") + SCR-IV-03 (nút header "Công khai lên Cổng pháp luật quốc gia")` |
| `:645` | `**Mô tả:** Công khai / gỡ công khai TVV … theo mô hình KÉO (PULL): phần mềm chỉ đặt cờ cong_khai + chuyển trạng thái CONG_KHAI / HUY_CONG_KHAI; Cổng PLQG **tự kéo** dữ liệu công khai định kỳ qua API outbound … Phần mềm KHÔNG đẩy trực tiếp, KHÔNG gọi API ra Cổng.` |
| `:647` | `**Tác nhân:** CB NV (có quyền "Công khai mạng lưới tư vấn viên")` |
| `:656` | §Inputs #4 — `mo_ta_cong_khai` · text (long) · **Bắt buộc = Y (nếu CONG_KHAI)** · *"Max 5000 ký tự — mô tả hiển thị trên Cổng pháp luật quốc gia. **Bắt buộc trước khi công khai** để tránh TVV công khai không có mô tả"* · Nguồn: **"CB Nghiệp vụ nhập trong modal MD-CONG-KHAI"** ← **đúng điểm tranh chấp vế (1)** |
| `:657` | §Inputs #5 — `file_dinh_kem_cong_khai` · **Bắt buộc = N** (tùy chọn) · *"CB Nghiệp vụ upload (tùy chọn) trong modal MD-CONG-KHAI"* |
| `:663` | §Processing bước 1 — kiểm đối tượng: TVV ở trạng thái `CHO_KICH_HOAT` **HOẶC** `HOAT_DONG` |
| `:664` | §Processing bước 2 — *"Công khai: **lưu mo_ta_cong_khai** + file_dinh_kem_cong_khai (nếu có), **đặt cong_khai = 1**, **chuyển trạng thái CONG_KHAI**, **auto fill thoi_gian_dang_tai**"* ← **đúng 4 kết cục của vế (2)** |
| `:666` | §Processing bước 4 — **"Hỗ trợ thao tác hàng loạt"** |
| `:667` | §Processing bước 5 — ghi nhật ký thao tác (BR-DATA-05) |
| `:673`–`:675` | §Outputs — `tvv_id` · `trang_thai_moi` (CONG_KHAI/HUY_CONG_KHAI) · `thoi_gian_dang_tai` |
| `:681` | §Error Handling **E1** `ERR-CK-01` — TVV không ở `CHO_KICH_HOAT`/`HOAT_DONG` → *"Chỉ tư vấn viên đã được công nhận (Chờ kích hoạt hoặc Đang hoạt động) hoặc tổ chức đang hoạt động mới được công khai"* |
| `:682` | §Error Handling **E2** `ERR-CK-02` — **"Thiếu mô tả công khai khi CONG_KHAI"** → *"Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia"* ← **câu đối tác gặp, nhưng đặc tả xếp nó vào ca THIẾU MÔ TẢ, không phải ca vừa bấm nút** |
| `:685`–`:686` | §Postconditions — TVV được đánh dấu `cong_khai = 1/0` + trạng thái CONG_KHAI/HUY_CONG_KHAI; Cổng PLQG hiển thị/ẩn **sau lần kéo định kỳ kế tiếp** |
| `:689` | AC1 — `**Given** CB NV chọn TVV đang hoạt động **When** nhấn "Công khai" **Then** đặt cong_khai = 1 + trạng thái CONG_KHAI; Cổng PLQG tự kéo…` |
| `:1406` | **MD-CONG-KHAI** — tiêu đề *"Công khai lên Cổng pháp luật quốc gia"*; **"Form nhập trước khi xác nhận"**: (a) **Mô tả công khai** — text dài, **bắt buộc**, max 5000 ký tự; (b) File đính kèm — **tùy chọn**; (c) Cảnh báo *"Sau khi công khai, thông tin **{tên}** sẽ hiển thị toàn quốc trên Cổng pháp luật quốc gia. Bạn có thể hủy công khai bất kỳ lúc nào — mô tả + file vẫn được giữ lại để tái công khai sau."*; nút chính **"Công khai"** |
| `:1412` | **MD-PHE-DUYET-HANG-LOAT** — *"Bạn đang phê duyệt **{N}** hồ sơ…"*, nút `Phê duyệt {N} hồ sơ` ← **chỗ DUY NHẤT đặc tả dùng tham số {N}**, và là hộp thoại của **phê duyệt** hàng loạt, KHÔNG phải công khai |
| `:1420` | SCR-IV-01 §Quyền truy cập — *"Cán bộ Nghiệp vụ: thêm/sửa/xóa, xuất Excel, **công khai** (TVV thuộc đơn vị)"* |
| `:1445` | SCR-IV-01 thành phần **17** — *"Ô chọn · checkbox · **Chọn nhiều dòng cho thao tác hàng loạt**"* |
| `:1464` | §Quy tắc tương tác — **"Công khai hàng loạt (tab 'Đang hoạt động'): chọn nhiều dòng → nút 'Công khai lên Cổng pháp luật quốc gia' → **mở MD-CONG-KHAI** → đặt `cong_khai = 1` + chuyển trạng thái Công khai cho các dòng đã chọn. **Chỉ áp dụng cho dòng có trạng thái Đang hoạt động.** Cổng pháp luật quốc gia tự kéo (PULL)…; phần mềm KHÔNG gọi API ra Cổng."** ← **xương sống của case** |
| `:1465` | §Quy tắc tương tác — *"Hủy công khai hàng loạt (tab 'Đang hoạt động'): chọn dòng đã công khai → nút 'Hủy công khai' → MD-HUY-CONG-KHAI…"* (đường hoàn nguyên) |
| `:1557` | SCR-IV-03 thành phần 10 — nút **Công khai** ở màn chi tiết: *"Click → MD-CONG-KHAI (form nhập mô tả + file đính kèm) → lưu mo_ta_cong_khai … → đặt cong_khai = 1 + chuyển trạng thái Công khai, **ghi thời gian đăng tải**"*; điều kiện hiển thị: *"trạng thái = Chờ kích hoạt tài khoản HOẶC Đang hoạt động … **AND chưa công khai**"* |
| `:1564` | SCR-IV-03 tab "Hồ sơ" nhóm **(f) Thông tin công khai** — *"**chỉ hiển thị khi cong_khai=1**: mô tả công khai + danh sách file đính kèm công khai + **ngày đăng tải**"* ← **đường đọc lại 4 kết cục của vế (2) bằng chính giao diện** |
| `:2046`–`:2049` | Bảng `HO_SO_TU_VAN_VIEN` — `cong_khai` boolean mặc định 0 · `thoi_gian_dang_tai` datetime *"Auto fill khi cong_khai=1 … Clear khi cong_khai=0"* · `mo_ta_cong_khai` text_long |
| `srs-v3.5.md:5685` | **BR-PUBLIC-01** — *"Entity có quy trình (SM): chỉ bản ghi ở trạng thái cuối (… /Đang hoạt động) mới được set cong_khai = 1"* |
| `srs-v3.5.md:5697` | **BR-PUBLIC-03** — *"Auto fill = thời điểm cuối cùng set cong_khai = 1. Không cho phép sửa tay"* |
| `srs-v3.5.md:6722` | Phụ lục **E.I** — *"**Mô hình KÉO (C-INT-01):** công khai = phần mềm đặt cờ `cong_khai` + trạng thái CONG_KHAI; Cổng PLQG tự kéo (PULL) định kỳ… Phần mềm **KHÔNG gọi API đẩy/gỡ trực tiếp**."* |
| `srs-v3.5.md:6728` | E.I.1 mẫu thông báo **"Công khai thành công"** — Toast success (tự tắt 4s): *"Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp luật Quốc gia."* |
| `srs-v3.5.md:6729` | E.I.1 mẫu **"Hủy công khai thành công"** — *"Đã hủy công khai {ten_doi_tuong} '{ma_hoac_ten}' khỏi Cổng Pháp luật Quốc gia."* |

**Rẽ nhánh TỪNG VẾ (flow 04 §Đối chiếu đặc tả):**

- **Vế (1) — giao diện nhập:** đặc tả **NÓI RÕ** và **KHỚP** kỳ vọng đối tác. `:1464` bắt buộc luồng
  *chọn dòng → nút → **mở MD-CONG-KHAI***; `:656` ghi đích danh nguồn của `mo_ta_cong_khai` là *"CB Nghiệp vụ
  **nhập trong modal MD-CONG-KHAI**"*; `:1406` mô tả MD-CONG-KHAI là **"Form nhập trước khi xác nhận"**.
  ⇒ **Không phải nhánh cần BA. Đo bình thường theo mục 4.**
- **Vế (2) — 4 kết cục nghiệp vụ:** đặc tả **NÓI RÕ** ở `:664`, `:685`, `:1557`, `:2046`–`:2049`.
  ⇒ **Đo bình thường.**
- **Phần đối tác nêu mà đặc tả IM LẶNG (KHÔNG chấm lỗi, chỉ ghi nhận hiện trạng):** **câu chữ chính xác
  `"Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"`**. Đặc tả chỉ dùng tham số `{N}` ở
  **MD-PHE-DUYET-HANG-LOAT** (`:1412`); cảnh báo của MD-CONG-KHAI (`:1406`) dùng `{tên}`, viết cho ca **một**
  đối tượng và không có bản riêng cho hàng loạt. ⇒ Yêu cầu ĐO ĐƯỢC rút ra là: **hộp thoại phải cho biết thao
  tác đang áp cho ĐÚNG các dòng đã chọn (số lượng hoặc danh sách tên/mã)**; **cấm** chấm Fail vì câu chữ không
  trùng từng chữ với ô *Kết quả mong đợi*.

---

## 3. Precondition

- **Tài khoản:** `cbnv_tw_02` / `Test@1234` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**,
  đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*. **Trùng khít vai trò + cấp đọc được trên ảnh của đối tác**
  (`Cán bộ NV Trung ương`, huy hiệu `CB_NV_TW`, `BTP · TW`). Đặc tả cho phép đúng vai trò này công khai
  (`:647`, `:1420`). Dự phòng theo Rule 7 nếu đăng nhập fail: `cbnv_tw_03` (cùng vai trò, cùng cấp).
- **Màn:** `https://18.143.165.120.nip.io/chuyen-gia-tvv/danh-sach` → tab **"Đang hoạt động"**.
- **Dữ liệu tiền đề (theo đúng ô *Điều kiện* của phiếu):** ≥ **3 hồ sơ TVV/CG** thuộc đơn vị của tài khoản đo,
  **trạng thái "Đang hoạt động"** và **CHƯA công khai** (`cong_khai = 0`). Đây là tiền đề **tạo được** ⇒
  theo flow 04 §Chuẩn bị điểm 3, **CẤM mọi verdict nếu không dựng**.
  - Env đã có sẵn ≥ 6 hồ sơ ở tab "Đang hoạt động" (số đo case QLTVV_02 cùng lô, 06/08). Nếu hồ sơ nào đã
    công khai → dùng chính luồng chuẩn **"Hủy công khai"** (`:1465`) để đưa về *chưa công khai*, đo xong
    **hoàn nguyên**.
  - Thiếu hồ sơ *Đang hoạt động* → tạo mới qua luồng chuẩn hoặc dùng bản ghi QA đã có
    (`TVV-BTP-TW-0038` do lô này tạo, đang *Mới đăng ký* — **không** dùng cho nhánh hợp lệ, chỉ dùng cho
    nhánh ngược "hồ sơ không hợp lệ").
- **Nhánh ngược cần có:** ≥ 1 hồ sơ **đã công khai** (dựng bằng chính lượt đo) và ≥ 1 hồ sơ **không ở
  "Đang hoạt động"** (tab khác) để kiểm hành vi `ERR-CK-01` / điều kiện hiển thị `:1464`.
- **Hoàn nguyên bắt buộc:** mọi hồ sơ bị đổi cờ công khai trong lúc đo phải **trả về đúng trạng thái ban đầu**
  bằng luồng "Hủy công khai" (`:1465`), và ghi rõ trong bug entry + bảng seed.

---

## 4. Tiêu chí chấm

### Vế (1) — giao diện nhập mô tả công khai

**✅ PASS vế (1) khi — thoả ĐỦ 4 điều, ở MỌI lượt bấm (đủ M dạng):**

1. Bấm nút công khai hàng loạt (sau khi đã tích chọn ≥ 1 dòng hợp lệ) → **hệ thống MỞ một lớp nhập** có
   **ô nhập mô tả công khai** — đúng `:1464` (*"→ mở MD-CONG-KHAI"*) và `:656` (*"CB Nghiệp vụ nhập trong
   modal MD-CONG-KHAI"*). **Không** bắn thẳng thông báo chặn thay cho lớp nhập.
2. Lớp nhập đó cho biết thao tác **áp cho đúng các dòng đã chọn** — bằng số lượng, hoặc danh sách tên/mã của
   đúng những dòng đã tích. Chọn 1 dòng thì phải phản ánh 1; chọn nhiều dòng thì phải phản ánh đúng số đó.
3. Có **đường xác nhận** (nút chính) để hoàn tất thao tác, đúng `:1406` (*"Form nhập trước khi xác nhận"*,
   nút chính *"Công khai"*).
4. **Nhánh ngược đúng chỗ:** để TRỐNG ô mô tả rồi xác nhận → hệ thống **từ chối** và nói rõ mô tả công khai là
   bắt buộc (`:682` `ERR-CK-02`); dữ liệu **không** bị công khai. Đây là chỗ ĐÚNG của câu *"Mô tả công khai là
   bắt buộc…"*.

**❌ FAIL vế (1) nếu — chỉ cần 1 điều:**

- Bấm nút mà **không** có lớp nhập nào mở ra, hoặc lớp nhập mở ra nhưng **không có ô nhập mô tả công khai**.
- **Bắn thông báo chặn THAY CHO lớp nhập** (đúng triệu chứng đối tác) — kể cả khi thông báo đó đúng chữ `:682`.
- Lớp nhập báo **sai số lượng / sai tập bản ghi** so với các dòng đã tích (vd chọn 3 mà báo 1).
- Bỏ trống mô tả mà hệ thống **vẫn công khai** (mất ràng buộc bắt buộc của `:656`).

### Vế (2) — 4 kết cục nghiệp vụ

**✅ PASS vế (2) khi — sau khi xác nhận với mô tả hợp lệ, THOẢ ĐỦ 4 kết cục, và phải đọc lại SAU KHI TẢI LẠI TRANG:**

1. **Mô tả công khai được lưu** — mở lại đúng bản ghi, đọc thấy **đúng nguyên văn** chuỗi vừa nhập
   (`:664` *"lưu mo_ta_cong_khai"*; đọc ở nhóm (f) *Thông tin công khai* theo `:1564`).
2. **Cờ công khai được đặt** — bản ghi thể hiện đang ở trạng thái đã công khai (`cong_khai = 1`, `:664`,
   `:2046`). Dấu hiệu đo được trên giao diện: nhóm (f) *Thông tin công khai* **hiện ra** (chỉ hiện khi
   `cong_khai=1`, `:1564`) và nút ở màn chi tiết đổi sang **Hủy công khai** (`:1557`, `:1558`).
3. **Trạng thái công khai chuyển** — bản ghi mang trạng thái **CONG_KHAI** / nhãn "Đã công khai" (`:664`,
   `:685`).
4. **Thời điểm được ghi** — có **ngày đăng tải** với giá trị bám đúng thời điểm bấm (`:664` *auto fill
   thoi_gian_dang_tai*, `:1564` *"ngày đăng tải"*, BR-PUBLIC-03 `srs-v3.5.md:5697`).
5. **Áp cho ĐỦ các dòng đã chọn** — chọn N dòng thì đủ N bản ghi đạt cả 4 kết cục trên, không sót dòng nào.
6. **Đường đo thứ hai khớp** — đọc lại bản ghi qua máy chủ cho ra đúng những gì màn hình đang hiện.
   Hai đường mâu thuẫn ⇒ **chưa được chốt**.

**❌ FAIL vế (2) nếu — chỉ cần 1 điều:** thiếu bất kỳ kết cục nào trong 4 kết cục · báo thành công nhưng tải
lại trang thì bản ghi **không** đổi (fix bề mặt) · chọn N dòng mà chỉ áp cho một phần · mô tả lưu sai/rỗng ·
ngày đăng tải trống hoặc lệch hẳn thời điểm bấm.

### Bar về thông báo (áp cho cả 2 vế)

- Cài `tools/toast-capture.js` **TRƯỚC khi bấm**, tự kiểm `soObserverDangSong = 1` mới tin số liệu.
- **Đếm thông báo theo MỐC GIỜ KHÁC NHAU**, không đếm số phần tử (1 thông báo sinh 2 phần tử cùng mốc giờ).
- Đọc bằng `innerText`, **CẤM lọc trùng**. **Đếm request ghi song song số thông báo.**
- Đọc **chữ**, không chỉ đếm: so nguyên văn với ① `:682` (ca thiếu mô tả) ② `srs-v3.5.md:6728` (mẫu công khai
  thành công) ③ ô *Kết quả mong đợi* của đối tác.

### KHÔNG được chấm Fail vì (đặc tả im lặng / ngoài vế đối tác nêu)

- **Không thấy phần mềm gọi API sang Cổng PLQG** — mô hình **KÉO** (`:645`, `srs-v3.5.md:6722`): phần mềm
  **chỉ đặt cờ**, Cổng tự kéo. Chấm Fail vì "không thấy đẩy sang Cổng" là **sai đặc tả**.
- **Câu chữ chính xác của hộp thoại/nút** (`"Công khai {N} tư vấn viên đã chọn…?"`) — đặc tả không có mẫu này
  cho luồng công khai hàng loạt (xem §2, phần IM LẶNG). Chỉ đo *có phản ánh đúng tập dòng đã chọn hay không*.
- **Câu chữ chính xác của thông báo thành công** — mẫu `srs-v3.5.md:6728` là *mẫu chuẩn*, chỉ ghi nhận sai lệch
  ở mức nhận xét, không kéo verdict của case (đối tác không nêu vế này).
- **Nhãn nút / kiểu khung** (Drawer hay Modal, "Đồng ý" hay "Công khai") — đặc tả `:1406` chỉ chốt *có form
  nhập trước khi xác nhận*, không chốt loại khung.
- **Hệ thống từ chối ĐÚNG** khi dòng được chọn không hợp lệ (`ERR-CK-01` `:681`: không ở *Chờ kích hoạt* /
  *Đang hoạt động*), hoặc khi **bỏ trống mô tả** (`ERR-CK-02` `:682`) — đó là hành vi **đúng**.
- **Cổng PLQG chưa hiển thị TVV ngay** — `:686` nói rõ *"sau lần kéo định kỳ kế tiếp"*.

---

## 5. Dạng dữ liệu phải phủ

**Nguồn xác định M:** ① ô *Các bước thực hiện* của phiếu (*"Tích chọn **các** ứng viên hợp lệ"* — số nhiều
⇒ phải phủ cả 1 dòng và nhiều dòng, vì câu xác nhận có tham số `{N}`); ② `:1464` (*"chọn **nhiều** dòng"*)
+ `:1445` (ô chọn hàng loạt); ③ bộ điều kiện lỗi `:681`–`:682` (2 nhánh ngược).

**M = 5 dạng thao tác** (M1–M2 là **tối thiểu bắt buộc**, M3–M5 là nhánh ngược đặc tả nêu đích danh):

| # | Dạng | Căn cứ |
|---|---|---|
| M1 | Tích chọn **1** hồ sơ hợp lệ → bấm công khai hàng loạt → nhập mô tả → xác nhận | ô *Các bước*; `:1464` |
| M2 | Tích chọn **nhiều** hồ sơ hợp lệ (≥ 2) → kiểm lớp nhập phản ánh **đúng số N** → nhập mô tả → xác nhận | ô *Kết quả mong đợi* (`{N}`); `:1464` *"cho các dòng đã chọn"* |
| M3 | **Bỏ trống mô tả** rồi xác nhận → phải bị chặn, không bản ghi nào bị công khai | `:656` (*bắt buộc*), `:682` `ERR-CK-02` |
| M4 | Chọn hồ sơ **đã công khai** → quan sát hệ thống xử lý thế nào | `:1557` (*AND chưa công khai*), `:1465` |
| M5 | Chọn hồ sơ **không ở "Đang hoạt động"** (tab khác) → quan sát | `:681` `ERR-CK-01`, `:1464` (*chỉ áp dụng cho dòng Đang hoạt động*) |

**N = ≥ 3 hồ sơ TVV/CG** *Đang hoạt động* + *chưa công khai* thuộc đơn vị của tài khoản đo
(1 dùng cho M1, ≥ 2 dùng cho M2), cộng các bản ghi mượn cho M4/M5.

**Mọi lượt hợp lệ đều phải:** tải lại trang → mở lại bản ghi → đọc lại **đủ 4 kết cục** của vế (2).
**CẤM chấm bằng quan sát tĩnh** ("thấy có ô nhập mô tả rồi") và **CẤM dừng ở thông báo thành công**.

---

## 6. Bảng điều kiện — đóng GAP

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** (*Cán bộ NV Trung ương*), đơn vị hiển thị `BTP · TW`; ô *Tác nhân* của phiếu ghi *Cán bộ nghiệp vụ TW, BN, ĐP* | `cbnv_tw_02` — **CB_NV_TW**, cấp **TW**, đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*, giao diện hiện đúng `BTP · TW`. **Trùng khít vai trò + cấp + đơn vị, KHÔNG nới chiều nào.** Đăng nhập 1 lượt, không phải dùng tài khoản dự phòng | **Không** |
| Entity + trạng thái | Hồ sơ TVV/CG trên màn danh sách, tab *Đang hoạt động*, 10 bản ghi; ô *Điều kiện* đòi **Đang hoạt động + chưa công khai** | Cùng entity, cùng màn `/chuyen-gia-tvv/danh-sach`, cùng tab *Đang hoạt động*. Trước khi bấm: `CG-QLND38-UAT` · `TVV-STP-AG-0001` · `TVV-SEED-0001` đều **Đang hoạt động + Chưa công khai**; `TVV-BTP-TW-0002` · `DDD-TVV-022` · `DDD-TVV-021` **đã công khai** (mượn cho nhánh ngược) | **Không** |
| Dữ liệu tiền đề | 10 bản ghi ở tab *Đang hoạt động*; 0 dòng đang chọn tại khoảnh khắc chụp | Tab có **6** bản ghi thay vì 10, trong đó **N = 3 hồ sơ đúng tiền đề** (đạt ngưỡng ≥3 của mục 3) + 2 hồ sơ đã công khai + 2 tab khác cho M5. Thao tác áp trên **tập dòng đã tích**, không phụ thuộc tổng số dòng của tab, và đã phủ cả 1 dòng lẫn 2 dòng ⇒ chênh lệch 10 vs 6 không đổi được kết quả. Mọi hồ sơ bị đổi cờ công khai **đã hoàn nguyên**, đọc lại sau khi tải lại trang | **Không** |
| Input / filter / giá trị nhập | Không nói rõ đã tích mấy dòng (ô chọn trên ảnh đều rỗng); không nói mô tả đã nhập gì | Phủ **cả hai khả năng**: tích **1** dòng (M1, M2b, M2c, M4) và tích **2** dòng (M2 ×2 lượt); phủ **cả hai khả năng** của ô mô tả: **có nhập** (chuỗi `QA UAT B7 CNDSMLTVV_01 - …` mỗi lượt một chuỗi riêng) và **bỏ trống** (M3). Bộ lọc để nguyên mặc định của tab | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | 1 lượt bấm, tập dòng đã chọn không đọc được từ ảnh | **N = 4 hồ sơ** thao tác thật (3 hợp lệ + 1 đã công khai) × **M = 5/5 dạng** (+2 dạng phụ M2b/M2c) = **9 lượt bấm xác nhận thật** + **2 lượt hủy công khai** + **7 lượt đối chứng đọc lại bản ghi qua máy chủ**; mọi lượt hợp lệ đều **tải lại trang rồi đọc lại 4 kết cục** | **Không** |

**Giới hạn hiệu lực (KHÔNG phải GAP):** đo trên env **nội bộ** `18.143.165.120.nip.io` và bản dựng ghi ở đầu
file — **khác env + khác bản dựng** với ảnh của đối tác (`htpldn-uat.ospgroup.vn`, `HTPLDN · V1.0`, 25/07).
Dòng bảng **không có** *DEV phản hồi lần 1* ⇒ không có mô tả fix nào của dev để kế thừa; đo lại từ đầu.

---

## 7. Sửa đổi tiêu chí (ghi bổ sung nếu có, kèm mốc giờ)

- **18:05 — bản dựng đã đọc lại ở đầu giai đoạn B:** trùng khít số ghi ở đầu file (`V1.0.8` ·
  `assets/index-DIABnbIr.js` · last-modified `Thu, 06 Aug 2026 07:13:15 GMT` · etag `W/"6a74340b-428"`).
  Không phải sửa ngưỡng nào.

- **18:10 — BỔ SUNG 2 dạng phụ M2b + M2c (tách biệt từng hồ sơ trong lô).** Lý do: lượt M2 (2 hồ sơ) cho
  kết quả nhập nhằng — giao diện báo thành công nhưng tải lại thì **cả 2** hồ sơ đều chưa công khai, trong
  khi máy chủ tự báo 1 bản ghi thành công / 1 bản ghi thất bại. Không tách biệt thì không biết lỗi thuộc về
  *bản ghi nào* hay thuộc về *cơ chế lô*. M2b = chỉ hồ sơ máy chủ báo thành công; M2c = chỉ hồ sơ máy chủ
  báo thất bại. **Không nới lỏng ngưỡng nào**, chỉ thêm phép đo để quy trách nhiệm đúng chỗ.

- **18:20 — chạy LẠI M2 lần 2** (cùng 2 hồ sơ, cùng thao tác) để chụp ảnh quyết định "báo thành công nhưng
  tải lại vẫn chưa công khai". Kết quả trùng khít lượt 17:48 ⇒ hiện tượng ổn định, không phải trục trặc
  nhất thời. Lượt này **không đổi dữ liệu** (cả lô bị hoàn tác) nên không phải hoàn nguyên.

- **18:35 — đo LẠI M4 bằng hồ sơ SẠCH.** Lượt M4 đầu tiên mượn `DDD-TVV-022` (đã công khai sẵn), nhưng hồ sơ
  này lại thuộc nhóm *loại Tư vấn viên thiếu Số thẻ hành nghề* — vốn luôn bị máy chủ từ chối vì ràng buộc
  `CHK_tu_van_vien_tvv_so_the_hanh_nghe` ⇒ **kết quả bị nhiễu**, không tách bạch được "bị chặn vì đã công
  khai" với "bị chặn vì thiếu số thẻ". Đã dựng lại tiền đề sạch: công khai `CG-QLND38-UAT` (loại Chuyên gia,
  không dính ràng buộc trên) rồi bấm công khai lần nữa trên chính hồ sơ đó. **Đã hoàn nguyên** ngay sau khi
  đo (Hủy công khai → cờ tắt, thời gian đăng tải về rỗng).

- **Ghi chú giới hạn (không đổi tiêu chí):** không đo lượt công khai lại trên `TVV-BTP-TW-0002` /
  `DDD-TVV-021` — công khai lại sẽ **ghi đè thời gian đăng tải** của bản ghi người khác đang giữ, mà
  BR-PUBLIC-03 (`srs-v3.5.md:5697`) cấm sửa tay trường này ⇒ không hoàn nguyên được. Dùng hồ sơ QA tự dựng
  tiền đề thay thế.
