# Báo cáo cuối đợt — Batch B5 (BC đào tạo / tư vấn / hoạt động) — 2026-08-06

| | |
|---|---|
| **Flow** | `flows/04-verify-bug-dev-fix-khong-ho-so.md` — verify bug dev đã fix, không có hồ sơ nội bộ |
| **Bảng** | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219) |
| **Phạm vi** | 6 case / 6 màn báo cáo: dòng 174 · 200 · 205 · 210 · 214 · 218 |
| **Môi trường** | `https://18.143.165.120.nip.io` — env kiểm thử **nội bộ**, KHÔNG phải env nghiệm thu `htpldn-uat.ospgroup.vn` |
| **Tài khoản ra verdict** | `cbnv_tw_05` (CB Nghiệp vụ TW) — không dùng fallback Rule 7 ở bất kỳ case nào. `admin` (QTHT) chỉ dùng để dựng lại đúng tiền đề của đối tác |
| **Cách chạy** | 6 agent con, chạy **lần lượt**; agent sau chỉ khởi sau khi agent trước đã ghi bảng và đọc lại xác nhận |

## Verdict

| Dòng | Mã TC | Màn (FR) | Verdict | Vế a "không tạo được tệp" | Vế tên tệp | Vế b "Forbidden" |
|---|---|---|:-:|:-:|:-:|:-:|
| 174 | SLHDVM_06 | BC Số lượng hỏi đáp/vướng mắc PL (FR-IX-01) | 🔁 Reopen | ✅ hết lỗi | *(đối tác không nêu)* | ❌ tái hiện |
| 200 | CLDTBDDDR_06 | BC Lớp đào tạo đang diễn ra (FR-IX-06) | 🔁 Reopen | ✅ hết lỗi | ✅ đạt | ❌ tái hiện |
| 205 | LDTBDDDR_06 | BC Lớp đào tạo đã diễn ra (FR-IX-07) | 🔁 Reopen | ✅ hết lỗi | ✅ đạt | ❌ tái hiện |
| 210 | CGTVPL_06 | BC Số lượng CG/TVV (FR-IX-08) | 🔁 Reopen | ✅ hết lỗi | ✅ đạt | ❌ tái hiện |
| 214 | DGHQHTPL_06 | BC Đánh giá hiệu quả HTPL (FR-IX-09) | 🔁 Reopen | ✅ hết lỗi | ✅ đạt | ❌ tái hiện |
| 218 | CLDTBDPL_06 | BC Chất lượng đào tạo (FR-IX-10) | 🔁 Reopen | ✅ hết lỗi | ✅ đạt | ❌ tái hiện |

**Vì sao Reopen chứ không Pass:** vế b là triệu chứng vòng 2 của đối tác (`TKM phản hồi lần 1`, retest 31/07:
*"Hệ thống hiển thị thông báo Forbidden"*). Đo lại đúng vai trò đối tác dùng trong ảnh — **Quản trị viên · QTHT**,
đơn vị BTP·TW — thì cả 6 màn vẫn: xem báo cáo được (HTTP 200, hai nút Xuất bật), bấm xuất thì
`POST /api/v1/bao-cao/export` trả **403 `ERR-PERM-SYS-00-01`** và chữ hiện cho người dùng là chuỗi tiếng Anh thô
**"Forbidden"** — lệch `srs-fr-11-bao-cao.md:117` (E7/ERR-RPT-05 quy định thông báo tiếng Việt nêu rõ không có quyền).
Với `cbnv_tw_05` thì xuất tệp chạy tốt ở cả 6 màn. Theo flow §Ca biên: còn ≥1 vế lỗi ⇒ Reopen.

**Vế tên tệp đo được, không phải câu hỏi BA:** BA đã chốt **2026-08-04** (dấu `[BA chốt 2026-08-04]` trong
`srs-fr-11-bao-cao.md:85` `:123` `:1092`) khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`, giờ-phút bắt buộc. Bản dựng
hiện tại đặt tên đúng khuôn (vd `BaoCaoDanhGiaHieuQua_20260806_1514.xlsx`) ⇒ vế này **hết lỗi** ở 5/5 case có nêu.
Số đo cũ 03/08 (`bao-cao-<slug>-YYYY-MM-DD.xlsx`) đã lạc hậu.
⚠️ `tasks/srs-contradictions.md` §SRS-C-010 vẫn ghi *Open* — **tracker chưa cập nhật**, không phải chưa có quyết định.

**Bar Pass đã áp:** mở tệp .xlsx đọc bằng `openpyxl` (số liệu khớp màn hình + header có tiêu đề BC · kỳ · đơn vị ·
ngày tạo theo `:1092`), tên tệp lấy từ nguồn người dùng thật thấy, đo lại bằng đường thứ hai, mỗi case ≥3 dạng dữ liệu.

## 1. Lỗi phát hiện thêm ngoài phạm vi

Cả 3 mục dưới đây **không kéo verdict** của case nào, đã đối chiếu đặc tả (mở file đọc đúng dòng), đo lại bằng
đường thứ hai, và **không** làm đổi dữ liệu nghiệp vụ. Đã mở dòng mới trên bảng:

| Dòng bảng | Mã | Nội dung | Owner |
|---|---|---|---|
| 373 | `BCTK_QA10` | Bộ lọc **Lĩnh vực** vô tác dụng ở FR-IX-06 và FR-IX-08 — giao diện gửi `linhVuc` / `linhVucCm`, máy chủ nhận `linhVucId`; tệp xuất cũng không theo lọc (trái `:1280` BR-DATA-06). Đã loại trừ nhớ đệm bằng mốc `ngayTaoBc` dùng chung | Dev FE (BE xác nhận tên tham số) |
| 374 | `BCTK_QA11` | 4 màn thiếu nhóm dữ liệu đặc tả ghi điều kiện hiển thị **"Luôn"**: `:380` `:381` (FR-IX-06) · `:421` `:422` (FR-IX-07) · `:507` (FR-IX-09) · `:548` (FR-IX-10) | Dev BE |
| 375 | `BCTK_QA12` | Hai lượt xuất trong **cùng một phút** ra tệp trùng tên, không có hậu tố `_1`/`_2` như Phụ lục E §H8 (`srs-v3.5.md:6716`, `[BA chốt 2026-08-06]`) đòi | Dev BE |

**Lỗi gặp lại đã có phiếu — không mở dòng mới:**

- Gốc 403 "Forbidden" khi xuất báo cáo: đã có `BCTK_QA01` (dòng 363, do lô B2 mở). Trạng thái dòng cũ vẫn đúng.
  6 case của lô này ghi entry riêng trong `bug-report.md` và dẫn chiếu về phiếu đó.
- Hai nút Xuất bị vô hiệu sau lần bấm [Xem báo cáo] thứ hai: đã có `BCTK_QA02` (dòng 365) và `BCTK_QA07` (dòng 370).
  Lô này gặp lại 1 lần ở FR-IX-07 sau khi xóa bộ lọc bằng chuột thật — **chưa chốt được điều kiện kích hoạt tối thiểu**
  (giả thuyết bộ đệm 304 đã bị bác bỏ), nên chỉ ghi nhận, không mở dòng.

**Quan sát thấy lệch nhưng KHÔNG log** (trượt cửa "đặc tả có đòi không"): thẻ KPI cắt phần thập phân
(33,9 → `33`; 6,35 → `6`) trong khi bảng làm tròn 1 chữ số và tệp giữ đủ — đặc tả im lặng về quy tắc làm tròn.

## 2. Dữ liệu đã seed / thay đổi

**Không có.** Cả 6 case đều là thao tác chỉ đọc (xem báo cáo + xuất tệp): không tạo, không sửa, không xóa bản ghi
nghiệp vụ nào, không đổi trạng thái tài khoản nào. Vết duy nhất để lại trên env là các lượt đăng nhập của
`cbnv_tw_05` và `admin`. Tệp hệ thống giao ra được giữ ở `testfiles/` làm bằng chứng.

## 3. Case chưa chốt được / giới hạn hiệu lực

| Việc | Vì sao | Cần ai làm gì |
|---|---|---|
| Vế a + vế tên tệp mới chỉ "hết lỗi **tạm**" | Đo trên env nội bộ `18.143.165.120.nip.io`, không phải env nghiệm thu của đối tác | Dev/Infra đưa bản dựng này lên `htpldn-uat.ospgroup.vn`, QA verify lại |
| **QTHT có được xuất báo cáo hay không** — chưa kết luận | Đặc tả tự mâu thuẫn: `:62` / `:140` / `:440` / `:485` khai tác nhân là CB Nghiệp vụ / CB Phê duyệt, còn `:1268` cho QTHT bypass | BA chốt — câu hỏi đã nằm ở `cau-hoi-BA.md` §Mục 2 (không mở mục trùng) |
| Bản dựng **trôi giữa lô** | Env dựng lại lúc 14:13 giờ máy: bó mã `index-CNwX9JjX.js` (md5 `e0e4f737…`) → `index-DIABnbIr.js` (md5 `39041317…`), **nhãn trong app vẫn V1.0.8 ở cả hai** | Khi so số giữa case 174/200/205 (bản cũ) và 210/214/218 (bản mới) phải tính tới việc này. Kết luận không đổi chiều: bản mới vẫn tái hiện Forbidden, vẫn xuất được với CB nghiệp vụ |
| Ô `Ảnh/vieo 1` dòng **205** trỏ nhầm tệp | Ô này trỏ đúng cùng tệp Drive với dòng 200 (`CLDTBDDDR_06.jpg`) ⇒ vòng 1 của `LDTBDDDR_06` coi như **không có bằng chứng riêng**; đã dùng ảnh vòng 2 `LDTBDDDR_06_v2.jpg` | Đối tác gắn lại đúng tệp cho dòng 205 |
| Chưa đo | Khổ giấy / phông bên trong tệp xuất, nội dung PDF ngoài phần header — nằm ngoài vế đối tác nêu | — |

## 4. Bảng bị sửa sau khi ghi — đã có người chốt

Đối soát lúc 16:45 cho thấy **5/6 dòng** đã bị đổi `Trạng thái dev fix` từ `Reopen` (giá trị QA ghi, có đọc lại xác nhận)
sang **`BA confirm`** — một giá trị **mới được thêm vào danh sách chọn** sau 12:05 (lúc đầu đợt danh sách chỉ có
`In Progress · Fixed · UAT done · Bug · Test done · reject · Reopen`). Dòng 218 vẫn còn `Reopen` vì ghi sau cùng (16:35).

Ngoài ra `Kết quả verify` của dòng **210** và **214** đã bị viết lại theo một khuôn khác
(*"▌CÒN LỖI Ở ĐÂU — đọc 5 dòng này là đủ…"*); nhật ký `tools/sheet_bug_verify_write.log` ghi hai lượt ghi lúc
16:18 với `mode=chi-sua-ketqua` — chế độ **không tồn tại** trong bản công cụ đầu đợt, tức công cụ cũng đã được
phiên khác sửa trong lúc lô đang chạy.

**Quyết của chủ việc (06/08/2026): giữ `BA confirm`, đồng bộ dòng 218.** Đã ghi `Trạng thái dev fix` dòng 218
`Reopen` → `BA confirm`; đọc lại xác nhận. Sau đối soát, **cả 6 dòng** cùng `Trạng thái dev fix = BA confirm`,
`Dopai = dev done`. Ô `Kết quả verify` dòng 218 **giữ nguyên** không đụng (chạy với `--chi-sua-trang-thai`) —
lời văn "🔁 Còn lỗi — chuyển lại dev…" của cả 6 dòng vẫn thống nhất như nhau, kể cả 2 dòng phiên khác viết lại.

Verdict đo được **không đổi**: mục Verdict phía trên vẫn là kết quả phép đo (còn vế b lỗi ⇒ Reopen theo flow).
`BA confirm` ở đây là **cách phân loại trên bảng** do chủ việc chốt (gom 6 dòng cùng gốc 403 QTHT về nhánh chờ BA),
không phải kết luận mới của QA. Câu hỏi BA tương ứng: `cau-hoi-BA.md` §Mục 2.

**Rút gọn ô `Kết quả verify` (06/08, theo yêu cầu chủ việc):** cả 6 ô viết lại còn ~1.1–1.6k ký tự (trước là
2.3–5.5k), chạy `--chi-sua-ketqua` nên **không** đụng cột trạng thái. Giữ lại 4 thứ tối thiểu để dev tái hiện
được: vai trò gặp lỗi · nguyên văn chữ hiện ra · dòng đặc tả quyết định (`:117` · `:79` `:1052`) · tên ảnh.
Phần dài (bảng đo từng bộ lọc, khối `CÁCH VERIFY sau Dev fix` đầy đủ) nằm ở `bug-report.md` Phần 3·6·7·8·9·10;
mỗi ô đều trỏ về đúng Phần của nó. Giá trị cũ của cả 6 ô nằm trong `tools/sheet_bug_verify_write.log`.

Để ghi được nước đi này mà không phá guard, `tools/sheet_bug_verify_write.py` được thêm verdict `baconfirm`
(→ `Trạng thái dev fix = "BA confirm"`) kèm danh sách nguồn **riêng cho verdict đó** (`WRITABLE_FROM_BY_VERDICT
= {'Fixed','Reopen'}`). Cố ý **không** nới `WRITABLE_FROM` chung — nới ở đó là mở đường ghi đè trạng thái cho mọi
verdict. Giá trị cũ nằm trong `tools/sheet_bug_verify_write.log` nên vẫn khôi phục được nếu BA quyết ngược lại.

## Hồ sơ

| Loại | Đường dẫn |
|---|---|
| File tiêu chí (6) | `tieuchi/{SLHDVM_06, CLDTBDDDR_06, LDTBDDDR_06, CGTVPL_06, DGHQHTPL_06, CLDTBDPL_06}.md` |
| Bug entry (6) | `bug-report.md` — Phần 3 · 6 · 7 · 8 · 9 · 10, mỗi phần có bảng riêng + khối `CÁCH VERIFY sau Dev fix` |
| Câu hỏi BA | `cau-hoi-BA.md` §Mục 2 (đã có sẵn từ lô khác; lô này thêm blockquote, không mở mục trùng) |
| Ảnh + nguyên văn thông báo | `image/` — mỗi case 7–10 tệp, có 1 tệp `.txt` chứa nguyên văn chữ trên màn + phản hồi máy chủ |
| Tệp hệ thống giao ra | `testfiles/` |
| Bằng chứng đối tác | `partner-evidence/` (tải bằng `tools/fetch_evidence.py`) |
| Dòng bug mới | `oos-rows/BCTK_QA1{0,1,2}.json` — bằng chứng đã tải lên Drive qua `tools/drive_upload_evidence.py --batch b5bctk0806` |
| Bối cảnh dùng chung | `B5-CONTEXT.md` |
