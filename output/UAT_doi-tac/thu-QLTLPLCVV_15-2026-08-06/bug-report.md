# Bug Report — Tư vấn chuyên sâu / Tư liệu pháp lý liên kết (QLTLPLCVV)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — UAT đối tác |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **HTPLDN V1.0.8** (`assets/index-CNwX9JjX.js`) |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-08-06 11:32:00 |
| **Loại test** | Re-verify sau Dev fix (Negative — tải tệp chứa mã độc) |
| **Round** | Verify bug dev fix 2026-08-06 |
| **Tài liệu tham chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` · file tiêu chí `tieuchi/QLTLPLCVV_15.md` |

---

## Tổng hợp

Re-verify **1** case đối tác báo (QLTLPLCVV_15). Kết quả: **hết lỗi** trên môi trường + bản dựng ghi ở
trên → bug đóng ngay trong đợt này. Không phát hiện lỗi mới cần mở phiếu.

Có **1 ghi nhận ngoài phạm vi** (thông báo phía máy chủ khi tệp vượt 20MB) — giao diện và máy chủ lệch
nhau nên chuyển thành câu hỏi cho BA ở [`cau-hoi-BA.md`](cau-hoi-BA.md), **không** mở phiếu lỗi và
**không** ảnh hưởng verdict của case.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 0     | 0      | 1     | 0       | 1      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-QLTLPLCVV-015~~ | Minor | P2 | Negative | QLTLPLCVV_15 (tab `bug` dòng 299) | `srs-fr-12-tv-chuyen-sau.md:872` (Tải lên file — bước 3 Quét virus) · `:969` (E4 `ERR-TLPL-04`) | Tải tệp chứa mã độc chỉ báo chung chung "Tải file thất bại", không nêu tệp chứa mã độc | Closed |

---

## ~~BUG-QLTLPLCVV-015~~ [CLOSED] — Tải tệp chứa mã độc chỉ báo chung chung "Tải file thất bại", không nêu tệp chứa mã độc

> **Re-test:** 2026-08-06 11:32 — ✅ PASS trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**. Tệp PDF hợp lệ
> nhúng chữ ký thử EICAR bị từ chối kèm thông báo `Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc,
> không thể tải lên`; tệp sạch vẫn đính kèm được; tệp vượt 20MB báo bằng câu khác hẳn ⇒ chặn đúng ở bước
> quét virus. N = 1 tư liệu · M = 3 dạng tệp · dữ liệu seed: 1 tư liệu Nháp mới tạo (id `18183dfb-…`).
> **Pass tạm** cho tới khi bản dựng này lên môi trường của đối tác.

### Mô tả

Trong cửa sổ chỉnh sửa tư liệu pháp lý của một nội dung tư vấn chuyên sâu, vai trò CB Nghiệp vụ Trung
ương tải lên một tệp chứa mã độc. Hệ thống có chặn tệp, nhưng chỉ báo một câu chung chung
*"Tải file thất bại"* — người dùng không biết tệp bị từ chối vì chứa mã độc hay vì lý do khác (sai định
dạng, quá dung lượng, lỗi mạng). Đặc tả quy định bước "Quét virus" là một bước riêng trong luồng tải
tệp và có phản hồi lỗi riêng cho tình huống tệp chứa mã độc.

### Các bước tái hiện

1. Đăng nhập vai trò **CB Nghiệp vụ Trung ương** (`cbnv_tw`, `CB_NV_TW`, cấp TW — vai trò được đặc tả
   cho phép Thêm/Sửa/Xóa tư liệu pháp lý theo `srs-fr-12-tv-chuyen-sau.md:853`).
2. Vào **Tư vấn → Tư vấn chuyên sâu**, mở **Xem chi tiết** một nội dung tư vấn.
3. Mở nhóm **"Tư liệu pháp lý liên kết"**, bấm **[Sửa]** trên một tư liệu ở trạng thái **Nháp**
   (tư liệu đã công khai bị chặn sửa theo `:902`, không dùng được).
4. Ở widget **"File đính kèm"**, chọn một tệp PDF **hợp lệ** có nhúng chữ ký thử mã độc chuẩn EICAR
   (bắt buộc là PDF hợp lệ — tệp EICAR thô đổi đuôi `.pdf` có thể bị chặn ở cổng định dạng trước đó).
5. Quan sát thông báo hệ thống trả về, rồi đóng và mở lại tư liệu để kiểm tra danh sách đính kèm.

### Kết quả mong đợi

- Theo `srs-fr-12-tv-chuyen-sau.md:872`, luồng "Tải lên file" có bước 3 là **Quét virus** — tách bạch với
  bước 2 kiểm dung lượng/định dạng.
- Theo `srs-fr-12-tv-chuyen-sau.md:969`, khi tệp chứa mã độc, hệ thống phải phản hồi bằng **thông báo
  riêng nêu rõ tệp chứa mã độc và kèm tên tệp** — không dùng chung câu lỗi tải tệp thất bại.
- Tệp chứa mã độc không được đính kèm vào tư liệu; tệp sạch vẫn phải tải lên bình thường.

### Kết quả thực tế

**Trước khi sửa** (đối tác ghi nhận 17/07/2026, môi trường `htpldn-uat.ospgroup.vn`): hệ thống chặn tệp
nhưng chỉ hiển thị *"Tải file thất bại"*.

**Đo lại 2026-08-06 trên `18.143.165.120.nip.io`, bản dựng V1.0.8 — đã đúng đặc tả:**

- Tệp PDF hợp lệ nhúng EICAR → bị từ chối, thông báo:
  `Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc, không thể tải lên`
  (1 request ↔ 1 khung thông báo; máy chủ trả HTTP 400 `ERR-TLPL-04` cùng nguyên văn câu đó).
- Tệp PDF sạch → tải lên bình thường, không có thông báo lỗi, máy chủ trả 201 `trangThaiQuet: "SACH"`.
- Tệp PDF sạch vượt 20MB → thông báo `Kích thước vượt quá giới hạn 20MB.` — **khác hẳn** câu của tệp mã
  độc, chứng minh tệp mã độc bị chặn ở **bước quét virus** chứ không phải bộ lọc dung lượng/định dạng.
- Sau khi bấm Lưu và **tải lại trang**: cột File = 1, đọc lại bản ghi `files = [B-pdf-sach.pdf]` — tệp mã
  độc không lọt vào bản ghi ở bất kỳ lớp nào.

### Bằng chứng

![BUG-QLTLPLCVV-015 — cửa sổ Sửa tư liệu ngay sau khi tệp chứa mã độc bị từ chối: widget "File đính kèm" chỉ còn B-pdf-sach.pdf (594 B), tệp mã độc không được thêm vào](image/A-01-widget-sau-khi-A-bi-tu-choi-chi-con-B.png)

![BUG-QLTLPLCVV-015 — sau khi Lưu và tải lại trang, mở lại cửa sổ Sửa: danh sách đính kèm vẫn chỉ có B-pdf-sach.pdf](image/A-03-mo-lai-sau-reload-chi-con-tep-sach.png)

Nguyên văn thông báo + phản hồi máy chủ của cả 3 dạng tệp (và 4 lượt đo bằng đường thứ hai):
[`image/A-02-thong-bao-va-phan-hoi-may-chu.txt`](image/A-02-thong-bao-va-phan-hoi-may-chu.txt).

> **Vì sao thông báo không nằm trong ảnh:** công cụ chụp màn hình đang dùng không bắt được lớp thông báo
> của thư viện giao diện (đã thử 4 lượt, gồm cả hẹn giờ thao tác trước rồi mới chụp và lặp thao tác 25
> lượt × 2 giây). Đã đo trực tiếp trên DOM để chứng minh khung thông báo **có hiển thị thật** với người
> dùng: `position: fixed`, `top: 8px`, khung `x=0 y=8 w=1440 h=56`, `opacity: 1`, `z-index: 2010`, sống
> **3,34 giây**. Chữ được đọc bằng `innerText` (chỉ chữ người dùng nhìn thấy) và trùng khớp từng ký tự
> với `error.message` trong phản hồi máy chủ.

Phản hồi máy chủ khi tải tệp chứa mã độc:

```json
{
  "success": false,
  "error": {
    "code": "ERR-TLPL-04",
    "message": "Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc, không thể tải lên",
    "timestamp": "2026-08-06T04:23:28.987Z",
    "requestId": "5e569e13-d8b7-496d-82c2-68aaa724b975"
  }
}
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io |
| OTP login | Lấy từ MailHog (không có mã bypass trên môi trường này) |
| MailHog (OTP inbox) | http://18.143.165.120:8025 |
| API base | https://18.143.165.120.nip.io/api/v1 |
| Frontend | React + Vite + Ant Design (bó mã `assets/index-CNwX9JjX.js`) |
| Xác thực | JWT trong cookie + OTP qua email |
| Tool test | Chrome DevTools MCP · bộ bắt thông báo dùng chung `tools/toast-capture.js` |

---

*Bug report generated: 2026-08-06 11:32:00 | QA Automation via Claude Code*

---
---

# Phần 2 — Batch B4 (Báo cáo Chương trình HTPLDN)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — UAT đối tác |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **HTPLDN V1.0.8**; bó mã giao diện `assets/index-CNwX9JjX.js` cho SLCTHT_06 + CTTLV_05, đổi sang `assets/index-DIABnbIr.js` từ ~14:22 (chuỗi phiên bản không đổi) cho CTTTG_04 |
| **Người test** | QA Automation via Claude Code |
| **Ngày** | 2026-08-06 14:38:00 |
| **Loại test** | Re-verify sau Dev fix (Xuất tệp báo cáo thống kê + phân quyền vai trò) |
| **Round** | Verify bug dev fix 2026-08-06 |
| **Tài liệu tham chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` · file tiêu chí [`tieuchi/SLCTHT_06.md`](tieuchi/SLCTHT_06.md) · [`tieuchi/CTTLV_05.md`](tieuchi/CTTLV_05.md) · [`tieuchi/CTTTG_04.md`](tieuchi/CTTTG_04.md) |

## Tổng hợp

Re-verify 3 case cùng màn *Báo cáo thống kê*: **SLCTHT_06** (BC Số lượng chương trình hỗ trợ,
FR-IX-20/UC143), **CTTLV_05** (BC Chương trình theo lĩnh vực, FR-IX-22/UC145) và **CTTTG_04**
(BC Chương trình theo thời gian, FR-IX-23/UC146).
Kết quả cả ba: **còn lỗi một phần** ⇒ chuyển lại dev. Vai trò đặc tả (CB Nghiệp vụ Trung ương) xuất tệp
bình thường và nội dung tệp đúng đặc tả; nhưng chính vai trò **QTHT** mà đối tác dùng vẫn bị chặn ở
bước xuất, kèm thông báo là chuỗi tiếng Anh thô *"Forbidden"*.

Ghi nhận ngoài phạm vi, **không** ảnh hưởng verdict của case nào:
(1) bộ lọc *Trạng thái chương trình* có thêm giá trị *"Đã phê duyệt"* so với tập giá trị ở
`srs-fr-11-bao-cao.md:897` — đặc tả tự mâu thuẫn với `:82`, đã chuyển thành câu hỏi cho BA ở
[`cau-hoi-BA.md`](cau-hoi-BA.md), **không** mở phiếu lỗi.
(2) trên màn *BC Chương trình theo lĩnh vực*: sau khi **xuất tệp thành công một lần**, lần bấm
[Xem báo cáo] **kế tiếp** làm nút [Xuất Excel] / [Xuất PDF] **bị khoá và giữ nguyên tới khi tải lại
trang**, dù báo cáo trên màn vẫn đủ dữ liệu (trái `:1052`) ⇒ mỗi lần tải trang chỉ xuất được 1 tệp.
Đo lại 2026-08-06 14:52–15:01 sau khi tải lại trang: bộ lọc *Lĩnh vực* **không** liên quan (mô tả
ban đầu quy sai cho thao tác xoá bộ lọc). Gọi thẳng máy chủ đúng lúc nút khoá, cùng bộ tiêu chí →
**200 + tệp .xlsx hợp lệ, nội dung khớp màn** ⇒ **lỗi phía giao diện**, không phải máy chủ từ chối.
**Chưa mở phiếu** vì bug ngoài phạm vi cần mở dòng mới trên bảng theo dõi phải được duyệt mã trước;
chi tiết ở [`tieuchi/CTTLV_05.md`](tieuchi/CTTLV_05.md) mục 7.
(3) trên màn *BC Chương trình theo thời gian*: báo cáo **vẫn thống kê "Số DN"** (thẻ · chú giải biểu đồ ·
cột bảng · khối và cột trong tệp xuất) dù `srs-fr-11-bao-cao.md:1018` đã chốt ngày 2026-07-24 **bỏ**
`so_dn`; và **không cấu hình nào trên màn cho ra biểu đồ trend nhiều điểm** nên AC `:1023` (*"chọn 12
tháng → hiển thị biểu đồ trend"*) không với tới được bằng giao diện, dù máy chủ làm được. Cả hai
**chưa mở phiếu**, cùng lý do như (2); chi tiết ở [`tieuchi/CTTTG_04.md`](tieuchi/CTTTG_04.md) mục 7.
(4) thẻ *Tổng ngân sách toàn kỳ* trên cùng màn đó — đặc tả im lặng ⇒ đã thêm mục hỏi BA, không mở phiếu.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 3    | 0        | 3     | 0      | 0     | 0       | 0      | 3    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| BUG-SLCTHT-006 | Major | P1 | Permission | SLCTHT_06 (tab `bug` dòng 267) | `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`) · `:79` (Processing bước 1) · `:1268` (BR-AUTH-08, ngoại lệ "QTHT bypass") | Vai trò QTHT xem được báo cáo nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden" | Open |
| BUG-CTTLV-005 | Major | P1 | Permission | CTTLV_05 (tab `bug` dòng 277) | `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`) · `:79` (Processing bước 1) · `:1268` (BR-AUTH-08, ngoại lệ "QTHT bypass") | Vai trò QTHT xem được BC Chương trình theo lĩnh vực nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden" | Open |
| BUG-CTTTG-004 | Major | P1 | Permission | CTTTG_04 (tab `bug` dòng 281) | `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`) · `:79` (Processing bước 1) · `:1268` (BR-AUTH-08, ngoại lệ "QTHT bypass") | Vai trò QTHT xem được BC Chương trình theo thời gian nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden" | Open |

> ⚠️ **Batch B4 có 4 case, phiếu nằm ở 2 chỗ.** Ba phiếu trên ở Phần 2 này; phiếu thứ tư
> **`BUG-CTTDVQL-004`** (case `CTTDVQL_04`, tab `bug` dòng 272) nằm ở [Phần 5](#phần-5--batch-b4-bc-chương-trình-theo-đơn-vị)
> — lúc đó file đang được nhiều phiên cùng ghi nên phiếu đó lỡ mở thành Phần riêng.
> Đếm đủ B4 phải cộng cả 4; bảng Severity của Phần 2 chỉ đếm 3 phiếu trong Phần 2.

---

## BUG-SLCTHT-006 — Vai trò QTHT xem được báo cáo nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 12:33 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vai trò CB Nghiệp vụ Trung ương xuất Excel bình thường (tệp `BaoCaoSoLuongCtHoTro_20260806_1224.xlsx`,
> nội dung khớp màn, áp đúng bộ lọc). Vai trò QTHT — đúng vai trò đối tác dùng — **xem** được báo cáo
> (7/1/1) nhưng **xuất** thì bị từ chối kèm chữ *"Forbidden"*. N = 7 chương trình · M = 3 dạng bộ lọc
> (+1 nhánh phụ) · **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Số lượng chương trình hỗ trợ**, người dùng vai trò **Quản
trị hệ thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu, nhưng bấm tiếp [Xuất Excel]
thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** — một chuỗi
tiếng Anh thô, không cho biết chuyện gì đã xảy ra. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ
Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, `vaiTro = ["QTHT"]`, `capDonVi = TW`,
   đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*) — đây đúng là vai trò trên bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Số lượng chương trình hỗ trợ**; *Kỳ báo cáo* = **Năm**
   (tự điền 01/01/2026 → 31/12/2026); *Đơn vị* = **Toàn quốc**; *Trạng thái chương trình* để trống.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng chương trình 7 · Đang thực hiện 1 ·
   Hoàn thành 1 + bảng theo đơn vị + biểu đồ), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_04`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117`, khi hệ thống từ chối vì người dùng không có quyền thì phải cho người
  dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ thuật
  tiếng Anh ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo
  đơn vị"*), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng. Nếu vai trò này thật sự không được
  phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không phải cho xem đầy đủ số liệu rồi mới
  chặn ở bước xuất — hai bước phải nhất quán với nhau.
- `srs-fr-11-bao-cao.md:1268` (BR-AUTH-08) ghi ngoại lệ **"QTHT bypass"** cho toàn bộ nhóm FR-IX, tức
  đặc tả có tính đến việc vai trò QTHT chạm vào báo cáo.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 12:32:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/so-luong-ct-ho-tro?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ 7 · 1 · 1 + bảng theo đơn vị + 2 biểu đồ, **0 thông báo**.
- [Xuất Excel]: **1** request `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (1 mốc giờ,
  không double-toast); chữ người dùng đọc được: **"Forbidden"**; **0 tệp** được giao.
  Khung thông báo hiển thị thật: `position: fixed`, khung `w=1432 h=41`, sống **≥ 3,241 giây**.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_04`) — cùng bộ lọc, 2026-08-06 12:24:**

- [Xuất Excel]: 1 request `POST /api/v1/bao-cao/export` → **200**; chữ **"Đang tạo file..." → "Tạo file
  thành công."**; tệp `BaoCaoSoLuongCtHoTro_20260806_1224.xlsx` (6.959 byte, zip thật, mở được bằng
  `openpyxl`). Nội dung tệp: phần đầu có tiêu đề BC + kỳ + khoảng thời gian + đơn vị + ngày tạo; số liệu
  A8=7 / A12=1 / A16=1 khớp đúng 3 thẻ trên màn; bảng *Theo đơn vị* và *Theo kỳ* khớp màn; đổi bộ lọc thì
  nội dung tệp đổi theo (lọc *Hoàn thành* → 1/0/1).

⇒ Câu *"Không thể tạo file xuất. Vui lòng thử lại."* của vòng 1 **không còn tái hiện**; câu **"Forbidden"**
của vòng 2 **vẫn tái hiện nguyên vẹn** ở đúng vai trò đối tác dùng.

### Bằng chứng

![BUG-SLCTHT-006 — vai trò QTHT ("Quản trị hệ thống", avatar QT, BTP · TW) trên màn Báo cáo thống kê, bản dựng V1.0.8: bộ lọc trùng khít ảnh đối tác (BC Số lượng chương trình hỗ trợ · Năm · 01/01/2026–31/12/2026 · Toàn quốc · trạng thái để trống) và báo cáo ĐÃ XEM ĐƯỢC đầy đủ — Tổng 7 · Đang thực hiện 1 · Hoàn thành 1, thời điểm tạo 06/08/2026 12:32; đây là trạng thái ngay tại thao tác bấm [Xuất Excel] bị từ chối](image/SLCTHT_06-B1-qtht-forbidden-khi-xuat-excel-V108.png)

![BUG-SLCTHT-006 — đối chứng vai trò CB Nghiệp vụ Trung ương #04 (`cbnv_tw_04`), cùng bộ lọc, bản dựng V1.0.8: kết quả 7 · 1 · 1, thời điểm tạo 06/08/2026 12:24; ngay sau khi bấm [Xuất Excel] KHÔNG có thông báo đỏ nào ở đúng vị trí mà 2 ảnh của đối tác hiện "Không thể tạo file xuất. Vui lòng thử lại." và "Forbidden"](image/SLCTHT_06-A1-dang1-ngay-sau-bam-xuat-excel-V108.png)

![BUG-SLCTHT-006 — cùng nhánh CB Nghiệp vụ Trung ương, lượt chụp thứ 3 (bấm nút rồi chụp ngay): màn giữ nguyên bộ lọc dạng ① và kết quả 7 · 1 · 1 (thời điểm tạo 06/08/2026 12:29), không có thông báo lỗi nào sau thao tác xuất tệp. Ảnh KHÔNG bắt được lớp thông báo — xem ghi chú ngay dưới](image/SLCTHT_06-A3-dang1-luot-chup-thu-3-khong-bat-duoc-thong-bao-V108.png)

Nguyên văn thông báo trên màn + phản hồi máy chủ + nội dung 3 tệp xuất của cả 2 nhánh:
[`image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt`](image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt).
Tệp xuất thật đã tải về để đọc nội dung: `testfiles/slctht06-dang1.xlsx` (dạng ①),
`testfiles/slctht06-dang3.xlsx` (lọc *Hoàn thành*), `testfiles/slctht06-dang2.xlsx` (lọc đơn vị).

> **Vì sao chữ "Forbidden" không nằm trong ảnh:** công cụ chụp màn hình đang dùng không bắt được lớp
> thông báo do thư viện giao diện dựng qua portal (đã thử **4 lượt**: chụp ngay sau khi bấm · hẹn giờ bấm
> sau 2500ms rồi mới chụp · hẹn giờ 1500ms · bấm bằng lệnh rồi chụp ngay) — cùng hạn chế đã ghi nhận ở
> BUG-QLTLPLCVV-015 phần 1. Bằng chứng thay thế = chữ đọc bằng `innerText` (chỉ chữ người dùng nhìn thấy)
> + số đo chứng minh khung thông báo hiển thị thật + nguyên văn phản hồi máy chủ ngay dưới đây.
> Ảnh của lượt chụp thứ 2 (hẹn giờ bấm sau 2500ms rồi mới chụp) —
> [`image/SLCTHT_06-A2-dang1-luot-chup-thu-2-khong-bat-duoc-thong-bao-V108.png`](image/SLCTHT_06-A2-dang1-luot-chup-thu-2-khong-bat-duoc-thong-bao-V108.png):
> cùng bộ lọc dạng ①, kết quả 7 · 1 · 1, thời điểm tạo 06/08/2026 12:29, cũng không bắt được lớp thông báo.

Phản hồi máy chủ khi vai trò QTHT bấm [Xuất Excel]:

```json
{
  "success": false,
  "error": {
    "code": "ERR-PERM-SYS-00-01",
    "message": "Forbidden",
    "timestamp": "2026-08-06T05:32:36.886Z",
    "requestId": "08e57ea9-1b56-4c28-9fe0-70a05ad37850"
  }
}
```

Thân yêu cầu đã gửi (giống hệt nhánh CB Nghiệp vụ, chỉ khác phiên đăng nhập):

```json
{"loaiBaoCao":"BC_SO_LUONG_CT_HO_TRO","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
```

### So sánh (Comparison)

| Vai trò | Xem báo cáo | Xuất Excel | Chữ người dùng thấy khi xuất |
|---|---|---|---|
| CB Nghiệp vụ Trung ương (`cbnv_tw_04`) | ✅ 200 — hiện 7/1/1 | ✅ 200 — nhận tệp `.xlsx` đúng nội dung | "Đang tạo file..." → "Tạo file thành công." |
| Quản trị hệ thống / QTHT (`admin`) | ✅ 200 — hiện 7/1/1 | ❌ 403 — không có tệp | **"Forbidden"** (chuỗi tiếng Anh thô) |

### Cách verify sau khi fix

```
── CÁCH VERIFY sau Dev fix ──
CẦN CÓ TRƯỚC: tài khoản admin (Quản trị hệ thống, cấp TW); màn Báo cáo thống kê (/bao-cao);
  ≥1 chương trình HTPLDN đã duyệt / đang thực hiện / hoàn thành nằm trong năm 2026. Báo cáo
  trống thì phép thử không có giá trị — tạo chương trình mới ở màn Chương trình HTPLDN và đưa
  lên trạng thái đã duyệt trở đi.
Bước 1. Chọn loại báo cáo "BC Số lượng chương trình hỗ trợ", Kỳ "Năm", Đơn vị "Toàn quốc", để
  trống Trạng thái chương trình. Bấm [Xem báo cáo]. Ghi lại 3 số trên màn: Tổng chương trình /
  Đang thực hiện / Hoàn thành.
Bước 2. Bấm [Xuất Excel]. Chép lại NGUYÊN VĂN chữ hiện ra và kiểm có tệp về máy không.
Bước 3. Kiểm bằng đường thứ hai: mở tab Network xem lời gọi xuất báo cáo trả mã gì, thân phản
  hồi ghi gì. Có tệp thì MỞ TỆP RA ĐỌC, đối chiếu 3 số ở bước 1 với số trong tệp.
✅ ĐẠT khi một trong hai:
  · Vai trò Quản trị hệ thống bấm [Xuất Excel] thì nhận được tệp .xlsx mở đọc được, 3 số trong
    tệp khớp đúng 3 số trên màn, và không hiện thông báo từ chối nào.
  · Hoặc — nếu nghiệp vụ chốt vai trò này KHÔNG được xuất — hệ thống chặn ngay từ bước
    [Xem báo cáo], và chữ hiện ra là câu tiếng Việt cho người dùng biết họ không có quyền xem
    báo cáo này.
❌ CHƯA ĐẠT nếu: còn thấy "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào; hoặc vẫn
  cho Xem đủ số liệu rồi mới chặn ở bước Xuất. Đúng một nửa cũng tính là chưa đạt.
⚠️ 3 bẫy hay mắc khi đo:
  1. Chỉ thử bằng vai trò Cán bộ Nghiệp vụ rồi kết luận "đã fix". Vai trò đó vốn đã chạy tốt từ
     lượt đo 06/08/2026 — phép đo quyết định phải chạy bằng chính vai trò Quản trị hệ thống.
  2. Dừng ở "tải được tệp". Phải mở tệp ra đọc mới chốt được.
  3. Chấm hỏng vì tên sheet, thứ tự cột, màu sắc, dòng tổng cuối bảng hay tệp không nhúng biểu
     đồ — đặc tả không quy định những thứ đó (dòng 85, dòng 1092).
Ảnh lỗi lần này: image/SLCTHT_06-B1-qtht-forbidden-khi-xuat-excel-V108.png
  + nguyên văn phản hồi máy chủ ở image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho
vai trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không
đẩy nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt dứt điểm câu hỏi
"QTHT có được xuất báo cáo không" (đã nêu ở [`cau-hoi-BA.md`](cau-hoi-BA.md)) trước khi dev chọn hướng sửa.

---

## BUG-CTTLV-005 — Vai trò QTHT xem được BC Chương trình theo lĩnh vực nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:45 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**
> (`assets/index-CNwX9JjX.js`). Vai trò CB Nghiệp vụ Trung ương xuất Excel bình thường (tệp
> `BaoCaoCtTheoLinhVuc_20260806_1333.xlsx`, bảng hàng = lĩnh vực khớp từng hàng với màn, áp đúng bộ lọc).
> Vai trò QTHT — đúng vai trò đối tác dùng — **xem** được báo cáo (Tổng 7) nhưng **xuất** thì bị từ chối
> kèm chữ *"Forbidden"*. N = 7 chương trình trên 5 nhóm lĩnh vực · M = 3 dạng bộ lọc (+2 nhánh phụ) ·
> **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chương trình theo lĩnh vực**, người dùng vai trò **Quản
trị hệ thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu, nhưng bấm tiếp [Xuất Excel]
thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** — một chuỗi
tiếng Anh thô, không cho biết chuyện gì đã xảy ra. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ
Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, `vaiTro = ["QTHT"]`, `capDonVi = TW`,
   đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*) — đây đúng là vai trò trên cả 2 ảnh bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chương trình theo lĩnh vực**; *Kỳ báo cáo* = **Năm** (tự điền 01/01/2026 →
   31/12/2026); *Đơn vị* = **Toàn quốc**; *Lĩnh vực* để trống.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng chương trình 7 + bảng 5 hàng lĩnh vực +
   biểu đồ), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_04`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117`, khi hệ thống từ chối vì người dùng không có quyền thì phải cho người
  dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ thuật
  tiếng Anh ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo
  đơn vị"*), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng. Nếu vai trò này thật sự không được
  phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không phải cho xem đầy đủ số liệu rồi mới
  chặn ở bước xuất — hai bước phải nhất quán với nhau.
- `srs-fr-11-bao-cao.md:1268` (BR-AUTH-08) ghi ngoại lệ **"QTHT bypass"** cho toàn bộ nhóm FR-IX, tức
  đặc tả có tính đến việc vai trò QTHT chạm vào báo cáo.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 13:44–13:45:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/ct-theo-linh-vuc?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ Tổng chương trình 7 + bảng *Chưa phân loại 3 · Lao động 1 · Đất đai 1 · Thuế 1 ·
  Thương mại 1* + biểu đồ, **0 thông báo**.
- [Xuất Excel]: **1** request `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (1 mốc giờ,
  không double-toast); chữ người dùng đọc được đổi tại chỗ **"Đang tạo file..." → "Forbidden"**;
  **0 tệp** được giao. Khung thông báo hiển thị thật: `position: fixed`, rộng **1432 px**, cao 41–43 px.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_04`) — cùng bộ lọc, 2026-08-06 13:33:**

- [Xuất Excel]: 1 request `POST /api/v1/bao-cao/export` → **200**; chữ **"Đang tạo file..." → "Tạo file
  thành công."**; tệp `BaoCaoCtTheoLinhVuc_20260806_1333.xlsx` (6.674 byte, zip thật, mở được bằng
  `openpyxl`). Nội dung tệp: phần đầu có tiêu đề BC + kỳ + khoảng thời gian + đơn vị + ngày tạo; bảng
  *Lĩnh vực PL | Số chương trình* khớp **từng hàng** với màn và cộng dọc 3+1+1+1+1 = 7 = thẻ tổng; đổi
  bộ lọc thì nội dung tệp đổi theo (lọc *Lao động* → tổng 1, bảng chỉ còn 1 hàng).

⇒ Câu *"Không thể tạo file xuất. Vui lòng thử lại."* của vòng 1 **không còn tái hiện**; câu **"Forbidden"**
của vòng 2 **vẫn tái hiện nguyên vẹn** ở đúng vai trò đối tác dùng.

### Bằng chứng

![BUG-CTTLV-005 — vai trò QTHT ("Quản trị hệ thống", avatar QT, BTP · TW) trên màn Báo cáo thống kê, bản dựng V1.0.8: bộ lọc trùng khít ảnh đối tác (BC Chương trình theo lĩnh vực · Năm · 01/01/2026–31/12/2026 · Toàn quốc · Lĩnh vực để trống) và báo cáo ĐÃ XEM ĐƯỢC đầy đủ — Tổng chương trình 7, thời điểm tạo 06/08/2026 13:44; nút Xuất Excel đang bật, đây là trạng thái ngay trước thao tác bấm [Xuất Excel] bị từ chối](image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png)

![BUG-CTTLV-005 — cùng phiên QTHT, ngay sau khi bấm [Xuất Excel]: nút Xuất Excel đang được chọn (viền xanh), màn vẫn giữ báo cáo Tổng 7 và không có tệp nào về máy; ảnh KHÔNG bắt được lớp thông báo "Forbidden" — xem ghi chú ngay dưới](image/CTTLV_05-B2-qtht-ngay-sau-bam-xuat-excel-V108.png)

![BUG-CTTLV-005 — đối chứng vai trò CB Nghiệp vụ Trung ương #04 (`cbnv_tw_04`), cùng bộ lọc, bản dựng V1.0.8: kết quả Tổng chương trình 7, thời điểm tạo 06/08/2026 13:32; ngay sau khi bấm [Xuất Excel] KHÔNG có thông báo đỏ nào ở đúng vị trí mà 2 ảnh của đối tác hiện "Không thể tạo file xuất. Vui lòng thử lại." và "Forbidden"](image/CTTLV_05-A2-dang1-ngay-sau-bam-xuat-excel-V108.png)

Nguyên văn thông báo trên màn + phản hồi máy chủ + nội dung 4 tệp xuất của cả 2 nhánh:
[`image/CTTLV_05-thong-bao-va-phan-hoi-may-chu.txt`](image/CTTLV_05-thong-bao-va-phan-hoi-may-chu.txt).
Tệp xuất thật đã tải về để đọc nội dung: `testfiles/cttlv05-dang1.xlsx` (dạng ①),
`testfiles/cttlv05-dang2.xlsx` (lọc đơn vị BTP-TW), `testfiles/cttlv05-dang3.xlsx` (lọc lĩnh vực
*Lao động*), `testfiles/cttlv05-dang3b-datdai.xlsx` (lọc lĩnh vực *Đất đai*).

> **Vì sao chữ "Forbidden" không nằm trong ảnh:** công cụ chụp màn hình đang dùng không bắt được lớp
> thông báo do thư viện giao diện dựng qua portal (đã thử **3 lượt**: chụp ngay sau khi bấm · hẹn giờ bấm
> sau 2500 ms rồi mới chụp ở nhánh CB Nghiệp vụ · hẹn giờ 2500 ms ở nhánh QTHT; ảnh "ngay sau khi bấm" và
> ảnh "hẹn giờ" ra **byte giống hệt nhau**) — cùng hạn chế đã ghi nhận ở BUG-QLTLPLCVV-015 và
> BUG-SLCTHT-006. Bằng chứng thay thế = chữ đọc bằng `innerText` (chỉ chữ người dùng nhìn thấy) + số đo
> chứng minh khung thông báo hiển thị thật + nguyên văn phản hồi máy chủ ngay dưới đây.

Phản hồi máy chủ khi vai trò QTHT bấm [Xuất Excel]:

```json
{
  "success": false,
  "error": {
    "code": "ERR-PERM-SYS-00-01",
    "message": "Forbidden",
    "timestamp": "2026-08-06T06:45:02.556Z",
    "requestId": "d2432a2b-8188-4174-90e7-260149c6dfba"
  }
}
```

Thân yêu cầu đã gửi (giống hệt nhánh CB Nghiệp vụ, chỉ khác phiên đăng nhập):

```json
{"loaiBaoCao":"BC_CT_THEO_LINH_VUC","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
```

### So sánh (Comparison)

| Vai trò | Xem báo cáo | Xuất Excel | Chữ người dùng thấy khi xuất |
|---|---|---|---|
| CB Nghiệp vụ Trung ương (`cbnv_tw_04`) | ✅ 200 — hiện Tổng 7 + 5 hàng lĩnh vực | ✅ 200 — nhận tệp `.xlsx` đúng nội dung | "Đang tạo file..." → "Tạo file thành công." |
| Quản trị hệ thống / QTHT (`admin`) | ✅ 200 — hiện Tổng 7 + 5 hàng lĩnh vực | ❌ 403 — không có tệp | "Đang tạo file..." → **"Forbidden"** (chuỗi tiếng Anh thô) |

### Cách verify sau khi fix

```
── CÁCH VERIFY sau Dev fix ──
CẦN CÓ TRƯỚC: tài khoản admin (Quản trị hệ thống, cấp TW); màn Báo cáo thống kê (/bao-cao);
  ≥1 chương trình HTPLDN đã duyệt / đang thực hiện / hoàn thành nằm trong năm 2026, nên có
  chương trình thuộc ≥2 lĩnh vực khác nhau. Báo cáo trống thì phép thử không có giá trị — tạo
  chương trình mới ở màn Chương trình HTPLDN và đưa lên trạng thái đã duyệt trở đi.
Bước 1. Chọn loại báo cáo "BC Chương trình theo lĩnh vực", Kỳ "Năm", Đơn vị "Toàn quốc", để
  trống Lĩnh vực. Bấm [Xem báo cáo]. Ghi lại số Tổng chương trình và toàn bộ bảng (mỗi hàng:
  tên lĩnh vực + số chương trình).
Bước 2. Bấm [Xuất Excel]. Chép lại NGUYÊN VĂN chữ hiện ra và kiểm có tệp về máy không.
Bước 3. Kiểm bằng đường thứ hai: mở tab Network xem lời gọi xuất báo cáo trả mã gì, thân phản
  hồi ghi gì. Có tệp thì MỞ TỆP RA ĐỌC, đối chiếu số tổng và TỪNG HÀNG lĩnh vực ở bước 1 với
  số trong tệp, và kiểm cộng dọc các hàng bằng đúng số tổng.
✅ ĐẠT khi một trong hai:
  · Vai trò Quản trị hệ thống bấm [Xuất Excel] thì nhận được tệp .xlsx mở đọc được, bên trong
    có bảng mỗi hàng một lĩnh vực kèm số chương trình khớp đúng bảng trên màn, và không hiện
    thông báo từ chối nào.
  · Hoặc — nếu nghiệp vụ chốt vai trò này KHÔNG được xuất — hệ thống chặn ngay từ bước
    [Xem báo cáo], và chữ hiện ra là câu tiếng Việt cho người dùng biết họ không có quyền xem
    báo cáo này.
❌ CHƯA ĐẠT nếu: còn thấy "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào; hoặc vẫn
  cho Xem đủ số liệu rồi mới chặn ở bước Xuất. Đúng một nửa cũng tính là chưa đạt.
⚠️ 3 bẫy hay mắc khi đo:
  1. Chỉ thử bằng vai trò Cán bộ Nghiệp vụ rồi kết luận "đã fix". Vai trò đó vốn đã chạy tốt từ
     lượt đo 06/08/2026 — phép đo quyết định phải chạy bằng chính vai trò Quản trị hệ thống.
  2. Dừng ở "tải được tệp". Phải mở tệp ra đọc mới chốt được.
  3. Nút xuất xám vì đã xuất một lần trong lượt vào trang này (xem mục [7]), dễ tưởng nhầm là
     hệ thống chặn theo quyền. Tải lại trang rồi đo từ đầu.
⚠️ Đừng chấm hỏng vì tên sheet, thứ tự cột, thứ tự sắp xếp lĩnh vực, màu sắc, dòng tổng cuối
  bảng, tệp không nhúng biểu đồ, hay vì tên tệp không đúng chữ "BaoCaoChuongTrinh" — đặc tả
  không quy định những thứ đó. Xem mục [4].
Ảnh lỗi lần này: image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png
  + image/CTTLV_05-B2-qtht-ngay-sau-bam-xuat-excel-V108.png
  + nguyên văn phản hồi máy chủ ở image/CTTLV_05-thong-bao-va-phan-hoi-may-chu.txt
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho
vai trò QTHT trên loại BC này, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`.
**Dev FE** — không đẩy nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt dứt điểm
câu hỏi "QTHT có được xuất báo cáo không" (đã nêu ở [`cau-hoi-BA.md`](cau-hoi-BA.md) Mục 2) trước khi dev
chọn hướng sửa.

---

## BUG-CTTTG-004 — Vai trò QTHT xem được BC Chương trình theo thời gian nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 14:38 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**
> (`assets/index-DIABnbIr.js`). Vai trò CB Nghiệp vụ Trung ương xuất Excel bình thường (tệp
> `BaoCaoCtTheoThoiGian_20260806_1430.xlsx`, bảng *Theo kỳ* khớp từng hàng với màn, áp đúng bộ lọc).
> Vai trò QTHT — đúng vai trò đối tác dùng — **xem** được báo cáo (Tổng 6) nhưng **xuất** thì bị từ chối
> kèm chữ *"Forbidden"*. N = 6 chương trình trên 2 tháng · M = 3 dạng bộ lọc (+1 nhánh phụ) ·
> **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chương trình theo thời gian**, người dùng vai trò **Quản
trị hệ thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu, nhưng bấm tiếp [Xuất Excel]
thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** — một chuỗi
tiếng Anh thô, không cho biết chuyện gì đã xảy ra. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ
Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, `vaiTro = ["QTHT"]`, `capDonVi = TW`,
   đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*) — đây đúng là vai trò trên cả 2 ảnh bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chương trình theo thời gian**; *Kỳ báo cáo* = **Năm** (hệ thống tự điền
   01/01/2026 → 31/12/2026); *Đơn vị* = **Toàn quốc**. Màn này không có ô lọc đặc thù nào khác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng chương trình toàn kỳ 6 + biểu đồ đường +
   bảng *Theo kỳ*), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_04`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117`, khi hệ thống từ chối vì người dùng không có quyền thì phải cho người
  dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ thuật
  tiếng Anh ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo
  đơn vị"*), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng. Nếu vai trò này thật sự không được
  phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không phải cho xem đầy đủ số liệu rồi mới
  chặn ở bước xuất — hai bước phải nhất quán với nhau.
- `srs-fr-11-bao-cao.md:1268` (BR-AUTH-08) ghi ngoại lệ **"QTHT bypass"** cho toàn bộ nhóm FR-IX, tức
  đặc tả có tính đến việc vai trò QTHT chạm vào báo cáo.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 14:22–14:23:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/ct-theo-thoi-gian?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ *Tổng chương trình toàn kỳ 6 · Tổng DN toàn kỳ 0 · Tổng ngân sách toàn kỳ
  250.000.000* + biểu đồ đường + bảng *Theo kỳ*, **0 thông báo**.
- [Xuất Excel]: **1** request `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (1 mốc giờ,
  không double-toast); chữ người dùng đọc được đổi tại chỗ **"Đang tạo file..." → "Forbidden"**;
  **0 tệp** được giao. Khung thông báo hiển thị thật: `position: fixed`, rộng **1432 px**, cao 40 px,
  sống 3,401 giây. Tái hiện **2 lần**, kết quả y hệt.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_04`) — cùng bộ lọc, cùng bó mã, 2026-08-06 14:30–14:37:**

- [Xuất Excel]: 1 request `POST /api/v1/bao-cao/export` → **200**; chữ **"Đang tạo file..." → "Tạo file
  thành công."**; tệp `BaoCaoCtTheoThoiGian_20260806_1430.xlsx` (6.758 byte, zip thật, mở được bằng
  `openpyxl`). Nội dung tệp: phần đầu có tiêu đề BC + kỳ + khoảng thời gian + đơn vị + ngày tạo; khối
  *Theo kỳ* mỗi dòng là một kỳ thời gian kèm nhãn kỳ và số chương trình, khớp **từng hàng** với màn; đổi
  bộ lọc thì nội dung tệp đổi theo (Kỳ *Tháng* phủ cả năm → tệp ra **12 hàng** *Tháng 1/2026 … Tháng
  12/2026*, cộng dọc 5 + 1 = 6 = thẻ tổng; lọc đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp* → dòng đơn vị
  trong tệp đổi theo; lọc đơn vị *Bộ Công an* → báo cáo rỗng và 2 nút xuất bị khoá).

⇒ Câu *"Không thể tạo file xuất. Vui lòng thử lại."* của vòng 1 **không còn tái hiện**; câu **"Forbidden"**
của vòng 2 **vẫn tái hiện nguyên vẹn** ở đúng vai trò đối tác dùng.

### Bằng chứng

![BUG-CTTTG-004 — vai trò QTHT ("Quản trị hệ thống", avatar QT, BTP · TW) trên màn Báo cáo thống kê, bản dựng V1.0.8: bộ lọc trùng khít ảnh đối tác (BC Chương trình theo thời gian · Năm · 01/01/2026–31/12/2026 · Toàn quốc) và báo cáo ĐÃ XEM ĐƯỢC đầy đủ — Tổng chương trình toàn kỳ 6, thời điểm tạo 06/08/2026 14:22; nút Xuất Excel đang bật, đây là trạng thái ngay trước thao tác bấm [Xuất Excel] bị từ chối](image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png)

![BUG-CTTTG-004 — cùng phiên QTHT, lượt hẹn giờ bấm [Xuất Excel] trước 2500 ms rồi mới chụp: nút Xuất Excel đang được chọn, màn vẫn giữ báo cáo Tổng 6 và không có tệp nào về máy; ảnh KHÔNG bắt được lớp thông báo "Forbidden" — xem ghi chú ngay dưới](image/CTTTG_04-B2-qtht-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png)

![BUG-CTTTG-004 — đối chứng vai trò CB Nghiệp vụ Trung ương #04 (`cbnv_tw_04`), cùng bộ lọc, cùng bó mã index-DIABnbIr.js: kết quả Tổng chương trình toàn kỳ 6, thời điểm tạo 06/08/2026 14:30 — trạng thái ngay trước khi bấm [Xuất Excel], thao tác này xuất tệp thành công và không có thông báo lỗi nào](image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png)

Nguyên văn thông báo trên màn + phản hồi máy chủ + nội dung các tệp xuất của cả 2 nhánh:
[`image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt`](image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt).
Tệp xuất thật đã tải về để đọc nội dung: `testfiles/CTTTG_04-dang1-bandung-moi-DIABnbIr.xlsx` (dạng ①),
`testfiles/CTTTG_04-dang2-bandung-moi.xlsx` (lọc đơn vị BTP-TW),
`testfiles/CTTTG_04-dang3-bandung-moi-DIABnbIr.xlsx` (Kỳ Tháng, 12 mốc).

> **Vì sao chữ "Forbidden" không nằm trong ảnh:** công cụ chụp màn hình đang dùng không bắt được lớp
> thông báo do thư viện giao diện dựng qua portal (đã thử 3 lượt: chụp ngay sau khi bấm · 2 lượt hẹn giờ
> bấm sau 2500 ms rồi mới chụp) — cùng hạn chế đã ghi nhận ở BUG-QLTLPLCVV-015, BUG-SLCTHT-006 và
> BUG-CTTLV-005. Bằng chứng thay thế = chữ đọc bằng `innerText` (chỉ chữ người dùng nhìn thấy) + số đo
> chứng minh khung thông báo hiển thị thật + nguyên văn phản hồi máy chủ ngay dưới đây.

Phản hồi máy chủ khi vai trò QTHT bấm [Xuất Excel]:

```json
{
  "success": false,
  "error": {
    "code": "ERR-PERM-SYS-00-01",
    "message": "Forbidden",
    "timestamp": "2026-08-06T07:23:25.836Z",
    "requestId": "bf96f7f7-e505-4dec-913e-930a903f70d9"
  }
}
```

Thân yêu cầu đã gửi (cùng khuôn với nhánh CB Nghiệp vụ, chỉ khác phiên đăng nhập):

```json
{"loaiBaoCao":"BC_CT_THEO_THOI_GIAN","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","formatXuat":"XLSX"}
```

### So sánh (Comparison)

| Vai trò | Xem báo cáo | Xuất Excel | Chữ người dùng thấy khi xuất |
|---|---|---|---|
| CB Nghiệp vụ Trung ương (`cbnv_tw_04`) | ✅ 200 — hiện Tổng 6 + bảng *Theo kỳ* | ✅ 200 — nhận tệp `.xlsx` đúng nội dung | "Đang tạo file..." → "Tạo file thành công." |
| Quản trị hệ thống / QTHT (`admin`) | ✅ 200 — hiện Tổng 6 + bảng *Theo kỳ* | ❌ 403 — không có tệp | "Đang tạo file..." → **"Forbidden"** (chuỗi tiếng Anh thô) |

### Cách verify sau khi fix

```
── CÁCH VERIFY sau Dev fix ──
CẦN CÓ TRƯỚC: tài khoản admin (Quản trị hệ thống, cấp TW); màn Báo cáo thống kê (/bao-cao);
  ≥1 chương trình HTPLDN đã duyệt / đang thực hiện / hoàn thành nằm trong năm 2026. Báo cáo
  trống thì phép thử không có giá trị — tạo chương trình mới ở màn Chương trình HTPLDN và đưa
  lên trạng thái đã duyệt trở đi.
Bước 1. Chọn loại báo cáo "BC Chương trình theo thời gian", Kỳ "Năm", Đơn vị "Toàn quốc". Bấm
  [Xem báo cáo]. Ghi lại số Tổng chương trình toàn kỳ và toàn bộ bảng "Theo kỳ" (mỗi hàng:
  nhãn kỳ + từ ngày + đến ngày + số chương trình).
Bước 2. Bấm [Xuất Excel]. Chép lại NGUYÊN VĂN chữ hiện ra và kiểm có tệp về máy không.
Bước 3. Kiểm bằng đường thứ hai: mở tab Network xem lời gọi xuất báo cáo trả mã gì, thân phản
  hồi ghi gì. Có tệp thì MỞ TỆP RA ĐỌC, đối chiếu số tổng và TỪNG HÀNG kỳ ở bước 1 với số
  trong tệp, và kiểm cộng dọc cột số chương trình bằng đúng số tổng.
✅ ĐẠT khi một trong hai:
  · Vai trò Quản trị hệ thống bấm [Xuất Excel] thì nhận được tệp .xlsx mở đọc được, bên trong
    có bảng mỗi hàng một kỳ thời gian kèm nhãn kỳ và số chương trình, khớp đúng bảng trên màn,
    và không hiện thông báo từ chối nào.
  · Hoặc — nếu nghiệp vụ chốt vai trò này KHÔNG được xuất — hệ thống chặn ngay từ bước
    [Xem báo cáo], và chữ hiện ra là câu tiếng Việt cho người dùng biết họ không có quyền xem
    báo cáo này.
❌ CHƯA ĐẠT nếu: còn thấy "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào; hoặc vẫn
  cho Xem đủ số liệu rồi mới chặn ở bước Xuất. Đúng một nửa cũng tính là chưa đạt.
⚠️ 3 bẫy hay mắc khi đo:
  1. Chỉ thử bằng vai trò Cán bộ Nghiệp vụ rồi kết luận "đã fix". Vai trò đó vốn đã chạy tốt từ
     lượt đo 06/08/2026 — phép đo quyết định phải chạy bằng chính vai trò Quản trị hệ thống.
  2. Dừng ở "tải được tệp". Phải mở tệp ra đọc mới chốt được.
  3. Ghi kèm dấu vân tay bản dựng (tên bó mã assets/index-XXXX.js), đừng chỉ ghi chuỗi phiên
     bản: ngày 06/08/2026 bó mã đã đổi index-CNwX9JjX.js → index-DIABnbIr.js mà chuỗi phiên
     bản vẫn in V1.0.8. Hai vai trò phải đo trên CÙNG một bó mã thì mới so sánh được.
⚠️ Đừng chấm hỏng vì tên sheet, thứ tự cột, cách viết nhãn kỳ, màu sắc, dòng tổng cuối bảng,
  kỳ không có chương trình nào hiện thành 0 hay bị bỏ, tệp không nhúng biểu đồ, hay vì tên tệp
  không đúng chữ "BaoCaoChuongTrinh" — đặc tả không quy định những thứ đó. Xem mục [4].
Ảnh lỗi lần này: image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png
  + image/CTTTG_04-B2-qtht-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png
  + nguyên văn phản hồi máy chủ ở image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho
vai trò QTHT trên loại BC này, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`.
**Dev FE** — không đẩy nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt dứt điểm
câu hỏi "QTHT có được xuất báo cáo không" (đã nêu ở [`cau-hoi-BA.md`](cau-hoi-BA.md) Mục 2) trước khi dev
chọn hướng sửa.

---

## Phụ lục — Môi trường test (Phần 2)

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io |
| OTP login | Lấy từ MailHog (không có mã bypass trên môi trường này) |
| MailHog (OTP inbox) | http://18.143.165.120:8025 |
| API base | https://18.143.165.120.nip.io/api/v1 |
| Frontend | React + Vite + Ant Design (bó mã `assets/index-CNwX9JjX.js`) |
| Xác thực | JWT trong cookie + OTP qua email |
| Tool test | Chrome DevTools MCP · bộ bắt thông báo dùng chung `tools/toast-capture.js` · đọc tệp xuất bằng `openpyxl` |

---

*Phần 2 generated: 2026-08-06 12:40:00 · cập nhật 2026-08-06 13:50:00 (thêm BUG-CTTLV-005) | QA Automation via Claude Code*

---
---

# Phần 3 — Batch B5 (BC Số lượng hỏi đáp/vướng mắc pháp luật)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 174 |
| **Case** | `SLHDVM_06` — Báo cáo thống kê → BC Số lượng hỏi đáp/vướng mắc pháp luật (FR-IX-01) |
| **Ngày** | 2026-08-06 12:52:00 |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **V1.0.8** (md5 bó mã `e0e4f737b1fb7ab9409f459a4d0fa051`) |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW) — đúng vai trò đối tác dùng |
| **File tiêu chí** | [`tieuchi/SLHDVM_06.md`](tieuchi/SLHDVM_06.md) |

## Tổng hợp

Case gộp **2 vế**: vế a — *"Không thể tạo file xuất. Vui lòng thử lại."* (vòng 1) · vế b — *"Forbidden"*
(vòng 2, ô `TKM phản hồi lần 1`). Lượt đo 2026-08-06 cho kết quả **vế a hết lỗi, vế b tái hiện nguyên vẹn**
⇒ verdict **Reopen** (flow §Ca biên: còn ≥1 vế lỗi → Reopen).

Vai trò **CB Nghiệp vụ Trung ương** xuất Excel bình thường ở **3/3 cấu hình bộ lọc**, tệp mở bằng `openpyxl`
đủ 4 mục header và số liệu khớp màn từng con số. Vai trò **QTHT — đúng vai trò đối tác dùng** — **xem** được
báo cáo (HTTP 200) nhưng **xuất** thì bị từ chối kèm chữ *"Forbidden"*. Nguyên nhân là **phân quyền theo vai
trò**, không phải lỗi tạo tệp. **Không seed, không đổi dữ liệu nào.**

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Blocker | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 0      | 1    |

## Bug Summary Table

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-SLHDVM-006 | Major | P1 | Permission | `SLHDVM_06` (tab `bug` dòng 174) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` · `:1268` | [`image/SLHDVM_06-07-doichung-vaitro-QTHT-thong-bao-Forbidden-V108.png`](image/SLHDVM_06-07-doichung-vaitro-QTHT-thong-bao-Forbidden-V108.png) | Open |

---

## BUG-SLHDVM-006 — Vai trò QTHT xem được báo cáo hỏi đáp nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 12:41 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vai trò CB Nghiệp vụ Trung ương xuất Excel bình thường ở 3/3 cấu hình bộ lọc (tệp
> `BaoCaoHoiDap_20260806_1225.xlsx` · `_1229.xlsx` · `_1230.xlsx`, nội dung khớp màn, md5 khác nhau nên
> bám đúng bộ lọc). Vai trò QTHT — đúng vai trò đối tác dùng — **xem** được báo cáo (22/11/11/50,0 %)
> nhưng **xuất** thì bị từ chối kèm chữ *"Forbidden"*. N = 5 lượt xuất · M = 3 dạng bộ lọc (+ quét thêm
> 3 loại BC × 2 định dạng ở nhánh QTHT) · **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Số lượng hỏi đáp/vướng mắc pháp luật**, người dùng vai trò
**Quản trị hệ thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu và **hiện nút [Xuất Excel]
ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện
ra cho người dùng là **"Forbidden"** — một chuỗi tiếng Anh thô, không cho biết chuyện gì đã xảy ra. Cùng thao
tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

Việc bị chặn **không riêng báo cáo này**: vai trò QTHT xem được cả 3 loại báo cáo đã thử (HTTP 200) nhưng xuất
thì bị từ chối ở **3 loại báo cáo × 2 định dạng (Excel và PDF)** — tức là một quy tắc quyền chung của chức
năng xuất báo cáo, không phải lỗi cục bộ.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, `vaiTro = ["QTHT"]`, cấp TW) — đây đúng là
   vai trò trên bằng chứng của đối tác ở cả 2 vòng nghiệm thu.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Số lượng hỏi đáp/vướng mắc pháp luật**; *Kỳ báo cáo* = **Năm**
   (01/01/2026 → 31/12/2026); *Đơn vị* = **Toàn quốc**; để trống cả *Lĩnh vực PL* và *Trạng thái HĐ*.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng hỏi đáp 22 · Đã trả lời 11 · Chờ trả lời 11 ·
   Tỷ lệ trả lời 50,0 % + bảng theo lĩnh vực + bảng theo đơn vị), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117`, khi hệ thống từ chối vì người dùng không có quyền thì phải cho người dùng
  biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ thuật tiếng Anh ra
  màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng. Nếu vai trò này thật sự không được phép dùng
  báo cáo thì phải bị chặn ngay từ bước Xem, chứ không phải cho xem đầy đủ số liệu rồi mới chặn ở bước xuất —
  hai bước phải nhất quán với nhau.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.
- `srs-fr-11-bao-cao.md:1268` (BR-AUTH-08) ghi ngoại lệ **"QTHT bypass"** cho toàn bộ nhóm FR-IX, tức đặc tả
  có tính đến việc vai trò QTHT chạm vào báo cáo.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 12:37:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**,
  màn hiện đủ 22 · 11 · 11 · 50,0 % (*Thời điểm tạo 06/08/2026 12:37*), **0 thông báo**.
- Nút [Xuất Excel]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: **1** request `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (1 mốc giờ, không
  double-toast); chữ người dùng đọc được: **"Forbidden"**; **0 tệp** được giao. Khung thông báo hiện thật:
  xuất hiện sau khi bấm 102 ms, biến mất ở 3 440 ms, khung `x=8 · y=16 · w=1416 · h=40`, `opacity 1`,
  `visibility visible`. Console: *"Failed to load resource: the server responded with a status of 403"*.
- Nguyên văn phản hồi máy chủ:
  ```json
  {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
   "timestamp":"2026-08-06T05:33:42.073Z","requestId":"cc37e318-eee2-43b5-867b-125ed2693994"}}
  ```
- Phạm vi bị chặn: **XEM** → 200 ở `/bao-cao/hoi-dap`, `/bao-cao/lop-dao-tao-dang-dien-ra`,
  `/bao-cao/vu-viec-tiep-nhan`. **XUẤT** (`POST /api/v1/bao-cao/export`) → **403 ở cả 6 tổ hợp**
  (`BC_HOI_DAP` · `BC_LOP_DAO_TAO_DANG_DIEN_RA` · `BC_VU_VIEC_TIEP_NHAN`) × (`XLSX` · `PDF`).

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, cùng kỳ, 2026-08-06 12:25 → 12:32:**

| Dạng | Bộ lọc | Số trên màn | Kết quả bấm [Xuất Excel] |
|---|---|---|---|
| 1 | không lọc đặc thù (đúng điều kiện vòng 2 của đối tác) | 22 / 11 / 11 / 50,0 % | 1 request → **200**, `filename="BaoCaoHoiDap_20260806_1225.xlsx"`, 6 966 B, md5 `1eaf95ed…` |
| 2 | Lĩnh vực PL = **Thuế** (đúng điều kiện vòng 1 của đối tác) | 8 / 6 / 2 / 75,0 % | 1 request → **200**, `filename="BaoCaoHoiDap_20260806_1229.xlsx"`, 6 878 B, md5 `32cef683…` |
| 3 | Trạng thái HĐ = **Đã trả lời** | 11 / 11 / 0 / 100,0 % | 1 request → **200**, `filename="BaoCaoHoiDap_20260806_1230.xlsx"`, 6 928 B, md5 `aab88a6b…` |

- Cả 3 lượt: **1 request ↔ 1 khung thông báo** (1 mốc giờ), chữ trên màn = *"Đang tạo file..."*; **không**
  xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."*, **không** xuất hiện *"Forbidden"*.
- Trình duyệt **thật sự nhận tệp về máy**: Chrome ghi ra đĩa 3 tệp đúng 3 mốc giờ bấm, md5 **trùng khít** thân
  phản hồi.
- **Mở tệp ra đọc bằng `openpyxl`** (không dừng ở "200 + có byte"): cả 3 tệp có 1 sheet *"BC Số lượng hỏi
  đáp"*; 4 dòng đầu đủ 4 mục đặc tả `:1092` đòi — `A1 "BC Số lượng hỏi đáp/vướng mắc pháp luật"` ·
  `A2 "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"` · `A3 "Đơn vị: Toàn quốc"` · `A4 "Ngày tạo: 06/08/2026"`.
  Số liệu trong tệp **khớp từng con số** với màn (kể cả bảng theo lĩnh vực và theo đơn vị, cộng đúng tổng).
  3 tệp **md5 khác nhau** ⇒ tệp xuất bám đúng bộ lọc hiện tại (BR-DATA-06, `:1280`).
- **Đường đo thứ hai** (gọi thẳng máy chủ, ngoài trình duyệt, cùng tham số dạng 2): **200**, 6 879 B,
  `filename="BaoCaoHoiDap_20260806_1232.xlsx"`, 4 dòng header y hệt, số liệu 8 / 6 / 2 / 75 ⇒ **hai đường
  khớp nhau hoàn toàn**.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò, đúng màn,
đúng bộ lọc của đối tác.

### Bằng chứng

- [`image/SLHDVM_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png`](image/SLHDVM_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png)
  — vai trò CB Nghiệp vụ TW, dạng 1 không lọc đặc thù, báo cáo đã render 22 · 11 · 11 · 50,0 %, *Thời điểm
  tạo 06/08/2026 12:25*, nút [Xuất Excel] đang bật.
- [`image/SLHDVM_06-02-dang1-ngay-sau-khi-bam-xuat-excel-V108.png`](image/SLHDVM_06-02-dang1-ngay-sau-khi-bam-xuat-excel-V108.png)
  — ngay sau khi bấm [Xuất Excel] ở dạng 1: **không** có khung thông báo lỗi nào trên màn.
- [`image/SLHDVM_06-03-dang2-loc-linhvuc-Thue-man-hinh-truoc-khi-xuat-V108.png`](image/SLHDVM_06-03-dang2-loc-linhvuc-Thue-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 2, *Lĩnh vực PL = Thuế* (đúng bộ lọc vòng 1 của đối tác), số trên màn 8 · 6 · 2 · 75,0 %,
  *Thời điểm tạo 12:28*.
- [`image/SLHDVM_06-04-dang2-ngay-sau-khi-bam-xuat-excel-V108.png`](image/SLHDVM_06-04-dang2-ngay-sau-khi-bam-xuat-excel-V108.png)
  — ngay sau khi bấm [Xuất Excel] ở dạng 2: **không** có khung thông báo lỗi nào.
- [`image/SLHDVM_06-05-dang3-loc-trangthai-DaTraLoi-man-hinh-truoc-khi-xuat-V108.png`](image/SLHDVM_06-05-dang3-loc-trangthai-DaTraLoi-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 3, *Trạng thái HĐ = Đã trả lời*, số trên màn 11 · 11 · 0 · 100,0 %, *Thời điểm tạo 12:30*.
- [`image/SLHDVM_06-06-dang3-ngay-sau-khi-bam-xuat-excel-V108.png`](image/SLHDVM_06-06-dang3-ngay-sau-khi-bam-xuat-excel-V108.png)
  — ngay sau khi bấm [Xuất Excel] ở dạng 3: **không** có khung thông báo lỗi nào.
- 🔴 [`image/SLHDVM_06-07-doichung-vaitro-QTHT-thong-bao-Forbidden-V108.png`](image/SLHDVM_06-07-doichung-vaitro-QTHT-thong-bao-Forbidden-V108.png)
  — **ảnh lỗi**: phiên vai trò QTHT, báo cáo đã hiện đủ số liệu (22 · 11 · 11 · 50,0 %, *tạo 12:37*), khung
  thông báo đỏ **"Forbidden"** ở đầu màn — cùng một chữ với ảnh nghiệm thu vòng 2 của đối tác.
- [`image/SLHDVM_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/SLHDVM_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn + phản hồi máy chủ từng lượt, dấu vân tay bản dựng, kết quả đọc tệp bằng
  `openpyxl`, md5 đối chiếu, và bảng quét 3 loại BC × 2 định dạng.

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:140`) | 200, ra đủ số liệu | **200**, nhận được tệp .xlsx đọc được | *"Đang tạo file..."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra đủ số liệu | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* là điểm đặc tả tự mâu thuẫn
  (`:62`/`:140` liệt kê tác nhân là CB Nghiệp vụ / CB Phê duyệt, còn `:1268` ghi ngoại lệ *"QTHT bypass"*).
  Đã có mục dành cho BA ở [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2 — Vai trò QTHT có được XUẤT báo cáo thống
  kê không?* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của case: dù BA chốt hướng nào thì hành
  vi hiện tại vẫn lệch `:117`.
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2 của file này) — cùng endpoint `POST /api/v1/bao-cao/export`,
  cùng mã `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng cả hai; QA vòng sau vẫn phải
  verify riêng từng case trên đúng màn của nó.
- **Bác một kết luận cũ của tổ QA:** hồ sơ `reverify-week-4/DANH-SACH-53-BUG-REOPEN-KET-QUA-QA.md` từng xếp
  cụm 44 lỗi *"Forbidden"* màn Báo cáo thống kê là *"không phải bug code — env-drift, OSP chạy bản cũ"*. Lượt
  đo này tái hiện 100 % ngay trên bản dựng mới nhất: nguyên nhân là **phân quyền theo vai trò**. Vòng verify cũ
  không tái hiện được vì chỉ đo bằng vai trò CB Nghiệp vụ — đúng vai trò được phép — chứ không đo bằng vai trò
  đối tác thật sự dùng.
- **Ngoài phạm vi, không kéo verdict:** case này đối tác **không** nêu vế tên tệp, nên khuôn tên tệp không
  được chấm. Ghi nhận để tham khảo: tệp xuất lần này về đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` mà
  `:85`/`:1092` quy định.

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần ≥1 hỏi đáp/vướng mắc pháp luật đã duyệt nằm trong năm 2026 để báo cáo có dữ
  liệu; nếu báo cáo trống thì tạo hỏi đáp mới ở màn Hỏi đáp/vướng mắc pháp luật và đưa lên
  trạng thái đã duyệt trở đi, hoặc đổi kỳ báo cáo sang kỳ có dữ liệu.
1) Chọn Loại báo cáo "BC Số lượng hỏi đáp/vướng mắc pháp luật", Kỳ báo cáo "Năm"
   (01/01/2026 → 31/12/2026), Đơn vị "Toàn quốc", để trống cả Lĩnh vực PL và Trạng thái HĐ.
   Bấm [Xem báo cáo], ghi lại 4 số trên màn: Tổng hỏi đáp / Đã trả lời / Chờ trả lời / Tỷ lệ
   trả lời.
2) Bấm [Xuất Excel]. Đọc nguyên văn chữ hiện ra và kiểm có tệp về máy không. Làm lại bước 1-2
   một lần nữa với Lĩnh vực PL = "Thuế" để phủ đúng cấu hình bộ lọc của lần nghiệm thu đầu.
3) Đo bằng đường thứ hai: mở tab Network xem lời gọi xuất báo cáo trả mã gì và thân phản hồi ghi
   gì; nếu có tệp thì MỞ TỆP RA ĐỌC, đối chiếu 4 số ở bước 1 với số trong tệp, và so 2 tệp của
   2 cấu hình bộ lọc xem nội dung có khác nhau không.
✅ PASS khi: vai trò Quản trị hệ thống bấm [Xuất Excel] thì nhận được tệp .xlsx mở được, 4 số
   trong tệp khớp đúng 4 số trên màn của chính lần đó, tệp của cấu hình lọc "Thuế" khác tệp
   không lọc, và không hiện thông báo từ chối nào.
   HOẶC (nếu nghiệp vụ chốt là vai trò này không được xuất): hệ thống chặn NGAY từ bước
   [Xem báo cáo] chứ không cho xem rồi mới chặn, và chữ hiện ra là câu tiếng Việt cho người
   dùng biết họ không có quyền xem báo cáo này.
❌ FAIL nếu: vẫn hiện chuỗi "Forbidden" hoặc bất kỳ chuỗi tiếng Anh/mã kỹ thuật nào; hoặc vẫn cho
   Xem đầy đủ số liệu rồi mới chặn ở bước Xuất; hoặc xuất được ở cấu hình bộ lọc này nhưng vẫn bị
   chặn ở cấu hình kia (đúng một phần cũng tính FAIL).
⚠️ Đừng chấm Fail vì tên tệp, tên sheet, thứ tự cột, khổ giấy, phông chữ hay việc thiếu thông báo
   "Đang tạo file..." — những thứ đó nằm ngoài điều đối tác phản ánh ở case này.
⚠️ Đừng kết luận "đã fix" khi chỉ thấy vai trò Cán bộ Nghiệp vụ xuất được — vai trò đó vốn đã chạy
   tốt ở lượt đo 06/08/2026. Phép đo quyết định là chạy bằng chính vai trò Quản trị hệ thống. Cũng
   đừng dừng ở "tải được tệp": phải mở tệp ra đọc mới chốt được. Và đừng chỉ nghe bộ bắt thông báo
   kiểu "node mới thêm" — giao diện thay chữ ngay trong khung thông báo cũ nên dễ báo nhầm là
   "không có thông báo nào"; phải theo dõi nội dung khung thông báo theo thời gian.
Ảnh lỗi lần này: image/SLHDVM_06-07-doichung-vaitro-QTHT-thong-bao-Forbidden-V108.png
  + nguyên văn phản hồi máy chủ ở image/SLHDVM_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt dứt điểm câu hỏi *"QTHT có được xuất báo
cáo không"* (đã nêu ở [`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2) trước khi dev chọn hướng sửa.

---

## Phụ lục — Môi trường test (Phần 3)

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io |
| Bản dựng (tự đo 2026-08-06 12:23) | nhãn **HTPLDN · V1.0.8** · bó mã `assets/index-CNwX9JjX.js` · etag `"6a73f6a4-1124fd"` · 1 123 581 B · `index.html` last-modified `Thu, 06 Aug 2026 02:51:16 GMT` · **md5 bó mã `e0e4f737b1fb7ab9409f459a4d0fa051`** |
| OTP login | Lấy từ MailHog (không có mã bypass trên môi trường này) |
| MailHog (OTP inbox) | http://18.143.165.120:8025 |
| API base | https://18.143.165.120.nip.io/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | JWT trong cookie + OTP qua email |
| Tool test | Chrome DevTools MCP · bộ bắt thông báo dùng chung `tools/toast-capture.js` (bổ sung phép đo nội dung khung thông báo theo thời gian) · đọc tệp xuất bằng `openpyxl` |
| Giới hạn hiệu lực | Đo trên env kiểm thử nội bộ, khác env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác và bản dựng mới hơn ⇒ kết luận *hết lỗi* của vế a chỉ có hiệu lực khi bản dựng này lên môi trường nghiệm thu |

---

*Phần 3 generated: 2026-08-06 12:52:00 | QA Automation via Claude Code*

---

# Phần 4 — Batch B3 (BC chi phí hỗ trợ)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 238 · 243 · 258 · 263 · 264 |
| **Ngày** | 2026-08-06 13:15:00 |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **V1.0.8** (bó mã `assets/index-CNwX9JjX.js`) |
| **Tài khoản ra verdict** | `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW) — đúng vai trò đối tác dùng trong ảnh |
| **Thư mục tiêu chí** | [`tieuchi/`](tieuchi/) — mỗi case một file, viết xong trước khi mở màn |

> **Quan hệ với Phần 2 và Phần 3:** cùng một chức năng xuất báo cáo (`POST /api/v1/bao-cao/export`), khác loại
> báo cáo. Theo yêu cầu của lô — *"nhiều case cùng một câu triệu chứng vẫn phải đo từng case trên đúng màn của
> nó"* — mỗi dòng bảng vẫn được đo riêng, không suy kết quả từ case anh em.

## Bug Summary Table (Phần 4)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CPHTCT-006 | Major | P1 | Permission | `CPHTCT_06` (tab `bug` dòng 238) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CPHTCT_06-02-qtht-xem-duoc-bao-cao-nut-xuat-van-bam-duoc.png`](image/CPHTCT_06-02-qtht-xem-duoc-bao-cao-nut-xuat-van-bam-duoc.png) | Open |

---

## BUG-CPHTCT-006 — Vai trò QTHT xem được BC Chi phí chi trả hỗ trợ nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:15 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế a của đối tác (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất Excel được, tệp `BaoCaoChiPhiChiTra_20260806_1249.xlsx` (6 918 B) mở đọc được, số liệu khớp
> màn, xuất lần 2 lúc 12:51 ra tên khác nên không đè tệp. Vế b (*"Forbidden"*, 31/07) **tái hiện nguyên vẹn**
> ở đúng vai trò đối tác đã dùng. N = 3 lượt xuất (2 vai CB Nghiệp vụ + 1 vai QTHT) · **không seed, không đổi
> dữ liệu nào** — toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chi phí chi trả hỗ trợ**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu và **hiện hai nút [Xuất Excel] /
[Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**.
Chữ hiện ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy
chủ, không cho người dùng biết chuyện gì đã xảy ra và phải làm gì tiếp. Cùng thao tác, cùng bộ lọc, vai trò
Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, vé đăng nhập ghi `vaiTro = ["QTHT"]`,
   `capDonVi = "TW"`) — đúng vai trò trên bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chi phí chi trả hỗ trợ**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng chi phí 23.000.000 · Tổng hồ sơ 2 · TB/hồ sơ
   11.500.000 + bảng theo đơn vị), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_03`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 12:59:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/chi-phi-chi-tra` → **200**, màn hiện đủ 23.000.000 · 2 · 11.500.000
  (*Thời điểm tạo 06/08/2026 12:59*) — **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được**.
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (không có hiện tượng 2 thông
  báo chồng); chữ người dùng đọc được: **"Forbidden"**, khung sống **3 150 ms**, vị trí `x=0 · y=8 · w=1432`
  (nằm trong vùng nhìn thấy, không phải node ẩn); **0 tệp** được giao, **0 blob** được tạo.
- Nguyên văn nội dung gửi lên và phản hồi máy chủ:
  ```json
  → {"loaiBaoCao":"BC_CHI_PHI_CHI_TRA","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T05:59:34.537Z","requestId":"4eaa4039-50cd-41c1-91e7-f05759d154bd"}}
  ```

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_03`) — cùng màn, cùng kỳ, cùng đơn vị:**

| Lượt | Giờ bấm | Phản hồi máy chủ | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|
| 1 | 12:49 | **200**, kiểu nội dung `…spreadsheetml.sheet` | `BaoCaoChiPhiChiTra_20260806_1249.xlsx` — 6 918 B | *"Đang tạo file..."* |
| 2 | 12:51 | **200** | `BaoCaoChiPhiChiTra_20260806_1251.xlsx` — 6 917 B | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Tên tệp hai lượt khác nhau** (`…_1249` vs `…_1251`) ⇒ hai lần xuất trong cùng ngày không đè tệp nhau,
  đúng lý do BA chốt ở `:85`.
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): đủ 4 mục header `:1092` đòi — tên báo cáo · kỳ báo cáo ·
  đơn vị · ngày tạo; số liệu trong tệp khớp từng con số với màn (23.000.000 · 2 · 11.500.000, dòng
  *Cục Bổ trợ tư pháp*).
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò, đúng màn,
đúng bộ lọc của đối tác.

### Bằng chứng

- [`image/CPHTCT_06-01-xuat-excel-thanh-cong.png`](image/CPHTCT_06-01-xuat-excel-thanh-cong.png) — phiên vai
  trò CB Nghiệp vụ TW, báo cáo đã hiện đủ số liệu, sau khi bấm [Xuất Excel] **không** có khung thông báo lỗi.
- 🔴 [`image/CPHTCT_06-02-qtht-xem-duoc-bao-cao-nut-xuat-van-bam-duoc.png`](image/CPHTCT_06-02-qtht-xem-duoc-bao-cao-nut-xuat-van-bam-duoc.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, báo cáo hiện đủ số liệu và **hai nút Xuất đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị
  từ chối ngay sau đó.
  *Ghi chú thẳng thắn:* khung thông báo *"Forbidden"* chỉ sống 3,15 giây nên **không kịp vào ảnh** (đã thử 3
  lần). Bằng chứng của chính chữ đó nằm ở tệp chữ bên dưới (đo bằng máy, có mốc giờ + kích thước khung) và ở
  phản hồi 403 của máy chủ — đây là bằng chứng mạnh hơn ảnh.
- [`image/CPHTCT_06-thong-bao-va-phan-hoi-may-chu.txt`](image/CPHTCT_06-thong-bao-va-phan-hoi-may-chu.txt) —
  nguyên văn chữ trên màn từng lượt (có mốc giờ, kích thước, tuổi thọ khung), nguyên văn phản hồi máy chủ,
  vai trò đọc từ vé đăng nhập, và kết quả đọc nội dung tệp .xlsx.
- [`image/CPHTCT_06-xuat-excel.xlsx`](image/CPHTCT_06-xuat-excel.xlsx) — tệp thật hệ thống giao ra (6 918 B).
- Số liệu thô: [`testfiles/CPHTCT_06-xlsx-capture.json`](testfiles/CPHTCT_06-xlsx-capture.json) ·
  [`testfiles/CPHTCT_06-xlsx-capture-lan2.json`](testfiles/CPHTCT_06-xlsx-capture-lan2.json) ·
  [`testfiles/CPHTCT_06-qtht-xuat-excel.json`](testfiles/CPHTCT_06-qtht-xuat-excel.json).

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_03` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`) | 200, ra đủ số liệu | **200**, nhận được tệp .xlsx đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của case:
  phép thử là giả sử BA trả lời theo cả hai hướng — nếu QTHT *không* được xuất thì hệ thống vẫn phải hiện câu
  tiếng Việt `:117` thay vì `Forbidden`; nếu QTHT *được* xuất thì đang chặn nhầm. Khuyết tật tồn tại ở **cả
  hai nhánh trả lời**, nên không chờ BA. Lập luận đầy đủ ở [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7.
- Về `srs-fr-11-bao-cao.md:1268` (BR-AUTH-08): điều khoản này nói về **phạm vi dữ liệu theo `don_vi_id`**, và
  ngoại lệ *"QTHT bypass"* của nó có nghĩa QTHT không bị bó hẹp phạm vi đơn vị — **tự nó không khẳng định**
  QTHT được hay không được dùng chức năng xuất. Ghi rõ ở đây để dev/BA không đọc quá lời câu đó.
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2) và `BUG-SLHDVM-006` (Phần 3) — cùng endpoint
  `POST /api/v1/bao-cao/export`, cùng mã `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng
  cả ba; QA vòng sau vẫn phải verify riêng từng case trên đúng màn của nó.
- **Ngoài phạm vi, không kéo verdict case này:** khi mở tệp .xlsx và đối chiếu đặc tả, thấy khối **`theo_ky[]`**
  mà `srs-fr-11-bao-cao.md:724` khai điều kiện *Luôn* cho FR-IX-15 **không xuất hiện** ở cả ba đường đo (màn
  hình · tệp xuất · phản hồi máy chủ — payload chỉ có `theoDonVi`, `theoQuyMoDn`). Đây là khuyết tật của khâu
  **dựng báo cáo**, không phải khâu **xuất tệp** mà đối tác phản ánh, nên không chấm vào case này. Đang gom số
  đo trên cả 4 màn của lô B3 rồi mở phiếu riêng — xem [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7 Sửa 2.

### Khối giao việc

```
🔁 CÒN LỖI — chuyển lại dev.

■ CÒN LỖI Ở ĐÂU
Vai trò Quản trị hệ thống (tài khoản admin) — đúng vai trò trong ảnh nghiệm thu:
   [Xem báo cáo] → OK. Hiện đủ số liệu, hai nút Xuất bật sáng.
   [Xuất Excel]  → KHÔNG ra tệp. Màn hiện đúng một chữ "Forbidden"
                   (máy chủ trả 403 · mã ERR-PERM-SYS-00-01)
Đúng hiện tượng ô "TKM phản hồi lần 1" đã ghi.

■ VÌ SAO LÀ LỖI (đặc tả srs-fr-11-bao-cao.md)
1. Dòng :79 — kiểm quyền phải nằm ở ĐẦU luồng, nên bước Xem và bước Xuất phải cùng một quy
   tắc quyền. Hiện đang cho xem đủ số liệu rồi mới chặn ở bước xuất.
2. Dòng :117 — khi từ chối phải hiện câu tiếng Việt báo người dùng không có quyền xem báo
   cáo. Hiện đang ném thẳng chuỗi kỹ thuật tiếng Anh của máy chủ ra cho người dùng cuối.
KHÔNG phải chờ BA mới sửa được: câu hỏi "QTHT có được xuất báo cáo không" đã gửi BA, nhưng
trả lời hướng nào thì vẫn là lỗi — nếu không được xuất thì phải chặn từ bước Xem và báo bằng
tiếng Việt; nếu được xuất thì đang chặn nhầm.

■ ĐÃ HẾT LỖI — ĐỪNG ĐỤNG LẠI
Cán bộ Nghiệp vụ Trung ương xuất Excel tốt: tệp mở đọc được, đầu tệp đủ tên báo cáo + kỳ +
đơn vị + ngày tạo, số trong tệp khớp đúng số trên màn; hai lượt xuất ra hai tên tệp khác nhau
nên không đè nhau. Hết câu "Không thể tạo file xuất. Vui lòng thử lại." (đối tác báo 16/07).

■ AI SỬA
Dev BE — cho bước Xem và bước Xuất dùng chung quy tắc quyền; từ chối thì trả thông báo theo :117.
Dev FE — không đẩy chuỗi máy chủ trả về ra thẳng màn hình người dùng.
BA     — chốt "QTHT có được xuất báo cáo không" để dev chọn hướng sửa.

■ ĐÃ ĐO
06/08/2026 · bản dựng V1.0.8 · admin (QTHT/TW) + cbnv_tw_03 (CB Nghiệp vụ/TW) · BC Chi phí chi
trả hỗ trợ · Kỳ Năm 2026 · Toàn quốc · 3 lượt bấm xuất · không tạo/sửa/xoá bản ghi nào.
Bằng chứng: ô "Ảnh/video verify" cùng dòng.
Lỗi khác gặp lúc đo, đã tách phiếu riêng, KHÔNG tính vào phiếu này: BCTK_QA06 (dòng 369) —
báo cáo này thiếu hẳn phần chia theo kỳ.

────────── CÁCH VERIFY SAU KHI DEV FIX ──────────
Cần trước: tài khoản admin (QTHT, cấp TW) · màn Báo cáo thống kê (/bao-cao) · kỳ báo cáo phải
CÓ dữ liệu (báo cáo trống thì nút Xuất tự tắt, đo vô nghĩa).

B1. admin → BC Chi phí chi trả hỗ trợ · Kỳ Năm 01/01–31/12/2026 · Toàn quốc → [Xem báo cáo]
    (bấm đúng 1 lần). Ghi 3 số: Tổng chi phí · Tổng hồ sơ · TB mỗi hồ sơ.
B2. [Xuất Excel] → chép nguyên văn chữ hiện ra; kiểm có tệp về máy không.
B3. Đối chiếu bằng đường thứ 2: tab Network xem lời gọi xuất trả mã gì. Có tệp thì MỞ RA ĐỌC,
    so với 3 số ở B1.
B4. Lặp B1–B3 bằng cbnv_tw_03 để chắc vai trò này không bị chặn theo.

✅ PASS — đạt 1 trong 2:
   a) admin xuất được tệp .xlsx mở đọc được, số khớp màn, không thông báo từ chối; HOẶC
   b) nếu BA chốt QTHT không được xuất → chặn NGAY ở bước [Xem báo cáo], kèm câu tiếng Việt.
❌ FAIL nếu: còn "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào cho người dùng cuối ·
   vẫn cho xem đủ rồi mới chặn ở bước Xuất · chỉ ẩn/làm mờ nút Xuất mà bước Xem vẫn vào được ·
   Cán bộ Nghiệp vụ bị chặn theo.

⚠️ BẪY
1. Cán bộ Nghiệp vụ xuất được KHÔNG chứng minh đã fix — vai trò đó vốn đã tốt từ 06/08. Phép đo
   quyết định là chạy bằng chính tài khoản admin.
2. Tải được tệp chưa đủ — phải MỞ TỆP RA ĐỌC mới chốt.
3. Đừng chấm Fail vì tên tệp BaoCaoChiPhiChiTra_… (khuôn tên đã chốt 04/08/2026), hay vì số liệu
   khác ảnh nghiệm thu (25 hồ sơ / 226.308.268 đ) — khác dữ liệu, không phải lỗi.
4. Khung thông báo sống ~3 giây và đổi chữ NGAY TRONG khung cũ, không mọc khung mới → công cụ
   đếm "khung mới" chỉ thấy "Đang tạo file..." rồi báo nhầm là im lặng. Phải theo dõi nội dung
   khung theo thời gian. Tải lại trang trước khi đo — tab mở lâu vẫn chạy mã cũ.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa.

---

---

## Bug Summary Table (Phần 4 — bổ sung dòng 243)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CPCTHTTDVQL-006 | Major | P1 | Permission | `CPCTHTTDVQL_06` (tab `bug` dòng 243) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CPCTHTTDVQL_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png`](image/CPCTHTTDVQL_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png) | Open |

---

## BUG-CPCTHTTDVQL-006 — Vai trò QTHT xem được BC Chi phí theo đơn vị nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:45 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế a của đối tác (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được ở **cả 2 cấu hình bộ lọc**, tệp mở đọc được, bảng chéo hàng = đơn vị đủ 4 cột, số khớp
> màn từng con số, hai tệp khác md5 nên bám đúng bộ lọc. Vế b (*"Forbidden"*, 31/07) **tái hiện nguyên vẹn**
> ở đúng vai trò đối tác đã dùng, **đo 3 lượt** (2 lượt qua giao diện + 1 lượt gọi thẳng máy chủ, kết quả
> khớp nhau). N = 5 lượt bấm xuất · M = 2 dạng bộ lọc · **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chi phí theo đơn vị**, người dùng vai trò **Quản trị hệ thống
(QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu và **hiện hai nút [Xuất Excel] / [Xuất PDF]
ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện
ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ. Cùng
thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, cấp TW) — đúng vai trò trên bằng chứng của
   đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chi phí theo đơn vị**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng hồ sơ 2 · Tổng chi phí 23.000.000 + bảng chéo
   theo đơn vị), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_03`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng.
  Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không cho xem đầy đủ số
  liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò**.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — đo 3 lượt, kết quả giống hệt nhau:**

| Lượt | Giờ | Cách đo | Mã trả về | Chữ hiện cho người dùng | Tệp |
|---|---|---|---|---|---|
| 1 | 13:38 | bấm trên giao diện | **403** `ERR-PERM-SYS-00-01` | *"Đang tạo file..."* → **"Forbidden"** (tắt sau ~3,2 s) | 0 |
| 2 | 13:40 | gọi thẳng máy chủ | **403** `ERR-PERM-SYS-00-01` | — | 0 |
| 3 | 13:41 | bấm trên giao diện | **403** `ERR-PERM-SYS-00-01` | **"Forbidden"**, khung `x=657 y=3 w=118 h=40`, sống ~3,3 s | 0 |

- Bước [Xem báo cáo] **không** bị chặn: `GET /api/v1/bao-cao/chi-phi-theo-don-vi` → **200**, màn hiện đủ
  2 · 23.000.000 · 11.500.000 — **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**.
- Nguyên văn phản hồi lượt 3:
  ```json
  {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
   "timestamp":"2026-08-06T06:41:41.486Z","requestId":"c5060a92-0b6e-4edf-baa3-58135a8d9384"}}
  ```

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_03`) — cùng màn, cùng kỳ:**

| Dạng | Bộ lọc Đơn vị | Số trên màn | Kết quả bấm [Xuất Excel] |
|---|---|---|---|
| ① | Toàn quốc (đúng bộ lọc đối tác) | 2 / 23.000.000 / 11.500.000 | **200**, `BaoCaoChiPhiTheoDonVi_20260806_1335.xlsx`, 6 676 B, md5 `710b2bfb…` |
| ② | Cục Bổ trợ tư pháp - Bộ Tư pháp | 2 / 23.000.000 / 11.500.000 | **200**, `BaoCaoChiPhiTheoDonVi_20260806_1336.xlsx`, 6 670 B, md5 `6cb0acf8…` |

- **Tên tệp hai lượt khác nhau** (`…_1335` vs `…_1336`) ⇒ hai lần xuất trong cùng ngày không đè tệp nhau,
  đúng lý do BA chốt ở `:85`.
- **Mở tệp ra đọc bằng `openpyxl`** (không dừng ở "200 + có byte"): cả 2 tệp có sheet *"Chi phí theo đơn vị"*,
  đủ 4 mục header `:1092` đòi (`BC Chi phí theo đơn vị` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` ·
  `Đơn vị: …` · `Ngày tạo: 06/08/2026`), và bảng chéo **hàng = đơn vị** đủ 4 cột đặc tả FR-IX-16 (`:731-761`)
  đòi: *Đơn vị · Số hồ sơ · Tổng chi phí (₫) · Trung bình chi phí (₫)*. Số liệu khớp màn từng con số.
- **Tệp bám đúng bộ lọc:** dòng header tệp ① ghi `Đơn vị: Toàn quốc`, tệp ② ghi `Đơn vị: Cục Bổ trợ tư pháp -
  Bộ Tư pháp`; md5 hai tệp khác nhau.
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò, đúng màn,
đúng bộ lọc của đối tác.

### Bằng chứng

- [`image/CPCTHTTDVQL_06-01-cbnv-man-hinh-truoc-khi-xuat.png`](image/CPCTHTTDVQL_06-01-cbnv-man-hinh-truoc-khi-xuat.png)
  — phiên vai trò CB Nghiệp vụ TW, báo cáo đã hiện đủ số liệu, nút [Xuất Excel] đang bật.
- 🔴 [`image/CPCTHTTDVQL_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png`](image/CPCTHTTDVQL_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, báo cáo hiện đủ số liệu và **hai nút Xuất đang bấm được**.
  *Ghi chú thẳng thắn:* khung thông báo *"Forbidden"* chỉ sống ~3,3 giây; đã thử **4 cách hẹn giờ** khác nhau
  mà ảnh về đều không có khung, trong khi phép đo bằng máy ở cùng thời điểm xác nhận khung đang hiện và có
  kích thước thật. Nhiều khả năng công cụ chụp chờ trang hết hoạt ảnh mới bấm máy. Bằng chứng của chính chữ
  đó nằm ở tệp chữ bên dưới (có mốc giờ + toạ độ khung) và ở phản hồi 403 kèm số hiệu request.
- [`image/CPCTHTTDVQL_06-thong-bao-va-phan-hoi-may-chu.txt`](image/CPCTHTTDVQL_06-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt, phản hồi máy chủ, kết quả đọc nội dung 2 tệp .xlsx, và mục ghi hiện
  tượng lạ không tái hiện được.
- [`image/CPCTHTTDVQL_06-xuat-excel.xlsx`](image/CPCTHTTDVQL_06-xuat-excel.xlsx) ·
  [`image/CPCTHTTDVQL_06-xuat-excel-bienthe2.xlsx`](image/CPCTHTTDVQL_06-xuat-excel-bienthe2.xlsx) — hai tệp
  thật hệ thống giao ra.

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_03` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`) | 200, ra đủ số liệu | **200**, nhận được tệp .xlsx đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT có được xuất báo cáo thống kê không"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**, và **không** kéo verdict: dù BA chốt
  hướng nào thì hành vi hiện tại vẫn lệch `:117`. Lập luận đầy đủ ở
  [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7 Sửa 1.
- **Cùng nguyên nhân gốc với** `BUG-CPHTCT-006` (cùng Phần 4), `BUG-SLCTHT-006` (Phần 2) và `BUG-SLHDVM-006`
  (Phần 3) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã `ERR-PERM-SYS-00-01`. Dev sửa một chỗ có
  thể đóng cả bốn; QA vòng sau vẫn phải verify riêng từng case trên đúng màn của nó.
- **Hiện tượng lạ, đã thử tái hiện nhưng KHÔNG lặp lại — không log thành lỗi:** ở lượt đo đầu, cú xuất thứ
  hai trả **401** (thay vì 403) rồi FE tự gọi `/auth/logout` và đá về `/login` kèm chữ *"Phiên làm việc hết
  hạn"*, dù phiên mới đăng nhập ~2 phút. Đã thử tái hiện 2 đường (gọi thẳng máy chủ và bấm trên giao diện):
  cú 403 **không** giết phiên — kho lưu phiên không đổi, gọi lành tính sau đó vẫn 200. Ghi lại kèm số hiệu
  request ở tệp chữ § D để vòng sau có mốc đối chiếu.

### Khối giao việc

```
🔁 CÒN LỖI — chuyển lại dev.

■ CÒN LỖI Ở ĐÂU
Vai trò Quản trị hệ thống (tài khoản admin) — đúng vai trò trong ảnh nghiệm thu:
   [Xem báo cáo] → OK. Hiện đủ số liệu, hai nút Xuất bật sáng.
   [Xuất Excel]  → KHÔNG ra tệp. Màn hiện đúng một chữ "Forbidden"
                   (máy chủ trả 403 · mã ERR-PERM-SYS-00-01)
Đúng hiện tượng ô "TKM phản hồi lần 1" đã ghi. Đo 3 lượt (2 lượt bấm trên giao diện, 1 lượt
gọi thẳng máy chủ) — kết quả giống hệt nhau.

■ VÌ SAO LÀ LỖI (đặc tả srs-fr-11-bao-cao.md)
1. Dòng :79 — kiểm quyền phải nằm ở ĐẦU luồng, nên bước Xem và bước Xuất phải cùng một quy
   tắc quyền. Hiện đang cho xem đủ số liệu rồi mới chặn ở bước xuất.
2. Dòng :117 — khi từ chối phải hiện câu tiếng Việt báo người dùng không có quyền xem báo
   cáo. Hiện đang ném thẳng chuỗi kỹ thuật tiếng Anh của máy chủ ra cho người dùng cuối.
KHÔNG phải chờ BA mới sửa được: câu hỏi "QTHT có được xuất báo cáo không" đã gửi BA, nhưng
trả lời hướng nào thì vẫn là lỗi — nếu không được xuất thì phải chặn từ bước Xem và báo bằng
tiếng Việt; nếu được xuất thì đang chặn nhầm.

■ ĐÃ HẾT LỖI — ĐỪNG ĐỤNG LẠI
Cán bộ Nghiệp vụ Trung ương xuất Excel tốt ở CẢ 2 cấu hình bộ lọc: tệp mở đọc được, đầu tệp
đủ tên báo cáo + kỳ + đơn vị + ngày tạo, bảng đủ 4 cột (Đơn vị · Số hồ sơ · Tổng chi phí ·
Trung bình chi phí), số khớp đúng số trên màn. Đổi bộ lọc sang một đơn vị cụ thể thì dòng
"Đơn vị" trong tệp đổi theo và tệp ra mã kiểm tra khác hẳn — tệp bám bộ lọc, không xuất cứng.
Hai lượt xuất ra hai tên tệp khác nhau. Hết câu "Không thể tạo file xuất. Vui lòng thử lại."
(đối tác báo 16/07).

■ AI SỬA
Dev BE — cho bước Xem và bước Xuất dùng chung quy tắc quyền; từ chối thì trả thông báo theo :117.
Dev FE — không đẩy chuỗi máy chủ trả về ra thẳng màn hình người dùng.
BA     — chốt "QTHT có được xuất báo cáo không" để dev chọn hướng sửa.

■ ĐÃ ĐO
06/08/2026 · bản dựng V1.0.8 · admin (QTHT/TW) + cbnv_tw_03 (CB Nghiệp vụ/TW) · BC Chi phí
theo đơn vị · Kỳ Năm 2026 · 2 cấu hình đơn vị (Toàn quốc và Cục Bổ trợ tư pháp) · 5 lượt bấm
xuất · không tạo/sửa/xoá bản ghi nào. Bằng chứng: ô "Ảnh/video verify" cùng dòng.

────────── CÁCH VERIFY SAU KHI DEV FIX ──────────
Cần trước: tài khoản admin (QTHT, cấp TW) · màn Báo cáo thống kê (/bao-cao) · kỳ báo cáo phải
CÓ dữ liệu (báo cáo trống thì nút Xuất tự tắt, đo vô nghĩa).

B1. admin → BC Chi phí theo đơn vị · Kỳ Năm 01/01–31/12/2026 · Toàn quốc → [Xem báo cáo]
    (bấm đúng 1 lần). Ghi lại Tổng hồ sơ · Tổng chi phí và các dòng đơn vị.
B2. [Xuất Excel] → chép nguyên văn chữ hiện ra; kiểm có tệp về máy không.
B3. Đối chiếu bằng đường thứ 2: tab Network xem lời gọi xuất trả mã gì. Có tệp thì MỞ RA ĐỌC,
    so với số ở B1.
B4. Lặp B1–B3 bằng cbnv_tw_03; thêm 1 lượt đổi Đơn vị sang một đơn vị cụ thể để chắc tệp vẫn
    bám bộ lọc (dòng "Đơn vị" trong tệp phải đổi theo).

✅ PASS — đạt 1 trong 2:
   a) admin xuất được tệp .xlsx mở đọc được, số khớp màn, không thông báo từ chối; HOẶC
   b) nếu BA chốt QTHT không được xuất → chặn NGAY ở bước [Xem báo cáo], kèm câu tiếng Việt.
❌ FAIL nếu: còn "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào cho người dùng cuối ·
   vẫn cho xem đủ rồi mới chặn ở bước Xuất · chỉ ẩn/làm mờ nút Xuất mà bước Xem vẫn vào được ·
   Cán bộ Nghiệp vụ bị chặn theo · tệp xuất thiếu cột hoặc thiếu dòng đơn vị so với màn.

⚠️ BẪY
1. Cán bộ Nghiệp vụ xuất được KHÔNG chứng minh đã fix — vai trò đó vốn đã tốt từ 06/08. Phép đo
   quyết định là chạy bằng chính tài khoản admin.
2. Tải được tệp chưa đủ — phải MỞ TỆP RA ĐỌC mới chốt.
3. Đừng chấm Fail vì tên tệp BaoCaoChiPhiTheoDonVi_… (khuôn tên đã chốt 04/08/2026); vì số liệu
   khác ảnh nghiệm thu (25 hồ sơ / 226.308.268 đ); hay vì bảng chỉ có một dòng đơn vị — môi
   trường thử chỉ phát sinh chi phí ở một đơn vị.
4. Khung thông báo sống ~3 giây và đổi chữ NGAY TRONG khung cũ, không mọc khung mới → công cụ
   đếm "khung mới" chỉ thấy "Đang tạo file..." rồi báo nhầm là im lặng. Phải theo dõi nội dung
   khung theo thời gian. Ứng dụng gửi lời gọi xuất qua XHR chứ không qua fetch — bộ theo dõi
   chỉ móc fetch sẽ đếm ra 0 lời gọi. Tải lại trang trước khi đo — tab mở lâu vẫn chạy mã cũ.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa.

---

## Bug Summary Table (Phần 4 — bổ sung dòng 258)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CPCTHTTLHDN-006 | Major | P1 | Permission | `CPCTHTTLHDN_06` (tab `bug` dòng 258) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CPCTHTTLHDN_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png`](image/CPCTHTTLHDN_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png) | Open |

---

## BUG-CPCTHTTLHDN-006 — Vai trò QTHT xem được BC Chi phí theo loại hình DN nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:58 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế a của đối tác (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được, tệp mở đọc được, bảng trong tệp có **đủ 7 thông tin** đặc tả `:831-839` đòi, số khớp
> màn từng con số. Vế b (*"Forbidden"*, 31/07) **tái hiện nguyên vẹn** ở đúng vai trò đối tác đã dùng.
> N = 3 lượt bấm xuất · M = 2 dạng bộ lọc (+1 biến thể kiểm chứng) · **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chi phí theo loại hình DN**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ bảng 7 cột và **hiện hai nút [Xuất Excel] /
[Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**.
Chữ hiện ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy
chủ. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, cấp TW) — đúng vai trò trên bằng chứng của
   đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chi phí theo loại hình DN**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc**; **để trống ô Loại DN** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: bảng hiện đầy đủ 7 cột (*Quy mô DN · Số hồ sơ · Tổng chi phí · Mức hỗ
   trợ (%) · Trần / hồ sơ · Trần chi phí · Chênh lệch*), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_03`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng.
  Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không cho xem đầy đủ số
  liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò**.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 13:55:**

- [Xem báo cáo]: **200**, màn hiện đủ bảng 7 cột, dòng `Siêu nhỏ | 2 | 23.000.000 ₫ | 100,0 | 30.000.000 ₫ |
  60.000.000 ₫ | -37.000.000 ₫` — **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được**.
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo; chữ người dùng đọc được:
  *"Đang tạo file..."* → **"Forbidden"** (hiện ở mốc 151 ms, khung rộng 118 px cao 40 px, tắt ở 3 478 ms);
  **0 tệp**, **0 blob**.
- Nguyên văn phản hồi:
  ```json
  {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
   "timestamp":"2026-08-06T06:55:34.920Z","requestId":"1ee92915-4c4a-47ef-8942-c98263da501b"}}
  ```

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_03`) — cùng màn, cùng kỳ:**

| Dạng | Bộ lọc Loại DN | Màn hình | Kết quả bấm [Xuất Excel] |
|---|---|---|---|
| ① | **để trống** (đúng bộ lọc đối tác) | 1 dòng *Siêu nhỏ*, 7 cột đủ | **200**, `BaoCaoChiPhiTheoLoaiDn_20260806_1352.xlsx`, 6 774 B, md5 `01cca4cf…` |
| ② | **Siêu nhỏ** (`fd_loaiDn=SIEU_NHO`) | 1 dòng *Siêu nhỏ* | **200**, `BaoCaoChiPhiTheoLoaiDn_20260806_1353.xlsx`, 6 775 B, md5 `57ced0ca…` |
| ③ | **Nhỏ** (`fd_loaiDn=NHO`) | **rỗng**, có chữ báo không có dữ liệu | nút Xuất **tự tắt** — đúng, vì không có gì để xuất |

- **Tên tệp hai lượt khác nhau** (`…_1352` vs `…_1353`) ⇒ hai lần xuất trong cùng ngày không đè tệp nhau,
  đúng lý do BA chốt ở `:85`.
- **Mở tệp ra đọc bằng `openpyxl`**: sheet *"Chi phí theo loại DN"*, đủ 4 mục header `:1092` đòi, và bảng có
  **đủ 7 thông tin** `:831-839` đòi — `Quy mô DN · Số hồ sơ · Tổng chi phí (₫) · Mức hỗ trợ (%) · Trần / hồ
  sơ (₫) · Trần chi phí (₫) · Chênh lệch (₫)`. Số liệu khớp màn từng con số; chênh lệch `-37.000.000` khớp
  công thức `:839` (23.000.000 − 60.000.000, chi phí chưa chạm trần NĐ55).
- Ô *Loại DN* có đúng **3 lựa chọn** *Siêu nhỏ / Nhỏ / Vừa* — khớp enum `:823` (`SIEU_NHO / NHO / VUA`).
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò, đúng màn,
đúng bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CPCTHTTLHDN_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png`](image/CPCTHTTLHDN_06-02-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, bảng 7 cột hiện đủ và **hai nút Xuất đang bấm được**.
  *Ghi chú thẳng thắn:* khung thông báo *"Forbidden"* chỉ sống ~3,3 giây nên **không kịp vào ảnh**; ở case
  liền trước đã thử 4 cách hẹn giờ đều trượt, trong khi đo bằng máy cùng thời điểm xác nhận khung hiện thật.
  Bằng chứng của chính chữ đó nằm ở tệp chữ bên dưới và ở phản hồi 403 kèm số hiệu request.
- [`image/CPCTHTTLHDN_06-thong-bao-va-phan-hoi-may-chu.txt`](image/CPCTHTTLHDN_06-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt, phản hồi máy chủ, kết quả đọc nội dung tệp .xlsx, và ghi rõ giới hạn
  của phép đo bám-bộ-lọc.
- [`image/CPCTHTTLHDN_06-xuat-excel.xlsx`](image/CPCTHTTLHDN_06-xuat-excel.xlsx) ·
  [`image/CPCTHTTLHDN_06-xuat-excel-loc-sieunho.xlsx`](image/CPCTHTTLHDN_06-xuat-excel-loc-sieunho.xlsx) —
  hai tệp thật hệ thống giao ra.

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_03` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`) | 200, ra đủ bảng 7 cột | **200**, nhận được tệp .xlsx đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT có được xuất báo cáo thống kê không"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**, và **không** kéo verdict: dù BA chốt
  hướng nào thì hành vi hiện tại vẫn lệch `:117`. Lập luận đầy đủ ở
  [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7 Sửa 1.
- **Giới hạn của phép đo bám-bộ-lọc, nói thẳng:** môi trường thử chỉ có dữ liệu quy mô *Siêu nhỏ*, nên tệp ①
  và ② **trùng nội dung** (chỉ khác tên và md5 do dấu thời gian bên trong). Cặp ①–② vì thế **không** tự chứng
  minh tệp bám bộ lọc; điều chứng minh được là biến thể ③ (*Nhỏ* → màn rỗng, nút Xuất tự tắt).
- **Cùng nguyên nhân gốc với** `BUG-CPHTCT-006`, `BUG-CPCTHTTDVQL-006` (cùng Phần 4), `BUG-SLCTHT-006`
  (Phần 2) và `BUG-SLHDVM-006` (Phần 3) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã
  `ERR-PERM-SYS-00-01`. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng sau vẫn phải verify riêng từng case.

### Khối giao việc

```
🔁 CÒN LỖI — chuyển lại dev.

■ CÒN LỖI Ở ĐÂU
Vai trò Quản trị hệ thống (tài khoản admin) — đúng vai trò trong ảnh nghiệm thu:
   [Xem báo cáo] → OK. Hiện đủ bảng 7 cột, hai nút Xuất bật sáng.
   [Xuất Excel]  → KHÔNG ra tệp. Màn hiện đúng một chữ "Forbidden"
                   (máy chủ trả 403 · mã ERR-PERM-SYS-00-01)
Đúng hiện tượng ô "TKM phản hồi lần 1" đã ghi.

■ VÌ SAO LÀ LỖI (đặc tả srs-fr-11-bao-cao.md)
1. Dòng :79 — kiểm quyền phải nằm ở ĐẦU luồng, nên bước Xem và bước Xuất phải cùng một quy
   tắc quyền. Hiện đang cho xem đủ số liệu rồi mới chặn ở bước xuất.
2. Dòng :117 — khi từ chối phải hiện câu tiếng Việt báo người dùng không có quyền xem báo
   cáo. Hiện đang ném thẳng chuỗi kỹ thuật tiếng Anh của máy chủ ra cho người dùng cuối.
KHÔNG phải chờ BA mới sửa được: câu hỏi "QTHT có được xuất báo cáo không" đã gửi BA, nhưng
trả lời hướng nào thì vẫn là lỗi — nếu không được xuất thì phải chặn từ bước Xem và báo bằng
tiếng Việt; nếu được xuất thì đang chặn nhầm.

■ ĐÃ HẾT LỖI — ĐỪNG ĐỤNG LẠI
Cán bộ Nghiệp vụ Trung ương xuất Excel tốt: tệp mở đọc được, đầu tệp đủ tên báo cáo + kỳ +
đơn vị + ngày tạo, bảng có ĐỦ 7 cột nghiệp vụ đòi (Quy mô DN · Số hồ sơ · Tổng chi phí · Mức
hỗ trợ % · Trần mỗi hồ sơ · Trần chi phí · Chênh lệch), số khớp đúng số trên màn; hai lượt
xuất ra hai tên tệp khác nhau. Ô lọc "Loại DN" có đúng 3 lựa chọn Siêu nhỏ / Nhỏ / Vừa và có
tác dụng thật. Hết câu "Không thể tạo file xuất. Vui lòng thử lại." (đối tác báo 16/07).

■ ĐỪNG HIỂU NHẦM MỘT CHỖ
Chọn "Loại DN = Nhỏ" thì màn ra rỗng. KHÔNG phải do môi trường thiếu dữ liệu quy mô Nhỏ — kỳ
đó CÓ hồ sơ quy mô Nhỏ trị giá 15.000.000 đ (CT-QAW7-CLOSED); chính báo cáo này xếp nhầm hồ
sơ đó sang dòng Siêu nhỏ. Đó là lỗi RIÊNG, đã tách phiếu BCTK_QA05 (dòng 368), không tính vào
phiếu này.

■ AI SỬA
Dev BE — cho bước Xem và bước Xuất dùng chung quy tắc quyền; từ chối thì trả thông báo theo :117.
Dev FE — không đẩy chuỗi máy chủ trả về ra thẳng màn hình người dùng.
BA     — chốt "QTHT có được xuất báo cáo không" để dev chọn hướng sửa.

■ ĐÃ ĐO
06/08/2026 · bản dựng V1.0.8 · admin (QTHT/TW) + cbnv_tw_03 (CB Nghiệp vụ/TW) · BC Chi phí
theo loại hình DN · Kỳ Năm 2026 · Toàn quốc · 3 cấu hình Loại DN (để trống / Siêu nhỏ / Nhỏ) ·
3 lượt bấm xuất · không tạo/sửa/xoá bản ghi nào. Bằng chứng: ô "Ảnh/video verify" cùng dòng.

────────── CÁCH VERIFY SAU KHI DEV FIX ──────────
Cần trước: tài khoản admin (QTHT, cấp TW) · màn Báo cáo thống kê (/bao-cao) · kỳ báo cáo phải
CÓ dữ liệu (báo cáo trống thì nút Xuất tự tắt, đo vô nghĩa).

B1. admin → BC Chi phí theo loại hình DN · Kỳ Năm 01/01–31/12/2026 · Toàn quốc · để trống ô
    Loại DN → [Xem báo cáo] (bấm đúng 1 lần). Ghi lại đủ 7 cột của bảng.
B2. [Xuất Excel] → chép nguyên văn chữ hiện ra; kiểm có tệp về máy không.
B3. Đối chiếu bằng đường thứ 2: tab Network xem lời gọi xuất trả mã gì. Có tệp thì MỞ RA ĐỌC,
    so với 7 cột ở B1.
B4. Lặp B1–B3 bằng cbnv_tw_03; thêm 1 lượt chọn Loại DN = quy mô CÓ dữ liệu để chắc tệp vẫn
    khớp màn.

✅ PASS — đạt 1 trong 2:
   a) admin xuất được tệp .xlsx mở đọc được, đủ 7 cột và số khớp màn, không thông báo từ chối;
   b) nếu BA chốt QTHT không được xuất → chặn NGAY ở bước [Xem báo cáo], kèm câu tiếng Việt.
❌ FAIL nếu: còn "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào cho người dùng cuối ·
   vẫn cho xem đủ rồi mới chặn ở bước Xuất · chỉ ẩn/làm mờ nút Xuất mà bước Xem vẫn vào được ·
   Cán bộ Nghiệp vụ bị chặn theo · tệp xuất thiếu bất kỳ cột nào trong 7 cột.

⚠️ BẪY
1. Cán bộ Nghiệp vụ xuất được KHÔNG chứng minh đã fix — vai trò đó vốn đã tốt từ 06/08. Phép đo
   quyết định là chạy bằng chính tài khoản admin.
2. Tải được tệp chưa đủ — phải MỞ TỆP RA ĐỌC mới chốt.
3. Đừng chấm Fail vì cột Chênh lệch âm (chi phí chưa chạm trần theo Nghị định 55 — đúng công
   thức); vì tên tệp BaoCaoChiPhiTheoLoaiDn_… (khuôn tên đã chốt 04/08/2026); hay vì bảng ít
   dòng quy mô — điều phải đúng là TỆP KHỚP MÀN. Chuyện xếp sai quy mô doanh nghiệp theo phiếu
   BCTK_QA05, đừng chấm vào phiếu này.
4. Khung thông báo sống ~3 giây và đổi chữ NGAY TRONG khung cũ, không mọc khung mới → công cụ
   đếm "khung mới" chỉ thấy "Đang tạo file..." rồi báo nhầm là im lặng. Phải theo dõi nội dung
   khung theo thời gian. Ứng dụng gửi lời gọi xuất qua XHR chứ không qua fetch. Tải lại trang
   trước khi đo — tab mở lâu vẫn chạy mã cũ.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa.

---

## Bug Summary Table (Phần 4 — bổ sung dòng 263 + 264)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CPCTHTTTG-005 | Major | P1 | Permission | `CPCTHTTTG_05` (tab `bug` dòng 263) — nút **Xuất Excel** | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png) | Open |
| BUG-CPCTHTTTG-006 | Major | P1 | Permission | `CPCTHTTTG_06` (tab `bug` dòng 264) — nút **Xuất PDF** | `srs-fr-11-bao-cao.md:117` · `:79` · `:1053` | [`image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png) | Open |

---

## BUG-CPCTHTTTG-005 — Vai trò QTHT xem được BC Chi phí theo thời gian nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 14:30 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế a của đối tác (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được, tệp mở đọc được, dãy theo kỳ có **đủ 3 thông tin** đặc tả `:869` đòi, số khớp màn.
> Vế b (*"Forbidden"*, 31/07) **tái hiện nguyên vẹn** ở đúng vai trò đối tác đã dùng.
> N = 3 lượt bấm xuất · M = 3 biến thể kỳ (+1 lượt gọi thẳng máy chủ) · **không seed, không đổi dữ liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chi phí theo thời gian**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu và biểu đồ, **hiện hai nút [Xuất Excel]
/ [Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp
nào**. Chữ hiện ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của
máy chủ. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, cấp TW) — đúng vai trò trên bằng chứng của
   đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chi phí theo thời gian**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: hiện *Tổng chi phí toàn kỳ*, *Tổng hồ sơ toàn kỳ*, biểu đồ đường và
   bảng *Theo kỳ*, không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_03`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1), việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng.
  Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn ngay từ bước Xem, chứ không cho xem đầy đủ số
  liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- Theo `srs-fr-11-bao-cao.md:1052`, điều kiện hiện nút *Xuất Excel* chỉ là **"sau khi đã Xem báo cáo"**,
  không kèm điều kiện vai trò.

### Kết quả thực tế

**Vai trò `admin` (QTHT · BTP · TW) — 14:30, bản dựng V1.0.8**

- Bước **Xem báo cáo**: **không** bị chặn. Màn hiện đủ *Tổng chi phí toàn kỳ 23.000.000 · Tổng hồ sơ toàn kỳ
  2*, có biểu đồ đường, bảng *Theo kỳ* đủ dòng — **y hệt** số liệu vai trò CB Nghiệp vụ nhìn thấy. Hai nút
  [Xuất Excel] / [Xuất PDF] **bấm được** (không mờ, không ẩn).
- Bước **Xuất Excel**: đo bằng bộ theo dõi cài **trước khi bấm** (không lọc trùng, đọc `innerText`, lấy mẫu
  chữ mỗi 150 ms, móc cả `fetch` lẫn XHR) —
  - `+89 ms` khung thông báo hiện đúng một chữ **`"Forbidden"`**, khung rộng 1432 px cao 41 px (hiện thật,
    không phải node ẩn); `+3539 ms` khung tự tắt.
  - **1** request kèm lượt bấm: XHR `POST /api/v1/bao-cao/export` → **403**.
  - **0** tệp về máy, **0** blob.
  - Nguyên văn phản hồi:
    `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","timestamp":"2026-08-06T07:30:18.775Z","requestId":"5a47d617-f4c3-4ab3-905e-7d9a592db2d6"}}`

**Vai trò `cbnv_tw_03` (CB Nghiệp vụ TW — tác nhân đặc tả `:62`) — cùng màn, cùng bộ lọc**

| Biến thể | Kỳ báo cáo | Màn hình | Kết quả bấm [Xuất Excel] |
|:-:|---|---|---|
| ① | **Năm** 01/01 → 31/12/2026 (đúng ảnh đối tác) | 23.000.000 · 2 hồ sơ · 1 dòng *Năm 2026* | **200**, tệp `BaoCaoChiPhiTheoThoiGian_20260806_1413.xlsx` (6.660 B) |
| ② | **Khoảng tùy chọn** 01/06 → 30/06/2026 | 23.000.000 · 2 hồ sơ · 1 dòng *01/06/2026 - 30/06/2026* | **200**, tệp `…_20260806_1425.xlsx` (6.659 B) |
| ③ | **Quý** (hệ thống tự đặt 01/07 → 30/09/2026, kỳ không có dữ liệu) | *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* | nút Xuất **tự tắt** — đúng, vì không có gì để xuất |

- **Tên tệp hai lượt khác nhau** (`…_1413` vs `…_1425`) ⇒ hai lần xuất trong cùng ngày không đè tệp nhau,
  đúng lý do BA chốt ở `:85`.
- **Mở tệp ra đọc bằng `openpyxl`**: sheet *"Chi phí theo thời gian"*, đủ 4 mục header `:1092` đòi (tên báo
  cáo · kỳ · đơn vị · ngày tạo), và bảng *Theo kỳ* có **đủ 3 thông tin** `:869` đòi — nhãn kỳ · số hồ sơ ·
  tổng chi phí. Số liệu khớp màn từng con số. Đổi kỳ thì **nhãn kỳ và khoảng ngày trong tệp đổi theo** ⇒ tệp
  bám bộ lọc, không xuất cứng.
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò, đúng màn,
đúng bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png)
  — **ảnh chụp được đúng khung thông báo "Forbidden"** trên phiên vai trò QTHT (góc phải: *Quản trị hệ thống ·
  BTP · TW*), bản dựng V1.0.8, báo cáo bên dưới vẫn hiện đủ số liệu và hai nút Xuất vẫn bấm được. Ảnh chụp ở
  lượt [Xuất PDF] liền sau lượt [Xuất Excel] — **cùng màn, cùng tài khoản, cùng chữ, cùng mã lỗi**.
- [`image/CPCTHTTTG_05-B1-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc-V108.png`](image/CPCTHTTTG_05-B1-qtht-xem-duoc-bao-cao-nut-xuat-bam-duoc-V108.png)
  — trạng thái ngay trước khi bị từ chối: QTHT xem được đủ số liệu, nút Xuất đang bấm được.
- [`image/CPCTHTTTG_05-thong-bao-va-phan-hoi-may-chu.txt`](image/CPCTHTTTG_05-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt kèm mốc mili-giây, phản hồi máy chủ kèm số hiệu request, kết quả đọc
  nội dung tệp .xlsx.
- [`image/CPCTHTTTG_05-xuat-excel-dang1.xlsx`](image/CPCTHTTTG_05-xuat-excel-dang1.xlsx) ·
  [`image/CPCTHTTTG_05-xuat-excel-dang2-khoang-thang6.xlsx`](image/CPCTHTTTG_05-xuat-excel-dang2-khoang-thang6.xlsx)
  — hai tệp thật hệ thống giao ra.

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_03` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`) | 200, ra đủ số liệu + biểu đồ | **200**, nhận được tệp .xlsx đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT có được xuất báo cáo thống kê không"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**, và **không** kéo verdict: dù BA chốt
  hướng nào thì hành vi hiện tại vẫn lệch `:117`. Lập luận đầy đủ ở
  [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7 Sửa 1.
- **Cùng nguyên nhân gốc với** `BUG-CPHTCT-006`, `BUG-CPCTHTTDVQL-006`, `BUG-CPCTHTTLHDN-006`,
  `BUG-CPCTHTTTG-006` (cùng Phần 4), `BUG-SLCTHT-006` (Phần 2) và `BUG-SLHDVM-006` (Phần 3) — cùng endpoint
  `POST /api/v1/bao-cao/export`, cùng mã `ERR-PERM-SYS-00-01`. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng
  sau vẫn phải verify riêng từng case.

### Khối giao việc

```
🔁 CÒN LỖI — chuyển lại dev.

■ CÒN LỖI Ở ĐÂU
Vai trò Quản trị hệ thống (tài khoản admin) — đúng vai trò trong ảnh nghiệm thu:
   [Xem báo cáo] → OK. Hiện đủ số liệu và biểu đồ, hai nút Xuất bật sáng.
   [Xuất Excel]  → KHÔNG ra tệp. Màn hiện đúng một chữ "Forbidden"
                   (máy chủ trả 403 · mã ERR-PERM-SYS-00-01)
Đúng hiện tượng ô "TKM phản hồi lần 1" đã ghi. Lần này đã CHỤP ĐƯỢC ẢNH khung thông báo đó.

■ VÌ SAO LÀ LỖI (đặc tả srs-fr-11-bao-cao.md)
1. Dòng :79 — kiểm quyền phải nằm ở ĐẦU luồng, nên bước Xem và bước Xuất phải cùng một quy
   tắc quyền. Hiện đang cho xem đủ số liệu rồi mới chặn ở bước xuất.
2. Dòng :117 — khi từ chối phải hiện câu tiếng Việt báo người dùng không có quyền xem báo
   cáo. Hiện đang ném thẳng chuỗi kỹ thuật tiếng Anh của máy chủ ra cho người dùng cuối.
KHÔNG phải chờ BA mới sửa được: câu hỏi "QTHT có được xuất báo cáo không" đã gửi BA, nhưng
trả lời hướng nào thì vẫn là lỗi — nếu không được xuất thì phải chặn từ bước Xem và báo bằng
tiếng Việt; nếu được xuất thì đang chặn nhầm.

■ ĐÃ HẾT LỖI — ĐỪNG ĐỤNG LẠI
Cán bộ Nghiệp vụ Trung ương xuất Excel tốt: tệp mở đọc được, đầu tệp đủ tên báo cáo + kỳ +
đơn vị + ngày tạo, bảng "Theo kỳ" đủ 3 thông tin nghiệp vụ đòi (nhãn kỳ · số hồ sơ · tổng chi
phí), số khớp đúng số trên màn. Đổi kỳ sang Khoảng tùy chọn 01/06–30/06/2026 thì nhãn kỳ và
khoảng ngày trong tệp đổi theo — tệp bám bộ lọc, không xuất cứng. Chọn kỳ Quý (quý không có
dữ liệu) thì màn ra rỗng và nút Xuất tự tắt, đúng mong đợi. Hai lượt xuất ra hai tên tệp khác
nhau. Hết câu "Không thể tạo file xuất. Vui lòng thử lại." (đối tác báo 16/07).

■ AI SỬA
Dev BE — cho bước Xem và bước Xuất dùng chung quy tắc quyền; từ chối thì trả thông báo theo :117.
Dev FE — không đẩy chuỗi máy chủ trả về ra thẳng màn hình người dùng.
BA     — chốt "QTHT có được xuất báo cáo không" để dev chọn hướng sửa.

■ ĐÃ ĐO
06/08/2026 · bản dựng V1.0.8 · admin (QTHT/TW) + cbnv_tw_03 (CB Nghiệp vụ/TW) · BC Chi phí
theo thời gian · Kỳ Năm 2026 · Toàn quốc · thêm 2 cấu hình kỳ (Khoảng tùy chọn tháng 6; Quý
không có dữ liệu) · 3 lượt bấm xuất · không tạo/sửa/xoá bản ghi nào. Bằng chứng: ô "Ảnh/video
verify" cùng dòng.
Ba lỗi khác gặp lúc đo, đã tách phiếu riêng, KHÔNG tính vào phiếu này:
   · BCTK_QA07 (dòng 370) — bấm [Xem báo cáo] lần 2 thì hai nút Xuất bị khoá cả phiên
   · BCTK_QA08 (dòng 371) — giao diện không chọn được nhiều điểm kỳ, biểu đồ đường luôn 1 điểm
   · BCTK_QA09 (dòng 372) — tệp xuất in mã kỹ thuật "KHOANG" thay cho chữ tiếng Việt

────────── CÁCH VERIFY SAU KHI DEV FIX ──────────
Cần trước: tài khoản admin (QTHT, cấp TW) · màn Báo cáo thống kê (/bao-cao) · kỳ báo cáo phải
CÓ dữ liệu (báo cáo trống thì nút Xuất tự tắt, đo vô nghĩa).

B1. admin → BC Chi phí theo thời gian · Kỳ Năm 01/01–31/12/2026 · Toàn quốc → [Xem báo cáo]
    (bấm đúng 1 lần). Ghi lại Tổng chi phí · Tổng hồ sơ và các dòng bảng "Theo kỳ".
B2. [Xuất Excel] → chép nguyên văn chữ hiện ra; kiểm có tệp về máy không.
B3. Đối chiếu bằng đường thứ 2: tab Network xem lời gọi xuất trả mã gì. Có tệp thì MỞ RA ĐỌC,
    so với số ở B1.
B4. Lặp B1–B3 bằng cbnv_tw_03; thêm 1 lượt đổi kỳ (vd Khoảng tùy chọn 01/06–30/06/2026) để
    chắc nhãn kỳ trong tệp đổi theo bộ lọc.

✅ PASS — đạt 1 trong 2:
   a) admin xuất được tệp .xlsx mở đọc được, số khớp màn, không thông báo từ chối; HOẶC
   b) nếu BA chốt QTHT không được xuất → chặn NGAY ở bước [Xem báo cáo], kèm câu tiếng Việt.
❌ FAIL nếu: còn "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào cho người dùng cuối ·
   vẫn cho xem đủ rồi mới chặn ở bước Xuất · chỉ ẩn/làm mờ nút Xuất mà bước Xem vẫn vào được ·
   Cán bộ Nghiệp vụ bị chặn theo · tệp xuất thiếu thông tin so với màn.

⚠️ BẪY
1. Cán bộ Nghiệp vụ xuất được KHÔNG chứng minh đã fix — vai trò đó vốn đã tốt từ 06/08. Phép đo
   quyết định là chạy bằng chính tài khoản admin.
2. Tải được tệp chưa đủ — phải MỞ TỆP RA ĐỌC mới chốt.
3. Nút Xuất bị mờ dù báo cáo đang hiện số liệu = do đã bấm [Xem báo cáo] từ 2 lần trở lên (lỗi
   riêng BCTK_QA07). Tải lại trang, chọn lại bộ lọc, bấm đúng 1 lần.
4. Đừng chấm Fail vì tên tệp BaoCaoChiPhiTheoThoiGian_… (khuôn tên đã chốt 04/08/2026); vì số
   liệu khác ảnh nghiệm thu (25 hồ sơ / 226.308.268 đ); hay vì bảng chỉ có một dòng kỳ — điều
   phải đúng là TỆP KHỚP MÀN.
5. Khung thông báo sống ~3 giây và đổi chữ NGAY TRONG khung cũ, không mọc khung mới → công cụ
   đếm "khung mới" chỉ thấy "Đang tạo file..." rồi báo nhầm là im lặng. Phải theo dõi nội dung
   khung theo thời gian; muốn chụp ảnh thì hẹn giờ bấm nút sau ~2500 mili-giây rồi mới gọi lệnh
   chụp. Ứng dụng gửi lời gọi xuất qua XHR chứ không qua fetch. Tải lại trang trước khi đo.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa.

---

## BUG-CPCTHTTTG-006 — Vai trò QTHT xem được BC Chi phí theo thời gian nhưng bị chặn khi Xuất PDF, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 14:30 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế a của đối tác (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được tệp PDF **đúng khung hành chính TT17/2025** — A4, đầu trang có quốc hiệu + tiêu ngữ +
> tên cơ quan, cuối trang có ngày ký + họ tên + chỗ con dấu. Vế b (*"Forbidden"*, 31/07) **tái hiện nguyên
> vẹn** ở đúng vai trò đối tác đã dùng. N = 3 lượt bấm xuất · M = 2 biến thể kỳ · **không seed, không đổi dữ
> liệu nào**.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chi phí theo thời gian**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị đầy đủ số liệu; bấm [Xuất PDF] thì hộp thoại *"Tùy
chọn in báo cáo PDF"* **mở bình thường**, nhưng bấm [Xuất file] trong hộp thoại thì bị từ chối và **không
nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản
hồi kỹ thuật của máy chủ. Cùng thao tác, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp PDF bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, cấp TW).
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chi phí theo thời gian**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát số liệu hiện ra.
5. Bấm **[Xuất PDF]** → hộp thoại *"Tùy chọn in báo cáo PDF"* mở ra (Khổ giấy mặc định **A4**, Hướng giấy
   mặc định **Dọc**).
6. Bấm **[Xuất file]** trong hộp thoại — quan sát chữ hiện ra và xem có tệp nào về máy không.
7. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_03`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79`, việc kiểm quyền truy cập báo cáo nằm ở **đầu** luồng ⇒ bước Xem và bước
  Xuất phải nhất quán.
- Theo `srs-fr-11-bao-cao.md:1053`, điều kiện hiện nút *Xuất PDF* chỉ là **"sau khi đã Xem báo cáo"**, không
  kèm điều kiện vai trò.

### Kết quả thực tế

**Vai trò `admin` (QTHT · BTP · TW) — 14:30, bản dựng V1.0.8**

- Bước **Xem báo cáo**: **không** bị chặn, màn hiện đủ *23.000.000 · 2 hồ sơ*, hai nút Xuất bấm được.
- Bấm **[Xuất PDF]**: hộp thoại mở bình thường, **0** request (nút này chỉ mở hộp thoại).
- Bấm **[Xuất file]** trong hộp thoại — đo bằng bộ theo dõi cài **trước khi bấm**:
  - `+2565 ms` khung hiện *"Đang tạo file..."*; `+2715 ms` khung **đổi chữ ngay trong khung cũ** thành
    **`"Forbidden"`**, khung rộng 1440 px cao 53 px; `+6015 ms` khung tự tắt (~3,3 s).
  - **1** request: XHR `POST /api/v1/bao-cao/export` → **403**. **0** tệp, **0** blob.
  - Nguyên văn phản hồi:
    `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","timestamp":"2026-08-06T07:30:41.143Z","requestId":"f99880a3-1dad-4429-bc8f-50c1a2a90cd1"}}`

**Vai trò `cbnv_tw_03` (CB Nghiệp vụ TW) — cùng màn, cùng bộ lọc, khổ A4 hướng Dọc**

| Biến thể | Kỳ báo cáo | Kết quả bấm [Xuất file] |
|:-:|---|---|
| ① | **Năm** 01/01 → 31/12/2026 (đúng ảnh đối tác) | **200**, tệp `BaoCaoChiPhiTheoThoiGian_20260806_1426.pdf` (31.915 B) |
| ② | **Khoảng tùy chọn** 01/06 → 30/06/2026 | **200**, tệp `…_20260806_1428.pdf` (32.169 B) |

**Mở tệp PDF ra đọc bằng PyMuPDF** — tệp ①, 1 trang, khổ **595,3 × 841,9 pt = đúng A4 dọc**:

| Thành phần `:86` đòi | Có trong tệp? | Nguyên văn |
|---|:-:|---|
| Tên cơ quan ban hành (đầu trang) | ✅ | *CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP* |
| Quốc hiệu (đầu trang) | ✅ | *CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM* |
| Tiêu ngữ | ✅ | *Độc lập - Tự do - Hạnh phúc* |
| Ngày ký (cuối trang) | ✅ | *Ngày 06 tháng 08 năm 2026* |
| Họ tên cán bộ xuất báo cáo | ✅ | *CB Nghiệp vụ - Trung ương #03* |
| Chỗ trống cho con dấu | ✅ | *NGƯỜI XUẤT BÁO CÁO* / *(Ký, ghi rõ họ tên và đóng dấu)* |
| **Không** in dòng chức danh người ký | ✅ | không có dòng chức danh — đúng quyết định nghiệp vụ 04/08/2026 |
| Phông Times New Roman (hoặc bản tương thích số đo) | ✅ | `Tinos-Regular` / `Tinos-Bold` / `Tinos-Italic` |
| 4 mục header `:1092` | ✅ | tên BC · kỳ · đơn vị · ngày tạo |
| Dãy theo kỳ `:869` | ✅ | *Năm 2026 / 01/01/2026 / 31/12/2026 / 2 / 23.000.000* — khớp màn |

- **Tên tệp hai lượt khác nhau** (`…_1426` vs `…_1428`) ⇒ không đè tệp nhau, đúng `:86`.
- Tệp ② đổi dòng kỳ và dòng bảng theo bộ lọc ⇒ tệp **bám bộ lọc**, không xuất cứng.
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế a (`ERR-RPT-04`, `:116`) hết lỗi. Vế b (*"Forbidden"*) tái hiện nguyên vẹn.**

### Bằng chứng

- 🔴 [`image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/CPCTHTTTG_06-B2-qtht-thong-bao-Forbidden-khi-xuat-pdf-V108.png)
  — **ảnh chụp đúng khung thông báo "Forbidden"** trên phiên vai trò QTHT, bản dựng V1.0.8; báo cáo bên dưới
  vẫn hiện đủ số liệu và hai nút Xuất vẫn bấm được.
- [`image/CPCTHTTTG_06-A1-hop-thoai-tuy-chon-in-PDF-V108.png`](image/CPCTHTTTG_06-A1-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *Tùy chọn in báo cáo PDF* (A4 / A3 / Letter · Dọc / Ngang), để dev thấy rõ nút xuất thật là
  [Xuất file] chứ không phải [Xuất PDF].
- [`image/CPCTHTTTG_06-thong-bao-va-phan-hoi-may-chu.txt`](image/CPCTHTTTG_06-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn kèm mốc mili-giây, phản hồi máy chủ kèm số hiệu request, toàn văn nội dung tệp
  PDF đọc bằng máy, bảng đo cỡ chữ và phông nhúng.
- [`image/CPCTHTTTG_06-xuat-pdf-dang1.pdf`](image/CPCTHTTTG_06-xuat-pdf-dang1.pdf) ·
  [`image/CPCTHTTTG_06-xuat-pdf-dang2-khoang-thang6.pdf`](image/CPCTHTTTG_06-xuat-pdf-dang2-khoang-thang6.pdf)
  — hai tệp thật hệ thống giao ra.

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất PDF] → [Xuất file] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_03` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`) | 200, ra đủ số liệu | **200**, nhận được tệp .pdf đúng khung TT17/2025 | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- **Kỳ vọng "cuối trang có chức danh người ký" của đối tác KHÔNG phải khuyết tật.** Đặc tả `:86` đã chốt ngày
  **04/08/2026**: *"Không in dòng chức danh người ký — hồ sơ tài khoản không lưu chức vụ"*. Đây là quyết định
  nghiệp vụ có sẵn.
- Câu hỏi *"vai trò QTHT có được xuất báo cáo thống kê không"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — không kéo verdict (lập luận ở
  [`tieuchi/CPHTCT_06.md`](tieuchi/CPHTCT_06.md) § 7 Sửa 1).
- **Về cỡ chữ:** đặc tả `:86` viết gọn *"font Times New Roman cỡ 13"*. Đo được: quốc hiệu / tiêu ngữ / tên cơ
  quan / ngày ký / họ tên / dòng con dấu đều **cỡ 13**; tên báo cáo cỡ 14; nội dung bảng cỡ 11-12. QA **không**
  chấm Fail vì đây là cách trình bày thường thấy của văn bản hành chính; ghi lại để BA quyết nếu muốn siết.
- **Cùng nguyên nhân gốc với** `BUG-CPCTHTTTG-005` (cùng màn, khác nút) và cả nhóm `POST
  /api/v1/bao-cao/export` → `ERR-PERM-SYS-00-01` ở Phần 2/3/4.

### Khối giao việc

```
🔁 CÒN LỖI — chuyển lại dev.

■ CÒN LỖI Ở ĐÂU
Vai trò Quản trị hệ thống (tài khoản admin) — đúng vai trò trong ảnh nghiệm thu:
   [Xem báo cáo]         → OK. Hiện đủ số liệu, hai nút Xuất bật sáng.
   [Xuất PDF]            → hộp thoại "Tùy chọn in báo cáo PDF" mở bình thường.
   [Xuất file] trong hộp → KHÔNG ra tệp. Màn hiện đúng một chữ "Forbidden"
                           (máy chủ trả 403 · mã ERR-PERM-SYS-00-01)
Đúng hiện tượng ô "TKM phản hồi lần 1" đã ghi. Lần này đã CHỤP ĐƯỢC ẢNH khung thông báo đó.

■ VÌ SAO LÀ LỖI (đặc tả srs-fr-11-bao-cao.md)
1. Dòng :79 — kiểm quyền phải nằm ở ĐẦU luồng, nên bước Xem và bước Xuất phải cùng một quy
   tắc quyền. Hiện đang cho xem đủ số liệu rồi mới chặn ở bước xuất.
2. Dòng :117 — khi từ chối phải hiện câu tiếng Việt báo người dùng không có quyền xem báo
   cáo. Hiện đang ném thẳng chuỗi kỹ thuật tiếng Anh của máy chủ ra cho người dùng cuối.
KHÔNG phải chờ BA mới sửa được: câu hỏi "QTHT có được xuất báo cáo không" đã gửi BA, nhưng
trả lời hướng nào thì vẫn là lỗi — nếu không được xuất thì phải chặn từ bước Xem và báo bằng
tiếng Việt; nếu được xuất thì đang chặn nhầm.

■ ĐÃ HẾT LỖI — ĐỪNG ĐỤNG LẠI
Cán bộ Nghiệp vụ Trung ương xuất PDF tốt, tệp ra ĐÚNG khung văn bản hành chính Thông tư
17/2025: 1 trang khổ A4; đầu trang có tên cơ quan + quốc hiệu + tiêu ngữ; giữa trang đủ tên
báo cáo + kỳ + đơn vị + ngày tạo, bảng số khớp đúng số trên màn; cuối trang có ngày ký, dòng
"NGƯỜI XUẤT BÁO CÁO", "(Ký, ghi rõ họ tên và đóng dấu)" và họ tên cán bộ xuất báo cáo. Xuất
lần 2 với kỳ khác ra tên tệp khác và nội dung đổi theo bộ lọc. Hết câu "Không thể tạo file
xuất. Vui lòng thử lại." (đối tác báo 16/07).

■ MỘT CHỖ TRONG Ô "KẾT QUẢ MONG ĐỢI" KHÔNG CÒN ĐÚNG
Ô đó chờ phần ký cuối trang có DÒNG CHỨC DANH người ký. Nghiệp vụ đã chốt 04/08/2026 là KHÔNG
in dòng chức danh (hồ sơ tài khoản không lưu chức vụ). Tệp hiện tại làm ĐÚNG quyết định đó —
không phải khuyết tật, đừng ghi thành lỗi.

■ AI SỬA
Dev BE — cho bước Xem và bước Xuất dùng chung quy tắc quyền; từ chối thì trả thông báo theo :117.
Dev FE — không đẩy chuỗi máy chủ trả về ra thẳng màn hình người dùng.
BA     — chốt "QTHT có được xuất báo cáo không" để dev chọn hướng sửa.

■ ĐÃ ĐO
06/08/2026 · bản dựng V1.0.8 · admin (QTHT/TW) + cbnv_tw_03 (CB Nghiệp vụ/TW) · BC Chi phí
theo thời gian · Kỳ Năm 2026 · Toàn quốc · thêm 1 cấu hình kỳ (Khoảng tùy chọn tháng 6) · hộp
thoại in để mặc định A4 Dọc · 3 lượt bấm xuất · không tạo/sửa/xoá bản ghi nào. Bằng chứng: ô
"Ảnh/video verify" cùng dòng.
Hai lỗi khác gặp lúc đo, đã tách phiếu riêng, KHÔNG tính vào phiếu này: BCTK_QA07 (dòng 370)
— nút Xuất bị khoá sau lần xem thứ 2; BCTK_QA09 (dòng 372) — tệp PDF in mã kỹ thuật "KHOANG"
thay cho chữ tiếng Việt ở dòng Kỳ báo cáo.

────────── CÁCH VERIFY SAU KHI DEV FIX ──────────
Cần trước: tài khoản admin (QTHT, cấp TW) · màn Báo cáo thống kê (/bao-cao) · kỳ báo cáo phải
CÓ dữ liệu (báo cáo trống thì nút Xuất tự tắt, đo vô nghĩa).

B1. admin → BC Chi phí theo thời gian · Kỳ Năm 01/01–31/12/2026 · Toàn quốc → [Xem báo cáo]
    (bấm đúng 1 lần).
B2. [Xuất PDF] → hộp thoại mở → để mặc định A4 + Dọc → [Xuất file]. Chép nguyên văn chữ hiện
    ra; kiểm có tệp về máy không.
B3. Đối chiếu bằng đường thứ 2: tab Network xem lời gọi xuất trả mã gì. Có tệp thì MỞ RA ĐỌC
    bằng phần mềm đọc PDF, kiểm khổ giấy và các mục đầu/cuối trang.
B4. Lặp B1–B3 bằng cbnv_tw_03 để chắc vai trò này không bị chặn theo.

✅ PASS — đạt 1 trong 2:
   a) admin xuất được tệp .pdf mở đọc được — khổ A4, đầu trang có quốc hiệu + tiêu ngữ + tên
      cơ quan, cuối trang có ngày ký + họ tên + chỗ trống cho con dấu, số khớp màn — và không
      thông báo từ chối; HOẶC
   b) nếu BA chốt QTHT không được xuất → chặn NGAY ở bước [Xem báo cáo], kèm câu tiếng Việt.
❌ FAIL nếu: còn "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào cho người dùng cuối ·
   vẫn cho xem đủ rồi mới chặn ở bước Xuất · chỉ ẩn/làm mờ nút Xuất mà bước Xem vẫn vào được ·
   tệp PDF thiếu mục nào của khung hành chính hoặc khổ giấy khác A4 khi để mặc định · Cán bộ
   Nghiệp vụ bị chặn theo.

⚠️ BẪY
1. Nút [Xuất PDF] CHỈ MỞ HỘP THOẠI — lượt xuất thật là nút [Xuất file] bên trong. Dừng ở nút
   [Xuất PDF] sẽ không thấy lời gọi nào và dễ kết luận nhầm là hệ thống im lặng.
2. Cán bộ Nghiệp vụ xuất được KHÔNG chứng minh đã fix — vai trò đó vốn đã tốt từ 06/08. Phép đo
   quyết định là chạy bằng chính tài khoản admin.
3. Tải được tệp chưa đủ — phải MỞ TỆP RA ĐỌC mới chốt.
4. Đừng chấm Fail vì tệp không có dòng chức danh người ký (đã chốt 04/08/2026 là KHÔNG in); vì
   phông đọc ra là "Tinos" (bản tương thích số đo của Times New Roman); vì tệp không có chữ ký
   số (đặc tả chỉ đòi CHỖ TRỐNG cho con dấu); hay vì tên tệp BaoCaoChiPhiTheoThoiGian_…
5. Khung thông báo sống ~3 giây và đổi chữ NGAY TRONG khung cũ, không mọc khung mới → công cụ
   đếm "khung mới" chỉ thấy "Đang tạo file..." rồi báo nhầm là im lặng. Phải theo dõi nội dung
   khung theo thời gian; muốn chụp ảnh thì hẹn giờ bấm nút sau ~2500 mili-giây rồi mới gọi lệnh
   chụp. Ứng dụng gửi lời gọi xuất qua XHR chứ không qua fetch. Nút Xuất mờ dù báo cáo đang
   hiện số liệu = do đã bấm [Xem báo cáo] từ 2 lần trở lên (lỗi riêng BCTK_QA07).
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa.

# Phần 5 — Batch B4 (BC Chương trình theo đơn vị)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 272 |
| **Ngày** | 2026-08-06 13:10:00 |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **V1.0.8** (bó mã `assets/index-CNwX9JjX.js`) |
| **Tài khoản ra verdict** | `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW) — đúng vai trò đối tác dùng trong ảnh |
| **Tiêu chí** | [`tieuchi/CTTDVQL_04.md`](tieuchi/CTTDVQL_04.md) — viết xong **trước** khi mở màn Báo cáo thống kê |

> **Quan hệ với Phần 2 · 3 · 4:** cùng một chức năng xuất báo cáo (`POST /api/v1/bao-cao/export`), khác loại
> báo cáo. Theo yêu cầu của lô — *"nhiều case cùng một câu triệu chứng vẫn phải đo từng case trên đúng màn
> của nó"* — dòng 272 vẫn được đo riêng trên màn **BC Chương trình theo đơn vị** (FR-IX-21/UC144), không suy
> kết quả từ case anh em.
>
> ⚠️ **Đọc nhãn cho đúng:** `CT` trong mã case này là **Chương trình**, **không** phải "chi trả". Màn thật là
> *BC Chương trình theo đơn vị* (`?loai=ct-theo-don-vi`).

## Bug Summary Table (Phần 5)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CTTDVQL-004 | Major | P1 | Permission | `CTTDVQL_04` (tab `bug` dòng 272) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png`](image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png) | Open |

---

## BUG-CTTDVQL-004 — Vai trò QTHT xem được BC Chương trình theo đơn vị nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:10 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế đối tác nêu vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*, 16/07) **hết lỗi**: vai trò CB Nghiệp
> vụ Trung ương xuất Excel được, tệp `BaoCaoCtTheoDonVi_20260806_1257.xlsx` (6 693 B) mở đọc được, đúng hình
> hài cross-tab, số khớp màn. Vế vòng 2 (*"Forbidden"*, TKM 31/07) **tái hiện nguyên vẹn** ở đúng vai trò đối
> tác đã dùng, và lần này **đã chụp được** khung thông báo. N = 3 lượt xuất thành công (3 bộ lọc khác nhau) +
> 1 lượt bị chặn ở vai QTHT · **không seed, không tạo/sửa/xoá bản ghi nào** — toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chương trình theo đơn vị**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng chương trình 7 · Tổng ngân
sách 350.000.000 + biểu đồ + bảng chéo theo đơn vị) và **hiện hai nút [Xuất Excel] / [Xuất PDF] ở trạng thái
bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người
dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ, không cho người
dùng biết chuyện gì đã xảy ra và phải làm gì tiếp. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ
Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, vé đăng nhập ghi `vaiTro = ["QTHT"]`,
   `capDonVi = "TW"`) — đúng vai trò trên bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chương trình theo đơn vị**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc** — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng chương trình 7 · Tổng ngân sách 350.000.000 +
   biểu đồ cột + bảng chéo *Cục Bổ trợ tư pháp - Bộ Tư pháp · TW · 7 · 350.000.000 ₫*), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_04`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi kỹ
  thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 13:05–13:06:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/ct-theo-don-vi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **7 chương trình / 350.000.000 ₫** (*Thời điểm tạo 06/08/2026 13:05*) — **đúng bằng
  số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được**.
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (không có hiện tượng 2 thông
  báo chồng); chữ người dùng đọc được đổi tại chỗ **"Đang tạo file..." → "Forbidden"**; khung sống
  **3 370 ms**, vị trí `x=0 · y=8 · w=1432 · h=56`, `opacity 1`, vùng chứa `position: fixed`, `z-index 2010`
  (nằm trong vùng nhìn thấy, không phải node ẩn); **0 tệp** được giao, **0 blob** được tạo.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_CT_THEO_DON_VI","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T06:06:15.027Z","requestId":"05ed4987-9bce-4a93-930d-1de2eb3326ad"}}
  ```

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_04`) — cùng màn, 3 bộ lọc khác nhau:**

| Lượt | Bộ lọc | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc (đúng bộ lọc đối tác) | 12:57 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoCtTheoDonVi_20260806_1257.xlsx` — 6 693 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Năm 2026 · Đơn vị = Cục Bổ trợ tư pháp | 13:00 | **200** | `BaoCaoCtTheoDonVi_20260806_1300.xlsx` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Khoảng 01/02–31/12/2026 · Toàn quốc | 13:03 | **200** | `BaoCaoCtTheoDonVi_20260806_1303.xlsx` | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Ba lượt ra ba tên tệp khác nhau** (`…_1257` / `…_1300` / `…_1303`) ⇒ xuất nhiều lần trong cùng ngày không
  đè tệp nhau, đúng chủ đích quy ước đặt tên ở `:85` + `srs-v3.5.md:6716` (Phụ lục E §H8).
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): đủ 4 mục đầu tệp `:1092` đòi — *BC Chương trình theo đơn
  vị* · *Kỳ báo cáo* · *Đơn vị* · *Ngày tạo*; đúng hình hài **bảng chéo** `:927`/`:948` — hàng là **đơn vị**,
  cột có **cả** *Số chương trình* lẫn *Tổng ngân sách*, kèm *Cấp đơn vị* (`:943`); số trong tệp khớp từng con
  số với màn (7 · 350 000 000) và cộng dọc bằng đúng hai thẻ tổng.
- Đổi bộ lọc thì tệp đổi theo (`:1280`): lượt 3 ra **2 / 150 000 000** đúng bằng màn.
- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* ở bất kỳ lượt nào.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên vẹn** đúng vai trò,
đúng màn, đúng bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png`](image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, khung thông báo đỏ ✗ **"Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 7 / 350.000.000.
  *Ghi chú thẳng thắn:* khung chỉ sống 3,37 giây nên hai lượt chụp đầu bị trượt (giữ lại ở hai ảnh dưới); ảnh
  này chụp được nhờ bấm lặp nút thật 8 lượt cách nhau 1,5 giây để khung luôn hiện — 8 lượt đó đều là lời gọi
  xuất trả 403, **không** đổi dữ liệu.
- [`image/CTTDVQL_04-B1-qtht-xem-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](image/CTTDVQL_04-B1-qtht-xem-bao-cao-day-du-truoc-khi-bam-xuat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ số liệu và **hai nút Xuất
  đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/CTTDVQL_04-B2-qtht-luot-chup-thu-1-ngay-sau-bam-xuat-excel-V108.png`](image/CTTDVQL_04-B2-qtht-luot-chup-thu-1-ngay-sau-bam-xuat-excel-V108.png)
  · [`image/CTTDVQL_04-B3-qtht-luot-chup-thu-2-hen-gio-bam-truoc-2500ms-V108.png`](image/CTTDVQL_04-B3-qtht-luot-chup-thu-2-hen-gio-bam-truoc-2500ms-V108.png)
  — hai lượt chụp trượt, giữ lại để người đọc thấy đủ quá trình đo.
- [`image/CTTDVQL_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png`](image/CTTDVQL_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png)
  · [`image/CTTDVQL_04-A2-dang1-ngay-sau-bam-xuat-excel-V108.png`](image/CTTDVQL_04-A2-dang1-ngay-sau-bam-xuat-excel-V108.png)
  — phiên CB Nghiệp vụ TW: trước khi bấm và ngay sau khi bấm [Xuất Excel], **không** có khung thông báo lỗi ở
  đúng vị trí mà hai ảnh của đối tác từng hiện lỗi.
- [`image/CTTDVQL_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png`](image/CTTDVQL_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png)
  · [`image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png`](image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png)
  — hai biến thể bộ lọc, dùng chứng minh tệp xuất bám đúng bộ lọc hiện tại.
- [`image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt`](image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt) —
  nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · tuổi thọ khung), nguyên văn phản hồi máy chủ, vai
  trò đọc từ vé đăng nhập trước/sau mỗi phép đo, và toàn bộ nội dung ô của 3 tệp .xlsx.
- Tệp thật hệ thống giao ra: [`testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx`](testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx)
  · [`testfiles/BaoCaoCtTheoDonVi_20260806_1300.xlsx`](testfiles/BaoCaoCtTheoDonVi_20260806_1300.xlsx)
  · [`testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx`](testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx).

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_04` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:929`) | 200, ra đủ số liệu | **200**, nhận được tệp .xlsx mở đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của case:
  giả sử BA trả lời theo cả hai hướng — nếu QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt
  `:117` thay vì `Forbidden`; nếu QTHT *được* xuất thì đang chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả
  lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoChuongTrinh_{YYYYMMDD_HHmm}.xlsx`, hệ thống ra
  `BaoCaoCtTheoDonVi_20260806_1257.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85` + `srs-v3.5.md:6716` Phụ
  lục E §H8: `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}`, PascalCase, không dấu), **không** ấn định chuỗi
  `BaoCaoChuongTrinh`. Tên hệ thống dùng khớp khuôn ⇒ không phải khuyết tật.
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006`
  (Phần 4) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã `ERR-PERM-SYS-00-01`, khác loại báo cáo.
  Dev sửa một chỗ có thể đóng cả bốn; QA vòng sau vẫn phải verify riêng từng case trên đúng màn của nó.
- **Ngoài phạm vi, không kéo verdict case này:** ở lượt xuất với kỳ *Khoảng tùy chọn*, dòng thứ hai của tệp
  ghi nhãn kỳ bằng **mã nội bộ** — *"Kỳ báo cáo: **KHOANG** (từ 01/02/2026 đến 31/12/2026)"* — trong khi màn
  cùng lúc ghi *"Kỳ: Khoảng"* và tệp kỳ Năm ghi *"Năm"*. Đặc tả **im lặng** về nhãn kỳ trong tệp (`:1092` chỉ
  đòi *"chèn… thông tin kỳ"*), nên **chưa mở phiếu lỗi** — đã chuyển thành
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 4*. Bộ lọc của đối tác là kỳ **Năm**, chỗ đó tệp ghi đúng.

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
CẦN CÓ TRƯỚC: tài khoản admin (Quản trị hệ thống, cấp TW); màn Báo cáo thống kê (/bao-cao);
  ≥1 chương trình HTPLDN đã phê duyệt nằm trong năm 2026. Báo cáo trống thì nút Xuất không bật
  và phép thử không có giá trị.
Bước 1. Chọn loại báo cáo "BC Chương trình theo đơn vị", Kỳ "Năm" (01/01/2026 – 31/12/2026),
  Đơn vị "Toàn quốc". Bấm [Xem báo cáo]. Ghi lại 2 số trên màn — Tổng chương trình / Tổng ngân
  sách — và các dòng trong bảng theo đơn vị.
Bước 2. Bấm [Xuất Excel]. Chép lại NGUYÊN VĂN chữ hiện ra và kiểm có tệp về máy không.
Bước 3. Kiểm bằng đường thứ hai: mở tab Network xem lời gọi xuất báo cáo trả mã gì, thân phản
  hồi ghi gì. Có tệp thì MỞ TỆP RA ĐỌC, đối chiếu 2 số ở bước 1 và từng dòng đơn vị với nội
  dung trong tệp.
Bước 4. Làm lại bước 1–3 bằng tài khoản cbnv_tw_04 (Cán bộ Nghiệp vụ) để chắc là không hỏng
  phần đang chạy tốt.
✅ ĐẠT khi một trong hai:
  · Vai trò Quản trị hệ thống bấm [Xuất Excel] thì nhận được tệp .xlsx mở đọc được, số trong
    tệp khớp đúng số trên màn, và không hiện thông báo từ chối nào.
  · Hoặc — nếu nghiệp vụ chốt vai trò này KHÔNG được xuất — hệ thống chặn ngay từ bước
    [Xem báo cáo], và chữ hiện ra là câu tiếng Việt cho người dùng biết họ không có quyền xem
    báo cáo này.
  Kèm điều kiện không hỏng phần cũ: vai trò Cán bộ Nghiệp vụ vẫn xuất được, tệp vẫn giữ đủ
  chiều đơn vị cùng hai cột Số chương trình / Tổng ngân sách.
❌ CHƯA ĐẠT nếu: còn thấy "Forbidden" hay bất kỳ chuỗi tiếng Anh / mã kỹ thuật nào; hoặc vẫn
  cho Xem đủ số liệu rồi mới chặn ở bước Xuất (đúng một nửa cũng tính là chưa đạt); hoặc sửa
  bằng cách ẩn / làm mờ nút Xuất mà bước Xem vẫn cho vào — người dùng vẫn không biết vì sao
  mình không xuất được.
⚠️ 4 bẫy hay mắc khi đo:
  1. Chỉ thử bằng vai trò Cán bộ Nghiệp vụ rồi kết luận "đã fix". Vai trò đó vốn đã chạy tốt từ
     lượt đo 06/08/2026 — phép đo quyết định phải chạy bằng chính vai trò Quản trị hệ thống.
  2. Dừng ở "tải được tệp". Phải mở tệp ra đọc mới chốt được.
  3. Khung thông báo chỉ sống khoảng 3–4 giây, và giao diện đổi chữ NGAY TRONG khung cũ chứ
     không mọc khung mới. Chỉ để ý "khung nào mới mọc" thì sẽ chỉ thấy "Đang tạo file..." rồi
     kết luận nhầm là hệ thống im lặng.
  4. Kỳ "Tháng" / "Quý" có ô Thời gian chỉ đọc, tự tính theo kỳ hiện tại. Muốn đổi khoảng thời
     gian phải chọn "Khoảng tùy chọn".
⚠️ Đừng chấm hỏng vì tên sheet, thứ tự cột, màu sắc, dòng tổng cuối bảng, tệp không nhúng biểu
  đồ, hay vì tên tệp không đúng chữ "BaoCaoChuongTrinh" — đặc tả không quy định, hoặc chỉ quy
  định khuôn tên (dòng 85, dòng 1092). Xem mục [4].
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy nguyên
chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở [`cau-hoi-BA.md`](cau-hoi-BA.md)
§ Mục 2 trước khi dev chọn hướng sửa; § Mục 4 (nhãn kỳ trong tệp) là việc riêng, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 5)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — HTPLDN **V1.0.8**, bó mã giao diện `assets/index-CNwX9JjX.js` |
| **Màn đo** | Báo cáo thống kê → **BC Chương trình theo đơn vị** (`/bao-cao?loai=ct-theo-don-vi`), FR-IX-21 / UC144 |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng `isolatedContext="cttdvql04"` — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước và sau** mỗi phép đo quyết định, trùng khớp cả 2 nhánh |
| **Khung giờ đo** | 2026-08-06 12:54 → 13:08 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 14 chương trình, đủ cho cả 3 dạng biến thể |

*Phần 5 generated: 2026-08-06 13:10:00 | QA Automation via Claude Code*

---

# Phần 6 — Batch B5 (BC Lớp đào tạo đang diễn ra)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 200 |
| **Ngày** | 2026-08-06 13:30:00 |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **V1.0.8** (bó mã `assets/index-CNwX9JjX.js`, md5 `e0e4f737b1fb7ab9409f459a4d0fa051`) |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW) — đúng vai trò đối tác dùng ở **cả hai** ảnh |
| **Tiêu chí** | [`tieuchi/CLDTBDDDR_06.md`](tieuchi/CLDTBDDDR_06.md) — viết xong **trước** khi mở màn Báo cáo thống kê |

> **Quan hệ với Phần 2 · 3 · 4 · 5:** cùng một chức năng xuất báo cáo (`POST /api/v1/bao-cao/export`), khác
> loại báo cáo. Theo yêu cầu của lô — *"nhiều case cùng một câu triệu chứng vẫn phải đo từng case trên đúng
> màn của nó"* — dòng 200 vẫn được đo riêng trên màn **BC Lớp đào tạo đang diễn ra** (FR-IX-06 / UC129,
> `srs-fr-11-bao-cao.md:346`), không suy kết quả từ case anh em.

## Bug Summary Table (Phần 6)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CLDTBDDDR-006 | Major | P1 | Permission | `CLDTBDDDR_06` (tab `bug` dòng 200) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CLDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CLDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Open |

---

## BUG-CLDTBDDDR-006 — Vai trò QTHT xem được BC Lớp đào tạo đang diễn ra nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 13:24 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế đối tác nêu vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được cả Excel lẫn PDF, tệp mở đọc được, đủ 4 mục đầu tệp, số khớp màn. Vế tên tệp cũng
> **đạt** (`BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx` — đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}`,
> hai lượt cùng ngày ra hai tên khác nhau). Vế vòng 2 (*"Forbidden"*, TKM 31/07) **tái hiện nguyên vẹn** ở
> đúng vai trò đối tác đã dùng. N = 4 lượt xuất thành công (3 bộ lọc Excel + 1 PDF) + 4 lượt bị chặn ở vai
> QTHT · **không seed, không tạo/sửa/xoá bản ghi nào** — toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Lớp đào tạo đang diễn ra**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng số 2 · Trực tuyến 1 · Trực
tiếp 1 + bảng theo đơn vị) và **hiện hai nút [Xuất Excel] / [Xuất PDF] ở trạng thái bấm được**, nhưng bấm
tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là
**"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ, không cho người dùng biết
chuyện gì đã xảy ra và phải làm gì tiếp. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương
xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`, vé đăng nhập ghi `vaiTro = ["QTHT"]`,
   `capDonVi = "TW"`, `donViId = 00000000-0000-4000-8000-000000000001` = *Cục Bổ trợ tư pháp - Bộ Tư pháp*)
   — đúng vai trò trên bằng chứng của đối tác ở **cả hai vòng**.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Lớp đào tạo đang diễn ra**; *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc**; không đặt bộ lọc đặc thù — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng số 2 · Trực tuyến 1 · Trực tiếp 1 + bảng theo
   đơn vị), không có cảnh báo nào.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi
  kỹ thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 13:20–13:24:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/lop-dao-tao-dang-dien-ra?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **Tổng số 2 · Trực tuyến 1 · Trực tiếp 1** (*Thời điểm tạo 06/08/2026 13:20*) —
  **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (không có hiện tượng 2 thông
  báo chồng); chữ người dùng đọc được đổi tại chỗ **"Đang tạo file..." → "Forbidden"**; khung xuất hiện
  **+102 ms** sau khi bấm và biến mất ở **+3 302 ms** (sống ~3,2 giây), vị trí `x=0 · y=8 · w=1432 · h=40`,
  `opacity 1`, `z-index 2010` (nằm trong vùng nhìn thấy, không phải node ẩn); **0 tệp** được giao, **0** thẻ
  tải được kích hoạt. Đã tái hiện **4 lượt liên tiếp**, lượt nào cũng ra đúng chữ đó.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_LOP_DAO_TAO_DANG_DIEN_RA","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T06:21:19.649Z","requestId":"ad1678d6-05f8-4619-9c88-106a91148a2f"}}
  ```
  Chữ trên màn **trùng khít** `error.message` của máy chủ ⇒ giao diện đẩy nguyên chuỗi kỹ thuật ra cho
  người dùng cuối.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, 3 bộ lọc + 1 lượt PDF:**

| Lượt | Bộ lọc / định dạng | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc · không lọc đặc thù (đúng bộ lọc đối tác) | 13:08 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx` — 6 793 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Lặp lại y hệt lượt 1 (phép thử chống đè tệp) | 13:10 | **200** | `BaoCaoLopDaoTaoDangDienRa_20260806_1310.xlsx` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Lọc *Hình thức = Trực tuyến* | 13:11 | **200** | `BaoCaoLopDaoTaoDangDienRa_20260806_1311.xlsx` — 6 735 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 4 | Lọc *Lĩnh vực = Dân sự* | 13:14 | **200** | `BaoCaoLopDaoTaoDangDienRa_20260806_1314.xlsx` — 6 793 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 5 | **Xuất PDF** (A4 · Dọc) | 13:17 | **200**, kiểu `application/pdf` | `BaoCaoLopDaoTaoDangDienRa_20260806_1317.pdf` | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* (`ERR-RPT-04`, `:116`) ở bất kỳ lượt
  nào, cũng **không** có *"Forbidden"* ⇒ vế vòng 1 của đối tác hết lỗi.
- **Tên tệp** — đo từ **hai đường độc lập và trùng khít**: header `content-disposition` của máy chủ, và
  thuộc tính `download` mà chính ứng dụng giao cho trình duyệt (đúng thứ người dùng thật nhìn thấy).
  Khớp khuôn đặc tả `:85` + `srs-v3.5.md:6716` (Phụ lục E §H8) — `{TenTep}_{YYYYMMDD_HHmm}.{đuôi}`,
  PascalCase, không dấu, không ký tự lạ, **có đủ giờ-phút**. Hai lượt xuất **cùng ngày** (13:08 / 13:10) ra
  **hai tên khác nhau** ⇒ không đè tệp nhau, đúng chủ đích BA chốt 2026-08-04 khi bắt buộc phần giờ-phút.
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): sheet *"Lớp đào tạo đang diễn ra"*, đủ 4 mục đầu tệp
  `:1092` đòi — *BC Lớp đào tạo đang diễn ra* · *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* ·
  *Đơn vị: Toàn quốc* · *Ngày tạo: 06/08/2026*. Số trong tệp khớp **từng con số** với màn của chính lượt đó
  (2 · 1 · 1), và chiều *theo đơn vị* cộng dọc bằng đúng thẻ tổng (1 + 1 = 2).
- Đổi bộ lọc thì tệp đổi theo (`:1280`): tệp lượt 3 ra **Tổng 1 · Trực tuyến 1 · Trực tiếp 0**, chỉ còn một
  dòng *Bộ Kế hoạch và Đầu tư* — khác hẳn tệp lượt 1.
- Tệp PDF: 1 trang khổ **A4** (595,28 × 841,89 pt) đúng tùy chọn đã chọn, có quốc hiệu + tên cơ quan ở đầu
  trang, khối ký cuối trang, số liệu 2/1/1 khớp màn.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế tên tệp đạt. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên
vẹn** đúng vai trò, đúng màn, đúng bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CLDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CLDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, khung thông báo **"Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 2 / 1 / 1.
  *Ghi chú thẳng thắn:* khung chỉ sống ~3,2 giây nên **3 lượt chụp đầu bị trượt**, ảnh này là lượt thứ 4 —
  cả 4 lượt đều là lời gọi xuất trả 403, **không** đổi dữ liệu.
- [`image/CLDTBDDDR_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-excel-bat-V108.png`](image/CLDTBDDDR_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-excel-bat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ số liệu và **hai nút
  Xuất đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/CLDTBDDDR_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png`](image/CLDTBDDDR_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png)
  — phiên CB Nghiệp vụ TW, dạng 1 (đúng bộ lọc đối tác), màn hình **trước** khi bấm Xuất: Tổng số 2 · Trực
  tuyến 1 · Trực tiếp 1, dùng làm mốc đối chiếu số liệu với nội dung tệp.
- [`image/CLDTBDDDR_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png`](image/CLDTBDDDR_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png)
  — **ngay sau** khi bấm [Xuất Excel] ở dạng 1: **không** có khung thông báo lỗi ở đúng vị trí mà hai ảnh
  của đối tác từng hiện lỗi.
- [`image/CLDTBDDDR_06-03-dang2-loc-hinhthuc-TrucTuyen-ngay-sau-bam-xuat-excel-V108.png`](image/CLDTBDDDR_06-03-dang2-loc-hinhthuc-TrucTuyen-ngay-sau-bam-xuat-excel-V108.png)
  — dạng 2 (lọc *Hình thức = Trực tuyến*), ngay sau khi bấm Xuất: màn còn Tổng số 1, cũng không có lỗi —
  dùng chứng minh tệp xuất bám đúng bộ lọc hiện tại.
- [`image/CLDTBDDDR_06-04-dang3-loc-linhvuc-DanSu-man-hinh-van-ra-tong-2-V108.png`](image/CLDTBDDDR_06-04-dang3-loc-linhvuc-DanSu-man-hinh-van-ra-tong-2-V108.png)
  — dạng 3 (lọc *Lĩnh vực = Dân sự*): xuất vẫn chạy bình thường, **và** đây là ảnh cho thấy màn vẫn ra Tổng
  số 2 y như không lọc — cơ sở của ghi nhận ngoài phạm vi D1 bên dưới.
- [`image/CLDTBDDDR_06-05-hop-thoai-tuy-chon-in-PDF-V108.png`](image/CLDTBDDDR_06-05-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *"Tùy chọn in báo cáo PDF"* (Khổ giấy · Hướng giấy · [Hủy] [Xuất file]) mà [Xuất PDF] mở ra;
  giữ lại vì đây là bước dễ hiểu nhầm thành *"bấm Xuất PDF không có phản ứng gì"*.
- [`image/CLDTBDDDR_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/CLDTBDDDR_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · tuổi thọ khung), nguyên văn phản hồi máy chủ,
  vai trò đọc từ vé đăng nhập, tên tệp đo từ cả hai đường, và toàn bộ nội dung ô của 3 tệp .xlsx + nội dung
  chữ của tệp .pdf.
- Tệp thật hệ thống giao ra:
  [`testfiles/CLDTBDDDR_06-dang1-khong-loc-BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx`](testfiles/CLDTBDDDR_06-dang1-khong-loc-BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx)
  · [`testfiles/CLDTBDDDR_06-dang2-loc-TrucTuyen-BaoCaoLopDaoTaoDangDienRa_20260806_1311.xlsx`](testfiles/CLDTBDDDR_06-dang2-loc-TrucTuyen-BaoCaoLopDaoTaoDangDienRa_20260806_1311.xlsx)
  · [`testfiles/CLDTBDDDR_06-dang3-loc-DanSu-BaoCaoLopDaoTaoDangDienRa_20260806_1314.xlsx`](testfiles/CLDTBDDDR_06-dang3-loc-DanSu-BaoCaoLopDaoTaoDangDienRa_20260806_1314.xlsx)
  · [`testfiles/CLDTBDDDR_06-pdf-BaoCaoLopDaoTaoDangDienRa_20260806_1317.pdf`](testfiles/CLDTBDDDR_06-pdf-BaoCaoLopDaoTaoDangDienRa_20260806_1317.pdf)
  (tên tệp gốc hệ thống đặt được giữ nguyên phía sau tiền tố mã case).

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:357`) | 200, ra đủ số liệu | **200**, nhận được tệp .xlsx/.pdf mở đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- **Hai đường đo độc lập cùng kết luận, không mâu thuẫn:** đường giao diện (thao tác chuột thật, đọc chữ
  hiện trên màn) và đường máy chủ (mã HTTP + thân phản hồi) khớp nhau ở cả hai vai trò ⇒ không có điểm nào
  cần hỏi thêm trước khi kết luận.
- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của
  case: nếu BA chốt QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt `:117` thay vì
  `Forbidden`, và phải chặn ngay từ bước Xem cho nhất quán (`:79`); nếu BA chốt QTHT *được* xuất thì đang
  chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoDaoTao_{YYYYMMDD_HHmm}`, hệ thống ra
  `BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85` +
  `srs-v3.5.md:6716` Phụ lục E §H8), **không** ấn định chuỗi `BaoCaoDaoTao`. Tên hệ thống dùng khớp khuôn,
  có đủ giờ-phút, hai lượt cùng ngày không đè nhau ⇒ **không** phải khuyết tật.
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006`
  (Phần 4), `BUG-CTTDVQL-004` (Phần 5) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã
  `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng cả năm; QA vòng sau vẫn phải verify
  riêng từng case trên đúng màn của nó. **Không mở dòng bug mới trên bảng theo dõi** cho case này.

#### Ghi nhận ngoài vế đối tác nêu — **không** kéo verdict case, chưa mở dòng trên bảng

Hai điểm dưới đây phát hiện trong lúc đo nhưng đối tác **không** nêu ở case này. Ghi lại đầy đủ để phiên
chính quyết có mở dòng riêng hay không; QA không tự mở.

- **D1 — Bộ lọc *Lĩnh vực* trên màn này không có tác dụng.** Giao diện gửi
  `GET /api/v1/bao-cao/lop-dao-tao-dang-dien-ra?...&linhVuc=<id>` → Tổng **2**; gọi đúng tên tham số
  `...&linhVucId=<id>` → Tổng **1** (Dân sự = 1, Thương mại = 1, 8 lĩnh vực còn lại = 0). Lệnh xuất mang
  **cùng khoá sai**: `"filterDacThu":{"linhVuc":...}`. Hệ quả: chọn lĩnh vực nào thì màn **và** tệp xuất
  vẫn ra y như không lọc. Bộ lọc *Hình thức* thì chạy đúng. Đặc tả liên quan: `srs-fr-11-bao-cao.md:366`
  (`linh_vuc_id`) · `:370` · `:1071` · `:1280`.
- **D2 — Báo cáo thiếu 2 chiều dữ liệu mà đặc tả ghi điều kiện hiển thị *"Luôn"*.**
  `srs-fr-11-bao-cao.md:380` (`theo_linh_vuc[]`) và `:381` (`ds_khoa_hoc[]`). Phản hồi máy chủ chỉ có
  `tenBaoCao · ngayTaoBc · tongSo · trucTuyen · trucTiep · theoDonVi · chartType`; cả màn hình lẫn tệp xuất
  đều không có hai mục này.

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần >=1 lớp đào tạo đang diễn ra trong năm 2026 để báo cáo có dữ liệu; nếu báo
  cáo trống thì nút Xuất sẽ không bật và phép thử không có giá trị.

Các bước:
  1. Đăng nhập admin (QTHT). Vào Báo cáo thống kê. TẢI LẠI TRANG và ghi lại nhãn bản dựng
     trước khi đo.
  2. Loại báo cáo = BC Lớp đào tạo đang diễn ra; Kỳ = Năm 01/01/2026 - 31/12/2026;
     Đơn vị = Toàn quốc; không đặt bộ lọc đặc thù. Bấm [Xem báo cáo], chờ ra số liệu.
  3. Cài bộ theo dõi thông báo TRƯỚC khi bấm (không lọc trùng, đọc innerText, lấy mẫu chữ
     theo thời gian - xem tools/toast-capture.js), rồi bấm [Xuất Excel].
  4. Ghi lại: chữ hiện cho người dùng · mã trả về của POST /api/v1/bao-cao/export · số tệp
     nhận được.
  5. Lặp lại bước 2-4 bằng tài khoản cbnv_tw_05 (CB Nghiệp vụ TW) để đối chiếu, và MỞ TỆP
     xuất ra đọc: phải còn đủ 4 mục đầu tệp (tên BC, kỳ, đơn vị, ngày tạo), còn đủ 3 con số
     Tổng/Trực tuyến/Trực tiếp và bảng theo đơn vị, số khớp màn.

PASS khi:
  - Vai trò QTHT: KHÔNG còn thấy chuỗi "Forbidden" trên màn. Nếu hệ thống vẫn từ chối thì
    câu hiện ra phải là câu tiếng Việt cho biết người dùng không có quyền (yêu cầu :117);
    nếu BA chốt QTHT được xuất thì phải nhận được tệp .xlsx mở đọc được.
  - Bước Xem và bước Xuất nhất quán: không còn cảnh cho xem đủ số liệu rồi chặn ở bước xuất.
    Nếu vai trò bị cấm thì phải chặn ngay từ bước Xem (yêu cầu :79).
  - Vai trò cbnv_tw_05 vẫn xuất được cả Excel lẫn PDF, tên tệp vẫn đúng khuôn có giờ-phút,
    nội dung tệp vẫn đúng như mô tả ở bước 5 (không hồi quy).

FAIL nếu:
  - Còn bất kỳ chỗ nào hiện chuỗi kỹ thuật tiếng Anh (Forbidden / Unauthorized / Internal
    Server Error) cho người dùng cuối.
  - Sửa bằng cách ẩn/làm mờ nút Xuất mà bước Xem vẫn cho vào: người dùng vẫn không biết vì
    sao mình không xuất được -> chưa đạt :117.
  - Vai trò CB Nghiệp vụ bị chặn theo, hoặc tệp xuất mất mục đầu tệp / mất chiều theo đơn vị
    / mất phần giờ-phút trong tên tệp (hồi quy).

Bẫy hay gặp:
  - Khung thông báo chỉ sống ~3,2 giây và thư viện giao diện CẬP NHẬT CHỮ NGAY TRONG khung cũ
    chứ không mọc khung mới. Nếu chỉ ghi "khung nào mới mọc" sẽ chỉ thấy "Đang tạo file..."
    và kết luận nhầm là hệ thống im lặng. Phải lấy mẫu chữ theo thời gian.
  - Đo bằng vai trò CB Nghiệp vụ rồi kết luận "hết lỗi" là sai - vòng verify trước đã vấp
    đúng chỗ này. Phải đo bằng đúng vai trò QTHT như trên bằng chứng của đối tác.
  - [Xuất PDF] KHÔNG tải tệp ngay: nó mở hộp thoại "Tùy chọn in báo cáo PDF", phải bấm tiếp
    [Xuất file]. Bỏ qua bước này rất dễ báo oan "bấm không có phản ứng"; hộp thoại còn mở
    cũng nuốt luôn cú bấm [Xuất Excel] ngay sau đó.
  - Tab trình duyệt mở lâu vẫn chạy mã cũ: phải tải lại trang và ghi lại nhãn bản dựng trước
    khi kết luận.
  - Số trên màn có thể là số máy chủ đã nhớ sẵn: xem trường "Thời điểm tạo" có nhảy theo lượt
    bấm không, nếu đứng yên thì đổi ngày kết thúc 1 ngày để lấy số mới.
  - Đổi bộ lọc bằng thao tác giả lập (bắn sự kiện chuột) có thể làm nút Xuất kẹt ở trạng thái
    mờ - đó là lỗi của cách đo, không phải của phần mềm. Tải lại trang và bấm thật.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy
nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở
[`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2 trước khi dev chọn hướng sửa. Hai ghi nhận D1 · D2 ở trên chuyển
**phiên chính** quyết, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 6)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — HTPLDN **V1.0.8**, bó mã giao diện `assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`, 1 123 581 byte) — **tự đo**, không chép từ case khác |
| **Màn đo** | Báo cáo thống kê → **BC Lớp đào tạo đang diễn ra** (`/bao-cao?loai=lop-dao-tao-dang-dien-ra`), FR-IX-06 / UC129 (`srs-fr-11-bao-cao.md:346`) |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng `isolatedContext="cldtbdddr06"` — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước và sau** mỗi phép đo quyết định, trùng khớp cả 2 nhánh |
| **Khung giờ đo** | 2026-08-06 13:07 → 13:24 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 2 lớp đào tạo đang diễn ra, đủ cho cả 3 dạng biến thể |

*Phần 6 generated: 2026-08-06 13:30:00 | QA Automation via Claude Code*

# Phần 7 — Batch B5 (BC Lớp đào tạo ĐÃ diễn ra)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 205 |
| **Ngày** | 2026-08-06 14:10:00 |
| **Môi trường** | https://18.143.165.120.nip.io — bản dựng **V1.0.8** (bó mã `assets/index-CNwX9JjX.js`, md5 `e0e4f737b1fb7ab9409f459a4d0fa051`) — **tự đo**, không chép từ case khác |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback Rule 7 |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW, đơn vị BTP) — đúng vai trò đối tác dùng ở ảnh vòng 2 |
| **Tiêu chí** | [`tieuchi/LDTBDDDR_06.md`](tieuchi/LDTBDDDR_06.md) — viết xong **trước** khi mở màn Báo cáo thống kê |

> **Quan hệ với Phần 2 · 3 · 4 · 5 · 6:** cùng một chức năng xuất báo cáo (`POST /api/v1/bao-cao/export`),
> khác loại báo cáo. Dòng 205 vẫn được đo **riêng** trên đúng màn của nó — **BC Lớp đào tạo ĐÃ diễn ra**
> (FR-IX-07 / UC130, `srs-fr-11-bao-cao.md:389`), **không** phải màn *đang* diễn ra của Phần 6. Hai màn khác
> nhau ở: tên loại báo cáo, đường dẫn dữ liệu (`lop-dao-tao-da-dien-ra`), bộ chỉ số đầu ra
> (`tong_da_dien_ra` + `tong_hoc_vien`) và **bộ lọc đặc thù chỉ có Hình thức**, không có Lĩnh vực (`:1070`).
> Không suy kết quả từ case anh em.

## Bug Summary Table (Phần 7)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-LDTBDDDR-006 | Major | P1 | Permission | `LDTBDDDR_06` (tab `bug` dòng 205) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/LDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/LDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Open |

---

## BUG-LDTBDDDR-006 — Vai trò QTHT xem được BC Lớp đào tạo đã diễn ra nhưng bị chặn khi Xuất Excel, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 14:01 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bản dựng **V1.0.8**.
> Vế đối tác nêu ở vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được cả Excel lẫn PDF ở **cả 3 dạng bộ lọc**, tệp mở đọc được, đủ 4 mục đầu tệp, số khớp
> màn từng con số. Vế tên tệp cũng **đạt** (`BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx` — đúng khuôn
> `{TenBaoCao}_{YYYYMMDD_HHmm}`, hai lượt cùng ngày ra hai tên khác nhau). Vế vòng 2 (*"Forbidden"*, TKM
> retest 31/07) **tái hiện nguyên vẹn** ở đúng vai trò đối tác đã dùng. N = 5 lượt xuất thành công
> (4 Excel + 1 PDF) + 3 lượt bị chặn ở vai QTHT · **không seed, không tạo/sửa/xoá bản ghi nào** — toàn bộ
> thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Lớp đào tạo đã diễn ra**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng khóa học 9 · Tổng học viên
17 + bảng theo đơn vị) và **hiện hai nút [Xuất Excel] / [Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp
[Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** —
chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ, không cho người dùng biết chuyện gì đã xảy
ra và phải làm gì tiếp. Cùng thao tác, cùng bộ lọc, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`; vé đăng nhập ghi `vaiTro = ["QTHT"]`,
   `capDonVi = "TW"`, `donViId = 00000000-0000-4000-8000-000000000001` = *Cục Bổ trợ tư pháp - Bộ Tư pháp*)
   — đúng vai trò và đơn vị đọc được ở góc phải trên bằng chứng vòng 2 của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Lớp đào tạo đã diễn ra** (đường dẫn phải chứa `loai=lop-dao-tao-da-dien-ra`
   — **không** nhầm sang *đang* diễn ra); *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc**; để trống bộ lọc *Hình thức* — đúng bộ lọc trên ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (Tổng khóa học 9 · Tổng học viên 17 + bảng theo đơn
   vị + biểu đồ), không có cảnh báo nào; hai nút Xuất bật lên.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi
  kỹ thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 13:56–13:59:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/lop-dao-tao-da-dien-ra?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **Tổng khóa học 9 · Tổng học viên 17** (*Thời điểm tạo 06/08/2026 13:56*) —
  **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** khung thông báo (không có hiện tượng 2 thông
  báo chồng); chữ người dùng đọc được đổi tại chỗ **"Đang tạo file..." → "Forbidden"**; khung sống
  **3 201 ms**, vị trí `x=0 · y=8 · w=1431 · h=40`, `opacity 1` (nằm trong vùng nhìn thấy, không phải node
  ẩn); **0 tệp** được giao — đếm thư mục tải xuống trước/sau không thêm tệp nào. Đã tái hiện **3 lượt**,
  lượt nào cũng ra đúng chữ đó.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_LOP_DAO_TAO_DA_DIEN_RA","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T06:57:29.480Z","requestId":"eae4abd3-80d0-4855-9de3-57e3276097cb"}}
  ```
  Chữ trên màn **trùng khít** `error.message` của máy chủ ⇒ giao diện đẩy nguyên chuỗi kỹ thuật ra cho
  người dùng cuối.
- Đo lại bằng **đường thứ hai** (gọi thẳng máy chủ, ngoài trình duyệt, cùng phiên QTHT): GET báo cáo
  **200** ra đúng 9 / 17 · POST xuất **403** với thân phản hồi y hệt ⇒ **hai đường khớp nhau**, không phải
  lỗi thao tác trên giao diện.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, 3 dạng bộ lọc + 1 lượt lặp + 1 lượt PDF:**

| Lượt | Bộ lọc / định dạng | Màn trước khi bấm | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc · Hình thức trống (**đúng bộ lọc đối tác**) | 9 / 17 | 13:48 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx` — 6 822 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Lọc *Hình thức = Trực tuyến* | 8 / 15 | 13:50 | **200** | `BaoCaoLopDaoTaoDaDienRa_20260806_1350.xlsx` — 6 816 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Lọc *Hình thức = Trực tiếp* | 1 / 2 | 13:51 | **200** | `BaoCaoLopDaoTaoDaDienRa_20260806_1351.xlsx` — 6 709 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 4 | Lặp lại y hệt lượt 1 (phép thử chống đè tệp) | 9 / 17 | 13:53 | **200** | `BaoCaoLopDaoTaoDaDienRa_20260806_1353.xlsx` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 5 | **Xuất PDF** (A4 · Dọc) | 9 / 17 | 13:54 | **200**, kiểu `application/pdf` | `BaoCaoLopDaoTaoDaDienRa_20260806_1354.pdf` — 33 601 B | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* (`ERR-RPT-04`, `:116`) ở bất kỳ lượt
  nào, cũng **không** có *"Forbidden"* ⇒ vế vòng 1 của đối tác hết lỗi. Mỗi lượt đúng **1** lời gọi xuất,
  **1** khung thông báo (đếm theo mốc giờ khác nhau, bộ theo dõi không lọc trùng).
- **Tên tệp** — đo từ **hai đường độc lập và trùng khít**: header `content-disposition` của máy chủ, và
  **tệp rơi thật về thư mục tải xuống** (đúng thứ người dùng thật nhìn thấy). Khớp khuôn đặc tả `:85` +
  `srs-v3.5.md:6716` (Phụ lục E §H8) — `{TenTep}_{YYYYMMDD_HHmm}.{đuôi}`, PascalCase, không dấu, không gạch
  nối, **có đủ giờ-phút** và giờ-phút **khớp thời điểm xuất thật**. Hai lượt xuất **cùng ngày, cùng bộ lọc**
  (13:48 / 13:53) ra **hai tên khác nhau** ⇒ không đè tệp nhau, đúng chủ đích BA chốt 2026-08-04 khi bắt
  buộc phần giờ-phút. Phần `{TenBaoCao}` là `BaoCaoLopDaoTaoDaDienRa` — **đúng loại báo cáo này**, không
  phải `…DangDienRa` của màn kia.
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): sheet *"Lớp đào tạo đã diễn ra"*, đủ 4 mục đầu tệp
  `:1092` đòi — *BC Lớp đào tạo đã diễn ra* · *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* ·
  *Đơn vị: Toàn quốc* · *Ngày tạo: 06/08/2026*. Số trong tệp khớp **từng con số** với màn của chính lượt đó
  (9 / 17), và bảng *theo đơn vị* cộng dọc bằng đúng thẻ tổng: 6 + 1 + 2 = 9 khóa học · 11 + 3 + 3 = 17 học
  viên (Cục Bổ trợ tư pháp · Bộ Kế hoạch và Đầu tư · Sở Tư pháp Hà Nội).
- Đổi bộ lọc thì tệp đổi theo (`:1280`) — kiểm chéo bằng md5, **3 dạng ra 3 tệp khác nhau**:
  `2569fc2c…` (9/17) · `15928d7b…` (8/15) · `2a641099…` (1/2). Hai nhánh hình thức cộng lại khớp bản không
  lọc: 8 + 1 = 9 khóa học · 15 + 2 = 17 học viên.
- Đo lại bằng **đường thứ hai**: GET báo cáo trả đúng 9/17 · 8/15 · 1/2 theo từng bộ lọc; POST xuất trả 200
  kèm tệp 6 822 byte **bằng đúng** tệp lấy từ giao diện ⇒ hai đường không mâu thuẫn.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế tên tệp đạt. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên
vẹn** đúng vai trò, đúng màn, đúng bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/LDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/LDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), bản dựng V1.0.8, đúng bộ lọc của đối
  tác, khung thông báo **"Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 9 / 17.
  *Ghi chú cách chụp:* khung chỉ sống ~3,2 giây nên phải **hẹn giờ bấm trước rồi mới gọi chụp** — bắt được
  ngay lượt đầu; cả 3 lượt bấm đều là lời gọi xuất trả 403, **không** đổi dữ liệu.
- [`image/LDTBDDDR_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png`](image/LDTBDDDR_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ 9 / 17 và **hai nút Xuất
  đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/LDTBDDDR_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png`](image/LDTBDDDR_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png)
  — phiên CB Nghiệp vụ TW, dạng 1 (đúng bộ lọc đối tác), màn hình **trước** khi bấm Xuất: *Thời điểm tạo
  13:47*, Tổng khóa học 9 · Tổng học viên 17 — mốc đối chiếu số liệu với nội dung tệp.
- [`image/LDTBDDDR_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png`](image/LDTBDDDR_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png)
  — **ngay sau** khi bấm [Xuất Excel] ở dạng 1: **không** có khung thông báo lỗi ở đúng vị trí mà ảnh vòng 2
  của đối tác từng hiện *"Forbidden"*. *(Khung thông báo thành công không kịp vào khung hình — chữ và kết
  quả của lượt này lấy từ bộ theo dõi + phản hồi máy chủ + tệp rơi về máy, ghi trong tệp bằng chứng 08.)*
- [`image/LDTBDDDR_06-03-dang2-loc-hinhthuc-TrucTuyen-man-hinh-truoc-khi-xuat-V108.png`](image/LDTBDDDR_06-03-dang2-loc-hinhthuc-TrucTuyen-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 2 (lọc *Hình thức = Trực tuyến*), *Thời điểm tạo 13:49*, Tổng 8 / 15 — dùng chứng minh tệp xuất bám
  đúng bộ lọc hiện tại.
- [`image/LDTBDDDR_06-04-dang3-loc-hinhthuc-TrucTiep-man-hinh-truoc-khi-xuat-V108.png`](image/LDTBDDDR_06-04-dang3-loc-hinhthuc-TrucTiep-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 3 (lọc *Hình thức = Trực tiếp*), *Thời điểm tạo 13:51*, Tổng 1 / 2 — cộng với ảnh dạng 2 ra đúng
  ảnh dạng 1 (8+1 = 9 · 15+2 = 17).
- [`image/LDTBDDDR_06-05-hop-thoai-tuy-chon-in-PDF-V108.png`](image/LDTBDDDR_06-05-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *"Tùy chọn in báo cáo PDF"* (Khổ giấy · Hướng giấy · [Hủy] [Xuất file]) mà [Xuất PDF] mở ra;
  giữ lại vì đây là bước dễ hiểu nhầm thành *"bấm Xuất PDF không có phản ứng gì"*.
- [`image/LDTBDDDR_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/LDTBDDDR_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · tuổi thọ khung), nguyên văn phản hồi máy chủ
  của cả hai vai trò, vai trò đọc từ vé đăng nhập, tên tệp đo từ cả hai đường, nội dung ô của các tệp .xlsx,
  md5 3 dạng, phép thử chống đè tệp và kết quả đo bằng đường thứ hai.
- Tệp thật hệ thống giao ra (tên gốc hệ thống đặt được giữ nguyên phía sau tiền tố mã case):
  [`testfiles/LDTBDDDR_06-dang1-khong-loc-BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx`](testfiles/LDTBDDDR_06-dang1-khong-loc-BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx)
  · [`testfiles/LDTBDDDR_06-dang2-loc-TrucTuyen-BaoCaoLopDaoTaoDaDienRa_20260806_1350.xlsx`](testfiles/LDTBDDDR_06-dang2-loc-TrucTuyen-BaoCaoLopDaoTaoDaDienRa_20260806_1350.xlsx)
  · [`testfiles/LDTBDDDR_06-dang3-loc-TrucTiep-BaoCaoLopDaoTaoDaDienRa_20260806_1351.xlsx`](testfiles/LDTBDDDR_06-dang3-loc-TrucTiep-BaoCaoLopDaoTaoDaDienRa_20260806_1351.xlsx)
  · [`testfiles/LDTBDDDR_06-dang1-lap-lai-BaoCaoLopDaoTaoDaDienRa_20260806_1353.xlsx`](testfiles/LDTBDDDR_06-dang1-lap-lai-BaoCaoLopDaoTaoDaDienRa_20260806_1353.xlsx)
  · [`testfiles/LDTBDDDR_06-pdf-BaoCaoLopDaoTaoDaDienRa_20260806_1354.pdf`](testfiles/LDTBDDDR_06-pdf-BaoCaoLopDaoTaoDaDienRa_20260806_1354.pdf)

### So sánh vai trò

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Chữ hiện cho người dùng |
|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:400`) | 200, ra đủ 9 / 17 | **200**, nhận được tệp .xlsx/.pdf mở đọc được | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW, đơn vị BTP (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *"Forbidden"* |

### Ghi chú liên quan

- **Bằng chứng vòng 1 của đối tác không thuộc case này:** ô `Ảnh/vieo 1` của dòng 205 trỏ đúng **cùng tệp
  Drive với dòng 200**, và mở ra là màn *BC Lớp đào tạo **đang** diễn ra* (có 2 bộ lọc đặc thù, tổng số 3)
  — tức màn của FR-IX-06. Vế vòng 1 vì vậy đi nhánh *"đối tác không gắn bằng chứng"*: chỉ kết luận
  **hiện trạng trên bản dựng đang đo** (thao tác này hiện chạy đúng đặc tả), **không** kết luận
  *"không phải lỗi"*. Vòng 2 có bằng chứng riêng đúng case, đủ 3 dữ kiện neo.
- **Hai đường đo độc lập cùng kết luận, không mâu thuẫn:** đường giao diện (thao tác chuột thật, đọc chữ
  hiện trên màn) và đường máy chủ (mã HTTP + thân phản hồi) khớp nhau ở cả hai vai trò ⇒ không có điểm nào
  cần hỏi thêm trước khi kết luận.
- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của
  case: nếu BA chốt QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt `:117` thay vì
  `Forbidden`, và phải chặn ngay từ bước Xem cho nhất quán (`:79`); nếu BA chốt QTHT *được* xuất thì đang
  chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoDaoTao_{YYYYMMDD_HHmm}`, hệ thống ra
  `BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85` +
  `srs-v3.5.md:6716` Phụ lục E §H8), **không** ấn định chuỗi `BaoCaoDaoTao`. Tên hệ thống dùng khớp khuôn,
  có đủ giờ-phút, đúng tên loại báo cáo này, hai lượt cùng ngày không đè nhau ⇒ **không** phải khuyết tật.
  *(So với số đo cũ 03/08 — `bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu giờ-phút, có gạch nối — khuôn tên đã
  được sửa đúng ở bản dựng V1.0.8.)*
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006` /
  `BUG-CPCTHTTDVQL-006` / `BUG-CPCTHTTLHDN-006` (Phần 4), `BUG-CTTDVQL-004` (Phần 5),
  `BUG-CLDTBDDDR-006` (Phần 6) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã
  `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng sau vẫn phải verify
  riêng từng case trên đúng màn của nó. **Không mở dòng bug mới trên bảng theo dõi** cho case này.

#### Ghi nhận ngoài vế đối tác nêu — **không** kéo verdict case, chưa mở dòng trên bảng

Ba điểm dưới đây phát hiện trong lúc đo nhưng đối tác **không** nêu ở case này. Ghi lại đầy đủ để phiên
chính quyết có mở dòng riêng hay không; QA không tự mở.

- **D1 — Hai nút Xuất có lúc kẹt ở trạng thái không bấm được, và [Xem báo cáo] ngừng phát lời gọi.** 13:52,
  sau khi **xóa bộ lọc *Hình thức* bằng biểu tượng ✕ (bấm chuột thật)** rồi bấm [Xem báo cáo]: báo cáo
  **có chạy lại** (đường dẫn rụng tham số bộ lọc, *Thời điểm tạo* nhảy 13:52, tổng về lại 9) nhưng
  [Xuất Excel] / [Xuất PDF] **vẫn ở trạng thái không bấm được**, và các cú bấm [Xem báo cáo] tiếp theo
  **không sinh lời gọi nào**. Tải lại trang là hết. Lệch `srs-fr-11-bao-cao.md:1052` / `:1053` — điều kiện
  hiển thị của hai nút **chỉ** là *"Sau khi đã 'Xem báo cáo'"*, không kèm điều kiện nào khác.
  *Đã thử bác bỏ:* chạy lại **đúng nguyên tham số** lúc 13:59 thì nút vẫn bấm được ⇒ giả thuyết "do bộ đệm
  304" **không đứng vững**; **chưa chốt được điều kiện kích hoạt tối thiểu**. Phần 6 quy hiện tượng này
  **hoàn toàn** cho thao tác giả lập — số đo ở đây cho thấy nó **cũng xảy ra sau cú bấm chuột thật**.
  **Không ảnh hưởng phép đo nào của case:** 8/8 lượt xuất đều thực hiện trên báo cáo vừa render xong với
  nút ở trạng thái bấm được.
- **D2 — Báo cáo thiếu chiều dữ liệu mà đặc tả ghi điều kiện hiển thị *"Luôn"*.** `:421` (`theo_hinh_thuc[]`)
  và `:422` (`theo_ky[]`): phản hồi máy chủ có `theoDonVi[]` và `trendData[]` nhưng **không** có
  `theoHinhThuc[]` riêng; tệp .xlsx xuất ra **không có bảng "Theo kỳ"** — dữ liệu tương ứng chỉ tồn tại trên
  màn dưới dạng biểu đồ xu hướng theo tháng.
- **D3 — Bộ lọc trên màn này chạy ĐÚNG; khuyết tật `linhVuc` của màn *đang diễn ra* (D1 Phần 6) KHÔNG lan
  sang đây.** Màn FR-IX-07 **chỉ có 1 bộ lọc đặc thù = *Hình thức*** — đúng `:1070`, **không có** bộ lọc
  *Lĩnh vực*. Giao diện gửi `?hinhThuc=TRUC_TUYEN` khi chạy báo cáo và `"filterDacThu":{"hinhThuc":…}` khi
  xuất; máy chủ áp đúng (9/17 → 8/15 → 1/2) và tệp xuất đổi theo (3 md5 khác nhau).

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần >=1 lớp đào tạo ĐÃ KẾT THÚC trong năm 2026 để báo cáo có dữ liệu; nếu báo
  cáo trống thì nút Xuất sẽ không bật và phép thử không có giá trị.

Các bước:
  1. Đăng nhập admin (QTHT). Vào Báo cáo thống kê. TẢI LẠI TRANG và ghi lại nhãn bản dựng
     trước khi đo.
  2. Loại báo cáo = BC Lớp đào tạo ĐÃ diễn ra (kiểm cả 3 chỗ: chuỗi trong đường dẫn phải là
     lop-dao-tao-da-dien-ra, chữ trong ô chọn, tiêu đề khối kết quả - RẤT DỄ nhầm sang màn
     "đang diễn ra"); Kỳ = Năm 01/01/2026 - 31/12/2026; Đơn vị = Toàn quốc; để trống bộ lọc
     Hình thức. Bấm [Xem báo cáo], chờ ra số liệu.
  3. Cài bộ theo dõi thông báo TRƯỚC khi bấm (không lọc trùng, đọc innerText, lấy mẫu chữ
     theo thời gian - xem tools/toast-capture.js), rồi bấm [Xuất Excel].
  4. Ghi lại: chữ hiện cho người dùng · mã trả về của POST /api/v1/bao-cao/export · số tệp
     nhận được.
  5. Lặp lại bước 2-4 bằng tài khoản cbnv_tw_05 (CB Nghiệp vụ TW) để đối chiếu, và MỞ TỆP
     xuất ra đọc: phải còn đủ 4 mục đầu tệp (tên BC, kỳ, đơn vị, ngày tạo), còn đủ 2 con số
     Tổng khóa học / Tổng học viên và bảng theo đơn vị, số khớp màn và cộng dọc khớp tổng.
  6. Đo thêm 2 dạng lọc Hình thức = Trực tuyến và Trực tiếp: tệp xuất phải đổi theo bộ lọc,
     và hai nhánh cộng lại phải bằng bản không lọc.

PASS khi:
  - Vai trò QTHT: KHÔNG còn thấy chuỗi "Forbidden" trên màn. Nếu hệ thống vẫn từ chối thì
    câu hiện ra phải là câu tiếng Việt cho biết người dùng không có quyền (yêu cầu :117);
    nếu BA chốt QTHT được xuất thì phải nhận được tệp .xlsx mở đọc được.
  - Bước Xem và bước Xuất nhất quán: không còn cảnh cho xem đủ số liệu rồi chặn ở bước xuất.
    Nếu vai trò bị cấm thì phải chặn ngay từ bước Xem (yêu cầu :79).
  - Vai trò cbnv_tw_05 vẫn xuất được cả Excel lẫn PDF ở cả 3 dạng lọc, tên tệp vẫn đúng khuôn
    có giờ-phút và mang đúng tên loại báo cáo "đã diễn ra", nội dung tệp vẫn đúng như mô tả ở
    bước 5 (không hồi quy).

FAIL nếu:
  - Còn bất kỳ chỗ nào hiện chuỗi kỹ thuật tiếng Anh (Forbidden / Unauthorized / Internal
    Server Error) cho người dùng cuối.
  - Sửa bằng cách ẩn/làm mờ nút Xuất mà bước Xem vẫn cho vào: người dùng vẫn không biết vì
    sao mình không xuất được -> chưa đạt :117.
  - Vai trò CB Nghiệp vụ bị chặn theo, hoặc tệp xuất mất mục đầu tệp / mất chiều theo đơn vị
    / mất phần giờ-phút trong tên tệp / tên tệp mang tên loại báo cáo khác (hồi quy).

Bẫy hay gặp:
  - Khung thông báo chỉ sống ~3,2 giây và thư viện giao diện CẬP NHẬT CHỮ NGAY TRONG khung cũ
    chứ không mọc khung mới. Nếu chỉ ghi "khung nào mới mọc" sẽ chỉ thấy "Đang tạo file..."
    và kết luận nhầm là hệ thống im lặng. Phải lấy mẫu chữ theo thời gian; muốn chụp được thì
    hẹn giờ bấm trước rồi mới gọi chụp.
  - Đo bằng vai trò CB Nghiệp vụ rồi kết luận "hết lỗi" là sai. Phải đo bằng đúng vai trò
    QTHT như trên bằng chứng vòng 2 của đối tác.
  - Rất dễ mở nhầm màn "Lớp đào tạo ĐANG diễn ra" (case dòng 200) - hai màn khác endpoint,
    khác bộ lọc, khác bộ chỉ số. Kiểm đủ 3 chỗ như bước 2.
  - [Xuất PDF] KHÔNG tải tệp ngay: nó mở hộp thoại "Tùy chọn in báo cáo PDF", phải bấm tiếp
    [Xuất file]. Bỏ qua bước này rất dễ báo oan "bấm không có phản ứng"; hộp thoại còn mở
    cũng nuốt luôn cú bấm [Xuất Excel] ngay sau đó.
  - Tab trình duyệt mở lâu vẫn chạy mã cũ: phải tải lại trang và ghi lại nhãn bản dựng trước
    khi kết luận.
  - Số trên màn có thể là số máy chủ đã nhớ sẵn: xem trường "Thời điểm tạo" có nhảy theo lượt
    bấm không, nếu đứng yên thì đổi ngày kết thúc 1 ngày để lấy số mới.
  - Sau khi xóa bộ lọc rồi xem lại, hai nút Xuất có thể kẹt ở trạng thái mờ và [Xem báo cáo]
    ngừng phát lời gọi (ghi nhận D1). Tải lại trang rồi đo lại - đừng ghi nhầm thành "nút
    xuất biến mất sau khi dev sửa".
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy
nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở
[`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2 trước khi dev chọn hướng sửa. Ba ghi nhận D1 · D2 · D3 ở trên
chuyển **phiên chính** quyết, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 7)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — HTPLDN **V1.0.8**, bó mã giao diện `assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`, 1 123 581 byte) — **tự đo**, không chép từ case khác |
| **Màn đo** | Báo cáo thống kê → **BC Lớp đào tạo ĐÃ diễn ra** (`/bao-cao?loai=lop-dao-tao-da-dien-ra`), FR-IX-07 / UC130 (`srs-fr-11-bao-cao.md:389`) |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng `isolatedContext="qa-ldtbdddr06-0806"` (CB Nghiệp vụ) và `"qa-ldtbdddr06-qtht"` (QTHT) — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước** mỗi phép đo quyết định; QTHT trả `vaiTro ["QTHT"] · capDonVi "TW" · donViId 0000…0001` |
| **Khung giờ đo** | 2026-08-06 13:41 → 14:01 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 9 khóa đã kết thúc / 17 học viên trong kỳ Năm 2026, trải 3 đơn vị và đủ cả 2 nhánh hình thức, đủ cho cả 3 dạng biến thể |

*Phần 7 generated: 2026-08-06 14:10:00 | QA Automation via Claude Code*

---

# Phần 8 — Batch B5 (BC Số lượng CG/TVV)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 210 |
| **Ngày** | 2026-08-06 14:50:00 |
| **Môi trường** | https://18.143.165.120.nip.io — nhãn ứng dụng **V1.0.8**, bó mã `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, `last-modified` 06/08/2026 07:13:15 GMT) — **tự đo lúc 14:47**, không chép từ case khác |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback Rule 7 |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW, đơn vị BTP `…0001`) — đúng vai trò đối tác dùng ở **cả hai** ảnh |
| **Tiêu chí** | [`tieuchi/CGTVPL_06.md`](tieuchi/CGTVPL_06.md) — viết xong **trước** khi mở màn Báo cáo thống kê |

> 🔴 **Cảnh báo trôi bản dựng — đọc trước khi so số với các Phần trên.** Môi trường được **dựng lại lúc
> 07:13 GMT (14:13 giờ máy)**, tức **sau khi** các Phần 2–7 đo xong. Các Phần đó đo trên bó mã
> `assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`); Phần 8 đo trên
> `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`). **Nhãn trong ứng dụng vẫn là `V1.0.8`
> ở cả hai lần dựng** ⇒ **không được dùng nhãn để nhận biết bản dựng**. Số đo giữa Phần 8 và các Phần trên
> **không so trực tiếp được với nhau**.

> **Quan hệ với Phần 2 · 3 · 4 · 5 · 6 · 7:** cùng một chức năng xuất báo cáo
> (`POST /api/v1/bao-cao/export`), khác loại báo cáo. Dòng 210 vẫn được đo **riêng** trên đúng màn của nó —
> **BC Số lượng CG/TVV** (FR-IX-08 / UC131, `srs-fr-11-bao-cao.md:429`). Màn này khác hẳn các màn đào tạo ở:
> đường dẫn dữ liệu (`so-luong-cg-tvv`), bản chất báo cáo (**snapshot** đếm người đang hoạt động, `:438`),
> bộ chỉ số đầu ra (`tong_tvv` / `so_tvv` / `so_cg`) và **có tới 2 bộ lọc đặc thù** — *Loại TVV* + *Lĩnh vực
> chuyên môn* (`:448`, `:449`, `:1071`). Không suy kết quả từ case anh em.

## Bug Summary Table (Phần 8)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CGTVPL-006 | Major | P1 | Permission | `CGTVPL_06` (tab `bug` dòng 210) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` | [`image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Open |

---

## BUG-CGTVPL-006 — Vai trò QTHT xem được BC Số lượng CG/TVV nhưng bị chặn khi Xuất Excel/PDF, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 14:47 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bó mã `index-DIABnbIr.js`.
> Vế đối tác nêu ở vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được **7/7 lượt** (4 dạng bộ lọc + 1 lượt lặp chống đè + 1 PDF + 1 gọi thẳng máy chủ), tệp
> mở đọc được, đủ 4 mục đầu tệp, số khớp màn từng con số và cộng dọc khớp tổng. Vế tên tệp cũng **đạt**
> (`BaoCaoSoLuongCgTvv_20260806_1429.xlsx` — đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}`, hai lượt cùng ngày ra
> hai tên khác nhau). Vế vòng 2 (*"Forbidden"*, TKM retest 31/07) **tái hiện nguyên vẹn 4/4 lượt** ở đúng vai
> trò đối tác đã dùng · **không seed, không tạo/sửa/xoá bản ghi nào** — toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Số lượng CG/TVV**, người dùng vai trò **Quản trị hệ thống
(QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng Tư vấn viên 6 · Số Tư vấn viên 4 ·
Số Chuyên gia 2, kèm bảng theo đơn vị và theo lĩnh vực) và **hiện hai nút [Xuất Excel] / [Xuất PDF] ở trạng
thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho
người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ, không cho
người dùng biết chuyện gì đã xảy ra và phải làm gì tiếp. Cùng thao tác, cùng bộ lọc, **cùng đơn vị**, vai trò
Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`; `/api/v1/auth/me` và vé đăng nhập đều ghi
   `vaiTro = ["QTHT"]`, `capDonVi = "TW"`, `donViId = 00000000-0000-4000-8000-000000000001` = *Cục Bổ trợ tư
   pháp - Bộ Tư pháp*) — đúng vai trò và đơn vị đọc được ở góc phải trên **cả hai** bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Số lượng CG/TVV** (đường dẫn phải chứa `loai=so-luong-cg-tvv` — **không** nhầm
   sang *BC Đánh giá hiệu quả HTPL*); *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026);
   *Đơn vị* = **Toàn quốc**; để trống cả hai bộ lọc *Loại TVV* và *Lĩnh vực chuyên môn* — đúng cấu hình trên
   ảnh vòng 2 của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (6 · 4 · 2 + bảng theo đơn vị + bảng theo lĩnh vực +
   biểu đồ), không có cảnh báo nào; hai nút Xuất bật lên.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi
  kỹ thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` ghi điều kiện hiển thị của nút Xuất Excel chỉ là *"Sau khi đã 'Xem báo cáo'"*,
  **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 14:40–14:47:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/so-luong-cg-tvv?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **Tổng Tư vấn viên 6 · Số Tư vấn viên 4 · Số Chuyên gia 2** (*Thời điểm tạo
  06/08/2026 14:40*) — **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; **1** lời gọi, **1** khung thông báo (không có hiện
  tượng 2 thông báo chồng); chữ người dùng đọc được đổi **tại chỗ trong khung cũ**: *"Đang tạo file..."* →
  **"Forbidden"** (khung nằm trong vùng nhìn thấy, `w=1432 · h=42`); **0 tệp** được giao. Bấm chuột thật
  **2 lượt** (14:41 và 14:47) — lượt nào cũng ra đúng chữ đó.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_SO_LUONG_CG_TVV","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T07:41:07.458Z","requestId":"ca4646b9-2e53-4ca1-a4d4-eafe3a7f9948"}}
  ```
  Header trả về **không có** `content-disposition` ⇒ không có tệp đính kèm. Chữ trên màn **trùng khít**
  `error.message` của máy chủ ⇒ giao diện đẩy nguyên chuỗi kỹ thuật ra cho người dùng cuối.
- Đo lại bằng **đường thứ hai** (gọi thẳng máy chủ, cùng phiên QTHT, cùng thân yêu cầu): `formatXuat` =
  **XLSX** → **403**, `formatXuat` = **PDF** → **403**, thân phản hồi cùng mã `ERR-PERM-SYS-00-01`.
  ⇒ Cộng lại **4/4 lượt** (2 bấm chuột + 2 gọi thẳng) đều bị chặn — **không phải chập chờn**, và **không**
  phải lỗi thao tác trên giao diện.
- **Quét thư mục tải xuống** với mốc *"mới hơn 14:40:30"*: **không có** tệp `.xlsx`/`.pdf` nào ⇒ qua 4 lượt
  thử, người dùng vai trò này ra về tay trắng.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, 4 dạng bộ lọc + 1 lượt lặp + 1 lượt PDF:**

| Lượt | Bộ lọc / định dạng | Màn trước khi bấm (Tổng/TVV/CG) | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc · **cả 2 bộ lọc trống** (đúng cấu hình vòng 2 của đối tác) | 6 / 4 / 2 | 14:29 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoSoLuongCgTvv_20260806_1429.xlsx` — 7 034 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Lọc *Loại TVV = Tư vấn viên* | 4 / 4 / 0 | 14:31 | **200** | `BaoCaoSoLuongCgTvv_20260806_1431.xlsx` — 6 954 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Lọc *Loại TVV = Chuyên gia* | 2 / 0 / 2 | 14:32 | **200** | `BaoCaoSoLuongCgTvv_20260806_1432.xlsx` — 6 871 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 4 | Lọc *Lĩnh vực chuyên môn = Thuế* (**đúng cấu hình vòng 1 của đối tác**) | 6 / 4 / 2 — **không đổi** | 14:35 | **200** | `BaoCaoSoLuongCgTvv_20260806_1435.xlsx` — 7 034 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 5 | Lặp lại y hệt lượt 1 (phép thử chống đè tệp) | 6 / 4 / 2 | 14:36 | **200** | `BaoCaoSoLuongCgTvv_20260806_1436.xlsx` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 6 | **Xuất PDF** (qua hộp thoại *Tùy chọn in báo cáo PDF*) | 6 / 4 / 2 | 14:37 | **200**, `%PDF-1.3` | `BaoCaoSoLuongCgTvv_20260806_1437.pdf` — 34 227 B | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* (`ERR-RPT-04`, `:116`) ở bất kỳ lượt
  nào, cũng **không** có *"Forbidden"* ⇒ vế vòng 1 của đối tác hết lỗi. Mỗi lượt đúng **1** lời gọi xuất,
  **1** khung thông báo (đếm theo mốc giờ khác nhau, bộ theo dõi không lọc trùng, tự kiểm 1 observer).
- **Tên tệp** — đo từ **hai đường độc lập và trùng khít**: header `content-disposition` của máy chủ
  (`attachment; filename="BaoCaoSoLuongCgTvv_20260806_1445.xlsx"`), và **tệp rơi thật về thư mục tải xuống**
  (đúng thứ người dùng thật nhìn thấy). Khớp khuôn đặc tả `:85` + `srs-v3.5.md:6716` (Phụ lục E §H8) —
  `{TenTep}_{YYYYMMDD_HHmm}.{đuôi}`, PascalCase, không dấu, không gạch nối, **có đủ giờ-phút** và giờ-phút
  **khớp thời điểm xuất thật** (7 tệp → 7 mốc giờ-phút khác nhau). Hai lượt xuất **cùng ngày, cùng bộ lọc**
  (14:29 / 14:36) ra **hai tên khác nhau** ⇒ không đè tệp nhau, đúng chủ đích BA chốt 2026-08-04 khi bắt
  buộc phần giờ-phút. Phần `{TenBaoCao}` là `BaoCaoSoLuongCgTvv` — **đúng loại báo cáo này**.
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): sheet *"BC Số lượng CG TVV"*, đủ 4 mục đầu tệp `:1092`
  đòi — *BC Số lượng CG/TVV* · *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · *Đơn vị: Toàn quốc* ·
  *Ngày tạo: 06/08/2026*. Số trong tệp khớp **từng con số** với màn của chính lượt đó (6 / 4 / 2), bảng
  *Theo đơn vị* cộng dọc bằng đúng thẻ tổng — TVV 1+1+1+1 = 4 · CG 2+0+0+0 = 2 · Tổng 3+1+1+1 = 6 (Cục Bổ
  trợ tư pháp · Bộ Kế hoạch và Đầu tư · Sở Tư pháp Hà Nội · Sở Tư pháp An Giang), và `so_tvv + so_cg` =
  4 + 2 = 6 = `tong_tvv`.
- **Bộ lọc *Loại TVV* chạy đúng** — AC `:470` (*"lọc loại CG → chỉ hiển thị Chuyên gia"*) thoả: lượt 3 cho
  tệp chỉ còn Chuyên gia (2 / 0 / 2, bảng theo đơn vị rút còn 1 dòng). Hai nhánh cộng lại khớp bản không lọc:
  4 (TVV) + 2 (CG) = 6.
- **Bộ lọc *Lĩnh vực chuyên môn* KHÔNG có tác dụng** — lượt 4 cho tệp **giống hệt từng ô** với lượt 1. Đây là
  điểm **đối tác không nêu**, ghi riêng ở mục *Ghi nhận ngoài vế đối tác nêu* bên dưới và **không** kéo
  verdict của case.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế tên tệp đạt. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên
vẹn** đúng vai trò, đúng màn, đúng cấu hình bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), đúng cấu hình bộ lọc vòng 2 của đối
  tác, khung thông báo **đỏ chữ "Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 6 · 4 · 2.
  *Ghi chú cách chụp:* khung chỉ sống ~3 giây và thư viện giao diện **thay chữ ngay trong khung cũ**, nên
  phải **hẹn giờ bấm trước rồi mới gọi chụp**; cả 2 lượt bấm đều là lời gọi xuất trả 403, **không** đổi dữ liệu.
- [`image/CGTVPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png`](image/CGTVPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ 6 · 4 · 2 và **hai nút
  Xuất đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/CGTVPL_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png`](image/CGTVPL_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png)
  — phiên CB Nghiệp vụ TW, dạng 1 (đúng cấu hình vòng 2 của đối tác), màn hình **trước** khi bấm Xuất:
  *Thời điểm tạo 14:28*, 6 · 4 · 2 — mốc đối chiếu số liệu với nội dung tệp.
- [`image/CGTVPL_06-02-dang2-loc-LoaiTVV-TuVanVien-man-hinh-truoc-khi-xuat-V108.png`](image/CGTVPL_06-02-dang2-loc-LoaiTVV-TuVanVien-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 2 (lọc *Loại TVV = Tư vấn viên*), số đổi thành 4 · 4 · 0 — dùng chứng minh tệp xuất bám đúng bộ lọc.
- [`image/CGTVPL_06-03-dang3-loc-LoaiTVV-ChuyenGia-man-hinh-truoc-khi-xuat-V108.png`](image/CGTVPL_06-03-dang3-loc-LoaiTVV-ChuyenGia-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 3 (lọc *Loại TVV = Chuyên gia*), 2 · 0 · 2, bảng theo đơn vị rút còn 1 dòng ⇒ AC `:470` thoả; cộng
  với ảnh dạng 2 ra đúng ảnh dạng 1 (4 + 2 = 6).
- [`image/CGTVPL_06-04-dang4-loc-LinhVuc-Thue-so-lieu-khong-doi-V108.png`](image/CGTVPL_06-04-dang4-loc-LinhVuc-Thue-so-lieu-khong-doi-V108.png)
  — dạng 4 (lọc *Lĩnh vực chuyên môn = Thuế*, **đúng cấu hình vòng 1 của đối tác**): số liệu **vẫn 6 · 4 ·
  2**, y hệt dạng 1 — ảnh nền cho ghi nhận D1 bên dưới.
- [`image/CGTVPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png`](image/CGTVPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *"Tùy chọn in báo cáo PDF"* mà [Xuất PDF] mở ra; giữ lại vì đây là bước dễ hiểu nhầm thành
  *"bấm Xuất PDF không có phản ứng gì"*.
- [`image/CGTVPL_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/CGTVPL_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · độ mờ), nguyên văn phản hồi máy chủ của cả hai
  vai trò (kể cả thân 403), vai trò đọc từ vé đăng nhập, tên tệp đo từ cả hai đường, nội dung ô của 5 tệp
  .xlsx đọc bằng `openpyxl`, md5 từng tệp, phép thử chống đè tệp và **bảng đo bộ lọc 7 dòng**.
- Tệp thật hệ thống giao ra (tên gốc hệ thống đặt được giữ nguyên phía sau tiền tố mã case):
  [`testfiles/CGTVPL_06-dang1-khong-loc-BaoCaoSoLuongCgTvv_20260806_1429.xlsx`](testfiles/CGTVPL_06-dang1-khong-loc-BaoCaoSoLuongCgTvv_20260806_1429.xlsx)
  · [`testfiles/CGTVPL_06-dang2-loc-TVV-BaoCaoSoLuongCgTvv_20260806_1431.xlsx`](testfiles/CGTVPL_06-dang2-loc-TVV-BaoCaoSoLuongCgTvv_20260806_1431.xlsx)
  · [`testfiles/CGTVPL_06-dang3-loc-CG-BaoCaoSoLuongCgTvv_20260806_1432.xlsx`](testfiles/CGTVPL_06-dang3-loc-CG-BaoCaoSoLuongCgTvv_20260806_1432.xlsx)
  · [`testfiles/CGTVPL_06-dang4-loc-LinhVuc-Thue-BaoCaoSoLuongCgTvv_20260806_1435.xlsx`](testfiles/CGTVPL_06-dang4-loc-LinhVuc-Thue-BaoCaoSoLuongCgTvv_20260806_1435.xlsx)
  · [`testfiles/CGTVPL_06-dang1-lap-lai-BaoCaoSoLuongCgTvv_20260806_1436.xlsx`](testfiles/CGTVPL_06-dang1-lap-lai-BaoCaoSoLuongCgTvv_20260806_1436.xlsx)
  · [`testfiles/CGTVPL_06-pdf-BaoCaoSoLuongCgTvv_20260806_1437.pdf`](testfiles/CGTVPL_06-pdf-BaoCaoSoLuongCgTvv_20260806_1437.pdf)

### So sánh vai trò

Phép đối chứng đổi **đúng một biến** — cùng đường dẫn, cùng thân yêu cầu **từng chữ**, cùng
`donViId …0001`, cùng phiên đo, chỉ khác vai trò:

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Header trả về | Chữ hiện cho người dùng |
|---|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:440`) | 200, ra đủ 6 · 4 · 2 | **200**, nhận được tệp .xlsx/.pdf mở đọc được | `content-disposition: attachment; filename="BaoCaoSoLuongCgTvv_20260806_1445.xlsx"` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW, **cùng đơn vị BTP** (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *(không có `content-disposition`)* | *"Forbidden"* |

⇒ Đường xuất tệp **không hỏng**; đúng vai trò thì chạy. Chỉ vai trò QTHT bị chặn, và bị chặn **sau khi** đã
được cho xem đủ số liệu.

### Ghi chú liên quan

- **Cả hai bằng chứng của đối tác đều đúng case này** — kiểm bằng 3 chỗ: chuỗi `so-luong-cg-tvv` trong đường
  dẫn · chữ trong ô chọn *Loại báo cáo* · tiêu đề khối kết quả *BC Số lượng CG/TVV*. **Không** nhầm với
  *BC Đánh giá hiệu quả HTPL* (FR-IX-09). Tuy vậy **hai vòng không so trực tiếp được với nhau**: cùng vai trò
  và cùng loại báo cáo, nhưng khác bản dựng (V1.0 → V1.0.3), khác đơn vị (Cục BTTP → Toàn quốc) và khác bộ
  lọc Lĩnh vực (Thuế → trống) ⇒ đã đo **cả hai cấu hình**, không chỉ cấu hình vòng 2.
- **Hai đường đo độc lập cùng kết luận, không mâu thuẫn:** đường giao diện (thao tác chuột thật, đọc chữ
  hiện trên màn) và đường máy chủ (mã HTTP + thân phản hồi) khớp nhau ở cả hai vai trò ⇒ không có điểm nào
  cần hỏi thêm trước khi kết luận.
- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của
  case: nếu BA chốt QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt `:117` thay vì
  `Forbidden`, và phải chặn ngay từ bước Xem cho nhất quán (`:79`); nếu BA chốt QTHT *được* xuất thì đang
  chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoDanhGia_{YYYYMMDD_HHmm}`, hệ thống ra
  `BaoCaoSoLuongCgTvv_20260806_1429.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85` + `srs-v3.5.md:6716`
  Phụ lục E §H8), **không** ấn định chuỗi `BaoCaoDanhGia` — chuỗi đó thực ra là tên của **loại báo cáo khác**
  (*BC Đánh giá hiệu quả HTPL*, FR-IX-09), đối tác chép nhầm sang dòng này. Tên hệ thống dùng khớp khuôn, có
  đủ giờ-phút, đúng tên loại báo cáo này, hai lượt cùng ngày không đè nhau ⇒ **không** phải khuyết tật.
  *(So với số đo cũ 03/08 — `bao-cao-so-luong-cg-tvv-2026-08-03.xlsx`, thiếu giờ-phút, có gạch nối — khuôn
  tên đã được sửa đúng ở bản dựng đang đo.)*
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006` /
  `BUG-CPCTHTTDVQL-006` / `BUG-CPCTHTTLHDN-006` (Phần 4), `BUG-CTTDVQL-004` (Phần 5),
  `BUG-CLDTBDDDR-006` (Phần 6), `BUG-LDTBDDDR-006` (Phần 7) — cùng endpoint `POST /api/v1/bao-cao/export`,
  cùng mã `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng sau vẫn phải
  verify riêng từng case trên đúng màn của nó. **Không mở dòng bug mới trên bảng theo dõi** cho case này.

#### Ghi nhận ngoài vế đối tác nêu — **không** kéo verdict case, chưa mở dòng trên bảng

Điểm dưới đây phát hiện trong lúc đo nhưng đối tác **không** nêu ở case này (cả hai ảnh chỉ nêu thông báo
khi bấm xuất). Ghi lại đầy đủ để phiên chính quyết có mở dòng riêng hay không; QA không tự mở.

- **D1 — Bộ lọc *Lĩnh vực chuyên môn* của màn này KHÔNG có tác dụng: giao diện gửi khoá `linhVucCm`, máy chủ
  chỉ nhận `linhVucId`.** Đo cùng phiên, cùng kỳ, cùng khoảng thời gian, chỉ đổi **tên khoá**
  (lĩnh vực *Thuế* = `bbbbbbbb-0000-4000-8000-000000000018`):

  | Khoá gửi lên | Mã | Tổng | TVV | CG | Dòng theo ĐV | Dòng theo LV | `ngayTaoBc` |
  |---|:-:|:-:|:-:|:-:|:-:|:-:|---|
  | *(không có)* | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
  | **`linhVucCm`** ← giao diện gửi | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
  | **`linhVucId`** ← máy chủ nhận | 200 | **1** | **0** | **1** | **1** | **1** | `07:47:30.053Z` |
  | `linhVuc` | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
  | `linh_vuc_id` | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
  | `loaiTvv=CG` *(đối chứng)* | 200 | **2** | **0** | **2** | 1 | 4 | `07:47:30.297Z` |
  | `loaiTvv=TVV` *(đối chứng)* | 200 | **4** | **4** | **0** | 4 | 2 | `07:47:30.370Z` |

  **Đã loại trừ nhớ đệm bằng bằng chứng cứng:** 4 dòng cho ra 6/4/2 dùng **chung một `ngayTaoBc`**
  `07:45:41.477Z` ⇒ máy chủ coi chúng là **cùng một khoá nhớ đệm**, tức `linhVucCm` / `linhVuc` /
  `linh_vuc_id` **không hề tham gia** khoá; còn `linhVucId` và `loaiTvv` sinh `ngayTaoBc` **mới** ⇒ được nhận.
  Hai hành vi này không thể giải thích bằng nhớ đệm.
  Ảnh hưởng tới tệp xuất: thân lệnh xuất của lượt 4 có ghi
  `"filterDacThu":{"linhVucCm":"bbbbbbbb-…-018"}` — tức giao diện **có** gửi bộ lọc lên — nhưng tệp nhận về
  **giống hệt từng ô** với bản không lọc ⇒ lệch `:1280` (*"file xuất theo bộ lọc hiện tại"*) và làm điều kiện
  `:449` (`linh_vuc_id`) mất tác dụng. Kích thước tệp qua gọi thẳng: không lọc 7 033 B · `linhVucCm` 7 033 B
  (y hệt) · `linhVucId` 6 789 B · `loaiTvv=CG` 6 870 B.
  **Liên hệ với ghi nhận của màn khác:** màn FR-IX-06 có khuyết tật **cùng kiểu** (giao diện đặt tên khoá
  khác máy chủ) nhưng **khác chuỗi** — bên đó gửi `linhVuc`, bên này gửi `linhVucCm` ⇒ **sửa phải sửa cả hai
  chỗ**, không phải một. Bộ lọc *Loại TVV* của màn này **chạy đúng**, AC `:470` thoả.
  **Không ảnh hưởng phép đo nào của case:** 7/7 lượt xuất của vai trò CB Nghiệp vụ đều thực hiện trên báo cáo
  vừa render xong với nút ở trạng thái bấm được, và verdict REOPEN đứng vững chỉ bằng vế *"Forbidden"*.

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần >=1 chuyên gia/tư vấn viên ĐANG HOẠT ĐỘNG để báo cáo có dữ liệu; nếu báo
  cáo trống thì nút Xuất sẽ không bật và phép thử không có giá trị.

Các bước:
  1. Đăng nhập admin (QTHT). Vào Báo cáo thống kê. TẢI LẠI TRANG và ghi lại bản dựng trước
     khi đo - ghi bằng TÊN BÓ MÃ assets/index-*.js, ĐỪNG ghi bằng nhãn V1.0.x: hai lần dựng
     khác nhau ngày 06/08 đều mang nhãn V1.0.8.
  2. Loại báo cáo = BC Số lượng CG/TVV (kiểm cả 3 chỗ: chuỗi trong đường dẫn phải là
     so-luong-cg-tvv, chữ trong ô chọn, tiêu đề khối kết quả - DỄ nhầm sang BC Đánh giá hiệu
     quả HTPL); Kỳ = Năm 01/01/2026 - 31/12/2026; Đơn vị = Toàn quốc; để trống cả hai bộ lọc
     Loại TVV và Lĩnh vực chuyên môn. Bấm [Xem báo cáo], chờ ra số liệu.
  3. Cài bộ theo dõi thông báo TRƯỚC khi bấm (không lọc trùng, đọc innerText, lấy mẫu chữ
     theo thời gian - xem tools/toast-capture.js), rồi bấm [Xuất Excel].
  4. Ghi lại: chữ hiện cho người dùng · mã trả về của POST /api/v1/bao-cao/export · số tệp
     nhận được.
  5. Lặp lại bước 2-4 bằng tài khoản cbnv_tw_05 (CB Nghiệp vụ TW) để đối chiếu, và MỞ TỆP
     xuất ra đọc: phải còn đủ 4 mục đầu tệp (tên BC, kỳ, đơn vị, ngày tạo), còn đủ 3 con số
     Tổng CG/TVV - Số TVV - Số CG, bảng theo đơn vị và bảng theo lĩnh vực; số khớp màn, cộng
     dọc khớp tổng và Số TVV + Số CG = Tổng.
  6. Đo thêm 2 dạng lọc Loại TVV = Tư vấn viên và = Chuyên gia: tệp xuất phải đổi theo bộ lọc,
     và hai nhánh cộng lại phải bằng bản không lọc.

PASS khi:
  - Vai trò QTHT: KHÔNG còn thấy chuỗi "Forbidden" trên màn. Nếu hệ thống vẫn từ chối thì
    câu hiện ra phải là câu tiếng Việt cho biết người dùng không có quyền (yêu cầu :117);
    nếu BA chốt QTHT được xuất thì phải nhận được tệp .xlsx mở đọc được.
  - Bước Xem và bước Xuất nhất quán: không còn cảnh cho xem đủ số liệu rồi chặn ở bước xuất.
    Nếu vai trò bị cấm thì phải chặn ngay từ bước Xem (yêu cầu :79).
  - Vai trò cbnv_tw_05 vẫn xuất được cả Excel lẫn PDF ở cả 4 dạng lọc, tên tệp vẫn đúng khuôn
    có giờ-phút và mang đúng tên loại báo cáo "số lượng CG/TVV", nội dung tệp vẫn đúng như mô
    tả ở bước 5 (không hồi quy).

FAIL nếu:
  - Còn bất kỳ chỗ nào hiện chuỗi kỹ thuật tiếng Anh (Forbidden / Unauthorized / Internal
    Server Error) cho người dùng cuối.
  - Sửa bằng cách ẩn/làm mờ nút Xuất mà bước Xem vẫn cho vào: người dùng vẫn không biết vì
    sao mình không xuất được -> chưa đạt :117.
  - Vai trò CB Nghiệp vụ bị chặn theo, hoặc tệp xuất mất mục đầu tệp / mất bảng theo đơn vị /
    mất bảng theo lĩnh vực / mất phần giờ-phút trong tên tệp / tên tệp mang tên loại báo cáo
    khác (hồi quy).

Bẫy hay gặp:
  - Khung thông báo chỉ sống ~3 giây và thư viện giao diện CẬP NHẬT CHỮ NGAY TRONG khung cũ
    chứ không mọc khung mới. Nếu chỉ ghi "khung nào mới mọc" sẽ chỉ thấy "Đang tạo file..."
    và kết luận nhầm là hệ thống im lặng. Phải lấy mẫu chữ theo thời gian; muốn chụp được thì
    hẹn giờ bấm trước rồi mới gọi chụp.
  - Đo bằng vai trò CB Nghiệp vụ rồi kết luận "hết lỗi" là sai. Phải đo bằng đúng vai trò
    QTHT như trên bằng chứng của đối tác.
  - Rất dễ mở nhầm màn "BC Đánh giá hiệu quả HTPL" - màn đó có bộ lọc Đợt đánh giá và chỉ số
    điểm trung bình, khác hẳn 3 thẻ đếm người ở đây. Kiểm đủ 3 chỗ như bước 2.
  - [Xuất PDF] KHÔNG tải tệp ngay: nó mở hộp thoại "Tùy chọn in báo cáo PDF", phải bấm tiếp
    nút xác nhận. Bỏ qua bước này rất dễ báo oan "bấm không có phản ứng"; hộp thoại còn mở
    cũng nuốt luôn cú bấm [Xuất Excel] ngay sau đó.
  - Tab trình duyệt mở lâu vẫn chạy mã cũ: phải tải lại trang; và ghi bản dựng bằng tên bó mã
    assets/index-*.js chứ đừng tin nhãn V1.0.x.
  - Số trên màn có thể là số máy chủ đã nhớ sẵn: xem trường "Thời điểm tạo" có nhảy theo lượt
    bấm không, nếu đứng yên thì đổi ngày kết thúc 1 ngày để lấy số mới.
  - Bộ lọc Lĩnh vực chuyên môn hiện KHÔNG có tác dụng (ghi nhận D1). Đừng dùng bộ lọc đó làm
    phép thử "tệp xuất bám bộ lọc" - hãy dùng bộ lọc Loại TVV.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy
nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở
[`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2 trước khi dev chọn hướng sửa. Ghi nhận D1 ở trên chuyển **phiên
chính** quyết, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 8)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — nhãn HTPLDN **V1.0.8**, bó mã giao diện `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, etag `W/"6a74340b-1124ed"`, `last-modified` Thu, 06 Aug 2026 07:13:15 GMT) — **tự đo lúc 14:47**, không chép từ case khác. ⚠️ Bản dựng này **mới hơn** bản các Phần 2–7 đo (`index-CNwX9JjX.js`) dù **nhãn không đổi** |
| **Màn đo** | Báo cáo thống kê → **BC Số lượng CG/TVV** (`/bao-cao?loai=so-luong-cg-tvv`), FR-IX-08 / UC131 (`srs-fr-11-bao-cao.md:429`) |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng `isolatedContext="qa-cgtvpl06-cbnv"` (CB Nghiệp vụ) và `"qa-cgtvpl06-qtht"` (QTHT) — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước** mỗi phép đo quyết định; QTHT trả `vaiTro ["QTHT"] · capDonVi "TW" · donViId 0000…0001`; CB Nghiệp vụ trả `vaiTro ["CB_NV_TW"] · capDonVi "TW" · donViId 0000…0001` — **cùng đơn vị**, chỉ khác vai trò |
| **Khung giờ đo** | 2026-08-06 14:26 → 14:47 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 6 CG/TVV đang hoạt động trong kỳ Năm 2026 (4 TVV + 2 CG), trải 4 đơn vị và 5 lĩnh vực (gồm cả *Thuế* mà đối tác dùng ở vòng 1), đủ cho cả 4 dạng biến thể |

*Phần 8 generated: 2026-08-06 14:50:00 | QA Automation via Claude Code*

---

# Phần 9 — Batch B5 (BC Đánh giá hiệu quả HTPL)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 214 |
| **Ngày** | 2026-08-06 15:45:00 |
| **Môi trường** | https://18.143.165.120.nip.io — nhãn ứng dụng **V1.0.8**, bó mã `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, `last-modified` 06/08/2026 07:13:15 GMT) — **tự đo 2 lần** (đầu phiên 15:06 và cuối phiên 15:36), không chép từ case khác |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback Rule 7 |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW, đơn vị BTP `…0001`) — đúng vai trò đối tác dùng ở **cả hai** ảnh |
| **Tiêu chí** | [`tieuchi/DGHQHTPL_06.md`](tieuchi/DGHQHTPL_06.md) — viết xong **trước** khi mở màn Báo cáo thống kê |

> 🔴 **Cảnh báo trôi bản dựng — đọc trước khi so số với các Phần trên.** Môi trường được **dựng lại lúc
> 07:13 GMT (14:13 giờ máy)**, tức **sau khi** các Phần 2–7 đo xong. Các Phần đó đo trên bó mã
> `assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`); Phần 8 và Phần 9 đo trên
> `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`). **Nhãn trong ứng dụng vẫn là `V1.0.8`
> ở cả hai lần dựng** ⇒ **không được dùng nhãn để nhận biết bản dựng**. Riêng trong phiên đo Phần 9, bó mã
> được đo **2 lần cách nhau 30 phút và giống hệt nhau** ⇒ **không trôi thêm** trong lúc đo; kết luận dưới đây
> chỉ có hiệu lực cho đúng bó mã `md5 3904131c…`.

> **Quan hệ với Phần 2 · 3 · 4 · 5 · 6 · 7 · 8:** cùng một chức năng xuất báo cáo
> (`POST /api/v1/bao-cao/export`), khác loại báo cáo. Dòng 214 vẫn được đo **riêng** trên đúng màn của nó —
> **BC Đánh giá hiệu quả HTPL** (FR-IX-09 / UC132, `srs-fr-11-bao-cao.md:474`). Màn này khác hẳn màn
> *BC Số lượng CG/TVV* của Phần 8 ở: đường dẫn dữ liệu (`danh-gia-hieu-qua`), bản chất báo cáo (**điểm trung
> bình có trọng số theo kỳ**, `:495`, không phải snapshot đếm người), bộ chỉ số đầu ra (`diem_trung_binh` /
> `so_vu_viec_danh_gia` / `theo_don_vi[]` / `theo_tieu_chi[]` / `theo_dot[]`) và **chỉ có 1 bộ lọc đặc thù** —
> *Đợt đánh giá* (`:493`, `:1072`). Không suy kết quả từ case anh em.

## Bug Summary Table (Phần 9)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-DGHQHTPL-006 | Major | P1 | Permission | `DGHQHTPL_06` (tab `bug` dòng 214) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` · `:1053` | [`image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Open |

---

## BUG-DGHQHTPL-006 — Vai trò QTHT xem được BC Đánh giá hiệu quả HTPL nhưng bị chặn khi Xuất Excel/PDF, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 15:39 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bó mã `index-DIABnbIr.js`.
> Vế đối tác nêu ở vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được **8/8 lượt** (4 dạng bộ lọc + 1 lượt lặp chống đè + 1 PDF + 2 lượt gọi thẳng máy chủ),
> tệp mở đọc được, đủ 4 mục đầu tệp, số khớp màn từng con số và cộng dọc khớp tổng. Vế tên tệp cũng **đạt**
> (`BaoCaoDanhGiaHieuQua_20260806_1514.xlsx` — đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}`, hai lượt cùng ngày ra
> hai tên khác nhau). Vế vòng 2 (*"Forbidden"*, TKM retest 31/07) **tái hiện nguyên vẹn 13/13 lượt** ở đúng
> vai trò đối tác đã dùng, **cả nhánh Excel lẫn nhánh PDF** · **không seed, không tạo/sửa/xoá bản ghi nào** —
> toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Đánh giá hiệu quả HTPL**, người dùng vai trò **Quản trị hệ
thống (QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng đợt đánh giá 4 · Tổng lượt
đánh giá 8 · Tổng số vụ việc đã đánh giá 7 · Điểm trung bình chung 33, kèm bảng theo đơn vị, bảng theo tiêu
chí và hai biểu đồ) và **hiện hai nút [Xuất Excel] / [Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp
[Xuất Excel] thì bị từ chối và **không nhận được tệp nào**. Chữ hiện ra cho người dùng là **"Forbidden"** —
chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy chủ, không cho người dùng biết chuyện gì đã xảy ra
và phải làm gì tiếp. Nhánh [Xuất PDF] cũng vậy: hộp thoại *Tùy chọn in báo cáo PDF* mở bình thường, bấm
[Xuất file] mới hiện đúng chuỗi đó. Cùng thao tác, cùng bộ lọc, **cùng đơn vị**, vai trò Cán bộ Nghiệp vụ
Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`; `/api/v1/auth/me` và vé đăng nhập đều ghi
   `vaiTro = ["QTHT"]`, `capDonVi = "TW"`, `donViId = 00000000-0000-4000-8000-000000000001` = *Cục Bổ trợ tư
   pháp - Bộ Tư pháp*) — đúng vai trò và đơn vị đọc được ở góc phải trên **cả hai** bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Đánh giá hiệu quả HTPL** (đường dẫn phải chứa `loai=danh-gia-hieu-qua` —
   **không** nhầm sang *BC Số lượng CG/TVV*, cũng **không** nhầm sang màn nghiệp vụ *Đánh giá hiệu quả* ở
   thanh bên); *Kỳ báo cáo* = **Năm** (01/01/2026 → 31/12/2026); *Đơn vị* = **Toàn quốc**; để trống bộ lọc
   *Đợt đánh giá* — đúng cấu hình trên ảnh vòng 2 của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (4 · 8 · 7 · 33 + bảng theo đơn vị + bảng theo tiêu
   chí + biểu đồ), không có cảnh báo nào; hai nút Xuất bật lên.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Bấm **[Xuất PDF]** → trong hộp thoại *Tùy chọn in báo cáo PDF* bấm **[Xuất file]** — quan sát tương tự.
7. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi
  kỹ thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` và `:1053` ghi điều kiện hiển thị của nút Xuất Excel / Xuất PDF chỉ là *"Sau
  khi đã 'Xem báo cáo'"*, **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ
  chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 15:31–15:35:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/danh-gia-hieu-qua?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **4 đợt · 8 lượt · 7 vụ việc · điểm TB 33** (*Thời điểm tạo 06/08/2026 15:31*) —
  **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; mỗi cú bấm đúng **1** lời gọi và **1** khung thông
  báo (không có hiện tượng 2 thông báo chồng); chữ người dùng đọc được đổi **tại chỗ trong khung cũ**:
  *"Đang tạo file..."* → **"Forbidden"**. Khung nằm trong vùng nhìn thấy (`w=1432 · h=56`) và **sống ~3,3 s**
  (mẫu chữ theo thời gian: xuất hiện ở mốc 2 618 ms, biến mất ở mốc 5 918 ms). Bấm chuột thật **8 lượt** —
  lượt nào cũng ra đúng chữ đó; **0 tệp** được giao.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_DANH_GIA_HIEU_QUA","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T08:32:44.008Z","requestId":"8c55457f-5e95-4fc7-8f9e-be7d5d91b029"}}
  ```
  Header trả về **không có** `content-disposition` ⇒ không có tệp đính kèm. Chữ trên màn **trùng khít**
  `error.message` của máy chủ ⇒ giao diện đẩy nguyên chuỗi kỹ thuật ra cho người dùng cuối.
- [Xuất PDF]: hộp thoại *Tùy chọn in báo cáo PDF* mở bình thường (A4 · Dọc mặc định); bấm [Xuất file] →
  **403** với thân gửi lên `…"formatXuat":"PDF","khoGiay":"A4","huongGiay":"portrait"`, phản hồi cùng mã
  `ERR-PERM-SYS-00-01` / `"Forbidden"` (3 lượt). ⇒ **không phải khuyết tật riêng của nhánh Excel**.
- Đo lại bằng **đường thứ hai** (gọi thẳng máy chủ, cùng phiên QTHT, cùng thân yêu cầu): `formatXuat` =
  **XLSX** → **403**, `formatXuat` = **PDF** → **403**, thân phản hồi cùng mã `ERR-PERM-SYS-00-01`.
  ⇒ Cộng lại **13/13 lượt** (11 bấm chuột + 2 gọi thẳng) đều bị chặn — **không phải chập chờn**, và **không**
  phải lỗi thao tác trên giao diện.
- **Quét thư mục tải xuống** với mốc *"mới hơn 15:29"*: **không có** tệp `.xlsx`/`.pdf` nào ⇒ qua 13 lượt
  thử, người dùng vai trò này ra về tay trắng.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, 4 dạng bộ lọc + 1 lượt lặp + 1 lượt PDF:**

| Lượt | Bộ lọc / định dạng | Màn trước khi bấm (đợt/lượt/VV/điểm TB) | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc · **Đợt đánh giá trống** (đúng cấu hình vòng 2 của đối tác) | 4 / 8 / 7 / 33 | 15:14 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoDanhGiaHieuQua_20260806_1514.xlsx` — 7 358 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Lọc *Đợt đánh giá = Đợt đánh giá seed 2026* (**đúng kiểu cấu hình vòng 1 của đối tác**) | 1 / 3 / 3 / 76 | 15:17 | **200** | `BaoCaoDanhGiaHieuQua_20260806_1517.xlsx` — 7 018 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Lọc *Đợt đánh giá = QA-THDG05-partial-save-te…* | 1 / 3 / 3 / 8 | 15:21 | **200** | `BaoCaoDanhGiaHieuQua_20260806_1521.xlsx` — 7 128 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 4 | Thu hẹp *Đơn vị = Sở Tư pháp Hà Nội (STP-HN)*, đợt trống | 2 / 3 / 2 / 25 | 15:23 | **200** | `BaoCaoDanhGiaHieuQua_20260806_1523.xlsx` — 7 166 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 5 | Lặp lại y hệt lượt 4 (phép thử chống đè tệp) | 2 / 3 / 2 / 25 | 15:25 | **200** | `BaoCaoDanhGiaHieuQua_20260806_1525.xlsx` — 7 167 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 6 | **Xuất PDF** (qua hộp thoại *Tùy chọn in báo cáo PDF*) | 2 / 3 / 2 / 25 | 15:24 | **200**, `%PDF` | `BaoCaoDanhGiaHieuQua_20260806_1524.pdf` — 34 996 B | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* (`ERR-RPT-04`, `:116`) ở bất kỳ lượt
  nào, cũng **không** có *"Forbidden"* ⇒ vế vòng 1 của đối tác hết lỗi. Mỗi lượt đúng **1** lời gọi xuất,
  **1** khung thông báo (đếm theo mốc giờ khác nhau, bộ theo dõi không lọc trùng, tự kiểm 1 observer).
- **Tên tệp** — đo từ **hai đường độc lập và trùng khít**: header `content-disposition` của máy chủ
  (`attachment; filename="BaoCaoDanhGiaHieuQua_20260806_1539.xlsx"`), và **tệp rơi thật về thư mục tải xuống**
  (đúng thứ người dùng thật nhìn thấy); md5 hai nguồn **trùng nhau từng lượt** (vd dạng 1 cùng
  `12cddfb63d6cb252ec522eeafc88eaed`). Khớp khuôn đặc tả `:85` + `srs-v3.5.md:6716` (Phụ lục E §H8) —
  `{TenTep}_{YYYYMMDD_HHmm}.{đuôi}`, PascalCase, không dấu, không gạch nối, **có đủ giờ-phút** và giờ-phút
  **khớp thời điểm xuất thật**. Hai lượt xuất **cùng ngày, cùng bộ lọc** (15:23 / 15:25) ra **hai tên khác
  nhau** ⇒ không đè tệp nhau, đúng chủ đích BA chốt 2026-08-04 khi bắt buộc phần giờ-phút. Phần
  `{TenBaoCao}` là `BaoCaoDanhGiaHieuQua` — **đúng loại báo cáo này**.
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): sheet *"BC Đánh giá hiệu quả"*, đủ 4 mục đầu tệp `:1092`
  đòi — *BC Đánh giá hiệu quả HTPL* · *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · *Đơn vị: Toàn quốc*
  (dạng 4 đổi đúng thành *Đơn vị: Sở Tư pháp Hà Nội*) · *Ngày tạo: 06/08/2026*. Số trong tệp khớp **từng con
  số** với màn của chính lượt đó, bảng *Theo đơn vị* cộng dọc bằng đúng thẻ tổng — số lượt 1+4+3 = 8 · số vụ
  việc 1+4+2 = 7 (Bộ Kế hoạch và Đầu tư · Cục Bổ trợ tư pháp - Bộ Tư pháp · Sở Tư pháp Hà Nội), và điểm trung
  bình chung 33,9 nằm trong khoảng [25,53 ; 80] của các điểm thành phần — đúng tính chất *trung bình có trọng
  số* ở `:495`.
- **Bộ lọc *Đợt đánh giá* chạy đúng** — AC `:511` (*"chọn đợt cụ thể → hiển thị chi tiết đợt đánh giá đó"*)
  thoả: lượt 2 và lượt 3 cùng chiều lọc cho **hai kết quả khác hẳn** (76,67 điểm / 3 đơn vị ↔ 8,2 điểm /
  1 đơn vị). Giao diện gửi khoá `dotDanhGiaId` — **đúng khoá máy chủ nhận** — ở cả lượt Xem lẫn trong
  `filterDacThu` của lượt Xuất; đã loại trừ nhớ đệm bằng `ngayTaoBc` (bảng đo ở
  [`image/DGHQHTPL_06-09-…txt`](image/DGHQHTPL_06-09-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt) §PHẦN 5).
  ⇒ Màn này **không** dính khuyết tật lệch tên khoá bộ lọc như các màn khác.
- **Tệp bám đúng bộ lọc hiện tại** (`:1280`): 4 dạng cho 4 tệp có md5 và nội dung khác nhau (7 358 / 7 018 /
  7 128 / 7 166 B), không có cặp nào *"màn khác số mà tệp giống hệt"*.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế tên tệp đạt. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên
vẹn** đúng vai trò, đúng màn, đúng cấu hình bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · BTP · TW*), đúng cấu hình bộ lọc vòng 2 của đối
  tác, khung thông báo **đỏ chữ "Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 4 · 8 · 7 · 33.
  *Ghi chú cách chụp:* khung chỉ sống ~3,3 giây và thư viện giao diện **thay chữ ngay trong khung cũ**, nên
  phải **hẹn giờ bấm trước rồi mới gọi chụp**; mọi lượt bấm đều là lời gọi xuất trả 403, **không** đổi dữ liệu.
- 🔴 [`image/DGHQHTPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/DGHQHTPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png)
  — cùng vai trò QTHT nhưng đi **nhánh [Xuất PDF]**: hộp thoại tuỳ chọn in mở bình thường, bấm [Xuất file]
  cũng ra đúng chuỗi **"Forbidden"** ⇒ khuyết tật nằm ở đường xuất chung, không riêng nhánh Excel.
- [`image/DGHQHTPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png`](image/DGHQHTPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ 4 · 8 · 7 · 33 và **hai
  nút Xuất đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/DGHQHTPL_06-01-dang1-khong-loc-dot-man-hinh-truoc-khi-xuat-V108.png`](image/DGHQHTPL_06-01-dang1-khong-loc-dot-man-hinh-truoc-khi-xuat-V108.png)
  — phiên CB Nghiệp vụ TW, dạng 1 (đúng cấu hình vòng 2 của đối tác), màn hình **trước** khi bấm Xuất:
  *Thời điểm tạo 15:13*, 4 · 8 · 7 · 33 — mốc đối chiếu số liệu với nội dung tệp.
- [`image/DGHQHTPL_06-02-dang2-loc-DotDanhGia-seed2026-man-hinh-truoc-khi-xuat-V108.png`](image/DGHQHTPL_06-02-dang2-loc-DotDanhGia-seed2026-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 2 (lọc *Đợt đánh giá = Đợt đánh giá seed 2026*), số đổi thành 1 · 3 · 3 · 76 — dùng chứng minh tệp
  xuất bám đúng bộ lọc. *(Env không có đợt tên "TKM kiểm thử 2" mà đối tác dùng ở vòng 1 nên đã đổi sang đợt
  này; đã khai trong tiêu chí mục 6.)*
- [`image/DGHQHTPL_06-03-dang3-loc-DotDanhGia-THDG05-so-lieu-doi-V108.png`](image/DGHQHTPL_06-03-dang3-loc-DotDanhGia-THDG05-so-lieu-doi-V108.png)
  — dạng 3 (đợt thứ hai), 1 · 3 · 3 · **8** — khác hẳn dạng 2 ⇒ máy chủ không trả cùng một tập, AC `:511` thoả.
- [`image/DGHQHTPL_06-04-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png`](image/DGHQHTPL_06-04-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 4 (thu hẹp *Đơn vị = Sở Tư pháp Hà Nội*), 2 · 3 · 2 · 25; mục *Đơn vị* trong tệp xuất đổi theo.
- [`image/DGHQHTPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png`](image/DGHQHTPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *"Tùy chọn in báo cáo PDF"* mà [Xuất PDF] mở ra; giữ lại vì đây là bước dễ hiểu nhầm thành
  *"bấm Xuất PDF không có phản ứng gì"*.
- [`image/DGHQHTPL_06-09-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/DGHQHTPL_06-09-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · thời gian sống), nguyên văn phản hồi máy chủ
  của cả hai vai trò (kể cả thân 403), vai trò đọc từ vé đăng nhập, tên tệp đo từ cả hai đường, nội dung ô
  của 5 tệp .xlsx đọc bằng `openpyxl`, md5 từng tệp, phép thử chống đè tệp và **bảng đo bộ lọc 5 dòng**.
- Tệp thật hệ thống giao ra (tên gốc hệ thống đặt được giữ nguyên phía sau tiền tố mã case):
  [`testfiles/DGHQHTPL_06-dang1-khong-loc-BaoCaoDanhGiaHieuQua_20260806_1514.xlsx`](testfiles/DGHQHTPL_06-dang1-khong-loc-BaoCaoDanhGiaHieuQua_20260806_1514.xlsx)
  · [`testfiles/DGHQHTPL_06-dang2-loc-dot-seed2026-BaoCaoDanhGiaHieuQua_20260806_1517.xlsx`](testfiles/DGHQHTPL_06-dang2-loc-dot-seed2026-BaoCaoDanhGiaHieuQua_20260806_1517.xlsx)
  · [`testfiles/DGHQHTPL_06-dang3-loc-dot-THDG05-BaoCaoDanhGiaHieuQua_20260806_1521.xlsx`](testfiles/DGHQHTPL_06-dang3-loc-dot-THDG05-BaoCaoDanhGiaHieuQua_20260806_1521.xlsx)
  · [`testfiles/DGHQHTPL_06-dang4-donvi-STPHN-BaoCaoDanhGiaHieuQua_20260806_1523.xlsx`](testfiles/DGHQHTPL_06-dang4-donvi-STPHN-BaoCaoDanhGiaHieuQua_20260806_1523.xlsx)
  · [`testfiles/DGHQHTPL_06-dang4-lap-lai-BaoCaoDanhGiaHieuQua_20260806_1525.xlsx`](testfiles/DGHQHTPL_06-dang4-lap-lai-BaoCaoDanhGiaHieuQua_20260806_1525.xlsx)
  · [`testfiles/DGHQHTPL_06-pdf-dang4-BaoCaoDanhGiaHieuQua_20260806_1524.pdf`](testfiles/DGHQHTPL_06-pdf-dang4-BaoCaoDanhGiaHieuQua_20260806_1524.pdf)

### So sánh vai trò

Phép đối chứng đổi **đúng một biến** — cùng đường dẫn, cùng thân yêu cầu **từng chữ**, cùng
`donViId …0001`, cùng phiên đo, chỉ khác vai trò:

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Header trả về | Chữ hiện cho người dùng |
|---|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:485`) | 200, ra đủ 4 · 8 · 7 · 33 | **200**, nhận được tệp .xlsx/.pdf mở đọc được | `content-disposition: attachment; filename="BaoCaoDanhGiaHieuQua_20260806_1539.xlsx"` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW, **cùng đơn vị BTP** (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *(không có `content-disposition`)* | *"Forbidden"* |

⇒ Đường xuất tệp **không hỏng**; đúng vai trò thì chạy. Chỉ vai trò QTHT bị chặn, và bị chặn **sau khi** đã
được cho xem đủ số liệu.

### Ghi chú liên quan

- **Cả hai bằng chứng của đối tác đều đúng case này** — kiểm bằng 3 chỗ: chuỗi `danh-gia-hieu-qua` trong
  đường dẫn · chữ trong ô chọn *Loại báo cáo* · tiêu đề khối kết quả *BC Đánh giá hiệu quả HTPL*. **Không**
  nhầm với *BC Số lượng CG/TVV* (FR-IX-08, dòng 210) và **không** nhầm với màn nghiệp vụ *Đánh giá hiệu quả*
  ở thanh bên. Tuy vậy **hai vòng không so trực tiếp được với nhau**: cùng vai trò, cùng loại báo cáo, cùng
  kỳ và cùng đơn vị, nhưng khác bản dựng (V1.0 → V1.0.3), khác bộ lọc *Đợt đánh giá* (có chọn → trống) và
  khác cả số thẻ hiện trên màn (3 thẻ → 4 thẻ) ⇒ đã đo **cả hai cấu hình**, không chỉ cấu hình vòng 2.
- **Hai đường đo độc lập cùng kết luận, không mâu thuẫn:** đường giao diện (thao tác chuột thật, đọc chữ
  hiện trên màn) và đường máy chủ (mã HTTP + thân phản hồi) khớp nhau ở cả hai vai trò ⇒ không có điểm nào
  cần hỏi thêm trước khi kết luận.
- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của
  case: nếu BA chốt QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt `:117` thay vì
  `Forbidden`, và phải chặn ngay từ bước Xem cho nhất quán (`:79`); nếu BA chốt QTHT *được* xuất thì đang
  chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoDanhGia_{YYYYMMDD_HHmm}`, hệ thống ra
  `BaoCaoDanhGiaHieuQua_20260806_1514.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85`, `:86` +
  `srs-v3.5.md:6716` Phụ lục E §H8) với `{TenBaoCao}` là **tên loại báo cáo**, **không** ấn định đúng chuỗi
  `BaoCaoDanhGia`. Tên hệ thống dùng khớp khuôn, có đủ giờ-phút, mang đúng tên loại báo cáo này (chỉ dài hơn
  chuỗi đối tác viết), hai lượt cùng ngày không đè nhau ⇒ **không** phải khuyết tật.
  *(So với số đo cũ 03/08 — `bao-cao-<slug>-2026-08-03.xlsx`, thiếu giờ-phút, có gạch nối — khuôn tên đã được
  sửa đúng ở bản dựng đang đo.)*
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006` /
  `BUG-CPCTHTTDVQL-006` / `BUG-CPCTHTTLHDN-006` / `BUG-CPCTHTTTG-005` / `BUG-CPCTHTTTG-006` (Phần 4),
  `BUG-CTTDVQL-004` (Phần 5), `BUG-CLDTBDDDR-006` (Phần 6), `BUG-LDTBDDDR-006` (Phần 7),
  `BUG-CGTVPL-006` (Phần 8) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng mã `ERR-PERM-SYS-00-01`,
  khác loại báo cáo. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng sau vẫn phải verify riêng từng case trên
  đúng màn của nó. **Không mở dòng bug mới trên bảng theo dõi** cho case này.

#### Ghi nhận ngoài vế đối tác nêu — **không** kéo verdict case, chưa mở dòng trên bảng

Hai điểm dưới đây phát hiện trong lúc đo nhưng đối tác **không** nêu ở case này (cả hai ảnh chỉ nêu thông báo
khi bấm xuất). Ghi lại đầy đủ để phiên chính quyết có mở dòng riêng hay không; QA không tự mở.

- **D2 — Thiếu hẳn nhóm kết quả *theo đợt đánh giá* (`theo_dot[]`, điều kiện hiển thị *"Luôn"*,
  `srs-fr-11-bao-cao.md:507`).** Phản hồi của màn này trả về đúng các khoá
  `tenBaoCao · ngayTaoBc · tuNgay · denNgay · tongDotDanhGia · tongLuotDanhGia · soVuViecDanhGia ·
  diemTrungBinhChung · theoDonVi · theoTieuChi · chartTypes` — **không có** phần theo đợt; tệp xuất cũng chỉ
  có bảng *Theo đơn vị* và *Theo tiêu chí*, **không có** bảng *Theo đợt*. Đây là nhóm đầu ra đặc tả ghi điều
  kiện *"Luôn"*, tức phải có ở mọi lượt chạy báo cáo. **Không ảnh hưởng phép đo nào của case:** cả 8 lượt
  xuất của vai trò CB Nghiệp vụ đều thực hiện trên báo cáo vừa render xong với nút ở trạng thái bấm được, và
  verdict REOPEN đứng vững chỉ bằng vế *"Forbidden"*.
- **D3 — Thẻ *"Điểm trung bình chung"* trên màn cắt cụt phần thập phân.** Máy chủ và tệp xuất trả 33,9 nhưng
  thẻ hiện `33`; tương tự 76,67 → `76`, 8,2 → `8`, 25,53 → `25`. Bảng *Theo đơn vị* trên màn lại làm tròn 1
  chữ số (80,0 · 28,7 · 25,5) trong khi tệp giữ đủ (80 · 28,65 · 25,53) ⇒ **ba cách hiển thị khác nhau cho
  cùng một con số**. Đặc tả **không** nêu công thức làm tròn nên tiêu chí đã ghi trước là **không chấm Fail**;
  ghi lại vì người dùng đọc thẻ 33 rồi mở tệp thấy 33,9 sẽ tưởng số liệu lệch.

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần >=1 đợt đánh giá ĐÃ CÓ LƯỢT CHẤM trong kỳ để báo cáo có dữ liệu; nếu báo
  cáo trống thì nút Xuất sẽ không bật và phép thử không có giá trị.

Các bước:
  1. Đăng nhập admin (QTHT). Vào Báo cáo thống kê. TẢI LẠI TRANG và ghi lại bản dựng trước
     khi đo - ghi bằng TÊN BÓ MÃ assets/index-*.js, ĐỪNG ghi bằng nhãn V1.0.x: hai lần dựng
     khác nhau ngày 06/08 đều mang nhãn V1.0.8.
  2. Loại báo cáo = BC Đánh giá hiệu quả HTPL (kiểm cả 3 chỗ: chuỗi trong đường dẫn phải là
     danh-gia-hieu-qua, chữ trong ô chọn, tiêu đề khối kết quả - DỄ nhầm sang BC Số lượng
     CG/TVV và sang màn nghiệp vụ "Đánh giá hiệu quả" ở thanh bên); Kỳ = Năm 01/01/2026 -
     31/12/2026; Đơn vị = Toàn quốc; để trống bộ lọc Đợt đánh giá. Bấm [Xem báo cáo], chờ ra
     số liệu.
  3. Cài bộ theo dõi thông báo TRƯỚC khi bấm (không lọc trùng, đọc innerText, lấy mẫu chữ
     theo thời gian - xem tools/toast-capture.js), rồi bấm [Xuất Excel].
  4. Ghi lại: chữ hiện cho người dùng · mã trả về của POST /api/v1/bao-cao/export · số tệp
     nhận được.
  5. Làm lại bước 3-4 cho nhánh [Xuất PDF]: nút này mở hộp thoại "Tùy chọn in báo cáo PDF",
     phải bấm tiếp [Xuất file] mới gọi máy chủ.
  6. Lặp lại bước 2-5 bằng tài khoản cbnv_tw_05 (CB Nghiệp vụ TW) để đối chiếu, và MỞ TỆP
     xuất ra đọc: phải còn đủ 4 mục đầu tệp (tên BC, kỳ, đơn vị, ngày tạo), còn đủ các chỉ số
     Tổng đợt - Tổng lượt - Số vụ việc được đánh giá - Điểm trung bình chung, bảng theo đơn vị
     và bảng theo tiêu chí; số khớp màn, cộng dọc cột số lượt và số vụ việc khớp thẻ tổng.
  7. Đo thêm 2 đợt đánh giá KHÁC NHAU: tệp xuất phải đổi theo đợt được chọn (đây là bộ lọc
     đặc thù duy nhất của màn này).

PASS khi:
  - Vai trò QTHT: KHÔNG còn thấy chuỗi "Forbidden" trên màn, ở CẢ nhánh Excel lẫn nhánh PDF.
    Nếu hệ thống vẫn từ chối thì câu hiện ra phải là câu tiếng Việt cho biết người dùng không
    có quyền (yêu cầu :117); nếu BA chốt QTHT được xuất thì phải nhận được tệp mở đọc được.
  - Bước Xem và bước Xuất nhất quán: không còn cảnh cho xem đủ số liệu rồi chặn ở bước xuất.
    Nếu vai trò bị cấm thì phải chặn ngay từ bước Xem (yêu cầu :79).
  - Vai trò cbnv_tw_05 vẫn xuất được cả Excel lẫn PDF ở cả 4 dạng lọc, tên tệp vẫn đúng khuôn
    có giờ-phút và mang đúng tên loại báo cáo "đánh giá hiệu quả", nội dung tệp vẫn đúng như
    mô tả ở bước 6 (không hồi quy).

FAIL nếu:
  - Còn bất kỳ chỗ nào hiện chuỗi kỹ thuật tiếng Anh (Forbidden / Unauthorized / Internal
    Server Error) cho người dùng cuối.
  - Sửa bằng cách ẩn/làm mờ nút Xuất mà bước Xem vẫn cho vào: người dùng vẫn không biết vì
    sao mình không xuất được -> chưa đạt :117.
  - Chỉ sửa nhánh Excel mà quên nhánh PDF (hoặc ngược lại).
  - Vai trò CB Nghiệp vụ bị chặn theo, hoặc tệp xuất mất mục đầu tệp / mất bảng theo đơn vị /
    mất bảng theo tiêu chí / mất phần giờ-phút trong tên tệp / tên tệp mang tên loại báo cáo
    khác (hồi quy).

Bẫy hay gặp:
  - Khung thông báo chỉ sống ~3,3 giây và thư viện giao diện CẬP NHẬT CHỮ NGAY TRONG khung cũ
    chứ không mọc khung mới. Nếu chỉ ghi "khung nào mới mọc" sẽ chỉ thấy "Đang tạo file..."
    và kết luận nhầm là hệ thống im lặng. Phải lấy mẫu chữ theo thời gian; muốn chụp được thì
    hẹn giờ bấm trước rồi mới gọi chụp.
  - Đo bằng vai trò CB Nghiệp vụ rồi kết luận "hết lỗi" là sai. Phải đo bằng đúng vai trò
    QTHT như trên bằng chứng của đối tác.
  - Rất dễ mở nhầm màn: "BC Số lượng CG/TVV" có bộ lọc Loại TVV + Lĩnh vực chuyên môn và 3 thẻ
    đếm người; còn màn nghiệp vụ "Đánh giá hiệu quả" ở thanh bên là danh sách kế hoạch/đợt,
    không có nút Xuất của báo cáo thống kê. Kiểm đủ 3 chỗ như bước 2.
  - [Xuất PDF] KHÔNG tải tệp ngay: nó mở hộp thoại "Tùy chọn in báo cáo PDF", phải bấm tiếp
    [Xuất file]. Bỏ qua bước này rất dễ báo oan "bấm không có phản ứng"; hộp thoại còn mở cũng
    nuốt luôn cú bấm [Xuất Excel] ngay sau đó.
  - Tab trình duyệt mở lâu vẫn chạy mã cũ: phải tải lại trang; và ghi bản dựng bằng tên bó mã
    assets/index-*.js chứ đừng tin nhãn V1.0.x.
  - Số trên màn có thể là số máy chủ đã nhớ sẵn: xem trường "Thời điểm tạo" có nhảy theo lượt
    bấm không, nếu đứng yên thì đổi ngày kết thúc 1 ngày để lấy số mới.
  - Thẻ "Điểm trung bình chung" đang cắt phần thập phân (ghi nhận D3): thẻ hiện 33 trong khi
    tệp và máy chủ là 33,9. Đừng vội kết luận "tệp lệch màn" - so bằng con số máy chủ trả về.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy
nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở
[`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2 trước khi dev chọn hướng sửa. Ghi nhận D2 · D3 ở trên chuyển **phiên
chính** quyết, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 9)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — nhãn HTPLDN **V1.0.8**, bó mã giao diện `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, etag `W/"6a74340b-1124ed"`, `last-modified` Thu, 06 Aug 2026 07:13:15 GMT) — **tự đo 2 lần, lúc 15:06 và 15:36, giống hệt nhau**. ⚠️ Bản dựng này **mới hơn** bản các Phần 2–7 đo (`index-CNwX9JjX.js`) dù **nhãn không đổi** |
| **Màn đo** | Báo cáo thống kê → **BC Đánh giá hiệu quả HTPL** (`/bao-cao?loai=danh-gia-hieu-qua`), FR-IX-09 / UC132 (`srs-fr-11-bao-cao.md:474`) |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng `isolatedContext="qa-dghqhtpl06-cbnv"` (CB Nghiệp vụ) và `"qa-dghqhtpl06-qtht"` (QTHT) — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước** mỗi phép đo quyết định; QTHT trả `vaiTro ["QTHT"] · capDonVi "TW" · donViId 0000…0001`; CB Nghiệp vụ trả `vaiTro ["CB_NV_TW"] · capDonVi "TW" · donViId 0000…0001` — **cùng đơn vị**, chỉ khác vai trò |
| **Khung giờ đo** | 2026-08-06 15:06 → 15:39 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 4 đợt đánh giá có lượt chấm trong kỳ Năm 2026 (8 lượt · 7 vụ việc), trải 3 đơn vị (Bộ Kế hoạch và Đầu tư · Cục Bổ trợ tư pháp - Bộ Tư pháp · Sở Tư pháp Hà Nội), đủ cho cả 4 dạng biến thể. Env **không có** đợt tên *TKM kiểm thử 2* mà đối tác dùng ở vòng 1 ⇒ đã thay bằng *Đợt đánh giá seed 2026* và khai rõ trong tiêu chí |

*Phần 9 generated: 2026-08-06 15:45:00 | QA Automation via Claude Code*

---

# Phụ lục — 5 dòng phiếu ngoài phạm vi mở từ lô B3 (BC chi phí hỗ trợ)

Năm phát hiện dưới đây gặp trong lúc verify 5 case lô B3 nhưng **không thuộc phạm vi phiếu nào của
đối tác**, nên theo flow phải mở dòng riêng trên tab `bug` thay vì nhét vào ô *Kết quả verify*.
Không phát hiện nào trong số này làm đổi verdict của 5 case (cả 5 case đều Reopen vì lý do riêng).

**Quy tắc mã:** nối tiếp dãy `BCTK_QA01..04` đã có sẵn trên tab (dòng 363–367). Cả 5 phát hiện đều
thuộc màn **Báo cáo thống kê** nên tiền tố module là `BCTK`, không dùng tiền tố của từng loại báo cáo.

| Dòng | Mã TC | Màn / thành phần | Nội dung | Gặp khi verify | Biên bản đo |
|---|---|---|---|---|---|
| 368 | `BCTK_QA05` | BC Chi phí theo loại hình DN | Xếp sai quy mô doanh nghiệp — hồ sơ quy mô *Nhỏ* bị gộp vào dòng *Siêu nhỏ*; lọc "Loại DN = Nhỏ" ra rỗng dù kỳ có hồ sơ Nhỏ | CPCTHTTLHDN_06 | [`OOS-01`](image/OOS-01-bao-cao-loai-hinh-DN-phan-sai-quy-mo.txt) |
| 369 | `BCTK_QA06` | BC Chi phí chi trả hỗ trợ | Thiếu hẳn phần chia theo kỳ (`theo_ky[]`, điều kiện *Luôn*, `srs-fr-11-bao-cao.md:718-724`) ở cả dữ liệu máy chủ, màn hình và tệp xuất | CPHTCT_06 | [`OOS-02`](image/OOS-02-thieu-phan-chia-theo-ky-o-BC-chi-phi-chi-tra.txt) |
| 370 | `BCTK_QA07` | Nút Xuất Excel / Xuất PDF (dùng chung cả màn) | Nhấn [Xem báo cáo] lần thứ hai là hai nút Xuất bị khoá và không mở lại được trong cùng phiên, dù báo cáo vẫn hiện đủ số liệu | CPCTHTTTG_05 · CPCTHTTTG_06 | [`OOS-03`](image/OOS-03-nut-xuat-bi-khoa-sau-lan-xem-thu-hai.txt) |
| 371 | `BCTK_QA08` | BC Chi phí theo thời gian | Giao diện không có đường nào cho ra nhiều điểm kỳ → biểu đồ đường luôn 1 điểm, tiêu chí nghiệm thu `:874` (12 tháng → 12 điểm) không thực hiện được; máy chủ thì trả đúng 12 điểm | CPCTHTTTG_05 | [`OOS-04`](image/OOS-04-khong-dung-duoc-nhieu-diem-ky-tren-giao-dien.txt) |
| 372 | `BCTK_QA09` | Tệp xuất Excel / PDF | Kỳ "Khoảng tùy chọn" in ra mã kỹ thuật `KHOANG` ở dòng *Kỳ báo cáo* trong tệp (màn hình thì hiện đúng "Khoảng"); dính cả bản PDF văn bản hành chính | CPCTHTTTG_05 · CPCTHTTTG_06 | [`OOS-05`](image/OOS-05-tep-xuat-in-ma-ky-thuat-KHOANG.txt) |

**Đã ghi lên bảng:** `Tuần` = Tuần 3 · `Trạng thái` = Fail · `Dopai` = bug · `Ảnh/vieo 1` = link Drive
xem được (mỗi dòng 2 tệp: biên bản đo + tệp/ảnh bằng chứng), gắn siêu liên kết bấm được.
Không đụng vào ô nào của các dòng đã có.

> **Lưu ý tên tệp:** ảnh bằng chứng của `BCTK_QA07` mang tên
> `CPCTHTTTG_QA01-bam-xem-bao-cao-lan-2-nut-xuat-bi-khoa-V108.png` — đặt theo mã dự kiến ban đầu,
> trước khi chốt dãy mã `BCTK_QA*` theo tiền lệ trên tab. Giữ nguyên tên tệp để không phá link Drive
> đã gắn; nhãn hiển thị trong ô bảng mô tả đúng nội dung ảnh.

*Phụ lục generated: 2026-08-06 | QA Automation via Claude Code*

---

# Phần 10 — Batch B5 (BC Chất lượng đào tạo)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN — Phần mềm Hỗ trợ Pháp lý Doanh nghiệp |
| **Đợt** | Verify bug dev fix — bảng theo dõi của đối tác, tab `bug` dòng 218 |
| **Ngày** | 2026-08-06 16:25:00 |
| **Môi trường** | https://18.143.165.120.nip.io — nhãn ứng dụng **V1.0.8**, bó mã `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, `last-modified` 06/08/2026 07:13:15 GMT) — **tự đo 2 lần** (đầu phiên 16:01 và cuối phiên 16:19), không chép từ case khác |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — **không** dùng fallback Rule 7 |
| **Tài khoản đối chứng** | `admin` (Quản trị hệ thống, `QTHT`, cấp TW, đơn vị BTP `…0001`) — đúng vai trò đối tác dùng ở **cả hai** ảnh |
| **Tiêu chí** | [`tieuchi/CLDTBDPL_06.md`](tieuchi/CLDTBDPL_06.md) — viết xong **trước** khi mở màn Báo cáo thống kê (15:58), mục 4 và mục 5 **không sửa một chữ nào** sau khi mở màn |

> 🔴 **Cảnh báo trôi bản dựng — đọc trước khi so số với các Phần trên.** Môi trường được **dựng lại lúc
> 07:13 GMT (14:13 giờ máy)**, tức **sau khi** các Phần 2–7 đo xong. Các Phần đó đo trên bó mã
> `assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`); Phần 8, 9 và 10 đo trên
> `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`). **Nhãn trong ứng dụng vẫn là `V1.0.8`
> ở cả hai lần dựng** ⇒ **không được dùng nhãn để nhận biết bản dựng**. Riêng trong phiên đo Phần 10, bó mã
> được đo **2 lần cách nhau 18 phút và giống hệt nhau** ⇒ **không trôi thêm** trong lúc đo; kết luận dưới đây
> chỉ có hiệu lực cho đúng bó mã `md5 3904131c…`.

> **Quan hệ với Phần 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9:** cùng một chức năng xuất báo cáo
> (`POST /api/v1/bao-cao/export`), khác loại báo cáo. Dòng 218 vẫn được đo **riêng** trên đúng màn của nó —
> **BC Chất lượng đào tạo** (FR-IX-10 / UC133, `srs-fr-11-bao-cao.md:515`). 🔴 Màn này **rất dễ nhầm** với
> hai màn đào tạo khác đã đo ở Phần 6 và Phần 7 — *BC Lớp đào tạo **đang** diễn ra* (FR-IX-06, dòng 200) và
> *BC Lớp đào tạo **đã** diễn ra* (FR-IX-07, dòng 205): hai màn đó lọc theo *Hình thức / Lĩnh vực*, còn màn
> này **chỉ có một bộ lọc đặc thù là *Khóa học*** (`:534`, `:1073`) và có thẻ **Tỷ lệ đạt**. Bản chất báo cáo
> cũng khác: FR-IX-10 tính **điểm trung bình kiểm tra + tỷ lệ học viên đạt điểm chuẩn trong kỳ** (`:536`),
> không phải đếm lớp. Không suy kết quả từ case anh em.

## Bug Summary Table (Phần 10)

| ID | Severity | Priority | Loại | Case | Đặc tả | Ảnh | Status |
|----|----------|----------|------|------|--------|-----|--------|
| BUG-CLDTBDPL-006 | Major | P1 | Permission | `CLDTBDPL_06` (tab `bug` dòng 218) | `srs-fr-11-bao-cao.md:117` · `:79` · `:1052` · `:1053` | [`image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Open |

---

## BUG-CLDTBDPL-006 — Vai trò QTHT xem được BC Chất lượng đào tạo nhưng bị chặn khi Xuất Excel/PDF, thông báo là chuỗi tiếng Anh thô "Forbidden"

> **Re-test:** 2026-08-06 16:19 R1 — 🔁 Reopen trên `18.143.165.120.nip.io`, bó mã `index-DIABnbIr.js`.
> Vế đối tác nêu ở vòng 1 (*"Không thể tạo file xuất. Vui lòng thử lại."*) **hết lỗi**: vai trò CB Nghiệp vụ
> Trung ương xuất được **10/10 lượt** (4 dạng bộ lọc + 1 lượt lặp chống đè + 1 lượt lặp cùng phút + 1 PDF +
> 3 lượt gọi thẳng máy chủ), tệp mở đọc được, đủ 4 mục đầu tệp, số khớp màn từng con số và cộng dọc khớp tổng.
> Vế tên tệp cũng **đạt** (`BaoCaoChatLuongDaoTao_20260806_1605.xlsx` — đúng khuôn
> `{TenBaoCao}_{YYYYMMDD_HHmm}`, hai lượt cùng ngày khác phút ra hai tên khác nhau). Vế vòng 2 (*"Forbidden"*,
> TKM retest 31/07) **tái hiện nguyên vẹn 19/19 lượt** ở đúng vai trò đối tác đã dùng, **cả nhánh Excel lẫn
> nhánh PDF** · **không seed, không tạo/sửa/xoá bản ghi nào** — toàn bộ thao tác chỉ đọc.

### Mô tả

Trên màn *Báo cáo thống kê*, loại báo cáo **BC Chất lượng đào tạo**, người dùng vai trò **Quản trị hệ thống
(QTHT)** bấm [Xem báo cáo] thì hệ thống hiển thị **đầy đủ** số liệu (Tổng khóa học 7 · Tổng học viên 17 ·
Điểm trung bình 6 · Tỷ lệ đạt 28.6 %, kèm bảng danh sách khóa học và biểu đồ) và **hiện hai nút [Xuất Excel] /
[Xuất PDF] ở trạng thái bấm được**, nhưng bấm tiếp [Xuất Excel] thì bị từ chối và **không nhận được tệp nào**.
Chữ hiện ra cho người dùng là **"Forbidden"** — chuỗi tiếng Anh thô lấy thẳng từ phản hồi kỹ thuật của máy
chủ, không cho người dùng biết chuyện gì đã xảy ra và phải làm gì tiếp. Nhánh [Xuất PDF] cũng vậy: hộp thoại
*Tùy chọn in báo cáo PDF* mở bình thường, bấm [Xuất file] mới hiện đúng chuỗi đó. Cùng thao tác, cùng bộ lọc,
**cùng đơn vị**, vai trò Cán bộ Nghiệp vụ Trung ương xuất tệp bình thường.

### Các bước tái hiện

1. Đăng nhập vai trò **Quản trị hệ thống** (tài khoản `admin`; `/api/v1/auth/me` ghi `vaiTro = ["QTHT"]`,
   `capDonVi = "TW"`, `donViId = 00000000-0000-4000-8000-000000000001` = *Cục Bổ trợ tư pháp - Bộ Tư pháp*) —
   đúng vai trò và đơn vị đọc được ở góc phải trên **cả hai** bằng chứng của đối tác.
2. Vào menu **Báo cáo thống kê**.
3. Chọn *Loại báo cáo* = **BC Chất lượng đào tạo** (đường dẫn phải chứa `loai=chat-luong-dao-tao` —
   **không** nhầm sang *BC Lớp đào tạo đang diễn ra* hay *BC Lớp đào tạo đã diễn ra*); *Kỳ báo cáo* = **Năm**
   (01/01/2026 → 31/12/2026); *Đơn vị* = **Toàn quốc**; để trống bộ lọc *Khóa học* — đúng cấu hình trên **cả
   hai** ảnh của đối tác.
4. Bấm **[Xem báo cáo]** — quan sát: báo cáo hiện đầy đủ (7 · 17 · 6 · 28.6 % + bảng danh sách khóa học +
   biểu đồ), không có cảnh báo nào; hai nút Xuất bật lên.
5. Bấm **[Xuất Excel]** — quan sát chữ hiện ra và xem có tệp nào về máy không.
6. Bấm **[Xuất PDF]** → trong hộp thoại *Tùy chọn in báo cáo PDF* bấm **[Xuất file]** — quan sát tương tự.
7. Lặp lại đúng các bước trên bằng tài khoản **CB Nghiệp vụ Trung ương** (`cbnv_tw_05`) để đối chiếu.

### Kết quả mong đợi

- Theo `srs-fr-11-bao-cao.md:117` (E7 `ERR-RPT-05`), khi hệ thống từ chối vì người dùng không có quyền thì
  phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo** — không đẩy nguyên chuỗi
  kỹ thuật tiếng Anh của máy chủ ra màn hình.
- Theo `srs-fr-11-bao-cao.md:79` (Processing bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn
  vị"*), việc kiểm quyền nằm ở **đầu** luồng. Nếu vai trò này không được phép dùng báo cáo thì phải bị chặn
  ngay từ bước Xem, chứ không cho xem đầy đủ số liệu rồi mới chặn ở bước xuất — **hai bước phải nhất quán**.
- `srs-fr-11-bao-cao.md:1052` và `:1053` ghi điều kiện hiển thị của nút Xuất Excel / Xuất PDF chỉ là *"Sau
  khi đã 'Xem báo cáo'"*, **không kèm điều kiện vai trò** — phần mềm đang mời người dùng bấm một nút rồi từ
  chối chính thao tác đó.

### Kết quả thực tế

**Vai trò QTHT (`admin`) — 2026-08-06 16:14–16:18:**

- [Xem báo cáo]: `GET /api/v1/bao-cao/chat-luong-dao-tao?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  → **200**, màn hiện đủ **7 khóa học · 17 học viên · điểm TB 6 · tỷ lệ đạt 28.6 %** (*Thời điểm tạo
  06/08/2026 16:14*) — **đúng bằng số liệu vai trò CB Nghiệp vụ thấy**, không thiếu dòng nào.
- Hai nút [Xuất Excel] / [Xuất PDF]: **hiện và ở trạng thái bấm được** (`disabled = false`).
- [Xuất Excel]: `POST /api/v1/bao-cao/export` → **403**; mỗi cú bấm đúng **1** lời gọi và **1** khung thông
  báo (không có hiện tượng 2 thông báo chồng); chữ người dùng đọc được đổi **tại chỗ trong khung cũ**:
  *"Đang tạo file..."* → **"Forbidden"**. Khung nằm trong vùng nhìn thấy (`x=8 · y=16 · w=1416 · h=40`, sát
  đỉnh trang) và **sống ~3,2 s** (mẫu chữ theo thời gian: khung trượt vào ở mốc 2 601 ms, đứng yên ở 2 902 ms,
  bắt đầu trượt ra ở 5 702 ms). Bấm chuột thật **10 lượt** — lượt nào cũng ra đúng chữ đó; **0 tệp** được giao.
- Nội dung gửi lên **giống hệt** phiên CB Nghiệp vụ, chỉ khác phiên đăng nhập:
  ```json
  → {"loaiBaoCao":"BC_CHAT_LUONG_DAO_TAO","kyBaoCao":"NAM","tuNgay":"2026-01-01",
     "denNgay":"2026-12-31","filterDacThu":{},"formatXuat":"XLSX"}
  ← {"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",
     "timestamp":"2026-08-06T09:17:12.865Z","requestId":"7c1edd46-6581-4b37-9773-d3edc693d92e"}}
  ```
  Header trả về **không có** `content-disposition` (`content-type: application/json`, `content-length: 167`)
  ⇒ không có tệp đính kèm. Chữ trên màn **trùng khít** `error.message` của máy chủ ⇒ giao diện đẩy nguyên
  chuỗi kỹ thuật ra cho người dùng cuối.
- [Xuất PDF]: hộp thoại *Tùy chọn in báo cáo PDF* mở bình thường (A4 · Dọc mặc định); bấm [Xuất file] →
  **403** với thân gửi lên `…"formatXuat":"PDF"`, phản hồi cùng mã `ERR-PERM-SYS-00-01` / `"Forbidden"`
  (**7 lượt**). ⇒ **không phải khuyết tật riêng của nhánh Excel**.
- Đo lại bằng **đường thứ hai** (gọi thẳng máy chủ, cùng phiên QTHT, cùng thân yêu cầu): `formatXuat` =
  **XLSX** → **403**, `formatXuat` = **PDF** → **403**, thân phản hồi cùng mã `ERR-PERM-SYS-00-01`.
  ⇒ Cộng lại **19/19 lượt** (17 bấm chuột + 2 gọi thẳng) đều bị chặn — **không phải chập chờn**, và **không**
  phải lỗi thao tác trên giao diện.
- **Quét thư mục tải xuống** với mốc *"mới hơn 16:12"*: **không có** tệp `.xlsx`/`.pdf` nào ⇒ qua 19 lượt
  thử, người dùng vai trò này ra về tay trắng.

**Vai trò CB Nghiệp vụ Trung ương (`cbnv_tw_05`) — cùng màn, 4 dạng bộ lọc + 2 lượt lặp + 1 lượt PDF:**

| Lượt | Bộ lọc / định dạng | Màn trước khi bấm (KH/HV/điểm TB/tỷ lệ đạt) | Giờ bấm | Phản hồi | Tệp nhận được | Chữ hiện cho người dùng |
|---|---|---|---|---|---|---|
| 1 | Năm 2026 · Toàn quốc · **Khóa học trống** (đúng cấu hình **cả hai** vòng của đối tác) | 7 / 17 / 6 / 28.6 % | 16:05 | **200**, kiểu `…spreadsheetml.sheet` | `BaoCaoChatLuongDaoTao_20260806_1605.xlsx` — 7 424 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 2 | Lọc *Khóa học = Khóa pháp luật cơ bản cho DN 2026 (đợt 1)* (`KH-2026-001`) | 1 / 2 / 7 / 100.0 % | 16:07 | **200** | `BaoCaoChatLuongDaoTao_20260806_1607.xlsx` — 6 950 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 3 | Lọc *Khóa học = QA RV5 - Khoa hoc test diem danh theo buoi* (`KH-20260716-002`) | 1 / 2 / 1 / 0.0 % | 16:08 | **200** | `BaoCaoChatLuongDaoTao_20260806_1608.xlsx` — 6 964 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 4 | Thu hẹp *Đơn vị = Sở Tư pháp Hà Nội (STP-HN)*, khóa học trống | 1 / 3 / 6 / 0.0 % | 16:09 | **200** | `BaoCaoChatLuongDaoTao_20260806_1609.xlsx` — 6 922 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 5 | **Xuất PDF** (qua hộp thoại *Tùy chọn in báo cáo PDF*) | 1 / 3 / 6 / 0.0 % | 16:10 | **200**, `%PDF` | `BaoCaoChatLuongDaoTao_20260806_1610.pdf` — 34 281 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 6 | Lặp lại y hệt lượt 4 (**phép thử chống đè tệp**) | 1 / 3 / 6 / 0.0 % | 16:11 | **200** | `BaoCaoChatLuongDaoTao_20260806_1611.xlsx` — 6 921 B | *"Đang tạo file..."* → *"Tạo file thành công."* |
| 7 | Quay lại dạng 1 (lượt kèm bắt nội dung gửi lên) | 7 / 17 / 6 / 28.6 % | 16:12 | **200** | `BaoCaoChatLuongDaoTao_20260806_1612.xlsx` — 7 423 B | *"Đang tạo file..."* → *"Tạo file thành công."* |

- **Không** xuất hiện *"Không thể tạo file xuất. Vui lòng thử lại."* (`ERR-RPT-04`, `:116`) ở bất kỳ lượt
  nào, cũng **không** có *"Forbidden"* ⇒ vế vòng 1 của đối tác hết lỗi. Mỗi lượt đúng **1** lời gọi xuất,
  **1** khung thông báo (đếm theo mốc giờ khác nhau, bộ theo dõi không lọc trùng, tự kiểm 1 observer).
- **Tên tệp** — đo từ **hai đường độc lập và trùng khít**: header `content-disposition` của máy chủ
  (`attachment; filename="BaoCaoChatLuongDaoTao_20260806_1613.xlsx"`) và **tệp rơi thật về thư mục tải xuống**
  (đúng thứ người dùng thật nhìn thấy). Khớp khuôn đặc tả `:85` + `srs-v3.5.md:6716` (Phụ lục E §H8) —
  `{TenTep}_{YYYYMMDD_HHmm}.{đuôi}`, PascalCase, không dấu, không gạch nối, **có đủ giờ-phút** và giờ-phút
  **khớp thời điểm xuất thật**. Hai lượt xuất **cùng ngày, cùng bộ lọc, khác phút** (16:09 / 16:11) ra **hai
  tên khác nhau** ⇒ không đè tệp nhau, đúng chủ đích BA chốt 2026-08-04 khi bắt buộc phần giờ-phút. Phần
  `{TenBaoCao}` là `BaoCaoChatLuongDaoTao` — **đúng loại báo cáo này**, dài 41 ký tự (≤ 255).
- **Mở tệp ra đọc** (không dừng ở "200 + có byte"): sheet *"BC Chất lượng đào tạo"*, đủ 4 mục đầu tệp `:1092`
  đòi — *BC Chất lượng đào tạo* · *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · *Đơn vị: Toàn quốc*
  (dạng 4 đổi đúng thành *Đơn vị: Sở Tư pháp Hà Nội*) · *Ngày tạo: 06/08/2026*. Số trong tệp khớp **từng con
  số** với màn của chính lượt đó (7 / 17 / 6,35 / 28,6 — 1 / 2 / 7,85 / 100 — 1 / 2 / 1,5 / 0 — 1 / 3 / 6 / 0);
  bảng *Danh sách khóa học* cộng dọc bằng đúng thẻ tổng — số học viên 2+3+2+3+2+1+4 = **17**, đếm dòng = **7**;
  điểm trung bình tổng 6,35 nằm trong khoảng [1,5 ; 10] của các khóa thành phần và tỷ lệ đạt tổng 28,6 nằm
  trong [0 ; 100] — đúng tính chất *trung bình theo khóa học / đơn vị* ở `:536`.
- **Bộ lọc *Khóa học* chạy đúng** — AC `:552` (*"chọn KH cụ thể → hiển thị chi tiết KH đó"*) thoả: lượt 2 và
  lượt 3 cùng chiều lọc cho **hai kết quả khác hẳn** (7,85 điểm / 100 % ↔ 1,5 điểm / 0 %). Giao diện gửi khoá
  `khoaHocId` — **đúng khoá máy chủ nhận** — ở cả lượt Xem lẫn trong `filterDacThu` của lượt Xuất; đo thêm
  4 cách viết khoá khác (`fd_khoaHocId` · `khoa_hoc_id` · `khoaHoc` · không lọc) thì máy chủ **bỏ qua** hết và
  trả nguyên tập 7 khóa (bảng đo 5 dòng ở
  [`image/CLDTBDPL_06-10-…txt`](image/CLDTBDPL_06-10-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt) §PHẦN 5).
  ⇒ Màn này **không** dính khuyết tật lệch tên khoá bộ lọc như các màn khác.
- **Tệp bám đúng bộ lọc hiện tại** (`:1280`): 6 tệp `.xlsx` cho **6 md5 khác nhau** (7 424 / 6 950 / 6 964 /
  6 922 / 6 921 / 7 423 B), không có cặp nào *"màn khác số mà tệp giống hệt"*; và **đường đo thứ hai** (gọi
  thẳng máy chủ) trả về đúng **7 423 / 6 950 / 6 964 B** cho ba cấu hình tương ứng ⇒ hai đường khớp nhau.

⇒ **Vế vòng 1 (`ERR-RPT-04`, `:116`) hết lỗi. Vế tên tệp đạt. Vế vòng 2 (*"Forbidden"*) tái hiện nguyên
vẹn** đúng vai trò, đúng màn, đúng cấu hình bộ lọc của đối tác.

### Bằng chứng

- 🔴 [`image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png)
  — phiên vai trò **QTHT** (góc phải: *Quản trị hệ thống · QT*), đúng cấu hình bộ lọc của đối tác, khung
  thông báo **đỏ chữ "Forbidden"** nổi giữa đỉnh trang trên nền báo cáo đã hiện đủ 7 · 17 · 6 · 28.6 %.
  *Ghi chú cách chụp:* khung chỉ sống ~3,2 giây và thư viện giao diện **thay chữ ngay trong khung cũ**, nên
  phải **hẹn giờ bấm trước rồi mới gọi chụp**; mọi lượt bấm đều là lời gọi xuất trả 403, **không** đổi dữ liệu.
- 🔴 [`image/CLDTBDPL_06-09-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](image/CLDTBDPL_06-09-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png)
  — cùng vai trò QTHT nhưng đi **nhánh [Xuất PDF]**: hộp thoại tuỳ chọn in mở bình thường, bấm [Xuất file]
  cũng ra đúng chuỗi **"Forbidden"** ⇒ khuyết tật nằm ở đường xuất chung, không riêng nhánh Excel.
- [`image/CLDTBDPL_06-07-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png`](image/CLDTBDPL_06-07-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png)
  — cùng phiên QTHT, trạng thái **ngay trước** thao tác bị từ chối: báo cáo hiện đủ 7 · 17 · 6 · 28.6 % và
  **hai nút Xuất đang bấm được** — tức người dùng được mời bấm đúng nút sẽ bị từ chối ngay sau đó.
- [`image/CLDTBDPL_06-01-dang1-khong-loc-khoahoc-man-hinh-truoc-khi-xuat-V108.png`](image/CLDTBDPL_06-01-dang1-khong-loc-khoahoc-man-hinh-truoc-khi-xuat-V108.png)
  — phiên CB Nghiệp vụ TW, dạng 1 (**đúng cấu hình cả hai vòng của đối tác**), màn hình **trước** khi bấm
  Xuất: *Thời điểm tạo 16:04*, 7 · 17 · 6 · 28.6 % — mốc đối chiếu số liệu với nội dung tệp.
- [`image/CLDTBDPL_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png`](image/CLDTBDPL_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png)
  — **ngay sau** cú bấm [Xuất Excel] ở vai trò CB Nghiệp vụ: khung thông báo *"Tạo file thành công."*, không
  còn câu *"Không thể tạo file xuất. Vui lòng thử lại."* mà đối tác gặp ở vòng 1.
- [`image/CLDTBDPL_06-03-dang2-loc-KhoaHoc-KH2026001-man-hinh-truoc-khi-xuat-V108.png`](image/CLDTBDPL_06-03-dang2-loc-KhoaHoc-KH2026001-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 2 (lọc *Khóa học = KH-2026-001*), số đổi thành 1 · 2 · 7 · 100.0 % — dùng chứng minh tệp xuất bám
  đúng bộ lọc.
- [`image/CLDTBDPL_06-04-dang3-loc-KhoaHoc-KH20260716002-so-lieu-doi-V108.png`](image/CLDTBDPL_06-04-dang3-loc-KhoaHoc-KH20260716002-so-lieu-doi-V108.png)
  — dạng 3 (khóa học thứ hai), 1 · 2 · **1** · **0.0 %** — khác hẳn dạng 2 ⇒ máy chủ không trả cùng một tập,
  AC `:552` thoả.
- [`image/CLDTBDPL_06-05-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png`](image/CLDTBDPL_06-05-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png)
  — dạng 4 (thu hẹp *Đơn vị = Sở Tư pháp Hà Nội*), 1 · 3 · 6 · 0.0 %; mục *Đơn vị* trong tệp xuất đổi theo.
- [`image/CLDTBDPL_06-06-hop-thoai-tuy-chon-in-PDF-V108.png`](image/CLDTBDPL_06-06-hop-thoai-tuy-chon-in-PDF-V108.png)
  — hộp thoại *"Tùy chọn in báo cáo PDF"* mà [Xuất PDF] mở ra; giữ lại vì đây là bước dễ hiểu nhầm thành
  *"bấm Xuất PDF không có phản ứng gì"*.
- [`image/CLDTBDPL_06-10-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](image/CLDTBDPL_06-10-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt)
  — nguyên văn chữ trên màn từng lượt (mốc giờ · kích thước · thời gian sống), nguyên văn phản hồi máy chủ
  của cả hai vai trò (kể cả thân 403), vai trò đọc từ `/api/v1/auth/me`, tên tệp đo từ cả hai đường, nội dung
  ô của 6 tệp .xlsx đọc bằng `openpyxl` + đầu trang PDF đọc bằng PyMuPDF, md5 từng tệp, phép thử chống đè tệp
  và **bảng đo bộ lọc 5 dòng**.
- Tệp thật hệ thống giao ra (tên gốc hệ thống đặt được giữ nguyên phía sau tiền tố mã case):
  [`testfiles/CLDTBDPL_06-dang1-khong-loc-BaoCaoChatLuongDaoTao_20260806_1605.xlsx`](testfiles/CLDTBDPL_06-dang1-khong-loc-BaoCaoChatLuongDaoTao_20260806_1605.xlsx)
  · [`testfiles/CLDTBDPL_06-dang2-loc-khoahoc-KH2026001-BaoCaoChatLuongDaoTao_20260806_1607.xlsx`](testfiles/CLDTBDPL_06-dang2-loc-khoahoc-KH2026001-BaoCaoChatLuongDaoTao_20260806_1607.xlsx)
  · [`testfiles/CLDTBDPL_06-dang3-loc-khoahoc-KH20260716002-BaoCaoChatLuongDaoTao_20260806_1608.xlsx`](testfiles/CLDTBDPL_06-dang3-loc-khoahoc-KH20260716002-BaoCaoChatLuongDaoTao_20260806_1608.xlsx)
  · [`testfiles/CLDTBDPL_06-dang4-donvi-STPHN-BaoCaoChatLuongDaoTao_20260806_1609.xlsx`](testfiles/CLDTBDPL_06-dang4-donvi-STPHN-BaoCaoChatLuongDaoTao_20260806_1609.xlsx)
  · [`testfiles/CLDTBDPL_06-dang4-lap-lai-chong-de-BaoCaoChatLuongDaoTao_20260806_1611.xlsx`](testfiles/CLDTBDPL_06-dang4-lap-lai-chong-de-BaoCaoChatLuongDaoTao_20260806_1611.xlsx)
  · [`testfiles/CLDTBDPL_06-dang1-lap-lai-cung-phut-BaoCaoChatLuongDaoTao_20260806_1612.xlsx`](testfiles/CLDTBDPL_06-dang1-lap-lai-cung-phut-BaoCaoChatLuongDaoTao_20260806_1612.xlsx)
  · [`testfiles/CLDTBDPL_06-pdf-dang4-BaoCaoChatLuongDaoTao_20260806_1610.pdf`](testfiles/CLDTBDPL_06-pdf-dang4-BaoCaoChatLuongDaoTao_20260806_1610.pdf)

### So sánh vai trò

Phép đối chứng đổi **đúng một biến** — cùng đường dẫn, cùng thân yêu cầu **từng chữ**, cùng
`donViId …0001`, cùng bó mã, chỉ khác vai trò:

| Vai trò | [Xem báo cáo] | [Xuất Excel] | Header trả về | Chữ hiện cho người dùng |
|---|---|---|---|---|
| `cbnv_tw_05` — CB Nghiệp vụ TW (tác nhân đặc tả `:62`, `:526`) | 200, ra đủ 7 · 17 · 6 · 28.6 % | **200**, nhận được tệp .xlsx/.pdf mở đọc được | `content-disposition: attachment; filename="BaoCaoChatLuongDaoTao_20260806_1613.xlsx"` | *"Đang tạo file..."* → *"Tạo file thành công."* |
| `admin` — QTHT, cấp TW, **cùng đơn vị BTP** (vai trò đối tác dùng) | 200, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | *(không có `content-disposition`)* | *"Forbidden"* |

⇒ Đường xuất tệp **không hỏng**; đúng vai trò thì chạy. Chỉ vai trò QTHT bị chặn, và bị chặn **sau khi** đã
được cho xem đủ số liệu.

### Ghi chú liên quan

- **Cả hai bằng chứng của đối tác đều đúng case này** — kiểm bằng nội dung màn: chữ trong ô chọn *Loại báo
  cáo* = *BC Chất lượng đào tạo* · bộ lọc đặc thù trên màn là ***Khóa học*** (chỉ màn FR-IX-10 có) · tiêu đề
  khối kết quả · các thẻ số liệu có *Tỷ lệ đạt*. **Không** nhầm với *BC Lớp đào tạo đang diễn ra* (FR-IX-06,
  dòng 200) và *BC Lớp đào tạo đã diễn ra* (FR-IX-07, dòng 205).
  🔴 **Một điểm phải nói rõ:** thanh địa chỉ trên ảnh **vòng 2** (`CLDTBDPL_06_v2.jpg`) còn sót
  `loai=danh-gia-hieu-qua` (loại báo cáo của case `DGHQHTPL_06`, dòng 214) trong khi **toàn bộ nội dung màn**
  là *BC Chất lượng đào tạo*. Giải thích khớp nhất: đối tác chụp liền mạch nhiều case trong một phiên, đổi
  loại báo cáo trong ô chọn rồi bấm [Xem báo cáo] nhưng đường dẫn chưa đồng bộ lại. ⇒ **Vẫn nhận ảnh này là
  bằng chứng của case này** (4 dấu hiệu nội dung đều trỏ đúng màn), nhưng **không** dùng đường dẫn của ảnh
  vòng 2 làm dữ kiện neo, và **không** dùng chi tiết này để bác đối tác. Ảnh vòng 1 thì đường dẫn và nội dung
  khớp nhau hoàn toàn (`loai=chat-luong-dao-tao`).
- **Hai vòng của đối tác không so trực tiếp được với nhau**: cùng vai trò, cùng loại báo cáo, cùng kỳ, cùng
  đơn vị và cùng bộ lọc *Khóa học* để trống, nhưng khác bản dựng (V1.0 → V1.0.3), khác số thẻ hiện trên màn
  (3 thẻ → 4 thẻ, vòng 2 có thêm *Tổng học viên*) và khác số liệu (3 khóa / 80,0 % → 5 khóa / 14 HV / 58,0 %).
- **Hai đường đo độc lập cùng kết luận, không mâu thuẫn:** đường giao diện (thao tác chuột thật, đọc chữ
  hiện trên màn) và đường máy chủ (mã HTTP + thân phản hồi) khớp nhau ở cả hai vai trò ⇒ không có điểm nào
  cần hỏi thêm trước khi kết luận.
- Câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* đã có mục dành cho BA ở
  [`cau-hoi-BA.md`](cau-hoi-BA.md) § *Mục 2* — **không lặp lại ở đây**. Mục đó **không** kéo verdict của
  case: nếu BA chốt QTHT *không* được xuất thì hệ thống vẫn phải hiện câu tiếng Việt `:117` thay vì
  `Forbidden`, và phải chặn ngay từ bước Xem cho nhất quán (`:79`); nếu BA chốt QTHT *được* xuất thì đang
  chặn nhầm. Khuyết tật tồn tại ở **cả hai nhánh trả lời**, nên không chờ BA.
- **Không** chấm lỗi phần tên tệp: đối tác kỳ vọng `BaoCaoDaoTao_{YYYYMMDD_HHmm}`, hệ thống ra
  `BaoCaoChatLuongDaoTao_20260806_1605.xlsx`. Đặc tả chỉ quy định **khuôn** tên (`:85`, `:86` +
  `srs-v3.5.md:6716` Phụ lục E §H8) với `{TenBaoCao}` là **tên loại báo cáo**, **không** ấn định đúng chuỗi
  `BaoCaoDaoTao`. Tên hệ thống dùng khớp khuôn, có đủ giờ-phút, mang đúng tên loại báo cáo này (chỉ dài hơn
  chuỗi đối tác viết), hai lượt cùng ngày khác phút không đè nhau ⇒ **không** phải khuyết tật.
  *(So với số đo cũ 03/08 — `bao-cao-<slug>-2026-08-03.xlsx`, thiếu giờ-phút, có gạch nối — khuôn tên đã được
  sửa đúng ở bản dựng đang đo.)*
- **Cùng nguyên nhân gốc với** `BUG-SLCTHT-006` (Phần 2), `BUG-SLHDVM-006` (Phần 3), `BUG-CPHTCT-006` /
  `BUG-CPCTHTTDVQL-006` / `BUG-CPCTHTTLHDN-006` / `BUG-CPCTHTTTG-005` / `BUG-CPCTHTTTG-006` (Phần 4),
  `BUG-CTTDVQL-004` (Phần 5), `BUG-CLDTBDDDR-006` (Phần 6), `BUG-LDTBDDDR-006` (Phần 7),
  `BUG-CGTVPL-006` (Phần 8), `BUG-DGHQHTPL-006` (Phần 9) — cùng endpoint `POST /api/v1/bao-cao/export`, cùng
  mã `ERR-PERM-SYS-00-01`, khác loại báo cáo. Dev sửa một chỗ có thể đóng cả nhóm; QA vòng sau vẫn phải
  verify riêng từng case trên đúng màn của nó. **Không mở dòng bug mới trên bảng theo dõi** cho case này.

#### Ghi nhận ngoài vế đối tác nêu — **không** kéo verdict case, chưa mở dòng trên bảng

Ba điểm dưới đây phát hiện trong lúc đo nhưng đối tác **không** nêu ở case này (cả hai ảnh chỉ nêu thông báo
khi bấm xuất). Ghi lại đầy đủ để phiên chính quyết có mở dòng riêng hay không; QA không tự mở.

- **D4 — Thiếu hẳn nhóm kết quả *theo đơn vị* (`theo_don_vi[]`, điều kiện hiển thị *"Luôn"*,
  `srs-fr-11-bao-cao.md:548`).** Phản hồi của màn này chỉ trả `tenBaoCao · tuNgay · denNgay · tongKhoaHoc ·
  tongHocVien · diemTrungBinhTong · tyLeDatTong · danhSachKhoaHoc · chartType` — có phần theo khóa học
  (≈ `theo_khoa_hoc[]`, `:547`) nhưng **không có** phần theo đơn vị; tệp xuất cũng chỉ có bảng *Danh sách
  khóa học*, **không có** bảng tổng hợp {đơn vị · điểm TB · tỷ lệ đạt}. Cột *Đơn vị* trong bảng khóa học là
  thuộc tính của từng khóa, không phải số liệu tổng hợp theo đơn vị. Đây là nhóm đầu ra đặc tả ghi điều kiện
  *"Luôn"* và `:524` cũng mô tả báo cáo *"phân theo khóa học, **đơn vị**"*. **Không ảnh hưởng phép đo nào của
  case:** cả 10 lượt xuất của vai trò CB Nghiệp vụ đều thực hiện trên báo cáo vừa render xong với nút ở trạng
  thái bấm được, và verdict REOPEN đứng vững chỉ bằng vế *"Forbidden"*.
- **D5 — Hai lượt xuất trong CÙNG một phút ra TRÙNG tên tệp.** Hai lượt lúc 16:12 (cùng cấu hình) đều được
  máy chủ đặt tên `BaoCaoChatLuongDaoTao_20260806_1612.xlsx`, trình duyệt phải tự thêm `" (1)"`; ba lượt gọi
  thẳng lúc 16:13 cũng cùng nhận `…_1613.xlsx`. Phụ lục E §H8 (`srs-v3.5.md:6716`) ghi rõ *"trùng tên (hai lần
  xuất trong cùng phút) thì tự thêm hậu tố `_1`, `_2`"*. **Không** kéo verdict: đối tác chỉ đòi khuôn
  `{TenBaoCao}_{YYYYMMDD_HHmm}`, và phép thử chống đè của tiêu chí (hai **phút khác nhau**) vẫn **đạt**.
- **D6 — Thẻ *"Điểm trung bình"* trên màn cắt cụt phần thập phân.** Máy chủ và tệp xuất trả 6,35 nhưng thẻ
  hiện `6`; tương tự 7,85 → `7`, 1,5 → `1`. Bảng *Danh sách khóa học* trên màn lại làm tròn 1 chữ số (1,5 ·
  6,3 · 7,9) trong khi tệp giữ đủ (1,5 · 6,25 · 7,85) ⇒ **ba cách hiển thị khác nhau cho cùng một con số**.
  Đặc tả **không** nêu công thức làm tròn nên tiêu chí đã ghi trước là **không chấm Fail**; ghi lại vì người
  dùng đọc thẻ 6 rồi mở tệp thấy 6,35 sẽ tưởng số liệu lệch. *(Kèm theo: thẻ "Tỷ lệ đạt" tổng 28,6 % ứng với
  2/7 khóa học, trong khi cộng theo học viên là 4/17 ≈ 23,5 %; `:536` không nói mẫu số là học viên hay khóa
  học nên không đủ căn cứ chấm.)*

### Khối giao việc

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản admin (vai trò Quản trị hệ thống, cấp TW) + màn Báo cáo thống kê
  (/bao-cao). Cần >=1 khóa học ĐÃ KẾT THÚC VÀ ĐÃ CHẤM ĐIỂM HỌC VIÊN trong kỳ để báo cáo có
  dữ liệu; nếu báo cáo trống thì nút Xuất sẽ không bật và phép thử không có giá trị.

Các bước:
  1. Đăng nhập admin (QTHT). Vào Báo cáo thống kê. TẢI LẠI TRANG và ghi lại bản dựng trước
     khi đo - ghi bằng TÊN BÓ MÃ assets/index-*.js, ĐỪNG ghi bằng nhãn V1.0.x: hai lần dựng
     khác nhau ngày 06/08 đều mang nhãn V1.0.8.
  2. Loại báo cáo = BC Chất lượng đào tạo (kiểm cả 3 chỗ: chuỗi trong đường dẫn phải là
     chat-luong-dao-tao, chữ trong ô chọn, tiêu đề khối kết quả - DỄ nhầm sang "BC Lớp đào
     tạo đang diễn ra" và "BC Lớp đào tạo đã diễn ra"); Kỳ = Năm 01/01/2026 - 31/12/2026;
     Đơn vị = Toàn quốc; để trống bộ lọc Khóa học. Bấm [Xem báo cáo], chờ ra số liệu.
  3. Cài bộ theo dõi thông báo TRƯỚC khi bấm (không lọc trùng, đọc innerText, lấy mẫu chữ
     theo thời gian - xem tools/toast-capture.js), rồi bấm [Xuất Excel].
  4. Ghi lại: chữ hiện cho người dùng · mã trả về của POST /api/v1/bao-cao/export · số tệp
     nhận được.
  5. Làm lại bước 3-4 cho nhánh [Xuất PDF]: nút này mở hộp thoại "Tùy chọn in báo cáo PDF",
     phải bấm tiếp [Xuất file] mới gọi máy chủ.
  6. Lặp lại bước 2-5 bằng tài khoản cbnv_tw_05 (CB Nghiệp vụ TW) để đối chiếu, và MỞ TỆP
     xuất ra đọc: phải còn đủ 4 mục đầu tệp (tên BC, kỳ, đơn vị, ngày tạo), còn đủ các chỉ số
     Tổng khóa học - Tổng học viên - Điểm trung bình - Tỷ lệ đạt và bảng danh sách khóa học;
     số khớp màn, cộng dọc cột số học viên khớp thẻ Tổng học viên, đếm dòng khớp thẻ Tổng
     khóa học.
  7. Đo thêm 2 khóa học KHÁC NHAU: tệp xuất phải đổi theo khóa học được chọn (đây là bộ lọc
     đặc thù duy nhất của màn này).

PASS khi:
  - Vai trò QTHT: KHÔNG còn thấy chuỗi "Forbidden" trên màn, ở CẢ nhánh Excel lẫn nhánh PDF.
    Nếu hệ thống vẫn từ chối thì câu hiện ra phải là câu tiếng Việt cho biết người dùng không
    có quyền (yêu cầu :117); nếu BA chốt QTHT được xuất thì phải nhận được tệp mở đọc được.
  - Bước Xem và bước Xuất nhất quán: không còn cảnh cho xem đủ số liệu rồi chặn ở bước xuất.
    Nếu vai trò bị cấm thì phải chặn ngay từ bước Xem (yêu cầu :79).
  - Vai trò cbnv_tw_05 vẫn xuất được cả Excel lẫn PDF ở cả 4 dạng lọc, tên tệp vẫn đúng khuôn
    có giờ-phút và mang đúng tên loại báo cáo "chất lượng đào tạo", nội dung tệp vẫn đúng như
    mô tả ở bước 6 (không hồi quy).

FAIL nếu:
  - Còn bất kỳ chỗ nào hiện chuỗi kỹ thuật tiếng Anh (Forbidden / Unauthorized / Internal
    Server Error) cho người dùng cuối.
  - Sửa bằng cách ẩn/làm mờ nút Xuất mà bước Xem vẫn cho vào: người dùng vẫn không biết vì
    sao mình không xuất được -> chưa đạt :117.
  - Chỉ sửa nhánh Excel mà quên nhánh PDF (hoặc ngược lại).
  - Vai trò CB Nghiệp vụ bị chặn theo, hoặc tệp xuất mất mục đầu tệp / mất bảng danh sách
    khóa học / mất phần giờ-phút trong tên tệp / tên tệp mang tên loại báo cáo khác (hồi quy).

Bẫy hay gặp:
  - Khung thông báo chỉ sống ~3,2 giây và thư viện giao diện CẬP NHẬT CHỮ NGAY TRONG khung cũ
    chứ không mọc khung mới. Nếu chỉ ghi "khung nào mới mọc" sẽ chỉ thấy "Đang tạo file..."
    và kết luận nhầm là hệ thống im lặng. Phải lấy mẫu chữ theo thời gian; muốn chụp được thì
    hẹn giờ bấm trước rồi mới gọi chụp.
  - Đo bằng vai trò CB Nghiệp vụ rồi kết luận "hết lỗi" là sai. Phải đo bằng đúng vai trò
    QTHT như trên bằng chứng của đối tác.
  - Rất dễ mở nhầm màn: hai màn "BC Lớp đào tạo đang/đã diễn ra" lọc theo Hình thức và Lĩnh
    vực; chỉ màn này có bộ lọc "Khóa học" và thẻ "Tỷ lệ đạt". Kiểm đủ 3 chỗ như bước 2.
  - [Xuất PDF] KHÔNG tải tệp ngay: nó mở hộp thoại "Tùy chọn in báo cáo PDF", phải bấm tiếp
    [Xuất file]. Bỏ qua bước này rất dễ báo oan "bấm không có phản ứng"; hộp thoại còn mở cũng
    nuốt luôn cú bấm [Xuất Excel] ngay sau đó.
  - Tab trình duyệt mở lâu vẫn chạy mã cũ: phải tải lại trang; và ghi bản dựng bằng tên bó mã
    assets/index-*.js chứ đừng tin nhãn V1.0.x.
  - Màn này KHÔNG có trường ngayTaoBc trong dữ liệu máy chủ trả về (dòng "Thời điểm tạo" trên
    màn do giao diện tự sinh) nên không dùng được mẹo loại trừ nhớ đệm bằng ngayTaoBc như các
    màn báo cáo khác. Muốn loại trừ nhớ đệm thì gọi nhiều biến thể tham số trong CÙNG một
    phiên và so kết quả với nhau.
  - Thẻ "Điểm trung bình" đang cắt phần thập phân (ghi nhận D6): thẻ hiện 6 trong khi tệp và
    máy chủ là 6,35. Đừng vội kết luận "tệp lệch màn" - so bằng con số máy chủ trả về.
```

**Owner + việc tiếp theo:** **Dev BE** — thống nhất quy tắc quyền giữa bước xem và bước xuất báo cáo cho vai
trò QTHT, và trả thông báo từ chối theo đúng yêu cầu `srs-fr-11-bao-cao.md:117`. **Dev FE** — không đẩy
nguyên chuỗi kỹ thuật của máy chủ ra màn hình người dùng. Cần **BA** chốt câu hỏi ở
[`cau-hoi-BA.md`](cau-hoi-BA.md) § Mục 2 trước khi dev chọn hướng sửa. Ghi nhận D4 · D5 · D6 ở trên chuyển
**phiên chính** quyết, không chặn bản sửa này.

## Phụ lục — Môi trường test (Phần 10)

| Hạng mục | Giá trị |
|---|---|
| **Ứng dụng** | https://18.143.165.120.nip.io — nhãn HTPLDN **V1.0.8**, bó mã giao diện `assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`, 1 123 565 byte, etag `W/"6a74340b-1124ed"`, `last-modified` Thu, 06 Aug 2026 07:13:15 GMT) — **tự đo 2 lần, lúc 16:01 và 16:19, giống hệt nhau**. ⚠️ Bản dựng này **mới hơn** bản các Phần 2–7 đo (`index-CNwX9JjX.js`) dù **nhãn không đổi** |
| **Màn đo** | Báo cáo thống kê → **BC Chất lượng đào tạo** (`/bao-cao?loai=chat-luong-dao-tao`), FR-IX-10 / UC133 (`srs-fr-11-bao-cao.md:515`) |
| **Trình duyệt** | Chrome (Chrome DevTools MCP), tab riêng cho từng vai trò — cách ly cookie/bộ nhớ khỏi phiên QA chạy song song |
| **Danh tính** | `/api/v1/auth/me` đo **trước** mỗi phép đo quyết định; QTHT trả `vaiTro ["QTHT"] · capDonVi "TW" · donViId 0000…0001`; CB Nghiệp vụ trả `vaiTro ["CB_NV_TW"] · capDonVi "TW" · donViId 0000…0001` — **cùng đơn vị**, chỉ khác vai trò |
| **Khung giờ đo** | 2026-08-06 16:01 → 16:19 |
| **Dữ liệu** | **Không seed, không tạo/sửa/xoá bản ghi nào** — env sẵn 7 khóa học đã chấm điểm trong kỳ Năm 2026 (17 học viên), trải 3 đơn vị (Cục Bổ trợ tư pháp - Bộ Tư pháp · Sở Tư pháp Hà Nội · Bộ Kế hoạch và Đầu tư), đủ cho cả 4 dạng biến thể. **Không** lượt nào rơi vào `INF-RPT-01` |

*Phần 10 generated: 2026-08-06 16:25:00 | QA Automation via Claude Code*
