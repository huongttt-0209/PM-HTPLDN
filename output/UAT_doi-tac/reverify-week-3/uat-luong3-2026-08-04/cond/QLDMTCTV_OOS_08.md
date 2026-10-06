# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_08 (dòng 334) — Biểu mẫu không chia 6 nhóm thu gọn

**Kết luận:** Pass — biểu mẫu nay chia đúng 6 nhóm có tiêu đề, bấm tiêu đề thì co/giãn được cả hai chiều, ở cả Thêm mới lẫn Chỉnh sửa.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (`cbnv_tw`, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbnv_tw` — cùng vai trò, cùng đơn vị | Không |
| Màn hình / entity + trạng thái | Biểu mẫu Thêm mới **và** Chỉnh sửa Tổ chức tư vấn | Đo cả hai: `/to-chuc/tao-moi` và `/to-chuc/{id}/chinh-sua` (TC-BTP-TW-0003, Đang hoạt động) | Không |
| Dữ liệu tiền đề | Một tổ chức bất kỳ để mở chế độ Sửa | TC-BTP-TW-0003 "Trung tâm TVPL Gamma Đà Nẵng" — hồ sơ có sẵn từ trước | Không |
| Thao tác / input — **ý 1: nhóm có thu gọn/mở được không** | Không nhóm nào co/giãn được | **Bấm thật vào tiêu đề nhóm**, đo chiều cao khối trước/sau: Công bố 47↔166px · File đính kèm 47↔291px · Liên hệ 252↔47↔252px · Thông tin cơ bản 338↔47↔338px. Lặp lại ở chế độ Sửa cho cùng kết quả | Không |
| Thao tác / input — **ý 2: đủ 6 tiêu đề nhóm chưa** | Chỉ 2/6 nhóm có tiêu đề | Đếm được **6/6 nhóm có tiêu đề**: Thông tin cơ bản · Lĩnh vực & Nhân sự · Liên hệ · Công bố · File đính kèm · Ghi chú — đúng tên và thứ tự đặc tả dòng 1669 | Không |
| Trạng thái mặc định khi vừa mở | — | Nhóm 1 mở sẵn, 5 nhóm còn lại thu gọn — đúng "riêng nhóm 1 mặc định mở" (dòng 1676) | Không |

**Bằng chứng:**
- `image/QLDMTCTV_OOS_08-v2-01-them-moi-6-nhom-thu-gon-nhom-1-mo.png` — Thêm mới: 6 thanh tiêu đề nhóm, nhóm 1 mở (mũi tên xuống), 5 nhóm thu gọn (mũi tên phải).
- `image/QLDMTCTV_OOS_08-v2-02-them-moi-mo-het-6-nhom-phan-tren.png` — sau khi bấm mở hết: các nhóm bung ra kèm ô nhập.
- `image/QLDMTCTV_OOS_08-v2-03-che-do-Sua-cung-6-nhom-thu-gon-duoc.png` — chế độ Sửa TC-BTP-TW-0003: cùng 6 nhóm, nhóm 1 mở, 5 nhóm thu gọn.
- Số liệu chiều cao khối nhóm trước/sau mỗi lần bấm: xem `reverify-audit/QLDMTCTV_OOS_08-vong2.md`.
