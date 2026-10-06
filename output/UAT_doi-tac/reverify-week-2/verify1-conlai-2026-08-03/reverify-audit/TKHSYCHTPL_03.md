# Audit verify vòng 1 — TKHSYCHTPL_03 (row 129, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

| Mục | Giá trị |
|---|---|
| **Mã TC** | `TKHSYCHTPL_03` — "Tìm kiếm bộ lọc có kết quả" |
| **Chức năng** | Tìm kiếm / lọc danh sách hồ sơ vụ việc — `FR-V.I-08 (UC58)`, màn `SCR-V.I-01` |
| **Verdict QA vòng 1** | **`Pass`** (cột Q `Verify`) — cột P `Trạng thái dev fix 1` giữ nguyên `dev done`, KHÔNG đụng |
| **Tài khoản thực dùng** | `cbnv_tw_03` / `Test@1234` — `CB_NV_TW`, `capDonVi: TW`, `donViId: 00000000-0000-4000-8000-000000000001` (BTP · TW). Không phải fallback, đăng nhập lần đầu OK |
| **Môi trường QA** | `https://18.143.165.120.nip.io/` — bản dựng **`HTPLDN · V1.0.5`** |
| **Môi trường đối tác (từ bằng chứng)** | `htpldn-uat.ospgroup.vn` — bản dựng **`HTPLDN · V1.0.2`** |
| **Ngày verify** | 2026-08-03 |
| **Bảng điều kiện** | [`cond/TKHSYCHTPL_03.md`](../cond/TKHSYCHTPL_03.md) — **0 GAP** |
| **Note gửi đối tác** | [`notes/TKHSYCHTPL_03.txt`](../notes/TKHSYCHTPL_03.txt) |

---

## Note dev trước khi QA đè (2026-08-03)

> **Cột R (`DEV phản hồi lần 1`) TRỐNG — dev KHÔNG giải trình gì.**
> Cột P (`Trạng thái dev fix 1`) chỉ ghi `dev done`. Đây là **CLAIM, không phải bằng chứng** — không nêu sửa gì, sửa ở đâu, bản dựng nào.
> QA đã test độc lập, không dựa vào claim này để ra verdict. Toàn bộ kết luận dưới đây dựa trên phép đo do QA tự chạy trên bản `V1.0.5`.
> Sau khi QA ghi verdict, cột R sẽ mang nội dung QA viết (note partner-facing) — không có nội dung dev nào bị xoá vì cột vốn trống.

---

## Cổng 1 — Bằng chứng đối tác (đã mở xem full-res)

- **File:** `partner-evidence/TKHSYCHTPL_03.webm` (video ~8 giây, 1920×1080).
- **Frame đã trích:** `frames/TKHSYCHTPL_03/` — 16 frame, bước 0,5 giây (thêm 5 frame bước 2 giây).
- **Frame chứa LỖI:** `t002.58s.jpg` → `t008.00s.jpg` (khung thông báo lỗi xuất hiện từ giây ~2,5 và **còn nguyên tới hết video** ⇒ loại `notification`, không tự tắt). Frame đọc rõ nhất: **`t004.12s.jpg`**.
- **Frame trước lỗi (baseline của đối tác):** `t000.00s.jpg`.

### 3 dữ kiện neo (ghi TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Nội dung đọc được từ khung hình full-res |
|---|---|---|
| (a) | URL / màn hình đối tác đang đứng | `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1` — màn "Vụ việc HTPL / Danh sách", vai trò góc phải "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW", bản dựng góc trái "HTPLDN · V1.0.2" |
| (b) | Bộ lọc đối tác đã chọn (đủ các ô) | Ô từ khóa **trống** · "Lĩnh vực PL" **trống** · "Đơn vị" **trống** · "Kênh tiếp nhận" **trống** · **"Mức SLA" = "Sắp hết hạn"** · "Bộ lọc nâng cao (3)" **đang thu gọn** (không mở ⇒ để nguyên mặc định) · tab đang chọn = **"Tất cả"** |
| (c) | Nguyên văn thông báo lỗi + số khung | **ĐÚNG 1 khung** thông báo đỏ, nguyên văn:<br>`mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG`<br>Bảng kết quả rỗng, hiện "Không tìm thấy hồ sơ phù hợp" |

**Dữ kiện phụ quan trọng từ `t000.00s.jpg` (trước khi lọc):** tab "Tất cả **56**" · "Đang xử lý 35" · "Chờ phê duyệt 2" · "Hoàn thành 14" · "Từ chối 5"; và **cột "Cảnh báo thời hạn" của 3 dòng đầu ghi rõ "Sắp hết hạn · còn 1 ngày LV" / "còn 0 ngày LV"**.
⇒ Dữ liệu bên đối tác **CÓ** bản ghi thuộc nhóm "Sắp hết hạn". Nên danh sách rỗng ở `t004.12s` **không phải** màn rỗng hợp lệ do thiếu dữ liệu, mà là hệ quả của việc yêu cầu bị từ chối.

---

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `partner-evidence/TKHSYCHTPL_03.webm`, frame chứa lỗi `frames/TKHSYCHTPL_03/t004.12s.jpg` (giây 4,12) — chọn "Mức SLA" = "Sắp hết hạn" thì hệ thống hiện 1 khung thông báo lỗi bằng tiếng Anh và trả về danh sách rỗng.
2. **Đối tác phản ánh CỤ THỂ:** *"Khi chọn Mức SLA là 'Sắp hết hạn' hệ thống hiển thị thông báo lỗi"* — tức không lấy được kết quả cho đúng một giá trị của bộ lọc, trong khi phiếu kỳ vọng "Có kết quả, hiển thị danh sách, phân trang 20 bản ghi/trang".
3. **Data + bước tái hiện:** vai trò CB_NV_TW đơn vị BTP·TW; dữ liệu có sẵn bản ghi mức "Sắp hết hạn"; bước: mở "Vụ việc HTPL" → tab "Tất cả" → ô "Mức SLA" chọn "Sắp hết hạn" → chạy tìm kiếm.

---

## Cổng 3 — Đối chiếu SRS vs thực tế web

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` (SRS chuẩn, đã mở file đọc đúng dòng).

| # | SRS yêu cầu (dẫn dòng + trích nguyên văn) | Thực tế web (bản V1.0.5, QA tự đo) | Đạt? |
|---|---|---|:-:|
| 1 | `srs-fr-05-vu-viec.md:1644` — SCR-V.I-01 thành phần row 9: `\| 9 \| filter-bar \| Mức SLA \| C10 dropdown \| BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG \| change → filter \| Luôn \|` | Ô "Mức SLA" tồn tại trên thanh lọc, mở ra đúng **4** lựa chọn: "Bình thường", "Sắp hết hạn", "Quá hạn", "Quá hạn nghiêm trọng" | ✅ |
| 2 | `srs-fr-05-vu-viec.md:1516` — bảng ánh xạ mã DB → nhãn UI: `\| `SAP_HET` \| Sắp hết hạn \| Vàng \|` | Nhãn hiển thị "Sắp hết hạn"; giá trị FE gửi lên là `SAP_HET` (đọc từ query string `?mucSla=SAP_HET`) — khớp mã DB | ✅ |
| 3 | `srs-fr-05-vu-viec.md:87` — FR-V.I-01 (UC51): "Hỗ trợ tìm kiếm, lọc theo trạng thái, lĩnh vực, kênh tiếp nhận, **mức SLA**" | Lọc theo mức SLA chạy được, cả 4 giá trị đều trả kết quả | ✅ |
| 4 | `srs-fr-05-vu-viec.md:636` — FR-V.I-08 (UC58) §Processing bước 4: `\| 4 \| Phân trang (20/trang) \| BR-DATA-07 \|` | Chân bảng ghi "Hiển thị 1-20 / 37 kết quả", ô kích thước trang mặc định "20 / trang" | ✅ |
| 5 | `srs-fr-05-vu-viec.md:636` — FR-V.I-08 §Error Handling E1: `\| E1 \| Không có kết quả \| INF-VV-TK-01 \| "Không tìm thấy hồ sơ phù hợp" \| INFO \|` | Giá trị "Quá hạn nghiêm trọng" (0 bản ghi) hiện đúng màn rỗng "Không tìm thấy hồ sơ phù hợp", mức INFO, **không** kèm khung lỗi | ✅ |
| 6 | `srs-fr-05-vu-viec.md:2031` — ràng buộc DB: `\| muc_do_canh_bao \| text \| N \| CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') \| 'BINH_THUONG' \| Mức cảnh báo SLA \|` | Bản ghi trả về mang `mucDoCanhBao: "SAP_HET"` — nằm trong tập CHECK | ✅ |

---

## Phép đo phân biệt — 5 phép đo trên cùng 1 phiên (GATE bằng chứng real-data)

**Cách đo:** vai trò `cbnv_tw_03`, màn "Vụ việc HTPL", tab "Tất cả", các ô lọc khác để trống. Mỗi lần: cài lại [`tools/toast-capture.js`](../../../tools/toast-capture.js) (tự kiểm `soObserverDangSong = 1` ✅) → chọn giá trị trong ô "Mức SLA" → bấm **[Tìm kiếm]** → chụp màn hình NGAY → đợi 3 giây rồi đọc số khung thông báo + số bản ghi.

| # | Phép đo | Giá trị FE gửi lên (query string) | HTTP | Số bản ghi thực | Số khung thông báo lỗi | Ảnh QA tự chụp |
|---|---|---|:-:|:-:|:-:|---|
| 0 | **Baseline — không lọc** | `?page=1&pageSize=20` | 200 | **37** ("Hiển thị 1-20 / 37 kết quả") | 0 | `image/BUG-TKHSYCHTPL_03-01-baseline-khong-loc-37-ket-qua.png` |
| 1 | Lọc **"Bình thường"** | `?mucSla=BINH_THUONG&page=1&pageSize=20` | 200 | **30** | 0 | `image/BUG-TKHSYCHTPL_03-02-loc-Binh-thuong-30-ket-qua.png` |
| 2 | Lọc **"Sắp hết hạn"** ← giá trị đối tác phản ánh | `?mucSla=SAP_HET&page=1&pageSize=20` | 200 | **2** (`VV-BTP-TW-20260712-006`, `-005`) | **0** — không có khung lỗi, không có nội dung lỗi nào | `image/BUG-TKHSYCHTPL_03-03-loc-Sap-het-han-ngay-sau-khi-bam-Tim-kiem.png` |
| 3 | Lọc **"Quá hạn"** | `?mucSla=QUA_HAN&page=1&pageSize=20` | 200 | **5** | 0 | `image/BUG-TKHSYCHTPL_03-04-loc-Qua-han.png` |
| 4 | Lọc **"Quá hạn nghiêm trọng"** | `?mucSla=QUA_HAN_NGHIEM_TRONG&page=1&pageSize=20` | 200 | **0** + màn rỗng hợp lệ "Không tìm thấy hồ sơ phù hợp" | 0 | `image/BUG-TKHSYCHTPL_03-05-loc-Qua-han-nghiem-trong.png` |

**Kiểm tra cộng dồn:** `30 + 2 + 5 + 0 = 37` = đúng baseline ⇒ 4 nhóm chia hết tập dữ liệu, không sót và không đếm trùng bản ghi nào.

**Kết luận của phép đo phân biệt:** KHÔNG giá trị nào gây lỗi ⇒ loại bỏ cả hai giả thuyết "chỉ hỏng riêng giá trị Sắp hết hạn" và "hỏng toàn bộ bộ lọc". Nhánh còn lại: **đã được sửa**.

---

## Phương pháp đo thứ hai (bug candidate ≠ bug) — gọi thẳng dịch vụ danh sách

Gọi trực tiếp cùng một dịch vụ danh sách bằng phiên đăng nhập của chính `cbnv_tw_03`, thử **cả hai biến thể tên mã** để cô lập nguyên nhân:

| Tham số gửi lên | HTTP | `meta.total` | Mã lỗi / thông điệp trả về |
|---|:-:|:-:|---|
| (không có `mucSla`) | 200 | 37 | — |
| `mucSla=BINH_THUONG` | 200 | 30 | — |
| **`mucSla=SAP_HET`** | **200** | **2** | — (bản ghi trả về có `mucDoCanhBao: "SAP_HET"`) |
| **`mucSla=SAP_HET_HAN`** | **422** | — | `ERR-VAL-SYS-00-01`, field `mucSla`, message `mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG` |
| `mucSla=QUA_HAN` | 200 | 5 | — |
| `mucSla=QUA_HAN_NGHIEM_TRONG` | 200 | 0 | — |
| `mucSla=` (rỗng) | 422 | — | cùng mã `ERR-VAL-SYS-00-01`, cùng thông điệp |

**Hai phương pháp KHÔNG mâu thuẫn:** số bản ghi giao diện (37 / 30 / 2 / 5 / 0) khớp tuyệt đối với `meta.total` của lời gọi trực tiếp.

**Điểm chốt nguyên nhân:** thông điệp trả về khi gửi `SAP_HET_HAN` **trùng khít từng ký tự** với thông báo trong khung hình bằng chứng của đối tác. Máy chủ **không đổi hành vi** (vẫn từ chối `SAP_HET_HAN`). Thứ đã đổi là **giao diện**: bản `V1.0.2` gửi `SAP_HET_HAN`, bản `V1.0.5` gửi `SAP_HET`. ⇒ Bản vá nằm ở phía giao diện, và nó thật sự giải quyết đúng lỗi đối tác báo — không phải "không tái hiện được vì môi trường khác".

**Đối chứng bổ sung:** mở thẳng đúng địa chỉ cũ của đối tác `.../vu-viec/danh-sach?mucSla=SAP_HET_HAN&page=1` trên bản V1.0.5 → giao diện vẫn chuyển tiếp giá trị hỏng đó và nhận 422, danh sách rỗng (ảnh `image/BUG-TKHSYCHTPL_03-06-mo-thang-URL-cu-SAP_HET_HAN-cua-doi-tac.png`). Đây là **địa chỉ tự gõ/đánh dấu trang từ bản cũ**, không phải thao tác của người dùng trên giao diện hiện tại (ô "Mức SLA" không còn sinh ra giá trị này) ⇒ không tính là lỗi của case, chỉ ghi lại để dev biết.

---

## Kiểm tra chống "phép đo nói dối" (theo QA_POSTMORTEM §4)

| Dấu hiệu cần loại trừ | Kết quả kiểm |
|---|---|
| Bộ đo tự lọc trùng | Dùng nguyên `tools/toast-capture.js` dùng chung, **không** lọc trùng, **không** tự viết observer mới |
| Đọc chữ bằng `textContent` (gom node ẩn) | Bộ đo dùng `innerText`; các số liệu bảng cũng đọc bằng `innerText` |
| Observer bị nhân bản → đếm bội | Chạy tự kiểm chèn node giả: `soObserverDangSong = 1` (hợp lệ) ở **cả 2 lần** cài (trước loạt đo và sau khi tải lại trang) |
| Kết luận 100% từ mã lệnh, không có ảnh | 8 ảnh QA tự chụp, **đã mở đọc từng ảnh** bằng công cụ đọc ảnh, đối chiếu tên file ↔ nội dung ↔ kết luận |
| Tab mở lâu còn chạy mã cũ | Đã `navigate` tải lại **bỏ bộ nhớ đệm** rồi lặp lại phép đo "Sắp hết hạn": vẫn 2 bản ghi, 0 khung thông báo (ảnh `...-07-tai-lai-trang-loc-Sap-het-han-2-ket-qua.png`); bản dựng đọc lại từ giao diện = `HTPLDN · V1.0.5` |
| Bảng điều khiển trình duyệt có lỗi ngầm | `list_console_messages` (lọc error + warn): **không có thông điệp nào** |

---

## Mâu thuẫn tên mã trong SRS (đã tự mở file kiểm 3 dòng, KHÔNG tin số dòng do người khác cấp)

| Dòng SRS | Nội dung nguyên văn | Mã dùng |
|---|---|---|
| `:1449` | `\| SAP_HET_HAN \| ≤ 50% còn lại \| Thông báo CB NV \|` (bảng "4 mức cảnh báo (BR-SLA-02)" của FR-V.I-CROSS-01) | **`SAP_HET_HAN`** |
| `:1516` | `\| `SAP_HET` \| Sắp hết hạn \| Vàng \|` (bảng ánh xạ `VU_VIEC.muc_do_canh_bao` → nhãn UI) | **`SAP_HET`** |
| `:2031` | `\| muc_do_canh_bao \| text \| N \| CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG') \| ... \|` | **`SAP_HET`** |

**Kết luận: SRS CÓ mâu thuẫn thật.** Thêm 2 chỗ nữa cùng phe:
- `:1644` (bộ lọc SCR-V.I-01) và `:1656` (cột "Cảnh báo thời hạn") dùng `SAP_HET`.
- `:2430` (BR-SLA-03) dùng `SAP_HET_HAN`.
- Ngoài ra `:114` (Inputs FR-V.I-01 cũ) và `:87`→`:113` liệt kê `muc_sla` chỉ 3 giá trị `BINH_THUONG / SAP_HET / QUA_HAN`, **thiếu** `QUA_HAN_NGHIEM_TRONG` so với `:1644` và `:2031`.

**Vì sao KHÔNG chấm `BA confirm` dù SRS tự mâu thuẫn:** theo bảng Verdict của QA_VERIFY_PROTOCOL, `BA confirm` dùng khi kỳ vọng đối tác khác SRS, SRS silent, hoặc **SRS tự mâu thuẫn mà web vẫn chạy được nhưng chưa rõ đúng/sai**. Ở đây **phe `SAP_HET` là phe quyết định và đã thắng rõ ràng**: nó là ràng buộc dữ liệu (`:2031` CHECK), là mã ánh xạ ra nhãn UI (`:1516`), và là danh sách giá trị của **đúng bộ lọc đang tranh chấp** (`:1644`). Phần mềm hiện chạy đúng theo phe này và cho kết quả đúng nghiệp vụ. Mâu thuẫn còn lại chỉ nằm ở phần mô tả BR-SLA-02/03 (`:1449`, `:2430`) — không làm đổi kết luận của case này.

**Đề nghị BA dọn tài liệu (không chặn case, không cần trả lời trước khi đóng phiếu):**
1. Thống nhất một tên mã duy nhất cho mức "Sắp hết hạn" trong toàn bộ SRS — đề xuất giữ `SAP_HET` theo ràng buộc DB dòng `:2031`; sửa `:1449` và `:2430` cho khớp.
2. Bổ sung `QUA_HAN_NGHIEM_TRONG` vào danh sách giá trị `muc_sla` ở FR-V.I-01 dòng `:114` cho khớp `:1644` và `:2031`.

---

## Quan sát thêm ngoài tiêu chí phiếu (đã đọc ảnh, không suy đoán)

1. **Hai hồ sơ do bộ lọc "Sắp hết hạn" trả về đều đang hiển thị "Đã hoàn thành" ở cột "Cảnh báo thời hạn".**
   - Đo 2 chiều: giao diện hiện `Đã hoàn thành` cho cả 2 dòng; dữ liệu trả về có `mucDoCanhBao: "SAP_HET"`, `trangThai` lần lượt `TU_CHOI` và `HOAN_THANH`, `deadline` 31/07/2026 (đã qua so với ngày kiểm 03/08/2026), `ngayCapNhat` dừng ở 29/07/2026.
   - Tức mức cảnh báo bị **đóng băng tại thời điểm hồ sơ đóng**, không còn được cập nhật theo `BR-CALC-03` (`:2442` — công thức `(NOW() - ngay_tiep_nhan) / deadline * 100`, job chạy mỗi 30 phút).
   - ~~**Chưa mở dòng lỗi mới**~~ → **ĐÃ mở dòng `TKHSYCHTPL_OOS_01` (row 145) ngày 03/08/2026, verdict `BA confirm`** — xem mục "Dòng TC mở thêm" ở cuối file. Lý do chọn `BA confirm` chứ không `Open`: SRS **không** quy định hồ sơ ở trạng thái kết thúc thì mức cảnh báo phải được xoá / đặt lại, và nhãn "Đã hoàn thành" cũng không nằm trong 4 mức ở `:1656` nhưng là quy ước hiển thị **có sẵn từ trước** (thấy cả trong khung hình `t000.00s.jpg` của chính đối tác, dòng `VV-BTP-TW-20260713-001`). Không trích được điều khoản SRS nào bị vi phạm ⇒ theo §Tự vấn bắt buộc, không được chấm `Open`.
2. **"Bộ lọc nâng cao (3)"** khi mở ra gồm đúng 3 mục: Trạng thái (chọn nhiều, mặc định thẻ "Tất cả"), Từ ngày, Đến ngày — khớp `SCR-V.I-01` row 7 + row 10. Không có gì bất thường (ảnh `...-08-bo-loc-nang-cao-mo-rong.png`).
3. Không phát hiện thông báo lặp (double toast) trong bất kỳ phép đo nào của case này: cả 4 lần bấm "Tìm kiếm" đều cho 0 khung thông báo.

---

## Danh sách ảnh QA tự chụp (đã mở đọc từng ảnh)

| # | Tên file (trong `bug-reports/vu-viec/image/`) | Nội dung đã đọc được từ pixel |
|---|---|---|
| 1 | `BUG-TKHSYCHTPL_03-01-baseline-khong-loc-37-ket-qua.png` | Ô "Mức SLA" trống, tab "Tất cả 37", tài khoản "CB Nghiệp vụ - Trung ương #03 · CB_NV_TW", đơn vị "BTP · TW", bản dựng "HTPLDN · V1.0.5" |
| 2 | `BUG-TKHSYCHTPL_03-02-loc-Binh-thuong-30-ket-qua.png` | Ô "Mức SLA" = "Bình thường", tab "Tất cả 30", không có khung thông báo |
| 3 | `BUG-TKHSYCHTPL_03-03-loc-Sap-het-han-ngay-sau-khi-bam-Tim-kiem.png` | Ô "Mức SLA" = "Sắp hết hạn", 2 dòng kết quả, "Hiển thị 1-2 / 2 kết quả", **không có khung thông báo lỗi** |
| 4 | `BUG-TKHSYCHTPL_03-04-loc-Qua-han.png` | Ô "Mức SLA" = "Quá hạn", tab "Tất cả 5", 5 dòng kết quả, không có khung thông báo |
| 5 | `BUG-TKHSYCHTPL_03-05-loc-Qua-han-nghiem-trong.png` | Ô "Mức SLA" = "Quá hạn nghiêm trọng", màn rỗng "Không tìm thấy hồ sơ phù hợp", không có khung thông báo |
| 6 | `BUG-TKHSYCHTPL_03-06-mo-thang-URL-cu-SAP_HET_HAN-cua-doi-tac.png` | Mở thẳng địa chỉ cũ của đối tác: ô "Mức SLA" hiện mã thô `SAP_HET_HAN`, danh sách rỗng |
| 7 | `BUG-TKHSYCHTPL_03-07-tai-lai-trang-loc-Sap-het-han-2-ket-qua.png` | Sau khi tải lại trang bỏ bộ nhớ đệm: "Sắp hết hạn" → 2 kết quả, không có khung thông báo |
| 8 | `BUG-TKHSYCHTPL_03-08-bo-loc-nang-cao-mo-rong.png` | "Bộ lọc nâng cao (3)" mở ra: Trạng thái "Tất cả", Từ ngày, Đến ngày |

*(Ảnh đặt chung thư mục `bug-reports/vu-viec/image/` theo quy ước co-locate của repo; case này verdict `Pass` nên KHÔNG mở entry trong `bug-report-vu-viec.md`.)*

> **Khai báo trung thực về ảnh trùng:** đã đối chiếu md5 cả 8 ảnh. Ảnh **#3 và #7 TRÙNG KHÍT byte-per-byte** (`71a75ee0e1b86768288160f4e18f7d48`). Đây **không phải** một ảnh dùng lại cho hai chú thích khác nhau — đó là **hai lần chụp riêng biệt** (lần 1 lúc 16:40, lần 2 lúc 16:43 sau khi tải lại trang bỏ bộ nhớ đệm), và chúng giống hệt nhau **vì kết quả của phép đo giống hệt nhau**: cùng 2 bản ghi, cùng dòng "Hiển thị 1-2 / 2 kết quả", cùng 0 khung thông báo, cùng bố cục màn hình. Tức bản thân sự trùng khít này chính là bằng chứng phép đo lặp lại được. 6 ảnh còn lại có md5 khác nhau đôi một.



---

## Vì sao KHÔNG mở entry bug-report

Verdict `Pass` ⇒ theo QA_VERIFY_PROTOCOL §"Open → bug-report", chỉ `Open` mới tạo entry bug-report. `Pass` chỉ cần lưu evidence audit — chính là file này + 8 ảnh + bảng điều kiện. Không có `BUG-TKHSYCHTPL_03`.

---

## Dòng TC mở thêm — `TKHSYCHTPL_OOS_01` (bổ sung 2026-08-03 17:47)

Quan sát #1 ở mục trên đã được mở thành **dòng TC riêng** (bug ngoài phạm vi case, theo QA_POSTMORTEM §3 "bug ngoài phạm vi case cũng PHẢI log").

| Mục | Giá trị |
|---|---|
| **Mã TC** | `TKHSYCHTPL_OOS_01` |
| **Vị trí** | **row 145**, tab `UAT_TGPL Doanh Nghiệp-tuần 2` (dòng trống kế tiếp — đã đọc sheet live xác nhận trước khi ghi, lưới 144 dòng → nới thêm 1) |
| **Verdict** | **`BA confirm`** (cột Q `Verify`). Cột P `Trạng thái dev fix 1` **để TRỐNG, không đụng** — cột của dev. Cột N `Trạng thái 1` = `Fail` |
| **Note partner-facing** | [`notes/TKHSYCHTPL_OOS_01.txt`](../notes/TKHSYCHTPL_OOS_01.txt) — đã ghi vào cột R `DEV phản hồi lần 1` |
| **Bảng điều kiện** | [`cond/TKHSYCHTPL_OOS_01.md`](../cond/TKHSYCHTPL_OOS_01.md) — **0 GAP**, mọi ô GAP ghi "Không" |
| **Ảnh bằng chứng** | [`bug-reports/vu-viec/image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png`](../bug-reports/vu-viec/image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png) |
| **Tài khoản thực dùng** | `cbnv_tw_03` / `Test@1234` (CB_NV_TW, BTP · TW, bản dựng `HTPLDN · V1.0.5`) — đăng nhập lần đầu OK, **không** fallback Rule 7 |
| **Audit log ghi sheet** | `tools/sheet_add_bug_row.log` — `ts=2026-08-03T17:47:31, row=145, ma_tc=TKHSYCHTPL_OOS_01, ok=true`, 13 ô `B/C/D/G/H/I/J/K/L/M/N/Q/R145` |

### Vì sao phải chụp lại ảnh (bài học — GATE bằng chứng)

8 ảnh của case gốc **KHÔNG chứng minh được** quan sát #1: chúng chụp ở bề rộng hẹp hơn nên cột "Cảnh báo thời hạn" (cột 21 theo `:1656`, đứng sau "Ngày tiếp nhận" / "Thời hạn xử lý") **nằm ngoài khung hình**. Chữ "Hoàn thành" đọc được trong 2 ảnh đó là ở cột **"Trạng thái"** — **khác cột**, và là "Hoàn thành" chứ không phải "Đã hoàn thành". Theo §GATE ("tên file ↔ nội dung ↔ claim lệch = INVALID") thì không được ghi sheet bằng bộ ảnh đó.

Ảnh mới chụp lại ở viewport **1920×1080**: đo trước khi chụp thấy cột cuối kết thúc ở x=1896 < 1920 và `document.scrollWidth == innerWidth == 1920` ⇒ **không cột nào bị cắt**, cột "Mã vụ việc" (x 314–485) và cột "Cảnh báo thời hạn" (x 1586–1768) **cùng lọt một khung hình**. Đã mở đọc pixel ảnh gốc 3840×1488 + crop vùng bảng để đọc chắc chữ trên nhãn.

### 2 phép đo trên dòng mới (đều khớp, không mâu thuẫn)

| Phép đo | Kết quả |
|---|---|
| **Giao diện** (ảnh đã đọc pixel) | Bộ lọc "Mức SLA" = "Sắp hết hạn" → "Hiển thị 1-2 / 2 kết quả". `VV-BTP-TW-20260712-006`: cột "Trạng thái" = "Từ chối" (nhãn đỏ), cột **"Cảnh báo thời hạn" = "Đã hoàn thành"** (nhãn xám). `VV-BTP-TW-20260712-005`: "Trạng thái" = "Hoàn thành" (nhãn xanh), cột **"Cảnh báo thời hạn" = "Đã hoàn thành"** |
| **Dữ liệu danh sách trả về** | `GET /api/v1/vu-viecs?mucSla=SAP_HET&page=1&pageSize=20` → HTTP 200, `total=2`. Cả 2 bản ghi `mucDoCanhBao: "SAP_HET"`; `trangThai` = `TU_CHOI` / `HOAN_THANH`; `ngayTiepNhan` 12/07/2026, `deadline` 31/07/2026 (đã qua so với ngày kiểm 03/08/2026); `ngayCapNhat` dừng ở 29/07/2026 và 24/07/2026 |

⇒ Không mâu thuẫn: bản ghi lọt bộ lọc vì giá trị lưu trữ vẫn là `SAP_HET`; nhãn "Đã hoàn thành" là cách giao diện hiển thị đè khi hồ sơ đã đóng.

### Căn cứ SRS cho verdict `BA confirm` (đã tự mở file kiểm từng dòng, không tin số dòng người khác cấp)

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md`.

| Dòng | Nội dung nguyên văn | Ý nghĩa cho case |
|---|---|---|
| `:636` | `### FR-V.I-08: Tìm kiếm hồ sơ (UC58)` — `**UC Reference:** UC 58`, `**Màn hình:** SCR-V.I-01` | Không nêu bộ lọc mức cảnh báo có loại trừ hồ sơ đã kết thúc hay không |
| `:1436` | `\| 2 \| Lấy danh sách VV đang hoạt động (DA_TIEP_NHAN, DANG_KIEM_TRA, DA_PHAN_CONG, DANG_XU_LY, CHO_PHE_DUYET) \| — \|` (FR-V.I-CROSS-01 §Processing) | **Job CỐ Ý loại `HOAN_THANH` / `TU_CHOI` khỏi phạm vi rà** ⇒ giá trị đóng băng là đúng phạm vi job, không phải job hỏng |
| `:1656` | `\| 21 \| table \| Cảnh báo thời hạn \| C07 \| 4 mức màu: 🟢 BINH_THUONG / 🟡 SAP_HET / 🔴 QUA_HAN / ⚫ QUA_HAN_NGHIEM_TRONG (80px) \| — \| Luôn \|` | Chỉ định nghĩa **4** mức — "Đã hoàn thành" KHÔNG có trong đó |
| `:2442` | `Mức cảnh báo tính theo công thức \`(NOW() - ngay_tiep_nhan) / deadline * 100\`. Scheduled job CROSS-01 chạy mỗi 30 phút để cập nhật mức cảnh báo VU_VIEC theo BR-SLA-02.` (BR-CALC-03, heading ở `:2440`) | Chỉ nêu công thức + chu kỳ, **silent** về giá trị còn sót của hồ sơ đã đóng |

**Grep xác nhận SRS silent:** `grep "Đã hoàn thành" srs-fr-05-vu-viec.md` → **0 hit**; `grep -E "đặt lại mức cảnh báo\|xoá cảnh báo\|xóa cảnh báo\|reset cảnh báo\|dừng cảnh báo\|ngừng cảnh báo"` → **0 hit**.

⇒ Không trích được điều khoản nào bị vi phạm ⇒ theo bảng Verdict (`BA confirm` = "SRS/BA silent") thì **KHÔNG được chấm `Open`**. 3 câu hỏi cụ thể gửi BA nằm trong note partner-facing.

**Không phải hồi quy do bản vá:** hiện tượng đã có từ trước lần sửa bộ lọc "Mức SLA" — quan sát được ngay trong khung hình `t000.00s.jpg` của bản dựng cũ (dòng `VV-BTP-TW-20260713-001` cũng mang nhãn "Đã hoàn thành" ở cột này). Đã nêu rõ trong note để BA không hiểu nhầm là lỗi mới.

---

*Audit generated: 2026-08-03 | QA Automation via Claude Code + Chrome DevTools MCP*
