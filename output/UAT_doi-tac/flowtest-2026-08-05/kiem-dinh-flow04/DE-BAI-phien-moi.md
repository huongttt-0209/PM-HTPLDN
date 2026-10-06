# ĐỀ BÀI — chạy ở phiên mới

Mở Claude Code phiên mới ở repo này, dán nguyên khối dưới. Không đưa thêm gì khác, **không** đưa file bảng chấm.
Khối này chính là mục `## PROMPT MẪU` của flow 04, điền đủ slot.

Đã kiểm trước (2026-08-05): env dev trả 200 · 4 case đều tải được bằng chứng · thư mục đặc tả có đủ file.

---

```
Áp dụng @flows/04-verify-bug-dev-fix-khong-ho-so.md
- Bảng: https://docs.google.com/spreadsheets/d/1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s | Tab: bug
- Ô mã case: "Mã TC" | Ô trạng thái dev: "Trạng thái dev fix" + "Trạng thái dev fix 2" (chỉ ĐỌC)
  | Ô kết quả QA + Ô note: KHÔNG ghi sheet đợt này (chỉ chạy để đối chiếu)
- Từ vựng: đã fix="Fixed" hoặc "UAT done"  (các nhãn khác không dùng đợt này vì không ghi sheet)
- Đặc tả: Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/
  | Môi trường + tài khoản: output/UAT_doi-tac/input/input.md
- MÔI TRƯỜNG VERIFY: https://18.143.165.120.nip.io   (dev, đã có build fix mới)
- Bug report: output/UAT_doi-tac/flowtest-kiemdinh/bug-report.md
  | Ảnh: output/UAT_doi-tac/flowtest-kiemdinh/image/
- File gửi BA: output/UAT_doi-tac/flowtest-kiemdinh/cau-hoi-BA.md
- Thư mục tiêu chí: output/UAT_doi-tac/flowtest-kiemdinh/tieuchi/
- Công cụ: ghi kết quả=không ghi sheet
  · tải bằng chứng=cd output/UAT_doi-tac && UAT_TAB=bug python3 tools/fetch_evidence.py --row <N>
- Phạm vi: LKHDG_12 (row 126) · QLHSDNHTCP_03 (row 72)

Cuối đợt ghi thêm 1 file ngắn flowtest-kiemdinh/NHAT-KY-NGUON.md: mỗi việc bạn phải tự
quyết mà file flow không nói thẳng — 1 dòng, kèm bạn lấy căn cứ từ đâu.

flowtest-kiemdinh/ là thư mục NHÁP, sẽ xoá sau khi đánh giá. Vẫn làm đầy đủ hồ sơ như
thật (đó là thứ đang được kiểm), nhưng KHÔNG đụng vào output/qa-reports/ hay bất kỳ
file báo cáo nào có sẵn, và KHÔNG ghi lên Google Sheet.
```

---

## Ghi chú cho người chấm (không dán vào phiên mới)

- **Không cấm đọc file gì cả.** Nếu phiên mới đi mở `flows/01|02|03` hay `flowtest-2026-08-05/`, đó chính là
  kết quả cần biết: flow 04 không trả lời được chỗ nào nên nó phải đi tìm. Kiểm sau bằng transcript (BANG-CHAM §A0).
- Slot `Công cụ: bắt thông báo=` để trống có chủ ý — flow 04 nói "dự án có script dùng chung thì dùng,
  không có thì tự dựng". Xem nó xử lý ra sao khi slot rỗng.
- Nhãn dev cố ý **2 giá trị khác nhau** (`Fixed` / `UAT done`) → thử luôn slot `Từ vựng:`.
- 4 case đều nằm **trong tab `bug`** (295 case). Số dòng trong file
  `bug-con-fail-doi-tac-2026-07-31.csv` là dòng của **tab tuần**, KHÔNG dùng cho tab `bug` — đã sai một lần.
- Không case nào trùng 5 case chạy ngày 2026-08-05 → giảm rủi ro bắt được đáp án cũ.
- **Bộ lọc dùng để chọn:** `Dopai = dev done` AND `Trạng thái dev fix = Fixed` → 47 case.
  (`Reopen` không có trong cột đó — cột chỉ nhận `Fixed` / rỗng / `UAT done` / `reject`.)
- Trong 47 case, chọn 2 theo tỉ trọng nhóm: xuất tệp 26 · cột hiển thị 5 · thông báo 4 · số liệu 3.
  LKHDG_12 nằm ở **cả 2 nhóm đông nhất** và gộp 2 vế → thử luôn luật "case gộp nhiều vế".
  QLHSDNHTCP_03 là case tràn cột duy nhất chưa chạy (QLTVV_02 và VVDTN_04 cùng nhóm đã chạy 2026-08-05).
- Đợt sau (nếu cần thêm tín hiệu): CNKQHT_07 (row 62 — bẫy *đúng người nhận thông báo*) ·
  QLLSHTCTVV_03 (row 38 — 2 vế tràn cột + thiếu cột).

## Cho lúc chạy hàng loạt

Điền thêm 2 slot `Ô kết quả QA` + `Ô note` vào prompt (đợt kiểm định này bỏ trống vì không ghi sheet).
25 tên cột của tab `bug` không trùng nhau → định vị bằng tên header chạy được.
Cột hiện có: `Trạng thái` · `Trạng thái 2` · `TKM phản hồi lần 1/2` · `Trạng thái dev fix 1/2` ·
`DEV phản hồi lần 1/2`.
