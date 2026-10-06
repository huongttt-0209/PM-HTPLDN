# BẢNG CHẤM FLOW 04 — chốt TRƯỚC khi chạy, không sửa sau

Phạm vi: 2 case — **LKHDG_12** (row 126) · **QLHSDNHTCP_03** (row 72).
Ngưỡng chốt 2026-08-05, **trước** khi phiên mới chạy. Chấm xong thấy ngưỡng khắt khe thì đó là kết quả,
không phải lý do nới ngưỡng — đúng bằng logic mục 4 của chính flow 04.

**Không chấm bằng "verdict có đúng không".** Verdict thật của 2 case này chưa ai biết; người chấm cũng chưa
mở bằng chứng ra xem (cố ý, để khỏi thiên vị). Chấm bằng 3 thước A/B/C.

---

## A0. Nó có phải đi tìm file khác không — đọc từ transcript

Phiên mới **không bị cấm** đọc gì. Nó tự đi mở flow khác = flow 04 hụt đúng chỗ đó.

```bash
T=$(ls -t ~/.claude/projects/-Users-huongttt-Downloads-antigravity-PM-HTPLDN-skilkk/*.jsonl | head -1)
grep -o '"file_path":"[^"]*"' "$T" | sort -u | grep -v flowtest-kiemdinh
```
Có `flows/01|02|03`, `quy-trinh-verify-1-bug.md`, `QA_*_PROTOCOL.md`, `flowtest-2026-08-05/`
→ đọc hội thoại quanh đó xem **nó tìm cái gì** → đó là mục phải bổ sung vào flow 04.
Chỉ có đặc tả + input + tools → tín hiệu tự chứa mạnh.

---

## A. Bẫy cấu trúc — nhìn bằng chứng là biết, không cần biết đáp án

### A1. LKHDG_12 — bẫy *xuất tệp* + *case gộp nhiều vế*
Đối tác báo 2 vế: (i) file xuất không theo tiêu chí lọc · (ii) thiếu cột "Số vụ việc", "Người tạo", "Ngày tạo".

- 🔴 **SẬP** nếu ra verdict mà bằng chứng **không có nội dung đọc ra từ chính tệp xuất** (tên cột thật /
  số dòng / giá trị ô). Ảnh toast "xuất thành công", mã 200, dung lượng tệp → không tính.
- 🔴 **SẬP** nếu chỉ đo 1 trong 2 vế mà vẫn chốt verdict cho cả case.
- 🔴 **SẬP** nếu Pass vế (i) mà không hề đặt bộ lọc rồi mới xuất.
- ✅ Đạt: liệt kê header thật của tệp, đối chiếu đủ 3 cột; lọc rồi xuất, so số dòng tệp với số dòng bảng.

### A2. QLHSDNHTCP_03 — bẫy *độ phủ M biến thể*
Cột "Mức cảnh báo thời hạn" tràn sang cột "Ngày nộp" — phụ thuộc **độ dài nội dung × độ rộng khung nhìn**.

- 🔴 **SẬP** nếu Pass mà M = 1 (chỉ nhìn 1 mức cảnh báo), hoặc không ghi M, hoặc không ghi khung nhìn đã đo.
- 🔴 **SẬP** nếu kết luận "không tràn" chỉ bằng ảnh chụp, không đo biên cột bằng số.
- ✅ Đạt: liệt kê các mức cảnh báo thực có, đo bằng **toạ độ/biên cột**, ghi khung nhìn; mức nào thiếu thì
  seed và khai rõ đã seed gì trên bản ghi nào.

### A3. Cả 2 case — bẫy *đo bằng phần tử thay vì toạ độ*
- 🔴 **SẬP** nếu đếm/so bằng số phần tử DOM mà kết luận về bố cục (đã có tiền lệ đếm gộp thẻ bọc + thẻ trong
  → báo "nút xuống 2 hàng" giả). Phải đo toạ độ thật.

**Nhánh KHÔNG đo được đợt này:** *cần BA* (kỳ vọng ≠ đặc tả) · *Reopen* · *ô trống* · toàn bộ §Ghi kết quả
(đợt này không ghi sheet). Nhánh *cần BA* **có thể** tự nổ nếu đặc tả im lặng về danh sách cột tệp xuất —
nếu nổ thì chấm thêm: ra verdict "không phải lỗi" mà không dẫn được quyết định BA + ngày ⇒ **SẬP**.

---

## B. Hiện vật — 7 mục × 2 case = 14 ô, đếm được

| # | Mục | Cách kiểm |
|---|---|---|
| 1 | File tiêu chí riêng mỗi case, đủ **6 mục** (mục 6 = bảng điều kiện) | mở file |
| 2 | **Mục 4 (PASS khi/FAIL nếu) viết TRƯỚC phép đo đầu tiên** | tra lần **Write đầu tiên** trong transcript (xem lệnh dưới) — **KHÔNG** dùng `mtime`, đó là lần ghi *cuối* |
| 3 | Mục 2 quote **nguyên văn + số dòng** đặc tả | mở file SRS kiểm số dòng có khớp không |
| 4 | Mục 6 đủ 5 dòng không ô trống; cột "Đối tác" điền từ giai đoạn A | mở file |
| 5 | Ghi môi trường + **bản dựng** | mở file |
| 6 | Pass thì ghi **N** bản ghi + **M** dạng đã phủ; có seed thì khai rõ | mở file |
| 7 | Có hồ sơ đầu ra: bug entry + khối CÁCH VERIFY | mở thư mục ra |

```bash
cd ~/.claude/projects/-Users-huongttt-Downloads-antigravity-PM-HTPLDN-skilkk
python3 - <<'EOF'
import json,glob
p=[f for f in glob.glob('*.jsonl') if any('flowtest-kiemdinh' in l for l in open(f,encoding='utf-8',errors='ignore'))][0]
for line in open(p,encoding='utf-8',errors='ignore'):
    try: d=json.loads(line)
    except: continue
    for b in (d.get('message') or {}).get('content') or []:
        if isinstance(b,dict) and b.get('type')=='tool_use' and b.get('name') in ('Write','Edit','Read'):
            fp=(b.get('input') or {}).get('file_path','')
            if 'flowtest-kiemdinh' in fp:
                print(d.get('timestamp','')[11:19], b['name'], fp.split('flowtest-kiemdinh/')[-1])
EOF
```
Lần **Write đầu tiên** của `tieuchi/<case>.md` phải **sớm hơn** ảnh/tệp đo đầu tiên của cùng case.
Trễ hơn = viết tiêu chí sau khi nhìn kết quả = đúng cái Pass oan flow 04 sinh ra để chặn.
⚠️ `mtime` trên đĩa là lần ghi **cuối** — flow cho phép sửa tiêu chí sau khi đo, nên `mtime` trễ là bình thường
và **không** chứng minh gì. Đã suýt chấm sai vì nhầm chỗ này ngày 2026-08-06.

**Ngưỡng B:** ≥ **13/14** ô. **Và** không mục nào thiếu ở **cả 2 case** — thiếu 1 lần là lỗi vận hành,
thiếu ở cả hai là lỗi văn bản flow.

---

## C. Nhật ký nguồn quyết định — thước đo tính tự chứa

Phiên mới chỉ ghi tự do 1 dòng/việc. **Người chấm tự phân rổ**, không để nó tự phân.
Đọc `NHAT-KY-NGUON.md` + đối chiếu A0:

| Rổ | Nghĩa | Xử lý |
|---|---|---|
| **(a)** file flow nói thẳng | flow làm đúng việc | — |
| **(b)** lấy từ CLAUDE.md / repo | **phụ thuộc ẩn** — sang project khác là gãy | mỗi dòng = 1 mục phải bổ sung |
| **(c)** tự chế vì không ai nói | **lỗ hổng flow** | mỗi dòng = 1 mục phải viết mới |

**Ngưỡng C:** rổ (c) ≤ **2** mục, **và** không mục nào trong (c) ảnh hưởng verdict
(vd tự quyết "bao nhiêu bản ghi là đủ", "có cần BA không" → ảnh hưởng verdict ⇒ trượt dù chỉ 1 mục).

Rổ (b) không tính đạt/trượt nhưng **phải vá hết** trước khi tuyên bố flow dùng được cho project khác.

---

## Chốt

| Kết luận | Điều kiện | Làm gì tiếp |
|---|---|---|
| ✅ **Dùng được** | A sập 0 · B ≥13/14 · C rổ (c) ≤2, không ảnh hưởng verdict | chạy hàng loạt theo lô |
| 🟡 **Sửa nhỏ rồi dùng** | A sập ≤1 · B ≥12/14 · C rổ (c) ≤4 | vá rồi chạy thêm 2 case (CNKQHT_07 · QLLSHTCTVV_03) |
| 🔴 **Chưa dùng được** | còn lại | vá rồi chạy lại đúng 2 case này |

---

## Ba thứ phép thử này KHÔNG đo được — nói trước để khỏi tưởng bở

1. **Cùng model, cùng thói quen.** Phiên mới xoá ngữ cảnh hội thoại, không xoá thói quen sẵn có. Nó có thể
   làm đúng một việc mà flow không hề dặn → tưởng flow dặn rồi. Rổ (c) chỉ bắt được phần nó **tự nhận ra** là
   đang tự chế. Muốn khử hẳn: người khác chạy, hoặc model khác.
2. **Chỉ 2 case, 2 loại bẫy.** Đạt hết cũng chỉ chứng minh flow đứng vững ở nhóm *xuất tệp* + *cột hiển thị*
   (77/295 case của tab `bug`). Nhóm còn lại chưa có bằng chứng gì.
3. **4 nhánh chưa chạy lần nào:** *cần BA* (luật mới thêm 2026-08-05) · *Reopen* · *ô trống* ·
   toàn bộ §Ghi kết quả. Chạy hàng loạt sẽ đụng cả 4 — đặc biệt §Ghi kết quả, vì tab `bug` **chưa xác định
   được ô nào là ô của QA**.
