# Audit verdict `Reject` — tab UAT_TGPL Doanh Nghiệp-tuần 4

**Ngày audit:** 2026-07-27 17:30–17:45 · **Người audit:** QA (Claude) · **Env re-verify:** `https://18.143.165.120.nip.io` · **Account:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW)
**Phạm vi:** toàn bộ 3 dòng có `Trạng thái dev fix 1` chứa `Reject` trong tab tuần 4 (không có dòng nào khác).
**SRS đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md` (mọi số dòng dưới đây đã MỞ FILE verify, không quote từ trí nhớ).
**Trạng thái ghi sheet:** ✅ **ĐÃ GHI** (user duyệt 2026-07-27 17:47). 3 dòng 28/30/31 → `Trạng thái dev fix 1` = **`BA confirm`** + note mới ở `DEV phản hồi lần 1`; cột `Verify` (Q) **không đụng**, giữ TRỐNG. Đọc lại xác nhận khớp; tab tuần 4 hiện **còn 0 dòng mang `Reject`**. Dấu vết + giá trị cũ: `tools/sheet_write.log` (3 dòng 17:46–17:47).

---

## Kết luận tổng

| Row | Mã TC | P hiện tại | Audit | P đề xuất | Lý do 1 câu |
|:-:|---|---|:-:|---|---|
| 28 | KHTHCTHTPLDN_03 | `Reject` | ❌ SAI | `BA confirm` | Đối tác quan sát ĐÚNG; tranh chấp là kỳ vọng vs đặc tả → protocol cấm Reject. Cùng bảng đó QA đã tự chứng minh thiếu cột `Lĩnh vực pháp lý`. |
| 30 | KHTHCTHTPLDN_08 | `Reject` | ❌ SAI | `BA confirm` | Kỳ vọng của đối tác lấy từ CHÍNH bảng `:1193–1207` của SRS; SRS im lặng về việc nút nằm ở dòng hay trang chi tiết. |
| 31 | KHTHCTHTPLDN_12 | `Reject, BA confirm` | ⚠️ SAI phần Reject | `BA confirm` | 2 điểm bị Reject dựa trên cùng lỗ hổng căn cứ (UX-spec MH-15.1 không có) mà 2 điểm kia đã được đẩy sang BA; riêng "Chờ PD" còn bị `:1174` phản lại. |

**Cột `Verify` (Q):** cả 3 giữ **TRỐNG** — không case nào thuộc dạng "không tái hiện + đối tác có bằng chứng", nên `Resolved` không áp dụng.

### Lỗi hệ thống lặp ở cả 3 case

QA dùng **"web khớp / không trái SRS v3.5"** làm căn cứ `Reject`. Protocol `QA_VERIFY_PROTOCOL.md` §Verdict chỉ cho `Reject` khi **chứng minh được đối tác thao tác/hiểu sai** và **lỗi đối tác báo không có thật** (bất đồng về THỰC TẾ), và ghi thẳng: *"**KHÔNG** dùng `Reject` cho bất đồng kỳ vọng vs SRS (dù web đúng SRS)"* + *"evidence đúng actual mà chỉ tranh chấp expected/spec → `BA confirm`, không Reject"*.

Trong cả 3 case, **quan sát hiện trạng của đối tác đều đúng** — chính cond-table của QA viết "trùng khít" (_03), "đúng như phiếu mô tả" (_08), "quan sát đúng" (_12), và tôi đã re-verify LIVE lại đúng như vậy. Không có case nào QA chứng minh đối tác thao tác sai hay bịa lỗi.

---

## Artifact re-verify LIVE (2026-07-27, env nip.io, `cbnv_tw`)

| Artifact | Nội dung đã mở đọc | Phục vụ case |
|---|---|---|
| `AUDIT-03-08-danh-sach-9-cot-va-cot-hanh-dong.png` | Màn `/ct-htpldn/danh-sach`, tab "Tất cả 8". Tiêu đề bảng đọc rõ 9 cột; cột Hành động mọi dòng chỉ 1 biểu tượng con mắt | _03, _08 |
| `AUDIT-12-chi-tiet-dau-trang-va-phan-thong-tin-day-du.png` (full-page) | Chi tiết `CT-20260721-0002` (Đang thực hiện): thanh điều hướng, tiêu đề + nhãn, 6 bước tiến trình (bước 2 = "Chờ PD"), **trọn phần Thông tin gồm cả Đối tượng thụ hưởng / Thời gian / Ngân sách**, nút [Tạm dừng] ở thanh cố định | _12, _08 |

Đọc DOM bằng mã lệnh (phương pháp thứ hai, không chỉ nhìn ảnh):

- **Tập cột danh sách (9 cột):** `Mã CT · Tên chương trình · Mục tiêu · Thời gian · Ngân sách · Đơn vị · Trạng thái · Số đợt BC · Hành động` → **không có** `Lĩnh vực pháp lý`, **không có** `Đợt báo cáo`, **có** `Số đợt BC`.
- **Cột Hành động:** 8/8 dòng chỉ có `Xem chương trình <mã>` (dòng Đang thực hiện `CT-20260721-0002` **không** có [Tạm dừng]).
- **Đầu trang chi tiết:** breadcrumb `Trang chủ / Chương trình HTPLDN / Chi tiết`; tiêu đề `CT-20260721-0002`; 6 bước `["Dự thảo" finish, "Chờ PD" finish, "Đã duyệt" finish, "Công bố" finish, "Thực hiện" process, "Hoàn thành" wait]`.
- **Phần Thông tin (chi tiết):** `Đơn vị · Mã CT · Tên chương trình · Lĩnh vực pháp lý · Mục tiêu · Đối tượng thụ hưởng · Thời gian bắt đầu · Thời gian kết thúc · Ngân sách (VNĐ) · Ghi chú · File đính kèm` → 4 thông tin phiếu nói "thiếu" đều **đang hiển thị**.
- **Thanh hành động trang chi tiết theo trạng thái** (đọc toàn trang, gồm thanh cố định): Đã duyệt (`CT-20260725-0002`) → `[Công bố lên Cổng PLQG] [Bắt đầu thực hiện]` · Đã công bố (`CTHTPL-SEED-0001`) → `[Hủy công bố] [Bắt đầu thực hiện]` · Đang thực hiện (`CT-20260721-0002`) → `[Tạm dừng]`.

⇒ **Mọi dữ kiện THỰC TẾ trong 3 note của QA đều đúng.** Sai lệch nằm ở **nhãn verdict** và ở **mấy chỗ suy luận vượt căn cứ**, không ở phép đo.

**Kiểm lại citation (mở file, không quote từ trí nhớ):** `:1113` `:618` `:1096` `:1107` `:1120` `:1128` `:1132` `:1136` `:1138` — **đúng nguyên văn**. Hai chỗ cần chỉnh nhỏ trong `cond/KHTHCTHTPLDN_08.md`: trích *"`:262` bước 1 — Kiểm tra quyền CB PD"* nhưng `:262` là **dòng tiêu đề bảng**, nội dung đó ở **`:264`**; `:274` (mã lỗi `ERR-XI-01-HT-01` — *"Chỉ CB Phê duyệt mới được hoàn thành CT"*) thì đúng. Không ảnh hưởng kết luận, nhưng phải sửa để lần sau không quote lệch.
Ngoài ra: `grep -rniE "thông tin nhanh|thong tin nhanh" srs-v3.5/` → **0 hit**; `find . -iname "*dac-ta-man-hinh*"` → **không tồn tại** (xác nhận lỗ hổng căn cứ mà BA-20 nêu là thật).

---

## Case 28 — KHTHCTHTPLDN_03 · `Reject` → đề xuất `BA confirm`

**Phiếu ghi:** *"SRS yêu cầu có cột 'Đợt báo cáo' - Liên kết nhanh mở màn hình 'Đợt báo cáo định kỳ' độc lập nhưng bảng danh sách không có cột thông tin trên mà hiển thị cột 'Số đợt BC'"*.

**Đo lại (live):** đúng — không có cột "Đợt báo cáo", có cột "Số đợt BC". Quan sát của đối tác **không sai một chữ**.

**Vì sao `Reject` không đứng được — 4 điểm:**

1. **Protocol.** Đối tác quan sát đúng, chỉ khác nhau ở **kỳ vọng** (có cột + liên kết nhanh hay không). §Verdict: *"Expected/kỳ vọng đối tác KHÁC SRS (**kể cả khi SRS đã ghi rõ**) → bất đồng về ĐẶC TẢ → `BA confirm`, QA KHÔNG tự Reject"*. QA chưa chứng minh đối tác thao tác/hiểu sai.
2. **Note tự mâu thuẫn.** Note gắn nhãn "❌ Không phải bug" nhưng câu cuối mục 1 lại viết *"Nhờ đối tác xác nhận lại giúp bản đang dùng để hai bên thống nhất"* — một câu hỏi còn mở không thể nằm dưới kết luận "không phải bug".
3. **SRS tự mâu thuẫn về vị trí Đợt BC**, nên lập luận "đối tác đối chiếu bản trước 3.5.2" chưa sạch:
   - `:618` — *"(v3.5.2: tab 'Đợt báo cáo' độc lập, không drill-down từ CT)"*.
   - `:1101` — *"**Trang chi tiet CT:** Tab 'Thong tin' ... + Tab 'Dot bao cao' (bang dot BC + drill-down dot -> form lap BC ...)"*, và cả bảng `:1143–1166` mô tả chi tiết tab đó **vẫn nằm trong SCR-XI-01**.
   - Thực tế web: trang chi tiết CT **chỉ có 1 tab "Thông tin"**, không có tab "Đợt báo cáo" (đúng `:618`, trái `:1101`).
   - ⇒ Bản đặc tả đang hiệu lực **còn giữ song song 2 mô hình**. Protocol: *"mâu thuẫn giữa các nguồn ... → `BA confirm`"*.
4. **Chính case này đang FAIL theo Kết quả mong đợi của nó.** Kết quả mong đợi row 28 là *"Hệ thống hiển thị các trường thông tin giống với thiết kế"*. `:1113` liệt kê **10** cột, web có **9** — thiếu đúng `Linh vuc phap ly` (live-verified). QA đã tách sang `KHTHCTHTPLDN_OOS_05` (đang `Open`, Bug `BUG-CT-BANG-THIEU-COT-LINHVUC`), nhưng để dòng gốc là "❌ Không phải bug" thì với đối tác đọc sheet, thông điệp là "bảng danh sách không có vấn đề gì" — sai với chính kết luận của QA.

**Đề xuất:**

- **P = `BA confirm`** (giữ OOS_05 làm dòng dev-facing cho cột thiếu). Nếu bạn muốn chính dòng 28 gánh luôn phần lỗi thay vì để ở OOS_05 → dùng **`Open, BA confirm`**; khi đó phải ghi rõ trong note là cùng một lỗi với OOS_05 để dev không log trùng.
- **Q = TRỐNG** (không thay đổi).
- **Note đề xuất** (BA confirm ⇒ theo protocol PHẢI giữ mã FR/UC + số dòng):

```
⚠️ Cần BA xác nhận.

Quan sát của phiếu là đúng: bảng danh sách chương trình không có cột "Đợt báo cáo" mà hiển thị cột "Số đợt BC". QA đã kiểm lại ngày 27/07/2026 bằng tài khoản cbnv_tw (CB Nghiệp vụ - Trung ương, BTP · TW).

1) Vì sao phải để BA chốt thay vì kết luận đúng/sai ngay.
- FR-XI-01 (UC160) — SCR-XI-01, dòng 1113: bảng danh sách được liệt kê 10 cột, cột thứ 9 ghi "Số đợt BC". Không có mục nào tên "Đợt báo cáo" và không mô tả liên kết nhanh từ dòng chương trình.
- Nhưng cùng bản đặc tả này còn hai chỗ chưa thống nhất về màn Đợt báo cáo: dòng 618 ghi "v3.5.2: tab Đợt báo cáo độc lập, không drill-down từ CT", còn dòng 1101 và bảng dòng 1143-1166 vẫn mô tả "Đợt báo cáo" là một thẻ nằm trong trang chi tiết chương trình. Thực tế trang chi tiết chỉ có thẻ "Thông tin".
- Câu hỏi cho BA: bản đang hiệu lực chốt theo hướng nào, và có bổ sung liên kết nhanh từ dòng chương trình sang màn Đợt báo cáo định kỳ hay không? Nếu chốt theo dòng 618 thì đề nghị BA gỡ phần tab Đợt báo cáo ở dòng 1101/1143-1166 để đối tác không mở lại case ở vòng sau.

2) Một lỗi khác trên cùng bảng, đã chuyển dev.
- Đối chiếu từng mục với dòng 1113: web có 9 cột, thiếu đúng cột "Lĩnh vực pháp lý". Dữ liệu đã có sẵn (tệp Excel xuất từ chính màn này in ra Đất đai, Thuế, Lao động) nên không phải do thiếu dữ liệu. Lĩnh vực pháp lý là trường bắt buộc khi tạo chương trình (dòng 1128).
- QA đã mở dòng riêng mã KHTHCTHTPLDN_OOS_05 cho dev xử lý. Bug ID: BUG-CT-BANG-THIEU-COT-LINHVUC.
```

---

## Case 30 — KHTHCTHTPLDN_08 · `Reject` → đề xuất `BA confirm`

**Phiếu mong:** trên **dòng** danh sách — Đang thực hiện → [Tạm dừng]; Đã duyệt / Đã công bố → [Kích hoạt]; Dự thảo → [Sửa].

**Đo lại (live):** cột Hành động 8/8 dòng chỉ có [Xem] → quan sát của đối tác **đúng**. Trang chi tiết có đủ nút theo trạng thái (đã đọc toàn trang, gồm thanh cố định) → dữ kiện của QA cũng **đúng**.

**Vì sao `Reject` không đứng được:**

1. **Kỳ vọng của đối tác lấy từ CHÍNH đặc tả, không phải họ tự nghĩ ra.** SRS có bảng `#### Bang hanh dong theo trang thai CT` (`:1193`–`:1207`) map trạng thái → nút, **không nói nút nằm ở đâu**:
   - `:1202` `DA_DUYET | [Kich hoat] | DANG_THUC_HIEN` · `:1204` `DA_CONG_BO | [Kich hoat]` → khớp ý 2 của phiếu.
   - `:1205` `DANG_THUC_HIEN | [Tam dung] | TAM_DUNG | Modal ly do` → khớp ý 1 của phiếu.
   - `:1211` *"Sua/Xoa CT: chi khi DU_THAO"* → khớp ý 3 của phiếu.
   ⇒ Kết luận trong cond-table hiện tại (*"kết quả mong đợi đặt sai chỗ so với đặc tả v3.5"*) là **suy luận vượt căn cứ**: SRS không có dòng nào nói các nút này **không được** nằm trên dòng danh sách.
2. **SRS im lặng đúng chỗ đang tranh chấp.** `:1113` chỉ ghi cột `Hanh dong (conditional)` — không liệt kê tập nút, không nói "conditional" theo tiêu chí gì. Protocol §Ca biên: *"SRS chỉ nêu nghiệp vụ chung, app đáp ứng cách khác → `BA confirm`"*.
3. **Note của QA tự mô tả đúng tình huống BA confirm.** Mục 5 viết: *"Đây là đề xuất cải tiến trải nghiệm, không phải sai đặc tả. QA đề nghị đối tác nêu thành yêu cầu thay đổi để BA cân nhắc"* — đó chính là định nghĩa `BA confirm` (*"để BA chốt có bổ sung/đổi spec không"*), không phải `Reject`.
4. **Note đang bỏ sót bằng chứng có lợi cho đối tác.** Note nói *"Cột Hành động ... không liệt kê nút cụ thể nào"* nhưng không nhắc bảng `:1193–1207`. Bỏ một bảng SRS ủng hộ đối tác ra khỏi note "❌ Không phải bug" là thiếu công bằng khi đối chiếu.
5. **Điểm bất đối xứng nên đưa vào câu hỏi BA:** `:1211` gộp *"Sửa/Xóa CT: chỉ khi DU_THAO"*, mà ảnh của đối tác cho thấy dòng Dự thảo **có** biểu tượng xóa nhưng **không có** Sửa. (Env QA hiện không còn bản ghi Dự thảo nên chỉ ghi nhận từ ảnh đối tác, chưa re-verify được — không dùng làm căn cứ chấm lỗi.)

**Đề xuất:** P = `BA confirm` · Q = TRỐNG.

**Note đề xuất:**

```
⚠️ Cần BA xác nhận.

Quan sát của phiếu là đúng: cột "Hành động" trên dòng danh sách chỉ có nút Xem, không có Tạm dừng / Kích hoạt / Sửa. QA đã kiểm lại ngày 27/07/2026 bằng cbnv_tw (CB Nghiệp vụ - Trung ương) và cbpd_tw (CB Phê duyệt - Trung ương).

1) Về chức năng nghiệp vụ: không thiếu.
- Các nút vòng đời có đủ ở thanh hành động của trang chi tiết chương trình, đúng theo từng trạng thái: Đã duyệt có [Công bố lên Cổng PLQG] + [Bắt đầu thực hiện]; Đã công bố có [Hủy công bố] + [Bắt đầu thực hiện]; Đang thực hiện có [Tạm dừng], và với tài khoản Cán bộ phê duyệt thì thêm [Hoàn thành].
- FR-XI-01 (UC160) — SCR-XI-01 mô tả các nút này ở thanh hành động trang chi tiết: dòng 1132 (nhóm nút khi Dự thảo), 1136 ([Kích hoạt], nhãn nguyên văn "Bắt đầu thực hiện"), 1138 ([Tạm dừng]). Riêng [Hoàn thành] chỉ dành cho Cán bộ phê duyệt (dòng 264 và 274).

2) Vì sao vẫn phải để BA chốt chứ không kết luận phiếu sai.
- Kỳ vọng của phiếu trùng với bảng "Hành động theo trạng thái CT" trong chính bản đặc tả: dòng 1202 và 1204 ([Kích hoạt] khi Đã duyệt / Đã công bố), dòng 1205 ([Tạm dừng] khi Đang thực hiện), dòng 1211 (Sửa/Xóa chỉ khi Dự thảo). Bảng này nêu trạng thái nào có nút nào nhưng KHÔNG quy định nút nằm trên dòng danh sách hay ở trang chi tiết.
- Cột Hành động của bảng danh sách chỉ được mô tả là "Hành động (tùy điều kiện)" ở dòng 1113, không liệt kê tập nút.
- Câu hỏi cho BA: cột Hành động trên dòng danh sách có phải hiển thị thêm các nút theo trạng thái (Kích hoạt / Tạm dừng / Sửa) không, hay chỉ giữ nút Xem và mọi hành động thực hiện ở trang chi tiết? Nếu chốt phương án chỉ có Xem, đề nghị BA ghi rõ tập nút của cột này vào dòng 1113 để đối tác không mở lại case ở vòng sau.
- Một điểm liên quan cần chốt cùng lúc: dòng 1211 gộp "Sửa/Xóa CT: chỉ khi Dự thảo", nhưng dòng Dự thảo hiện chỉ có biểu tượng xóa, không có Sửa (việc sửa thực hiện trong trang chi tiết). Đề nghị BA xác nhận cách bày này là đúng ý.
```

---

## Case 31 — KHTHCTHTPLDN_12 · `Reject, BA confirm` → đề xuất `BA confirm`

Phiếu nêu 4 điểm; điểm 1–2 đã chuyển BA-20 (đúng). Vấn đề ở **điểm 3 và 4 bị Reject**.

**Đo lại (live) — cả 4 điểm phiếu quan sát đều đúng:** breadcrumb `Trang chủ / Chương trình HTPLDN / Chi tiết` (không có mã CT) · tiêu đề `CT-20260721-0002` (không có tên CT) · bước 2 = `Chờ PD` · không có khối tóm tắt riêng (nhưng 4 thông tin đều hiển thị trong phần Thông tin).

**Điểm 3 — "Chờ PD": Reject là RỦI RO, không phải chắc chắn.**

- Căn cứ QA dùng: `:1120` — *"| 9 | content | Thanh tien trinh (C17) | progress-bar | [Du thao] -- [Cho PD] -- [Da duyet] -- [Cong bo] -- [Thuc hien] -- [Hoan thanh] |"*. Đúng, có "Cho PD".
- **Nhưng cùng file, `:1169`–`:1174` có bảng `#### Bang nhan trang thai SM-KH-CTHTPL` quy định nhãn chuẩn của trạng thái: `| CHO_PHE_DUYET | Cho phe duyet | Vang | --color-warning |`** — tức đặc tả **có** một dòng quy định nhãn đầy đủ "Chờ phê duyệt", đúng như kỳ vọng của đối tác.
- **Bản thân web cũng không nhất quán** (live-verified cùng phiên): thẻ lọc ở màn danh sách ghi **"Chờ phê duyệt"**, còn bước 2 của thanh tiến trình ghi **"Chờ PD"**.
- ⇒ Hai dòng SRS cho hai dạng nhãn khác nhau → protocol: *"mâu thuẫn giữa các nguồn → `BA confirm`"*. Câu *"nếu dev đổi thành Chờ phê duyệt thì lại lệch với đặc tả"* + *"đề nghị dev không sửa"* trong note và trong BA-20 (dòng 970) là **kết luận vượt căn cứ** và có thể khoá sai hướng fix.

**Điểm 4 — khối thông tin nhanh: cùng lỗ hổng căn cứ với điểm 1–2, nhưng bị chấm khác.**

- QA Reject điểm 4 với lý do *"SRS không có thành phần nào tên khối thông tin nhanh"* (đúng — tôi đã grep toàn bộ `srs-v3.5/`, **0 hit** cho "thông tin nhanh").
- Nhưng chính QA đã dùng lập luận ngược lại cho điểm 1–2: SRS không mô tả ⇒ *"không có căn cứ để chấm"* ⇒ đẩy BA, vì mức chi tiết đó thuộc `dac-ta-man-hinh-chuc-nang-v2.md — MH-15.1` mà `:1096` trỏ tới và **QA không có** (tôi đã `find` toàn repo: file không tồn tại).
- Cụm 4 thông tin (Ngân sách / Thời gian / Đơn vị / Đối tượng) là **bố cục** — cùng loại chi tiết, cùng nguồn căn cứ thiếu. Cùng một lỗ hổng mà 2 điểm → BA, 2 điểm → Reject là **không nhất quán**; phần "thông tin không mất" là đúng và nên giữ trong note, nhưng nó chỉ hạ severity, không biến thành "đối tác báo lỗi không có thật".

**Đề xuất:** P = `BA confirm` (bỏ `Reject`) · Q = TRỐNG · bổ sung 2 câu hỏi vào **BA-20** và sửa dòng 970 (bỏ khuyến nghị "dev không sửa").

**Note đề xuất:**

```
⚠️ Cần BA xác nhận.

Phiếu nêu 4 điểm. QA đo tách riêng từng điểm ngày 27/07/2026 bằng cbnv_tw (CB Nghiệp vụ - Trung ương, BTP · TW), có kiểm lại bằng cbpd_tw để chắc đầu trang không đổi theo quyền. Cả 4 điểm quan sát của phiếu đều đúng; vướng là chưa có căn cứ đủ rõ để chấm đúng/sai, nên QA gửi BA chốt.

1) Hai điểm về đầu trang.
- Thanh điều hướng hiện là "Trang chủ / Chương trình HTPLDN / Chi tiết", không kèm mã chương trình.
- Tiêu đề trang hiện chỉ là mã chương trình kèm nhãn trạng thái; tên chương trình nằm ở dòng dưới trong phần Thông tin.
- FR-XI-01 (UC160) — SCR-XI-01 chỉ quy định thanh điều hướng cho trang danh sách (dòng 1107); bảng thành phần trang chi tiết bắt đầu từ dòng 1120 và không có dòng nào cho thanh điều hướng hay định dạng tiêu đề. Mức chi tiết này thuộc bản đặc tả màn hình mà đặc tả trỏ tới ở dòng 1096 (MH-15.1) — bản này QA không có trong bộ tài liệu đối chiếu.

2) Điểm hiển thị viết tắt "Chờ PD".
- Thanh tiến trình đang ghi "Chờ PD" đúng như phiếu quan sát. Cùng lúc, thẻ lọc ở màn danh sách lại ghi đầy đủ "Chờ phê duyệt".
- Bản đặc tả có hai chỗ chưa thống nhất: dòng 1120 viết thanh tiến trình dạng viết tắt "[Chờ PD]", còn bảng nhãn trạng thái ở dòng 1169-1174 quy định nhãn của trạng thái này là "Chờ phê duyệt".
- Câu hỏi cho BA: nhãn hiển thị trên thanh tiến trình lấy theo bảng nhãn trạng thái (dòng 1174) hay giữ dạng viết tắt ở dòng 1120? Cần chốt để hai chỗ trong phần mềm hiển thị thống nhất.

3) Điểm thiếu khối thông tin nhanh.
- Không có khối tóm tắt riêng ở đầu trang, nhưng cả 4 thông tin phiếu nói thiếu đều đang hiển thị đầy đủ trong phần Thông tin ngay bên dưới: đơn vị chủ trì, thời gian bắt đầu và kết thúc, ngân sách, đối tượng thụ hưởng. QA đã đọc từng cặp nhãn và giá trị bằng mã lệnh, không chỉ nhìn ảnh.
- Bản đặc tả liệt kê 4 thông tin này là các trường của phần Thông tin (dòng 1124, 1125, 1126, 1127, 1129), không có thành phần nào tên "khối thông tin nhanh".
- Câu hỏi cho BA: bản đặc tả màn hình (MH-15.1) có quy định khối tóm tắt riêng ở đầu trang không? Nếu không, đề nghị BA bổ sung mô tả đầu trang chi tiết vào đặc tả để chốt dứt điểm.

4) QA đã kiểm chéo trạng thái.
- Ảnh của phiếu chụp chương trình ở Dự thảo, QA đo trên chương trình Đang thực hiện. Để chắc kết luận không phụ thuộc điều đó, QA mở thêm 3 chương trình ở Đã duyệt, Đã công bố và Hoàn thành: thanh điều hướng, dạng tiêu đề và thanh tiến trình đều giữ nguyên cách hiển thị.
```

---

## Việc đã làm sau khi user duyệt (2026-07-27 17:46–17:55)

| # | Việc | Trạng thái | File / công cụ |
|:-:|---|:-:|---|
| 1 | Ghi `BA confirm` + note mới cho 3 dòng 28/30/31 (dry-run trước, đọc lại sau) | ✅ | `tools/sheet_write.py` · dấu vết `tools/sheet_write.log` |
| 2 | Sửa 3 cond-table: dòng **Kết luận** Reject → BA confirm + căn cứ mới (`:1193–1207`, `:1169–1174`, `:1101` vs `:618`); sửa citation lệch `:262` → `:264` | ✅ | `reverify-week-4/cond/KHTHCTHTPLDN_{03,08,12}.md` |
| 3 | 3 note partner-facing mới (giữ nguyên file note Reject cũ để còn dấu vết) | ✅ | `cond/note-KHTHCTHTPLDN_{03,08,12}-baconfirm.txt` |
| 4 | **BA-20:** thêm mâu thuẫn `:1120` vs `:1174` + câu hỏi (c) về nhãn trạng thái; **gỡ** ghi chú "đề nghị dev không sửa"; điểm 3+4 chuyển từ *không phải lỗi* → *cần BA*; verdict → `BA confirm` | ✅ | `ba-confirmation-needed-week-4.md` |
| 5 | **BA-23** (mô hình Đợt báo cáo `:618` vs `:1101`/`:1143-1166` + liên kết nhanh) và **BA-24** (tập nút cột Hành động + bất đối xứng Sửa/Xóa `:1211`) — mở mới, kèm bảng verify UI + citation | ✅ | `ba-confirmation-needed-week-4.md` |
| 6 | Cập nhật đầu file BA: tổng 22 → **24 câu hỏi**, bảng chỉ mục, phân dạng (BA-23 = dạng B; BA-20 = A có 1 điểm dạng B), ghi rõ lý do bổ sung | ✅ | `ba-confirmation-needed-week-4.md` |

**Chưa làm (chờ bạn quyết):** ghi 2 mâu thuẫn SRS vào `tasks/srs-contradictions.md`. Bỏ qua có chủ ý — 2 mâu thuẫn này đã được track ở **BA-20** (`:1120` vs `:1174`) và **BA-23** (`:618` vs `:1101`/`:1143-1166`); ghi thêm vào tracker sẽ tạo 2 nguồn theo dõi song song cho cùng 1 việc. Nói bạn nếu muốn track cả ở đó (dùng ID kế tiếp **SRS-C-010**, **SRS-C-011**).

**Không đề xuất đổi:** cột `Verify` (Q) của cả 3 dòng — giữ TRỐNG. Không có dữ kiện đo nào của QA cần rút lại; toàn bộ phép đo đã được re-verify LIVE và khớp.
