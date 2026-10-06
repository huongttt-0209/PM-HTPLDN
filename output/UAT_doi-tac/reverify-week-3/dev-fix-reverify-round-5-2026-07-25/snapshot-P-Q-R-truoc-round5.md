# Snapshot cột P/Q/R trước round 5 — 2026-07-25 11:05:32

Tab `UAT_TGPL Doanh Nghiệp-tuần 3` · 24 dòng cần re-verify.

Mục đích: chế độ `--reopen` của `sheet_verify_write.py` GHI ĐÈ cột R, xoá khối `── CÁCH VERIFY ──` do BA/dev viết. File này là đường lùi.


---

## Row 11 — CNKQHT_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Ô đính kèm "Tệp kết quả hỗ trợ" đã được bổ sung, ô "Kết luận" đã gỡ khỏi cửa sổ nhập, nội dung nhận đủ 10.000 ký tự và chặn khi vượt mốc — các điểm này đã đạt.
- Còn lỗi: đăng nhập bằng tài khoản người được phân công xử lý vụ việc (tư vấn viên), chọn tệp kết quả thì hệ thống báo "Forbidden" và không đính kèm được tệp nào.
- Còn lỗi: đăng nhập bằng tài khoản cán bộ nghiệp vụ thì tệp đính kèm lên được và hiện trong cửa sổ nhập, bấm Xác nhận có thông báo "Đã cập nhật kết quả"; nhưng thoát ra mở lại vụ việc thì mục Kết quả hỗ trợ chỉ còn phần nội dung, tệp vừa đính kèm biến mất, không xem hay tải lại được.
- Kiểm thử ngày 25/07/2026 trên vụ việc VV-BTP-TW-20260712-004 đang ở trạng thái "Đang xử lý".
```

---

## Row 16 — QLHSDNHTCP_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Cột SLA đã có nhãn mức kèm số ngày, nhưng mức gắn cho nhiều hồ sơ vẫn sai.
- Hồ sơ còn hạn bị báo quá hạn: CT-SEED-101 nộp 15/07, hạn xử lý 10 ngày làm việc là 29/07 nên vẫn còn hạn, đúng ra phải là "Sắp hết hạn", nhưng danh sách hiện "Quá hạn · 0 ngày LV".
- Hồ sơ mới trễ ít đã bị đẩy lên mức nặng nhất: CT-SEED-105 (nộp 03/07, hạn 17/07) trễ 5 ngày làm việc và CT-SEED-106 (nộp 01/07, hạn 15/07) trễ 7 ngày làm việc, nhưng cả hai đều hiện "Quá hạn nghiêm trọng"; mức này chỉ dùng khi trễ vượt quá 2 lần thời hạn.
- Hồ sơ đã kết thúc vẫn tiếp tục bị đếm quá hạn: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV"; CT-SEED-109 từ chối ngày 27/06 (hạn 03/07) và CT-SEED-110 đã hủy cũng bị gắn "Quá hạn nghiêm trọng".
- Nguyên nhân chung: hạn xử lý đang tính 10 ngày liên tục kể từ ngày nộp, không trừ thứ Bảy, Chủ nhật và ngày lễ, nên tỷ lệ thời hạn đã dùng bị đội lên và nhảy mức sớm (ví dụ CT-SEED-103 chú thích 188% trong khi tính đúng chỉ 150%).
- Duyệt hết 10 hồ sơ của cả 5 thẻ trạng thái chỉ thấy 2 mức "Quá hạn" và "Quá hạn nghiêm trọng"; không hồ sơ nào hiện "Bình thường" hoặc "Sắp hết hạn".
```

---

## Row 19 — QLHSDNHTCP_10

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Hồ sơ chưa quá hạn thì thanh thông tin tổng quan không có trường SLA. Mở CT-SEED-101 (Chờ tiếp nhận), thanh tổng quan chỉ có Mã HS, Quy mô DN và Trạng thái, không có mục cảnh báo thời hạn nào, trong khi ngoài danh sách hồ sơ này vẫn hiện nhãn SLA.
- Hồ sơ đã tiếp nhận thì trường SLA có hiện nhãn kèm số ngày, nhưng mức gắn sai giống lỗi ngoài danh sách: CT-SEED-108 thanh toán xong ngày 24/06 trong khi hạn là 29/06, tức xử lý đúng hạn, mà màn chi tiết vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV".
- Hai màn còn tính lệch nhau: cùng hồ sơ CT-SEED-107, chú thích tỷ lệ thời hạn đã dùng ngoài danh sách là 350% nhưng vào màn chi tiết lại là 400%, do màn chi tiết đếm từ ngày cán bộ tiếp nhận thay vì ngày doanh nghiệp nộp.
```

---

## Row 70 — THDG_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Nhập điểm vượt điểm tối đa (gõ 15 vào tiêu chí có điểm tối đa 10): hệ thống đã hiện dòng chữ "Điểm phải từ 0 đến 10" ngay dưới ô và chặn không cho lưu — phần này đã đạt.
- Nhập điểm âm (gõ -3 vào cùng ô đó rồi bấm ra ngoài): ô lặng lẽ tự đổi về 0, không hiện bất kỳ thông báo hay dòng chữ báo lỗi nào, ô cũng không được tô đỏ. Người dùng không biết giá trị vừa nhập đã bị hệ thống thay đổi.
- Điểm hợp lệ (nhập 8) vẫn lưu và hiển thị lại đúng, không có thông báo lỗi thừa.
- Đề nghị: trường hợp nhập dưới 0 cần được báo cho người dùng biết giống như trường hợp vượt điểm tối đa.
```

---

## Row 86 — QLTMBMHD_20

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Thao tác XÓA hàng loạt (1 thư mục rỗng + 1 thư mục còn biểu mẫu): đã đạt. Hộp xác nhận ghi "Xóa 1 thư mục? Hành động này không thể hoàn tác. Bạn có chắc không? (1 thư mục không đủ điều kiện (còn biểu mẫu) sẽ được bỏ qua)"; thông báo kết quả ghi "Đã xóa 1/2 thư mục. 1 thư mục không đủ điều kiện (còn biểu mẫu)." — nêu đủ số xử lý được, số bị bỏ qua và lý do.
- Thao tác CÔNG KHAI hàng loạt (1 thư mục có biểu mẫu + 1 thư mục rỗng): thông báo kết quả đã đạt ("Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).") NHƯNG hộp xác nhận trước khi chạy chỉ hiện "Công khai 2 thư mục?" kèm câu chung "Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo." — không cho người dùng biết sẽ bỏ qua mấy thư mục và vì sao.
- Hộp xác nhận của thao tác ẨN hàng loạt cũng vậy: "Ẩn 2 thư mục? Gỡ cờ công khai cho các thư mục đủ điều kiện." — thiếu số bị bỏ qua và lý do.
- Đề nghị đưa hộp xác nhận của Công khai và Ẩn về cùng cách viết như hộp xác nhận của Xóa (đã đúng).
- Không còn chữ "thất bại" ở bất kỳ thông báo nào — phần này đạt. Thư mục còn biểu mẫu không bị xóa nhầm — đúng.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
```

---

## Row 89 — TKTMBMHD_04

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Mở màn Thư viện biểu mẫu > Thư mục lần đầu: hai ô lọc "Lĩnh vực" và "Trạng thái" đã đổi chữ hiển thị thành "Tất cả", nhưng vẫn là chữ gợi ý mờ (xám nhạt) chứ chưa phải giá trị đang được chọn. Khi người dùng thực sự chọn một mục thì chữ mới đậm lên — nên nhìn vào ô lọc lúc mới mở màn vẫn không biết đang để "Tất cả" hay đang bỏ trống.
- Mở danh sách chọn của ô "Lĩnh vực": chỉ có 10 lĩnh vực (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư), KHÔNG có mục "Tất cả".
- Ô "Trạng thái" đã có đủ 4 mục (Tất cả / Nháp / Đã công khai / Đã ẩn) và "Tất cả" đứng đầu — phần này đạt; nhưng lúc mới mở màn mục "Tất cả" không được đánh dấu là đang chọn.
- Chọn Trạng thái = Nháp rồi chọn lại "Tất cả" thì danh sách trở về đủ 4 thư mục — phần này đạt.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
```

---

## Row 101 — QLBMHD_08

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Phần chặn và chữ thông báo: ĐÃ ĐẠT trên giao diện.
- Tệp .docx đúng cấu trúc Office có chèn chuỗi thử diệt virus (EICAR) bên trong nội dung: bị TỪ CHỐI, yêu cầu tải lên trả mã 400 với mã lỗi ERR-BM-07, thông báo hiện lên đúng chữ "Tệp chứa mã độc, không thể lưu trữ", dòng tệp chuyển sang trạng thái lỗi và tệp không được đính kèm vào biểu mẫu.
- Tệp rác đổi đuôi .docx cũng bị từ chối với đúng thông báo mã độc nêu trên (trước đây bị chặn ở bước kiểm định dạng).
- Kiểm tra lại danh sách biểu mẫu: không sinh ra bản ghi nào từ các lần thử trên.
- Việc bộ quét đọc được nội dung BÊN TRONG tệp nén Office đã được chứng minh qua kết quả trên.
- Còn 1 việc chưa thể xác nhận từ phía kiểm thử: bộ quét mã độc chạy TRƯỚC khi ghi tệp vào kho lưu trữ (không quan sát được từ giao diện). Theo hướng dẫn kiểm thử của case, cần Dev/An toàn thông tin xác nhận bằng văn bản điểm này rồi mới đóng case. Rất mong đội phát triển bổ sung xác nhận, sau đó chúng tôi sẽ chuyển sang Pass ngay.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
```

---

## Row 106 — QLBMHD_13

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Đã kiểm tra trên một biểu mẫu MỚI tạo qua luồng chuẩn (mã BM-20260724-005, tệp đính kèm qa-edit-src.docx, 931 B).
- Phần đã đạt: form Chỉnh sửa nay CÓ hiện tên tệp đang đính kèm (qa-edit-src.docx).
- Phần đã đạt: sửa Tên biểu mẫu rồi bấm Lưu mà KHÔNG chọn lại tệp thì lưu thành công, ô File biểu mẫu không báo lỗi bắt buộc; sau khi lưu, tệp đính kèm vẫn nguyên tệp cũ (đúng tên, kích thước vẫn 931 B).
- Còn thiếu 1: không tải được tệp đang đính kèm ngay trên form Chỉnh sửa. Tên tệp chỉ là dòng chữ, không bấm vào được; nút duy nhất cạnh tên tệp là "Gỡ bỏ tập tin", không có nút hay liên kết tải tệp về.
- Còn thiếu 2: form chưa nói rõ để trống ô tải tệp nghĩa là giữ nguyên tệp hiện tại. Toàn bộ chữ ở vùng File biểu mẫu chỉ có "Kéo thả hoặc click để chọn file" và "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB". Người dùng vẫn dễ hiểu nhầm là phải tải đè tệp mới.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
```

---

## Row 113 — TKBMHD_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Ý (b) — bỏ PDF khỏi ô lọc Định dạng: ĐÃ ĐẠT. Danh sách chọn của ô Định dạng chỉ còn đúng 5 mục: Tất cả, DOC, DOCX, XLS, XLSX — không còn mục PDF.
- Lọc chạy đúng: chọn DOCX ra 9 biểu mẫu, chọn XLSX ra 2 biểu mẫu, chọn lại Tất cả trở về đúng 11 biểu mẫu như lúc mới mở màn.
- Ý (a) — 4 ô lọc mặc định Tất cả: CHƯA ĐẠT. Khi mới mở màn Danh sách biểu mẫu (chưa bấm gì), cả 4 ô Thư mục, Lĩnh vực, Loại hình, Định dạng đều chỉ hiện chữ Tất cả dưới dạng chữ mờ gợi ý (màu xám nhạt), không phải giá trị đang được chọn: ô còn rỗng, và khi mở danh sách chọn thì mục Tất cả không được đánh dấu là đang chọn.
- Đối chiếu cho thấy đây không phải hạn chế hiển thị: sau khi người dùng tự tay chọn mục Tất cả thì chữ Tất cả chuyển sang màu đậm như một giá trị đã chọn, và mục Tất cả trong danh sách được đánh dấu. Nghĩa là trạng thái lúc mới mở màn vẫn là ô trống.
- Theo tiêu chí, hai ý (a) và (b) phải cùng đạt mới tính đạt, nên case này còn mở vì ý (a).
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
```

---

## Row 119 — IBMHD_07

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Kịch bản: thư mục đích QA-IMPORT-KQ mới tạo (trống). Chọn 4 tệp trong 1 lượt: 2 tệp .docx hợp lệ, 1 tệp qa-loi.txt sai định dạng, 1 tệp qa-hong.docx đúng đuôi nhưng nội dung hỏng.
- Phần đã đạt: 2 tệp hợp lệ vẫn được nhập bình thường, không bị chặn cả lô — mở danh sách lọc theo thư mục QA-IMPORT-KQ đếm đúng 2 biểu mẫu.
- Còn lỗi 1: màn kết quả cuối ghi "Nhập biểu mẫu hoàn tất: 2 thành công / 0 lỗi" — báo 0 lỗi trong khi thực tế có 2 tệp bị loại: qa-loi.txt bị loại ngay lúc chọn tệp, qa-hong.docx bị loại lúc tải lên (có thông báo "Tệp không hợp lệ hoặc bị hỏng" và dòng đếm ở bước chọn tệp ghi "Đã tải lên thành công: 2/3 · Có file lỗi"). Người dùng nhìn màn kết quả vẫn không biết mình mất 2 tệp nào.
- Còn lỗi 2: màn kết quả không có lối xem chi tiết tệp lỗi. Toàn màn chỉ có dòng kết quả và 2 nút "Quay lại danh sách" / "Nhập tiếp"; không có bảng liệt kê tên tệp lỗi kèm lý do.
- Ghi nhận thêm: ở bước Kiểm tra, bảng kiểm tra có liệt kê qa-loi.txt kèm lý do, nhưng qa-hong.docx không có dòng nào trong bảng đó.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Bộ ngành.
```

---

## Row 135 — QLDMCTHT_13

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Mở "Sửa" một chương trình hỗ trợ, chọn lại Thời gian kết thúc rồi bấm Đồng ý thì hệ thống báo "Dữ liệu không hợp lệ" và không lưu được; form vẫn mở, tải lại trang thì giá trị vừa chọn mất hẳn.
- Kèm theo là dòng nhắc ngày phải ở dạng năm-tháng-ngày, trong khi ô trên màn đang hiển thị và nhận ngày theo dạng ngày/tháng/năm.
- Ô "Thời gian bắt đầu" vẫn đang có sẵn giá trị 01/01/2020 trên form, không hề bỏ trống, nhưng hệ thống vẫn báo thiếu ngày bắt đầu.
- Lỗi lặp lại cả khi gõ tay lẫn khi chọn ngày từ lịch. Thêm mới một chương trình hỗ trợ cũng bị chặn y hệt, nên hiện không tạo mới lẫn không sửa được bản ghi nào ở mục Chương trình hỗ trợ.
- Hai điểm còn lại của phiếu đã đạt: form Sửa không còn ô "Danh mục cha", và ngày đang lưu nạp lên form đúng 01/01/2020 theo dạng ngày/tháng/năm.
```

---

## Row 140 — QLDMCQDVQL_12

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Ở mục Cơ quan đơn vị, chọn một đơn vị trên cây rồi bấm Sửa, nhập nội dung mới vào ô Địa chỉ (hoặc sửa ô Tên đơn vị) nhưng chưa bấm Lưu.
- Bấm Hủy: hệ thống thoát khỏi chế độ chỉnh sửa ngay lập tức, không hiện hộp thoại hỏi xác nhận, nội dung vừa nhập mất hẳn.
- Đang sửa dở mà bấm chọn một đơn vị khác trên cây: khung thông tin chuyển thẳng sang đơn vị mới, cũng không có cảnh báo nào, nội dung đang nhập bị bỏ.
- Chọn lại đúng đơn vị vừa sửa thì các ô trở về giá trị cũ, xác nhận là dữ liệu đang nhập đã mất mà người dùng không được hỏi trước.
- Khung chỉnh sửa hiện chỉ có hai nút Hủy và Lưu; đã thử trên hai đơn vị khác nhau, kết quả giống nhau.
```

---

## Row 148 — QLDMHSDNHT_13

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Mở [Sửa] một danh mục "Hồ sơ đề nghị hỗ trợ" đang có (đã thử "Đơn đề nghị hỗ trợ" và "Hồ sơ chứng minh điều kiện"): trường "Danh mục cha" đã được gỡ, nhưng khối "Thành phần bắt buộc → Thành phần 1" hiện ra hoàn toàn trống.
- Hai ô "Mã thành phần" và "Tên thành phần" có dấu * bắt buộc nhưng không nạp dữ liệu của bản ghi đang sửa; nút xóa khối "Thành phần 1" bị làm mờ, không bấm được.
- Bấm [Đồng ý] để lưu thì bị chặn, hiện lỗi "Mã thành phần là bắt buộc" và "Tên thành phần là bắt buộc" → không lưu được thay đổi trên bản ghi cũ nếu không tự nhập thêm một thành phần mới.
- Ngoài ra, cột "Loại" (Bắt buộc / Tùy chọn) hiển thị ở danh sách không có ô tương ứng trên biểu mẫu để xem hoặc chỉnh sửa.
```

---

## Row 153 — QLCHTHXLHS_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Bảng cấu hình thời hạn xử lý (SLA) hiện chỉ có các cột: Loại yêu cầu, Tên loại, Thời hạn (ngày LV), Vùng cảnh báo, Email, Thông báo app, Hành động — vẫn chưa có cột Số ngày bổ sung tối đa.
- Mở cửa sổ Sửa của dòng Vụ việc hỗ trợ pháp lý thì đã có ô Số ngày bổ sung tối đa với giá trị 5, tức là dữ liệu đã có nhưng chưa được đưa ra ngoài bảng để xem nhanh.
- Khối cảnh báo về ảnh hưởng khi lưu cấu hình cũng chưa xuất hiện trên thẻ SLA; nội dung này hiện chỉ nằm bên trong cửa sổ Sửa nên người dùng chỉ thấy khi đã mở cửa sổ.
- Các điểm còn lại đã đạt: không còn Hệ số quá hạn ở cả bảng và cửa sổ Sửa; xóa trắng Số ngày bổ sung tối đa bị chặn kèm thông báo yêu cầu nhập số nguyên dương và giá trị cũ giữ nguyên; dòng Hỏi đáp pháp luật không có ô này; khung giải thích 4 mức cảnh báo hiển thị đầy đủ ở đầu thẻ.
```

---

## Row 173 — QLPQCN_02

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Màn phân quyền không cho biết đang thao tác trên vai trò nào: tiêu đề chỉ ghi "Phân quyền vai trò", đường dẫn phía trên ghi "Vai trò / Chi tiết / Quyền hạn", không hiển thị tên hay mã vai trò ở bất kỳ vị trí nào trên màn. Người dùng không có cách tự xác nhận mình đang sửa đúng vai trò trước khi bấm Lưu.
- Chức năng "Reset về mặc định" hiện chỉ bỏ các thay đổi chưa lưu, chưa khôi phục bộ quyền mặc định của vai trò: sau khi lưu một tập quyền đã bị sửa rồi bấm Reset, hệ thống trả về đúng tập vừa lưu chứ không trở lại bộ quyền gốc của vai trò, dù thông báo xác nhận ghi là khôi phục bộ quyền mặc định.
- Nút "Reset về mặc định" cũng bị làm mờ khi màn chưa có thay đổi nào, nên không dùng được để đưa vai trò về mặc định ở trạng thái bình thường.
- Phần đã đạt: mở phân quyền từ danh sách vai trò nạp đúng bộ quyền của từng vai trò (hai vai trò kiểm thử cho hai tập quyền khác nhau); nút Reset có hỏi xác nhận trước khi áp, chọn Hủy thì tập quyền giữ nguyên; bấm Lưu và tải lại màn thì kết quả được giữ.
```

---

## Row 174 — QLPQCN_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Màn phân quyền hiển thị 14 nhóm chức năng dạng gập-mở, nhưng 5 nhóm đang lấy mã kỹ thuật làm tên nhóm: BIEU_MAU, CT_HTPLDN, DOANH_NGHIEP, NGUOI_HO_TRO, TU_VAN — trong khi 9 nhóm còn lại có tên tiếng Việt (Báo cáo, Chi trả, Đánh giá, Đào tạo, Hỏi đáp pháp luật, HTPL địa phương, Quản trị hệ thống, Tư vấn viên, Vụ việc HTPL).
- Tên từng quyền bên trong các nhóm đều viết tiếng Việt KHÔNG dấu, ví dụ "Cap nhat bao cao", "Duyet bao cao", "Xem nhat ky kiem toan" — không đồng nhất với phần còn lại của phần mềm.
- Các nội dung khác đã đạt: mọi nhóm mở ra đều có danh sách quyền, gồm cả quyền cơ bản (xem/thêm/sửa/xóa/phê duyệt/xuất) và quyền nghiệp vụ riêng; tích thêm 1 quyền rồi Lưu, tải lại màn vẫn giữ đúng; ô chọn ở đầu nhóm chọn được toàn bộ quyền trong nhóm và Lưu không báo lỗi.
```

---

## Row 186 — QLDKTK_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Mục "Tài khoản đăng nhập" trên biểu mẫu đăng ký hiện chỉ có 3 thành phần: Mật khẩu, Xác nhận mật khẩu và ô cam kết — vẫn chưa có ô Tên đăng nhập ở dạng chỉ đọc.
- Do không có ô này nên khi nhập Mã số thuế (thử 0101234567 rồi đổi sang 0107654321) cũng không có chỗ nào hiển thị tên đăng nhập tương ứng để doanh nghiệp biết mình sẽ đăng nhập bằng gì.
- Phần đã đạt: hai ô "Họ và tên người đăng ký" và "Số điện thoại" của người đăng ký đã được gỡ khỏi mục Tài khoản, không còn tồn tại ẩn trong trang; ô "Điện thoại doanh nghiệp" ở mục Thông tin doanh nghiệp vẫn giữ nguyên và vẫn bắt buộc.
- Đăng ký thử với đầy đủ thông tin bắt buộc vẫn thành công bình thường, không phát sinh lỗi bắt buộc nào liên quan đến hai ô đã gỡ.
```

---

## Row 286 — QLNDTVVCG_22

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Cửa sổ "Phân công chuyên gia": ô "Chuyên môn" đã hiển thị đúng tên lĩnh vực của chuyên gia khi chuyên gia chưa nhập chuyên ngành — phần này đã đạt.
- Vẫn còn lỗi ở khối "Thông tin cơ bản" của màn Thêm yêu cầu tư vấn: chọn đúng chuyên gia đó thì ô "Chuyên môn" vẫn hiển thị dấu "—", trong khi cửa sổ Phân công của cùng chuyên gia hiển thị "Thương mại". Hai nơi cho kết quả khác nhau với cùng một chuyên gia.
- Màn Sửa yêu cầu tư vấn: sau khi chọn chuyên gia, hệ thống không hiển thị ô "Chuyên môn" (cũng không có số điện thoại, email) như màn Thêm mới.
- Chưa kiểm được trường hợp chuyên gia trống cả chuyên ngành lẫn lĩnh vực (kỳ vọng hiển thị "Chưa cập nhật") vì hệ thống bắt buộc chọn ít nhất 1 lĩnh vực khi tạo/sửa hồ sơ chuyên gia.
```

---

## Row 289 — QLNDTVVCG_36

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Open`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
⚠️ Hành vi hủy hiện tại ĐÚNG ĐẶC TẢ — KHÔNG phải bug. Chỉ còn 1 việc dọn dẹp (BA chốt 24/07/2026).

THEO SRS (srs-fr-12-tv-chuyen-sau.md:238-244, Processing "Hủy yêu cầu"):
- Ở trạng thái ĐANG_TƯ_VẤN, CHỈ Cán bộ Phê duyệt được hủy; CB Nghiệp vụ / Chuyên gia bị chặn (:238, tag [QLNDTVVCG_36 chốt 2026-07-24]).
- Hủy chuyển TRỰC TIẾP ĐANG_TƯ_VẤN → HỦY, KHÔNG tạo trạng thái trung gian "chờ duyệt hủy" (:241).
- "Từ chối duyệt hủy" = Cán bộ Phê duyệt KHÔNG thực hiện hủy → bản ghi giữ nguyên ĐANG_TƯ_VẤN. Không cần màn duyệt hủy riêng trong app.
- Yêu cầu hủy của DN là văn bản/email NGOÀI hệ thống; hệ thống KHÔNG lưu thành cột riêng trên entity (:244).

→ Vì vậy: Kết quả thực tế (Cán bộ Phê duyệt hủy thẳng sang "Đã hủy") là ĐÚNG SRS. Kết quả mong đợi của đối tác (đòi trạng thái trung gian "chờ duyệt hủy" + luồng duyệt hủy trong app) TRÁI SRS → KHÔNG dựng thêm luồng này.

VIỆC DEV CÒN LẠI (cleanup — BA chốt 24/07/2026): gỡ phần dư đã lỡ xây cho cơ chế "DN gửi / duyệt yêu cầu hủy trong app" — theo BA là 3 cột lưu yêu-cầu-hủy + 2 endpoint (gửi / duyệt yêu cầu hủy). Căn cứ: SRS :244 nói yêu cầu hủy của DN nằm NGOÀI hệ thống, không lưu cột riêng. (Số cột/endpoint theo BA liệt kê; QA chưa mở được mã nguồn để đếm độc lập — dev đối chiếu khi gỡ.)

── CÁCH VERIFY sau khi Dev cleanup ──
Precondition: env https://18.143.165.120.nip.io; có TVCS ở trạng thái ĐANG_TƯ_VẤN.
1) Login Cán bộ Phê duyệt: mở bản ghi ĐANG_TƯ_VẤN → [Hủy yêu cầu] → nhập lý do → xác nhận → bản ghi chuyển THẲNG sang "Đã hủy" (không qua state trung gian).
2) Login Cán bộ Nghiệp vụ / Chuyên gia: nút [Hủy yêu cầu] phải bị ẩn/chặn ở bản ghi ĐANG_TƯ_VẤN.
3) Đối chiếu với dev: không còn 3 cột + 2 endpoint "yêu cầu duyệt hủy" trong hệ thống.
✅ PASS khi: (a) Cán bộ Phê duyệt hủy trực tiếp được; (b) CB NV/CG bị chặn ở ĐANG_TƯ_VẤN; (c) không còn cột/endpoint "yêu cầu duyệt hủy" dư.
❌ FAIL khi: vẫn còn cột/endpoint duyệt-hủy trong app, HOẶC CB NV/CG hủy được ở ĐANG_TƯ_VẤN.
⚠️ KHÔNG chấm FAIL vì thiếu màn "duyệt hủy" hay thiếu state "chờ duyệt hủy" — SRS KHÔNG yêu cầu các thành phần đó.
```

---

## Row 290 — QLNDTVVCG_40

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Tệp xuất ra vẫn luôn kèm sẵn cột "Nội dung tư vấn (đầy đủ)" với toàn bộ nội dung tư vấn; màn danh sách không có tùy chọn nào để người dùng chọn có xuất đầy đủ hay không.
- Tên tệp tải về dạng "tv-chuyen-sau-1784921668017.xlsx": phần đuôi là một dãy số máy sinh, người dùng không đọc được ngày và giờ-phút xuất tệp.
- Cột "Ngày tạo" trong tệp lệch 1 ngày so với màn danh sách: bản ghi hiển thị "25/07/2026 02:33" trên lưới nhưng trong tệp ghi "24/7/2026".
- Các điểm đã đạt: tệp có đủ các cột Mã tư vấn, Doanh nghiệp, Chuyên gia, Lĩnh vực, Tiêu đề, Trạng thái, Ngày bắt đầu, Ngày tạo; số dòng khớp lưới; xuất theo bộ lọc lĩnh vực cho đúng 1 dòng.
```

---

## Row 293 — QLHSPLDN_03

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Biểu mẫu Thêm/Sửa hồ sơ pháp lý đã có ô "Lĩnh vực pháp lý", ô "Mô tả" và ô "Tệp đính kèm"; ô "Số/Ký hiệu" đã được gỡ.
- Tạo mới 1 hồ sơ: chọn lĩnh vực "Lao động", nhập nội dung vào ô "Mô tả", đính 1 tệp PDF sạch dưới 20MB → lưu thành công.
- Mở lại đúng hồ sơ vừa tạo bằng nút [Sửa]: lĩnh vực và mô tả hiển thị đúng, NHƯNG ô "Tệp đính kèm" TRỐNG — không hiển thị tên tệp đã đính, không có cách nào xem hoặc tải lại tệp từ hồ sơ.
- Trong khi đó bảng danh sách vẫn hiển thị cột "Có tệp đính kèm" = "Có" cho hồ sơ này, tức tệp vẫn được lưu nhưng màn hồ sơ không hiển thị lại.
- Đã thử nhiều lần, kết quả giống nhau. Sửa một trường khác rồi lưu thì tệp không bị mất, nên đây là lỗi hiển thị khi mở lại hồ sơ.
- Đề nghị: mở lại hồ sơ phải liệt kê được các tệp đã đính kèm và cho xem/tải tệp.
```

---

## Row 296 — QLTLPLCVV_07

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Reopen`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
- Phần đã đạt: tư liệu đang ở trạng thái "Đã công khai" không còn hiển thị nút [Sửa] (chỉ còn Xem tệp / Hủy công khai / Xóa), không vào được biểu mẫu sửa.
- Còn lỗi: hủy công khai tư liệu đó (về "Nháp") rồi sửa ô "Mô tả" và bấm [Lưu] → hệ thống báo "Một hoặc nhiều file đã được gắn vào bản ghi khác" và KHÔNG lưu được.
- Làm tương tự trên một tư liệu vốn ở trạng thái "Nháp" (chưa từng công khai) → cũng báo đúng thông báo trên, không lưu được.
- Tạo mới một tư liệu khác có đính kèm 1 tệp rồi sửa mô tả → vẫn gặp lỗi giống hệt.
- Thử gỡ tệp đính kèm ra khỏi tư liệu rồi bấm [Lưu] → lưu thành công. Như vậy chỉ cần tư liệu còn giữ tệp đính kèm sẵn có thì không sửa được bất kỳ thông tin nào.
- Sau khi báo lỗi, nội dung vừa nhập ở ô "Mô tả" bị xóa trắng, người dùng phải nhập lại từ đầu.
- Đề nghị: tư liệu ở trạng thái "Nháp" (kể cả tư liệu vừa hủy công khai) phải sửa và lưu được bình thường trong khi vẫn giữ nguyên tệp đính kèm sẵn có.
```

---

## Row 307 — QLDNDHTPL_OOS_01

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Open`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
[Dev báo] Đã fix double-toast (1 thao tác → 1 thông báo). Nhưng DN đơn vị khác vẫn hiện nút Sửa + mở được biểu mẫu chỉnh sửa, mới chỉ chặn ở bước Lưu.
[BA chốt 24/07/2026] Phải ẨN nút Sửa/Xóa theo quyền (không chỉ chặn ở Lưu): CB Phê duyệt R* → ẩn; CB Nghiệp vụ → chỉ hiện với DN thuộc đơn vị mình. Áp cả nút "Chỉnh sửa" ở màn chi tiết SCR-V.III-02. Backend vẫn kiểm quyền — ẩn nút chỉ là UX. Căn cứ: srs-fr-07-doanh-nghiep.md:443, :451 [QLDNDHTPL_005_01 chốt 2026-07-24]. (Mã BA/SRS QLDNDHTPL_005_01 ↔ mã sheet QLDNDHTPL_OOS_01.)
── CÁCH VERIFY ──
Precondition: env https://18.143.165.120.nip.io.
1) Login CB Phê duyệt (R*): mở danh sách DN → nút Sửa/Xóa phải ẩn ở mọi dòng; mở chi tiết 1 DN → nút "Chỉnh sửa" cũng ẩn.
2) Login CB Nghiệp vụ (TW): dòng DN thuộc đơn vị mình → có Sửa/Xóa; dòng DN đơn vị khác → ẩn Sửa/Xóa (không chỉ chặn ở Lưu).
3) Regression double-toast: gây 1 lỗi (vd sửa DN đơn vị khác rồi Lưu) → chỉ hiện 1 thông báo lỗi.
✅ PASS: nút Sửa/Xóa ẩn đúng theo quyền + double-toast không tái diễn.
❌ FAIL: DN đơn vị khác vẫn hiện Sửa/Xóa (dù đã chặn ở Lưu), HOẶC vẫn 2 khung thông báo cho 1 thao tác.
```

---

## Row 308 — QLTLPLCVV_OOS_01

- **Trạng thái dev fix 1 (P):** `dev done`
- **Verify (Q):** `Open`

**DEV phản hồi lần 1 (R) — nguyên văn trước round 5:**

```
[Dev báo] Sửa tư liệu giờ lưu OK. Nhưng gỡ tệp trong form Sửa thì tệp vẫn còn — update mới chỉ re-link, chưa có logic UNLINK.
[BA chốt 24/07/2026] Phải thêm xóa thật: gỡ tệp → xóa file khỏi storage + gỡ liên kết FILE_DINH_KEM; mở lại tư liệu không còn tệp, cột "File" giảm. Nếu CÔNG_KHAI + hết tệp → cảnh báo CB NV. Căn cứ: srs-fr-12-tv-chuyen-sau.md:918-927 [GAP-X.1-02]. (Mã BA QLTLPLCVV_005_01 ↔ mã sheet QLTLPLCVV_OOS_01.)
── CÁCH VERIFY ──
Precondition: env https://18.143.165.120.nip.io; có tư liệu "Nháp" với ≥1 tệp đính kèm.
1) Regression save: mở tư liệu Nháp còn tệp → sửa Mô tả → Lưu → lưu thành công, giữ nguyên tệp (không còn báo "file đã gắn vào bản ghi khác").
2) Unlink: trong form Sửa gỡ 1 tệp → Lưu → mở lại tư liệu: tệp đó KHÔNG còn, cột "File" giảm 1.
✅ PASS: lưu-giữ-tệp OK + gỡ tệp thì tệp biến mất thật (khỏi storage + FILE_DINH_KEM).
❌ FAIL: gỡ tệp nhưng mở lại tệp vẫn còn / cột File không giảm; HOẶC còn báo "file đã gắn vào bản ghi khác" khi lưu.
```
