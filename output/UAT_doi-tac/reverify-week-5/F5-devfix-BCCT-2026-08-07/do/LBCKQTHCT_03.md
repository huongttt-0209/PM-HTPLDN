# Phép đo — LBCKQTHCT_03 (dòng 336) · 2026-08-07 — Biểu mẫu **21a**

**Verdict logic: PASS** — 2/2 vế `MATCH` đều ĐẠT trên 2 đợt khác nhau, cả 2 đường đo.
Lỗi đối tác báo (*"thiếu cột Số liệu kỳ trước, Ghi chú"*) **không tái hiện**.

Chuẩn chấm: [`../chuan/LBCKQTHCT_03.md`](../chuan/LBCKQTHCT_03.md) · Chuẩn bị chung: [`../chuan/00-CHUAN-BI-CHUNG.md`](../chuan/00-CHUAN-BI-CHUNG.md)

---

## 1. Sửa Scope Lock trước khi đo — bỏ "C3" khỏi danh sách vế

File chuẩn chấm khóa 3 vế; **chỉ C1 + C2 là vế hợp lệ**. "C3" (điều kiện hiển thị ngoài `DANG_LAP_BC`)
**bị loại khỏi danh sách vế**, không phải vì kết quả đo, mà vì **luật khóa 1 của Flow 04**:

> *"Vai trò, trạng thái hoặc dữ liệu mà SRS quy định để vế đó có hiệu lực phải được dùng làm **tiền đề**,
> không tách thành bug mới."*

Chính file chuẩn chấm cũng tự chú *"không phải claim của đối tác"*. ⇒ `dot o DANG_LAP_BC` là **tiền đề**, không phải vế.

**Quyết định này đối xứng, không phải bẻ luật cho hợp kết quả:** nếu đo ra **thiếu** cột ở trạng thái này thì
theo §7 chuẩn chấm cũng **không được chấm FAIL** (ô TRỐNG + nêu blocker). Sự bất đối xứng nằm ở logic, không ở luật:
**vắng mặt** ở trạng thái SRS không yêu cầu thì không chứng minh được gì, còn **có mặt** thì chứng minh
thành phần tồn tại và đủ cột. Đối tác khiếu nại *"hệ thống hiển thị thiếu cột"* — đo được là có, claim bị bác.

| Vế | Expected đối tác | SRS | Quan hệ | Route |
|---|---|---|---|---|
| **C1** | Bảng 21a cho cán bộ thấy **số liệu kỳ trước** theo từng chỉ tiêu | `srs-fr-15-ct-htpldn.md:1167` | MATCH | TEST |
| **C2** | Bảng 21a có **chỗ ghi chú** theo từng chỉ tiêu | `srs-fr-15-ct-htpldn.md:1167` | MATCH | TEST |

`:1167` nguyên văn ô "Dữ liệu/Nội dung": `Chi tieu / So lieu ky truoc / Ky nay / Ghi chu. Goi y so lieu tu HT…`

---

## 2. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` |
| 🔴 Bản dựng | **`assets/index-D4Buvu4S.js`** · `index.html` Last-Modified `Thu, 06 Aug 2026 19:23:01 GMT` = **07/08/2026 02:23 VN** |
| ⚠️ Đổi bản dựng giữa lô | Case 1 đo trên `index-DsMHK7Dp.js` (01:51 VN). **Env đã triển khai lại lúc ~02:23 VN**, giữa case 1 và case 2. Đã tải lại bằng địa chỉ + đọc lại tên bó mã ngay trong tab trước khi đo (bẫy 7). Nhãn sidebar vẫn `HTPLDN · V1.0.9` ⇒ **nhãn phiên bản KHÔNG phân biệt được 2 bản dựng này** |
| Tài khoản | `cbnv_hn` — CB_NV_DP, cấp ĐP, Sở Tư pháp Hà Nội (`donViId …8002-000000000001`), userId `87bb5785` — xác thực lại bằng `GET /api/v1/auth/me` → 200 |
| Vai trò hợp lệ? | ✅ `:712` yêu cầu **CB NV cấp ĐP/BN** — đúng vai trò, đúng cấp |
| Đợt đo #1 | `DOT-SO_BO_NAM-2026-1` (`e9909d96…`) — `bieuMauSuDung = MAU_21A`, **có dữ liệu thật** |
| Đợt đo #2 | `DOT-SO_BO_6_THANG-2026-1` (`a61e07f1…`) — `MAU_21A`, **rỗng hoàn toàn** (`baoCaoId = null`) |
| Đã seed gì cho case này | **Không.** Dùng lại đúng bản ghi case 1 để lại + 1 đợt nguyên trạng |

---

## 3. Kết quả — 2 đường đo × 2 đợt

### 3.1 Đường 1 — giao diện (`innerText`, không `textContent`)

| Đợt | `trangThai` ĐỢT | `trangThaiNop` ĐƠN VỊ | Chế độ | Số cột | **Tiêu đề cột đọc được** | Số dòng chỉ tiêu |
|---|---|---|---|---|---|---|
| `DOT-SO_BO_NAM-2026-1` | `TAO_DOT` | `DANG_LAP` | Nhập (15 ô input) | **4** | `Chỉ tiêu` · **`Số liệu kỳ trước`** · `Kỳ này` · **`Ghi chú`** | 13 |
| `DOT-SO_BO_6_THANG-2026-1` | `TAO_DOT` | `CHUA_NOP` | **Chỉ đọc (0 ô input)** | **4** | `Chỉ tiêu` · **`Số liệu kỳ trước`** · `Kỳ này` · **`Ghi chú`** | 13 |

- 13 dòng chỉ tiêu khớp `:802` (*BA chốt 2026-08-06 — MAU_21A → 13 chỉ tiêu*). (`tbody` đếm 14 dòng vì
  có 1 dòng tiêu đề dính (sticky) lặp lại trong `tbody` — **không phải chỉ tiêu thứ 14**.)
- Kiểm cuộn ngang (bẫy 2): `scrollWidth 1009` vs `clientWidth 1005` — lệch 4px, **không cột nào bị giấu**;
  cả 4 tiêu đề đã đọc được trực tiếp.
- Ảnh: [`../image/LBCKQTHCT_03-21a-du-4-cot-dot2.png`](../image/LBCKQTHCT_03-21a-du-4-cot-dot2.png) ·
  [`../image/LBCKQTHCT_03-21a-du-4-cot-dot3-chidoc.png`](../image/LBCKQTHCT_03-21a-du-4-cot-dot3-chidoc.png)

### 3.2 Đường 2 — dữ liệu nguồn (`GET /api/v1/dot-bao-caos/{id}`, cùng phiên `cbnv_hn`)

- Khóa cấp cao nhất **có `soLieuKyTruoc`** (giá trị `null` ở cả 2 đợt — chưa có kỳ trước).
- `soLieuTongHop` (đợt #1) chứa khóa **`ghiChu`**: `{"soTvvKienToan": "QA-BCCT-20260807-0209-ghichu-ct1"}`
  — đúng giá trị đã nhập ở case 1, tức **ô Ghi chú là trường thật, lưu được và đọc lại được theo từng chỉ tiêu**.

### 3.3 Vế C1 — ĐẠT

Cột **"Số liệu kỳ trước"** hiện ở **cả 2 đợt, cả 2 chế độ**, hiển thị dấu **`—`** cho mọi chỉ tiêu vì
`soLieuKyTruoc = null` (chưa có kỳ báo cáo trước).

> 🟢 **Bẫy 10 bị vô hiệu bằng số, không bằng suy đoán.** Giả thuyết "cột bị ẩn vì rỗng" **sai**: dữ liệu
> nguồn `null` mà cột **vẫn hiện** kèm ô giữ chỗ `—`. Không cần seed kỳ trước để kết luận.

### 3.4 Vế C2 — ĐẠT

Cột **"Ghi chú"** hiện ở cả 2 đợt. Ở chế độ nhập, **mỗi dòng chỉ tiêu có đúng 1 ô Ghi chú riêng**
(13 ô + 2 ô số liệu chỉ tiêu 12/13 = 15 ô toàn bảng). Ô của chỉ tiêu 1 đang giữ đúng giá trị đã lưu.

> ⚠️ **Suýt chấm oan — ghi lại để lần sau không mắc.** Đọc `innerText` của ô Ghi chú trả về **chuỗi rỗng**
> ở mọi dòng, kể cả dòng đã có ghi chú. Nguyên nhân: giá trị nằm trong thuộc tính `value` của ô nhập,
> **`innerText` không bao giờ đọc được**. Nếu chỉ nhìn `innerText` sẽ kết luận sai *"ghi chú không lưu"*.
> Đã đọc `.value` + đối chiếu dữ liệu nguồn ⇒ **hai đường khớp**.

---

## 4. Tiền đề KHÔNG thỏa được — phải khai, nhưng không đổi verdict

`:1167` ràng buộc hiển thị *"khi bieu mau ap dung va **dot o DANG_LAP_BC**"*. Env **không có đợt nào**
ở `DANG_LAP_BC`: cả 3 đợt đều `TAO_DOT`, **kể cả đợt `DOT-THBC01-UAT` đã có đơn vị `DA_NOP` (nộp xong)**.

Bảng 21a vẫn hiển thị đầy đủ ở `TAO_DOT` ⇒ **phần mềm gác hiển thị theo trục ĐƠN VỊ (`trangThaiNop`),
không theo trục ĐỢT (`trangThai`)** như chữ `:1167`. Việc này **không kéo verdict case này** (xem §1),
nhưng là dữ kiện thật, đã ghi lại và sẽ xử đúng chỗ ở phiếu **TPDBCKQTHCT_01** — phiếu duy nhất trong lô
có expected nhắm thẳng trục ĐỢT.

---

## 5. Quan sát ngoài vế — chỉ ghi nhận, KHÔNG đổi verdict, KHÔNG suy cho case khác

| # | Quan sát | Xử lý |
|---|---|---|
| 1 | Ở `CHUA_NOP` bảng 21a hiển thị **chỉ đọc** (0 ô nhập, chỉ có nút [Lập báo cáo]); ở `DANG_LAP` mới thành bảng nhập | Ghi nhận. **Liên quan trực tiếp LBCKQTHCT_05/06** nhưng **CẤM suy chéo** (bẫy 6) — 2 case đó phải tự đo dưới chuẩn chấm riêng |
| 2 | Có **2 nút [Lưu nháp]** trên màn (thẻ biểu mẫu + thẻ nhận xét) | Đã ghi ở case 1, không lặp lại thành bug mới |
| 3 | Chỉ tiêu 1–11 hiển thị `0 (HT)` do hệ thống tự tính, chỉ 12–13 nhập tay | Khớp `:743` (gợi ý số liệu từ HT). Không thuộc vế |

**Không** phát hiện tràn/đè hay lẫn tiếng Anh trong bảng 21a ⇒ không phát sinh bug tình cờ ở case này.

---

## 6. Giới hạn hiệu lực

Verdict chỉ có hiệu lực cho `18.143.165.120.nip.io` + bó mã **`index-D4Buvu4S.js`** (07/08/2026 02:23 VN).
Bằng chứng gốc của đối tác quay trên môi trường khác, trên bản ghi `DOT-SO_BO_NAM-2026-2` (`9ef97e44…`)
**hiện không còn tồn tại**, vai trò `CB_NV_BN`; video `LBCKQTHCT_03.webm` lại quay màn **21b** trong khi
phiếu này soi **21a**.
