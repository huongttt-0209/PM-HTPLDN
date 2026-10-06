# BA confirmation needed — Nhóm B2 (BC thống kê vụ việc — xuất tệp) — 2026-08-06

> **File này để làm gì:** 5 phiếu B2 đo lại trên bản dựng V1.0.8 đều dừng ở cùng một câu hỏi mà đặc tả không trả lời được: **vai trò Quản trị hệ thống (QTHT) có được xuất tệp báo cáo hay không**. Câu trả lời của BA quyết định 5 phiếu này là *Pass* hay *Reopen*, nên QA không tự chốt.
>
> Lỗi có SRS reference rõ ràng phát sinh trong lúc đo (câu chữ thông báo từ chối) đã log riêng ở [`bug-reports/bug-report-BCTK.md`](../bug-reports/bug-report-BCTK.md), không nằm trong file này.

> **Quy tắc citation:** mọi khẳng định đặc tả đều trỏ `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/<file>.md:<dòng>` — đã mở file đọc từng dòng, không lấy số dòng từ trí nhớ.

---

## VVDHTHT_06 · VVTDVQL_06 · VVTLV_05 · VVTLHDN_05 · VVTTGCT_05 — Vai trò QTHT có được xuất tệp báo cáo không?

**Bối cảnh testcase**

- Dòng bảng theo dõi: 189 (`VVDHTHT_06`) · 222 (`VVTDVQL_06`) · 226 (`VVTLV_05`) · 230 (`VVTLHDN_05`) · 234 (`VVTTGCT_05`).
- Nội dung kiểm tra: trên màn **Báo cáo thống kê**, bấm **[Xuất Excel]** sau khi đã [Xem báo cáo] thành công.
- *Kết quả mong đợi* của đối tác: hệ thống xuất và **tự động tải tệp về máy người dùng** (4/5 phiếu nêu thêm tên tệp theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`; riêng VVDHTHT_06 không nêu tên tệp).
- *Kết quả thực tế* đối tác ghi: vòng 1 (15–16/07, bản dựng V1.0) hiện `Không thể tạo file xuất. Vui lòng thử lại.`; vòng 2 (31/07, bản dựng V1.0.3) hiện `Forbidden`.
- **Dữ kiện then chốt mà các vòng trước bỏ sót:** cả **10/10 ảnh** đối tác gửi (2 vòng × 5 phiếu) đều hiển thị góc phải trên là **"Quản trị viên · QTHT"** — đối tác thao tác bằng vai trò **QTHT**, không phải cán bộ nghiệp vụ.

**Kết quả verify UI hiện tại**

- Verify ngày 06/08/2026 qua Chrome DevTools MCP trên `https://18.143.165.120.nip.io`, bản dựng **HTPLDN · V1.0.8**.
- Mỗi phiếu đo 3 dạng: D1 vai trò QTHT (`admin`) — D2 vai trò CB_NV_TW (`cbnv_tw_02`) cùng bộ lọc — D3 CB_NV_TW đổi bộ lọc.

| Loại báo cáo | Vai trò **QTHT** | Vai trò **CB_NV_TW** |
|---|---|---|
| BC Vụ việc đã hoàn thành | ❌ 403 `Forbidden`, không có tệp | ✅ `BaoCaoVuViecHoanThanh_20260806_1301.xlsx` (6 990 B) |
| BC Vụ việc theo đơn vị quản lý | ❌ 403 `Forbidden`, không có tệp | ✅ `BaoCaoVuViecTheoDonVi_20260806_1305.xlsx` (6 834 B) |
| BC Vụ việc theo lĩnh vực | ❌ 403 `Forbidden`, không có tệp | ✅ `BaoCaoVuViecTheoLinhVuc_20260806_1306.xlsx` (6 826 B) |
| BC Vụ việc theo loại hình DN | ❌ 403 `Forbidden`, không có tệp | ✅ `BaoCaoVuViecTheoLoaiDn_20260806_1306.xlsx` (6 801 B) |
| BC Vụ việc theo thời gian chi tiết | ❌ 403 `Forbidden`, không có tệp | ✅ `BaoCaoVuViecTheoTgChiTiet_20260806_1307.xlsx` (6 638 B) |

- Ở vai trò **CB_NV_TW**, đã mở đọc nội dung từng tệp `.xlsx` (không chỉ kiểm tệp có tạo được): 4 mục đầu tệp (tên báo cáo · kỳ + khoảng thời gian · đơn vị · ngày tạo) đủ ở cả 5 tệp; số liệu trong tệp khớp số liệu trên màn hình; đổi bộ lọc rồi xuất lại thì tệp đổi theo đúng bộ lọc mới. Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`.
- Ở vai trò **QTHT**: phần mềm **vẫn cho vào màn báo cáo, vẫn render báo cáo đầy đủ, nút [Xuất Excel] vẫn bật**; chỉ tới khi bấm mới bị máy chủ từ chối `HTTP 403` / `ERR-PERM-SYS-00-01` / `Forbidden`.
- Evidence: `../bug-reports/image/VVDHTHT_06-D1-qtht-toast.png` · `../bug-reports/image/VVTDVQL_06-D1-qtht-forbidden.png` · `../bug-reports/image/VVTLV_05-D1-qtht-forbidden.png` · `../bug-reports/image/VVTTGCT_05-D1-qtht-forbidden.png` · `../bug-reports/image/VVTLHDN_05-D1-qtht-man-hinh.png` · 5 ảnh `*-D2-cbnvtw*.png`.

**Điểm chưa rõ trong đặc tả v3.5**

1. Phần **tiền đề và tác nhân** của nhóm báo cáo chỉ kể tên cán bộ nghiệp vụ và cán bộ phê duyệt, **không nhắc QTHT**:
   - `srs-fr-11-bao-cao.md:62` — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"*
   - `srs-fr-11-bao-cao.md:281` (FR-IX-04) — Tác nhân: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*
   - `srs-fr-11-bao-cao.md:79` — bước xử lý 1: *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01"*

2. Nhưng **ma trận quyền lại cho QTHT quyền đọc** trên chính thực thể báo cáo, và không nói thao tác xuất tệp thuộc nhóm quyền nào:
   - `srs-v3.5.md:1335` — `| BAO_CAO | R | CRU* | CRU* | CRU* | RU* | RU* | RU* | — | — | — | — |` (thứ tự cột QTHT · CB_NV_TW · CB_NV_BN · CB_NV_DP · CB_PD_TW · CB_PD_BN · CB_PD_DP · DN · NHT · TVV · CG) ⇒ **QTHT = `R`**, CB_NV_TW = `CRU*`.
   - `srs-fr-11-bao-cao.md:1052` (SCR-IX-01, thành phần 8) — nút Xuất Excel chỉ đặt **một** điều kiện hiện: *"Sau khi đã \"Xem báo cáo\""*, không đặt điều kiện vai trò.
   - `srs-fr-11-bao-cao.md:1221` — thực thể `BAO_CAO` có trường `duong_dan_file`, tức mỗi lần xuất **có thể** được hiểu là tạo một bản ghi mới (thuộc quyền `C`) chứ không phải chỉ đọc (`R`).

⇒ Đặc tả không nói dứt khoát **thao tác "Xuất Excel" nằm trong quyền `R` (đọc) hay quyền `C` (tạo)**. Hai cách hiểu cho hai kết luận trái ngược cho cùng một hiện trạng.

**Câu hỏi cần BA xác nhận**

Vai trò **Quản trị hệ thống (QTHT)** — đang được phần mềm cho **xem** báo cáo thống kê — có được phép **xuất tệp** (.xlsx / .pdf) của báo cáo đó không?

1. **Hướng 1 — QTHT KHÔNG được xuất** (hiểu "Xuất" là quyền `C`, bám tiền đề `:62` chỉ liệt kê CB NV / CB PD): máy chủ chặn là **đúng**. Khi đó 5 phiếu B2 là *không phải lỗi ở phần chặn*, vì đối tác đã thao tác bằng vai trò không có quyền — nhưng vẫn phải sửa 2 điểm:
   - nút **[Xuất Excel]** không nên hiện ở trạng thái bấm được cho vai trò không có quyền (mời thao tác rồi mới từ chối);
   - câu từ chối phải theo `:117` (đã log [`bug-reports/bug-report-BCTK.md`](../bug-reports/bug-report-BCTK.md) BUG-BCTK-QA01).
2. **Hướng 2 — QTHT ĐƯỢC xuất** (hiểu "Xuất" là một dạng đọc, bám `srs-v3.5.md:1335` QTHT = `R` và `:1052` nút không đặt điều kiện vai trò): máy chủ chặn là **sai** → 5 phiếu B2 chuyển **Reopen**, owner **Dev BE** (nới quyền `bao-cao/export` cho QTHT).

**Đề xuất QA tạm thời**

- Chưa chuyển 5 phiếu này cho Dev cho tới khi BA chốt hướng, vì hai hướng cho hai owner khác nhau (Dev FE vs Dev BE).
- Verdict tạm cho cả 5 phiếu (189 · 222 · 226 · 230 · 234): **Cần BA xác nhận**.
- Nếu BA chọn **hướng 1**: 5 phiếu → *không phải lỗi* (đối tác dùng sai vai trò); riêng phần giao diện mời thao tác + câu chữ từ chối vẫn là lỗi, owner `Dev FE` (nút) và `Dev FE/BE` (câu chữ, theo BUG-BCTK-QA01).
- Nếu BA chọn **hướng 2**: 5 phiếu → *Reopen*, owner `Dev BE`. Phần chức năng còn lại đã đạt (tệp về máy, tên tệp đúng khuôn, 4 mục đầu tệp đủ, số liệu khớp màn, tệp bám bộ lọc) nên chỉ cần mở quyền, không phải làm lại luồng xuất.

**Ghi chú phạm vi hiệu lực:** đối tác đo trên `htpldn-uat.ospgroup.vn`; lượt này đo trên `18.143.165.120.nip.io` theo chỉ định. Hai môi trường khác bộ dữ liệu nên con số tuyệt đối khác nhau — kết luận ở trên chỉ dựa vào *tệp có khớp màn hình của chính lượt đo này hay không*, không đối chiếu với số của đối tác.
