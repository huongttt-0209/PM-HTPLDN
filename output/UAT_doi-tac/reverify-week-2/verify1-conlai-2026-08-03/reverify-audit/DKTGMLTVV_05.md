# DKTGMLTVV_05 — evidence audit (verify vòng 1, 2026-08-03)

## 0. Note CŨ của dev ở cột R (backup TRƯỚC khi đè)

> **R123 (DEV phản hồi lần 1) — giá trị cũ, dev ghi:**
> KHÔNG phải bug: Nhóm 4 có đủ tệp Bằng cấp/Chứng chỉ; tệp Thẻ hành nghề đặt ở Nhóm 2 đúng SRS (mục 3.6). Không thiếu chức năng, chỉ khác vị trí nhóm.

> **P123 (Trạng thái dev fix 1) — giá trị hiện tại:** `Reject` (KHÔNG đụng vào cột P)

---

## 1. Cổng 1 — Bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `partner-evidence/DKTGMLTVV_05_v2.jpg` (219.226 B) |
| Tình trạng | ⚠️ **TRÙNG md5 với `DKTGMLTVV_04_v2.jpg`** (`929d428dafad27beab53ef1266866053`) — hai case dùng CHUNG một file ảnh, không phải 2 ảnh riêng |
| Đã mở xem | ✅ Có, đọc full-res bằng Read tool (không đọc từ montage thu nhỏ) |

**3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**

- **(a) URL / ID bản ghi:** `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi` — form tạo mới, chưa có bản ghi nên không có ID. Đồng hồ máy đối tác: 03:43 PM 2026-07-25.
- **(b) Trạng thái entity:** form "Thêm mới" chưa lưu; breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới"; vai trò góc phải "hương 3 NHT · NHT", đơn vị "BTP · DP". Nhóm 3 và nhóm 4 đều đang mở (chevron xuống).
- **(c) Dữ liệu tiền đề:** form rỗng hoàn toàn — nhóm 3 còn nguyên placeholder, nhóm 4 chưa đính kèm file nào (khung kéo-thả trống, chưa có dòng file).

## 2. Cổng 2 — Hiểu bug (3 dòng bắt buộc)

1. **Evidence đã xem:** `DKTGMLTVV_05_v2.jpg`, vùng nửa dưới khung hình chứa nhóm "File đính kèm". Trong khung đó nhóm 4 chỉ hiện **đúng 1 mục** — "File đính kèm (Bằng cấp / Chứng chỉ)" + khung kéo-thả "Tối đa 10 tệp. Định dạng: .pdf. Dung lượng tối đa: 10MB/tệp." — **không có** mục "Tệp thẻ hành nghề".
2. **Đối tác phản ánh CỤ THỂ:** nhóm 4 phải gồm 2 tệp — "Tệp bằng cấp / chứng chỉ" **và** "Tệp thẻ hành nghề" (cột L). Web chỉ có tệp thứ nhất → họ chấm Fail.
3. **Data + bước tái hiện:** không cần seed. Đăng nhập NHT → Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Mới đăng ký" → "Thêm mới" → cuộn xuống nhóm "File đính kèm".

**Đánh giá độ đủ của bằng chứng (không tự nhận bừa):** ảnh bị **CẮT ngay dưới khung kéo-thả** nên tự nó **không chứng minh được sự VẮNG MẶT** của "File thẻ hành nghề" ở phần dưới nhóm 4. Tuy nhiên đây là claim về **hiển thị tĩnh của một biểu mẫu** mà QA mở lại được y hệt bằng đúng vai trò/đúng màn hình, và protocol §GATE quy định artifact quyết định cho claim dạng "absence" phải là **phép đo của chính QA trên data thật**, không phải frame của đối tác. Vì vậy: Cổng 1 + Cổng 2 **ĐÓNG** (bằng chứng mở được, thấy đúng vùng tranh chấp, trích đủ 3 dữ kiện neo), còn kết luận vắng mặt **lấy từ phép đo live bên dưới**, KHÔNG lấy từ ảnh. **Không** rơi vào ô TRỐNG.

## 3. Cổng 3 — Đối chiếu SRS vs web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` (bản chốt 2026-07-25). Màn `SCR-IV-02` mở tại dòng 1470; bảng thành phần nhóm 4 tại dòng 1518–1521. Đã mở file đọc trực tiếp, không quote từ trí nhớ.

| # | SRS yêu cầu (nguyên văn + dòng) | Web thực tế (đo live) | Đạt? |
|---|---|---|:-:|
| Nhóm 4 | `:1518` — "File đính kèm \| nhóm thu gọn" | Nhóm 4 tên **"File đính kèm"**, thu gọn được | ✅ |
| 5.1 | `:1519` — "**Bằng cấp / Chứng chỉ \***  \| tải nhiều file \| **Bắt buộc khi Người hỗ trợ đăng ký ứng viên mới**. Định dạng PDF, tối đa 10MB/file, tổng 50MB, tối đa 10 file" | Có mục "File đính kèm (Bằng cấp / Chứng chỉ)", nhận nhiều file, giới hạn hiển thị "Tối đa 10 tệp · .pdf · 10MB/tệp". **NHƯNG: không có dấu `*`** (`ant-form-item-required` = `false`) **và KHÔNG chặn** khi bỏ trống — hồ sơ vẫn lưu thành công | ❌ |
| 5.2 | `:1520` — "File thẻ hành nghề \| tải 1 file \| PDF, tối đa 10MB" (ô Ràng buộc **không ghi điều kiện** nào) | **KHÔNG có trong nhóm 4.** Trường này nằm ở **nhóm 2 "Nghề nghiệp"** với nhãn "File thẻ hành nghề (PDF)" (tối đa 1 tệp, .pdf, 10MB) | ⚠️ khác vị trí |
| 5.3 | `:1521` — "Danh sách file đã tải \| bảng \| Mỗi dòng: tên file + kích thước + nút Xem / Xóa"; hành vi "Xem: mở hộp xem PDF; **Xóa: xác nhận trước khi xóa**" | Sau khi upload thật: hiện dòng `bang-cap-qa-test.pdf` + `(620 B)` + nút **Xem** + **Xóa**. "Xem" mở PDF ở tab mới (blob URL) → xem được. **NHƯNG "Xóa" gỡ file NGAY, không có bước xác nhận** | ⚠️ một phần |

**Mâu thuẫn nội tại của SRS (quan trọng cho ý 1):** trường "File thẻ hành nghề" được SRS liệt kê **HAI LẦN**:
- `:1508` mục 3.6, **nhóm 2** — "File thẻ hành nghề \| tải file \| PDF, tối đa 10MB; **bắt buộc nếu Loại = Tư vấn viên**"
- `:1520` mục 5.2, **nhóm 4** — "File thẻ hành nghề \| tải 1 file \| PDF, tối đa 10MB" (không ghi điều kiện)

Cùng một trường, hai nhóm khác nhau, không có câu nào nói nó xuất hiện ở cả hai. Đây là **lỗi đặc tả**, không phải lỗi phần mềm → thuộc thẩm quyền BA.

## 4. Phép đo live (Chrome DevTools MCP)

**Môi trường:** `https://18.143.165.120.nip.io`, bản dựng **HTPLDN · V1.0.5**, 2026-08-03.
**Tài khoản:** `nht_qa_tw` / "QA NHT Trung uong" — `vaiTro:["NHT"]`, `capDonVi:"TW"`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp`, có quyền `register_tu_van_vien`. **Không dùng admin ra verdict.**

### 4.1 Cấu trúc nhóm 4 — đo bằng DOM (`innerText`, KHÔNG dùng `textContent`)

Cờ bắt buộc đọc từ **class `ant-form-item-required`**, không đọc từ chữ — vì dấu `*` của Ant Design là pseudo-element `::before`, `innerText` không bao giờ thấy. Đây chính là "phương pháp thứ hai" mà postmortem §4 yêu cầu.

| Loại = | Số mục trong nhóm 4 | Nhãn | `ant-form-item-required` |
|---|:-:|---|:-:|
| Chuyên gia (CG) | **1** | File đính kèm (Bằng cấp / Chứng chỉ) | `false` |
| Tư vấn viên (TVV) | **1** | File đính kèm (Bằng cấp / Chứng chỉ) | `false` |

Đối chứng cùng phép đo: "Lĩnh vực pháp luật" (`:1517`) trả `true` và ảnh chụp thấy rõ dấu `*` đỏ → phép đo đúng, dấu `*` CÓ render khi trường thật sự bắt buộc. Vậy mục 5.1 **thật sự** không được đánh dấu bắt buộc.

Cây trợ năng (a11y) xác nhận độc lập: mọi trường bắt buộc đều có node `StaticText "*"` đứng trước nhãn; nhãn "File đính kèm (Bằng cấp / Chứng chỉ)" **không có** node đó.

### 4.2 Mục 5.3 "Danh sách file đã tải" — upload file thật

Upload `bang-cap-qa-test.pdf` (PDF 1.4 hợp lệ, 620 B) vào nhóm 4 → nhóm 4 hiện thêm dòng: `bang-cap-qa-test.pdf` · `(620 B)` · nút `Xem` · nút `Xóa`. Đủ 4 thành phần SRS `:1521` yêu cầu.

- Nút **Xem** (click chuột thật qua MCP): mở PDF ở **tab mới** (`blob:https://18.143.165.120.nip.io/6736…`). SRS ghi "mở hộp xem PDF" — mở tab là cách hiện thực khác nhưng **đáp ứng đúng yêu cầu nghiệp vụ** (xem được PDF) → không log.
- Nút **Xóa** (click chuột thật qua MCP, không phải script): file bị gỡ **ngay lập tức**, `.ant-modal-wrap / .ant-popconfirm` đều rỗng → **không có bước xác nhận**, trái `:1521`. Đã đo 2 lần bằng 2 cách (script `.click()` và click chuột thật của MCP), kết quả giống nhau → không phải lỗi phép đo.

**SRS ghi "bảng"** còn web dựng dạng danh sách 1 dòng — khác kiểu UI nhưng đủ 4 thông tin yêu cầu; theo nguyên tắc "mô tả yêu cầu, không áp đặt cách hiện thực" → **không log**.

### 4.3 Ràng buộc bắt buộc của mục 5.1 — thử submit thật

Bộ bắt thông báo: dùng nguyên `tools/toast-capture.js` (không tự viết observer, không lọc trùng, đọc `innerText`, đếm request song song). **Tự kiểm trước khi tin số liệu: `soObserverDangSong = 1` ✅.**

**Lần 1 — điền đủ mọi trường bắt buộc khác, KHÔNG đính kèm gì cả:**

```
SO_REQUEST = 0   ·   SO_KHUNG_THONG_BAO = 1
chu = ["File thẻ hành nghề là bắt buộc đối với Tư vấn viên"]
BI_LAP = false   ·   URL vẫn là /chuyen-gia-tvv/tao-moi
```
→ Bị chặn ở client, **không tạo bản ghi rác**. Lưu ý: lỗi báo về **thẻ hành nghề** (nhóm 2), **không** nhắc gì tới Bằng cấp / Chứng chỉ.

**Lần 2 — nạp File thẻ hành nghề (nhóm 2), CỐ Ý để nhóm 4 rỗng:**

```
SO_REQUEST = 3
  POST  /api/v1/tu-van-viens
  POST  /api/v1/tu-van-viens/455f3047-b164-4b7c-a697-59e47e5db153/files
  PATCH /api/v1/tu-van-viens/455f3047-b164-4b7c-a697-59e47e5db153
SO_KHUNG_THONG_BAO = 1   ·   chu = ["Tạo hồ sơ TVV thành công"]
BI_LAP = false   ·   chuyển hướng sang /chuyen-gia-tvv/danh-sach
```

→ **Hồ sơ LƯU THÀNH CÔNG dù không có file Bằng cấp / Chứng chỉ.**

**Bản ghi đã tạo (dữ liệu test còn lại trên env):**

| Trường | Giá trị |
|---|---|
| Mã | **TVV-BTP-TW-0030** |
| Họ tên | QA Kiểm Thử Nhóm 4 |
| id | `455f3047-b164-4b7c-a697-59e47e5db153` |
| Trạng thái | Mới đăng ký |
| Loại / Lĩnh vực | Tư vấn viên / Thuế |

**Xác minh bằng phương pháp thứ hai (API, chỉ để điều tra — verdict vẫn theo UI):**

```json
{
  "fileTheHanhNgheId": "52ad3345-9553-4ecd-9e70-720eba73f738",
  "fileDinhKems": [
    { "id": "52ad3345-9553-4ecd-9e70-720eba73f738", "tenFile": "bang-cap-qa-test.pdf", "kichThuoc": 620 }
  ]
}
```
File duy nhất trong hồ sơ chính **là** file thẻ hành nghề (`fileTheHanhNgheId` trùng `fileDinhKems[0].id`) → **không có file Bằng cấp / Chứng chỉ nào**, khớp đúng điều UI thể hiện. UI và API **không mâu thuẫn**.

### 4.4 Ảnh đã chụp VÀ đã mở đọc (postmortem A2)

| Ảnh | Đã đọc | Nội dung đọc được |
|---|:-:|---|
| `image/DKTGMLTVV_05-web-nhom4-truoc-upload.png` | ✅ | Nhóm "File đính kèm" chỉ 1 mục, nhãn **không có dấu `*`**; ngay bên trên là "**\*** Lĩnh vực pháp luật" có dấu sao đỏ (đối chứng); ngay bên dưới là nhóm "Ghi chú" — không còn mục nào khác trong nhóm 4 |
| `image/DKTGMLTVV_05-web-nhom4-sau-upload.png` | ✅ | Sau upload hiện dòng `bang-cap-qa-test.pdf` · `(620 B)` · `Xem` · `Xóa` |
| `image/DKTGMLTVV_05-web-submit-khong-dinh-kem.png` | ✅ | Sau khi bấm Lưu lần 1: vẫn ở `/tao-moi`, nhóm 4 rỗng, chưa lưu. (Ảnh không bắt kịp toast vì toast hiện ở đỉnh trang; bằng chứng quyết định là observer + `SO_REQUEST=0`) |
| `image/DKTGMLTVV_05-web-hoso-luu-thieu-bangcap.png` | ✅ | Hồ sơ TVV-BTP-TW-0030 "Mới đăng ký" đã tạo; nhóm "File đính kèm" chỉ có 1 file (thẻ hành nghề) |

### 4.5 Console + network

Console: **0 lỗi, 0 cảnh báo**. Network XHR/fetch: không có 4xx/5xx nào trong phiên (riêng `GET /api/v1/auth/me 401` là lần gọi trước khi đăng nhập, bình thường).

## 5. Verdict từng ý con (protocol §"1 case gộp nhiều lỗi con")

| # | Ý | Kết luận | Verdict |
|:-:|---|---|---|
| 1 | Nhóm 4 thiếu "Tệp thẻ hành nghề" (**chính là điều đối tác phản ánh**) | Đối tác quan sát **ĐÚNG**: nhóm 4 không có trường này. Nhưng chức năng **có tồn tại** ở nhóm 2, và SRS tự liệt kê trường này ở **cả** `:1508` (nhóm 2) lẫn `:1520` (nhóm 4) → mâu thuẫn nội tại của đặc tả, không phải lỗi phần mềm | **BA confirm** |
| 2 | Nhóm 4 có "Tệp bằng cấp / chứng chỉ" | Có, đúng `:1519` về mặt tồn tại + giới hạn file | Đạt |
| 3 | Mục 5.1 **không** được đánh dấu bắt buộc **và** hệ thống **không chặn** khi bỏ trống, dù `:1519` ghi "Bắt buộc khi Người hỗ trợ đăng ký ứng viên mới" — đã test đúng vai trò NHT, đúng luồng đăng ký ứng viên mới, hồ sơ vẫn tạo được | Sai clause SRS rõ ràng, không có nguồn nào mâu thuẫn | **Open** |
| 4 | Mục 5.3: nút "Xóa" gỡ file ngay, không xác nhận, trái `:1521` "Xóa: xác nhận trước khi xóa" | Sai clause SRS rõ ràng. Đo ở chế độ tạo mới (file chưa lưu) nên hậu quả thấp; ở chế độ **Chỉnh sửa** (cùng màn SCR-IV-02, file đã lưu) thì mới là mất dữ liệu thật — chưa đo được chế độ đó | **Open** (nhẹ) |
| 5 | Mục 5.3 "Danh sách file đã tải" | Có đủ tên file + kích thước + nút Xem + nút Xóa | Đạt |

**VERDICT TỔNG: `Open`** — theo protocol, có ≥1 ý Open thì verdict tổng là Open. Ý 1 (điều đối tác phản ánh) vẫn được nêu rõ trong note để BA chốt; **không** Reject cả case.

## 6. Vì sao KHÔNG chọn `Reject` như dev

Dev ghi P123 = `Reject` với lý lẽ "tệp Thẻ hành nghề đặt ở Nhóm 2 đúng SRS (mục 3.6)". Phần đó **đúng sự thật** nhưng **đọc thiếu**: SRS còn liệt kê chính trường ấy ở mục 5.2 nhóm 4 (`:1520`). Khi đặc tả tự mâu thuẫn thì không bên nào "sai" về thực tế — protocol §Verdict cấm dùng `Reject` cho bất đồng đặc tả, và việc chốt lại đặc tả là thẩm quyền BA chứ không phải dev.

Ngoài ra, dev Reject cả case đã che mất **một lỗi thật nằm ngay trong nhóm 4** (ý 3): ràng buộc bắt buộc của "Bằng cấp / Chứng chỉ" không được thực thi. Đây là lý do phải tự đo thay vì tin claim.

**Cột P giữ nguyên `Reject`** (cột của dev), QA chỉ ghi cột Q = `Open`.
