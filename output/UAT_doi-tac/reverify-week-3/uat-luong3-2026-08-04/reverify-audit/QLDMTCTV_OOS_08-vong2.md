# Re-verify vòng 2 — QLDMTCTV_OOS_08 (dòng 334, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, Cục Bổ trợ tư pháp – Bộ Tư pháp)
**Verdict:** ✅ Pass

---

## Triệu chứng gốc cần kiểm (2 ý — phải hết cả hai)

1. Biểu mẫu để **phẳng**, không nhóm nào thu gọn hay mở ra được.
2. Chỉ **2 trong 6 nhóm** có tiêu đề mục ("Công bố" và "Tệp đính kèm"); 4 nhóm còn lại không có tiêu đề phân tách.
Giống nhau ở cả Thêm mới và Chỉnh sửa.

## Nhật ký đo

### 13:46 — Chế độ Thêm mới: đếm nhóm có tiêu đề
Biểu mẫu `/chuyen-gia-tvv/to-chuc/tao-moi` nay dựng bằng khối nhóm thu gọn. Đếm được **6 nhóm, cả 6 đều có tiêu đề**, đúng thứ tự đặc tả:

| # | Tiêu đề nhóm | Trạng thái khi vừa mở |
|---|---|---|
| 1 | Thông tin cơ bản | **mở sẵn** (cao 338px) |
| 2 | Lĩnh vực & Nhân sự | thu gọn (cao 47px = chỉ còn thanh tiêu đề) |
| 3 | Liên hệ | thu gọn (47px) |
| 4 | Công bố | thu gọn (47px) |
| 5 | File đính kèm | thu gọn (47px) |
| 6 | Ghi chú | thu gọn (46px) |

Cây trợ năng cũng ghi nhận 6 nút bung/thu: nút 1 `expanded`, 5 nút còn lại `collapsed`.
Ảnh: `image/QLDMTCTV_OOS_08-v2-01-them-moi-6-nhom-thu-gon-nhom-1-mo.png` (đã mở đọc: nhóm 1 mũi tên chỉ xuống và đang mở; 5 nhóm dưới mũi tên chỉ sang phải, chỉ còn thanh tiêu đề).

⇒ **Ý số 2 của triệu chứng hết:** 6/6 nhóm có tiêu đề, không còn cảnh chỉ 2 nhóm có tiêu đề.

### 13:47–13:53 — Bấm THẬT vào tiêu đề nhóm để đo co/giãn (không chỉ nhìn)
Bấm lần lượt và đo lại chiều cao khối nhóm sau mỗi lần bấm:

| Thao tác | Kết quả đo |
|---|---|
| Bấm "Công bố" | 47px → **166px**, hiện 2 ô "Số quyết định công bố" + "Ngày quyết định công bố" |
| Bấm "File đính kèm" | 47px → **291px**, hiện vùng kéo thả tệp |
| Bấm "Liên hệ" (lần 1) | 252px → **47px** (thu gọn lại) |
| Bấm "Liên hệ" (lần 2) | 47px → **252px** (mở ra lại) |
| Bấm "Thông tin cơ bản" | 338px → **47px** (nhóm mặc định mở cũng thu gọn được) |
| Bấm lại "Thông tin cơ bản" | 47px → **338px** |

⇒ **Ý số 1 hết:** nhóm co/giãn được cả hai chiều, kể cả nhóm mặc định mở.

Ảnh mở hết 6 nhóm: `image/QLDMTCTV_OOS_08-v2-02-them-moi-mo-het-6-nhom-phan-tren.png` (đã mở đọc: 3 nhóm đầu bung ra với đủ ô nhập) và `image/QLDMTCTV_06-v2-02-them-moi-mo-het-6-nhom-du-3-truong-cong-bo-va-tep.png` (phần dưới: Công bố, File đính kèm, Ghi chú).

### 14:01 — Lặp lại ở chế độ Chỉnh sửa
Mở Sửa **TC-BTP-TW-0003 "Trung tâm TVPL Gamma Đà Nẵng"**: cùng 6 nhóm có tiêu đề, nhóm 1 mở sẵn, 5 nhóm thu gọn.
Bấm thật: "Công bố" 166px → 47px → 166px; "Thông tin cơ bản" 338px → 47px → 338px.
Ảnh: `image/QLDMTCTV_OOS_08-v2-03-che-do-Sua-cung-6-nhom-thu-gon-duoc.png` (đã mở đọc: màn "Chỉnh sửa Tổ chức tư vấn", nhóm 1 mở với dữ liệu điền sẵn, 5 nhóm dưới thu gọn).

### Lưu ý kỹ thuật khi đo (để người sau khỏi hiểu nhầm)
Chụp ảnh chế độ **toàn trang** (`fullPage`) làm trình duyệt đổi kích thước khung nhìn, khiến các nhóm bị dựng lại về trạng thái mặc định (chỉ nhóm 1 mở) → ảnh chụp ra trông như "không mở được". Đã đổi sang chụp theo khung nhìn thường thì trạng thái mở giữ nguyên. Đây là hiện tượng của công cụ đo, không phải của phần mềm; số liệu chiều cao đo trực tiếp ở trên mới là phép đo chuẩn.

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`
- dòng 1664: "Loại màn hình: Biểu mẫu nhập liệu (6 nhóm)"
- dòng 1669: liệt kê 6 nhóm "Thông tin cơ bản, Lĩnh vực & Nhân sự, Liên hệ, Công bố, File đính kèm, Ghi chú"
- dòng 1676 / 1683 / 1686 / 1691: loại giao diện "nhóm thu gọn"; riêng nhóm 1 "Mặc định mở"

Tên 6 nhóm trên màn khớp từng chữ với dòng 1669; hành vi thu gọn + nhóm 1 mặc định mở khớp dòng 1676.

### Kết luận
Cả 2 ý của bug gốc đều hết ở cả Thêm mới lẫn Chỉnh sửa ⇒ **Pass**.
