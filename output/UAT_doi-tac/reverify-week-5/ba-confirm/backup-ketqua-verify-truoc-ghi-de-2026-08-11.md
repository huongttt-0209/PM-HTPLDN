# Bản sao nội dung cột "Kết quả verify" TRƯỚC khi ghi đè — 2026-08-11

Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219).
Ghi đè theo quyết định BA tại [phan-hoi-ba-6-dong-con-treo-2026-08-11.md](BA-phan-hoi/phan-hoi-ba-6-dong-con-treo-2026-08-11.md).
Cả 6 dòng: cột `Trạng thái dev fix` đổi `BA confirm` → `Bug`.
Nhật ký ghi: `output/UAT_doi-tac/tools/sheet_update_audit.jsonl`.

---

## Dòng 20 · `QLLKHDTBD_09` — nội dung cũ

```
⚠️ Cần BA xác nhận — phần lọc đã đạt, phần danh mục cột tệp xuất xin ý kiến BA.

Đo trên môi trường https://18.143.165.120.nip.io, bản dựng bó mã index-D4Buvu4S.js (bản cập nhật lúc 19:23 ngày 06/08/2026 giờ máy chủ, thẻ phiên bản W/"6a74df15-428"), lúc 03:00–03:07 ngày 07/08/2026. Tài khoản cbnv_tw_02 — Cán bộ Nghiệp vụ Trung ương (CB_NV_TW), đơn vị BTP · TW, đúng vai trò như trong tư liệu nghiệm thu. Đã tải lại trang trước khi đo để chắc chắn không chạy trên bản cũ còn lưu trong trình duyệt. Chuỗi phiên bản hiển thị ở chân thanh điều hướng ghi V1.0.9; chúng tôi đối chiếu bản dựng bằng thẻ phiên bản và bó mã nêu trên chứ không dựa vào chuỗi này.

Màn đo: Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách (/dao-tao/ke-hoach/danh-sach).

Tiền đề: khi KHÔNG đặt bộ lọc, danh sách có 14 bản ghi trong phạm vi dữ liệu của tài khoản. Con số 14 lấy từ tổng số bản ghi máy chủ trả về, không đếm bằng mắt, và được kiểm chéo bằng số trên các thẻ trạng thái (Nháp 7 + Chờ duyệt 2 + Đã duyệt 4 + Đã công khai 1 + Từ chối 0 = 14).

── PHẦN 1 — Xuất Excel theo điều kiện lọc hiện tại: ĐÃ ĐẠT ──

Chúng tôi đo hai bộ lọc, mỗi lần đều bấm nút "Xuất Excel" trực tiếp trên giao diện (không gọi lệnh thay thao tác), và không dừng ở chỗ "tải được tệp" mà mở tệp ra đếm nội dung bên trong.

Lần 1 — lọc theo Trạng thái = "Đã duyệt": màn còn 4 kết quả (trên tổng 14). Hệ thống báo "Xuất Excel thành công" và tải về tệp ke-hoach-dao-tao-1786046602595.xlsx. Mở tệp: đúng 4 dòng dữ liệu, và 4 mã kế hoạch trong tệp trùng khít 4 mã trên màn (KH-20260803-0001, KHDT-QAW7-01, KHDT-2026-001, KHDT-SEED-0001); cột Trạng thái của cả 4 dòng đều là "Đã duyệt".

Lần 2 — lọc Từ ngày 01/07/2026 đến Đến ngày 31/07/2026, đúng bộ lọc đã dùng trong tư liệu nghiệm thu: màn còn 1 kết quả. Tệp tải về ke-hoach-dao-tao-1786046777916.xlsx có đúng 1 dòng dữ liệu, là bản ghi KH-20260803-0003 — đúng bản ghi duy nhất trên màn.

Số đo quyết định: 4 dòng khi màn 4 kết quả, và 1 dòng khi màn 1 kết quả, trong khi danh sách chưa lọc có 14 bản ghi. Nếu chức năng xuất bỏ qua bộ lọc thì cả hai tệp đã phải có 14 dòng. Ngoài ra, nội dung màn gửi lên chức năng xuất có mang đúng các tham số đang lọc (trạng thái ở lần 1; cả hai mốc ngày ở lần 2), cho thấy tệp được tạo theo bộ lọc hiện tại. Như vậy triệu chứng đã ghi trên phiếu — "Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách" — không tái hiện trên bản dựng đo.

Căn cứ đặc tả cho phần này: srs-v3.5.md:5570 quy định "Export Excel: Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file", áp dụng cho "Toàn bộ CRUD list"; srs-fr-03-dao-tao.md:2243 xác nhận quy tắc này áp cho FR-III-14; srs-fr-03-dao-tao.md:1775 ghi 'Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng'; srs-fr-03-dao-tao.md:1175 ghi bước xử lý "Lấy danh sách theo filter, tối đa 10.000 dòng".

Phạm vi hiệu lực của phần 1: cả hai lần đo đều có số kết quả sau lọc (4 và 1) nhỏ hơn cỡ trang đang đặt (20 dòng/trang), và tổng dữ liệu (14) cũng nhỏ hơn cỡ trang, nên phép đo này khẳng định tệp bám theo bộ lọc, nhưng chưa tách bạch được trường hợp số kết quả sau lọc lớn hơn một trang. Chúng tôi nêu rõ để không ai hiểu kết quả rộng hơn thực tế.

── PHẦN 2 — Trường "Người tạo", "Ngày tạo" trong tệp xuất: XIN Ý KIẾN BA ──

Hiện trạng đo được: hàng tiêu đề của tệp xuất, giống hệt nhau ở cả hai tệp nêu trên, nguyên văn gồm 7 cột:

Mã KH | Tên kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái

Tệp KHÔNG có cột "Người tạo" và KHÔNG có cột "Ngày tạo". Chúng tôi không so tên cột theo chuỗi chữ cứng mà đã đối chiếu theo ý nghĩa, có xét các cách gọi khác như Người lập, Ngày lập, Thời điểm tạo, Cán bộ tạo: không cột nào trong 7 cột trên chứa họ tên người, và hai cột ngày duy nhất là thời gian hiệu lực của kế hoạch chứ không phải ngày lập bản ghi. Ví dụ quyết định: bản ghi KH-20260803-0003 trong tệp có Từ ngày 05/07/2026 và Đến ngày 25/07/2026, trong khi Ngày tạo của chính bản ghi đó trên màn là 03/08/2026 — ba giá trị khác nhau.

Xin lưu ý một điểm để tránh hiểu nhầm phạm vi: BẢNG HIỂN THỊ TRÊN MÀN đã có đủ hai cột "Người tạo" và "Ngày tạo" kèm dữ liệu thật (ví dụ "CB Nghiệp vụ - Trung ương" và "03/08/2026"), đúng như đặc tả màn quy định. Khoảng trống chỉ nằm ở tệp Excel xuất ra.

CẦN BA CONFIRM: đối tác kỳ vọng tệp Excel xuất từ màn Kế hoạch đào tạo năm phải có trường "Người tạo" và "Ngày tạo"; SRS quy định hai cột này thuộc BẢNG HIỂN THỊ TRÊN MÀN (srs-fr-03-dao-tao.md:1795-1796) nhưng không có điều khoản nào quy định danh mục cột của TỆP EXCEL XUẤT RA — phần xuất Excel chỉ ràng buộc phạm vi dữ liệu ("theo bộ lọc hiện tại", tối đa 10.000 dòng) tại srs-v3.5.md:5570 và srs-fr-03-dao-tao.md:1775, :1175; đồng thời mục "Outputs — Danh sách" của FR-III-14 tại srs-fr-03-dao-tao.md:1189-1200 lại KHÔNG có hai trường này, tức bản thân đặc tả đang có hai định nghĩa khác nhau cho chữ "danh sách"; web/dev hiện tại xuất tệp 7 cột không có "Người tạo" và "Ngày tạo".

Mục đích của việc xin ý kiến là BỔ SUNG NỘI DUNG NÀY VÀO ĐẶC TẢ để các vòng nghiệm thu sau có căn cứ chấm thống nhất — KHÔNG phải để chặn bàn giao. Xin lưu ý thêm: đây không phải lỗi mới phát sinh từ bản sửa lần này; tư liệu nghiệm thu vòng đầu (25/07) cho thấy tệp xuất đã gồm đúng 7 cột như trên ngay từ thời điểm đó.

Ba câu hỏi cụ thể xin BA quyết:

1. Tệp Excel xuất từ màn Kế hoạch đào tạo năm phải gồm đúng những cột nào — lấy theo bảng hiển thị trên màn (srs-fr-03-dao-tao.md:1786-1796, có "Người tạo" và "Ngày tạo"), hay theo mục "Outputs — Danh sách" của FR-III-14 (srs-fr-03-dao-tao.md:1189-1200, không có hai cột này)? Đề nghị bổ sung một bảng "Outputs — Tệp Xuất Excel" vào FR-III-14, theo đúng cách đặc tả đã làm ở FR-III-05 (srs-fr-03-dao-tao.md:609-625).

2. Nếu chốt theo bảng trên màn: cột "Số chương trình" (srs-fr-03-dao-tao.md:1793) có phải nằm trong tệp xuất không? Hiện tệp xuất cũng không có cột này, nên câu trả lời sẽ quyết định phạm vi cần chỉnh rộng hơn hai cột mà bên nghiệm thu nêu.

3. Cột "Mã KH" có trong tệp xuất thực tế nhưng không có trong cả hai bảng cột nói trên của đặc tả. Đây là cột được chấp nhận và cần bổ sung vào đặc tả, hay là cột thừa cần gỡ?

── Ghi chú chung ──

Không tạo, sửa hay xóa bản ghi nào trong quá trình đo; thao tác chỉ gồm chọn thẻ trạng thái, nhập hai ô ngày và bấm nút xuất. Nhật ký trình duyệt không ghi nhận lỗi nào. Mỗi lần bấm nút, hệ thống hiện đúng một thông báo "Xuất Excel thành công", không có hiện tượng thông báo lặp.

Chúng tôi không có ảnh hiện trạng trước khi sửa nên chỉ khẳng định được hiện trạng hiện nay so với đặc tả, không suy đoán về việc thao tác sửa nào đã tạo ra kết quả này. Kết quả trên chỉ có hiệu lực cho môi trường và bản dựng đã nêu tại thời điểm đo.

Hai tệp Excel đã tải về được giữ lại để đối chiếu: ke-hoach-dao-tao-1786046602595.xlsx (mã kiểm tra sha256 5cf082c473357c8b608bc8e62f3c246a4717fc9210f7494d8eefb1594b58bcae) và ke-hoach-dao-tao-1786046777916.xlsx (sha256 62e1eb2dbb8ee0dceadc874f2e09cce4c8d46b57c00c9894236270850bff8fad).

Ảnh bằng chứng:
- https://drive.google.com/file/d/1sAbSLkWYmRTV693XojhcvTIvDX3_Q8d2/view?usp=drivesdk (màn sau khi lọc Trạng thái "Đã duyệt": chân bảng "Hiển thị 1-4 / 4 kết quả", thẻ "Tất cả 14", nút "Xuất Excel" có mặt)
- https://drive.google.com/file/d/1ofW-UmqNK2SdSnu8qD6DcKDzejK_ikTx/view?usp=drivesdk (màn sau khi lọc Từ ngày 01/07/2026 – Đến ngày 31/07/2026: chân bảng "Hiển thị 1-1 / 1 kết quả")
- https://drive.google.com/file/d/1LTwZarKWmdDpMIhmGgCPJJwUiqI_It2F/view?usp=drivesdk (bảng trên màn đã cuộn sang phải, thấy rõ hai cột "Người tạo" và "Ngày tạo" có dữ liệu)
```

---

## Dòng 64 · `DGKQHTVV_01` — nội dung cũ

```
❌ CÒN LỖI — doanh nghiệp không thấy vụ việc của chính mình, nên không tới được chức năng đánh giá.

TÁI HIỆN
1) Đăng nhập tài khoản doanh nghiệp → mở danh sách vụ việc, không lọc.
2) Danh sách chỉ hiện 5 vụ việc, trong khi doanh nghiệp này sở hữu 7. Hai vụ việc bị thiếu là VV-BTP-TW-20260806-003 và -004 — đều ở "Đã đánh giá", đều do đơn vị TRUNG ƯƠNG xử lý.
3) Lọc "Hoàn thành" và lọc "Đã đánh giá" → đều rỗng. Dán thẳng địa chỉ 2 vụ việc đó → báo "Không tìm thấy vụ việc."
4) Cùng phiên đó, vụ việc do đơn vị ĐỊA PHƯƠNG xử lý vẫn mở bình thường.
⇒ QUY LUẬT: doanh nghiệp bị giấu vụ việc của chính mình khi vụ việc do đơn vị khác (Trung ương) xử lý.

VÌ SAO SAI
srs-fr-05-vu-viec.md:1793 — "DN chỉ thấy vụ việc của DN mình", chỉ chặn khi doanh nghiệp mở vụ việc KHÔNG phải của mình; :1792 gọi màn này là "hồ sơ của tôi". Phạm vi nhìn đang lọc theo ĐƠN VỊ XỬ LÝ, đúng ra phải lọc theo CHỦ SỞ HỮU (doanh nghiệp đã gửi vụ việc).

DEV SỬA
Danh sách + chi tiết vụ việc phía doanh nghiệp: lọc theo chủ sở hữu, bỏ điều kiện đơn vị xử lý. Không mở được bản ghi thì không có đường nào tới nút đánh giá — đây chính là triệu chứng phiếu báo ("không hiển thị nút chức năng").

✅ ĐANG ĐÚNG, ĐỪNG PHÁ: mở chi tiết không còn bị đẩy sang trang báo không có quyền · doanh nghiệp không thấy "Kết quả kiểm tra" và "Phân công xử lý" (:1805, :1806) — đúng đặc tả.

⏸ Chưa đo được thao tác nhập điểm vì lỗi trên chặn hết luồng. Sửa xong phạm vi nhìn phải đo tiếp mới chốt trọn phiếu.

KIỂM LẠI SAU FIX
1) Doanh nghiệp mở danh sách, không lọc → tổng phải bằng đúng số vụ việc nó sở hữu (đối chiếu bằng vai trò cán bộ Trung ương).
2) Bấm vụ việc do Trung ương xử lý → phải mở được; dán thẳng địa chỉ → cũng phải mở được.
3) Nhập đánh giá 9 · 8 · 10 + nhận xét có mốc giờ riêng → gửi → tải lại trang → đọc đúng nội dung vừa nhập.
4) Chứng âm: mở/đánh giá vụ việc của doanh nghiệp khác → phải bị từ chối.
✅ PASS: cả 4 bước đạt, điểm tổng bằng trung bình 3 điểm (:1220).
❌ FAIL: còn thiếu vụ việc · hoặc mở được mà không có đường vào đánh giá · hoặc gửi xong tải lại trang thì rỗng.
⚠️ Đừng chấm PASS chỉ vì trạng thái đổi sang "Đã đánh giá" hoặc có thông báo thành công — hai dấu hiệu này đã từng đúng trong khi lỗi còn nguyên.

ĐO: 07/08/2026 · env nội bộ 18.143.165.120.nip.io · bó mã index-BbPPdate.js · 1 doanh nghiệp / 7 vụ việc / 2 đường vào · đối chứng bằng 2 vai trò cán bộ để xác nhận 2 vụ việc kia có thật và đúng chủ sở hữu.

Lưu ý: ô "DEV phản hồi lần 1" của phiếu này đang TRỐNG — chưa có BA chốt nào cho case này, nên không có căn cứ BA để đổi verdict. Hai câu hỏi BA đã gửi 06/08 (cán bộ có được chấm khi vụ việc đã ở "Đã đánh giá"; đánh giá xong điểm TVV có cập nhật) đều KHÔNG phải căn cứ của verdict này và cũng đang bị chính lỗi trên chặn không đo được.
```

---

## Dòng 65 · `DGKQHTVV_02` — nội dung cũ

```
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
```

---

## Dòng 338 · `LBCKQTHCT_05` — nội dung cũ

```
⚠️ Cần BA xác nhận — khối Nhận xét, kiến nghị ĐÃ CÓ và dùng được, nhưng chỉ hiện sau khi cán bộ bấm [Lập báo cáo]; đặc tả chưa quy định màn phải hiện gì trước thời điểm đó.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả.

PHẦN ĐÃ ĐẠT — khối tồn tại và hoạt động đúng:
- Trên màn Chi tiết đợt báo cáo có thẻ "Nhận xét, kiến nghị", đặt ngay sau các thẻ biểu mẫu 21a/21b và trước nhóm nút hành động, đúng thứ tự đặc tả mô tả.
- Ô soạn nhiều dòng, giới hạn đúng 5.000 ký tự, có bộ đếm ký tự trên màn — khớp yêu cầu tại srs-fr-15-ct-htpldn.md:1169 ("Max 5000 ký tự").
- Nhập nội dung rồi bấm Lưu nháp: phát sinh đúng 1 lượt gọi lưu, không gửi trùng. Sau khi TẢI LẠI TRANG, nội dung đọc lại đúng từng chữ trên cả giao diện lẫn dữ liệu nguồn, nên không phải trường hợp "khối chỉ có vỏ, không lưu được".
- Kiểm lại trên 2 bản ghi độc lập, cả hai đều lưu và đọc lại được.

PHẦN CẦN BA QUYẾT — vì sao chưa chấm hết lỗi được:
Làm đúng 2 bước ghi trong phiếu (mở menu "Đợt báo cáo" rồi mở Chi tiết đợt báo cáo) trên một đợt mà đơn vị chưa bắt đầu lập báo cáo, thì màn Chi tiết CHỈ có thẻ Biểu mẫu 21a, KHÔNG có thẻ Nhận xét, kiến nghị, không có ô soạn nào và không có chữ "Nhận xét" ở bất kỳ đâu trong vùng nội dung. Khối chỉ xuất hiện sau khi bấm [Lập báo cáo]. Nghĩa là quan sát của đối tác không sai — chỉ là đo ở thời điểm trước khi bắt đầu lập.
Nhưng cũng chưa đủ căn cứ kết luận đây là lỗi: đặc tả tại :1169 đặt điều kiện hiển thị khối là "khi đợt ở trạng thái Đang lập BC", tức chỉ yêu cầu khối trong pha đang lập, và IM LẶNG về việc màn phải hiển thị gì ở các trạng thái còn lại. Không có dòng nào buộc phải hiện khối ở dạng chỉ đọc trước khi lập.

⚠️ CẦN BA CONFIRM:
(1) Khi đơn vị chưa vào pha lập báo cáo, màn Chi tiết đợt báo cáo có phải hiển thị khối "Nhận xét, kiến nghị" ở dạng chỉ đọc không, hay đúng là chỉ hiện khi bắt đầu lập? Đề nghị bổ sung điều kiện hiển thị cho các trạng thái còn lại vào dòng #39 của bảng thành phần màn hình.
(2) Đặc tả tách hai bậc trạng thái: trạng thái của ĐỢT (:1368, có giá trị "Đang lập BC") và trạng thái nộp của từng ĐƠN VỊ (:1389, có giá trị "Đang lập"). Điều kiện hiển thị ở dòng #39 chỉ nhắc trạng thái của ĐỢT, trong khi một đợt dùng chung cho nhiều chục đơn vị. Đề nghị BA chốt điều kiện hiển thị nên neo vào trạng thái nộp của ĐƠN VỊ hay trạng thái của ĐỢT. Hiện phần mềm đang neo vào ĐƠN VỊ.
Mục đích là bổ sung, làm rõ đặc tả màn hình, KHÔNG chặn bàn giao — chức năng nhập nhận xét đã dùng được bình thường.

Về bằng chứng gốc: file LBCKQTHCT_05.jpg và LBCKQTHCT_06.jpg là cùng một file ảnh (trùng mã băm), tức một ảnh đang dùng cho hai khiếu nại về hai khối khác nhau; ảnh lại chỉ bắt phần dưới trang nên không loại trừ được khả năng khối nằm phía trên. Vì vậy QA không dựa vào ảnh mà tự tái hiện đúng các bước phiếu mô tả để đo.
```

---

## Dòng 339 · `LBCKQTHCT_06` — nội dung cũ

```
⚠️ Cần BA xác nhận — khối truy vết "Chương trình HTPL liên quan trong kỳ" ĐÃ CÓ và dùng được, nhưng chỉ hiện sau khi cán bộ bấm [Lập báo cáo]; đặc tả không có dòng nào quy định khối này nên chưa đủ căn cứ chấm hết lỗi.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js (07/08/2026 02:23) — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab trước khi đo.
Tài khoản: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả.

PHẦN ĐÃ ĐẠT — khối tồn tại và hoạt động đúng:
- Trên màn Chi tiết đợt báo cáo, trong thẻ "Nhận xét, kiến nghị" có khối nhãn "Chương trình HTPL liên quan trong kỳ", kèm dòng mô tả "Tùy chọn — dùng để truy vết các chương trình đơn vị đã triển khai trong kỳ báo cáo" — gần như nguyên văn yêu cầu tại srs-fr-15-ct-htpldn.md:732.
- Điều khiển đúng kiểu chọn nhiều giá trị có tìm kiếm, khớp mô tả "Multi-select" và cột Nguồn nhập ghi "Chọn" tại :732.
- Chọn được chương trình, bấm Lưu nháp, rồi TẢI LẠI TRANG: lựa chọn vẫn còn trên giao diện và dữ liệu nguồn lưu đúng mã chương trình đã chọn. Hai đường đo khớp nhau, nên không phải trường hợp "khối chỉ có vỏ".

Một chi tiết cần nói rõ để không hiểu nhầm: lượt quét đầu tiên, ô chọn mở ra nhưng hiện "Trống". Đã kiểm và xác định đây KHÔNG phải lỗi: giao diện gọi đúng địa chỉ lấy danh sách chương trình và nhận phản hồi thành công với 0 bản ghi, vì toàn bộ 14 chương trình đang có trên môi trường đều thuộc đơn vị Cục Bổ trợ tư pháp (Trung ương), còn đơn vị đang đo (Sở Tư pháp Hà Nội) chưa sở hữu chương trình nào. Đúng theo :732 thì khối này chỉ liệt kê chương trình của chính đơn vị, nên danh sách rỗng là phân quyền dữ liệu đúng. Để kiểm được trọn vẹn, QA đã tạo một chương trình thử cho Sở Tư pháp Hà Nội (mã CT-20260807-0001) — đây là dữ liệu QA dựng để kiểm thử, có thể xóa sau khi đối tác đọc xong kết quả. Sau khi có dữ liệu, khối hoạt động đầy đủ như mô tả ở trên.

PHẦN CẦN BA QUYẾT — vì sao chưa chấm hết lỗi được:
Làm đúng 2 bước ghi trong phiếu (mở menu "Đợt báo cáo" rồi mở Chi tiết đợt báo cáo) trên đợt mà đơn vị chưa bắt đầu lập báo cáo, thì màn chỉ có thẻ Biểu mẫu 21a; thẻ "Nhận xét, kiến nghị" không hiện, mà khối truy vết lại nằm bên trong thẻ đó nên cũng không hiện. Nghĩa là quan sát của đối tác không sai — chỉ là đo ở thời điểm trước khi bắt đầu lập.
Nhưng cũng chưa đủ căn cứ kết luận là lỗi: bảng thành phần màn hình của màn Chi tiết đợt báo cáo (:1163–1175, gồm 11 dòng) KHÔNG có dòng nào khai khối truy vết chương trình liên quan, nên đặc tả cũng không quy định nó phải là khối riêng, đặt ở đâu, hay hiện ở trạng thái nào. Yêu cầu về khối này hiện chỉ nằm ở phần dữ liệu đầu vào của chức năng Lập báo cáo (:732, :744, :745, :1417).

⚠️ CẦN BA CONFIRM (chung với phiếu LBCKQTHCT_05, chỉ cần trả lời một lần):
(1) Khi đơn vị chưa vào pha lập báo cáo, màn Chi tiết đợt báo cáo có phải hiển thị phần lập báo cáo — gồm khối "Nhận xét, kiến nghị" và khối "Chương trình HTPL liên quan" — ở dạng chỉ đọc không, hay đúng là chỉ hiện khi bắt đầu lập?
(2) Đề nghị bổ sung một dòng cho khối truy vết chương trình liên quan vào bảng thành phần màn hình Chi tiết đợt báo cáo (hiện dừng ở dòng #45), ghi rõ kiểu điều khiển, vị trí và điều kiện hiển thị, để các vòng sau có căn cứ chấm thay vì phải suy từ phần dữ liệu đầu vào.
(3) Khối này đang đặt lồng trong thẻ "Nhận xét, kiến nghị" — có đúng ý đồ thiết kế không, hay cần tách thành khối riêng?
Mục đích là bổ sung, làm rõ đặc tả màn hình, KHÔNG chặn bàn giao — chức năng truy vết đã dùng được bình thường.

Ghi nhận thêm, không thuộc phạm vi phiếu: danh sách đổ vào ô chọn hiện không lọc theo trạng thái chương trình (chương trình còn ở Dự thảo vẫn xuất hiện) và không lọc theo kỳ báo cáo. Đặc tả không quy định các bộ lọc này nên chỉ ghi nhận, có thể gộp vào câu hỏi (2) nếu BA muốn siết lại.

Về bằng chứng gốc: file LBCKQTHCT_06.jpg và LBCKQTHCT_05.jpg là cùng một file ảnh (trùng mã băm), tức một ảnh đang dùng cho hai khiếu nại về hai khối khác nhau; ảnh lại chỉ bắt phần dưới trang. Vì vậy QA không dựa vào ảnh mà tự tái hiện đúng các bước phiếu mô tả để đo.
```

---

## Dòng 342 · `GKQTHCTHTPL_01` — nội dung cũ

```
⚠️ Cần BA xác nhận — lỗi "Forbidden" ĐÃ HẾT và thao tác gửi lên Trung ương nay chạy trót lọt, 4/5 vế kỳ vọng đều đạt. Chỉ còn vế "chuyển trạng thái ĐỢT báo cáo" chưa chốt được, vì cùng một đợt lại hiện hai trạng thái khác nhau tùy vai trò người xem, mà đặc tả đang tự mâu thuẫn ở đúng chỗ này.

Đo ngày 07/08/2026 trên môi trường nội bộ 18.143.165.120.nip.io, bó mã giao diện index-D4Buvu4S.js — đã tải lại trang bằng địa chỉ và đọc lại tên bó mã ngay trong tab ở cả hai nhịp đo.
Tài khoản bấm gửi: cbnv_hn (Cán bộ Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đúng vai trò và đúng cấp theo đặc tả. Tiền đề phê duyệt kết quả do cbpd_hn (Cán bộ Phê duyệt CÙNG đơn vị, đã đối chiếu trùng mã đơn vị) thực hiện. Vế phía Trung ương đo bằng tài khoản cbnv_tw đăng nhập riêng, không dùng tài khoản quản trị. Đợt đo: DOT-SO_BO_NAM-2026-1, phạm vi 83 đơn vị.

PHẦN ĐÃ ĐẠT:
- Trước khi bấm, màn Chi tiết đợt đọc được "Đã duyệt kết quả" và có nút [Gửi lên TW]. Bấm nút → hộp xác nhận "Gửi báo cáo lên TW? Sau khi gửi, báo cáo của đơn vị sẽ chuyển sang trạng thái Đã nộp" → [Đồng ý]: thao tác thành công, KHÔNG còn thông báo "Forbidden".
- Hệ thống hiện thông báo nhanh đúng nguyên văn câu đối tác kỳ vọng: "Đã gửi báo cáo lên Trung ương". Đúng 1 thông báo cho 1 lần bấm, không hiện trùng.
- Ghi nhận thời điểm gửi: mốc gửi lưu lại là 07/08/2026 03:11:24 (giờ VN), lệch khoảng một phần mười giây so với lúc bấm xác nhận. Trên màn Chi tiết đợt (vai trò Trung ương) có bảng "Tiến độ nộp theo đơn vị", trong 83 dòng chỉ đúng một dòng "Đã nộp" — Sở Tư pháp Hà Nội, cấp DP, ngày nộp 07/08/2026.
- Vào danh sách tổng hợp của cấp Trung ương: đọc bằng chính phiên của cán bộ nghiệp vụ Trung ương, có dòng khớp đủ ba yếu tố mã đợt + tên đơn vị + ngày gửi.
- Thông báo cho cán bộ nghiệp vụ Trung ương: có, trùng mốc giờ, tiêu đề "Đơn vị đã nộp BC đợt DOT-SO_BO_NAM-2026-1 lên TW".
- Lưu vết thao tác: nhật ký hệ thống có mục ứng với lần gửi, đúng tài khoản cbnv_hn, đúng mốc giờ; bước phê duyệt tiền đề cũng được ghi đúng tài khoản cbpd_hn.
- Đo trạng thái hai nhịp theo yêu cầu: ngay sau thao tác và sau khi tải lại trang bằng địa chỉ — cả hai nhịp màn của đơn vị vừa gửi đều đọc được "Đã gửi TW", thanh tiến trình nhảy sang bước 5.

PHẦN CẦN BA QUYẾT — vì sao chưa chốt hết lỗi được:
Cùng một đợt DOT-SO_BO_NAM-2026-1, sau khi gửi thành công:
- Màn của cán bộ Địa phương (người vừa gửi) đọc: "Đã gửi TW".
- Màn của cán bộ Trung ương (bên nhận) đọc: "Tạo đợt" — cả ở danh sách đợt lẫn ở Chi tiết đợt. Tab lọc "Đã gửi TW" trong danh sách đợt của Trung ương đang rỗng, không có đợt vừa gửi.
Dữ liệu nguồn cho thấy trạng thái, dấu đã-gửi và thời điểm gửi đều được ghi ở bản ghi THEO TỪNG ĐƠN VỊ, còn bản ghi ĐỢT thì không đổi.
Đặc tả đang tự mâu thuẫn đúng ở chỗ này: :937 (chức năng gửi TW) yêu cầu chuyển trạng thái ĐỢT sang "Đã gửi TW", đánh dấu đã gửi và ghi thời điểm gửi; nhưng :938 ngay sau đó lại quy định chính ba việc ấy ở cấp ĐƠN VỊ; trong khi :1368 chỉ cho mỗi đợt MỘT giá trị trạng thái, mà một đợt lại dùng chung cho 83 đơn vị (:621, :646, :1398). Ba dòng này không thể cùng đúng khi các đơn vị đang ở những bước khác nhau. Vì đặc tả mâu thuẫn, QA không được phép tự chọn bên nào là đúng, nên không chốt Pass và cũng không mở lại lỗi cho vế này.

⚠️ CẦN BA CONFIRM:
(1) Trạng thái mà người dùng nhìn thấy ở màn Chi tiết đợt phải là trạng thái CỦA ĐƠN VỊ MÌNH hay trạng thái chung CỦA ĐỢT? Hiện phần mềm đang cho cán bộ Địa phương thấy trạng thái của đơn vị, còn cán bộ Trung ương thấy trạng thái của đợt — nên hai vai trò đọc ra hai kết quả khác nhau cho cùng một đợt.
(2) Nếu chốt theo trục ĐƠN VỊ, đề nghị phát biểu lại :937 cho khớp :938 (bỏ phần chuyển trạng thái đợt), đồng thời làm rõ khi nào thì trạng thái chung của ĐỢT mới đổi — vì hiện tại đợt đứng nguyên ở "Tạo đợt" suốt cả vòng đời, kể cả khi đã có đơn vị nộp xong.
(3) Bộ lọc "Đã gửi TW" ở danh sách đợt của Trung ương nên hiểu thế nào: liệt kê đợt có ít nhất một đơn vị đã gửi, hay chỉ đợt mà toàn bộ đơn vị đã gửi?
Mục đích là làm rõ mô hình trạng thái trong đặc tả, KHÔNG chặn bàn giao — chức năng gửi lên Trung ương đã dùng được bình thường và đầy đủ.

Ghi nhận thêm, KHÔNG thuộc phạm vi phiếu và không ảnh hưởng kết luận:
- Đã truy được nguồn của chữ "Forbidden" mà phiếu mô tả: nếu dùng tài khoản CẤP TRUNG ƯƠNG để gọi chức năng gửi lên Trung ương thì hệ thống chặn với đúng chữ "Forbidden". Việc chặn là ĐÚNG đặc tả (:918, :922 quy định chỉ cán bộ nghiệp vụ Bộ/Ngành hoặc Địa phương mới được gửi), nên đây không phải lỗi. Tuy nhiên thông điệp trả về là chuỗi tiếng Anh thô kèm mã quyền chung, không phải thông điệp tiếng Việt mà đặc tả đã khai sẵn cho chức năng này (:962 "Đợt BC chưa được phê duyệt kết quả" và :963 "Chỉ đơn vị BN/ĐP mới gửi BC lên TW"). Đề nghị dev gắn đúng thông điệp đã đặc tả để người dùng hiểu vì sao bị chặn.
- Thông báo gửi cho cán bộ Trung ương chỉ nêu mã đợt, không nêu tên đơn vị đã nộp; đặc tả không quy định nội dung nên chỉ nêu để BA cân nhắc, vì một đợt có tới 83 đơn vị.
- Một lần gửi sinh 2 mục nhật ký cùng mốc giờ; đặc tả không quy định số mục nên chỉ ghi nhận.

Lưu ý về dữ liệu: bước phê duyệt kết quả là tiền đề do QA dựng để đo được phiếu này; đợt DOT-SO_BO_NAM-2026-1 hiện đang ở trạng thái đã nộp lên Trung ương do QA thao tác chứ không phải người dùng thật, có thể đưa về trạng thái cũ sau khi đối tác đọc xong. QA chủ động KHÔNG bấm nút [Tổng hợp] ở màn Trung ương vì đó là chức năng khác, ngoài phạm vi phiếu.
```
