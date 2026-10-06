# Nhật ký đo — XNTGHTVV_03 (dòng 51) · R3 2026-08-07

**Chuẩn chấm đã khóa:** [`../chuan/XNTGHTVV_03.md`](../chuan/XNTGHTVV_03.md)
**Bug entry:** `BUG-VV-XNTGHTVV-03` trong `../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md`
**Verdict đề xuất: ✅ PASS (Closed-verified)**

---

## 1. Vân tay bản dựng (BƯỚC 0 — đo trước mọi thao tác)

Tải lại trang bằng địa chỉ `https://18.143.165.120.nip.io/login`, đọc `GET /` bằng `fetch(cache:'no-store')`:

| Mục | Giá trị đo được | Đối chiếu bản đã biết |
|---|---|---|
| Chuỗi phiên bản chân sidebar | `HTPLDN · V1.0.10` | **TRÙNG** |
| Bó mã FE | `assets/index-B2W2Krcs.js` (+ `assets/index-DVlgOkLg.css`) | **TRÙNG** |
| `last-modified` | `Thu, 06 Aug 2026 17:39:54 GMT` | **TRÙNG** |
| `etag` | `W/"6a74c6ea-428"` | **TRÙNG** |

⇒ Env **không** deploy thêm trong lúc đo. Không có cảnh báo bản dựng.

---

## 2. Tiền đề đã dựng (kho đã cạn — bắt buộc dựng mới)

Xác nhận trước khi dựng: `GET /api/v1/vu-viecs?trangThai=DA_TIEP_NHAN` trả **15 hồ sơ**, **0 hồ sơ ở "Đã phân công"** — đúng như chuẩn chấm §3.3 mô tả. Dùng **Công thức A (tái sử dụng)**: phân công lại 3 hồ sơ đã bị tiêu vòng 06/08.

**Chốt định danh trước khi bấm** (đọc từ `GET /api/v1/vu-viecs/{id}`):

| Dạng | Mã VV | `id` | `nguoiTaoId` | `nguoiTiepNhanId` | Người **phân công lại** (R3) | Người **từ chối** (R3) |
|---|---|---|---|---|---|---|
| **①** người tạo ≡ người phân công | `VV-BTP-TW-20260806-001` | `1d26d8c7-e99d-42f6-956a-ab4726f722b2` | `6647b7bb…` (cbnv_tw_01) | `6647b7bb…` (cbnv_tw_01) | `cbnv_tw_01` | `qa_tvvseed28` (`5432719c…`) |
| **②** người tạo ≠ người phân công | `VV-BTP-TW-20260806-002` | `ca7d0fb0-b1e0-4da2-b067-73b9ac918775` | `6647b7bb…` (cbnv_tw_01) | `6647b7bb…` (cbnv_tw_01) | **`cbnv_tw_02`** (`75ef9f6b…`) | `qa_tvvseed28` |
| **③** người tạo là **Doanh nghiệp** | `VV-STP-AG-20260806-004` | `4100caae-7772-4474-b405-c197e7ac2104` | `b9c7f944…` (**DN** QA UAT DN An Giang) | `e81aa51b…` (cbnv_dp_01) | **`cbnv_dp_02`** (`7a4e1b00…`) | **`nht_ag_uat2`** (`acf00fb8…`) |

Cả 3 lần phân công đều làm bằng **UI thật** (nút [Phân công] → thẻ "Cá nhân" → chọn trong danh sách gợi ý → [Xác nhận]), đọc lại máy chủ xác nhận `trangThai = DA_PHAN_CONG` + `nguoiXuLyId` đúng người.

> Pool gợi ý **không** bị ảnh hưởng bởi việc `qa_tvvseed28` đã đổi `loaiTvv` TVV→CG: modal vẫn liệt kê `[TVV] QA TVV Seed28 Active (TVV-BTP-TW-0002)`. **Không phải mutate gì thêm.**

**Chuỗi lý do đã nhập (ghi nguyên văn TRƯỚC khi bấm):**

| Dạng | Chuỗi lý do (52 ký tự) |
|---|---|
| ① | `QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1` |
| ② | `QA-XNTG-20260807-0130-tu-choi-tham-gia-ho-tro-dang-2` |
| ③ | `QA-XNTG-20260807-0140-tu-choi-tham-gia-ho-tro-dang-3` |

---

## 3. Từng bước đo + số liệu thô

### 3.1 Ba lần bấm [Từ chối] bằng UI thật (bộ bắt thông báo cài TRƯỚC mỗi lần bấm)

Mỗi lần: dán `output/UAT_doi-tac/tools/toast-capture.js` → chạy đoạn TỰ KIỂM → bấm → đợi 3s → đọc.
**Cả 3 lần `soObserverDangSong = 1`** ⇒ số liệu hợp lệ.

| Dạng | Mã VV | Giờ máy chủ (UTC) | Giờ hiển thị (VN) | `SO_REQUEST` | Request | `SO_KHUNG_THONG_BAO` | `chu` | `BI_LAP` | `khoangCachMs` |
|---|---|---|---|---|---|---|---|---|---|
| ① | -001 | `2026-08-06T18:22:40.206Z` | 07/08 01:22 | **1** | `POST /api/v1/vu-viecs/1d26d8c7…/tu-choi-phan-cong` | **1** | `Đã từ chối phân công` | false | null |
| ② | -002 | `2026-08-06T18:23:33.898Z` | 07/08 01:23 | **1** | `POST /api/v1/vu-viecs/ca7d0fb0…/tu-choi-phan-cong` | **1** | `Đã từ chối phân công` | false | null |
| ③ | -004 | `2026-08-06T18:24:49.161Z` | 07/08 01:24 | **1** | `POST /api/v1/vu-viecs/4100caae…/tu-choi-phan-cong` | **1** | `Đã từ chối phân công` | false | null |

Cả 3 lần: **1 lời gọi → đúng 1 khung thông báo**, không lặp, tự quay về màn danh sách `/vu-viec/danh-sach`.

### 3.2 Đường đo 1 — cán bộ phụ trách đọc trên màn chi tiết

Đăng nhập **đúng cán bộ đang phụ trách hồ sơ** (không dùng `admin`), mở `/vu-viec/{id}`, cuộn tới khối **"Dòng thời gian"**, đồng thời quét `document.body.innerText` toàn màn tìm chuỗi lý do.

| Dạng | Tài khoản đọc | Trạng thái hồ sơ lúc đọc | Nhóm "Phân công NHT/TVV" còn hiện? | Tìm thấy chuỗi lý do trên màn? | Đoạn đọc được |
|---|---|---|---|---|---|
| ① | `cbnv_tw_01` (`6647b7bb…` = `nguoiTiepNhanId`) | Đã tiếp nhận | **KHÔNG** | ✅ **CÓ** | `Từ chối phân công · 07/08/2026 01:22 · QA TVV Seed28 Active` → **`Lý do: QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1`** |
| ② | `cbnv_tw_01` | Đã tiếp nhận | **KHÔNG** | ✅ **CÓ** | `Từ chối phân công · 07/08/2026 01:23 · QA TVV Seed28 Active` → **`Lý do: QA-XNTG-20260807-0130-tu-choi-tham-gia-ho-tro-dang-2`** |
| ③ | `cbnv_dp_01` (`e81aa51b…` = `nguoiTiepNhanId`) | Đã tiếp nhận | **KHÔNG** | ✅ **CÓ** | `Từ chối phân công · 07/08/2026 01:24 · QA NHT An Giang UAT2` → **`Lý do: QA-XNTG-20260807-0140-tu-choi-tham-gia-ho-tro-dang-3`** |

🔴 **Điểm quyết định:** nhóm "Phân công Người hỗ trợ / Tư vấn viên" (chỗ vòng trước còn cột *Lý do từ chối*) **đã ẩn** vì hồ sơ về "Đã tiếp nhận" — **giống hệt tình huống FAIL vòng 06/08**. Lần này lý do đọc được **ngay trong dòng nhật ký của khối "Dòng thời gian"**, tức đúng chỗ chuẩn chấm đòi.

### 3.3 Đường đo 2 (độc lập) — đọc lại nhật ký từ máy chủ

`GET /api/v1/vu-viecs/{id}/lich-su` **bằng chính phiên đăng nhập của cán bộ phụ trách** (cookie-auth), không dùng `admin`.

Cấu trúc mục nhật ký nay là `id, hanhDong, entityType, nguoiThucHienId, nguoiThucHien, thoiGian, **lyDo**, duLieuCu, duLieuMoi` — **trường `lyDo` là trường MỚI so với vòng 06/08**.

| Dạng | Mục `hanhDong = TU_CHOI_PHAN_CONG` mới | `lyDo` trả về | `duLieuMoi.lyDo` | Khớp từng chữ chuỗi đã nhập? | Lệch giờ so với lúc bấm |
|---|---|---|---|---|---|
| ① | `2026-08-06T18:22:40.206Z` · QA TVV Seed28 Active | `QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1` | giống | ✅ **khớp 52/52 ký tự** | 0s |
| ② | `2026-08-06T18:23:33.898Z` · QA TVV Seed28 Active | `QA-XNTG-20260807-0130-tu-choi-tham-gia-ho-tro-dang-2` | giống | ✅ **khớp 52/52 ký tự** | 0s |
| ③ | `2026-08-06T18:24:49.161Z` · QA NHT An Giang UAT2 | `QA-XNTG-20260807-0140-tu-choi-tham-gia-ho-tro-dang-3` | giống | ✅ **khớp 52/52 ký tự** | 0s |

**Hai đường đo TRÙNG KHÍT trên cả 3 hồ sơ.** Không có ca "máy chủ có mà màn không đọc được" hay ngược lại.

### 3.4 Chứng cứ đã tránh được bẫy "record cũ đóng băng" (bẫy 5 + 6 chuẩn chấm)

Trong cùng lời gọi nhật ký, **mục từ chối CŨ của vòng 06/08 vẫn `lyDo: null`**:

| Mã VV | Mục cũ (sinh trước bản fix) | `lyDo` | Mục mới (sinh sau bản fix) | `lyDo` |
|---|---|---|---|---|
| -001 | `2026-08-06T07:43:10.514Z` | **null** | `2026-08-06T18:22:40.206Z` | có, khớp |
| -002 | `2026-08-06T07:53:24.373Z` | **null** | `2026-08-06T18:23:33.898Z` | có, khớp |
| -004 | `2026-08-06T08:02:58.196Z` | **null** | `2026-08-06T18:24:49.161Z` | có, khớp |

⇒ Nếu đo trên bản ghi cũ sẽ ra **Reopen oan**. Verdict chỉ dựa trên **3 thao tác từ chối MỚI thực hiện sau bản fix**. Trên ảnh chụp cũng thấy rõ dòng cũ (06/08 14:43 / 14:53 / 15:02) **không có** dòng `Lý do:`, dòng mới **có**.

---

## 4. Ảnh kèm chú thích (đã mở đọc lại từng ảnh, tên ↔ nội dung khớp)

Thư mục: `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/`

| Tên file | Thấy gì |
|---|---|
| `XNTGHTVV_03-R3-01-VV001-sau-bam-Tu-choi-toast-va-ve-danh-sach.png` | Ngay sau khi bấm [Xác nhận] từ chối VV-001: hệ thống đã tự chuyển về màn danh sách vụ việc (vế (a3) vẫn đạt). |
| `XNTGHTVV_03-R3-02-VV001-cbnv-tw-01-dong-thoi-gian-hien-Ly-do-tu-choi.png` | Phiên `cbnv_tw_01`, sidebar ghi `HTPLDN · V1.0.10`, hồ sơ VV-001. Khối "Dòng thời gian": mục `Từ chối phân công 07/08/2026 01:22 QA TVV Seed28 Active` kèm dòng **`Lý do: QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1`**. Mục cũ `06/08/2026 14:43` bên dưới **không có** dòng Lý do. |
| `XNTGHTVV_03-R3-03-VV002-cbnv-tw-01-dong-thoi-gian-hien-Ly-do-tu-choi.png` | Phiên `cbnv_tw_01`, hồ sơ VV-002 (dạng ②, người phân công là CB #02). Mục `Từ chối phân công 07/08/2026 01:23` kèm **`Lý do: QA-XNTG-20260807-0130-…-dang-2`**; mục cũ `06/08/2026 14:53` không có Lý do. |
| `XNTGHTVV_03-R3-04-VV004-cbnv-dp-01-dong-thoi-gian-hien-Ly-do-tu-choi-dang-DN-tao.png` | Phiên `cbnv_dp_01` (BTP·DP), hồ sơ VV-STP-AG-20260806-004 do **Doanh nghiệp** tạo (`Tạo vụ việc … QA UAT DN An Giang`). Mục `Từ chối phân công 07/08/2026 01:24 QA NHT An Giang UAT2` kèm **`Lý do: QA-XNTG-20260807-0140-…-dang-3`**. |

---

## 5. Bảng đối chiếu 5 dòng điều kiện

| # | Điều kiện chuẩn chấm | Yêu cầu | Thực tế đã đo | GAP |
|---|---|---|---|---|
| 1 | **Vai trò** | Người bấm = người được phân công; người ra verdict = **cán bộ nghiệp vụ đang phụ trách hồ sơ**; CẤM `admin` | Bấm: `qa_tvvseed28` (①②), `nht_ag_uat2` (③). Verdict: `cbnv_tw_01` (①②, `userId` = `nguoiTiepNhanId`), `cbnv_dp_01` (③, `userId` = `nguoiTiepNhanId`). **Không dùng `admin` bất kỳ bước nào.** | **Không** |
| 2 | **Entity + trạng thái** | VV ở "Đã phân công", bản ghi phân công "Chờ xác nhận", rồi bị từ chối | Cả 3 đưa về `DA_PHAN_CONG` + `Chờ xác nhận` trước khi bấm; sau khi bấm về `DA_TIEP_NHAN` | **Không** |
| 3 | **Dữ liệu tiền đề** | ≥2 hồ sơ (chuẩn khóa ⇒ ≥3), **thao tác từ chối MỚI sau bản fix** | **3 hồ sơ**, 3 thao tác từ chối mới lúc 07/08 01:22–01:24; bản ghi cũ đã tách bạch và không dùng | **Không** |
| 4 | **Input** | Lý do ≥10 ký tự, chuỗi mốc-giờ duy nhất, ghi nguyên văn trước khi bấm | 3 chuỗi `QA-XNTG-20260807-01xx-…`, mỗi chuỗi 52 ký tự, ghi trước khi bấm | **Không** |
| 5 | **Độ phủ biến thể** | **N ≥ 3 · M = 3 dạng** (① tạo≡phân công · ② tạo≠phân công · ③ người tạo là DN) | **N = 3 · M = 3/3** — ① `cbnv_tw_01` tự phân công · ② `cbnv_tw_02` phân công hồ sơ do `cbnv_tw_01` tạo · ③ DN tạo, `cbnv_dp_02` phân công, NHT từ chối | **Không** |

**Chiều không bắt buộc:** modal phân công có 2 thẻ "Cá nhân"/"Tổ chức tư vấn"; vòng này vẫn chỉ phủ **Cá nhân** (TVV cấp TW + NHT cấp ĐP) — đúng như chuẩn chấm §7 đã chốt là **không** thêm vào M.

---

## 6. Đối chiếu khối PASS/FAIL đã khóa

Khối nguyên văn (bug-report.md:738–741):

> ✅ PASS khi: mục nhật ký của thao tác từ chối phân công mang lý do khác rỗng và khớp từng chữ chuỗi đã nhập, ĐỒNG THỜI cán bộ đọc được lý do đó ngay trên hồ sơ. Đúng ở cả hai đường đo, và lặp lại được trên ít nhất 2 hồ sơ khác nhau.

| Vế PASS | Kết quả |
|---|---|
| Mục nhật ký mang lý do **khác rỗng** | ✅ 3/3 |
| **Khớp từng chữ** chuỗi đã nhập | ✅ 3/3 (52/52 ký tự) |
| Cán bộ **đọc được ngay trên hồ sơ** | ✅ 3/3 (khối "Dòng thời gian", dòng `Lý do:`) |
| **Đúng ở cả hai đường đo** | ✅ 3/3 trùng khít |
| Lặp lại trên **≥2 hồ sơ khác nhau** | ✅ 3 hồ sơ |

Không rơi vào vế FAIL nào: nhật ký **không** còn trống lý do · **không** phải "máy chủ có mà màn không đọc được" · lý do **không** lệch chuỗi đã nhập.

**Hai lằn ranh chống oan đều tuân thủ:**
- Không chấm PASS vì thấy lý do ở thông báo/bản ghi phân công — verdict đọc **đúng mục nhật ký** của vụ việc, và ở thời điểm đọc nhóm "Phân công NHT/TVV" đã **ẩn**.
- Không chấm FAIL vì cách trình bày — dev đặt lý do thành dòng phụ `Lý do: …` ngay dưới dòng nhật ký; chuẩn chấm §2 ghi rõ chỗ đặt lý do không bị quy định (`:1735` không khai chỗ cho `ly_do`; yêu cầu đứng trên `:2406`).

**⇒ VERDICT: ✅ PASS (Closed-verified).**

---

## 7. Hai câu bắt buộc

**a) Fix này có làm hỏng gì khác trong cùng luồng không? — KHÔNG.**
6/7 vế đã hết lỗi từ vòng 06/08 vẫn nguyên (quan sát tự lộ trong đúng bước bắt buộc, không mở rộng case):
- (a1) không văng màn chặn quyền — 3/3 lần bấm đều `POST … /tu-choi-phan-cong` thành công, không mã 403 nào.
- (a2) thông báo thành công `Đã từ chối phân công` — 3/3, **đúng 1 khung / 1 lời gọi**, không lặp.
- (a3) tự quay về màn danh sách — 3/3.
- (c) hồ sơ về đúng **"Đã tiếp nhận"** (không phải "Chờ phê duyệt") và **phân công lại được** — chính vòng này đã phân công lại thành công cả 3 hồ sơ đúng bằng nút [Phân công] ở trạng thái đó.
- (b) bản ghi phân công `TU_CHOI` + `lyDoTuChoi` + mốc thời gian — vẫn đọc được trên bảng nhóm phân công lúc hồ sơ còn ở "Đã phân công".

**b) Ngoài phạm vi bug, có thấy gì bất thường không? — Không phát hiện lỗi mới. Có 1 quan sát tích cực nêu để điều phối biết:**
`BUG-VV-LICHSU-THEO-NGUOI` (bug khác, đang Open trong cùng file: *"Dòng thời gian chỉ hiện sự kiện do chính người đang đăng nhập thực hiện"*) **không còn tái hiện** trên bản dựng này: `cbnv_tw_01` đọc được cả mục do `cbnv_tw_02` và `qa_tvvseed28` thực hiện; `cbnv_dp_01` đọc được mục do `cbnv_dp_02`, `nht_ag_uat2` và **doanh nghiệp** thực hiện (ảnh R3-02/03/04). Đây là **quan sát ngoài phạm vi vế 51** — **không** dùng để kéo verdict case này, và **không** tự đóng bug đó (bug đó có tiêu chí + độ phủ riêng, phải đo theo chuẩn của nó). Ghi để điều phối xếp lịch re-verify.

Không mở thêm màn / vai trò / bộ lọc nào chỉ để săn lỗi.

---

## 8. Dữ liệu đã dựng · đã hoàn nguyên

**Đã đổi:**
- Phân công lại 3 hồ sơ đang ở `DA_TIEP_NHAN` (`-001` → `qa_tvvseed28` bởi `cbnv_tw_01`; `-002` → `qa_tvvseed28` bởi `cbnv_tw_02`; `-004` → `nht_ag_uat2` bởi `cbnv_dp_02`).
- 3 thao tác **Từ chối phân công** mới kèm lý do (sinh thêm 3 mục nhật ký + 3 bản ghi phân công `TU_CHOI`).

**Đã hoàn nguyên:** cả 3 hồ sơ **tự quay về đúng trạng thái ban đầu `DA_TIEP_NHAN`, `nguoiXuLyId = null`** ngay khi thao tác từ chối hoàn tất — tức trạng thái sau khi đo **giống hệt trạng thái trước khi đo**. Không sửa/xóa bản ghi có sẵn nào, không tạo vụ việc mới, không đụng dữ liệu đối tác.

**Không hoàn nguyên được (bản chất audit trail, không nên xóa):** 3 mục nhật ký mới + 3 bản ghi phân công `TU_CHOI` mới. Ba hồ sơ vẫn dùng lại được làm tiền đề cho vòng sau bằng đúng công thức A.

---

## 9. Giới hạn hiệu lực

Verdict chỉ có giá trị cho **env nội bộ `18.143.165.120.nip.io`** + **bản dựng `V1.0.10` / `assets/index-B2W2Krcs.js` / `last-modified Thu, 06 Aug 2026 17:39:54 GMT` / `etag W/"6a74c6ea-428"`**. Bằng chứng gốc của đối tác quay trên môi trường nghiệm thu khác ⇒ phải re-verify khi bản dựng này lên môi trường đó.
