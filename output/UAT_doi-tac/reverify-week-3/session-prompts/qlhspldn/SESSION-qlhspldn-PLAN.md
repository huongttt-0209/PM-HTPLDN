# Kế hoạch verify "Hồ sơ pháp lý doanh nghiệp" (QLHSPLDN) — tuần 3

> **Vì sao tách folder riêng:** 2 case QLHSPLDN (rows **292–293**) truy cập qua menu **Doanh nghiệp → Xem chi tiết → thẻ "Hồ sơ pháp lý doanh nghiệp"** (MH-07.2) — **màn hình + luồng khác hẳn** cụm TVCS (menu Tư vấn). Dù SRS xếp chung Nhóm X.1, surface truy cập độc lập → tách folder để không trộn seed/tài khoản.
> 2 case = **1 batch duy nhất** (không cần chia nhỏ). Mở 1 cửa sổ Claude Code MỚI, dán `session-prompts/qlhspldn/SESSION-qlhspldn-batch1-prompt.md`.

## SRS gốc
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` — **FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150, dòng 529)**.
🔴 Màn cũ SCR-X1-03 **DEPRECATED v2.1** (dòng 535, 1161–1163) → chuyển thành **tab "Hồ sơ PL" trong MH-07.2 chi tiết Doanh nghiệp** (`srs-fr-07-doanh-nghiep.md`). Truy cập đúng qua menu Doanh nghiệp.

🔴 **Điểm neo SRS:**

| Chủ đề | Dòng SRS | Nội dung |
|---|---|---|
| **Inputs form Thêm/Sửa** | **548–562** | ma_ho_so (auto) / DN / ten_ho_so / loai_ho_so / **linh_vuc_id (Lĩnh vực, dòng 556)** / ngay_cap / ngay_het_han / co_quan_cap / **mo_ta (Mô tả, dòng 560)** / trang_thai / **file_dinh_kem (Tệp đính kèm, dòng 562)**. KHÔNG có field "Số/ký hiệu" |
| **Output cột danh sách** | **642–656** | ma_ho_so / ten_ho_so / ten_doanh_nghiep / loai_ho_so / ngay_cap / ngay_het_han / trang_thai / **co_file (Có tệp đính kèm, dòng 654)** / ngay_tao. KHÔNG có cột "Lĩnh vực pháp lý"/"Nguồn"/"Số/ký hiệu" trong Output list |

## 2 case (rows 292–293)

| Row | Mã TC | Đối tác phản ánh | Điểm neo SRS | Hướng nghi ngờ (chưa chốt) |
|---|---|---|---|---|
| 292 | QLHSPLDN_02 | Bảng danh sách **thiếu cột "Lĩnh vực pháp lý", "Nguồn", "Có tệp đính kèm"** + **thừa "Số/ký hiệu"** | Output dòng 642–656 (có **co_file** dòng 654; KHÔNG có Lĩnh vực/Nguồn/Số ký hiệu trong Output list) | Tách ý: thiếu "Có tệp đính kèm" (co_file có trong SRS) → **Open**; "Lĩnh vực PL"/"Nguồn" không có trong Output list → **BA confirm** (kỳ vọng UX vượt SRS); thừa "Số/ký hiệu" → **BA confirm/Open** |
| 293 | QLHSPLDN_03 | Biểu mẫu thêm mới **thiếu "Lĩnh vực pháp lý", "Mô tả", "Tệp đính kèm"** + **thừa "Số/ký hiệu"** | Inputs dòng **556 (linh_vuc), 560 (mo_ta), 562 (file_dinh_kem)** | 3 field thiếu **có trong SRS Inputs** → **Open**; "Số/ký hiệu" thừa → **BA confirm/Open** |

## Vai trò + tiền đề
- **Vai trò verdict = CB NV** (SRS dòng 540 tác nhân CB NV/NHT) → **login `cbnv_*` / `Test@1234`**, KHÔNG dùng admin.
- **Tiền đề (§Nguyên tắc 4):** cần **1 DN thuộc đơn vị của CB NV** có **≥1 hồ sơ pháp lý** (để bảng danh sách 02 có dữ liệu; form 03 chỉ cần mở Thêm mới). Đề xuất: `cbnv_hn` (Sở Tư pháp Hà Nội) + DN Hà Nội `0109998887`. Nếu DN chưa có hồ sơ PL → seed: menu Doanh nghiệp → chi tiết DN → thẻ Hồ sơ pháp lý → [+ Thêm mới hồ sơ pháp lý] → nhập → Lưu. Ghi account thực dùng.
- Cả 2 case là **bug hiển thị (cột/field cố định)** → chủ yếu **tĩnh** (`--static-bug`), miễn bảng đối chiếu điều kiện; nhưng vẫn cần **artifact real-data** (ảnh full-res header bảng / form) chạy trên DN đã seed (§GATE).

## Output — FOLDER BUG TỔNG của round
- **Verdict → Google Sheet NGAY** sau mỗi case: `python3 tools/sheet_write.py --mode verify1 --row N --ma-tc <MÃ> --status <...> --evidence <path> --static-bug "<lý do>" --note-file <note.txt>` (chạy từ `output/UAT_doi-tac/`).
- **Bug Open** → `reverify-week-3/bug-reports/Pass-bug-report-qlhspldn.md` (template `output/template/bug-report-template.md`, 6 sections; Bug ID `BUG-<mã TC>`) + ảnh `reverify-week-3/bug-reports/image/`.
- **BA confirm** → `reverify-week-3/ba-confirmation-needed-qlhspldn.md`.
- **Reject / BA confirm** → `reverify-week-3/reverify-audit/<mã TC>/`.

## Môi trường
- Web `https://18.143.165.120.nip.io/login` · MailHog `http://18.143.165.120:8025/` (xem `input/input.md`). Tool: **Chrome DevTools MCP**.
- Evidence: `python3 tools/fetch_evidence.py --row N` TRƯỚC mỗi case.
