# FLOW 03 · lô F3-devfix-2026-08-07 — tiến độ 6 case

**Bảng:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219)
**Môi trường đo:** https://18.143.165.120.nip.io (env nội bộ)
**SRS nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Ánh xạ ô:** mã case = `Mã TC` · note = `Kết quả verify` · trạng thái dev = kết quả QA = `Trạng thái dev fix`
(tab này chỉ có MỘT cột trạng thái ⇒ Pass ghi `Test done` vào đúng cột đó)

## Trạng thái bảng lúc bắt đầu (đọc live 2026-08-07)

| Dòng | Mã TC | Trạng thái dev fix | Dopai | DEV phản hồi lần 1 | Nhánh |
|---:|---|---|---|---|---|
| 36 | CNHSNLTVV_03 | Fixed | dev done | có (đề 04/08 — TRƯỚC lượt Reopen 06/08) | Re-verify dev fix |
| 37 | CNDSMLTVV_01 | Fixed | dev done | trống | Re-verify dev fix |
| 51 | XNTGHTVV_03 | Fixed | dev done | trống | Re-verify dev fix |
| 64 | DGKQHTVV_01 | Fixed | dev done | trống | Re-verify dev fix |
| 126 | LKHDG_12 | Fixed | dev done | trống | Re-verify dev fix |
| 127 | LKHDG_16 | Fixed | dev done | trống | Re-verify dev fix |

6/6 có bug entry + khối `CÁCH VERIFY` ⇒ **6/6 nhánh Re-verify dev fix**, 0 case rơi sang Flow 04.

## Cảnh báo đã ghi nhận ở BƯỚC 0

1. **Không có bằng chứng dev sửa gì.** Nhật ký `tools/sheet_bug_verify_write.log` cho thấy QA đã ghi
   `Reopen` lên đủ 6 dòng ngày 06/08 (126@08:09 · 127@08:38 · 51@15:13 · 64@17:18 · 36@17:31 · 37@18:18).
   Nay cả 6 lại về `Fixed` mà ô `DEV phản hồi lần 1` trống ở 5/6 dòng.
   ⇒ Mọi agent đo BẮT BUỘC ghi bản dựng + bó mã ở bước đầu và so với `V1.0.8 / assets/index-DIABnbIr.js`
   (bản đã đo 06/08). Trùng khít ⇒ báo điều phối trước khi chốt verdict.
2. **LKHDG_12 có 2 hồ sơ bug song song** — `flowtest-kiemdinh/bug-report.md` (prompt chỉ định) và
   `reverify-bug-devfix-2026-08-06/bug-reports/bug-report-LKHDG.md`. Phải đối chiếu 3 chiều trước khi chấm.
3. **SRS lệch +2 đã xác nhận** trên `srs-fr-08-danh-gia.md` (1280 dòng): `:821 → :823` ([Xuất Excel]),
   `:837 → :839` (Hành động: Xem / Sửa chỉ LAP_KE_HOACH/PHAN_CONG / Xóa).
   Hai dòng BA chèn 06/08 là `:852` **Cơ quan được đánh giá** `[CR-10][BA chốt 2026-08-06]` và
   `:854` **Tài liệu đính kèm** `[CR-07][BA chốt 2026-08-06]` — đúng 2 mục vòng trước QA tách sang hỏi BA
   ở LKHDG_16 ⇒ điểm đó nhiều khả năng đã được giải quyết, case 127 không còn vế chờ BA.
4. **Dòng 51 còn cặp cột vòng 2 của đối tác** (`Trạng thái 2` = Fail, `Trạng thái dev fix 2` = dev done).
   Theo ánh xạ prompt chỉ ghi cột `Trạng thái dev fix`; KHÔNG đụng cột vòng 2.

## Lịch chạy agent đo (tuần tự — mỗi thời điểm chỉ MỘT agent gọi chrome-devtools)

| Lượt | Case | Trạng thái |
|---|---|---|
| 1 | 36 CNHSNLTVV_03 + 37 CNDSMLTVV_01 | ✅ ĐO XONG cả 2 (Reopen · Reopen) |
| 2 | 51 XNTGHTVV_03 + 64 DGKQHTVV_01 | ✅ ĐO XONG cả 2 (Pass · Reopen) |
| 3 | 126 LKHDG_12 + 127 LKHDG_16 | ✅ ĐO XONG cả 2 (Pass · Pass) |
| 4 | 36 CNHSNLTVV_03 — **R4** đo lại hẹp trên bó mã mới | ✅ 2 quan sát quyết định đạt, **còn 3 GAP** (khối khoá đòi 6 lượt, R4 chạy 2) ⇒ agent **từ chối** nâng Pass |
| 5 | 36 CNHSNLTVV_03 — **R5** chạy nốt 4 lượt lấp GAP | ✅ vân tay khớp R4 (kiểm TRƯỚC khi đo) · 4/4 lượt đạt · GAP **trống** ⇒ **Pass** |

## Kết quả

| Dòng | Mã TC | Verdict | Ghi bảng | Bug-report đã cập nhật |
|---:|---|---|---|---|
| 36 | CNHSNLTVV_03 | ✅ **Pass** (R3 Reopen → R4+R5 đo lại trên bó mã mới) | ✅ `Test done` + note Pass MỚI 2630 ký tự. Note R3 giữ ở `note/CNHSNLTVV_03-R3-reopen.md` | ✅ đóng bug, **không** đổi tên `Pass-*` (file còn 1 Reopen + 1 Chờ BA) |
| 37 | CNDSMLTVV_01 | 🔁 Reopen | ghi 01:12 → **bị đổi về `fixed`** → **đã khôi phục** `Reopen` · note 5142 ký tự nguyên vẹn | ✅ |
| 51 | XNTGHTVV_03 | ✅ **Pass** | ✅ `Test done` + note 993 ký tự (đọc live khớp) | ✅ |
| 64 | DGKQHTVV_01 | 🔁 **Reopen** | ✅ `Reopen` + note 4585 ký tự (đọc live khớp) | ✅ |
| 126 | LKHDG_12 | ✅ **Pass** | ✅ `Test done` + note 1902 ký tự (đọc live khớp) | ✅ cả 2 file, không đổi tên `Pass-*` |
| 127 | LKHDG_16 | ✅ **Pass** (không dùng `reopenba`) | ✅ `Test done` + note 2682 ký tự (đọc live khớp) | ✅ |

**Đối chiếu live 6/6 dòng sau khi ghi xong (02:3x):** 6/6 ô ghi chú trùng khít từng ký tự với `note/*.md`.
Cột trạng thái: **4/6 giữ đúng verdict QA**, 2/6 (dòng 36, 37) bị đổi ngược — xem §Sự cố 2.

**Phạm vi đo lại (đã cân nhắc, không mở rộng tùy tiện):**
- **Case 36 — ĐO LẠI, trong phạm vi lô.** Lý do không phải vì dev khai fix mới, mà vì **phép đo của chính
  lô này** chạy trên bản dựng bị thay sau 9 phút ⇒ tự nó chưa đủ tin.
- **Case 37 — KHÔNG đo lại trong lô này.** Nó đo trên bản dựng đang hiện hành tại thời điểm đo ⇒ phép đo
  hợp lệ. Việc dev vừa khai "fixed" lần nữa là **claim MỚI**, thuộc vòng sau. Đo lại claim mới ngay trong
  lô sẽ không bao giờ kết thúc: dev deploy nhanh hơn tốc độ đo.

> Dòng 64 KHÔNG ghi `Dopai`=BA. Vế D3 ("một bên đã chấm, bên còn lại vào chấm") chưa dựng được là vì **bị
> chính lỗi đang Reopen chặn**, không phải vì đặc tả mơ hồ — `:1809` và `:1811` thống nhất ở nhánh doanh
> nghiệp. Đánh dấu BA sẽ đẩy bóng sang BA trong khi ô ghi chú không có câu hỏi nào cho BA. Quan sát này
> chuyển vào mục "case chưa kết luận" của báo cáo cuối đợt.

## 🔴 Sự cố 1 — công cụ ghi bảng bị thay giao diện giữa lô (07/08 ~02:00)

`tools/sheet_bug_verify_write.py` bị viết lại thành công cụ **tổng quát**: mất
`--verdict / --flow04 / --srs-root / --srs-ref / --expected-relation / --ketqua-file / --cho-phep-de-ketqua`;
thay bằng `--spreadsheet-id / --sheet-title / --id-column / --id-value / --set / --set-file / --expect /
--expect-file / --reason / --audit-log`.

| Chốt an toàn | Bản cũ | Bản mới | Ghi chú |
|---|---|---|---|
| Khớp định danh dòng trước khi ghi | ✅ | ✅ | `--id-column/--id-value` |
| Optimistic lock giá trị cũ | một phần (`WRITABLE_FROM`) | ✅ mạnh hơn — **bắt buộc** `--expect` cho MỌI cột sửa | chống đè thay đổi của dev |
| Kiểm dropdown thật của ô | ✅ | ✅ | chỉ danh sách literal |
| Ghi batch + đọc lại + audit log | ✅ | ✅ | log `tools/sheet_update_audit.jsonl` |
| **Bắt buộc dẫn dòng SRS** | ✅ ép | ❌ **mất** | thay bằng: đóng dẫn chứng vào `--reason` |
| **Chặn Pass khi quan hệ ≠ match** | ✅ ép | ❌ **mất** | thay bằng: điều phối tự kiểm trước khi ghi |
| Mapping verdict → cột | ✅ | ❌ mất | điều phối tự map theo mục 5 của prompt |

⇒ 2 chốt cuối nay do người chịu, không còn máy chặn. Mọi lệnh ghi của lô này đều nhét verdict + quan hệ +
dòng SRS vào `--reason` để audit log vẫn giữ vết.

## 🔴 Sự cố 2 — verdict QA bị ĐỔI NGƯỢC trên bảng khi lô còn đang chạy

**Chẩn đoán đầu tiên của tôi SAI.** Lúc 02:0x tôi thấy dòng 36 có ô ghi chú Reopen nhưng cột trạng thái vẫn
`Fixed`, và kết luận "công cụ ghi nửa vời" → đã ghi lại `Reopen`. Tra nhật ký công cụ cũ
(`tools/sheet_bug_verify_write.log`) mới thấy **cả 2 dòng đều ghi THÀNH CÔNG từ trước**:

```
[2026-08-07 00:42:06] row=36 CNHSNLTVV_03 verdict=reopen   Trạng thái dev fix R36: CŨ='Fixed' → MỚI='Reopen'
[2026-08-07 01:12:35] row=37 CNDSMLTVV_01 verdict=reopen   Trạng thái dev fix R37: CŨ='Fixed' → MỚI='Reopen'
```

⇒ Không phải lỗi công cụ. **Có người đổi ngược verdict về "đã fix"** trong lúc lô đang chạy:

| Dòng | QA ghi | Lúc | Bị đổi thành | Phát hiện lúc |
|---|---|---|---|---|
| 36 | `Reopen` | 00:42 | `Fixed` (viết hoa) | 02:0x |
| 37 | `Reopen` | 01:12 | `fixed` (viết **thường**) | 02:3x — tức trong 25 phút tôi đang làm việc |

Hai cách viết hoa/thường khác nhau ⇒ **gõ tay**, không phải công cụ. Nhiều khả năng dev đã sửa tiếp và tự
đánh dấu lại "fixed" để chuyển sang vòng sau — hành vi bình thường của luồng này, **nhưng** hệ quả thì
nghiêm trọng: cột `Trạng thái dev fix` **vừa là ô dev khai, vừa là ô QA chấm** (mục 5 của prompt), nên
verdict QA bị ghi đè trong vòng chưa tới 1 giờ. **Ô ghi chú thì còn nguyên** — nội dung QA không mất.

**Bài học đã áp dụng:** không suy từ ô sheet, phải **tra nhật ký ghi**; và đọc live **cả 2 ô** của **cả 6
dòng** sau khi ghi xong, chứ không tin mỗi dòng "đọc lại" của công cụ.

**Đề nghị với user (chưa tự làm):** hoặc xin **cửa sổ đóng băng** để dev không sửa cột trong lúc QA chấm,
hoặc xin **một cột riêng cho QA** — bằng không, mỗi vòng re-verify đều có thể bị ghi đè trước khi đối tác kịp đọc.

## 🔴 Sự cố 3 — env deploy liên tục trong lúc đo (đã loại trừ cân bằng tải)

6/6 lượt `GET /` trả **cùng một etag + cùng một bó mã** ⇒ **không phải** nhiều máy chủ phục vụ bản khác nhau.
Đúng là **deploy liên tiếp**:

| Bó mã FE | `GET /` last-modified (GMT) | Giờ VN | Ghi chú |
|---|---|---|---|
| `index-DIABnbIr.js` | 06/08 07:13:15 | 06/08 14:13 | sidebar V1.0.8 |
| `index-CxS5qW_0.js` | 06/08 12:48:25 | 06/08 19:48 | sidebar V1.0.9 |
| `index-B2W2Krcs.js` | 06/08 17:39:54 | 07/08 00:39 | sidebar V1.0.10 — **case 37, 51, 64 đo ở đây** |
| `index-DsMHK7Dp.js` | 06/08 18:51:25 | 07/08 01:51 | **sidebar lại ghi V1.0.9** — case 126, 127 đo ở đây |
| `index-D4Buvu4S.js` | 06/08 19:23:01 | 07/08 02:23 | lên **giữa lúc** agent còn đang đo case 127 |

🔴 **Chuỗi phiên bản ở sidebar KHÔNG đáng tin** — bó mã `DsMHK7Dp` mới hơn bó mã của bản gắn nhãn V1.0.10
mà sidebar vẫn ghi V1.0.9. Định danh bản dựng thật = **bó mã + `last-modified`**, không phải nhãn phiên bản.

⇒ Đã ghim **mốc giờ đo** vào note 126/127 để dev truy được ra bản dựng. Không đuổi theo bản mới cho từng
case — env thay nhanh hơn tốc độ đo, đuổi là vòng lặp vô hạn.

## Hồ sơ audit nội dung ô `Kết quả verify` CŨ (chép trước khi đè)

`audit/CNHSNLTVV_03-ketqua-verify-CU.md` · `audit/CNDSMLTVV_01-ketqua-verify-CU.md` ·
`audit/XNTGHTVV_03-ketqua-verify-CU.md` · `audit/DGKQHTVV_01-ketqua-verify-CU.md` ·
`audit/LKHDG_12-ketqua-verify-CU.md` · `audit/LKHDG_16-ketqua-verify-CU.md`

## Kết quả 4 agent đọc — chuẩn chấm 6/6 ĐÃ KHÓA (`chuan/*.md`)

### Độ lệch số dòng SRS — KHÔNG đồng nhất, cấm áp một offset chung
| File SRS | Lệch | Ghi chú |
|---|---|---|
| `srs-fr-08-danh-gia.md` | **+2** ở vùng `:161` / `:823` / `:839`; **+5** ở vùng bảng chuyển trạng thái `:1190-1199` | BA chèn ở 3 chỗ khác nhau (commit `2699898` trong repo lồng `Docs-PM-HTPLDN`) |
| `srs-v3.5.md` | **+44 … +45** (BR-DATA-06 `5525→5570`; BR-PUBLIC-01 `5685→5729`) | 2 commit BA ngày 06/08 |
| `srs-fr-11-bao-cao.md` | **+5** (`1276-1280 → 1281-1285`) | |
| `srs-fr-04-chuyen-gia-tvv.md` | **0** | không bị sửa 06/08 |
| `srs-fr-05-vu-viec.md` | **0** | mtime 04/08 17:17, 0/10 trích dẫn lệch |

### Quyết định điều phối
1. **Case 127 KHÔNG dùng `reopenba`.** Điểm chờ BA đã được BA giải quyết: `srs-fr-08-danh-gia.md:852`
   (`25a` Cơ quan được đánh giá `[CR-10][BA chốt 2026-08-06]`) và `:854` (`26a` Tài liệu đính kèm
   `[CR-07][BA chốt 2026-08-06]`). Verdict chỉ Pass / Reopen / ô trống.
   Hệ quả: vế "form Sửa hiện 2 mục đó" từ *không chấm được* thành **chấm được** — gỡ mất = bug mới có căn cứ.
2. **Căn cứ Reopen case 127 còn nguyên:** toàn `srs-fr-08` chỉ 1 dòng nói về thao tác Sửa kèm trạng thái
   (`:839`) và nó cho phép **cả `PHAN_CONG`**; `:161` cho phép sửa KH chưa duyệt; `ERR-BIZ-XI` = **0 kết quả**
   trong `srs-v3.5/`.
3. **Ô `Kết quả verify` trên bảng là bản NÉN, thiếu so với bug entry** ở case 37 / 51 / 64.
   Không mâu thuẫn, chỉ là tập con ⇒ **khóa chuẩn theo bug entry** (bản chặt hơn), và khi ghi note vòng này
   viết khối `CÁCH VERIFY` **giống hệt từng chữ bug entry** để dứt drift.
4. **LKHDG_12 giống nhau toàn bộ phần quyết định chấm** ở cả 3 bản (file prompt chỉ định ↔ file LKHDG ↔ ô sheet);
   chỉ lệch cách dọn lọc bước 4 (tương đương) ⇒ dùng bản `flowtest-kiemdinh/bug-report.md` theo prompt.

### Dòng SRS quyết định phải biết trước khi đo
- `srs-fr-04-chuyen-gia-tvv.md:1507` — *"Số thẻ hành nghề · **Bắt buộc nếu Loại = Tư vấn viên**"* ⇒ case 37:
  hệ thống **từ chối** TVV thiếu số thẻ là **ĐÚNG**; lỗi là **báo thành công sai** + không cho biết hồ sơ nào hỏng.
- `srs-fr-05-vu-viec.md:1805-1808` — Nhóm 4/5/7 **cố ý ẩn** ở chế độ DN · `:1810` — Dòng thời gian chế độ DN
  **không** liệt kê sự kiện Đánh giá ⇒ case 64: **cấm log 2 điểm này thành lỗi**.
- `srs-fr-08-danh-gia.md:831` — cột trên **màn** tên là *"Mã đợt"* (`DG-…`) ⇒ case 126: tìm cột trong tệp theo
  **nội dung**, không theo tiêu đề "Mã KH".

### Vân tay bản dựng để đối chiếu ở bước 0 của mọi agent đo
`HTPLDN · V1.0.8` · bó mã `assets/index-DIABnbIr.js` · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT`
· etag `W/"6a74340b-428"` (nguồn `reverify-week-5/BAN-DUNG.md`).
Vân tay thứ hai xuất hiện trong hồ sơ LKHDG: `assets/index-DThrFe1_.js` (đo 06/08 00:32 & 08:50).
Trùng khít một trong hai ⇒ **báo điều phối**, nhưng **vẫn phải đo đủ** (lỗi 126/37/51 nằm phía máy chủ, bó mã FE
không đổi KHÔNG chứng minh BE không đổi).

## 🔴 CẬP NHẬT BƯỚC 0 — env ĐÃ deploy bản dựng MỚI (đo 2026-08-07 00:1x giờ VN)

Vân tay đo được **KHÁC hoàn toàn** cả 2 vân tay 06/08 ⇒ **Cảnh báo 1 ở trên KHÔNG còn áp dụng**, có bản dựng
mới thật, mọi agent còn lại dùng vân tay này để đối chiếu:

| Hạng mục | Vân tay MỚI (07/08) | Vân tay cũ (06/08) |
|---|---|---|
| Phiên bản | **`HTPLDN · V1.0.9`** | `V1.0.8` |
| Bó mã FE | **`assets/index-CxS5qW_0.js`** | `index-DIABnbIr.js` · `index-DThrFe1_.js` |
| `GET /` last-modified | **`Thu, 06 Aug 2026 12:48:25 GMT`** (19:48 giờ VN 06/08) | `07:13:15 GMT` |
| `GET /` etag | **`W/"6a748299-428"`** | `W/"6a74340b-428"` |

Bản dựng lên lúc **19:48 giờ VN 06/08**, tức **SAU** cả 6 lượt Reopen của lô (muộn nhất 18:18) ⇒ việc bảng bị
lật `Reopen → Fixed` là có căn cứ về mặt bản dựng, dù 5/6 ô *DEV phản hồi lần 1* vẫn trống.

**Lỗi mới phát hiện ở lượt đo case 36, ảnh hưởng CHÉO các case khác có đính tệp:** mọi tệp thuộc hồ sơ tư vấn
viên đều **không đọc lại được** — `GET /api/v1/files/{id}` trả `403 ERR-PERM-FILE-03 "Loại đối tượng
'TVV_HO_SO' của tệp chưa được đăng ký"` (3/3 tệp thử). Màn nào lỡ nạp một tệp như vậy sẽ bị **đá thẳng sang
trang `/403`**. Agent đo case 51/64/126/127 gặp `/403` bất ngờ thì kiểm nhật ký trình duyệt trước khi kết luận
là lỗi phân quyền.

---

## 🔴 RỦI RO MỚI — env deploy liên tục, verdict có thể stale theo bản dựng

| Bản dựng | Bó mã FE | `GET /` last-modified | Lên lúc (giờ VN) |
|---|---|---|---|
| V1.0.8 | `assets/index-DIABnbIr.js` | Thu, 06 Aug 2026 07:13:15 GMT | 06/08 14:13 |
| V1.0.9 | `assets/index-CxS5qW_0.js` | Thu, 06 Aug 2026 12:48:25 GMT | 06/08 19:48 |
| **V1.0.10** | `assets/index-B2W2Krcs.js` | Thu, 06 Aug 2026 17:39:54 GMT | **07/08 00:39** |

- **Case 36 đo trên V1.0.9** (~00:19–00:30 giờ VN 07/08); **V1.0.10 lên lúc 00:39** — sau 9 phút.
  ⇒ Verdict Reopen dòng 36 là **đo trên bản dựng đã bị thay**. Phải **đo lại hẹp ở CUỐI LÔ**, khi env đã ổn:
  chỉ 2 quan sát quyết định — dòng "Chứng chỉ chi tiết" có hiện TÊN TỆP không · hồ sơ đã có tệp có mở lại
  được form [Cập nhật năng lực] không.
  ⚠️ Verdict này **nay đã nằm trên bảng đối tác** (vá sự cố 2). Nếu đo lại trên V1.0.10 cho kết quả đã fix
  thì phải sửa **cả 2 ô** — `Trạng thái dev fix` → `Test done` **và** viết lại ô `Kết quả verify` (bỏ khối
  CÁCH VERIFY, vì Pass không kèm khối đó), không được sửa mỗi cột trạng thái.
- **Case 37 đo trên V1.0.10** — sạch, không cần đo lại trừ khi env deploy tiếp.
- **Mọi agent đo còn lại BẮT BUỘC ghi vân tay đầu phiên** và báo nếu khác V1.0.10.

## ✅ Đã xác minh lại số dòng cho báo cáo cuối đợt (07/08, tự mở file đếm)

| Trích dẫn | Đã mở đọc | Kết luận |
|---|---|---|
| `srs-v3.5.md:6772` | E.I.1 — mẫu toast "Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp luật Quốc gia." | ✅ **đúng dòng** — candidate "toast thiếu mã/tên đối tượng" giữ nguyên |
| `srs-fr-05-vu-viec.md:1810` | Dòng thời gian chế độ DN: chỉ hiện *tiếp nhận, kết luận kiểm tra, kết quả phê duyệt, hoàn thành, **từ chối**, công khai/hủy công khai*; ẩn sự kiện nội bộ *(phân công, trao đổi giữa cán bộ)* | ⚠️ **candidate ghi QUÁ TAY** — xem dưới |
| `srs-fr-08-danh-gia.md:823` | hàng toolbar: tiêu đề trang + `[+ Tạo đợt đánh giá] [Xuất Excel] [Làm mới]` | ✅ **đúng dòng** — căn cứ case 126 |
| `srs-fr-08-danh-gia.md:827` | Lọc trạng thái, enum *Tất cả / LAP_KE_HOACH / PHAN_CONG / CHO_DUYET_PC / THUC_HIEN / BAO_CAO / CHO_PHE_DUYET / HOAN_THANH / **HUY*** | ✅ **đúng dòng** — enum CÓ `HUY` ⇒ candidate "dropdown thiếu mục Hủy" là lệch thật |
| `srs-fr-08-danh-gia.md:824-829` | trọn vùng filter-bar (ô tìm kiếm → nút Tìm kiếm/Xóa bộ lọc) | ✅ **đúng vùng** — "Bộ lọc nâng cao (2)" không có trong đặc tả |

🔴 **Sửa candidate "dòng thời gian chế độ DN hiện sự kiện nội bộ":** `:1810` **liệt kê "từ chối" trong nhóm
DN ĐƯỢC thấy**, nên hiện "Từ chối" **không** phải vi phạm. Chỉ **"Phân công"** mới nằm trong nhóm phải ẩn.
⇒ Báo cáo cuối đợt chỉ được nêu **"Phân công"**; phần "Từ chối" gỡ khỏi candidate (nếu muốn giữ thì phải
ghi rõ là **hỏi BA** chuyện "từ chối" ở đây là *hồ sơ bị từ chối* hay *người được phân công từ chối*, chứ
không được nêu như lỗi).

## Phát hiện dùng chung cho các case sau

- 🔴 **Tệp thuộc hồ sơ TVV không đọc lại được:** `GET /api/v1/files/{id}` → **403 `ERR-PERM-FILE-03`**
  *"Loại đối tượng 'TVV_HO_SO' của tệp chưa được đăng ký"*. Màn nào nạp tệp đó bị đá sang `/403`.
  Gặp `/403` bất ngờ ⇒ mở nhật ký trình duyệt tìm `[403] GET /files/…` TRƯỚC khi kết luận lỗi phân quyền.
  (Đã log ở case 36, không phải lỗi mới.)
- **`cbnv_tw_02` (cấp TW) CÓ nhìn thấy + tích chọn được hồ sơ khác đơn vị** (`TVV-STP-AG-0001`).
  Không log bug: `srs-fr-04-chuyen-gia-tvv.md:1420` im lặng về cấp TW (phạm vi "Toàn quốc").
- **Tiền đề case 37 nay đã có sẵn:** `TVV-BTP-TW-0016` (TVV, số thẻ `THN-TW-2026-016`, Đang hoạt động,
  đã hoàn nguyên về Chưa công khai). ⚠️ Máy trạng thái một chiều — không trả về `CHO_KICH_HOAT` được (422).
