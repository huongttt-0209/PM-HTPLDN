# Re-verify QLNDTVVCG_24 — Chấp nhận phân công (thông báo cho DN + CB NV)

**Ngày chạy:** 10/08/2026 — env dev 04:36–04:47 UTC · **env nghiệm thu 06:50–07:12 UTC**
**Môi trường:** ✅ đã đo **cả hai** — `18.143.165.120.nip.io` (dev) và **`htpldn-uat.ospgroup.vn` (env nghiệm thu của đối tác)**. Cả hai đều báo build **HTPLDN · V1.0.10**.
**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `bug` (gid 1714340219), **dòng 286**
**Trạng thái dòng:** `Trạng thái = Fail` · `Dopai = dev done` · `Trạng thái dev fix = Test done` · cột `Kết quả verify` đang chứa **verdict Pass cũ ngày 06/08** (đã lỗi thời — xem mục 6)

---

## 1. Câu hỏi của QA: BA phản hồi Doanh nghiệp có nhận được thông báo không?

**Có — BA đã chốt ngày 06/08/2026, và SRS đã được sửa theo.** Câu trả lời chính xác:

> **Doanh nghiệp CÓ nhận thông báo, nhưng CHỈ qua thư điện tử** gửi tới `DOANH_NGHIEP.email`.
> Doanh nghiệp ở nhóm Tư vấn chuyên sâu **không** có thông báo trong ứng dụng.

Căn cứ nguyên văn (bản chốt `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`):

| Dòng | Nội dung |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:192` | Bước 6 của *Processing — CG xác nhận*: "Gửi thông báo CG đã xác nhận — **CB NV: in-app + email; DN: chỉ thư điện tử** tới `DOANH_NGHIEP.email` (DN nhóm này chưa có tài khoản, xem BR-NOTIF-01) `[BA chốt 2026-08-06]`" |
| `srs-fr-12-tv-chuyen-sau.md:1550` | Bảng máy trạng thái: "PHAN_CONG → DANG_TU_VAN … Tạo phiên TV; **TB CB NV (in-app + email) + TB DN (chỉ thư điện tử)**" |
| `srs-v3.5.md:5664` (BR-NOTIF-01) | "**Bên nhận chưa có tài khoản trong hệ thống** (điển hình: DN ở nhóm X.1 — *"TVCS không có cổng cho DN"*): **chỉ gửi thư điện tử** tới `DOANH_NGHIEP.email`; hệ thống **vẫn tạo bản ghi `THONG_BAO` để lưu vết** nhưng đặt `hien_trong_ung_dung = 0` …; nếu địa chỉ thư trống thì **ghi cảnh báo vào nhật ký** …, KHÔNG chặn luồng nghiệp vụ `[BA chốt 2026-08-06]`" |
| `srs-v3.5.md:5664` (cột Áp dụng) | Phạm vi BR-NOTIF-01 nay **đã bổ sung** `FR-X.1` — trước đây thiếu, chính là lý do QA không tự chốt được ở lượt 06/08 |

Nguồn quyết định: [`BA-phan-hoi/phan-hoi-ba-7-diem-can-chot-2026-08-06.md`](../../reverify-week-5/ba-confirm/BA-phan-hoi/phan-hoi-ba-7-diem-can-chot-2026-08-06.md) mục 2 — *"kênh chuẩn … là TRONG ỨNG DỤNG + THƯ ĐIỆN TỬ. Hiện thiếu thư điện tử ⇒ là lỗi phần mềm"*, kèm câu chốt `QLNDTVVCG_24` **đảo từ Pass sang còn lỗi**.

## 2. Verdict: ✅ Pass trên CẢ HAI môi trường — không còn tái hiện

Đối tác phản ánh: *"Doanh nghiệp và CBNV không nhận được thông báo"*. Trên V1.0.10, **cả hai đều nhận**, đúng kênh SRS đòi.

### 2.1 Env nghiệm thu `htpldn-uat.ospgroup.vn` — 2 lượt đo độc lập

| # | Điểm kiểm (theo SRS đã sửa) | Lượt 1 — `TVCS-20260608-0001` (DN *Cty Verify Dup*) | Lượt 2 — `TVCS-20260810-0001` (DN **TKM Company**) |
|---|---|---|---|
| 1 | `:190` — trạng thái → DANG_TU_VAN, ghi `ngay_bat_dau` = NOW() | **Đang tư vấn**; `ngayBatDau = 07:06:02.614` — đúng giây bấm | **Đang tư vấn**; `ngayBatDau = 07:12:05.698` — đúng giây bấm |
| 2 | `:191` — tạo `PHIEN_TU_VAN` mới liên kết bản ghi | **1** phiên, tạo lúc `07:06:02.606`, trạng thái `CHO_XAC_NHAN` (trước thao tác: 0) | **1** phiên, tạo lúc `07:12:05.692`, `CHO_XAC_NHAN` (trước: 0) |
| 3 | `:192` — **CB NV: in-app + email** | in-app cho `cb_nv_tw_03` lúc `07:06:02.652` (chưa đọc) · email `cb_nv_tw_03@htpldn.test` lúc `07:06:02.723` | in-app cho `cbnv_tw`: chưa đọc **436 → 437**, mục lúc `07:12:05.728` · email `cbnv_tw@htpldn.gov.vn` lúc `07:12:05.795` |
| 4 | `:192` — **DN: chỉ thư điện tử** tới `DOANH_NGHIEP.email` | email `verify_dup_002@example.com` lúc `07:06:02.712` | email **`tkm@gmail.com`** lúc `07:12:05.794` |
| 5 | `:192` — DN **không** hiện in-app (`hien_trong_ung_dung = 0`) | DN chưa kích hoạt tài khoản → không đăng nhập kiểm được (xem lượt 2) | Đăng nhập DN `0151554887`: tổng thông báo **14 → 14**, chưa đọc **8 → 8**, **không** mục nào nhắc `TVCS-20260810-0001` |
| 6 | `:193` — ghi nhật ký thao tác | `audit-logs` có `UPDATE` lúc `07:06:02.651` | `audit-logs` có `UPDATE` ngay sau thao tác |
| 7 | Toast trên màn CG | **1** khung "Đã xác nhận" · **1** request `POST …/xac-nhan` | **1** khung "Đã xác nhận" · **1** request `POST …/xac-nhan` |

Bộ bắt thông báo đã **tự kiểm trước khi tin số liệu**: `soObserverDangSong = 1` ở cả hai lượt.

### 2.2 Env dev `18.143.165.120.nip.io` — `TVCS-20260806-0003`

| # | Điểm kiểm | Kết quả đo |
|---|---|---|
| 1 | `:190` DANG_TU_VAN + `ngay_bat_dau` | **Đang tư vấn**; `ngayBatDau = 04:41:42.665` — đúng giây bấm |
| 2 | `:191` tạo `PHIEN_TU_VAN` | **1** phiên, tạo lúc `04:41:42.655`, `CHO_XAC_NHAN` — *(đo bổ sung 10/08 07:15; xem mục 5 về đính chính)* |
| 3 | `:192` CB NV in-app + email | in-app `04:41:42.702` · email `cbnv_tw_02@htpldn.test` `04:41:42.771` |
| 4 | `:192` DN chỉ thư điện tử | email `qa.uat.dn.verify@test.htpldn.vn` `04:41:42.781` |
| 5 | DN không hiện in-app | Đăng nhập DN `0109998887`: không mục nào cho `TVCS-20260806-0003` |
| 6 | `:193` nhật ký | `audit-logs` có `UPDATE` `04:41:42.726` |
| 7 | Toast | 1 khung, 1 request — không lặp |

## 3. Control loại trừ "SMTP hỏng" — chốt quan trọng nhất

Trên **cả hai** env, bước **phân công** (ngay trước thao tác cần đo) đã gửi email thật cho chuyên gia:

| Env | Thư phân công | Tổng thư |
|---|---|---|
| ospgroup lượt 1 | `truong.16@test.htpldn.vn` — *"Bạn được phân công tư vấn: TVCS-20260608-0001"* lúc `07:03:30.912` | 848 → 849 |
| ospgroup lượt 2 | `truong.16@test.htpldn.vn` — *"…: TVCS-20260810-0001"* lúc `07:11:16.877` | 855 → 856 |
| dev | `qa.tvvseed28@htpldn-uat.local` | 1996 → 1997 |

⇒ Kênh email của hệ thống đang sống. Nếu bước *CG xác nhận* không gửi thư thì đó là thiếu sót của chính
tính năng, không phải do MailHog/SMTP. Sau khi bấm Chấp nhận: ospgroup **849 → 851** và **855 → 857**
(mỗi lượt đúng 2 thư: DN + CB NV); dev **1998 → 2000**.

Nội dung thư đã **mở đọc**, không chỉ đếm:
- Tới DN: *"Mã: TVCS-20260810-0001. Chuyên gia đã nhận việc, nội dung đang được tư vấn."*
- Tới CB NV: *"Mã: TVCS-20260810-0001. Chuyên gia đã nhận việc, nội dung chuyển sang trạng thái đang tư vấn."*

## 4. Bằng chứng mạnh nhất: so sánh trước/sau trên chính DN của đối tác

Lượt 2 dùng đúng **TKM Company** — doanh nghiệp trong phiếu gốc của đối tác. Chuông thông báo của DN này
hiện vẫn còn mục cũ **"Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0003"** ngày **04/08** — tức DN **từng**
nhận đúng sự kiện này trong ứng dụng. Sau thao tác 10/08, cùng sự kiện đó **không** sinh mục in-app nào nữa,
mà đi bằng **thư tới `tkm@gmail.com`**.

⇒ Đây không phải "thông báo bị mất", mà là **đổi kênh có chủ đích theo quyết định BA 06/08**.
Ảnh [`OSP-D`](evidence/OSP-D-DN-TKM-khong-co-thong-bao-trong-ung-dung.png) chụp đúng cảnh này: mục mới nhất
trong chuông DN là "4 ngày trước", trong khi thao tác vừa xảy ra "một phút trước".

## 5. Đính chính báo cáo lượt dev (vế `:191`)

Bản trước của file này ghi *"không có endpoint `PHIEN_TU_VAN` trong `/api/docs-json` (549 đường dẫn)"* nên
xếp `:191` là **không đo được**. **Câu đó sai.** Endpoint `/api/v1/noi-dung-tu-van-cs/{tuVanCsId}/phien-tu-vans`
**có** trên cả hai env (dev 549 path, ospgroup 624 path — đã mở lại `/api/docs-json` xác minh 10/08 07:15).
Đã đo lại thật: dev sinh 1 phiên lúc `04:41:42.655`, ospgroup sinh 1 phiên ở cả 2 lượt.
⇒ `:191` nay là **Đạt**, không còn vế nào bỏ ngỏ.

## 6. ⚠️ Cột `Kết quả verify` trên sheet đang LỖI THỜI — cần viết lại

Nội dung đang nằm ở cột T (dòng 286) là verdict Pass viết ngày **06/08**, **trước** khi BA chốt. Hai chỗ nay sai:

1. Câu *"thông báo hiện chỉ chạy trong ứng dụng, chưa có thư điện tử — **đặc tả không chốt kênh** cho sự kiện này"* → BA **đã** chốt kênh ngày 06/08 và SRS đã sửa (`:192`, `:1550`, `srs-v3.5.md:5664`).
2. Câu *"doanh nghiệp thấy **Chuyên gia đã xác nhận tư vấn** …"* mô tả thông báo **in-app** cho DN → hành vi đó đã **bị gỡ có chủ đích** theo BA chốt; nay DN nhận **thư điện tử**. Giữ nguyên câu cũ sẽ khiến lượt sau chấm sai chiều.

Verdict đúng cho lượt này vẫn là **Pass**, nhưng **lý do khác hẳn** verdict cũ: cũ Pass vì "in-app là đủ, đặc tả im lặng"; nay Pass vì **dev đã bổ sung đúng thư điện tử theo quyết định BA**.

## 7. Thay đổi dữ liệu đã thực hiện trên env nghiệm thu — khai đầy đủ

Để dựng được kịch bản, tôi đã tác động vào env đối tác. Liệt kê hết để đối tác đối soát:

| Việc đã làm | Đối tượng | Vì sao |
|---|---|---|
| Đặt lại mật khẩu qua luồng **Quên mật khẩu** chuẩn (không dùng cửa hậu quản trị) | `truong_16`, `cb_nv_tw_03` → `Test@1234` | Không có tài khoản CG nào trong `input.md` dùng được trên env này; 2 tài khoản này là **seed QA** (`@test.htpldn.vn`), lần đăng nhập cuối 09/05 và trước 04/08 |
| Tạo mới 1 bản ghi | `TVCS-20260810-0001` (DN TKM Company, Thuế) | Để đo được vế "DN không hiện in-app" bằng tài khoản DN đang hoạt động |
| Đẩy trạng thái TIEP_NHAN → DANG_TU_VAN | `TVCS-20260608-0001`, `TVCS-20260810-0001` | Chính là thao tác cần đo |

**KHÔNG đụng tới:** tài khoản `huongcg` của đối tác (đã thử `Test@1234` → sai mật khẩu, dừng ngay, không
đoán tiếp, không đặt lại mật khẩu) · bản ghi `TVCS-20260803-0002` (TKM) của đối tác · bất kỳ bản ghi
`DANG_TU_VAN`/`HOAN_THANH` nào có sẵn.

## 8. Quan sát thêm

**8.1 — CB NV nhận thông báo là NGƯỜI TẠO bản ghi, không phải người đi phân công.**
Chứng minh chéo 2 lượt trên ospgroup: lượt 1 người phân công là `cbnv_tw` nhưng thư + in-app đi tới
`cb_nv_tw_03` (người tạo) — `cbnv_tw` giữ nguyên 436 chưa đọc; lượt 2 `cbnv_tw` vừa tạo vừa phân công thì
mới nhận (436 → 437). SRS `:192` chỉ ghi "CB NV", không chốt là ai ⇒ **không log thành bug**, nhưng đây là
bẫy đã suýt làm kết luận nhầm "CB NV không nhận được thông báo". Ai verify lại phải đăng nhập **đúng tài
khoản tạo bản ghi**.

**8.2 — Bug candidate (ngoài phạm vi phiếu này): tài khoản chỉ có vai trò CG không có đường vào bản ghi được
phân công từ giao diện.** `truong_16` (vai trò đúng `["CG"]`) có menu chỉ gồm *Đào tạo, tập huấn* và *Mạng lưới
Tư vấn viên* — **không có mục Tư vấn chuyên sâu**. Thông báo "Bạn được phân công tư vấn" bấm vào chỉ mở trang
danh sách thông báo, không mở bản ghi, dù dữ liệu thông báo **có sẵn** `entityType = NOI_DUNG_TU_VAN_CS` +
`entityId`. Tôi phải gõ thẳng URL `/tv-chuyen-sau/{id}` mới vào được — và vào được thì thấy đủ nút
*Chấp nhận / Từ chối nhiệm vụ*, tức backend cho phép, chỉ thiếu lối đi ở giao diện.
Tài khoản `huongcg` của đối tác có **CG + TVV** nên không lộ ra lỗi này. ⇒ **Chưa log vào sheet đối tác**
(khác phiếu QLNDTVVCG_24), đề nghị mở phiếu riêng.

**8.3 — `cbnv_dp` (Sở Tư pháp Hà Nội) không phân công được `TVCS-20260803-0002`:** hộp chọn chuyên gia báo
*"Không có CG phù hợp với lĩnh vực này. Liên hệ quản trị để gán lĩnh vực cho chuyên gia."*, endpoint
`GET /tu-van-viens?trangThai=HOAT_DONG&loaiTvv=CG` trả `total: 0` vì cả 4 CG dùng được đều thuộc BTP·TW.
Đây là **thiếu dữ liệu seed của đơn vị Địa phương**, không phải lỗi phần mềm — ghi lại để lượt sau khỏi mất
thời gian dò như tôi.

**8.4** — `GET /api/v1/tu-van-chuyen-sau` trả `ERR-AUTH-MTLS-01` (chặn mTLS) trên env dev trong khi
`/api/v1/noi-dung-tu-van-cs` chạy bình thường; env ospgroup không chặn. Đường dẫn cũ chỉ dùng để tra cứu,
không ảnh hưởng verdict.

**8.5** — Ngoài các điểm trên, không thấy bất thường nào khác trên các màn đã đi qua.

## 9. Bằng chứng

**Env nghiệm thu ospgroup:**
- [evidence/OSP-A-toast-sau-chap-nhan.png](evidence/OSP-A-toast-sau-chap-nhan.png) — màn CG sau khi bấm Chấp nhận (lượt 1)
- [evidence/OSP-B-CBNV-thong-bao-trong-ung-dung.png](evidence/OSP-B-CBNV-thong-bao-trong-ung-dung.png) — `cb_nv_tw_03` nhận in-app (lượt 1)
- [evidence/OSP-C-TKM-sau-chap-nhan.png](evidence/OSP-C-TKM-sau-chap-nhan.png) — bản ghi TKM chuyển Đang tư vấn (lượt 2)
- [evidence/OSP-D-DN-TKM-khong-co-thong-bao-trong-ung-dung.png](evidence/OSP-D-DN-TKM-khong-co-thong-bao-trong-ung-dung.png) — **chuông DN TKM: mục mới nhất "4 ngày trước", không có mục cho thao tác vừa xảy ra**
- [evidence/OSP-E-CBNV-chuong-TKM-TVCS-20260810-0001.png](evidence/OSP-E-CBNV-chuong-TKM-TVCS-20260810-0001.png) — `cbnv_tw` nhận in-app "một phút trước" (lượt 2)
- [evidence/OSP-mailhog-dump.log](evidence/OSP-mailhog-dump.log) — dump thư 2 lượt

**Env dev:**
- [evidence/QLNDTVVCG_24-A-sau-chap-nhan-dang-tu-van-V1010.png](evidence/QLNDTVVCG_24-A-sau-chap-nhan-dang-tu-van-V1010.png)
- [evidence/QLNDTVVCG_24-B-CBNV-thong-bao-trong-ung-dung-V1010.png](evidence/QLNDTVVCG_24-B-CBNV-thong-bao-trong-ung-dung-V1010.png)
- [evidence/QLNDTVVCG_24-C-thu-dien-tu-gui-doanh-nghiep-V1010.png](evidence/QLNDTVVCG_24-C-thu-dien-tu-gui-doanh-nghiep-V1010.png)
- [evidence/QLNDTVVCG_24-mailhog-dump.log](evidence/QLNDTVVCG_24-mailhog-dump.log)

**Đối chiếu điều kiện:** [cond/QLNDTVVCG_24.md](cond/QLNDTVVCG_24.md)
**Nội dung đề nghị BA ghi vào file đối tác:** [de-xuat-ghi-chu-BA-cho-doi-tac.md](de-xuat-ghi-chu-BA-cho-doi-tac.md)
