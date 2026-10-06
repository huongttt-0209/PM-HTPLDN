# Bảng đối chiếu điều kiện — QLHSTVV_04 (nút "← Quay lại danh sách" có giữ bộ lọc không)

Evidence đối tác: partner-evidence/QLHSTVV_04.webm (frame 00:01 danh sách đang lọc tab "Mới đăng ký"; 00:05 mở chi tiết Tester TKM TVV-BTP-TW-0055; 00:08 sau khi bấm "Quay lại danh sách" → về tab mặc định "Đang hoạt động", URL mất tham số lọc).

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — "Cán bộ NV Trung ương", banner BTP·TW | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Entity + trạng thái | Danh sách TVV, đang đứng ở tab "Mới đăng ký"; mở chi tiết 1 TVV trạng thái Mới đăng ký | Danh sách TVV, tab "Mới đăng ký"; mở chi tiết TVV-BTP-TW-0003 (Mới đăng ký) | Không |
| Input / bộ lọc đang áp dụng | Tab trạng thái "Mới đăng ký" (khác tab mặc định "Đang hoạt động"); URL có tham số phân trang | Tab "Mới đăng ký" + từ khóa tìm kiếm "QA" (URL `?tuKhoa=QA&page=1`) → baseline 1 bản ghi | Không |
| Thao tác | Bấm nút "← Quay lại danh sách" ở đầu màn Chi tiết | Bấm đúng nút "← Quay lại danh sách" ở đầu màn Chi tiết | Không |

Kết luận: 0 GAP — tái hiện đúng. Baseline: tab "Mới đăng ký" + từ khóa "QA" → 1 bản ghi. Sau khi bấm "Quay lại danh sách": URL về `/chuyen-gia-tvv/danh-sach` (mất query), tab về "Đang hoạt động", ô tìm kiếm rỗng, danh sách trả 4 bản ghi ⇒ bộ lọc KHÔNG được giữ.
Đối chiếu SRS: SCR-IV-03 cell 2 (srs-fr-04-chuyen-gia-tvv.md dòng 1540) chỉ ghi: Nút "← Quay lại danh sách" → Click → SCR-IV-01. SCR-IV-01 §Quy tắc tương tác (dòng 1452-1459) KHÔNG có quy tắc ghi nhớ/khôi phục bộ lọc. ⇒ SRS im lặng về yêu cầu này → BA chốt.
