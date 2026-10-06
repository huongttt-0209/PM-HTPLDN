# BATCH PLAN — `Dopai = dev done` + `Trạng thái dev fix = Fixed`

Nguồn: sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab **`bug`** (gid 1714340219), đọc 2026-08-06.
Toàn tab 358 case → 45 case khớp bộ lọc → trừ 2 case **đã verify 2026-08-06** (`QLNDTVVCG_24`, `QLNDTVVCG_26`)
→ **43 case cần chạy**. Dữ liệu thô: [`loc-43-case.csv`](loc-43-case.csv).

> `LKHDG_12` / `LKHDG_16` cũng đã verify hôm nay nhưng **không nằm trong bộ lọc** — sau khi verify,
> `Trạng thái dev fix` của hai dòng đó đã đổi thành `In Progress` / `Reopen`, không còn là `Fixed`.
> Không phải trừ thêm.

43/43 đều `Trạng thái = Fail`, đều **có ảnh/video** và **có `Kết quả thực tế`** → khác hẳn đợt `N/R`
trước đó (đợt đó `Kết quả thực tế` rỗng 39/39). Triệu chứng đọc thẳng ở `Kết quả thực tế`,
`TKM phản hồi lần 1` chỉ bổ sung.

Phân bố: Tuần 3 = 35 · Tuần 2 = 6 · Tuần 4 = 2.

---

## Cảnh báo trước khi chạy

### 1. Bộ lọc bỏ sót 70 case dev cũng báo Fixed

`Trạng thái dev fix = Fixed` toàn tab = **115** case. Cắt thêm `Dopai = dev done` còn 45 (bỏ 2 case đã verify → 43 cần chạy). 70 case rơi ra:

| `Dopai` | Số case Fixed | Nên làm gì |
|---|:-:|---|
| `N/R` | 39 | Trùng đợt BATCH-PLAN `N/R` đã lập 2026-08-06 — chưa chạy test, không có bug để verify |
| `OSP` | 12 | Chưa rõ chủ việc — cần hỏi |
| `Open` | 10 | 🔴 Dev báo Fixed nhưng đối tác vẫn để **Open** — mâu thuẫn, giá trị verify **cao hơn** nhóm 43 |
| `bug` | 9 | 🔴 Tương tự — dev Fixed, đối tác vẫn coi là bug |

19 case `Open` + `bug` là chỗ hai bên đang **bất đồng**; nhóm `dev done` là chỗ hai bên **đã đồng thuận
dev xong**. Nếu mục tiêu là chốt nghiệm thu thì 43 case này đúng; nếu mục tiêu là gỡ tranh chấp thì nên
chạy 19 case kia trước.

### 2. Sáu case đã có chữ trong cột `Kết quả verify`

`QLTVV_02` (32) · `KTHSYCHTPL_11` (45) · `XNTGHTVV_03` (51) · `DGKQHTVV_01` (64) ·
`QLHSDNHTCP_03` (72) · `LBCKQTHCT_01` (335).

Chữ trong đó là **triệu chứng vòng 2 của đối tác**, không phải verdict QA (5/6 case có `Trạng thái 2 = Fail`).
QA ghi verdict vào cột này sẽ **đè mất**. Nội dung đó phần lớn đã lặp ở `TKM phản hồi lần 2` nên mất mát thấp —
nhưng phải xác nhận trước, không tự đè.

Lưu ý thêm: 5/6 case có `Trạng thái dev fix 2 = dev done` ⇒ dev đã fix **vòng 2** sau khi đối tác báo Fail lại.
Đo trên bản dựng mới nhất mới có nghĩa.

### 3. Chốt môi trường trước khi chạy

Đợt verify LKHDG hôm nay chạy trên `https://18.143.165.120.nip.io` (bản dựng V1.0.8, env nội bộ) và tự ghi chú
*"chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu"*. Env nghiệm thu thật là
`htpldn-uat.ospgroup.vn`. **Pass ở env nào chỉ có hiệu lực ở env đó** — chọn sai env thì cả 43 verdict phải chạy lại.

### 4. 23/43 case là cùng một câu triệu chứng

`Hệ thống hiển thị thông báo "Không thể tạo file xuất. Vui lòng thử lại."` — 23 case, 22 màn báo cáo khác nhau,
cùng luồng *menu "Báo cáo thống kê" → nhập tiêu chí → [Xem báo cáo] → [Xuất excel]*. Nhiều khả năng **một
nguyên nhân gốc** ở dịch vụ xuất tệp, nhưng vẫn phải **đo từng case** — mỗi báo cáo là một endpoint riêng,
sửa được cái này không suy ra sửa được cái kia.

Bar Pass cho nhóm này: **mở tệp đọc nội dung**, không dừng ở "tải được tệp"/"HTTP 200".
Chrome của MCP chạy `--isolated` có thể không đổ tệp về `~/Downloads` → dự phòng: giải nén zip xlsx ngay trong trang.
Với báo cáo thống kê còn có **cache phía máy chủ** → đổi `denNgay` 1 ngày để lấy khoá cache mới, tránh đọc số cũ rồi chấm Fail oan.

---

## 8 batch — 43 case

| Batch | Chủ đề | Số case | Màn | Ghi chú |
|---|---|:-:|:-:|---|
| B1 | BC vụ việc — lỗi **nội dung** + lỗi xuất tệp | 6 | 3 | nặng nhất, phải đối chiếu số liệu |
| B2 | BC vụ việc — chỉ lỗi xuất tệp | 5 | 5 | lặp |
| B3 | BC chi phí hỗ trợ (`CP*`) — xuất tệp | 5 | 4 | có 1 case xuất **PDF** |
| B4 | BC chi trả (`CT*`, `SLCTHT`) — xuất tệp | 4 | 4 | lặp |
| B5 | BC đào tạo / tư vấn / hoạt động — xuất tệp | 6 | 6 | lặp |
| B6 | Vụ việc HTPL | 5 | 1 menu | cần seed trạng thái + kiểm thông báo |
| B7 | Tư vấn + Mạng lưới tư vấn viên | 6 | 3 menu | gộp, cùng vai trò CB nghiệp vụ |
| B8 | Lẻ — DN / Chi trả / Biểu mẫu / Đào tạo / Đợt BC | 6 | 5 menu | mỗi case 1 màn |
| | **Tổng** | **43** | | |

---

### B1 — Báo cáo thống kê vụ việc, có lỗi nội dung (6 case / 3 màn)

Ghép cặp theo màn: mỗi màn có 1 case lỗi hiển thị-số liệu + 1 case lỗi xuất tệp ⇒ vào màn 1 lần đo được cả 2.

| row | Mã TC | Triệu chứng |
|---|---|---|
| 178 | VVDTN_04 | Không hiển thị biểu đồ tròn theo lĩnh vực; bảng tổng hợp thiếu cột Theo kênh, Theo lĩnh vực *(TKM retest 31/7: vẫn thiếu biểu đồ tròn)* |
| 179 | VVDTN_06 | Không thể tạo file xuất |
| 183 | VVDHT_01 | Đơn vị có dữ liệu nhưng chọn người hỗ trợ → *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* *(TKM retest 28/7: chưa fix)* |
| 185 | VVDHT_06 | Không thể tạo file xuất |
| 193 | VVTTG_01 | Số liệu sai — *BC Vụ việc đã tiếp nhận > BC theo thời gian dù cùng khoảng thời gian* |
| 195 | VVTTG_05 | Không thể tạo file xuất |

⚠️ VVTTG_01 phải đo bằng cách **so hai báo cáo cùng kỳ** (đã tiếp nhận vs theo thời gian), không đo một mình.

### B2 — Báo cáo thống kê vụ việc, chỉ lỗi xuất tệp (5 case / 5 màn)

| row | Mã TC |
|---|---|
| 189 | VVDHTHT_06 |
| 222 | VVTDVQL_06 |
| 226 | VVTLV_05 |
| 230 | VVTLHDN_05 |
| 234 | VVTTGCT_05 |

### B3 — Báo cáo chi phí hỗ trợ (5 case / 4 màn)

| row | Mã TC | Ghi chú |
|---|---|---|
| 238 | CPHTCT_06 | |
| 243 | CPCTHTTDVQL_06 | |
| 258 | CPCTHTTLHDN_06 | |
| 263 | CPCTHTTTG_05 | Xuất **excel** |
| 264 | CPCTHTTTG_06 | Xuất **PDF** — cùng màn với case trên, khác nút |

### B4 — Báo cáo chi trả (4 case / 4 màn)

| row | Mã TC |
|---|---|
| 267 | SLCTHT_06 |
| 272 | CTTDVQL_04 |
| 277 | CTTLV_05 |
| 281 | CTTTG_04 |

### B5 — Báo cáo đào tạo / tư vấn / hoạt động (6 case / 6 màn)

| row | Mã TC |
|---|---|
| 174 | SLHDVM_06 |
| 200 | CLDTBDDDR_06 |
| 205 | LDTBDDDR_06 |
| 210 | CGTVPL_06 |
| 214 | DGHQHTPL_06 |
| 218 | CLDTBDPL_06 |

### B6 — Vụ việc HTPL (5 case / cùng menu "Vụ việc HTPL")

| row | Mã TC | Triệu chứng | Tiền đề cần dựng |
|---|---|---|---|
| 45 | KTHSYCHTPL_11 | Hiện nút **[Kiểm tra lại]** thay vì **[Hoàn tất kiểm tra]** *(`Kết quả verify` cũ: không chuyển trạng thái hồ sơ)* | hồ sơ ở "Đang kiểm tra" |
| 50 | TKHSYCHTPL_03 | Lọc Mức SLA = "Sắp hết hạn" → báo lỗi | hồ sơ có SLA sắp hết hạn |
| 51 | XNTGHTVV_03 | Bấm [Từ chối] → 403 *"Vụ việc không được phân công cho bạn"* dù đã phân công | vụ việc phân công cho chính TVV đăng nhập |
| 62 | CNKQHT_07 | Cập nhật kết quả xong, CBNV **không nhận thông báo** | vụ việc đang hỗ trợ + 2 tài khoản để đối chiếu chuông |
| 64 | DGKQHTVV_01 | Nhóm 8 – Đánh giá không có nút chức năng *(TKM retest 27/7: vẫn chưa có)* | vụ việc ở trạng thái cho phép đánh giá |

⚠️ 62 và 64 phải **đăng nhập tài khoản người nhận** để kiểm thông báo — không kết luận từ màn người gửi.

### B7 — Tư vấn + Mạng lưới tư vấn viên (6 case / 3 menu)

Gộp từ hai nhóm cũ sau khi `QLNDTVVCG_24` + `_26` rời phạm vi (đã verify 2026-08-06).
Cùng vai trò CB nghiệp vụ ⇒ một phiên đăng nhập chạy hết.

**Tư vấn** — menu *Tư vấn → Tư vấn chuyên sâu* / *Tư vấn nhanh*

| row | Mã TC | Triệu chứng |
|---|---|---|
| 299 | QLTLPLCVV_15 | Tải tệp chứa mã độc → báo *"Tải file thất bại"* thay vì thông báo phát hiện mã độc |
| 300 | QLTLPLCVV_17 | Nút [Xem] tệp bị disable |
| 305 | QLKCHTV_37 | Tư vấn nhanh — màn không có nút [Xuất Excel] *(TKM retest 3/8: vẫn chưa có; DEV đã nhận và hứa sửa theo đặc tả)* |

**Mạng lưới tư vấn viên** — menu *Mạng lưới tư vấn viên → Tư vấn viên/Chuyên gia*

| row | Mã TC | Triệu chứng |
|---|---|---|
| 32 | QLTVV_02 | Cột Điểm ĐG tràn/đè cột Trạng thái · hiển thị không đồng nhất (`-/5` vs số sao) · nút Xem/Sửa xuống dòng · không mặc định sắp theo ngày công nhận mới nhất *(TKM retest 3/8: vẫn tràn cột)* |
| 36 | CNHSNLTVV_03 | Cập nhật năng lực → *"Lỗi hệ thống, vui lòng thử lại sau"* *(DEV đã verify E2E Pass trên server 120 V1.0.6 ngày 04/08)* |
| 37 | CNDSMLTVV_01 | [Công khai hàng loạt] không mở cửa sổ nhập mô tả, bắn thẳng *"Mô tả công khai là bắt buộc..."* |

⚠️ **299 nhiều khả năng KHÔNG phải bug** — chức năng quét mã độc trên env chưa bật (tiền lệ: upload EICAR
vẫn `trangThaiQuet=SACH`). Nếu đúng vậy thì đây là ca **cần BA chốt phạm vi**, không phải Pass/Reopen.
⚠️ 305: dev đã tự nhận còn thiếu ⇒ gần như chắc **Reopen**, đo nhanh để xác nhận rồi chuyển lại dev.

### B8 — Lẻ, mỗi case một màn (6 case / 5 menu)

| row | Mã TC | Menu | Triệu chứng |
|---|---|---|---|
| 291 | QLHSPLDN_06 | Doanh nghiệp → Hồ sơ pháp lý DN | Không có nút xem chi tiết |
| 292 | QLHSPLDN_07 | Doanh nghiệp → Hồ sơ pháp lý DN | Báo cập nhật thành công nhưng dữ liệu không đổi |
| 72 | QLHSDNHTCP_03 | Chi trả chi phí | Cột "Mức cảnh báo thời hạn" tràn sang cột "Ngày nộp" |
| 138 | QLBMHD_02 | Biểu mẫu → Danh sách biểu mẫu | Thiếu ô tích chọn + thiếu cột Cơ quan ban hành, Định dạng |
| 20 | QLLKHDTBD_09 | Đào tạo, tập huấn → Kế hoạch đào tạo | Xuất Excel ra toàn bộ danh sách thay vì theo bộ lọc; thiếu cột Người tạo, Ngày tạo |
| 335 | LBCKQTHCT_01 | Đợt báo cáo | 403 `ERR-AUTH-VPD-00-02` dù đơn vị đã trong phạm vi; không chuyển trạng thái "Đang lập" |

⚠️ 291 và 292 dùng chung màn ⇒ chạy liền nhau.
⚠️ 138: DEV đã trả lời *"màn không được thiết kế ô tích chọn từng dòng"* + TKM ghi cần chị `anhduong16.work@gmail.com`
xác nhận ⇒ vế "ô tích chọn" là **cần BA**, vế "thiếu cột Cơ quan ban hành / Định dạng" mới là bug đo được.
Một phiếu **hai vế hai kết luận** — ghi đa trạng thái, đừng ép về một.
⚠️ 20: bar Pass là **mở tệp đếm dòng + đối chiếu tập mã với màn sau khi lọc**, giống đúng bài LKHDG_12 hôm nay.

---

## Prompt chạy từng batch

Đổi dòng `Phạm vi:` theo bảng trên; các dòng khác giữ nguyên.

```
Áp dụng @flows/04-verify-bug-dev-fix-khong-ho-so.md
- Bảng: https://docs.google.com/spreadsheets/d/1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s | Tab: bug (gid 1714340219)
- Ô mã case: "Mã TC" | Ô trạng thái dev: "Trạng thái dev fix" + "Dopai" (chỉ ĐỌC)
  | Ô kết quả QA: "<CHỐT TRƯỚC — xem cảnh báo §2>" | Ô note: "<...>"
- Từ vựng: đã fix="Fixed" · Pass="<...>" · Reopen="<...>" · không phải lỗi="<...>" · cần BA="<...>"
- Triệu chứng đọc ở "Kết quả thực tế" (43/43 case đều có), bổ sung bằng "TKM phản hồi lần 1"
  và "Kết quả verify" (chỗ nào có chữ thì đó là retest vòng 2 của đối tác, KHÔNG phải verdict QA).
- Đặc tả: Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/
  | Môi trường + tài khoản: output/UAT_doi-tac/input/input.md
- MÔI TRƯỜNG VERIFY: <CHỐT TRƯỚC — xem cảnh báo §3>
- Bug report: output/UAT_doi-tac/batch-devdone-fixed-2026-08-06/<batch>/bug-report.md
  | Ảnh: output/UAT_doi-tac/batch-devdone-fixed-2026-08-06/<batch>/image/
- File gửi BA: output/UAT_doi-tac/batch-devdone-fixed-2026-08-06/<batch>/cau-hoi-BA.md
- Thư mục tiêu chí: output/UAT_doi-tac/batch-devdone-fixed-2026-08-06/<batch>/tieuchi/
- Công cụ: tải bằng chứng=cd output/UAT_doi-tac && UAT_TAB=bug python3 tools/fetch_evidence.py --row <N>
- Phạm vi: <dán danh sách "Mã TC (row N)" của batch>
```

Ba slot `Ô kết quả QA` · `Ô note` · `MÔI TRƯỜNG VERIFY` phải điền trước khi chạy thật — flow 04 dừng hỏi nếu thiếu.
