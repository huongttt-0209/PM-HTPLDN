# Chạy thử FLOW 04 — 5 case, env dev

**Ngày:** 2026-08-05 · **Env:** https://18.143.165.120.nip.io — bản dựng **V1.0.8** (bundle `index-D-YMo5bZ.js`)
**Tài khoản:** `cbnv_tw` (CB_NV_TW) · `qa_tvvseed28` (TVV·CG) · **Viewport:** 1440×741
**Nguồn case:** sheet làm việc `1OKBN2otlmdZ44…` tab `bug`, lọc `Dopai` ∈ {N/R, dev done} **và** `Trạng thái dev fix` = fixed

> **KHÔNG ghi gì lên sheet.** Đây là lượt chạy thử để kiểm chính bản thân 4 flow; verdict sẵn có trên sheet
> được giữ nguyên làm mốc đối chiếu.

---

## Kết quả 5 case

| Mã case | Verdict dev V1.0.8 | Verdict UAT V1.0.7 (lượt trước) | Bằng chứng |
|---|---|---|---|
| QLTVV_02 | **Pass** | Pass | `DEV-QLTVV_02-danhsach-…png` · `DEV-QLTVV_02-cot-hanhdong-…png` |
| KTHSYCHTPL_11 | **Không phải lỗi** | Không phải lỗi | `DEV-KTHSYCHTPL_11-dat-giu-DANGKIEMTRA-V108.png` |
| QLKTLBG_18 | **Pass** | (dở dang — có nút, 200, chưa đọc nội dung tệp) | `DEV-QLKTLBG_18-nut-xuat-excel-loc-slide-V108.png` |
| VVDTN_04 | **Pass** (vế "thiếu biểu đồ tròn" = không phải lỗi) | (chưa chạy) | `DEV-VVDTN_04-bang-kenh-va-linhvuc-V108.png` |
| XNTGHTVV_03 | **Pass** | (chưa chạy) | `DEV-XNTGHTVV_03-thongbao-inapp-tuchoi-V108.png` |

**Phát hiện đáng chú ý:** đổi từ V1.0.7 sang V1.0.8 **không đổi verdict case nào** trong 3 case đo được ở cả
hai env. Tiền đề "verify trên UAT cũng fail cả thôi" không đúng với bộ 5 case này.

> ## 🔴 CHẤM LẠI 2026-08-05 — sau khi chốt luật "kỳ vọng đối tác khác đặc tả ⇒ luôn hỏi BA"
>
> Lúc chạy, tôi dùng luật cũ (đặc tả nói rõ thì QA tự kết luận "không phải lỗi"). Luật đã đổi: **QA không
> được tự bác đối tác**, dù đặc tả rõ đến đâu — trừ khi **BA đã chốt trước** đúng điểm đó, dẫn được nguồn + ngày.
> Chấm lại bằng luật mới:
>
> | Mã case | Verdict cũ | **Verdict đúng theo luật mới** | Vì sao |
> |---|---|---|---|
> | QLTVV_02 | Pass | **Cần BA** | Vế (b): đối tác kỳ vọng cột Điểm ĐG hiển thị đồng nhất; đặc tả SCR-IV-01 #24 lại quy định đúng kiểu **không** đồng nhất (`—/5` khi chưa có điểm). Kỳ vọng ≠ đặc tả, BA chưa chốt ⇒ hỏi BA. Vế (a) tràn cột và (c) nút xuống dòng vẫn đo là hết lỗi |
> | VVDTN_04 | Pass | **Cần BA** | Vế (a): đối tác kỳ vọng biểu đồ **tròn**; đặc tả UC125 quy định **Bar + Trend**. Kỳ vọng ≠ đặc tả, BA chưa chốt ⇒ hỏi BA. Vế (b) phân rã theo kênh + lĩnh vực vẫn đo là đủ |
> | KTHSYCHTPL_11 | Không phải lỗi | **Không phải lỗi** *(giữ)* | Rơi đúng **ngoại lệ**: BA đã chốt riêng cho chính mã case này ở UAT tuần 2 (changelog:22, 2026-07-16). Note bắt buộc dẫn *BA chốt ngày 16/07/2026* |
> | QLKTLBG_18 | Pass | **Pass** *(giữ)* | Kỳ vọng đối tác (phải có chức năng xuất Excel) **khớp** đặc tả :1952 — không có bất đồng để hỏi |
> | XNTGHTVV_03 | Pass | **Pass** *(giữ)* | Kỳ vọng (CB NV phụ trách phải nhận thông báo) **khớp** BR-NOTIF-01. Vế "kèm lý do" đặc tả im lặng, nhưng bản dựng **có** kèm lý do ⇒ không còn bất đồng để hỏi BA |
>
> **Quy tắc case gộp nhiều vế đã áp:** không có vế nào còn lỗi, nhưng còn ≥1 vế cần-BA ⇒ verdict cả case lấy
> theo vế đó. Cụ thể: 2 case chuyển **Pass → Cần BA**.
>
> **Bài học:** đây là ca "phép đo đúng, luật chấm sai". Số đo ở dưới **không đổi một chữ** — chỉ cách quy đổi
> số đo ra verdict thay đổi. Vì vậy file tiêu chí phải khai rõ *đặc tả nói gì* tách khỏi *kết luận*, để đổi
> luật thì chấm lại được mà không phải đo lại.

---

## Số đo từng case (đo theo file tiêu chí chốt lúc 21:51, không sửa cho khớp kết quả)

### QLTVV_02 — Pass · N=6 bản ghi · M=4 dạng
- Chồng lấn "Điểm ĐG" × "Trạng thái": **0 cặp**; nội dung tràn ra khỏi ô: **0 px**; bảng **có cuộn ngang** (1530 > 1128).
- Bản có điểm hiện **đủ số + sao**: `4.1/5` (4 sao) · `3.3/5` (3 sao). Chưa có điểm: `—/5`. Không giá trị nào >5.
- Cụm hành động: **3 icon** (mắt/bút/thùng rác) cùng `top=20`, left 16/48/80 → **1 hàng**, không xuống dòng.
- M=4 phủ đủ: TVV chưa điểm · TVV có điểm · Chuyên gia · bản ghi ≥2 lĩnh vực (`Đất đai Lao động Thuế +1`).

> **Cảnh báo hụt đã loại:** phép đếm đầu ra "6/6 dòng nút xuống hàng" là do đếm cả thẻ `<a>` bọc ngoài lẫn
> `<button>` bên trong (2 `top` khác nhau). Đo lại chỉ trên `<button>` → 1 hàng. Nếu dừng ở phép đếm đầu thì
> đã log một bug ma.

### KTHSYCHTPL_11 — Không phải lỗi
- Vụ việc `VV-BTP-TW-20260805-004`, `Đã tiếp nhận` → bấm **Kiểm tra hồ sơ** → modal có **6 hạng mục** checklist
  + dropdown kết luận "Đạt — chuyển sang phân công".
- Đánh dấu Đạt cả 6 → **Xác nhận** → toast *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*, trạng thái **giữ
  "Đang kiểm tra"** đúng `srs-fr-05-vu-viec.md:541`, nút đổi thành `Phân công` + `Kiểm tra lại`.
- Dòng thời gian ghi **người + thời điểm**: `Kiểm tra · 05/08/2026 22:18 · CB Nghiệp vụ - Trung ương`.
- `Phân công` là thao tác **riêng**, modal đòi chọn người được phân công → chỉ khi đó mới sang `Đã phân công`.
⇒ Kỳ vọng của đối tác (Đạt phải tự nhảy "Đã phân công") đã bị BA bác từ UAT tuần 2. Web đúng đặc tả.

### QLKTLBG_18 — Pass · M=2
- Màn `/dao-tao/bai-giang/danh-sach` **có nút "Xuất Excel"** trên UI (ảnh đối tác 25/07 trên V1.0 thì chưa có).
- Bấm nút thật → bắt được `POST /api/v1/bai-giangs/export` **200**, blob **7635 byte**.
- **Đọc nội dung tệp** (giải nén zip trong trang): xlsx hợp lệ, sheet có **12 row = 1 tiêu đề + 11 dòng dữ liệu**,
  khớp "Hiển thị 1-11 / 11 kết quả"; tiêu đề `Tên bài giảng · Loại tài liệu · Lĩnh vực · Dung lượng · Công khai
  · Người tạo · Ngày tạo · Mô tả`; dòng đầu/cuối trùng đúng bảng trên màn.
- **Phép 2 — có lọc:** lọc `Loại tài liệu = Slide` → màn còn 3 dòng → xuất lại: **4 row = 1 tiêu đề + 3 dòng**,
  đúng 3 tên trên màn ⇒ xuất **theo bộ lọc hiện tại**.
- Không chấm Fail vì cột/tên tệp (đặc tả im lặng, đã khai trước ở mục 2 file tiêu chí).

### VVDTN_04 — Pass · M=2 chiều
- `/bao-cao` · loại `BC Vụ việc đã tiếp nhận` · kỳ **Năm** 01/01–31/12/2026 · Toàn quốc · tài khoản **CB NV**
  (không dùng QTHT như video đối tác).
- **Tổng vụ việc: 44** · **theo kênh:** Trực tiếp 41, Doanh nghiệp 3 · **theo lĩnh vực:** Thương mại 16 (36,4%),
  Dân sự 13 (29,5%), Lao động 12 (27,3%), Thuế 3 (6,8%) · theo đơn vị: 34/4/3/3.
- Cả 3 chiều **cộng đúng 44** → số đo tự nhất quán.
- `Thời điểm tạo: 05/08/2026 22:15` ⇒ không phải cache cũ (bẫy cache server-side đã loại).
- Biểu đồ hiện là **Bar + Trend**, đúng `srs-fr-11-bao-cao.md:1065` UC125. **Không có biểu đồ tròn là đúng** —
  Donut chỉ gán cho UC124/UC127/UC131.
⇒ Vế (a) của phiếu: **không phải lỗi**. Vế (b): có đủ phân rã theo kênh và theo lĩnh vực.

### XNTGHTVV_03 — Pass · M=2 kênh
Đóng được **GAP mà bằng chứng đối tác không đóng nổi** (video của họ không cho biết vụ việc nào bị từ chối và
ai là CB NV phụ trách) bằng cách **tự dựng tiền đề**, nên biết chắc ai đáng lẽ phải nhận thông báo:
1. `cbnv_tw` phân công `VV-BTP-TW-20260805-004` cho `QA TVV Seed28 Active` → `Đã phân công`.
2. Đăng nhập `qa_tvvseed28` → **Từ chối** kèm lý do → toast *"Đã từ chối phân công"*; sau đó tài khoản này gọi
   API vụ việc trả **403 `ERR-AUTH-VPD-00-04`** ⇒ quyền đã bị gỡ đúng.
3. Vụ việc về **`DA_TIEP_NHAN`** ✓
4. **In-app:** `cbnv_tw` có thông báo *"Người hỗ trợ đã từ chối tham gia vụ việc - VV-BTP-TW-20260805-004"*,
   chưa đọc, 15:21:26 ✓
5. **Email:** MailHog có thư tới `cbnv_tw@htpldn.test` cùng thời điểm ✓
- Nội dung cả 2 kênh **chứa nguyên văn lý do từ chối** + câu "Vụ việc đã chuyển về trạng thái "Đã tiếp nhận"
  để phân công lại".
⇒ Nhánh **"CHUYỂN BA nếu thông báo đến mà không kèm lý do" không kích hoạt** — bản dựng này có kèm lý do,
nên câu hỏi BA mà file tiêu chí dự phòng trở thành không cần thiết.

---

## Dữ liệu đã thay đổi trên env dev (để truy vết)

| Bản ghi | Thay đổi | Vì sao |
|---|---|---|
| TVV `TVV-BTP-TW-0002` (`98cfd963-3cd3-4c8a-bfa9-625460824d6d`) | `linhVucIds` 1 → 4 (Thương mại, Thuế, Lao động, Đất đai) | 42 TVV trên dev **không có bản ghi nào ≥2 lĩnh vực** → không phủ nổi dạng (4) của QLTVV_02, mà đây đúng là dạng gây tràn cột đối tác phản ánh |
| VV `VV-BTP-TW-20260805-004` | `DA_TIEP_NHAN` → `DANG_KIEM_TRA` → `DA_PHAN_CONG` → (bị từ chối) → `DA_TIEP_NHAN` | dựng tiền đề cho KTHSYCHTPL_11 và XNTGHTVV_03 |

---

## Lỗi của chính flow mà lượt chạy này phơi ra

1. **Không có ô "môi trường + bản dựng" trong file tiêu chí, và không có quy tắc khi đổi env giữa chừng.**
   Phải tự chế mục `SỬA ĐỔI #1`. Cần bổ sung vào FLOW 04 Giai đoạn A: file tiêu chí bắt buộc ghi env + bản
   dựng, và **Pass chỉ có hiệu lực cho bản dựng đó** — Pass ở dev là *Pass tạm* cho tới khi bản đó lên env đối tác.
2. **Quy tắc "công cụ chặn → DỪNG hỏi user" không phân biệt công cụ ĐỌC với công cụ GHI.**
   `fetch_evidence.py` chặn tab `bug` bằng allowlist vốn viết cho script ghi, dù nó chỉ tải file về. Cần tách:
   công cụ ghi bị chặn → dừng hỏi; công cụ chỉ đọc bị chặn → được nới, ghi lại lý do.
3. **Cổng "độ phủ M dạng" không nói phải làm gì khi dữ liệu dạng đó KHÔNG TỒN TẠI.** Chỉ có 2 lối: seed hoặc
   bỏ trống. Cần ghi rõ: **được phép seed**, nhưng bắt buộc khai bản ghi nào bị đổi, đổi gì, trên env nào
   (vì seed là mutate môi trường của người khác).
4. **Không có cảnh báo ảnh `fullPage` làm trang re-render.** Ảnh fullPage đầu tiên của VVDTN_04 chụp ra khung
   xám loading → bằng chứng vô giá trị. Cần thêm vào mục "artifact hợp lệ": ảnh phải đọc lại xem có đúng nội
   dung không, đặc biệt khi chụp fullPage trang có biểu đồ.
5. **Quy tắc "bộ bắt toast CẤM lọc trùng" thiếu vế đếm.** Không lọc trùng thì 1 toast luôn ra **2 bản ghi cùng
   `luc`** (node bọc + node trong). Cần bổ sung: đếm toast theo **mốc thời gian khác nhau**, không theo độ dài
   mảng — nếu không sẽ log bug "double toast" ma ở mọi case.
6. **Chưa làm phần "Đầu ra" của FLOW 04.** Flow đòi Pass cũng phải tạo bug entry + khối CÁCH VERIFY để case
   chuyển vĩnh viễn sang FLOW 03. Lượt này mới đo, **chưa tạo hồ sơ** cho 5 case — còn nợ.
