# Bảng đối chiếu điều kiện — QLDXDTTH_10 (re-verify vòng 2, lượt đo lại 05/08/2026)

Loại bug: **cột "Người đề xuất" ở bảng Đề xuất đào tạo** → phụ thuộc nguồn gửi của bản ghi ⇒ bắt buộc điền bảng.
Tiêu chí lấy từ ô *DEV phản hồi lần 2* của chính dòng này (phần "Phần còn lỗi").

| Điều kiện | Bug gốc (note vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** | Không |
| Vai trò | Cán bộ nghiệp vụ (đã đo cả cấp ĐP và TW) | `cbnv_tw` · CB_NV_TW · Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW; đối chứng thêm `admin` · **QTHT** (phạm vi toàn hệ thống) | Không |
| Màn hình | Đào tạo, tập huấn → Chương trình đào tạo → tab "Đề xuất đào tạo" | Đúng màn đó, đi bằng menu bên trái + thẻ tab, không gõ địa chỉ | Không |
| Bảng có cột "Người đề xuất" | Đã có (9 cột) | **Có** — 9 cột, cột "Người đề xuất" nằm giữa "SL dự kiến" và "Trạng thái" | Không |
| **Tiền đề của phần CÒN LỖI** | ≥1 đề xuất **gửi từ chuyên trang**, người gửi **không dùng tài khoản** trong phần mềm (note đo được 10/16 bản ghi thuộc nhóm này) | **KHÔNG CÒN bản ghi nào thuộc nhóm này** trong môi trường | **CÓ GAP — không đo được phần còn lỗi** |

**Kết luận: CÒN 1 GAP** — phần đã sửa kiểm được và đạt; phần còn lỗi **không có dữ liệu để chấm**.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6)

### A. Phần bảng và màn chi tiết — kiểm được, đạt

- ✅ Bảng có đủ **9 cột**: Nội dung · Lĩnh vực · Thời gian mong muốn · Địa điểm mong muốn · SL dự kiến · **Người đề xuất** · Trạng thái · Ngày tạo · Hành động.
- ✅ **7/7 bản ghi** hiện đúng **họ tên kèm đơn vị** ở cột Người đề xuất (vd `QA NHT Trung uong · Cục Bổ trợ tư pháp - Bộ Tư pháp`, `QA UAT Kiem Thu DN · Sở Tư pháp Hà Nội`, `QA UAT DN An Giang · Sở Tư pháp An Giang`). Không bản ghi nào hiện dấu gạch ngang.
  Ảnh: [`../image/QLDXDTTH_10-r3-de-xuat-7-dong-du-cot-nguoi-de-xuat.png`](../image/QLDXDTTH_10-r3-de-xuat-7-dong-du-cot-nguoi-de-xuat.png)
- ✅ **Màn chi tiết** cũng có dòng "Người đề xuất" với đủ họ tên + đơn vị.
  Ảnh: [`../image/QLDXDTTH_10-r3-chi-tiet-co-nguoi-de-xuat.png`](../image/QLDXDTTH_10-r3-chi-tiet-co-nguoi-de-xuat.png)

### B. Phần "còn lỗi" — không đo được, và đã loại trừ từng khả năng

Nhóm bản ghi mà note vòng 2 nêu (10/16 đề xuất trống người đề xuất, khoảng 23/06–25/07, gồm *"TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026"* và *"TKM đề xuất kiểm thử chức năng"*) **không còn tồn tại**.

Ba khả năng đã lần lượt loại trừ:

- ❌ **Không phải bị bộ lọc che.** Thanh phân trang ghi `Hiển thị 1-7 / 7 kết quả`, không có bộ lọc nào đang bật. Hỏi thẳng dữ liệu của màn với cỡ trang 200 cũng trả về `total = 7`, `0` bản ghi trống người đề xuất.
- ❌ **Không phải do phạm vi xem của vai trò.** Đăng nhập **Quản trị hệ thống** (`QTHT`, phạm vi toàn hệ thống) hỏi cùng dữ liệu với cỡ trang 500: vẫn **đúng 7 bản ghi**, **0** bản ghi trống người đề xuất, danh sách trùng khít với những gì cán bộ TW nhìn thấy. ⇒ các bản ghi đã bị xoá khỏi môi trường, không phải bị giấu.
- ❌ **Không tạo lại được.** Chỉ tồn tại đúng một đường tạo đề xuất và người đề xuất luôn lấy từ tài khoản đang đăng nhập — mô tả dữ liệu đầu vào của chức năng tạo (`CreateDeXuatDaoTaoDto`) chỉ có `linhVucId · noiDung · thoiGianMongMuon · diaDiemMongMuon · soLuongDuKien`, **không có trường người đề xuất** để đặt rỗng. Trong toàn bộ nhóm chức năng dành cho chuyên trang cũng **không có đầu mối nào cho đề xuất đào tạo**.
- ❌ **Không đi vòng qua chuyên trang được.** Toàn bộ nhóm chức năng chuyên trang trên môi trường này bị chặn ở tầng chứng thư: gọi thử 2 đầu mối đều trả `401` kèm mã `ERR-AUTH-MTLS-01` (*mTLS client certificate verification failed*).

### Kết luận

- Phần **kiểm được** đã đạt: cột "Người đề xuất" có ở cả bảng lẫn màn chi tiết, hiển thị đủ họ tên + đơn vị cho **mọi bản ghi đang tồn tại**.
- Phần **note vòng 2 nêu là còn lỗi** thì **không còn dữ liệu để chấm**, và **không có bằng chứng nào cho thấy phần mềm đang sai** ở thời điểm đo.
- Để chấm dứt điểm cần **khôi phục hoặc seed lại ≥1 đề xuất có người gửi không phải tài khoản trong phần mềm**. Việc này QA không tự làm được trên môi trường hiện tại.

> ⚠️ Không chấm **Pass** vì chưa chạy được đúng kịch bản của phần còn lỗi (cấm Pass bằng quan sát tĩnh).
> ⚠️ Cũng không có căn cứ để khẳng định **"vẫn còn lỗi"** — mọi bản ghi quan sát được đều đúng.
