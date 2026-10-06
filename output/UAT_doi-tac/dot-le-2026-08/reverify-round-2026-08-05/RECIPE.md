# RECIPE — re-verify vòng dev-fix 05/08/2026 (env nip.io, build V1.0.6)

> Đọc HẾT file này trước khi chạy. Mọi bước đã được kiểm chứng thật trên case mẫu `SLHDVM_07` (row 192,
> tuần 3) — đã Pass và ghi sheet thành công. Đừng tự chế quy trình khác.

## 0. Bối cảnh (đọc để không kết luận sai)

- Dev build **V1.0.6** lên `https://18.143.165.120.nip.io` rồi lật cột `Trạng thái dev fix 1/2` về
  `dev done`, nhờ QA verify lại. Đối tác CHƯA phản ánh vòng 2 → cột `Trạng thái 2` / `Kết quả thực tế
  lần 2` trống là ĐÚNG bản chất.
- Vòng đo trước (04/08, bản V1.0.5, môi trường khác) kết luận FAIL. **KHÔNG được chép lại kết luận cũ** —
  V1.0.6 đã sửa nhiều thứ. Phải đo lại thật.
- Ô note (`DEV phản hồi lần 1` / `DEV phản hồi lần 2`) chứa **tiêu chí PASS/FAIL của chính phiếu đó**.
  Đọc và làm ĐÚNG theo đó. **Cấm tự nghĩ tiêu chí.**

## 1. Tiêu chí lấy ở đâu

- Có khối `── CÁCH VERIFY sau Dev fix ──` → dùng nguyên khối đó (`Precondition` / `✅ PASS khi` /
  `❌ FAIL nếu` / dòng `⚠️` dặn KHÔNG chấm FAIL).
- Không có khối đó → dùng phần **"Phần còn lỗi"** trong note làm điều kiện FAIL, phần **"Phần đã hết lỗi"**
  làm mốc đã đạt. Chỉ verify đúng phạm vi note nêu.
- Dòng `⚠️` dặn "đừng chấm FAIL vì điều X" → tuyệt đối tôn trọng, kể cả khi thấy X.

## 2. Đăng nhập (1 lần/phiên)

```
new_page https://18.143.165.120.nip.io/login
wait_for ["Nhập tên đăng nhập","Đăng nhập"]
take_snapshot → fill_form: Tên đăng nhập = cbnv_tw , Mật khẩu = Test@1234
click [Đăng nhập] → màn OTP
```
Lấy OTP (chạy NGAY sau khi bấm Đăng nhập, lấy thư mới nhất đúng hộp thư của tài khoản):
```bash
curl -s --max-time 15 "http://18.143.165.120:8025/api/v2/messages?limit=5" | python3 -c "
import sys,json,re
d=json.loads(sys.stdin.read())
for m in d['items'][:5]:
    to=m['To'][0]['Mailbox']+'@'+m['To'][0]['Domain']
    o=re.search(r'\b(\d{6})\b', m['Content']['Body'])
    print(m['Created'],'|',to,'|',o.group(1) if o else 'n/a')
"
```
`take_snapshot` → `fill_form` 6 ô OTP (mỗi ô 1 chữ số) → tự chuyển `/dashboard`.

Xác nhận build: `evaluate_script (() => document.body.innerText.match(/V\d+\.\d+\.\d+/)[0])` → phải là **V1.0.6**.
Khác → DỪNG, báo lại.

**Rule 3:** sau khi đăng nhập, điều hướng bằng **click sidebar**, KHÔNG `navigate_page` (mất phiên).
Phiên rớt → đăng nhập lại theo đúng mục này.

## 3. Ghi verdict vào sheet (BẮT BUỘC dùng script, cấm ghi tay)

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk"
UAT_TAB="<tên tab>" python3 output/UAT_doi-tac/tools/sheet_write.py \
  --mode <reverify|reverify2> --row <N> --ma-tc <Mã TC> --status <Pass|Reopen> \
  --evidence <file bằng chứng> --condition-table output/UAT_doi-tac/reverify-round-2026-08-05/cond/<Mã TC>.md \
  --vong2-do-dev-build "Vòng 2 do DEV khởi xướng: dev build V1.0.6 lên env nip.io rồi flip 'Trạng thái dev fix 2' về 'dev done' nhờ QA verify lại; đối tác chưa phản ánh vòng 2 nên S/U trống là đúng bản chất." \
  [--note-file <file note>]   # chỉ khi Reopen \
  --dry-run
```
- Tab: `UAT_TGPL Doanh Nghiệp-tuần 2` hoặc `UAT_TGPL Doanh Nghiệp-tuần 3`.
- **Vòng 1** (cột `Verify`) → `--mode reverify`, **BỎ** cờ `--vong2-do-dev-build`.
- **Vòng 2** (cột `Verify 2`) → `--mode reverify2`, **GIỮ** cờ `--vong2-do-dev-build`.
- `--status Pass` → script chỉ ghi 1 ô Verify/Verify 2. **KHÔNG đụng cột khác** (đúng yêu cầu user).
  **CẤM dùng** `--pass-ghi-de-note` và `--pass-khoi-phuc-dev-done`.
- `--status Reopen` → script ghi 3 ô (Trạng thái dev fix + Verify + đè note). Bắt buộc `--note-file`.
- Chạy `--dry-run` trước, đọc kỹ old→new, rồi chạy lại BỎ `--dry-run`.
- **Script báo lỗi/chặn → DỪNG, báo lại. Cấm ghi tay, cấm viết script lách.**

### Note cột note (CHỈ khi Reopen) — người đọc là ĐỐI TÁC
Tiếng Việt có dấu, gạch đầu dòng, tả **triệu chứng đang thấy lần này**.
**Cấm lộ nội bộ:** video/ảnh đối tác, so sánh 2 môi trường, mã màn `SCR-xx`/`MH-xx`, tên build nội bộ,
jargon (API 200, endpoint, snake_case), lịch sử BA chốt.

## 4. File bảng đối chiếu điều kiện `cond/<Mã TC>.md`

🔴 **Chỉ được có ĐÚNG MỘT bảng markdown trong file**, đúng 4 cột:

```
| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | ... | nip.io — build V1.0.6 | Không |
| Vai trò | ... | cbnv_tw · CB_NV_TW | Không |
...
```
- Mọi phần liệt kê khác (đối chiếu từng tiêu chí, kết quả đo) phải viết bằng **gạch đầu dòng**, KHÔNG
  dùng bảng — script parse mọi bảng, gặp bảng ≠ 4 cột là DỪNG.
- Cột `GAP?` phải là `Không` ở mọi dòng. Còn 1 GAP = chưa verify xong, CẤM ra verdict.
- Thiếu tiền đề (data/state/account) → **seed/tạo rồi test lại**, KHÔNG được Pass, KHÔNG để trống.

## 5. Nguyên tắc chấm

- **Cấm Pass bằng quan sát tĩnh** ("nhìn thấy field rồi"). Phải chạy hết luồng tới bước sinh ra lỗi cũ.
- Bug gốc gộp nhiều ý → mọi ý hết lỗi mới Pass; còn ≥1 ý lỗi → **Reopen**.
- Fix một phần = **Reopen**, không phải Pass kèm ghi chú.
- Chụp màn hình ở mọi thao tác đổi trạng thái, lưu vào `image/`, **mở ảnh ra đọc** trước khi kết luận.
- Thấy bất thường NGOÀI phạm vi bug → ghi vào mục "Ghi nhận thêm" của file cond, báo lại, KHÔNG tự log dòng mới.

## 6. Riêng nhóm 20 phiếu XUẤT PDF (Báo cáo thống kê)

Sidebar → **Báo cáo thống kê** (`/bao-cao`).

Chọn loại báo cáo (danh sách ảo, phải cuộn mới nạp đủ 23 mục):
```js
async () => {
  const holder = document.querySelector('.rc-virtual-list-holder');
  for (let y=0; y<=holder.scrollHeight; y+=120) {
    holder.scrollTop=y; holder.dispatchEvent(new WheelEvent('wheel',{deltaY:120,bubbles:true}));
    await new Promise(r=>setTimeout(r,60));
  }
  const o=[...document.querySelectorAll('.ant-select-item-option')]
      .find(e=>(e.getAttribute('title')||'').includes('<CHUỖI NHẬN DẠNG>'));
  o.click(); return o.getAttribute('title');
}
```
Rồi: Kỳ báo cáo = **Năm** (tự điền 01/01/2026 → 31/12/2026) · Đơn vị = **Toàn quốc** (mặc định) →
bấm **Xem báo cáo** → bấm **Xuất PDF** → hộp thoại *Tùy chọn in báo cáo PDF* (A4 · Dọc mặc định) →
bấm **Xuất file**.

> ⚠️ Nút **Xuất PDF** chỉ MỞ HỘP THOẠI, không xuất luôn. Xuất thật ở nút **Xuất file** trong hộp thoại.
> Đừng kết luận "bấm Xuất PDF không có phản hồi".

Lấy nội dung tệp (Chrome isolated không đổ file về ~/Downloads → phải bắt blob):
```js
async () => {
  window.__blobs=[]; const oc=URL.createObjectURL;
  URL.createObjectURL=function(b){window.__blobs.push(b); return oc.apply(this,arguments);};
  const names=[]; const oa=HTMLAnchorElement.prototype.click;
  HTMLAnchorElement.prototype.click=function(){ if(this.download) names.push(this.download); return oa.apply(this,arguments); };
  [...document.querySelectorAll('button')].find(e=>e.innerText.includes('Xuất PDF')).click();
  await new Promise(r=>setTimeout(r,1200));
  [...document.querySelectorAll('.ant-modal button')].find(e=>e.innerText.trim()==='Xuất file').click();
  await new Promise(r=>setTimeout(r,7000));
  const b=window.__blobs[window.__blobs.length-1];
  const buf=new Uint8Array(await b.arrayBuffer());
  let s=''; for(let i=0;i<buf.length;i++) s+=String.fromCharCode(buf[i]);
  return {size:buf.length, names, b64:btoa(s)};
}
```
Gọi `evaluate_script` kèm `filePath: .../evidence/<Mã TC>-pdf-capture.json` (KHÔNG trả base64 inline — tốn context).

Giải mã + đo:
```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-round-2026-08-05/evidence"
python3 -c "
import json,base64
d=json.load(open('<Mã TC>-pdf-capture.json'))
open('<Mã TC>.pdf','wb').write(base64.b64decode(d['b64'])); print(d['size'], d['names'])
"
python3 -c "
import fitz; doc=fitz.open('<Mã TC>.pdf')
p=doc[0]; print('pages',doc.page_count,'sigflags',doc.get_sigflags()); print('rect',p.rect)
print('fonts',[f[3] for f in p.get_fonts()]); print(p.get_text()[:1500]); print('---TAIL---'); print(doc[-1].get_text()[-600:])
"
```

Kiểm tra 2 lần xuất cùng ngày ra 2 tên khác nhau (chờ sang phút mới rồi xuất lại):
```js
async () => { const m0=new Date().getMinutes();
  while(new Date().getMinutes()===m0) await new Promise(r=>setTimeout(r,3000)); /* rồi xuất lại */ }
```

### Chuẩn PASS của nhóm này (đã xác nhận trên case mẫu)
1. Tên tệp dạng `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` — có đủ ngày **và** giờ-phút.
2. Hai lần xuất cùng ngày (khác phút) ra hai tên khác nhau.
3. Đầu trang: `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` + `Độc lập - Tự do - Hạnh phúc`.
4. Đầu trang: tên cơ quan ban hành (vd `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP`).
5. Cuối trang: `Ngày ... tháng ... năm ...` + `NGƯỜI XUẤT BÁO CÁO` + `(Ký, ghi rõ họ tên và đóng dấu)` + họ tên tài khoản.
6. Khổ A4: rect ≈ `595,28 × 841,89 pt`.
7. Phông `Tinos-*` (tương thích số đo Times New Roman) — **đạt**, không chấm FAIL.
8. Đủ 4 mục: tên báo cáo · `Kỳ báo cáo:` · `Đơn vị:` · `Ngày tạo:`.
9. `sigflags = -1` (không ký số) → **ĐÚNG theo BA**, KHÔNG chấm FAIL.
10. Không có dòng chức danh người ký → **ĐÚNG theo BA**, KHÔNG chấm FAIL.

Thiếu bất kỳ mục 1–6, 8 → **Reopen** (nêu đúng mục thiếu).

### Bảng ánh xạ dòng → loại báo cáo (tab tuần 3)

| Row | Mã TC | Loại báo cáo chọn trên màn |
|---:|---|---|
| 192 | SLHDVM_07 | BC Số lượng hỏi đáp/vướng mắc pháp luật *(đã Pass — mẫu)* |
| 197 | VVDTN_07 | BC Vụ việc đã tiếp nhận |
| 204 | VVDHT_07 | BC Vụ việc đang hỗ trợ |
| 210 | VVDHTHT_07 | BC Vụ việc đã hoàn thành |
| 217 | VVTTG_06 | BC Vụ việc theo thời gian |
| 223 | CLDTBDDDR_07 | BC Lớp đào tạo đang diễn ra |
| 228 | LDTBDDDR_07 | BC Lớp đào tạo đã diễn ra |
| 231 | CGTVPL_07 | BC Số lượng CG/TVV |
| 234 | DGHQHTPL_07 | BC Đánh giá hiệu quả HTPL |
| 240 | VVTDVQL_07 | BC Vụ việc theo đơn vị quản lý |
| 247 | VVTLHDN_06 | BC Vụ việc theo loại hình DN |
| 249 | VVTTGCT_06 | BC Vụ việc theo thời gian chi tiết |
| 251 | CPHTCT_07 | BC Chi phí chi trả hỗ trợ |
| 254 | CPCTHTTDVQL_07 | BC Chi phí theo đơn vị |
| 258 | CPCTHTTLHDN_07 | BC Chi phí theo loại hình DN |
| 261 | CPCTHTTTG_06 | BC Chi phí theo thời gian |
| 265 | SLCTHT_07 | BC Số lượng chương trình hỗ trợ |
| 269 | CTTDVQL_05 | BC Chương trình theo đơn vị |
| 274 | CTTLV_06 | BC Chương trình theo lĩnh vực |
| 276 | CTTTG_05 | BC Chương trình theo thời gian |

23 loại có trên màn: 20 loại trên + `BC Chất lượng đào tạo` · `BC Chi phí theo lĩnh vực` · `BC Vụ việc theo lĩnh vực`.
Không thấy đúng loại của phiếu → DỪNG, báo lại, KHÔNG chọn loại gần giống.
