# TLHSBS_01 — Re-verify sau Dev fix

- Ngày đo: 14/08/2026
- Môi trường: `https://18.143.165.120.nip.io`
- Account: `cbnv_tw_02` (OTP lấy từ MailHog)
- Build hiển thị: `HTPLDN · V1.0.14`
- Sheet nguồn: tab `bug`, dòng 386
- Verdict: **REOPEN — Dev fix chưa đạt**

## Căn cứ đặc tả

SRS `srs-fr-01-dashboard.md`, KPI-S-01:

- Dòng 569: tử số là vụ đã từng bị yêu cầu bổ sung ít nhất một lần, trên tổng vụ hoàn thành trong kỳ.
- Dòng 574: dùng cùng cấu trúc bộ lọc Dashboard.
- Dòng 580: mỗi vụ chỉ đếm một lần; giá trị = tử số / mẫu số × 100; mẫu số 0 thì hiển thị `—` và không tính xu hướng.
- Dòng 589–592: acceptance criteria tương ứng.

## Kết quả đo nhánh chính

1. Đăng nhập đúng `cbnv_tw_02`; header xác nhận actor `CB Nghiệp vụ - Trung ương #02`.
2. Mở `VV-BTP-TW-20260712-005`: trạng thái `Hoàn thành`; timeline có `Hoàn thành` ngày 25/07/2026 và `Bổ sung hồ sơ` ngày 15/07/2026.
3. Mở Dashboard, áp dụng `2026 / Cả năm / Toàn quốc / Tất cả`.
4. Thẻ Vụ việc hoàn thành = `23`; drill-down danh sách cũng trả `23`, URL lọc theo `ngay_hoan_thanh` từ 01/01/2026 đến 14/08/2026.
5. Thẻ Tỷ lệ hồ sơ bổ sung = `0%`; phản hồi `/api/v1/dashboard?nam=2026` cũng trả `TY_LE_HO_SO_BO_SUNG.giaTri = 0`.

Vì đã xác nhận trực tiếp ít nhất một vụ thuộc tử số, tỷ lệ đúng phải lớn hơn 0%. Cận dưới từ riêng vụ mẫu là `1/23 × 100 ≈ 4,35%`. Giá trị `0%` vì vậy sai chắc chắn; không cần giả định tổng tử số chính xác là 1.

## Kết quả đo nhánh mẫu số 0

Chọn `Tháng 9/2026 / Toàn quốc / Tất cả`: Vụ việc hoàn thành = `0`; thẻ Tỷ lệ hồ sơ bổ sung hiển thị `—`, có “Chưa có dữ liệu” và không có chỉ dấu xu hướng. Nhánh này PASS.

## Bằng chứng

- `image/01-precondition-record-completed.png`
- `image/02-precondition-history-supplement.png`
- `image/03-dashboard-after-apply.png`
- `image/04-completed-list-current.png`
- `image/05-zero-denominator.png`
- `image/06-restored-dashboard.png`
- `audit/precondition-record-a11y.txt`
- `audit/completed-list-api.json`
- `audit/dashboard-2026.response.network-response`
- `audit/formula-measure.json`
- `audit/condition-table.md`

Không ghi nhận lỗi console. Không phát hiện bất thường độc lập mới trong phạm vi thẻ TLHSBS_01.
