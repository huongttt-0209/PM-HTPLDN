# Đo lại trên môi trường bàn giao trước khi ghi verdict — 04/08/2026

> **Vì sao phải đo lại:** quyết định của BA ngày 04/08 dựa trên phép đo tệp PDF do tổ QA thực hiện
> **ngày 03/08 trên bản dựng V1.0.4**. Ghi `Reopen` cho 21 phiếu mà không kiểm lại hiện trạng là chấm
> theo trí nhớ — đúng kiểu đã từng báo Reopen oan. Phiếu này đo lại toàn bộ trên bản dựng đang chạy.

## Bảng đối chiếu điều kiện

| Điều kiện | Giá trị khi đo |
|---|---|
| Môi trường | `https://htpldn-uat.ospgroup.vn` — môi trường bàn giao |
| Bản dựng | **HTPLDN · V1.0.5** (đọc từ thanh bên trái) |
| Tài khoản | `cbnv_tw` · vai trò `CB_NV_TW` · Cục Bổ trợ tư pháp — Bộ Tư pháp · cấp TW |
| Thời điểm | 04/08/2026, 18:00–18:03 |
| GAP còn lại | Không |

---

## A. Nhóm 21 phiếu Xuất PDF (Vấn đề 16 · 17 · 18)

**Cách lấy tệp:** màn *Báo cáo thống kê* → Loại báo cáo **BC Số lượng hỏi đáp/vướng mắc pháp luật**
(đúng loại của phiếu `SLHDVM_07`) → Kỳ **Năm**, 01/01/2026–31/12/2026 → Đơn vị **Toàn quốc** → xuất PDF.
Tệp thu được: [`evidence/bao-cao-hoi-dap-2026-08-04.pdf`](evidence/bao-cao-hoi-dap-2026-08-04.pdf) — 28.741 byte, 2 trang.
Phần đầu phản hồi lưu tại [`evidence/xuat-pdf-header-phan-hoi-2026-08-04.json`](evidence/xuat-pdf-header-phan-hoi-2026-08-04.json).

### Kết quả đo từng thành phần khung văn bản hành chính

| Thành phần | Yêu cầu | Tệp đo ngày 04/08 trên V1.0.5 |
|---|---|:-:|
| Khổ A4 | Có | ✅ 595 × 842 pt — đúng A4 dọc |
| Phông chữ Times New Roman cỡ 13 | Có | ✅ phông nhúng `Tinos-Regular` / `Tinos-Bold` (bản tương thích số đo của Times New Roman) |
| Tên báo cáo · kỳ báo cáo · đơn vị · ngày tạo | Có | ✅ đủ 4 mục, nằm ngay đầu tệp |
| **Quốc hiệu + tiêu ngữ** | Có | ❌ **KHÔNG có** |
| **Tên cơ quan ban hành** | Có | ❌ **KHÔNG có** ở phần đầu tệp |
| **Ngày ký + họ tên người xuất báo cáo** | Có | ❌ **KHÔNG có** ở cuối tệp |
| Chỗ chừa cho con dấu | Có | ❌ không có |

Chữ đầu tiên của tệp là *"BC SỐ LƯỢNG HỎI ĐÁP/VƯỚNG MẮC PHÁP LUẬT"* — không có dòng quốc hiệu nào phía trên.
Cụm "Bộ Tư pháp" chỉ xuất hiện bên trong bảng số liệu (dòng *"Cục Bổ trợ tư pháp - Bộ Tư pháp — 44"*),
không phải phần tên cơ quan ban hành. Chữ cuối cùng của tệp là một dòng số liệu, không có khối ký.

⇒ **Vấn đề 16 còn nguyên trên V1.0.5.**

### Tên tệp (Vấn đề 17)

Phần đầu phản hồi ghi:

```
content-disposition: attachment; filename="bao-cao-hoi-dap-2026-08-04.pdf"
```

Khuôn BA chốt là `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`. Tên thực tế **thiếu giờ-phút** — xuất hai lần
trong cùng ngày sẽ ra cùng một tên tệp, đúng rủi ro mà BA nêu.

⇒ **Vấn đề 17 còn nguyên trên V1.0.5.**

### Chữ ký số (Vấn đề 18)

Cờ chữ ký số của tệp (`sigflags`) trả về `-1` — tệp **không có** trường chữ ký điện tử nào.
Đúng với kết luận của BA: nhóm IX **không áp** ký số. ⇒ **không phải lỗi**, chỉ cần trả lời đối tác.

### Kết luận nhóm 21 phiếu

`Reopen` là đúng hiện trạng, không phải Reopen theo trí nhớ: hai trong ba điểm (khung văn bản
hành chính và tên tệp) vẫn chưa có trên bản dựng đang chạy.

---

## B. Row 339 — `QLDMTCTV_OOS_13` (Vấn đề 21: tên gọi + mức bắt buộc của giấy hành nghề)

BA chốt: tên gọi chuẩn **"Giấy đăng ký hoạt động"** (NĐ 77/2008 Đ.13), mức **bắt buộc: Có**;
và ghi *"Dev action: Có **nếu phần mềm đang cho lưu hồ sơ trống giấy này — cần QA đo lại**"*.

### B1. Mức bắt buộc — phần mềm ĐÃ đúng

Biểu mẫu *Thêm mới Tổ chức tư vấn* đánh dấu bắt buộc (`*` đỏ) cho cả hai trường giấy tờ.
Ảnh: [`image/QLDMTCTV_OOS_13-form-themmoi-hai-ten-goi-khac-nhau.png`](image/QLDMTCTV_OOS_13-form-themmoi-hai-ten-goi-khac-nhau.png)

Đo thêm bằng phương pháp thứ hai — gửi hồ sơ rỗng thẳng lên máy chủ (`POST /api/v1/to-chuc-tu-vans`
với thân rỗng, chọn cách này để **không tạo ra bản ghi nào**): trả **HTTP 422** kèm

```
soGiayDkhd   → "Số Giấy đăng ký hành nghề là bắt buộc (NĐ 77/2008 Đ.13)"
ngayCapDkhd  → "Ngày cấp Giấy ĐKHĐ là bắt buộc (NĐ 77/2008 Đ.13)"
```

⇒ Phần mềm **không cho lưu hồ sơ trống giấy này**. Điều kiện *"nếu phần mềm đang cho lưu"* mà BA
nêu **không xảy ra** → phần bắt buộc không có việc cho Dev.

### B2. Tên gọi — phần mềm ĐANG SAI, và sai không nhất quán

Hai trường của **cùng một giấy** đang mang **hai tên khác nhau**, và không tên nào là tên chuẩn BA chốt:

| Nơi hiển thị | Chữ đang dùng | Tên chuẩn BA chốt |
|---|---|---|
| Nhãn trường trên biểu mẫu | "Số Giấy **ĐKHĐ** Sở TP" | "Số Giấy đăng ký **hoạt động**" |
| Nhãn trường kế bên | "Ngày cấp Giấy đăng ký **hành nghề**" | "Ngày cấp Giấy đăng ký **hoạt động**" |
| Câu báo lỗi của máy chủ | "Số Giấy đăng ký **hành nghề** là bắt buộc (NĐ 77/2008 Đ.13)" | — |
| Câu báo lỗi của máy chủ | "Ngày cấp Giấy **ĐKHĐ** là bắt buộc (NĐ 77/2008 Đ.13)" | — |

Điểm đáng chú ý: chính câu báo lỗi viện dẫn **NĐ 77/2008 Đ.13** — điều luật quy định
*Giấy đăng ký **hoạt động*** do Sở Tư pháp cấp, không có khái niệm "giấy đăng ký hành nghề" cho tổ chức.
Phần mềm dẫn đúng căn cứ nhưng gọi sai tên ngay trong cùng một câu.

⇒ Verdict row 339: **Open** — phần cần sửa là tên gọi hiển thị (4 chỗ trên), không phải mức bắt buộc.

---

## C. Ghi nhận thêm khi đi qua màn Tổ chức tư vấn (không thuộc 33 dòng đang ghi)

| Quan sát trên V1.0.5 | Liên quan |
|---|---|
| Bảng danh sách **vẫn còn cột "Đơn vị quản lý"** giữa "Lĩnh vực" và "Người đại diện" | Vấn đề 19 — row 331, đúng là còn lỗi |
| Thẻ trạng thái đếm được **5** (Đang hoạt động · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa) — **không thấy thẻ "Chờ phê duyệt"** với vai trò `CB_NV_TW` | Vấn đề 20 — row 332. BA phân tích trên giả định "phần mềm đang làm 6". Với vai trò cán bộ nghiệp vụ chỉ hiện 5. Cần BA xác nhận: thẻ "Chờ phê duyệt" chỉ dành cho vai trò phê duyệt, hay bị thiếu |

## D. Việc KHÔNG kết luận vì chưa đủ căn cứ

Bấm nút **"Xuất PDF"** trên giao diện hai lần đều không thấy phát sinh yêu cầu mạng, không có tệp
tải về, không có thông báo. Nhưng cả hai lần đều rơi vào lúc phiên đăng nhập của môi trường này
rớt (đặc tính đã biết của `ospgroup.vn`), nên **chưa loại trừ được nguyên nhân mất phiên**.
Tệp PDF ở mục A lấy bằng cách gọi thẳng máy chủ nên không chứng minh được nút giao diện có chạy hay không.

**Chưa log thành lỗi** — cần một lượt đo riêng với phiên còn sống để phân định. Đã ghi lại để không rơi.
