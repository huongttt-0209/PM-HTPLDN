# Báo cáo audit 17 bug có `Trạng thái dev fix = BA confirm`

**Ngày đối chiếu:** 08/08/2026  
**Nguồn bug:** Google Sheet, tab `gid=1714340219`, bản CSV tải trực tiếp tại thời điểm audit  
**Nguồn BA:** 03 file phản hồi được cung cấp trong thư mục `BA-phan-hoi`  
**Nguồn đặc tả:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5`

## 1. Kết quả tổng quan

- Sheet có **378 dòng dữ liệu**; lọc chính xác cột `Trạng thái dev fix` thu được **17 bug = BA confirm**.
- Nếu chỉ công nhận phản hồi chính thức có **đúng mã bug** trong 03 file BA: **1/17** bug đã được BA phản hồi trực tiếp — `QLHDTVVCG_15` — nhưng phần tệp đính kèm vẫn chưa được đặc tả đủ.
- Có thêm **1 bug được trả lời gián tiếp nhưng đủ căn cứ áp dụng**: `QLDX_03`, vì BA đã chốt cùng cơ chế timeout 25/30 phút tại cụm `QLDX_04/05/06`.
- Có **1 bug chỉ có phản hồi BA không chính thức trong chính ô sheet**: `DKTGMLTVV_13` (tên nút), nhưng phản hồi này xung đột SRS hiện tại và chưa trả lời 03 điểm đang chờ.
- Có **1 bug chỉ được nhắc là lỗi chặn/chuyển lô sau, chưa có quyết định nghiệp vụ**: `GKQTHCTHTPL_01`.
- **13/17 bug còn lại không có phản hồi BA** trong 03 file đã cung cấp.
- Không nên chấp nhận toàn bộ 17 bug chỉ theo nhãn `BA confirm`: SRS chỉ đủ rõ để xử lý ngay `QLDX_03`; các bug còn lại có điểm thiếu, mâu thuẫn, hoặc kỳ vọng gốc không khớp đặc tả chi tiết.

## 2. Ma trận đối chiếu

| # | Mã bug | BA đã phản hồi? | Đối chiếu SRS với bug gốc | Kết luận xử lý |
|---:|---|---|---|---|
| 1 | `QLLKHDTBD_09` | Chưa | SRS có yêu cầu xuất theo bộ lọc hiện tại. Tuy nhiên SRS không chốt rõ bộ cột file xuất; danh sách màn hình có `Người tạo`, `Ngày tạo` nhưng phần Output lại thiếu. | Bug gốc về **bộ lọc** là đúng; yêu cầu bổ sung 2 cột cần BA/SRS chốt. |
| 2 | `QLTVV_02` | Chưa | SRS quy định 20 dòng/trang và có điều kiện lọc ngày công nhận, nhưng không quy định thứ tự mặc định theo ngày công nhận mới nhất hoặc cách xếp bản ghi không có ngày. | Chấp nhận phần phân trang; chưa đủ căn cứ chấp nhận kỳ vọng sắp xếp. |
| 3 | `DKTGMLTVV_13` | Một phần trong sheet; không có trong 03 file BA | SRS hiện tại cho NHT đăng ký hồ sơ loại **TVV/CG**, nút **Lưu**, tạo trạng thái `Mới đăng ký`, có thông báo/audit; quy tắc chung sau tạo mới quay về danh sách. SRS không bắt buộc toast chứa mã. | Kỳ vọng gốc sai ở loại hồ sơ `Người hỗ trợ`, tên nút `Gửi đăng ký` và điều hướng sang tiến trình; toast chứa mã chưa được quy định. |
| 4 | `DGKQHTVV_01` | Chưa | FR chi tiết cho DNNVV xem và đánh giá vụ việc của chính DN theo `doanh_nghiep_id`; quy tắc phân quyền nền lại lọc theo `don_vi_id` + DN và còn ghi chờ CĐT. | Bug thiếu quyền/nút là có căn cứ theo FR, nhưng SRS đang tự mâu thuẫn về tenant scope; BA phải chốt trước khi sửa. |
| 5 | `DGKQHTVV_02` | Chưa | Bảng màn hình, mô hình dữ liệu và quy tắc UI không đồng nhất về nhãn, người đánh giá, ngày đánh giá. Không có quy tắc làm tròn điểm và overflow cho khối chi tiết. | Chưa đủ SRS để kết luận các điểm UI hiện còn tranh chấp. |
| 6 | `QLDMTCTV_12` | Chưa | SRS chỉ cho CB nghiệp vụ cùng đơn vị, đúng trạng thái mới thấy nút; quy định lý do tối thiểu 10 ký tự nhưng không có tối đa 5.000. | Ảnh bug gốc dùng sai role/đơn vị nên kết luận “thiếu nút” không hợp lệ; giới hạn tối đa cần BA chốt. |
| 7 | `QLCHTHXLHS_02` | Chưa | FR-10 chi tiết đã bỏ tab `Quy trình hỗ trợ` và `Phân công mặc định`, chỉ còn 3 tab đúng như app. Nhưng mục tổng quan SRS vẫn ghi 4 nhóm cấu hình cũ. | Kỳ vọng bug gốc đã lỗi thời; sửa phần tổng quan SRS để đồng bộ FR chi tiết, không sửa app theo kỳ vọng 4 tab. |
| 8 | `QLDX_03` | **Có, gián tiếp** qua cụm `QLDX_04/05/06` | SRS quy định cảnh báo ở phút 25, tự đăng xuất ở phút 30; hết phiên phải là thông báo hết hạn, không phải đăng xuất thành công. | Bug gốc đúng. Dev sửa modal phút 25 và phân biệt `Phiên hết hạn`; áp dụng cho mọi phiên kể cả “Ghi nhớ đăng nhập”. |
| 9 | `QLNDTVVCG_38` | Chưa; file 7 điểm chỉ chốt loại người được phân công | SRS có chức năng phân công hàng loạt nhưng không nói một chuyên gia chung cho mọi hồ sơ hay chọn theo từng hồ sơ; cũng không mô tả xử lý khác lĩnh vực. | Cần BA chốt semantics của batch trước khi đóng bug. |
| 10 | `QLHSPLDN_15` | Chưa | SRS có luồng xuất Excel nhưng không quy định hành vi khi tập dữ liệu xuất rỗng. | Câu `Không có dữ liệu để xuất` đang là kỳ vọng ngoài SRS; bổ sung đặc tả hoặc sửa TC. |
| 11 | `QLTLPLCVV_22` | Chưa | Processing có yêu cầu tìm theo tên/mô tả và hỗ trợ `unaccent`; bảng màn hình lại không mô tả ô tìm kiếm, AC cũng thiếu. | Bug tìm có dấu có căn cứ ở xử lý, nhưng SRS màn hình/AC cần bổ sung. |
| 12 | `QLTLPLCVV_23` | Chưa | Dòng xử lý có `unaccent`, nhưng mapping business rule không gắn đầy đủ vào FR này và bảng màn hình thiếu điều khiển tìm kiếm. | Bug tìm không dấu có căn cứ một phần; đồng bộ BR, màn hình và AC trước khi đóng. |
| 13 | `QLHDTVVCG_15` | **Có, trực tiếp nhưng chưa đủ** | BA đã chốt toast `Đã lưu hợp đồng` và quay về đúng ngữ cảnh mở form; SRS đã cập nhật. Mã, trạng thái và dữ liệu con chính có căn cứ. Tệp đính kèm có trên form nhưng chưa được mô tả rõ trong processing/output là lưu cùng giao dịch tạo hợp đồng. | Có thể xử lý theo BA cho toast/điều hướng; vẫn cần chốt/làm rõ tệp đính kèm khi tạo mới. |
| 14 | `LBCKQTHCT_01` | Chưa | SRS cho BN/ĐP đúng phạm vi lập báo cáo, lưu nháp, đổi trạng thái đơn vị `DANG_LAP` và ghi audit. Không quy định toast thành công. | Lỗi 403 gốc là bug nếu chạy đúng vai trò/phạm vi; câu toast cần BA chốt. |
| 15 | `LBCKQTHCT_05` | Chưa | SRS chỉ hiển thị nhận xét khi trạng thái **toàn đợt** là `DANG_LAP_BC`, trong khi dữ liệu còn theo dõi trạng thái **từng đơn vị** và một đợt dùng cho khoảng 70 đơn vị. | Mô hình trạng thái mâu thuẫn; BA/SA phải chốt điều kiện hiển thị theo đợt hay theo đơn vị. |
| 16 | `LBCKQTHCT_06` | Chưa | Input, processing và entity có danh sách chương trình liên quan, nhưng bảng đặc tả màn hình không có khối này và không nêu điều kiện hiển thị. | Chức năng có căn cứ, nhưng SRS UI chưa đủ; bổ sung màn hình/visibility rule. |
| 17 | `GKQTHCTHTPL_01` | Chỉ được nhắc, **chưa phản hồi** | SRS cho BN/ĐP gửi TW, đồng thời đổi trạng thái toàn đợt `DA_GUI_TW` và trạng thái đơn vị `DA_NOP`. Một đợt dùng chung nhiều đơn vị nên hai mức trạng thái này xung đột khi đơn vị đầu tiên gửi. | Chưa được phép đóng theo SRS hiện tại; cần BA/SA chốt state machine và xác nhận role của lần test `Forbidden`. |

## 3. Các điểm BA/SA cần chốt ưu tiên

1. `DGKQHTVV_01`: quyền DNNVV theo `doanh_nghiep_id` hay bắt buộc đồng thời theo `don_vi_id` của đơn vị xử lý?
2. `GKQTHCTHTPL_01` và `LBCKQTHCT_05`: trạng thái báo cáo là trạng thái toàn đợt hay trạng thái từng đơn vị? Không được đổi toàn đợt sang `DA_GUI_TW` khi mới một đơn vị gửi nếu các đơn vị khác vẫn đang lập.
3. `QLNDTVVCG_38`: batch dùng một chuyên gia chung hay mapping riêng từng hồ sơ; hồ sơ khác lĩnh vực thì chặn cả lô hay xử lý từng dòng?
4. `DGKQHTVV_02`: chốt bộ trường UI, nhãn hiển thị, overflow và quy tắc làm tròn/hiển thị điểm thập phân.
5. `QLLKHDTBD_09`: chốt chính xác các cột file Excel, đặc biệt `Người tạo`, `Ngày tạo`.
6. `QLHDTVVCG_15`: tệp đính kèm có phải được lưu cùng transaction tạo hợp đồng hay là bước upload riêng sau khi sinh ID?
7. `QLHSPLDN_15` và `LBCKQTHCT_01`: bổ sung chính xác nội dung toast/hành vi khi không có dữ liệu nếu đây là yêu cầu bắt buộc.

## 4. Căn cứ nổi bật

- `QLDX_03`: `srs-fr-10-quan-tri.md` mô tả modal cảnh báo phút 25 và tự đăng xuất phút 30; BA đã chốt cùng cơ chế tại phần **Vấn đề 10 — QLDX_04/05/06** của file tổng hợp.
- `QLHDTVVCG_15`: `srs-fr-14-hop-dong-tv.md` đã có `INF-HDTV-01 = "Đã lưu hợp đồng"` và điều hướng về ngữ cảnh đã mở form. Quyết định BA nằm tại **Vấn đề 4** của file tổng hợp.
- `QLCHTHXLHS_02`: `srs-fr-10-quan-tri.md` ghi rõ đã bỏ 2 tab và màn hình còn 3 tab; phần tổng quan trong `srs-v3.5.md` chưa được cập nhật theo thay đổi này.
- `GKQTHCTHTPL_01`: file BA tổng hợp chỉ ghi đây là lỗi `Forbidden` ngoài phạm vi, đề nghị chuyển lô sau; không có quyết định về phân quyền hoặc state model.

## 5. Khuyến nghị trạng thái

- Giữ `BA confirm`: 16 bug chưa có quyết định trực tiếp/đủ phạm vi.
- Có thể chuyển Dev xử lý ngay theo căn cứ đã chốt: `QLDX_03`.
- `QLHDTVVCG_15`: tách phần đã chốt (toast + điều hướng) để Dev xử lý; giữ riêng câu hỏi tệp đính kèm cho BA.
- Không yêu cầu Dev sửa app theo kỳ vọng 4 tab của `QLCHTHXLHS_02`; sửa/đồng bộ SRS tổng quan và TC.
- Không dùng nhãn `BA confirm` như bằng chứng rằng BA đã trả lời; cần gắn link/quyết định BA vào từng dòng trước khi chuyển trạng thái.
