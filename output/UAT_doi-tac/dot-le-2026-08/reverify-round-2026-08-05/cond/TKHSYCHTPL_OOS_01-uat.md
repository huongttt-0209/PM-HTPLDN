# TKHSYCHTPL_OOS_01 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 145 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | Cán bộ nghiệp vụ xem danh sách vụ việc | `cbnv_tw` · CB_NV_TW · cấp TW | Không |
| Màn hình | Danh sách vụ việc HTPL, cột "Cảnh báo thời hạn" (đứng sau "Thời hạn xử lý") | Đúng cột đó, đã đối chiếu vị trí trong danh sách tiêu đề bảng | Không |
| Thao tác lọc | Lọc "Mức SLA" = "Sắp hết hạn" | Chọn đúng mục đó rồi bấm Tìm kiếm (`?mucSla=SAP_HET`) | Không |
| Hồ sơ trong phản ánh gốc | `VV-BTP-TW-20260712-006` và `…-005` | **Không còn trên môi trường này** — thay bằng hồ sơ cùng bản chất: đã đóng nhưng mức cảnh báo còn lưu "Sắp hết hạn" (`VV-BTP-TW-20260713-001`, trạng thái "Đã đánh giá", hạn 03/08/2026 đã trôi qua) | Không |
| Phạm vi rà nhãn | Cột chỉ được dùng 4 mức đã định nghĩa | Rà **69/69** hồ sơ qua cả 4 trang danh sách | Không |
| Cách đo | Đọc trên giao diện | Đọc bảng trên màn + đối chiếu mã mức lưu trong dữ liệu máy chủ | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Cột "Cảnh báo thời hạn" chỉ hiện đúng bốn mức đã định nghĩa**: rà 69/69 hồ sơ trên cả 4 trang, nhãn thu
  được chỉ gồm `Bình thường`, `Sắp hết hạn`, `Quá hạn`, `Quá hạn nghiêm trọng` (mức Quá hạn có kèm số ngày
  làm việc, ví dụ "Quá hạn · 3 ngày LV"). **Không dòng nào hiện "Đã hoàn thành"** — nhãn không tồn tại trong
  hệ thống mà phản ánh gốc bắt được đã hết. Đối chiếu dữ liệu máy chủ cũng chỉ có 4 mã
  `BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG`.
- **Danh sách chọn của bộ lọc "Mức SLA" cũng đúng 4 mức**: `Bình thường · Sắp hết hạn · Quá hạn ·
  Quá hạn nghiêm trọng`.
- **Bộ lọc và cột hiển thị nói cùng một điều**: lọc "Sắp hết hạn" → trả về 1 hồ sơ
  `VV-BTP-TW-20260713-001`, và cột "Cảnh báo thời hạn" của chính dòng đó hiện **"Sắp hết hạn"** — khớp với
  bộ lọc. Tình huống gây hiểu nhầm ở phản ánh gốc (lọc "Sắp hết hạn" nhưng cột ghi "Đã hoàn thành")
  **không còn**.
- **Hồ sơ đã đóng vẫn hiện đúng mức đang lưu** — đúng như BA chốt: hồ sơ trên đang ở trạng thái "Đã đánh giá"
  (đã đóng), hạn xử lý 03/08/2026 đã trôi qua, mức cảnh báo giữ nguyên "Sắp hết hạn". Cột hiển thị đúng giá
  trị đang lưu chứ không tự đổi sang nhãn khác. Các hồ sơ đã đóng khác cũng vậy (ví dụ `VV-BTP-TW-20260514-002`
  trạng thái "Từ chối" giữ mức "Quá hạn nghiêm trọng").
- **Hai phần BA chốt là đúng, dev không đụng**: (a) giữ nguyên mức cảnh báo của hồ sơ đã đóng — đúng như quan
  sát ở trên; (b) bộ lọc vẫn trả về hồ sơ đã đóng theo giá trị đã lưu — đúng, hồ sơ "Đã đánh giá" vẫn nằm
  trong kết quả lọc "Sắp hết hạn". Đây **không** phải căn cứ FAIL của phiếu này.

Ảnh: `../image/TKHSYCHTPL_OOS_01-uat-loc-sap-het-han-cot-khop.png`

## Ghi nhận thêm

- Hai hồ sơ nêu trong phản ánh gốc (`VV-BTP-TW-20260712-006`, `VV-BTP-TW-20260712-005`) không còn trên môi
  trường nghiệm thu này. Đã thay bằng hồ sơ đúng cùng bản chất (đã đóng + mức cảnh báo còn lưu "Sắp hết hạn"
  + hạn xử lý đã trôi qua) nên vẫn tái hiện được đúng tình huống của phản ánh.
- Không tạo, không sửa hồ sơ nào khi đo phiếu này — chỉ đọc và lọc.
