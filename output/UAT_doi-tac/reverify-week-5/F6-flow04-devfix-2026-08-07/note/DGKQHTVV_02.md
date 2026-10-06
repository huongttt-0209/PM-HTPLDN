⚠️ CẦN BA XÁC NHẬN — 3 vế đo được đều đạt, 3 vế đặc tả chưa quy định nên chưa chấm được.

ĐÃ ĐO
Env nội bộ 18.143.165.120.nip.io, bó mã index-DsMHK7Dp.js (lên lúc 01:51 ngày 07/08), tài khoản cbnv_tw_04 (Cán bộ Nghiệp vụ Trung ương), vụ việc VV-BTP-TW-20260806-003 đang "Đã đánh giá", cùng đơn vị tài khoản đo. Đo lúc 07/08/2026 02:00-02:12. Không seed, không sửa dữ liệu.

ĐÃ ĐẠT
1) Nhóm Đánh giá hiện đủ 5 trường đặc tả yêu cầu (srs-fr-05-vu-viec.md:1734): Điểm chất lượng tư vấn 9/10, Điểm đúng thời hạn 8/10, Điểm thái độ phục vụ 10/10, Điểm tổng 9/10, Nhận xét. 14/14 ô đều hiển thị thật, không ô nào ẩn.
2) Giá trị trên màn khớp đúng bản ghi đã lưu: đọc lại bản ghi vụ việc từ máy chủ được 9 - 8 - 10 - tổng 9, nhận xét QA-DGKQ-20260806-1634, ngày 06/08/2026 16:34. Hai đường đo khớp nhau.
3) Toàn bộ nhãn và giá trị là tiếng Việt, không lộ mã kỹ thuật, không có null/undefined (srs-fr-05-vu-viec.md:1492 và :1622).
Hai trường thêm "Người đánh giá" và "Ngày đánh giá" tuy không nằm trong bảng thành phần màn hình nhưng có căn cứ ở mô hình dữ liệu (:2115, :2122), nên theo quy ước UI-12 (srs-v3.5.md:584) là bảng đặc tả bị sót chứ phần mềm không sai.

CHƯA CHẤM ĐƯỢC - CẦN BA CHỐT
a) Bộ nhãn tiếng Việt và bố cục của nhóm Đánh giá: bảng thành phần màn hình (:1734) ghi mã kỹ thuật, trong khi quy ước của chính mục đó (:1486) nói cột ấy phải là chữ người dùng nhìn thấy, còn :1492 và :1622 lại cấm mã kỹ thuật lên giao diện; tài liệu thiết kế mà srs-v3.5.md:567 trỏ tới không có trong bộ đặc tả. Vì vậy không có chuẩn để chấm vế "hiển thị giống với thiết kế".
b) Đặc tả có bổ sung hai trường "Người đánh giá" và "Ngày đánh giá" vào bảng thành phần màn hình không.
c) Đặc tả có đặt tiêu chí "không tràn, không bẻ vỡ giá trị" cho vùng nhóm chi tiết không - hiện :1570 chỉ áp cho cột text trong bảng danh sách.
d) Điểm tổng hiển thị mấy chữ số thập phân và làm tròn ra sao - :2462 chỉ áp cho thang tư vấn viên 1-5 và loại trừ rõ trường hợp đánh giá vụ việc này.

ĐIỂM CẦN LƯU Ý CỦA VẾ (c)
Bảng của nhóm Đánh giá chia cột rất lệch: cột giá trị thứ nhất chỉ rộng 64-65px (trừ đệm hai bên còn vùng chữ 31-32px), trong khi cột giá trị thứ hai rộng 238px và cột thứ ba rộng 152px. Chuỗi dạng "x/10" cần đúng khoảng 31px, tức nằm SÁT ngưỡng của cột thứ nhất, nên chỉ cần chữ in đậm hoặc hụt 1px là vỡ dòng.
Đo được trên vụ việc VV-BTP-TW-20260806-003: ô "Điểm tổng" (in đậm) bị bẻ làm hai dòng, dòng trên "9/1" dòng dưới "0".
Đo thêm trên vụ việc VV-QAW7-DG01 cùng màn: vùng chữ cột thứ nhất còn 31px nên CẢ ô "Điểm chất lượng tư vấn" (chữ thường) LẪN ô "Điểm tổng" đều bị bẻ hai dòng — "4/1"/"0" và "7/1"/"0". Vậy nguyên nhân là bề rộng cột thứ nhất quá hẹp, không phải riêng chuyện chữ in đậm.
Giá trị vẫn đọc ra được nên chưa mất dữ liệu, nhưng vế "dữ liệu hiển thị không bị tràn, đè lên nhau" của phiếu đang KHÔNG được đáp ứng trọn vẹn. Nếu BA xác nhận đặc tả có tiêu chí này thì đây là lỗi cần dev sửa, hướng sửa nằm ở cách chia bề rộng cột. Ngoài hiện tượng bẻ dòng: không ô nào chồng lấn, không ô nào bị cắt mất chữ, trang không cuộn ngang.

BẰNG CHỨNG
Toàn nhóm Đánh giá của vụ việc VV-BTP-TW-20260806-003: https://drive.google.com/file/d/1zvSw030Fv-hRH-0UO9RdgLPk97PvzjA6/view?usp=drivesdk
Ô Điểm tổng bị bẻ dòng ("9/1" xuống dòng "0"): https://drive.google.com/file/d/1T-5tZbybeDH5HLM00x8IBx8mHmmrkHQh/view?usp=drivesdk
Cùng hiện tượng bẻ dòng ở vụ việc khác (VV-QAW7-DG01, cả ô chữ thường lẫn ô in đậm): https://drive.google.com/file/d/1INRY9n_US_ET8W6F-mrZPUOSaAAk409p/view?usp=drivesdk

GIỚI HẠN
Kết luận chỉ có hiệu lực cho env nội bộ và bó mã index-DsMHK7Dp.js đã đo. Bằng chứng gốc của đối tác quay trên môi trường nghiệm thu khác. Lượt đo này dùng bộ điểm 9-8-10 chia hết cho 3 nên không dùng để kết luận công thức tính điểm tổng; việc đó thuộc dòng 68.
