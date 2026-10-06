# BRIEF LÔ G3 — Verify lại 7 case dev đã fix, trên MÔI TRƯỜNG NGHIỆM THU ĐỐI TÁC

> Mọi agent trong lô này ĐỌC FILE NÀY TRƯỚC. Không lặp lại luật ở đây trong prompt con.

## 1. Tham số đợt (prompt user cấp — không tự đổi)

| Tham số | Giá trị |
|---|---|
| **Môi trường đo** | `https://htpldn-uat.ospgroup.vn/login` — **env NGHIỆM THU của đối tác**. TUYỆT ĐỐI KHÔNG đo trên `18.143.165.120.nip.io` (env nội bộ). |
| MailHog của env này | `https://htpldn-uat.ospgroup.vn/mailhog/` · API `…/mailhog/api/v2/messages?limit=5` |
| Sheet | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** · gid **1714340219** |
| SRS nguồn chuẩn DUY NHẤT | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` |
| Tài khoản | `output/UAT_doi-tac/input/input.md` §"Môi trường NGHIỆM THU của đối tác" |
| Thư mục lô | `output/UAT_doi-tac/reverify-week-5/G3-uatdoitac-7case-2026-08-07/` |

## 2. Phạm vi — 7 case, dòng đã xác định

| # | Mã TC | Dòng | Tuần | Mô tả | `Trạng thái dev fix` hiện tại | `Kết quả verify` hiện tại |
|---|---|---|---|---|---|---|
| 1 | KTDGKQHT_10 | **11** | 2 | Tải lên tệp Excel Kết quả kiểm tra | `Test done` | **TRỐNG** |
| 2 | QLKTLBG_18 | **12** | 2 | Xuất Excel với điều kiện lọc | `Test done` | **TRỐNG** |
| 3 | QLKTLBG_19 | **13** | 2 | Xuất excel không có điều kiện lọc | `Test done` | đã có (đo env NỘI BỘ) |
| 4 | QLKTLBG_20 | **14** | 2 | Xuất Excel với điều kiện lọc không có kết quả | `Test done` | đã có (đo env NỘI BỘ) |
| 5 | CNHSNLTVV_03 | **36** | 2 | Lưu thành công khi nhập dữ liệu hợp lệ (năng lực TVV) | `Test done` | đã có (đo env NỘI BỘ) |
| 6 | KTHSYCHTPL_11 | **45** | 2 | Nút "Hoàn tất kiểm tra" khi kết luận Đạt | `Test done` | đã có (đo env NỘI BỘ) |
| 7 | TKHSYCHTPL_03 | **50** | 2 | Tìm kiếm bộ lọc có kết quả (Mức SLA "Sắp hết hạn") | `Test done` | đã có (đo env NỘI BỘ) |

**Ý nghĩa:** 5/7 case đã Pass ở env nội bộ nhưng ghi chú cũ **tự nêu giới hạn** "chỉ có hiệu lực cho env nội bộ,
đề nghị xác nhận lại khi bản dựng lên môi trường nghiệm thu". Lô G3 chính là lượt xác nhận đó → **phải đo lại
thật trên env đối tác**, cấm chép kết luận cũ.

## 3. Pre-flight đã chạy (kết quả thật, 07/08/2026 ~16:20)

- `GET /login` → HTTP 200. Bó mã FE: **`assets/index-Bd1akG3f.js`**, `Last-Modified: Fri, 07 Aug 2026 08:15:32 GMT`
  (= **15:15 giờ VN cùng ngày**). Khác bó mã env nội bộ (`index-D4Buvu4S.js`) → **bản dựng khác, phải tự đọc lại
  số hiệu bản dựng trên UI khi đo, không suy từ env nội bộ.**
- Env này **CÓ bước nhập mã xác thực (OTP)**. Đã kiểm chứng thật:
  `POST /api/v1/auth/login` body `{"username":..., "password":...}` → trả `otpToken`; lấy mã 6 số ở MailHog của
  chính env → `POST /api/v1/auth/verify-otp` body `{"otpToken":..., "otpCode":...}` → trả `accessToken` + set cookie.
  (Ghi nhớ cũ nói "env đối tác không cần OTP" là **SAI** với bản hiện tại — bỏ qua ghi nhớ đó.)
- `cbnv_tw` / `Test@1234` **đăng nhập được**, `vaiTro=["CB_NV_TW"]`, `donViId=…8000-000000000001`, `capDonVi=TW`.
- `GET /api/docs-json` mở được không cần auth (624 path) — dùng để tra endpoint khi cần.
- Giới hạn đăng nhập **5 lượt / 60 giây** → đừng thử mật khẩu bừa.

## 3b. 🔴 THU HẸP PHẠM VI cho 3 case CUỐI (user chốt 2026-08-07, áp dụng từ KTDGKQHT_10 trở đi)

**Áp dụng cho:** KTDGKQHT_10 (dòng 11) · KTHSYCHTPL_11 (dòng 45) · CNHSNLTVV_03 (dòng 36).

**Chỉ verify ĐÚNG TRIỆU CHỨNG BUG GỐC — không chạy hết luồng nghiệp vụ.**
Triệu chứng gốc = nội dung ô `Kết quả thực tế` của đối tác; ô đó trống thì lấy ô `TKM phản hồi lần 1`.

| Case | Triệu chứng gốc phải verify | Ngoài phạm vi (bỏ) |
|---|---|---|
| KTDGKQHT_10 | "Màn hình không có nút chức năng" → màn có chức năng nạp Excel kết quả kiểm tra không, và **bấm có gọi được không** | Nạp tệp thật, bản xem trước, đối chiếu điểm đã lưu, khôi phục dữ liệu |
| KTHSYCHTPL_11 | "Màn hình không hiển thị nút 'Hoàn tất kiểm tra' mà hiển thị nút 'Kiểm tra lại'" → ở hồ sơ đúng tiền đề, màn có nút mở phiếu kết luận không, **bấm có mở được không** | Dựng vụ việc mới, tick lại checklist, lưu kết luận Đạt, đo chuyển trạng thái, đo Phân công |
| CNHSNLTVV_03 | "Hệ thống hiển thị thông báo *Lỗi hệ thống, vui lòng thử lại sau.*" khi Lưu dữ liệu hợp lệ → **bấm Lưu thật**, xem còn báo lỗi đó không | Đo các nhánh phụ, đo hiển thị tên tệp ở tab khác, đo tác dụng phụ trạng thái |

**🔴 Ranh giới KHÔNG được vượt xuống dưới:** "thu hẹp phạm vi" ≠ "chấm bằng mắt".
**VẪN CẤM Pass bằng quan sát tĩnh** (BRIEF §4.2). Thấy nút hiện ra là **chưa đủ** — phải bấm ít nhất 1 nhát để
chứng minh chức năng **gọi được** (hộp thoại mở ra / lời gọi trả về không lỗi). Dev thêm nút mà phần xử lý phía
sau vẫn hỏng là chuyện thường; Pass bằng mắt là loại Pass hay bị bật ngược nhất.

**Riêng CNHSNLTVV_03:** bug gốc **chính là** thao tác Lưu → **bắt buộc bấm Lưu thật**, không có cách nào verify
mà không lưu. Và phải lưu ở **nhánh có đính tệp chứng chỉ** (đúng nhánh trong ảnh đối tác) — lưu ở nhánh không
đính tệp là **Pass oan**, vì đó chính là nhánh dev đã tự khai chạy được.

**Note gửi đối tác phải khai rõ phạm vi đã kiểm** ("đã kiểm sự hiện diện và gọi được của chức năng", không khẳng
định về phần xử lý phía sau). Trung thực về phạm vi quan trọng hơn kết luận rộng.

## 4. Luật bắt buộc (rút từ QA_VERIFY_PROTOCOL + QA_REVERIFY_PROTOCOL + CLAUDE.md)

1. **Chạy ĐÚNG luồng ghi trong phiếu — user yêu cầu rõ "KO chạy khác luồng".** Các bước ở cột
   "Các bước thực hiện" là bắt buộc; được bổ sung phép đo phụ để chứng minh, nhưng **không được thay luồng chính**.
2. **CẤM Pass bằng quan sát tĩnh.** Phải chạy tới bước sinh ra lỗi cũ. "Thấy nút đã có" ≠ Pass.
3. **Bắt thông báo chỉ bằng `output/UAT_doi-tac/tools/toast-capture.js`** — cấm tự viết observer, cấm lọc trùng,
   cấm dùng `textContent` để kết luận. Cài observer TRƯỚC khi bấm; đếm cả số request kèm theo.
4. **Tải lại trang + ghi số hiệu bản dựng** trước khi đo (tab MCP mở lâu vẫn chạy JS cũ).
5. **Chụp màn hình ở mọi thao tác đổi trạng thái, và MỞ ẢNH RA ĐỌC** trước khi kết luận.
   Ảnh lưu vào `G3-uatdoitac-7case-2026-08-07/image/<MaTC>-<mô tả>.png`.
6. **Verify nội dung file xuất, không chỉ "tải được file"** — mở Excel/PDF đọc header + số dòng + đối chiếu màn.
7. **Không tái hiện được vì thiếu tiền đề → KHÔNG Pass.** Tiền đề dựng được thì phải seed (API cookie-auth chạy
   được trên env này) rồi đo lại. Pass ở đây là Pass oan.
8. **Fix một phần = Reopen.** Bug gộp nhiều ý → còn ≥1 ý lỗi = Reopen.
9. **Bug về trường lưu trong DB** (tên file, snapshot) → phép thử quyết định là **tạo bản ghi MỚI**, đừng Reopen
   theo bản ghi cũ.
10. **Quote SRS phải mở file đọc số dòng thật** — cấm quote từ trí nhớ, cấm bê số dòng từ phiếu/ghi chú cũ.
11. **Wording partner-facing:** mô tả yêu cầu nghiệp vụ, KHÔNG kê đơn cách implement. Không lộ chuyện đo 2 môi trường
    theo kiểu so sánh nội bộ — nhưng ĐƯỢC và NÊN ghi rõ env + bản dựng đã đo (đó là phạm vi hiệu lực).
12. **Thấy bug ngoài phạm vi case → vẫn phải ghi nhận** vào `note/` và báo lead; không tự thêm dòng sheet mới.

## 5. Verdict → ô sheet (user chỉ định, không tự đổi)

| Verdict | `Trạng thái dev fix` (cột 17) | `Kết quả verify` (cột 19) |
|---|---|---|
| **Pass** | **`UAT done`** | diễn giải đầy đủ |
| **Reopen** | `Reopen` | diễn giải đầy đủ |

> 🔴 **Sửa 2026-08-07 theo user:** Pass ghi **`UAT done`**, KHÔNG phải `Test done`.
> Lý do: cả 7 dòng đang mang sẵn `Test done` do DEV ghi — QA ghi `UAT done` để verdict của QA
> không lẫn vào giá trị dev. Cả 2 giá trị đều nằm trong dropdown hợp lệ của mọi dòng.

**Ô CHỈ ĐỌC — CẤM ghi đè:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.
Ngoài ra lô này **không đụng** các cột vòng 2 (`Trạng thái 2`, `TKM phản hồi lần 2`, `Trạng thái dev fix 2`,
`DEV phản hồi lần 2`) trừ khi lead yêu cầu.

## 6. Lệnh ghi sheet (bắt buộc dùng script, cấm ghi tay)

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk"
# 1) đổ giá trị CŨ ra file để làm guard --expect-file
python3 output/UAT_doi-tac/tools/sheet_dump_cell.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s --sheet-title bug --sheet-gid 1714340219 \
  --row <N> --column 'Kết quả verify' --out /tmp/g3_<MaTC>_old_kqv.txt
python3 output/UAT_doi-tac/tools/sheet_dump_cell.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s --sheet-title bug --sheet-gid 1714340219 \
  --row <N> --column 'Trạng thái dev fix' --out /tmp/g3_<MaTC>_old_tt.txt

# 2) xem trước (--dry-run) rồi mới ghi thật
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s --sheet-title bug --sheet-gid 1714340219 \
  --row <N> --id-column 'Mã TC' --id-value '<MaTC>' \
  --set-file 'Kết quả verify=<đường dẫn note mới>' \
  --expect-file 'Kết quả verify=/tmp/g3_<MaTC>_old_kqv.txt' \
  --set 'Trạng thái dev fix=<Test done|Reopen>' \
  --expect-file 'Trạng thái dev fix=/tmp/g3_<MaTC>_old_tt.txt' \
  --reason 'Lô G3 — verify env đối tác dòng <N> <MaTC>' --dry-run
```

**Script chặn / báo lỗi → DỪNG, báo lead. CẤM viết script ad-hoc để lách.**

**✅ Dropdown đã đọc thật cho CẢ 7 dòng (11·12·13·14·36·45·50) lúc 2026-08-07 — giống hệt nhau:**
```
['In Progress', 'Fixed', 'UAT done', 'Bug', 'Test done', 'reject', 'Reopen', 'BA confirm']
```
Cả `Test done` lẫn `Reopen` **đều hợp lệ trên mọi dòng** → không có rủi ro kẹt từ vựng (không phải `Reopent`).
Giá trị hiện tại của cả 7 dòng đều đang là `Test done`. **Không cần đọc lại dropdown nữa**, trừ khi script báo chặn.

## 6b. 🔴 BẮT BUỘC — tải ảnh lên Drive và nhúng LINK XEM ĐƯỢC vào note, TRƯỚC khi ghi sheet

**Đường dẫn file local trong ô sheet = coi như KHÔNG CÓ bằng chứng** (đối tác không mở được).
Ghi đè ô `Kết quả verify` sẽ **xoá mất link Drive của lượt trước** → note mới **phải tự mang link của chính nó**.
(Đã suýt mất bằng chứng ở case QLKTLBG_19 vì bỏ qua bước này — đã vá.)

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk"
python3 output/UAT_doi-tac/tools/drive_upload_g3.py \
  --file "<đường dẫn ảnh 1>" --ma-tc <MaTC> --label "<chú thích không dấu, ngắn>" \
  --file "<đường dẫn ảnh 2>" --ma-tc <MaTC> --label "<chú thích>"
# xem lại link đã tạo:
python3 output/UAT_doi-tac/tools/drive_upload_g3.py --list
```

Rồi **thêm vào CUỐI file note** đúng một đoạn dạng:
```
Ảnh bằng chứng: <link Drive 1> (mô tả ảnh 1) · <link Drive 2> (mô tả ảnh 2).
```
**Ảnh phải bắt đúng thao tác quyết định** — với verdict Reopen thì ảnh phải bắt **thao tác LỖI**
(toast/mã lỗi của chính thao tác đó), không phải ảnh biểu mẫu chụp sau.

## 7. Đọc lại xác nhận sau khi ghi (bắt buộc, trước khi sang case kế)

```bash
UAT_TAB=bug python3 output/UAT_doi-tac/tools/sheet_read.py --row <N>
```
So từng ký tự với nội dung đã ghi. Lệch → DỪNG, báo lead.

## 8. Sản phẩm mỗi case

| File | Nội dung |
|---|---|
| `chuan/<MaTC>.md` | Chuẩn chấm khoá TRƯỚC khi đo: SRS line thật + điều kiện của BUG GỐC + tiêu chí Pass/Reopen |
| `do/<MaTC>.md` | Nhật ký đo: env, bản dựng, tài khoản, từng bước, toast, network, ảnh, số đo quyết định |
| `note/<MaTC>-ketqua-verify.txt` | Nội dung sẽ ghi vào ô `Kết quả verify` (partner-facing, tiếng Việt) |
| `image/<MaTC>-*.png` | Ảnh bằng chứng |
