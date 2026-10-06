# Phiếu phản hồi — 27 lỗi tranh chấp đặc tả (nhóm 2)

**Ngày lập:** 30/07/2026
**Phạm vi:** 27 test case đang ở trạng thái `Reopent`, dạng đội phát triển bác bỏ với lý do "phần mềm đúng đặc tả". **Phát sinh thêm 5 mã bị kéo theo** (`DKTGKH_07`→`_11`) do quyết định gỡ luồng nhập tay/import — tổng ảnh hưởng 32 mã.
**Sheet theo dõi:** `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c`, tab `UAT_TGPL Doanh Nghiệp` (`gid=799081340`)
**Quy trình áp dụng:** `docs/Reference/Fix bug KTĐL/QUY-TRINH-phan-tich-bug-nghiep-vu.md`
**Phân tích nguồn:** `docs/Bao-cao-doi-soat/phan-tich-nhom-2-tranh-chap-dac-ta-2026-07-29.md`
**Trạng thái phiếu:** ✅ **ĐÃ CHỐT TOÀN BỘ — 30/07/2026.** Đã ghi sheet theo mục *Tổng hợp cập nhật sheet*; SRS đã sửa xong. Trong ngày có **một quyết định bị đảo lại** (`DKTGKH_12` — từ *giữ* luồng import sang *gỡ*); phiếu ghi theo quyết định cuối.

---

## Ghi chú phương pháp

**Bản chấm chuẩn:** SRS gốc `.md` tại `_bmad-output/planning-artifacts/srs-v3.5/`. Chủ đầu tư đã chốt đây là bản gốc duy nhất; bản `.docx` bàn giao là bản dẫn xuất.

**Bản `.docx` đối tác dùng khi ghi nhận:**

| Tuần | Bản đối tác cầm | Cách đánh số mục |
|---|---|---|
| Tuần 2 | `7.BTP_CPLQG_S7_2025_PM_L4_PMHTPLDN.docx` | 4.5.x, mã `HTPLDN-0xx` |
| Tuần 3 | `HTPLDN-PTYC-CT-v2.0.docx`, bàn giao 10/07 qua nhóm Zalo | 4.7.x / 4.11.x |

**Vì sao phát sinh cả cụm tranh chấp này:** bản `.docx` được **vá dần từ bản v1.0** chứ không dựng lại từ `.md`. Quy trình vá chỉ *thêm/sửa* chỗ `.md` có, **không gỡ** nội dung v1.0 mà `.md` không có. Nên `.docx` đọng lại nhiều yêu cầu không có trong bản gốc. Đối chiếu bản v1.0 xác nhận toàn bộ điểm lệch đều có sẵn từ v1.0, không phát sinh khi tạo v2.0.

→ **Đơn vị kiểm thử ghi nhận đúng theo tài liệu được giao.** Cái sai nằm ở khâu đồng bộ tài liệu, không ở bên nào. Toàn bộ nhóm này là **Loại 4** theo quy trình.

**Kết quả phân loại:** 22 ca Loại 4A · 2 ca Loại 4B (`QLDMTCDGHTCP_06/_12` — chốt thống nhất nhãn ngày 30/07) · 2 ca Loại 1 (lỗi phần mềm) · 1 ca Loại 2 (`DKTGKH_12` — SRS tự nới phạm vi ngoài CSV baseline, **chốt gỡ luồng import ngày 30/07**). `CPCTHTTTG_03` nằm trong 22 ca 4A nhưng là ca lai, vừa 4A vừa có lỗi phần mềm.

> **Đính chính trong ngày 30/07:** quyết định đầu tiên cho `DKTGKH_12` là **giữ** luồng import. Sau khi tra CSV baseline (UC22/UC23 không có transaction nhập/import nào; toàn bộ file transaction chỉ UC98 là luồng nhập) thì **đảo lại thành gỡ**. Phiếu này đã ghi theo quyết định cuối. Xem mục `DKTGKH_12`.

**Gom cụm:** các mã cùng một lỗi gốc được phân tích chung một lần, nhưng **cập nhật sheet vẫn theo từng dòng**.

---

## Cụm 1 — Nút "Xóa bộ lọc" trên màn hình báo cáo (6 mã)

`SLHDVM_09` · `VVDTN_09` · `VVDHT_09` · `VVDHTHT_09` · `CLDTBDDDR_09` · `VVTTG_08`

**(1) Phần mềm đúng SRS `.md` chưa?** ĐÚNG. `srs-fr-11-bao-cao.md` **không xuất hiện "Xóa bộ lọc" lần nào**; thanh nút màn báo cáo chỉ gồm Làm mới, Xem báo cáo, Xuất Excel, Xuất PDF.

**(1b) Bản `.docx` đối tác cầm có nói khác không?** CÓ. Mục **4.11.1.2.3** liệt kê hai nút tách bạch — mục 5 "Làm mới" (giữ nguyên điều kiện lọc) và mục 6 "Xóa bộ lọc" (đặt lại về mặc định). Mô tả nút 6 trùng từng chữ với Kết quả mong đợi.

**(2) Đối tác yêu cầu khác gì?** Đòi có nút "Xóa bộ lọc" riêng — đúng theo `.docx` họ cầm.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Không chặn luồng. Người dùng vẫn lọc và xem báo cáo được.

**Phân định hướng:** `.md` có dùng "Xóa bộ lọc" ở 8 nhóm FR khác nhưng thiếu ở `srs-fr-11`. Tín hiệu nghi **bị sót**, nhưng tra tiếp cây trọng tài: không có quyết định BA/CHANGELOG nào yêu cầu nút này cho màn báo cáo; ERD/§Outputs không liên quan; CSV UC không quy định thành phần giao diện. → Chốt **hướng A**.

**→ Kết luận: Loại 4A — phần mềm đúng bản gốc, bản `.docx` bàn giao mô tả thừa. Dev action: Không. Doc action: cập nhật `.docx` ở bản kế tiếp (bên soạn tài liệu bàn giao). Sheet: Resolve.**

**Phản hồi gửi đối tác:** *"Xác nhận bản SRS docx đang outdate. Sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần."*

---

## Cụm 2 — Bố cục và cột màn hình Chi tiết doanh nghiệp (5 mã)

`QLDNDHTPL_23` · `QLDNDHTPL_24` · `QLDNDHTPL_25` · `QLDNDHTPL_27` · `QLDNDHTPL_28`

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG. `srs-fr-07-doanh-nghiep.md` liệt kê trường màn Chi tiết theo **danh sách phẳng** ở vùng nội dung (dòng 481–484), **không có khái niệm "Nhóm"**, **không có mục "Chỉ số tổng hợp"**. Tab Lịch sử hỗ trợ chỉ ghi *"Read-only: 3 KPI + danh sách vụ việc"* (dòng 524), **không liệt kê cột**.

**(1b) Bản `.docx` nói khác không?** CÓ. Mục **4.7.1.3.2** chia **8 Nhóm** đánh số, trong đó Nhóm 2 "Người đại diện" là nhóm riêng, Nhóm 5 "Chỉ số tổng hợp" tồn tại nguyên văn, và Nhóm 6 liệt kê đủ 6 cột gồm *Lĩnh vực* và *Tư vấn viên*.

**(2) Đối tác yêu cầu khác gì?** Đòi hiển thị theo bố cục Nhóm, có Nhóm 5, và đủ cột ở tab Lịch sử hỗ trợ.

**(3) Có bắt buộc không?** Không. Các trường dữ liệu đều đã hiển thị đủ; khác nhau ở cách gom nhóm và số cột phụ.

**Phân định hướng:** `.md` không dùng bố cục "Nhóm" ở bất kỳ màn nào của FR-07, cũng không có "Chỉ số tổng hợp". Không tầng nào của cây trọng tài yêu cầu bổ sung. → **Hướng A**.

**→ Kết luận: Loại 4A. Dev action: Không. Doc action: cập nhật `.docx`. Sheet: Resolve.**

**Phản hồi:** câu chuẩn hướng A.

> **Ghi chú nội bộ — lá bài dự phòng cho Nhóm 6.** Nhóm 6 là thẻ *Lịch sử hỗ trợ*. Ngay dưới bảng liệt kê 6 cột, chính bản `.docx` có kèm dòng *"Ghi chú nguồn: SRS mô tả thẻ Lịch sử hỗ trợ ở mức tổng quát"* — tức người soạn tài liệu bàn giao **đã tự đánh dấu** rằng SRS chỉ nói chung chung, danh sách cột chi tiết là họ soạn thêm chứ không lấy từ `.md`.
>
> Dùng khi nào: nếu đối tác phản biện *"tài liệu ghi rõ 6 cột mà"*, chỉ vào đúng dòng ghi chú đó. Không đưa vào phản hồi gửi ra — chỉ nêu khi bị hỏi lại.

---

## Cụm 3 — Thông báo khi tìm kiếm không có kết quả (2 mã)

`QLTKND_06` (quản lý tài khoản) · `QLDMCQDVQL_05` (danh mục cơ quan, đơn vị)

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG. `srs-fr-10-quan-tri.md` không quy định câu thông báo cho hai màn này. Dòng "Không tìm thấy" duy nhất trong file thuộc lỗi xác thực VNeID, khác ngữ cảnh.

**(1b) Bản `.docx` nói khác không?** CÓ. Mục **4.10.3.2.3** Trường hợp 2: *"để trống vùng kết quả và hiển thị thông báo «Không tìm thấy tài khoản phù hợp»"*. Mục **4.10.1.2.3** Trường hợp 2: *"…«Không tìm thấy mục danh mục phù hợp»"*.

**(2) Đối tác yêu cầu khác gì?** Đòi hiển thị đúng câu thông báo đó thay vì chữ "Trống".

**(3) Có bắt buộc không?** Không chặn luồng, nhưng ảnh hưởng trải nghiệm.

**Phân định hướng:** `.md` có mẫu câu tương tự ở 13 file FR khác, thiếu đúng ở `srs-fr-10`. Tín hiệu nghi bị sót; tra cây trọng tài không có tầng nào chốt. → **Hướng A** cho đợt này, đồng thời **đưa vào danh sách rà `.md` có bị sót không** (việc riêng, không chặn phiếu).

**→ Kết luận: Loại 4A. Dev action: Không. Doc action: cập nhật `.docx`. Sheet: Resolve.**

**Phản hồi:** câu chuẩn hướng A.

---

## Cụm 4 — Nhãn trường trên danh mục Tiêu chí đánh giá hỗ trợ chi phí (2 mã) — **hướng B**

`QLDMTCDGHTCP_06` · `QLDMTCDGHTCP_12`

**(1) Phần mềm đúng `.md` chưa?** ĐÚNG một phần cần nói rõ: `srs-fr-10-quan-tri.md` dòng 1656 quy định **tên cột bảng danh sách** là *"Mức hỗ trợ (%)"* và *"Trần hỗ trợ/năm (VNĐ)"*, **không ràng buộc nhãn trên cửa sổ nhập liệu**.

**(1b) Bản `.docx` nói khác không?** CÓ. Mục **4.10.1.3.2** — mục mô tả màn chi tiết/nhập liệu — đặt tên trường là *"Mức hỗ trợ (%)"*, trong khi phần mềm hiển thị *"Tỷ lệ phần trăm"* / *"Mức chi phí tối đa"*.

**(2) Đối tác yêu cầu khác gì?** Đòi nhãn cửa sổ nhập liệu khớp tài liệu.

**(3) Có bắt buộc không?** Đơn vị kiểm thử lập luận nhãn sai dẫn tới **nhập sai dữ liệu định mức chi trả** — đây là lập luận nghiệp vụ có cơ sở, không chỉ là trải nghiệm.

**Lưu ý khi đọc:** hai test case này chấm **cửa sổ Thêm mới / Sửa**, không chấm bảng danh sách (bước kiểm thử: Quản trị hệ thống → chọn loại danh mục → Thêm mới / Sửa; kết quả thực tế: *"Tên trường thông tin «Tỷ lệ phần trăm», «Mức chi phí tối đa» không giống với thiết kế"*).

| Chỗ | Nhãn phần mềm | `.md` quy định |
|---|---|---|
| Bảng danh sách | — | dòng 1656: *"Mức hỗ trợ (%)"*, *"Trần hỗ trợ/năm (VNĐ)"* |
| Cửa sổ Thêm mới / Sửa | *"Tỷ lệ phần trăm"*, *"Mức chi phí tối đa"* | **không quy định** |

Cùng một trường đang có **hai cách gọi ở hai chỗ**, rủi ro nhập sai định mức chi trả là có thật, và lập luận nghiệp vụ của đơn vị kiểm thử đứng vững.

**→ Quyết định chốt 30/07/2026: thống nhất nhãn cửa sổ Thêm mới / Sửa theo tên cột bảng.** `.md` bị sót phần quy định nhãn cửa sổ nhập liệu → bổ sung `.md`, rồi phần mềm sửa theo.

| # | Việc | Nguồn / nơi sửa | Người làm |
|---|---|---|---|
| 1 | Bổ sung `srs-fr-10-quan-tri.md` — quy định nhãn trường trên cửa sổ Thêm mới / Sửa trùng tên cột bảng: *"Mức hỗ trợ (%)"*, *"Trần hỗ trợ/năm (VNĐ)"*. Đồng thời quyết trường *"Danh mục cha"* — cùng hai test case ghi nhận *"màn hình có trường «Danh mục cha» nhưng tài liệu SRS không có"* | `srs-fr-10` (cạnh dòng 1656) | BA |
| 2 | Đổi nhãn cửa sổ Thêm mới và Sửa: *"Tỷ lệ phần trăm"* → *"Mức hỗ trợ (%)"*, *"Mức chi phí tối đa"* → *"Trần hỗ trợ/năm (VNĐ)"* | Phần mềm | Dev |
| 3 | Cập nhật `.docx` mục 4.10.1.3.2 theo `.md` mới | `HTPLDN-PTYC-CT` | BA |

**→ Kết luận: Loại 4B. Dev action: Có. Doc action: bổ sung `.md` trước, rồi cập nhật `.docx`. Sheet: giữ `Reopent`.**

**Tình trạng 30/07/2026:** việc số 1 **đã xong** — `srs-fr-10-quan-tri.md` đã bổ sung cột *Nhãn hiển thị* ở Inputs FR-VIII-12, thêm 3 dòng đặc tả cửa sổ Thêm mới/Sửa ở SCR-VIII-01 kèm quy tắc nhãn cửa sổ phải trùng tên cột bảng. Trường **"Danh mục cha" đã xử lý xong, không cần BA quyết** — tra ra `DANH_MUC.danh_muc_cha_id` vốn đã có sẵn ở `srs-v3.5.md` §3.4.3.39 trường 7, nên phần mềm hiển thị là đúng mô hình dữ liệu, chỉ đặc tả màn hình bị sót; đã bổ sung dòng modal tương ứng. Còn lại việc số 2 (Dev đổi nhãn) và số 3 (cập nhật `.docx`).

**Phản hồi:** không gửi. Đây là ca chấp nhận sửa toàn bộ, không có phần nào từ chối.

---

## Các ca lẻ hướng A

Mọi ca dưới đây: **Loại 4A · Dev action Không · Doc action cập nhật `.docx` · Sheet Resolve · Phản hồi câu chuẩn hướng A.**

**(2) và (3) giống nhau ở cả 8 ca**, nên nêu chung một lần thay vì lặp:
- **(2) Đối tác yêu cầu khác gì:** đòi đúng nội dung mô tả trong bản `.docx` họ được giao. Không đòi thêm gì ngoài tài liệu.
- **(3) Có bắt buộc cho luồng nghiệp vụ không:** Không. Dữ liệu và thao tác nghiệp vụ vẫn thực hiện được đầy đủ; khác nhau ở thành phần giao diện, nhãn hiển thị hoặc cách gom nhóm.

| Mã | Bản `.docx` đối chiếu | (1) `.md` quy định gì | (1b) `.docx` quy định gì |
|---|---|---|---|
| `QLDNDHTPL_17` | v2.0 · 10/07 · Zalo | `srs-fr-07` chỉ có *"Sắp xếp mặc định: ngày cập nhật mới nhất trước"* | Mục **4.7.1.2.3** mục 6 *"Sắp xếp theo cột"* — bấm tiêu đề, luân phiên tăng/giảm |
| `QLNHCH_02` | tuần 2 · `7.BTP_CPLQG_S7…` | `srs-fr-03` không có thẻ thống kê tổng quan cho Ngân hàng câu hỏi | Mục **4.3.9.2.2** có mục *"Thẻ thống kê tổng quan"* |
| `QLNHCH_04` | tuần 2 · `7.BTP_CPLQG_S7…` | `srs-v3.5.md` §3.4.3.21 trường 9: `trang_thai — CHECK IN ('KICH_HOAT','VO_HIEU_HOA')` — **đúng y phần mềm đang làm** | Mục **4.3.9.2.2**: *"3 giá trị: Nháp, Công khai, Ẩn"* |
| `QLDXDTTH_09` | tuần 2 · `7.BTP_CPLQG_S7…` | `srs-fr-03` không quy định gửi thông báo cho người gửi khi cán bộ tiếp nhận đề xuất | Mục **4.3.13.2.2**: *"Cập nhật trạng thái «Mới» → «Đã tiếp nhận». Gửi thông báo cho người gửi"* |
| `VVTTG_02` | v2.0 · 10/07 · Zalo | `TPL-REPORT-FULL` bắt buộc `tong_ban_ghi` — *"Tổng số bản ghi"*, điều kiện *"Luôn"*, áp cho cả 23 báo cáo | Mục **4.11.2** ghi *"Không có chỉ số tổng hợp riêng"* cho loại báo cáo này |
| `CPCTHTTLHDN_04` | v2.0 · 10/07 · Zalo | `FR-IX-18` Dimensions gồm *Loại DN, Mức hỗ trợ, Số HS, Tổng chi phí, Trần so sánh* — đúng các nhóm phần mềm đang vẽ | Mục **4.11.5.2.2** mô tả hẹp hơn: *"Biểu đồ cột nhóm theo loại hình và mức hỗ trợ"* |
| `QLHSTVV_02` | tuần 2 · `7.BTP_CPLQG_S7…` | `SCR-IV-03` header card đúng **6 trường**: Ảnh · Họ tên · Mã TVV · Trạng thái · Điểm đánh giá TB · Ngày công nhận | Mục **4.4.11.2.2** liệt kê **9 trường**, thêm *Loại*, *Tổ chức tư vấn*, *Lĩnh vực pháp luật* |
| `PDHSTVV_06` | tuần 2 · `7.BTP_CPLQG_S7…` | `FR-IV-07`: *"Nếu PHE_DUYET: chuyển trạng thái **CHO_KICH_HOAT**"*. Nhật ký `.md` ngày **16/07/2026** ghi rõ đã chốt đúng điểm này cho chính mã `PDHSTVV_06` | Mục **4.4.6**: *"Chuyển hồ sơ sang trạng thái «Đang hoạt động»"* |

> **Lưu ý riêng `PDHSTVV_06`:** đội phát triển giải thích đúng cơ chế — *"Chờ kích hoạt tài khoản"* là trạng thái của **tài khoản đăng nhập** được hệ thống tự tạo sau phê duyệt, còn hồ sơ tư vấn viên có tập trạng thái riêng. Điểm này đã được chốt trong `.md` từ 16/07, tức trước đợt kiểm thử tuần 3.

---

## Ca lai — `CPCTHTTTG_03` (Báo cáo chi phí theo thời gian)

Ca này có **hai vấn đề tách rời**, phải xử lý riêng.

### Ý con 1 — biểu đồ vẽ hai đường (hướng A)

**(1)** `FR-IX-19` (UC142): `chart_type = LINE`, `trend_data[] = {ky_label, tong_chi_phi, so_ho_so}` — `.md` **không giới hạn số đường**.
**(1b)** Mục **4.11.5.2.2**: *"Biểu đồ đường thể hiện xu hướng chi phí"*; *Số hồ sơ* là **cột bảng tổng hợp**.
**(3)** Không bắt buộc.

→ **Hướng A** — phần mềm không trái `.md`.

### Ý con 2 — nhãn trục tung hỏng (LỖI PHẦN MỀM)

Ảnh minh chứng `CPCTHTTTG_03.jpg` cho thấy **cả 5 vạch chia trục tung đều hiển thị `000.000`**, không đọc được giá trị nào. Không văn bản nào quy định hay cho phép điều này.

Đây là **lỗi định dạng nhãn trục trong mã nguồn**, độc lập với tranh chấp đặc tả. Thêm nữa, vẽ chung một trục cho thang tiền (hàng trăm triệu) và thang đếm (25 hồ sơ) khiến đường số hồ sơ luôn bị nén sát đáy — cần trục phụ để biểu đồ dùng được.

**→ Kết luận: Case lai — ý con 1 là Loại 4A (không sửa), ý con 2 là lỗi phần mềm phải sửa. Dev action: CÓ (sửa nhãn trục + bổ sung trục phụ). Sheet: Giữ xử lý.**

**Phản hồi gửi đối tác** (vì có phần không sửa): *"Về nội dung biểu đồ: xác nhận bản SRS docx đang outdate, sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần. Về nhãn trục tung hiển thị không đọc được: ghi nhận là lỗi, sẽ khắc phục."*

---

## Hai ca hướng B (lỗi phần mềm) + một ca Loại 2 (gỡ chức năng)

Hai ca hướng B `TLCTCDG_11` và `TKDGHQHTPL_02` **không cần phản hồi gửi đối tác** — phần mềm sẽ được sửa theo đúng điều đối tác yêu cầu.

Ca `DKTGKH_12` khác hẳn: **có phản hồi**, vì kết quả là gỡ chức năng và đề nghị đối tác hủy test case — đó là phần không đáp ứng yêu cầu của họ.

### `TLCTCDG_11` — thiếu cảnh báo tổng trọng số

**(1)** SAI `.md`. `srs-fr-08-danh-gia.md` dòng 201: *"Kiểm tra tổng trọng số = 100% cho toàn đợt (**cảnh báo nếu khác, cho phép lưu**)"*. Hệ thống chỉ hiện thông báo thành công, không hiện cảnh báo.
**(1b)** `.docx` mục 4.8.2.2.3 nói **cùng nội dung** — hai bản khớp nhau, không có tranh chấp tài liệu.
**(2)** Đối tác đòi hệ thống hiện cảnh báo khi tổng trọng số khác 100% — **không khác đặc tả**, đây là yêu cầu đúng theo cả hai bản.
**(3)** Bắt buộc: thiếu cảnh báo thì cán bộ trình duyệt bộ tiêu chí chưa đủ 100% mà không biết.

> Đội phát triển trả lời đúng quy tắc nghiệp vụ nhưng **lệch trọng tâm** — điều đơn vị kiểm thử ghi nhận là hệ thống *không hiện cảnh báo*, không phải chuyện có chặn lưu hay không.

**→ Kết luận: Loại 1 — phần mềm sai đặc tả, Dev bổ sung cảnh báo khi tổng trọng số khác 100%. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi.**

### `TKDGHQHTPL_02` — điểm đánh giá vượt thang 0–100

**(1)** SAI `.md`. `srs-fr-01-dashboard.md` quy định thang **0–100** ở ba chỗ: dòng 416 (*"biểu đồ cột, thang 0-100 theo `KET_QUA_DANH_GIA.diem_tong` — ràng buộc 0-100"*), dòng 450, dòng 823 (*"Phạm vi giá trị trục Y: 0-100"*). Kiểm thử lượt 2 ghi nhận **số liệu vượt quá 100**.
**(1b)** Đội phát triển viện dẫn *"SRS hiện tại bản ngày 23/6"* — **chính là bản `.docx` v2.0** đơn vị kiểm thử đang dùng, không phải bản khác.
**(2)** Đối tác đòi điểm đánh giá nằm trong thang 0–100 — **không khác đặc tả**, đúng theo cả hai bản.
**(3)** Bắt buộc: điểm vượt thang làm sai số liệu đánh giá hiệu quả.

**→ Kết luận: Loại 1 — phần mềm sai đặc tả, Dev ràng buộc điểm tổng trong khoảng 0–100. Dev action: Có. Sheet: Giữ xử lý. Không phản hồi.**

### `DKTGKH_12` + `DKTGKH_07` — gỡ luồng nhập tay / import Excel danh sách đăng ký

**Quyết định chốt 30/07/2026: gỡ luồng theo CSV baseline.** Phần mềm phải bỏ chức năng, SRS phải bỏ mô tả, 6 test case bị hủy.

**(1) Phần mềm đúng `.md` chưa?** Đúng với FR-III-04 như đang viết — nhưng **chính FR-III-04 mới là chỗ sai**, vì nó tự thêm luồng ngoài baseline.

**(1b) Bản `.docx` đối tác cầm nói gì?** **Đã đúng sẵn.** Mục 4.3.4.2.1 ghi nguyên văn: *"Hệ thống tự gán «Chuyên trang» — Doanh nghiệp / Người hỗ trợ tự đăng ký qua chuyên trang Pháp luật quốc gia (theo UC23, đây là nguồn đăng ký duy nhất)"*. Mục 4.3.3 chỉ liệt kê Duyệt / Từ chối / Chọn khóa học. Tài liệu bàn giao **không phải sửa**.

**(2) Đối tác yêu cầu gì?** Có bản xem trước trước khi nạp tệp — dẫn từ điều khoản mục 4.5.5 / HTPLDN-024 vốn thuộc luồng nhập **kết quả học tập**, không phải luồng đăng ký. Đây là dẫn nhầm điều khoản.

**(3) Có bắt buộc không?** Không — vì chính chức năng nạp tệp bị gỡ.

**Căn cứ gỡ — CSV baseline là trọng tài:**

| Nguồn | Nội dung |
|---|---|
| CSV **UC22** *Quản lý đăng ký đào tạo* · tác nhân CB NV/CB PD | Đúng 4 transaction: xem danh sách · xem chi tiết · phê duyệt · từ chối. **Không có transaction tạo/nhập/import** |
| CSV **UC23** *Đăng ký tham gia học tập* · tác nhân DN/NHT | Đúng 4 transaction: xem danh sách khóa · xem chi tiết khóa · nhập thông tin đăng ký và gửi · hủy đăng ký. **Không có import** |
| Quét toàn bộ file transaction | 47 dòng nhắc Excel — **chỉ UC98 "Import biểu mẫu, hợp đồng" là luồng nhập**, có 4 transaction riêng. 46 dòng còn lại đều là *xuất*. Khi baseline muốn có import thì lập hẳn use case riêng; không có use case tương đương cho danh sách đăng ký |
| Thực thể `DANG_KY_DAO_TAO` §3.4.3.26 | **Không có trường `nguon_dang_ky`** → Input #7 của FR-III-04 là trường không tồn tại trong mô hình dữ liệu |

→ Luồng import ở FR-III-04 là **SRS tự nới phạm vi ngoài baseline**. Không phải "hai tầng chọi nhau chọn tầng nào cũng được".

**→ Kết luận: Loại 2 — sửa đặc tả cho khớp baseline, đồng thời phần mềm gỡ chức năng. Dev action: Có (gỡ). Sheet: `Reopent` cho tới khi gỡ xong.**

**Đã sửa SRS — 13 mục, hoàn tất 30/07/2026:**

| Nhóm | Tệp | Nội dung |
|---|---|---|
| A (5) | `srs-fr-03-dao-tao.md` | FR-III-04: bỏ *"3 cách…"* ở Mô tả · bỏ Input `nguon_dang_ky` · bỏ Processing bước 6 · bỏ Output `ket_qua_import` · giữ nguyên mệnh đề dòng 1683 |
| B (5) | `srs-v3.5.md` | `nguoi_dang_ky_id` N→Y · sửa lý do nullable của `HOC_VIEN.tai_khoan_id` · đồng bộ khối ERD `DANG_KY_DAO_TAO` · đổi quan hệ ERD sang `TAI_KHOAN` · sửa enum `'HUY'`→`'DA_HUY'` · sửa 2 dòng ma trận kiểm thử FR-III-03 và FR-III-04 |
| C (1) | `bpmn/fr-03-dao-tao/diagram-happy-path.drawio` | Node "6. Đăng ký tham gia" |
| D (3) | `srs-fr-03` header · `CHANGELOG-v3-to-v3.5.md` · `da-go-co-chu-dinh.md` | Nhật ký + sổ đã gỡ |

**Việc của Dev:** gỡ nút **Nhập thủ công** và **Tải lên tệp Excel** ở Tab Học viên màn Chi tiết khóa học. Lỗi *"Email không hợp lệ"* ghi nhận ở lượt 2 **không cần sửa nữa** — gỡ chức năng thì hết.

**Hủy 6 test case:**

| Mã | Nội dung | Trạng thái trước khi hủy |
|---|---|---|
| `DKTGKH_07` | Nhập đăng ký thủ công | Fail |
| `DKTGKH_08` | Nhập đăng ký thủ công — thiếu trường bắt buộc | Pass |
| `DKTGKH_09` | Nhập đăng ký thủ công — dữ liệu không hợp lệ | Pass |
| `DKTGKH_10` | Nhập đăng ký thủ công — học viên đã tồn tại | Pass |
| `DKTGKH_11` | Tải lên tệp Excel sai định dạng | Pass |
| `DKTGKH_12` | Tải lên tệp Excel | Fail |

Nhóm `KTDGKQHT_*` (điểm danh, điểm kiểm tra) **không ảnh hưởng** — thuộc UC24, luồng khác, đã chốt riêng ngày 16/07.

**Phản hồi gửi đối tác:** *"Đối chiếu danh sách use case và transaction gốc, luồng nhập tay và nhập tệp danh sách đăng ký không thuộc phạm vi UC22/UC23. Chức năng này sẽ được gỡ khỏi phần mềm và đặc tả. Đề nghị Quý đơn vị hủy các trường hợp kiểm thử DKTGKH_07 đến DKTGKH_12. Việc đăng ký khóa học thực hiện qua chuyên trang Pháp luật quốc gia."*

> **Lưu ý khi triển khai:** đổi `nguoi_dang_ky_id` sang bắt buộc là đúng đặc tả, nhưng phải kiểm tra và bù dữ liệu cũ đang rỗng trước khi áp ràng buộc ở cơ sở dữ liệu (`srs-v3.5.md` INS-06 — di trú dữ liệu đang chờ khảo sát).

---

## Việc kèm theo khi bàn giao bản `.docx` mới

Bản `.docx` dựng lại từ `.md` sẽ **không còn 22 mục thuộc hướng A**. Phải gửi kèm **danh sách mã test case cần sửa Kết quả mong đợi**, nếu không đơn vị kiểm thử chấm bản mới bằng thước cũ và ghi nhận lại đúng bấy nhiêu lỗi.

Danh sách mã và hướng sửa Expected: xem `docs/Bao-cao-doi-soat/phan-tich-nhom-2-tranh-chap-dac-ta-2026-07-29.md` mục 6.6.

Riêng `QLDMTCDGHTCP_06` / `QLDMTCDGHTCP_12` **không nằm trong danh sách sửa Expected** — Kết quả mong đợi của hai ca này giữ nguyên, vì phần mềm sẽ được sửa cho khớp thay vì sửa tài liệu.

**Kèm theo việc thứ hai — đề nghị đối tác hủy 6 test case:** `DKTGKH_07` · `DKTGKH_08` · `DKTGKH_09` · `DKTGKH_10` · `DKTGKH_11` · `DKTGKH_12`. Bốn ca trong đó đang ở trạng thái Pass. Bản `.docx` mới sẽ không còn mô tả luồng nhập tay/import danh sách đăng ký, nên nếu không báo trước thì đối tác vẫn chấm theo bộ cũ.

---

## Tổng hợp cập nhật sheet

| Nhóm | Số mã | Trạng thái dev fix 2 | DEV phản hồi lần 2 |
|---|---:|---|---|
| Hướng A thuần (cụm 1–3 + 8 ca lẻ) | 21 | `Resoved` | Câu chuẩn hướng A |
| Loại 4B `QLDMTCDGHTCP_06`, `QLDMTCDGHTCP_12` | 2 | Giữ nguyên `Reopent` | Không điền — BA chốt thống nhất nhãn, Dev sửa |
| Ca lai `CPCTHTTTG_03` | 1 | Giữ nguyên `Reopent` | Phản hồi 2 ý |
| Loại 1 `TLCTCDG_11`, `TKDGHQHTPL_02` | 2 | Giữ nguyên `Reopent` | Không điền |
| Loại 2 `DKTGKH_12` | 1 | Giữ nguyên `Reopent` | Phản hồi gỡ luồng (xem mục riêng). **Hủy cùng `DKTGKH_07`→`_11`** sau khi Dev gỡ chức năng |

**Tổng: 21 ghi trạng thái · 6 giữ `Reopent`.**

**Giá trị ghi vào sheet là `Resoved`** — đúng chính tả sheet đang dùng (xác nhận qua các ô sẵn có: `dev done` · `Resoved` · `Reopent` · `InProcess` · `Reject`). Không tự sửa thành `Resolve`.

### Đã thực hiện — 30/07/2026

| Việc | Kết quả |
|---|---|
| Ghi `Resoved` + câu chuẩn vào `V`/`W` của 21 dòng hướng A | 21/21 đúng, đã đọc lại sheet kiểm chứng |
| Ghi phản hồi 2 ý vào `W` cho `CPCTHTTTG_03` (dòng 1391) | Xong, cột `V` không đụng |
| Ghi phản hồi vào `W` cho `DKTGKH_12` (dòng 258) | **Đã ghi đè lần 2** — nội dung đầu viết theo quyết định *giữ* luồng import, sau khi đảo quyết định đã thay bằng nội dung đề nghị hủy `DKTGKH_07`→`_12` |
| `QLDMTCDGHTCP_06`, `QLDMTCDGHTCP_12`, `TLCTCDG_11`, `TKDGHQHTPL_02` | Để trống `V`/`W` theo thiết kế — chờ Dev sửa |
| Soát ghi lạc dòng | Không có dòng nào ngoài phạm vi bị thay đổi |

**Còn treo:** cột `Mã TC` vẫn là công thức, chưa chuyển thành giá trị cố định như đã thống nhất với đơn vị kiểm thử. Cần nhắc họ chuyển trước đợt ghi sau — nếu chèn/xóa dòng thì mã trôi và không lần lại được.

**Ghi vào cột lượt 2** (`Trạng thái dev fix 2` / `DEV phản hồi lần 2`), không ghi đè cột lượt 1 — cột lượt 1 đang giữ lời bác bỏ của đội phát triển, là bằng chứng của vòng trước.
