# QA BA-Apply Protocol — Cập nhật quyết định của BA (BƯỚC 2)

> **Luật chung ở [QA_VERIFY_PROTOCOL.md](QA_VERIFY_PROTOCOL.md)** — cách viết note partner-facing,
> thứ bậc nguồn (SRS/BA duyệt > thiết kế nội bộ > expected đối tác). File này CHỈ ghi phần
> **khác biệt của bước 2**. Mâu thuẫn → **QA_VERIFY_PROTOCOL.md thắng**.
>
> **Bước này KHÔNG test lại web.** Đầu vào là **quyết định của BA** cho các case vòng 1 đã chốt
> `BA confirm`. Việc của QA: dịch quyết định đó thành verdict + viết **CÁCH VERIFY** đủ cụ thể để
> bước 3 re-verify không sai.

---

## THAM SỐ ĐỢT — prompt phải cấp đủ, thiếu → DỪNG hỏi user

| Tham số | Ví dụ |
|---|---|
| Link sheet + **tên tab** | link + `UAT_TGPL Doanh Nghiệp-tuần 3` |
| **File BA phản hồi** | `reverify-week-3/ba-confirm/<module>/phan-hoi-ba-....md` |
| File bug-report gộp của module | `reverify-week-3/bug-reports/<module>/bug-report-....md` |
| Module / luồng | `Chi trả` |

🔴 **Phân biệt 2 loại file, nhầm là cập nhật sai toàn bộ:**

| File | Là gì | Dùng ở bước 2? |
|---|---|---|
| `ba-confirmation-needed-*.md` | **QA đi HỎI** BA — chỉ có câu hỏi | ❌ **KHÔNG** |
| `phan-hoi-ba-*.md` / `ba-response-*.md` | **BA TRẢ LỜI** — có quyết định | ✅ đúng file cần |

**Guard tab:** prompt có cả link `gid=...` lẫn tên tab bằng chữ → resolve gid ra tên tab rồi so sánh;
lệch → DỪNG. Tab phải khớp **tuần của bug** (file trong `reverify-week-3` → tab tuần 3).
Truyền tab qua env `UAT_TAB="<tên tab>"`.

**Định vị cột bằng TÊN HEADER** — `Mã TC` · `Trạng thái dev fix 1` · `Verify` · `DEV phản hồi lần 1`.`Trạng thái dev fix 2` · `Verify 2` · `DEV phản hồi lần 2`.
CẤM dùng chữ cái cột. Map bug ↔ dòng qua **`Mã TC`** (Bug ID = `BUG-<Mã TC>`).

---

## Vòng lặp MỖI BUG — làm dứt điểm từng bug

**CẤM gom lô.** Xử lý xong 1 bug → ghi sheet ngay → rồi mới sang bug kế.

1. **Đọc bug gốc trên sheet** (`Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` ·
   `Kết quả thực tế`) **+ quyết định của BA** → phân loại:

   | Phân loại | `Verify` | `Trạng thái dev fix 1` |
   |---|---|---|
   | **BUG cần dev fix** | `Open` | `Open` — **chỉ khi ô đang là `BA confirm`** |
   | **KHÔNG phải bug** | `Reject` | `Reject` — **chỉ khi ô đang là `BA confirm`** |

   🔴 Ô `Trạng thái dev fix 1` đang là `dev done` hay **bất kỳ giá trị nào khác** → **GIỮ NGUYÊN,
   không đụng.** Đó là trạng thái xử lý của dev, không phải ô của QA.

2. **BA nói chưa đủ rõ để viết được CÁCH VERIFY → DỪNG, hỏi user. CẤM đoán.**

3. Soạn note cột `DEV phản hồi lần 1` theo layout dưới → **ghi ngay dòng đó** → đọc lại xác nhận
   3 ô → sang bug kế.

---

## Layout note — BUG (Verify = Open)

Người đọc là **dev/BA** → được giữ reference `FR-<module>-NN (UCxx) §mục (dòng N)`.

```
✅ Bug đúng (BA <ngày>). Dev FE/BE: <việc dev phải làm + căn cứ BA đưa>. <Minor/Cosmetic/Major>.

── CÁCH VERIFY sau Dev fix ──
Precondition: <account CỤ THỂ vd cbnv_tw> + <màn/URL vd /doanh-nghiep/them-moi>.
1) <bước cụ thể, giá trị cụ thể>
2) <bước cụ thể>
✅ PASS khi: <đa tiêu chí, ĐO ĐƯỢC, riêng cho bug này>
❌ FAIL nếu: <điều kiện fail rõ ràng>
⚠️ <caveat chặn đúng bẫy FAIL-oan của bug — CHỈ thêm khi bug có bẫy>
Ảnh lỗi cũ: image/<tên file>.png
```

**Chất lượng CÁCH VERIFY — đây là phần dễ hỏng nhất của cả quy trình:**

- Account **thật** (`cbnv_tw`), giá trị **thật**, tiêu chí **đo được**.
- **CẤM** chung chung: "account phù hợp", "kiểm tra kết quả đúng", "hiển thị hợp lý".
- **Describe, KHÔNG prescribe** — tả *yêu cầu nghiệp vụ*, đừng chốt cứng nhãn nút / endpoint / mã lỗi.
  Dev có nhiều cách implement; prescribe → cãi qua lại nhiều vòng.
  - ❌ "Phải hiện button **Đồng ý/Hủy**" · "Phải gọi `POST /api/v1/X` trả 200"
  - ✅ "Khi role X bấm duyệt không hợp lệ, hệ thống phải từ chối + giữ nguyên trạng thái cũ"
- Dòng `⚠️` chỉ thêm khi bug **có bẫy** khiến bước 3 dễ FAIL oan (vd: nhãn không cần y hệt).

## Layout note — KHÔNG PHẢI BUG (Verify = Reject)

Người đọc là **đối tác** → **CHỈ** dùng UC + mô tả bằng lời. **CẤM** mã FR/BR, số dòng SRS, mã màn,
jargon kỹ thuật. **Không cần** CÁCH VERIFY.

```
❌ Không phải lỗi (BA xác nhận <ngày>).
- BA chốt: <lý do + căn cứ BA đưa>.
- <cải tiến / đối tác chỉnh lại KQ mong đợi — chỉ nếu BA có nêu>.
```

---

## Ghi sheet

⚠️ **Bước 2 hiện chưa có mode ghi an toàn.** `sheet_write.py` có 5 mode (`verify1`, `qaverdict`,
`verify2`, `reverify`, `reverify2`) nhưng **không mode nào ghi được đúng bộ 3 ô của bước 2**:
`qaverdict` tuyệt đối không đụng `Trạng thái dev fix 1`, và dừng nếu `Verify` đã có giá trị cũ.

**Cho tới khi có `--mode baapply`:** DỪNG và báo user. **CẤM ghi tay**, **CẤM viết thêm một script
`sheet_baconfirm_apply_<module>.py` mới** — thư mục `tools/` đã có 19 bản như vậy, mỗi bản hardcode
danh sách bug, không tái dùng được và không có guard đồng nhất.

Lệnh **dự kiến** sau khi có mode:

```bash
UAT_TAB="<tên tab>" python3 output/UAT_doi-tac/tools/sheet_write.py --mode baapply \
    --row <N> --ma-tc <Mã TC> --status Open|Reject \
    --note-file <file note> --ba-source <file BA phản hồi> --dry-run
```

Guard mode này cần có:

1. Chỉ ghi `Trạng thái dev fix 1` khi **giá trị hiện tại == `BA confirm`**; khác → giữ nguyên, in cảnh báo.
2. `--status Open` mà note **thiếu khối `── CÁCH VERIFY sau Dev fix ──`**, hoặc thiếu dòng
   `Precondition:` / `✅ PASS khi:` / `❌ FAIL nếu:` → **CHẶN**.
3. `--status Reject` mà note **có** khối CÁCH VERIFY → chặn (sai layout).
4. Giữ nguyên guard sẵn có: khớp `Mã TC`, kiểm dropdown, in old→new, đọc lại sau ghi, ghi log kèm giá trị cũ.

**Script chặn → DỪNG, báo user.** Dropdown cột `Trạng thái dev fix 1` ở dòng dev đã đụng dùng từ vựng
của dev (`New / Reopent / InProcess / Resoved / Reject / dev done`) — có thể **không chứa `Open`**.
Gặp thì báo, đừng bịa option.

---

## Sau khi BA chốt là BUG — thêm entry vào bug-report

BA chốt `Open` → **thêm 1 entry vào file bug-report gộp của module** (template
`output/template/bug-report-template.md`, đúng 6 sections) + ≥1 screenshot trong `image/`.

**Vì sao bắt buộc:** BƯỚC 0 của [QA_REVERIFY_PROTOCOL.md](QA_REVERIFY_PROTOCOL.md) đối chiếu
*số dòng `dev done` trên sheet* với *số bug trong file md*. Bug chốt ở bước 2 mà không có entry
→ bước 3 sẽ báo lệch và dừng.

`Reject` không vào bug-report, nhưng lưu vết quyết định BA vào `reverify-audit/`.
