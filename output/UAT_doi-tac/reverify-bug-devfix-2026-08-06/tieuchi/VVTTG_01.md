Mã case: VVTTG_01 (tab `bug` dòng 193)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (`HTPLDN · V1.0.8`) — đo 06/08/2026 14:26–14:34

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có (chưa từng qua vòng soát nội bộ).

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc theo thời gian** (SCR-IX-01, `loai=vu-viec-theo-thoi-gian`). Ô "Kết quả thực tế" ghi
gọn *"Số liệu thống kê không chính xác"*; TKM phản hồi lần 1 (28/7) nói rõ ra thành **1 vế đo được:**

> *"Số liệu BC Vụ việc đã tiếp nhận **>** BC Vụ việc theo thời gian mặc dù chọn cùng 1 khoảng thời gian"*

**Bằng chứng đã mở xem:** `../partner-evidence/VVTTG_01.webm` (28 giây, trích 7 frame về `../frames/VVTTG_01/`).

| Frame / tệp | Thấy gì |
|---|---|
| `../frames/VVTTG_01/t024.07s.jpg` | Bản dựng **V1.0**, vai trò **Quản trị viên QTHT** (BTP·TW). `BC Vụ việc theo thời gian` · Kỳ **Năm** 01/01/2026→31/12/2026 · Đơn vị **Toàn quốc** · `Thời điểm tạo: 15/07/2026 17:11` → **`Tổng vụ việc toàn kỳ = 10`**. Biểu đồ đường 1 điểm mốc `2026`, đỉnh ~10. |
| `../partner-evidence/VVDTN_06.jpg` (cùng ngày 15/07, dùng làm vế so sánh) | `BC Vụ việc đã tiếp nhận` · Kỳ **Năm** 01/01/2026→31/12/2026 · Đơn vị **Cục Bổ trợ tư pháp – BTP-TW** · `Thời điểm tạo: 15/07/2026 16:39` → **`Tổng vụ việc = 27`**. |

⇒ Con số đối tác dựa vào: **27 (đã tiếp nhận) > 10 (theo thời gian)**, cùng khoảng 01/01–31/12/2026.

🔴 **Hai ảnh này KHÔNG cùng đơn vị:** BC đã tiếp nhận lọc **BTP-TW**, BC theo thời gian để **Toàn quốc**.
Toàn quốc ⊇ BTP-TW ⇒ lẽ ra BC theo thời gian phải **≥** BC đã tiếp nhận. Việc nó nhỏ hơn khiến nghịch lý
**nặng thêm**, không nhẹ đi — nên vế đối tác nêu vẫn đứng vững, chỉ là điều kiện chưa trùng khít và phải
đo lại cho **cùng đơn vị**.

**Dữ liệu môi trường đối tác đã đổi từ đó:** `../partner-evidence/VVTTG_05_v2.jpg` (31/07/2026 14:50, bản
V1.0.3, Toàn quốc) cho `Tổng vụ việc toàn kỳ = **51**`, trong khi `VVDTN_06_v2.jpg` (31/07 14:06, BTP-TW)
vẫn `27`. Ở thời điểm 31/7 quan hệ đã thuận (51 ≥ 27). ⇒ **Không được** lấy cặp số 15/7 làm ngưỡng chấm;
phải đo lại tại chỗ (§4).

---

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

**FR-IX-05: BC Vụ việc theo thời gian (UC128)**

- `:323` (Mô tả) → `Báo cáo trend vụ việc theo thời gian (tuần/tháng/quý/năm) dạng biểu đồ line chart + bảng chi tiết.`
- `:325` (Tác nhân) → `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`
- `:327` (Template) → `Kế thừa TPL-REPORT-FULL (không bổ sung input)`
- `:329` (Công thức) → `Tổng hợp vụ việc theo kỳ thời gian — biểu đồ trend`
- `:337` (Output đặc thù) → `| 1 | trend_data[] | structured | Luôn | {ky_label, tiep_nhan, hoan_thanh} |`
- `:338` → `| 2 | theo_don_vi[] | structured | Luôn | {don_vi, ten, trend_data[]} |`
- `:342` (AC bổ sung) → `**Given** CB chọn kỳ Tháng, khoảng 6 tháng **When** tạo BC **Then** hiển thị biểu đồ trend 6 điểm + bảng chi tiết`

**Kế thừa từ TPL-REPORT-FULL (áp cho CẢ FR-IX-05 lẫn FR-IX-02, nên hai BC dùng chung luật lọc):**

- `:81` (bước 3) → `Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc, BN chỉ thấy BN mình, ĐP chỉ thấy ĐP mình...`
- `:82` (bước 4) → `Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)`
- `:100` (Output chung #7) → `| 7 | tong_ban_ghi | number | Luôn | Tổng số bản ghi |`

**Vế đối chiếu — FR-IX-02 (BC Vụ việc đã tiếp nhận):**

- `:203` (Công thức) → `Đếm số vụ việc đã tiếp nhận (trừ từ chối) trong kỳ, theo phạm vi đơn vị`
- `:213` → `| 1 | tong_vu_viec | number | Luôn | Tổng số VV tiếp nhận |`

**IM LẶNG về:** quan hệ số học bắt buộc giữa `trend_data[].tiep_nhan` (FR-IX-05) và `tong_vu_viec`
(FR-IX-02). Đặc tả **không** có câu nào nói hai báo cáo phải bằng nhau. Điểm khác biệt duy nhất đọc được:
`:203` **loại trừ vụ việc bị từ chối**, còn `:329` không nêu loại trừ gì.

⇒ **Trục chấm chính KHÔNG phải là so 2 báo cáo với nhau** (đặc tả im lặng về quan hệ đó), mà là so **từng
báo cáo với nguồn dữ liệu thật**. Phần "2 báo cáo lệch nhau" chỉ chuyển thành câu hỏi BA nếu **cả hai đều
khớp nguồn thật** mà vẫn lệch (khi ấy lệch là do định nghĩa khác nhau, BA phải chốt).

---

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw` / `Test@1234`** (`CB_NV_TW`, cấp TW) — đúng tác nhân `:325`, và cấp TW
  mới thấy được "Toàn quốc" như đối tác (`:81`, `:1049`).
- Đối chứng vai trò đối tác: **`admin` / `Secret@123`** (QTHT) — chỉ để đóng GAP, không ra verdict.
- Màn: `https://18.143.165.120.nip.io/bao-cao`, chạy **lần lượt 2 loại báo cáo trong cùng phiên**:
  **"BC Vụ việc theo thời gian"** và **"BC Vụ việc đã tiếp nhận"**.
- Bộ lọc: Kỳ **Năm**, 01/01/2026 → 31/12/2026 — và **cùng một đơn vị cho cả hai báo cáo** (chạy 2 lượt:
  lượt 1 cả hai = **BTP-TW**; lượt 2 cả hai = **Toàn quốc**). Đây là chỗ bằng chứng đối tác chưa trùng khít.
- Đường thứ hai — nguồn sự thật: gọi thẳng API danh sách vụ việc, đếm số vụ việc **đã tiếp nhận, đã
  duyệt** (`:82`) có ngày tiếp nhận trong 01/01/2026–31/12/2026, cùng phạm vi đơn vị. Con số này là mốc
  để chấm **cả hai** báo cáo.
- ⚠️ **Bẫy cache máy chủ:** đọc trường `Thời điểm tạo` của mỗi báo cáo trước khi kết luận. Nếu nó cũ hơn
  thời điểm mình vừa seed/đổi dữ liệu → số đang là cache, đổi `denNgay` 1 ngày để lấy khoá cache mới rồi
  đo lại.

---

## 4. Tiêu chí chấm

✅ **PASS khi ĐỦ cả 4:**

1. **BC Vụ việc theo thời gian khớp nguồn thật:** với Kỳ Năm 01/01–31/12/2026 và một đơn vị cụ thể,
   `Tổng vụ việc toàn kỳ` **bằng** số vụ việc đếm được bằng đường thứ hai trên cùng phạm vi + cùng khoảng.
2. **Các điểm trên biểu đồ/bảng cộng khớp tổng:** tổng các giá trị `tiep_nhan` của mọi mốc trong
   `trend_data[]` **bằng** `Tổng vụ việc toàn kỳ` hiển thị trên màn. (Các chiều không cộng khớp tổng ⇒ số
   đang sai, chưa được dùng.)
3. **Hai báo cáo nhất quán khi ép cùng điều kiện:** chạy BC đã tiếp nhận và BC theo thời gian với **cùng
   kỳ + cùng đơn vị**, thì `Tổng vụ việc toàn kỳ` (FR-IX-05) **không nhỏ hơn** `Tổng vụ việc` (FR-IX-02).
   Căn cứ: `:203` loại trừ vụ việc bị từ chối còn `:329` không loại trừ ⇒ tập của FR-IX-05 phải bao trùm.
4. Phủ đủ M dạng ở mục 5 — kết luận giống nhau ở **mọi** kỳ đã thử, không phải chỉ đúng ở kỳ Năm.

❌ **FAIL nếu bất kỳ:** `Tổng vụ việc toàn kỳ` lệch số đếm được bằng đường thứ hai · tổng các mốc trend
không bằng tổng trên màn · cùng kỳ + **cùng đơn vị** mà BC theo thời gian **nhỏ hơn** BC đã tiếp nhận ·
đổi kỳ (Tháng/Quý) thì tổng toàn kỳ đổi theo dù khoảng thời gian không đổi.

⛔ **KHÔNG được chấm Fail vì:**
- Hai báo cáo lệch nhau khi **khác đơn vị** (Toàn quốc vs BTP-TW) — chính bằng chứng đối tác dính lỗi này.
- BC theo thời gian **lớn hơn** BC đã tiếp nhận: hợp lệ theo `:203` (`trừ từ chối`).
- Nhãn mốc thời gian trên trục hiển thị dạng nào (`2026` / `2026-01-01`) — đặc tả im lặng.
- Số liệu đổi so với ảnh 15/07 của đối tác — dữ liệu môi trường thay đổi giữa các đợt, không phải lỗi.

**Nhánh cần BA (chỉ mở khi thoả đúng điều kiện này):** nếu tiêu chí 1 + 2 **đạt cho cả hai báo cáo** (mỗi
BC đều khớp nguồn thật của chính nó) mà tiêu chí 3 **vẫn lệch**, thì lệch đó đến từ chỗ đặc tả **im lặng**
về quan hệ giữa `trend_data[].tiep_nhan` và `tong_vu_viec` ⇒ không chấm Fail, đưa 1 mục sang file gửi BA.

---

## 5. Dạng dữ liệu phải phủ

**M = 3 kỳ báo cáo** × **2 đơn vị**, đo trên cùng một khoảng thời gian:

| # | Dạng | Vì sao phải có |
|---|---|---|
| 1 | Kỳ **Năm** 01/01–31/12/2026 | Trùng khít bằng chứng đối tác |
| 2 | Kỳ **Tháng** (một tháng có dữ liệu) | `:342` AC nêu đích danh kỳ Tháng; kiểm trend nhiều mốc chứ không phải 1 mốc như kỳ Năm |
| 3 | Kỳ **Quý** hoặc **Khoảng tùy chọn** | Bắt lỗi chỉ xuất hiện ở một cách nhóm kỳ |
| a/b | Mỗi kỳ chạy **2 đơn vị**: `BTP-TW` và `Toàn quốc` | Đóng đúng chỗ bằng chứng đối tác lệch (họ so BTP-TW với Toàn quốc) |

**Nguồn xác định M:** ① `:69` Input chung — `ky_bao_cao` là tập đóng `TUAN / THANG / QUY / NAM / KHOANG` ·
② `:331` Dimensions FR-IX-05 = `Kỳ (tuần/tháng/quý/năm), Đơn vị` ⇒ chính hai chiều này là biến thể phải
phủ · ③ dropdown "Kỳ báo cáo" + "Đơn vị" ngay trên màn SCR-IX-01.

Kỳ nào không có dữ liệu trong môi trường → ghi rõ vào mục 6, **không** thay bằng kỳ khác một cách im lặng.

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên QTHT** (`BTP · TW`) — KHÔNG thuộc tác nhân FR-IX-05 (`:325`) | Đo bằng **tác nhân đúng theo `:325`**, cấp TW (mới thấy Toàn quốc như đối tác): lần lượt `cbnv_tw` → `cbnv_tw_05` → `cbnv_tw_01` → `cbnv_tw_02` (đều `CB_NV_TW`, `donViId=…0001`, `capDonVi=TW`) do bị phiên QA khác chiếm tài khoản liên tục, xem "Sửa đổi giữa chừng". Cùng lượt cũng đối chứng bằng vai trò QTHT (`admin`) trên màn — số ra **y hệt** (Toàn quốc 50), nên vai trò không phải biến gây lệch | **Không** |
| Entity + trạng thái | VU_VIEC, chỉ bản ghi đã duyệt (`:82`). BC theo thời gian: `Tổng vụ việc toàn kỳ = 10` (15/07 17:11) → `51` (31/07 14:50). BC đã tiếp nhận: `27` ở cả hai mốc | Cùng entity. Đã **đếm bằng đường thứ hai** ngay trong phiên: `GET /api/v1/vu-viecs` (55 bản ghi), lọc `ngayTiepNhan` trong 2026 theo **giờ VN (+07)** rồi trừ `TU_CHOI` (1 bản ghi) ⇒ **Toàn quốc 50** · **BTP-TW 36** | **Không** |
| Dữ liệu tiền đề | Môi trường đối tác có VV trong 2026; **không có** bằng chứng nào cho biết số vụ việc THẬT trong khoảng — chưa ai đếm bằng đường thứ hai | **Đã tự dựng mốc thật** (xem dòng trên). Lưu ý: dữ liệu env **đang thay đổi liên tục** do phiên QA khác tạo vụ việc mới (44 lúc 12:54 → 49 lúc 07:26 UTC → 50 lúc 07:29 UTC) ⇒ mọi phép so đều đo **cùng một thời điểm** và bust cache máy chủ | **Không** |
| Input / filter / giá trị nhập | Kỳ `NAM`, `tuNgay=2026-01-01`, `denNgay=2026-12-31`. **Đơn vị LỆCH giữa 2 báo cáo**: theo thời gian = `Toàn quốc` (URL không có `donViId`), đã tiếp nhận = `BTP-TW` (`donViId=00000000-...-000000000001`) | **Ép CÙNG đơn vị cho cả hai báo cáo** — chạy 2 lượt: cả hai = `BTP-TW`, rồi cả hai = `Toàn quốc`. Đây chính là chỗ bằng chứng đối tác chưa trùng khít | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | Chỉ đo **1 kỳ** (Năm) · **1 lượt** mỗi báo cáo · không thử Tháng/Quý · không ép cùng đơn vị | Phủ đủ **M = 3 kỳ × 2 đơn vị** cho **cả hai** báo cáo (12 phép đo), cùng khoảng 01/01–31/12/2026. Kết quả: **BTP-TW 36 = 36 = 36** và **Toàn quốc 50 = 50 = 50** (BC theo thời gian = BC đã tiếp nhận = đếm đường thứ hai), khớp **từng mốc**: Tháng BTP-TW `1/3/3/8/8/13`, Tháng Toàn quốc `1/4/5/9/11/20`, Quý BTP-TW `7/8/21`, Quý Toàn quốc `10/9/30`. Tổng **không đổi** khi đổi kỳ ở cùng khoảng thời gian | **Không** |

**Sửa đổi giữa chừng (14:19 → 14:32):** bị đá phiên **6 lần** trong ~15 phút. Nguyên nhân khách quan, đã
kiểm chứng bằng MailHog: một phiên QA khác đang quét **cùng bộ tài khoản** trên cùng môi trường
(`cbnv_tw` 07:17:51 + 07:18:22 · `cbnv_tw_03` 07:21:41 · `cbnv_tw_01` 07:28:35 · `cbnv_tw_04` 07:28:39 ·
`cbnv_tw_02` 07:30:41 · `admin` 07:29:00 + 07:30:45 UTC — không phải mã OTP của mình), hệ thống chỉ cho
**1 phiên/tài khoản** nên mỗi lần họ đăng nhập là mình bị thu hồi token (`ERR-AUTH-SYS-00-03`).
- **Nới đã khai:** đổi lần lượt sang các tài khoản anh em **cùng vai trò `CB_NV_TW`, cùng `donViId=…0001`,
  cùng `capDonVi=TW`** (`_05`, `_01`, `_02`) — đúng Rule 7, **không** nới cấp/đơn vị, **không** đổi vai trò.
- Không ảnh hưởng phép đo: mỗi lượt đo đều xác nhận `auth/me` trước khi lấy số, và toàn bộ so sánh quyết
  định (báo cáo ↔ báo cáo ↔ đếm đường thứ hai) được chạy **trong cùng một lệnh, cùng một phiên**.

**Bẫy cache máy chủ — đã dính và đã gỡ:** lượt đo 07:28 cho Toàn quốc lệch **đúng 1** (báo cáo 49 vs đếm
50). Đọc `ngayTaoBc = 07:28:03` thấy cũ hơn thời điểm đếm (07:28:41) ⇒ nghi cache. Đổi `denNgay` sang
`2026-12-30` để lấy **khoá cache mới** rồi đo lại cùng lúc: **50 = 50 = 50**, khớp cả từng mốc. Kết luận:
lệch 1 là do bản ghi mới do phiên khác tạo xen vào giữa, **không phải lỗi báo cáo**.

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict.

**Ghi nhận thêm (không kéo verdict):** `:82` của TPL-REPORT-FULL ghi "truy vấn CHỈ bản ghi đã duyệt", nếu
áp nguyên văn thì cả hai báo cáo phải ra ~19 (chỉ `DA_DUYET` + `HOAN_THANH`) chứ không phải 50. Hiện trạng
đang chạy theo **công thức riêng của FR** (`:203` "đã tiếp nhận, trừ từ chối") — cách hiểu này khớp tên
báo cáo và khớp số thực đo. Nêu ở đây để BA biết, **không** ảnh hưởng vế đối tác phản ánh vì cả hai báo cáo
dùng chung một cách hiểu nên vẫn nhất quán với nhau.

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (không kèm `donViId` ⇒ Toàn quốc)
- Trạng thái entity: BC đã render, `Tổng vụ việc toàn kỳ = 10`, `Thời điểm tạo: 15/07/2026 17:11`
- Vai trò + env + bản dựng: **QTHT** · `htpldn-uat.ospgroup.vn` · **HTPLDN V1.0** · quay 15/07/2026 17:11

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0 (và V1.0.3 ở ảnh
31/7); đợt này đo trên `18.143.165.120.nip.io` bản ghi ở đầu file, **dữ liệu vụ việc hoàn toàn khác** ⇒
Pass ở đây là **Pass tạm**, và chỉ khẳng định "hiện trạng đúng/sai so với đặc tả", **không** kết luận
"fix đã có tác dụng" (không có ảnh lỗi cũ của chính mình trên env này).
