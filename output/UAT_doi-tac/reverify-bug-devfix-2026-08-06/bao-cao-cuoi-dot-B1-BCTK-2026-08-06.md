# Báo cáo cuối đợt — B1: BC thống kê vụ việc (6 case / 3 màn) — 06/08/2026

**Môi trường verify:** `https://18.143.165.120.nip.io` · bản dựng **V1.0.8** (đối tác đo trên V1.0 / V1.0.2 / V1.0.3)
**Bảng ghi:** spreadsheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `bug`
**Quy trình:** `flows/04-verify-bug-dev-fix-khong-ho-so.md` — hồ sơ tiêu chí viết TRƯỚC khi mở màn, verdict ghi ngay sau mỗi case.

---

## 1. Verdict 6 case trong phạm vi

| Dòng | Mã TC | Màn | Verdict | Đã ghi vào bảng |
|---|---|---|---|---|
| 178 | VVDTN_04 | BC Vụ việc đã tiếp nhận — số liệu | **cần BA** | `Dopai = BA` |
| 179 | VVDTN_06 | BC Vụ việc đã tiếp nhận — xuất tệp | **cần BA** | `Dopai = BA` |
| 183 | VVDHT_01 | BC Vụ việc đang hỗ trợ — số liệu | **Pass** | `Trạng thái dev fix = Test done` |
| 185 | VVDHT_06 | BC Vụ việc đang hỗ trợ — xuất tệp | **cần BA** | `Dopai = BA` |
| 193 | VVTTG_01 | BC Vụ việc theo thời gian — số liệu | **Pass** | `Trạng thái dev fix = Test done` |
| 195 | VVTTG_05 | BC Vụ việc theo thời gian — xuất tệp | **cần BA** | `Dopai = BA` |

**Hai nhóm "cần BA" thực chất chỉ là HAI câu hỏi:**

1. **Phạm vi vai trò QTHT với chức năng Báo cáo thống kê** — gộp `VVDTN_06` + `VVDHT_06` + `VVTTG_05`.
   Đã đo **độc lập trên cả ba màn**, kết quả **giống hệt nhau**: vai trò đúng tác nhân thì xuất tệp được
   (200, tệp mở đọc được, số khớp màn, bám đúng bộ lọc); vai trò QTHT thì xem được (200) nhưng xuất bị chặn
   (403 `ERR-PERM-SYS-00-01` "Forbidden"), phiên vẫn còn sống trước và sau cú chặn. Mâu thuẫn SRS: mục Tác nhân
   không liệt kê QTHT (`:192` / `:236` / `:325`) nhưng `BR-AUTH-08` (`:1268`) ghi ngoại lệ "QTHT bypass" áp
   **Toàn bộ FR-IX**, và luồng chỉ có **một** bước kiểm quyền chung cho cả xem lẫn xuất (`:79`).
   ⇒ **Một** quyết định của BA đóng cả 3 case; nếu chọn mở quyền thì sửa một chỗ ở tầng phân quyền là xong.
2. **Biểu đồ tròn theo lĩnh vực** — `VVDTN_04`: kỳ vọng đối tác **ngược** với đặc tả (`:1065` chốt Bar + Trend
   cho loại BC này, Donut chỉ gán cho UC124/UC127).

Chi tiết + đề xuất câu trả lời cho đối tác: [`ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md`](ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md).

**Hai case Pass đều là "Pass tạm"** — đo trên env nội bộ V1.0.8, chưa phải env đối tác; dữ liệu vụ việc hai
môi trường hoàn toàn khác nhau nên chỉ khẳng định "hiện trạng đúng đặc tả", chưa xác nhận bản vá đã lên env
đối tác.

---

## 2. Lỗi ngoài phạm vi phát hiện trong lúc verify

Đã log thành dòng mới trên tab `bug`, kèm bằng chứng link Drive xem được:

| Dòng | Mã TC | Nội dung | Mức |
|---|---|---|---|
| 365 | `BCTK_QA02` | Bấm [Xem báo cáo] lần thứ hai mà không đổi bộ lọc → **cả hai nút Xuất bị làm mờ vĩnh viễn** dù màn vẫn hiện đủ số liệu; chỉ hồi phục khi đổi bộ lọc hoặc tải lại trang. Tái hiện trên **3 loại báo cáo × 2 vai trò** ⇒ nhiều khả năng chung cho cả màn. Trái `:123` (nghiệm thu "nhấn → tải file") + `:1052`/`:1053` | Vừa |
| 366 | `BCTK_QA03` | Bảng "Thống kê theo người hỗ trợ" có dòng **"(Không xác định)"** gánh 2 vụ việc (máy chủ trả tên rỗng), và người đó **không có trong danh sách chọn** bộ lọc "NHT phụ trách" nên không tra tiếp được — trong khi người này **có đủ mã + họ tên** trong danh sách Người hỗ trợ (`NHT-STP-AG-0001` — "QA NHT An Giang UAT2"). Trái `:261` + `:244` | Vừa |
| 367 | `BCTK_QA04` | Lọc **đúng một đơn vị** → mục "Theo đơn vị" chỉ còn tiêu đề, không có dòng dữ liệu; để "Toàn quốc" thì hiện đủ. Xảy ra ở **3/5** loại báo cáo vụ việc; 2 loại còn lại xử lý đúng. Trái `:216` + `:262` + `:305` (đều ghi "Luôn") | Nhẹ |

**Không log trùng:** thông báo chặn quyền trả "Forbidden" (tiếng Anh, mã ngoài bộ mã báo cáo) trái `:117` —
**đã có** ở dòng 363 `BCTK_QA01` do phiên QA khác log sáng nay. Đã đối chiếu nội dung trước khi bỏ qua.

**Đã kiểm lại cả 3 bằng phương pháp thứ hai** (bù nốt bước còn thiếu của quy trình log bug) — cả 3 đều là
lỗi thật; giả thuyết ngược của từng lỗi đã bị bác bằng phép đo, không bằng lập luận. Riêng **dòng 366 và
367 đang mô tả hẹp hơn sự thật** nên cần sửa lại nội dung. Chi tiết + nội dung sửa đã soạn sẵn:
[`verify-lai-3-bug-moi-vs-srs-2026-08-06.md`](verify-lai-3-bug-moi-vs-srs-2026-08-06.md) ·
`note/BCTK_QA0{2,3,4}-fields-sua.json`.

---

## 3. Dữ liệu đã seed / đã đổi trên môi trường

**Không seed, không sửa, không xoá bản ghi nghiệp vụ nào.** Toàn bộ đợt này chỉ đọc: xem báo cáo, xuất tệp,
đọc danh sách vụ việc / tư vấn viên.

**Có thay đổi trạng thái phiên đăng nhập** của 7 tài khoản (đăng nhập → thu hồi phiên đang mở của tài khoản đó):
`cbnv_tw`, `cbnv_tw_01`, `cbnv_tw_02`, `cbnv_tw_03`, `cbnv_tw_05`, `cbpd_tw_01`, `admin`.
Không đổi mật khẩu, không khoá/mở khoá tài khoản nào.

---

## 4. Việc còn treo — cần người khác quyết

| # | Việc | Ai làm | Vì sao chưa đóng được |
|---|---|---|---|
| 1 | Chốt phạm vi vai trò QTHT với Báo cáo thống kê | **BA** | Đặc tả tự mâu thuẫn; QA không tự chọn được hướng |
| 2 | Chốt có bổ sung biểu đồ tròn theo lĩnh vực hay không | **BA** | Kỳ vọng đối tác ngược đặc tả |
| 3 | Làm mới ô "Kết quả verify" của dòng 178 / 179 nếu cần | **Người chủ bảng** | Công cụ ghi **chặn** ghi đè khi `Dopai` đã là `BA` (chỉ nhận `dev done`); không lách bằng tay |
| 4 | ~~Sửa lại nội dung dòng 365 / 366 / 367~~ — **đã xong 06/08** | — | Người chủ bảng đã đồng ý; ghi 12 ô, đọc lại khớp |
| 5 | Có gắn thêm bằng chứng ma trận 5 loại báo cáo cho dòng 367 hay không | **Người chủ bảng** | Ô bằng chứng hiện chỉ có tệp của 1 loại, trong khi dòng nay nói về 3 loại |
| 6 | Tránh đụng tài khoản giữa các phiên QA | **Điều phối QA / Infra** | Xem mục 5 |

---

## 5. Vấn đề môi trường cần nêu — **tranh chấp tài khoản giữa hai phiên QA**

Trong ~15 phút giữa đợt, phiên làm việc bị đá về `/login` **6 lần**. Đây **không phải lỗi phần mềm**: hệ thống
chỉ cho **1 phiên/tài khoản**, và một phiên QA khác đang chạy trên **cùng môi trường, cùng bộ tài khoản**.
Đối chiếu hộp thư MailHog (mã OTP không phải do mình yêu cầu) — giờ UTC:

`cbnv_tw` 07:17:51 + 07:18:22 · `cbnv_tw_03` 07:21:41 · `cbnv_tw_01` 07:28:35 · `cbnv_tw_04` 07:28:39 ·
`cbnv_tw_02` 07:30:41 · `admin` 07:29:00 + 07:30:45.

Hệ quả **hai chiều**: mình mất phiên giữa phép đo, và mỗi lần mình đăng nhập cũng đá phiên của họ —
đặc biệt `admin` là tài khoản QTHT **duy nhất**, nên mọi phép đo cần vai trò QTHT đều va nhau.

Ngoài ra dữ liệu env **đang được phiên kia thay đổi liên tục trong lúc đo** (tổng vụ việc toàn quốc 44 → 49 → 50
trong vòng ~35 phút). Đã xử lý bằng cách đo báo cáo và đếm đối chứng **trong cùng một lệnh**, và bust cache máy chủ
khi nghi ngờ — chi tiết ở [`tieuchi/VVTTG_01.md`](tieuchi/VVTTG_01.md).

**Đề xuất:** cấp thêm ít nhất **một tài khoản vai trò QTHT** cho môi trường dev, hoặc chia khung giờ giữa các
phiên QA. Nếu không, mọi đợt verify cần QTHT sẽ tiếp tục phá lẫn nhau.

---

## 6. Hồ sơ đính kèm

- Tiêu chí chấm từng case (viết trước khi mở màn): [`tieuchi/`](tieuchi/) — `VVDTN_04` · `VVDTN_06` · `VVDHT_01` · `VVDHT_06` · `VVTTG_01` · `VVTTG_05` · `_chung-xuat-excel.md`
- Diễn giải đã ghi lên bảng: [`note/`](note/)
- Kiểm lại 3 lỗi QA tự phát hiện (đối chiếu đặc tả + đo lại bằng cách khác): [`verify-lai-3-bug-moi-vs-srs-2026-08-06.md`](verify-lai-3-bug-moi-vs-srs-2026-08-06.md)
- Câu hỏi gửi BA: [`ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md`](ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md)
- Bằng chứng (ảnh · JSON phản hồi máy chủ · tệp Excel đã mở đọc): [`bug-reports/image/`](bug-reports/image/)
- Nhật ký ghi bảng: `output/UAT_doi-tac/tools/sheet_bug_verify_write.log` + `sheet_add_bug_row.log`
