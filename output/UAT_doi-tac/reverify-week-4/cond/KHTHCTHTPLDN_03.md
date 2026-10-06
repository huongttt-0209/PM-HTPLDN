# Bảng đối chiếu điều kiện — KHTHCTHTPLDN_03 (row 28) — Bảng danh sách chương trình

**Kết luận:** **BA confirm** — sửa từ `Reject` ngày 27/07/2026 sau audit ([AUDIT-reject-tuan-4.md](../reverify-audit/audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)). Đối tác quan sát ĐÚNG hiện trạng, tranh chấp nằm ở **kỳ vọng vs đặc tả** ⇒ protocol §Verdict cấm `Reject` cho dạng này. Ngoài ra khi đo đã lộ một thiếu sót khác, QA mở dòng riêng.

Phiếu ghi: *"SRS yêu cầu có cột 'Đợt báo cáo' - Liên kết nhanh mở màn hình 'Đợt báo cáo định kỳ' độc lập nhưng bảng danh sách không có cột thông tin trên mà hiển thị cột 'Số đợt BC'"*.

Về **tên cột**, bản SRS v3.5 đang dùng nói ngược với phiếu: `srs-fr-15-ct-htpldn.md:1113` quy định cột thứ 9 của bảng đúng là **"So dot BC"**, không phải "Đợt báo cáo", và không mô tả liên kết nhanh nào từ dòng chương trình.

Nhưng **không kết luận Reject** được, vì 2 lẽ:

1. **Quan sát của đối tác đúng** (re-verify live 27/07 17:35: đúng 9 cột, có "Số đợt BC", không có "Đợt báo cáo"). Chỗ khác nhau chỉ là **kỳ vọng** có cột + liên kết nhanh hay không → protocol: *"Expected/kỳ vọng đối tác KHÁC SRS (kể cả khi SRS đã ghi rõ) → bất đồng về ĐẶC TẢ → `BA confirm`"*.
2. **SRS tự mâu thuẫn về vị trí màn Đợt báo cáo**, nên lập luận "phiếu đối chiếu bản trước 3.5.2" chưa sạch:
   - `:618` — *"(v3.5.2: tab 'Đợt báo cáo' độc lập, không drill-down từ CT)"*.
   - `:1101` — *"**Trang chi tiet CT:** Tab 'Thong tin' ... + Tab 'Dot bao cao' (bang dot BC + drill-down dot -> form lap BC ...)"*, và bảng `:1143–1166` mô tả chi tiết tab đó **vẫn nằm trong SCR-XI-01**.
   - Thực tế web: trang chi tiết CT **chỉ có 1 tab "Thông tin"** (đúng `:618`, trái `:1101`).
   - ⇒ Bản đặc tả còn giữ song song 2 mô hình → protocol: *"mâu thuẫn giữa các nguồn → `BA confirm`"*. Đã mở **BA-23**.

**Phát hiện thêm khi đo (ngoài phiếu):** bảng thiếu cột **"Lĩnh vực pháp lý"** mà `:1113` có liệt kê, dù máy chủ đã trả sẵn dữ liệu và tệp Excel xuất ra lại có cột này. → mở dòng mới `KHTHCTHTPLDN_OOS_05`, lỗi `BUG-CT-BANG-THIEU-COT-LINHVUC`.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/KHTHCTHTPLDN_03.jpg`) | Mình test (env nip.io, 27/07/2026 14:45–15:05) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh cho thấy `CB_NV_TW` ("Cán bộ NV Trung ương"), đơn vị BTP · TW | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW. Đo thêm bằng `cbpd_tw` để chắc tập cột không đổi theo quyền | Không |
| Entity + trạng thái (state machine) | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả", dữ liệu trải nhiều trạng thái (Đang thực hiện, Tạm dừng, Chờ phê duyệt, Đã công bố, Dự thảo, Đã hủy, Hoàn thành) | Màn `/ct-htpldn/danh-sach`, thẻ "Tất cả", 8 chương trình trải 4 trạng thái (Đã duyệt, Đã công bố, Đang thực hiện, Hoàn thành) | Không |
| Dữ liệu tiền đề | Bảng có dữ liệu để đọc được tiêu đề cột | Có 8 chương trình, trong đó 3 chương trình **có gắn lĩnh vực** (Đất đai, Thuế, Lao động) và 1 chương trình **không gắn lĩnh vực** — chủ động dựng đủ hai chiều để nếu cột Lĩnh vực có tồn tại thì phải thấy cả giá trị lẫn ô trống | Không |
| Input / filter / giá trị nhập | Mở màn rồi đọc tiêu đề bảng | Đọc tiêu đề bảng bằng mã lệnh (cuộn hết chiều ngang), đối chiếu từng mục với `:1113`; sau đó xuất Excel để đối chứng tập cột lần hai | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thành phần giao diện / tập cột)

- `partner-evidence/KHTHCTHTPLDN_03.jpg` — đã mở đọc: bảng của đối tác có các cột `Mã CT`, (cột tên bị cuộn khuất), `Thời gian`, `Ngân sách`, `Đơn vị`, `Trạng thái`, **`Số đợt BC`**, `Hành động`. Trùng khít với môi trường QA — kể cả việc **không có cột Lĩnh vực pháp lý** ở cả hai nơi.
- `bug-reports/image/BUG-CT-danh-sach-thieu-loc-donvi-trangthai-va-cot-linhvuc.png` — đã mở đọc: tiêu đề bảng đọc rõ `Mã CT · Tên chương trình · Mục tiêu · Thời gian · Ngân sách · … · Hành động`, không có Lĩnh vực pháp lý.
- Tệp `ct-htpldn-2026-07-27.xlsx` do chính màn này xuất ra — đã mở đọc bằng công cụ đọc bảng tính: hàng tiêu đề **có** cột "Lĩnh vực" với giá trị "Đất đai", "Thuế", "Lao động".

## Phương pháp thứ hai (bắt buộc)

- **Đối chiếu từng mục thay vì đếm tổng.** Ghép 1-1 tập cột thực tế với 10 mục ở `:1113`: khớp 9, thiếu đúng mục số 4 "Linh vuc phap ly". Cách này tránh kết luận sai kiểu "9 cột ≈ 10 cột, coi như đủ".
- **Phép thử quyết định cho phần phiếu nêu — đọc đúng bản SRS đang có hiệu lực.** Trích nguyên văn `srs-fr-15-ct-htpldn.md:1113`: *"Ma CT (CT-{YYYYMMDD}-{SEQ}) / Ten CT / Muc tieu (cat 100 ky tu) / Linh vuc phap ly / Thoi gian ... / Don vi / Trang thai SM-KH-CTHTPL (C06) / **So dot BC** / Hanh dong (conditional)"*. Cột thứ 9 đúng là "So dot BC". Không có mục nào tên "Đợt báo cáo", cũng không có mô tả liên kết nhanh.
- **Truy nguyên vì sao phiếu lại mong khác:** `srs-fr-15-ct-htpldn.md:618` ghi *"**Màn hình:** SCR-XI-01 ... (**v3.5.2: tab "Đợt báo cáo" độc lập, không drill-down từ CT**)"*. Nghĩa là ý tưởng mở màn Đợt báo cáo từ dòng chương trình **đã bị bỏ** ở v3.5.2. Phiếu nhiều khả năng đối chiếu theo bản trước đó.
- **Kiểm hệ thống có làm đúng hướng mới không:** menu bên trái có mục **"Đợt báo cáo"** đứng độc lập ngang hàng với "CT HTPLDN" — đúng mô hình tab độc lập ở `:618`. Đồng thời cột "Số đợt BC" hiển thị số đếm (hiện là 0 cho mọi chương trình vì môi trường chưa tạo đợt). ⇒ Cả hai vế đều khớp đặc tả hiện hành.
- **Đối chứng cho phát hiện ngoài phiếu — loại trừ "chưa có dữ liệu lĩnh vực":** máy chủ trả kèm tên lĩnh vực cho từng chương trình (`CT-20260725-0002` → "Đất đai", `CT-20260725-0001` → "Thuế", `CT-20260724-0001` → "Lao động"), và tệp Excel xuất từ chính màn này in ra đúng 3 giá trị đó. ⇒ Dữ liệu sẵn sàng, chỉ thiếu phần dựng cột. `:1128` xác nhận lĩnh vực pháp lý là trường **bắt buộc** khi tạo chương trình và là chiều gom số liệu báo cáo, nên thiếu cột này là thiếu thật chứ không phải chi tiết trang trí.
