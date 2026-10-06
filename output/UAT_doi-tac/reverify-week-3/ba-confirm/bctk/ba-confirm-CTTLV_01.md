# BA confirmation — CTTLV_01 (dòng 270) · Báo cáo Chương trình theo lĩnh vực

## Tóm tắt

- Test case: `CTTLV_01` — Báo cáo Chương trình theo lĩnh vực.
- Tham chiếu: `UC145` (báo cáo theo lĩnh vực) và `UC160` (quản lý Chương trình HTPLDN).
- Phản ánh của đối tác: báo cáo hiển thị nhóm **“Không xác định”**.
- Kết quả kiểm tra: hiện tượng có tái hiện. Các chương trình có `linhVucId = null` được gom vào nhóm “Không xác định”; chương trình có lĩnh vực được hiển thị đúng tên lĩnh vực.
- Verdict đề xuất: **BA confirm** — chưa kết luận Reject hoặc Open cho đến khi BA chốt quy tắc nghiệp vụ.

## Đối chiếu SRS

1. `UC145` yêu cầu báo cáo Chương trình theo lĩnh vực, gồm mã/tên lĩnh vực, số chương trình và số doanh nghiệp tham gia.
2. `UC160` và entity `CHUONG_TRINH_HTPL` hiện không quy định trường lĩnh vực trong dữ liệu đầu vào/form tạo chương trình.
3. SRS chưa quy định cách xử lý chương trình không có lĩnh vực: hiển thị “Không xác định”, loại khỏi báo cáo hay bắt buộc bổ sung lĩnh vực.

Nguồn đối chiếu:

- `input/srs-update-2026-5-5/srs-fr-11-bao-cao.md:952-987`
- `input/srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:125-137`
- `input/srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:1316-1334`

## Bằng chứng kiểm tra

- Báo cáo hiển thị 3 chương trình không có lĩnh vực trong nhóm “Không xác định” và 1 chương trình có lĩnh vực “Thương mại” trong đúng nhóm tương ứng.
- UI khớp dữ liệu trả về từ API: chương trình có `linhVucId = null` được gắn nhãn “Không xác định”; chương trình có `linhVucId` hợp lệ được map đúng tên.
- Evidence: `../../reverify-audit/CTTLV_01/cttlv-report-khongxacdinh.png` và `../../reverify-audit/CTTLV_01/reconciliation.md`.

## Nội dung cần BA xác nhận

**Chương trình HTPLDN có bắt buộc phải có lĩnh vực không, và báo cáo theo lĩnh vực phải xử lý chương trình chưa có lĩnh vực như thế nào?**

Đề nghị BA chọn một phương án:

1. Bổ sung trường lĩnh vực cho chương trình và quy định là bắt buộc; báo cáo không còn nhóm “Không xác định”.
2. Cho phép chương trình không có lĩnh vực và giữ nhóm “Không xác định”; cập nhật SRS UC145 để quy định rõ.
3. Cho phép chương trình không có lĩnh vực nhưng loại các chương trình này khỏi báo cáo; cần quy định rõ ảnh hưởng đến tổng số liệu.

## Nội dung đề xuất phản hồi đối tác

> Dữ liệu “Không xác định” phát sinh do chương trình chưa có thông tin lĩnh vực. Tuy nhiên, UC145 yêu cầu báo cáo theo lĩnh vực, trong khi UC160 chưa quy định trường lĩnh vực cho chương trình và chưa nêu cách xử lý dữ liệu trống. Đề nghị BA xác nhận quy tắc hiển thị.

## Hành động sau khi BA chốt

- Phương án 1: cập nhật SRS, form/entity chương trình và chuyển Dev xử lý.
- Phương án 2: cập nhật expected của test case và giữ cách hiển thị hiện tại.
- Phương án 3: cập nhật SRS/công thức báo cáo, sau đó chuyển Dev điều chỉnh và QA re-test tổng số liệu.
