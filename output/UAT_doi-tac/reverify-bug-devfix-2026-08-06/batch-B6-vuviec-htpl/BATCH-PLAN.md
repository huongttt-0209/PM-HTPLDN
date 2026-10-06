# Batch B6 — Vụ việc HTPL · verify bug dev đã fix · 2026-08-06

Flow áp dụng: [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)

## Nguồn

| Mục | Giá trị |
|---|---|
| Bảng | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **bug** (gid 1714340219) |
| Ô mã case | `Mã TC` |
| Đặc tả | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` |
| Tài khoản | `output/UAT_doi-tac/input/input.md` — bộ **_01**, mật khẩu `Test@1234` |
| **Môi trường verify** | `https://18.143.165.120.nip.io` — Pass chỉ có hiệu lực cho env + bản dựng này |
| MailHog (OTP) | `http://18.143.165.120:8025` |

## Phạm vi — 5 case, 1 menu (Vụ việc HTPL)

| Dòng | Mã TC | Triệu chứng đối tác | `Kết quả verify` trước đợt | Vòng 2 trên bảng |
|---:|---|---|---|---|
| 45 | KTHSYCHTPL_11 | Không có nút "Hoàn tất kiểm tra", chỉ có "Kiểm tra lại" | *(có nội dung — sẽ đè)* | Fail · dev fix 2 = **Bỏ qua** (dev reject) |
| 50 | TKHSYCHTPL_03 | Lọc Mức SLA = "Sắp hết hạn" → báo lỗi | *(trống)* | — |
| 51 | XNTGHTVV_03 | Từ chối → 403 "Vụ việc không được phân công cho bạn" | *(có nội dung — sẽ đè)* | Fail · dev fix 2 = dev done |
| 62 | CNKQHT_07 | CBNV không nhận được thông báo sau Cập nhật kết quả | *(trống)* | — |
| 64 | DGKQHTVV_01 | Không hiển thị nút chức năng Đánh giá (Nhóm 8) | *(có nội dung — sẽ đè)* | TKM retest 27/7 vẫn thiếu nút |

**Giới hạn:** đúng 5 case này, không thêm không bớt.

**Tách phiên:** Giai đoạn A — 5 agent con SONG SONG (mỗi agent 1 case, chỉ đọc, cấm mở trình duyệt).
Giai đoạn B — mỗi case 1 agent con, chạy **LẦN LƯỢT** (dùng chung trình duyệt · file hồ sơ · dữ liệu env; chạy song song giẫm nhau mà không phát ra dấu hiệu nào).

## BƯỚC 0 — kết quả chốt phạm vi

- **Bug entry có sẵn kèm khối CÁCH VERIFY:** 0/5. Đã grep toàn `output/UAT_doi-tac/**/*.md`, mọi lần khớp đều là báo cáo lô / file bối cảnh nhắc mã case, không phải bug entry của chính case (riêng khối trong `reverify-round-2026-08-05/note/145-TKHSYCHTPL_OOS_01.md` thuộc case **TKHSYCHTPL_OOS_01**, khác case). ⇒ **cả 5 case chạy flow 04.**
- **Bằng chứng đối tác:** tải được **5/5**, không dòng nào rỗng → không case nào đi nhánh không-gắn-bằng-chứng.
- **Dropdown thật của ô đích** (đọc `dataValidation` từng ô, cả 5 dòng giống nhau):
  - `Trạng thái dev fix` → `In Progress · Fixed · UAT done · Bug · Test done · reject · Reopen` ✔ có đủ `Test done` + `Reopen`
  - `Dopai` → `InProcess · Resoved · dev done · OSP · Bỏ qua · Open · bug · BA` ✔ có `BA`
  - Cả 5 dòng đang `Trạng thái dev fix = Fixed` và `Dopai = dev done` → qua được guard WRITABLE_FROM.
- **Pre-flight env:** trang đăng nhập HTTP 200 (chứng thư hợp lệ) · `/api/docs-json` 200 · `POST /api/v1/auth/login` với `cbnv_tw_01` trả 200 + `otpToken` · MailHog 200.

## Ghi lên bảng

| Verdict | Ô | Giá trị |
|---|---|---|
| Pass | `Trạng thái dev fix` | `Test done` |
| Reopen | `Trạng thái dev fix` | `Reopen` |
| cần BA | `Dopai` | `BA` |
| ô trống | *(không đụng ô trạng thái)* | — |
| mọi verdict | `Kết quả verify` | diễn giải |

**Ô CHỈ ĐỌC, cấm ghi đè:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.

**Quyết định của user 2026-08-06:** 3 dòng (45 · 51 · 64) đang có nội dung ở `Kết quả verify` từ vòng trước → **ĐÈ**, dùng `--cho-phep-de-ketqua`; tool in giá trị cũ và ghi vào `tools/sheet_bug_verify_write.log` nên khôi phục được. Cột trạng thái **luôn** ghi `Trạng thái dev fix` (vòng 1) cho cả 5 dòng, kể cả dòng đã có hoạt động ở cột vòng 2.

**Dòng bug mới ngoài phạm vi:** mã `<tiền tố module>_QA<số thứ tự>`; điền `Mã TC · Tên chức năng · Mô tả · Các bước thực hiện · Kết quả mong đợi · Kết quả thực tế · Trạng thái=Fail · Dopai=bug · Ảnh/vieo 1=<link xem được>`. Ô nào prompt không nhắc → để trống.

## Nơi lưu hồ sơ

```
reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/
├── BATCH-PLAN.md          ← file này
├── tieuchi/<mã>.md        ← giai đoạn A viết, giai đoạn B điền nốt mục 6
├── bug-report.md          ← mẫu output/template/bug-report-template.md
├── cau-hoi-BA.md          ← mẫu output/template/ba-confirmation-needed-template.md
├── image/                 ← ảnh do MÌNH chụp (bằng chứng quyết định verdict)
└── partner-evidence/      ← bằng chứng đối tác + frames-<mã>/ trích từ video
```

## Công cụ

| Việc | Công cụ |
|---|---|
| Bắt thông báo | Chrome DevTools MCP — `MutationObserver` cài **trước** khi bấm, `innerText`, không lọc trùng, đếm theo mốc giờ khác nhau |
| Ghi bảng | `output/UAT_doi-tac/tools/sheet_bug_verify_write.py` (chạy `--dry-run` trước, ghi thật, rồi đọc lại xác nhận) |
| Tải bằng chứng | `output/UAT_doi-tac/tools/fetch_evidence.py` (đã chạy xong, `UAT_TAB=bug`) |
| Trích frame video | `output/UAT_doi-tac/tools/extract_frames.py` (máy không có ffmpeg) |

## Nới guard đã khai

`fetch_evidence.py` và `sheet_read.py` chặn tab `bug` bằng allowlist vốn viết cho script **ghi**. Cả hai script này **chỉ đọc**, và allowlist đã có sẵn mục `"bug"` từ 2026-08-05/08-06 → chạy bằng `UAT_TAB=bug`, không sửa code. Đọc `dataValidation` của 5 ô đích: nạp hàm `cell_dropdown` có sẵn trong `sheet_bug_verify_write.py`, **không ghi gì** — không viết script dùng-một-lần.
