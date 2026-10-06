# Bug Report — Dashboard

| Thông tin | Giá trị |
|---|---|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp |
| **Môi trường** | `https://18.143.165.120.nip.io` |
| **Người test** | QA Automation |
| **Ngày** | 2026-08-14 |
| **Loại test** | Functional / Data |
| **Round** | Verify bug đối tác vòng đầu |
| **Tài liệu tham chiếu** | `srs-v3.5/srs-fr-01-dashboard.md` |

## Tổng hợp

Phát hiện **1** lỗi có SRS reference cụ thể trong Dashboard.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|---|---|---|---|---|---|---|---|
| BUG-TLHSBS_01 | Major | P1 | Data | TLHSBS_01 | `KPI-S-01 (UC1-9 bổ sung) §Processing dòng 567-591` | Tỷ lệ hồ sơ bổ sung bằng 0 dù có vụ hoàn thành từng qua bước bổ sung hồ sơ | Open |

## BUG-TLHSBS_01 — Tỷ lệ hồ sơ bổ sung bằng 0 dù có dữ liệu hợp lệ

### Mô tả

Cán bộ Nghiệp vụ Trung ương xem Dashboard năm 2026, phạm vi Toàn quốc. Thẻ “Tỷ lệ hồ sơ bổ sung” hiển thị `0%` và “Chưa có dữ liệu”, dù có vụ hoàn thành trong kỳ đã từng qua bước bổ sung hồ sơ.

### Các bước tái hiện

1. Đăng nhập role `CB_NV_TW` bằng `cbnv_tw_02`; role có quyền `DASHBOARD_VIEW` theo SCR-I-01 dòng 683-685.
2. Mở Dashboard với Năm `2026`, Tháng `Cả năm`, Cấp đơn vị `Toàn quốc`, Đơn vị `Tất cả`.
3. Ghi nhận Dashboard có `23` vụ hoàn thành nhưng “Tỷ lệ hồ sơ bổ sung” là `0%`.
4. Mở danh sách 23 vụ hoàn thành, vào vụ `VV-BTP-TW-20260712-005`.
5. Quan sát vụ ở trạng thái `Hoàn thành` ngày 25/07/2026 và dòng thời gian có `Bổ sung hồ sơ` ngày 15/07/2026.

### Kết quả mong đợi

- Theo KPI-S-01 dòng 567-580, vụ hoàn thành từng qua “Yêu cầu bổ sung” ít nhất một lần phải được tính vào tử số.
- Với mẫu số 23 và tử số ít nhất 1, tỷ lệ phải lớn hơn 0%; không được hiển thị “Chưa có dữ liệu”.

### Kết quả thực tế

- Dashboard hiển thị `0%` và “Chưa có dữ liệu”.
- Vụ đối chiếu `VV-BTP-TW-20260712-005` đáp ứng đủ điều kiện của tử số và mẫu số trên UI.

### Bằng chứng

![BUG-TLHSBS_01 — Dashboard có 23 vụ hoàn thành nhưng tỷ lệ hồ sơ bổ sung bằng 0](image/TLHSBS_01-dashboard-live.png)

![BUG-TLHSBS_01 — Vụ hoàn thành có dòng thời gian Bổ sung hồ sơ](image/TLHSBS_01-record-history.png)

### So sánh (Comparison)

| Điểm đối chiếu | SRS | UI live |
|---|---|---|
| Mẫu số | Vụ hoàn thành trong kỳ | 23 vụ |
| Tử số | Vụ trong mẫu số từng qua Yêu cầu bổ sung | Có ít nhất 1 vụ: `VV-BTP-TW-20260712-005` |
| Kết quả | Tử số / mẫu số × 100 | 0% |

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|---|---|
| URL ứng dụng | `https://18.143.165.120.nip.io` |
| OTP login | MailHog DEV |
| MailHog | `http://18.143.165.120:8025/#` |
| Xác thực | JWT + OTP |
| Tool test | Chrome DevTools MCP |

*Bug report generated: 2026-08-14 | QA Automation*
