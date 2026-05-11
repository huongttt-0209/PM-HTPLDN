# Trả lời các nội dung cần BA xác nhận - Round 7

**Ngày:** 2026-05-11  
**Nguồn câu hỏi:** `/Users/linhsmac/Downloads/tong-hop-need-ba-round7-2026-05-11.md`  
**Nguồn đối chiếu:** `_bmad-output/planning-artifacts/srs-v3.5`

## Cách đọc

- **Quyết định đã chốt:** kết luận BA đã đồng ý để Dev/QA bám theo.
- **Căn cứ SRS:** đoạn SRS v3.5 tương ứng.
- **Việc cần làm:** nêu rõ sửa SRS hay Dev/QA sửa theo SRS hiện có.

## Danh sách việc cần làm sau khi BA chốt

### Cần sửa hoặc bổ sung SRS

1. **FR-05.6:** sửa wording FR-V.I-10 từ "NHT xác nhận" thành "người được phân công xác nhận", bao gồm NHT/TVV/CG hoặc TVV do tổ chức tư vấn cử.
2. **FR-06.2:** bổ sung ngưỡng SLA 4 mức `warning`, `urgent`, `critical`, `overdue`.
3. **FR-08.1:** tách rõ quyền QTHT CRUD danh mục tiêu chí dùng chung, còn tiêu chí trong từng đợt đánh giá do CB NV thao tác theo workflow của đợt.
4. **FR-08.5:** bổ sung rule KPI "Vụ việc hoàn thành": trạng thái được đếm, trường ngày dùng để lọc, và phạm vi đơn vị.
5. **FR-08.7:** đồng bộ field `KE_HOACH_DANH_GIA.muc_tieu` thành bắt buộc trong entity, hoặc ghi rõ DB nullable nhưng nghiệp vụ bắt buộc ở FE/BE.
6. **Hợp đồng TV:** bổ sung ghi chú route `/hop-dong-tv/danh-sach` nếu giữ thì chỉ là route kỹ thuật/ẩn, không phải menu nghiệp vụ độc lập.

### Dev/QA sửa theo SRS hiện có

1. **FR-05.1:** Dev sửa logic duplicate đánh giá theo `(vu_viec_id, loai_nguoi_danh_gia)`; QA sửa expected duplicate error về `ERR-DG-VV-03`.
2. **FR-05.2:** Dev bỏ fallback âm thầm ưu tiên 3 khi thiếu dữ liệu bắt buộc; QA test theo hướng chặn/cảnh báo.
3. **FR-05.3:** Dev lọc/chặn phân công người ngoài scope nếu người nhận không có quyền xem vụ việc.
4. **FR-05.4:** Dev/QA thống nhất SLA vụ việc mặc định là 15 ngày làm việc.
5. **FR-05.5:** QA sửa expected enum lịch sử phân công về `PHAN_CONG`.
6. **FR-06.1:** Dev chặn yêu cầu bổ sung lần 4 khi `bo_sung_count = 3`; QA test theo hướng bị chặn.
7. **FR-08.2:** Dev sửa API eligible vụ việc theo `HOAN_THANH` + trong kỳ + đúng phạm vi đơn vị; QA không thêm điều kiện lĩnh vực nếu SRS chưa bổ sung.
8. **FR-08.3:** Dev sửa state sau duyệt phân công thành `THUC_HIEN`, label "Thực hiện đánh giá".
9. **FR-08.4:** Dev/QA bỏ các state machine cũ, bám Section 5 của FR-08.
10. **FR-08.6:** Dev hỗ trợ sửa phân công khi đợt còn `PHAN_CONG`; QA không coi delete + add là cách duy nhất nếu UI/API đã có editable.
11. **FR-12.1:** Dev cung cấp mock time/trigger job/test command để QA kiểm thử cron 2 ngày; QA không chờ E2E thật trong regression thường xuyên.

---

## FR-05 Vụ việc

### 1. Cách chặn đánh giá trùng cho vụ việc

**Quyết định đã chốt:** Bắt buộc chặn duplicate bằng rule riêng, không chỉ dựa vào trạng thái `DA_DANH_GIA`. Mã lỗi đúng theo SRS v3.5 là `ERR-DG-VV-03`, không phải `ERR-DG-VV-04`.

**Giải thích dễ hiểu:** Trạng thái `DA_DANH_GIA` chỉ nói rằng vụ việc đã có ít nhất một đánh giá. Nhưng SRS cho phép mỗi vụ việc có tối đa 2 loại đánh giá: 1 từ `CB_NV` và 1 từ `DN`. Vì vậy nếu chỉ chặn theo trạng thái thì sẽ chặn nhầm lần đánh giá hợp lệ của loại người đánh giá còn lại.

**Căn cứ SRS:**
- `srs-fr-05-vu-viec.md`, FR-V.I-17: "Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc".
- Processing bước 5: nếu đã có `DANH_GIA_VU_VIEC` cùng vụ việc và cùng loại người đánh giá thì trả `ERR-DG-VV-03`.
- Entity `DANH_GIA_VU_VIEC`: `UNIQUE(vu_viec_id, loai_nguoi_danh_gia)`.
- `ERR-DG-VV-04` trong SRS là lỗi không có quyền đánh giá, không phải lỗi duplicate.

**Việc cần làm:** Dev cần kiểm tra duplicate theo `(vu_viec_id, loai_nguoi_danh_gia)`. QA sửa expected error duplicate về `ERR-DG-VV-03`; nếu tài liệu test đang ghi `ERR-DG-VV-04` thì test/spec phụ cần cập nhật.

### 2. Tạo vụ việc khi hồ sơ doanh nghiệp thiếu dữ liệu ưu tiên

**Quyết định đã chốt:** Không chấp nhận fallback mặc định về ưu tiên 3 khi thiếu dữ liệu bắt buộc để tính ưu tiên. Hệ thống phải cảnh báo/chặn tạo vụ việc và yêu cầu DN cập nhật đủ thông tin trước.

**Căn cứ SRS:**
- `srs-fr-05-vu-viec.md`, FR-V.I-02 ghi rõ các field `la_nu_lam_chu`, `so_lao_dong_nu`, `so_lao_dong_khuyet_tat` là input bắt buộc của `BR-CALC-07`.
- Nếu DN thiếu các field này, Processing bước 2 trả lỗi yêu cầu DN cập nhật thông tin trước khi tạo vụ việc.

**Việc cần làm:** Dev bỏ fallback âm thầm về mức 3 trong luồng tạo vụ việc chính. Có thể giữ mức 3 chỉ khi dữ liệu đủ nhưng không rơi vào nhóm ưu tiên cao hơn.

### 3. Phân công NHT/TVV khác đơn vị với vụ việc

**Quyết định đã chốt:** Không cho phân công người/tổ chức khác phạm vi hợp lệ nếu sau đó người được phân công không thể xem vụ việc. Màn hình phân công phải chỉ cho chọn người cùng đơn vị/phạm vi hợp lệ, hoặc backend phải reject ngay khi phân công.

**Căn cứ SRS:**
- FR-V.I-09 yêu cầu kiểm tra quyền + scope đơn vị khi phân công.
- Lỗi `ERR-PC-05`: "Bạn không có quyền phân công VV của đơn vị khác".
- `BR-AUTH-08`: cán bộ TW xem toàn bộ; cán bộ BN/ĐP chỉ xem dữ liệu thuộc đơn vị mình, BN và ĐP ngang cấp không thấy nhau.
- Entity `PHAN_CONG_VU_VIEC` có `don_vi_id` sở hữu dữ liệu.

**Việc cần làm:** Dev lọc danh sách ứng viên trong modal phân công theo scope mà người nhận có thể truy cập. Nếu sau này nghiệp vụ muốn "xem theo assignment" xuyên đơn vị, SRS phải bổ sung exception rõ vào `BR-AUTH-08`; hiện tại SRS chưa có exception này cho FR-05.

### 4. SLA vụ việc theo NĐ55/2019

**Quyết định đã chốt:** SLA vụ việc là **15 ngày làm việc**.

**Căn cứ SRS:**
- `srs-fr-05-vu-viec.md` phần tổng quan ghi SLA: 15 ngày làm việc, cite NĐ55/2019 Điều 8 Khoản 1.
- `BR-SLA-01`: SLA mặc định = 15 ngày làm việc, có thể cấu hình khác tại UC108.
- Changelog FR-05 v3.5 ghi đã đổi SLA 10 -> 15 ngày.

**Việc cần làm:** Dev/QA dùng 15 ngày làm việc làm mặc định. Nếu hệ thống có cấu hình SLA, test mặc định vẫn là 15 ngày trừ khi cấu hình bị override.

### 5. Enum lịch sử phân công

**Quyết định đã chốt:** Giữ enum chung `PHAN_CONG`.

**Căn cứ SRS:**
- FR-V.I-09 Processing bước 8 ghi lịch sử `hanh_dong='PHAN_CONG'`, nội dung chứa `loai_doi_tuong_xu_ly`, `nguoi_xu_ly_id`, `to_chuc_tu_van_id` nếu có.
- Entity `LICH_SU_VU_VIEC.hanh_dong` chỉ có enum `PHAN_CONG`, không có `PHAN_CONG_CA_NHAN` hoặc `PHAN_CONG_TO_CHUC`.
- Mô tả field ghi rõ tên neutral để cover mọi loại cá nhân được phân công.

**Việc cần làm:** QA sửa expected enum về `PHAN_CONG`. Nếu cần phân biệt cá nhân/tổ chức, đọc trong `noi_dung` hoặc các field phân công liên quan, không tách enum lịch sử.

### 6. Actor chấp nhận phân công ở bước B3

**Quyết định đã chốt:** Trong FR-05, bước chấp nhận/từ chối phân công áp dụng cho người được phân công xử lý vụ việc, gồm NHT/TVV/CG cá nhân hoặc TVV được tổ chức cử. UI đang ghi nhãn "NHT" nhưng SRS state machine và entity đã mở rộng sang NHT/TVV/CG.

**Căn cứ SRS:**
- FR-V.I-09 mô tả phân công cho cá nhân `TVV/CG/Người hỗ trợ` hoặc tổ chức tư vấn.
- Entity `PHAN_CONG_VU_VIEC.nguoi_xu_ly_id` ghi rõ cá nhân nhận phân công gồm TVV/CG/NHT; loại tổ chức thì `nguoi_xu_ly_id` là TVV thuộc tổ chức được cử.
- SM-VUVIEC có transition `DA_PHAN_CONG -> DANG_XU_LY: NHT/TVV xác nhận tham gia`.
- FR-V.I-10 hiện phần Preconditions dùng nhãn NHT, nhưng Cross-ref/entity/state đã rộng hơn.

**Việc cần làm:** SRS sửa nhãn FR-V.I-10 từ "NHT" thành "người được phân công" để hết mâu thuẫn. Dev hiển thị nút chấp nhận/từ chối cho tài khoản đang là `nguoi_xu_ly_id` của bản ghi phân công, không hard-code chỉ vai trò NHT.

---

## FR-06 Chi trả

### 1. Lần yêu cầu bổ sung thứ 4

**Quyết định đã chốt:** Không cho yêu cầu bổ sung lần thứ 4. Khi `bo_sung_count = 3`, backend phải chặn thao tác yêu cầu bổ sung tiếp và yêu cầu CB NV chọn kết quả khác: `DAT` để đi tiếp hoặc `KHONG_DAT` để chuyển `TU_CHOI`.

**Căn cứ SRS:**
- UI hiển thị "Lần bổ sung: {n}/3".
- Entity `HO_SO_CHI_TRA.bo_sung_count` có `CHECK BETWEEN 0 AND 3`.
- Ghi chú SRS nêu "giới hạn nghiệp vụ tối đa 3 lần".
- Processing kiểm tra hồ sơ đang tăng `bo_sung_count += 1` khi yêu cầu bổ sung.

**Việc cần làm:** Dev thêm guard trước khi tăng counter: nếu đã bằng 3 thì trả lỗi rõ ràng, không tự động chuyển `TU_CHOI` nếu CB NV chưa ra quyết định. QA test lần 4 theo expected "bị chặn". SRS có thể bổ sung error code/message để rõ hơn.

### 2. Ngưỡng SLA 4 mức cảnh báo

**Quyết định đã chốt:** SRS v3.5 chưa nêu ngưỡng cụ thể cho 4 mức `warning`, `urgent`, `critical`, `overdue`. Không tự suy diễn ngưỡng trong test. Cần bổ sung cấu hình chuẩn vào SRS.

**Ngưỡng chốt để đưa vào SRS:** Dùng cùng logic % thời gian đã dùng như FR-05:
- `warning`: từ 70% đến dưới 85%.
- `urgent`: từ 85% đến dưới 100%.
- `critical`: từ 100% trở lên nhưng chưa hoàn thành.
- `overdue`: quá deadline ngày làm việc.

**Lưu ý:** `critical` và `overdue` dễ trùng nghĩa nếu chỉ dựa vào deadline. Nếu muốn 4 mức thật sự tách biệt, nên định nghĩa `critical` là "còn 0-1 ngày làm việc trước deadline", còn `overdue` là "đã quá deadline".

**Căn cứ SRS:**
- `srs-fr-06-chi-tra.md` chỉ ghi UI có "SLA 4 mức cảnh báo".
- `BR-CALC-03` chỉ định deadline = ngày tiếp nhận + N ngày làm việc từ `CAU_HINH_SLA`, chưa định nghĩa ngưỡng 4 mức.

**Việc cần làm:** SRS/UC108 bổ sung ngưỡng SLA 4 mức trước khi QA khóa expected. Dev chỉ triển khai theo ngưỡng đã cấu hình/chốt.

---

## FR-08 Đánh giá HTPL

### 1. Quyền QTHT trên tiêu chí của từng đợt đánh giá

**Quyết định đã chốt:** QTHT chỉ CRUD danh mục tiêu chí dùng chung ở Nhóm VIII, không trực tiếp sửa tiêu chí đã gắn vào từng đợt đánh giá trong FR-08. Trong từng đợt, thao tác thêm/sửa/xóa tiêu chí thuộc CB NV quản lý đợt và phải bị khóa khi đang chấm điểm.

**Căn cứ SRS:**
- Entity `TIEU_CHI_DANH_GIA` mô tả là "Bộ tiêu chí đánh giá hiệu quả HTPL và đánh giá hồ sơ chi trả", module sở hữu là Nhóm VIII.
- FR-VI-02 lại mô tả "Quản lý tiêu chí đánh giá cho từng đợt".
- FR-VI-06 có lỗi `ERR-DG-TC-02`: không thể sửa tiêu chí khi đang đánh giá.

**Việc cần làm:** SRS tách rõ: QTHT quản lý master criteria; CB NV copy/chọn/cấu hình tiêu chí cho từng đợt. UI tab Tiêu chí của đợt không cho QTHT sửa nếu QTHT không phải actor quản lý đợt.

### 2. Điều kiện chọn vụ việc vào đợt đánh giá

**Quyết định đã chốt:** Lọc vụ việc eligible theo tổ hợp điều kiện: trạng thái `HOAN_THANH`, nằm trong kỳ đánh giá, thuộc phạm vi đơn vị của đợt/người dùng. Không lọc theo lĩnh vực người đánh giá ở bước chọn vụ việc vì SRS hiện chưa yêu cầu.

**Căn cứ SRS:**
- FR-VI-05 input `vu_viec_ids`: FK `VU_VIEC`, trạng thái `HOAN_THANH`.
- Processing bước 1: chỉ CB NV trong phạm vi đơn vị được chọn/bỏ chọn.
- Processing bước 1a: đợt phải ở trạng thái `THUC_HIEN`.
- Processing bước 2: lọc vụ việc đã hoàn thành trong kỳ đánh giá, thuộc phạm vi đơn vị.

**Việc cần làm:** Dev sửa API eligible theo 3 điều kiện trên. QA không thêm điều kiện lĩnh vực vào expected nếu SRS chưa bổ sung.

### 3. Tên trạng thái sau khi phê duyệt phân công

**Quyết định đã chốt:** Sau khi CB PD phê duyệt phân công, trạng thái chính thức là `THUC_HIEN`, label tiếng Việt: **"Thực hiện đánh giá"**.

**Căn cứ SRS:**
- Changelog FR-08 ngày 2026-05-11 chốt: CB PD duyệt thì đợt chuyển `CHO_DUYET_PC -> THUC_HIEN`.
- FR-VI-04 Processing bước 5: nếu duyệt, chuyển trạng thái sang `THUC_HIEN`.
- SM-DANHGIA Section 5: `CHO_DUYET_PC --> THUC_HIEN`.

**Việc cần làm:** App không được giữ label `CHO_DUYET_PC` sau khi duyệt. Dev cập nhật transition và UI badge/filter.

### 4. Chuẩn state machine của module Đánh giá

**Quyết định đã chốt:** Chuẩn chính thức là SM-DANHGIA 8 trạng thái nghiệp vụ + `HUY`:

`LAP_KE_HOACH -> PHAN_CONG -> CHO_DUYET_PC -> THUC_HIEN -> BAO_CAO -> CHO_PHE_DUYET -> HOAN_THANH`, kèm nhánh `HUY`.

**Căn cứ SRS:**
- Phần tổng quan FR-08 ghi `[GAP-VI-01]` thống nhất SM-DANHGIA về 8 states + `HUY`.
- Section 5 là source of truth.
- UI filter cũng liệt kê đúng 9 lựa chọn gồm 8 state trên + `HUY`.

**Việc cần làm:** Dev/QA bỏ các phiên bản 6 state hoặc 7 state cũ. Test plan phải bám Section 5 của `srs-fr-08-danh-gia.md`.

### 5. KPI "Vụ việc hoàn thành" trên Dashboard/Đánh giá

**Quyết định đã chốt:** KPI "Vụ việc hoàn thành" đếm cả `HOAN_THANH` và `DA_DANH_GIA`; không đếm `DA_DUYET` nếu tên KPI là "hoàn thành".

**Căn cứ SRS:**
- SM-VUVIEC: `HOAN_THANH -> DA_DANH_GIA`; `DA_DANH_GIA` là trạng thái sau hoàn thành, không phải trạng thái đang xử lý.
- Tab UI FR-05 nhóm "Hoàn thành" đang gộp `DA_DUYET + HOAN_THANH + DA_DANH_GIA`, nhưng đây là tab vận hành rộng, không phải định nghĩa KPI.
- FR-VI-05 chỉ chọn vụ việc trạng thái `HOAN_THANH` vào đợt đánh giá. Nếu cần chọn cả đã đánh giá, SRS cần sửa.

**Filter chốt:** Đếm theo `VU_VIEC.trang_thai IN ('HOAN_THANH','DA_DANH_GIA')`, trong khoảng thời gian theo `ngay_hoan_thanh`, và theo `don_vi_id` đúng phạm vi người xem.

**Việc cần làm:** SRS bổ sung rõ rule KPI vào Dashboard/Đánh giá. Riêng API chọn vụ việc đánh giá vẫn bám SRS hiện tại là `HOAN_THANH`.

### 6. Có cần chức năng sửa phân công không?

**Quyết định đã chốt:** Có chức năng sửa phân công. SRS hiện đã mô tả bảng phân công là editable/inline edit ở UI, nên coi sửa phân công là chức năng chính thức khi đợt còn ở `PHAN_CONG`.

**Căn cứ SRS:**
- FR-VI-03 mô tả quản lý phân công người đánh giá.
- UI `SCR-VI-01`, dòng 36: "Bảng phân công (Editable)" với inline table gồm Người ĐG, Vai trò, Lĩnh vực phụ trách, Ghi chú, Hành động xóa.
- Dòng 38 có `[Lưu nháp]`.

**Việc cần làm:** Dev hỗ trợ sửa inline trước khi trình duyệt. Sau khi đã `CHO_DUYET_PC` hoặc `THUC_HIEN`, không sửa trực tiếp; nếu cần thay đổi thì từ chối quay lại `PHAN_CONG` hoặc hủy/lập lại theo rule. Có thể bổ sung API/processing vào SRS nếu muốn chặt hơn.

### 7. Field "Mục tiêu" có bắt buộc không?

**Quyết định đã chốt:** `Mục tiêu` là bắt buộc theo form tạo/sửa, dù entity hiện để nullable. UI và backend phải validate bắt buộc.

**Căn cứ SRS:**
- FR-VI-01 Inputs: `muc_tieu` bắt buộc = `Y`.
- UI form tạo/sửa: "Mục tiêu" là bắt buộc.
- Entity `KE_HOACH_DANH_GIA.muc_tieu` đang `N`, đây là lệch entity so với FR/UI.

**Việc cần làm:** Dev thêm validate required ở FE/BE. SRS sửa entity `muc_tieu` từ `N` thành `Y` hoặc ghi rõ lý do DB nullable nhưng nghiệp vụ required. QA tiếp tục coi bỏ trống là lỗi.

---

## FR-12 TVCS

### 1. Cách kiểm thử rule cron 2 ngày

**Quyết định đã chốt:** Nghiệm thu không bắt QA chờ đủ 2 ngày làm việc thật. Dev cần cung cấp cách kiểm thử chủ động: mock thời gian, trigger job thủ công, hoặc endpoint/test command chỉ bật ở môi trường test.

**Căn cứ SRS:**
- FR-X.1-01: CG/TVV xác nhận trong SLA 2 ngày làm việc.
- Section 5 SM-TVCS: sau timeout, auto-reject và trả về `TIEP_NHAN` để phân công lại.
- Rule dùng `CAU_HINH_SLA`, nghĩa là có cơ sở cấu hình/mô phỏng trong môi trường test.

**Việc cần làm:** Dev cung cấp mock/trigger phục vụ QA. QA test 3 lớp: trước hạn không reset; quá hạn thì job chuyển `PHAN_CONG -> TIEP_NHAN`; có audit/thông báo đúng. Không cần test E2E chờ thời gian thật trong regression thường xuyên.

---

## Hợp đồng TV

### 1. Route standalone `/hop-dong-tv/danh-sach`

**Quyết định đã chốt:** Không hiển thị route standalone như một màn hình/menu nghiệp vụ độc lập. Nếu giữ route kỹ thuật thì phải là route ẩn, có guard quyền, và tốt nhất redirect về ngữ cảnh Vụ việc/TVV hoặc chỉ dùng nội bộ admin/dev.

**Căn cứ SRS:**
- `srs-v3.5.md` danh mục module ghi HĐ TV không nằm trong menu, accessible từ Vụ việc/TVV.
- `srs-fr-14-hop-dong-tv.md` Section 3 ghi: HĐ tư vấn không còn là mục menu riêng; truy cập từ chi tiết Vụ việc hoặc chi tiết TVV; nội dung MH-14.1 chỉ giữ để tham chiếu element-level, implement dạng modal/drawer.
- `srs-fr-09-bieu-mau.md` ghi FR-VII-08 đã chuyển sang `srs-fr-14-hop-dong-tv.md`.

**Việc cần làm:** Dev xóa khỏi sidebar/menu và chặn điều hướng user thường tới `/hop-dong-tv/danh-sach`. Nếu vẫn cần route để tái sử dụng component, route phải không public trong navigation, kiểm tra quyền đầy đủ, và không được QA coi là luồng chính. SRS bổ sung ghi chú nếu quyết định giữ route ẩn.

---

## Tóm tắt chốt nhanh

| Mục | Câu trả lời ngắn |
|---|---|
| FR-05.1 Duplicate đánh giá | Chặn bằng duplicate rule `(vu_viec_id, loai_nguoi_danh_gia)`, lỗi `ERR-DG-VV-03`; không chỉ chặn bằng trạng thái |
| FR-05.2 Thiếu dữ liệu ưu tiên DN | Chặn/cảnh báo, yêu cầu cập nhật DN; không fallback âm thầm mức 3 |
| FR-05.3 Phân công khác đơn vị | Không cho nếu người nhận không có quyền xem; lọc ứng viên theo scope |
| FR-05.4 SLA vụ việc | 15 ngày làm việc |
| FR-05.5 Enum lịch sử phân công | Giữ `PHAN_CONG` chung |
| FR-05.6 Actor chấp nhận PC | Người được phân công: NHT/TVV/CG hoặc TVV tổ chức cử |
| FR-06.1 Bổ sung lần 4 | Không cho yêu cầu bổ sung tiếp khi đã đủ 3 lần |
| FR-06.2 SLA 4 mức | SRS chưa đủ ngưỡng; cần BA bổ sung, khuyến nghị warning/urgent/critical/overdue theo % hoặc ngày còn lại |
| FR-08.1 Quyền QTHT tiêu chí | QTHT CRUD danh mục dùng chung; không sửa tiêu chí từng đợt trong FR-08 |
| FR-08.2 Eligible vụ việc | `HOAN_THANH` + trong kỳ + đúng phạm vi đơn vị; chưa lọc theo lĩnh vực |
| FR-08.3 State sau duyệt PC | `THUC_HIEN` - "Thực hiện đánh giá" |
| FR-08.4 State machine chuẩn | 8 state + `HUY`, Section 5 là source of truth |
| FR-08.5 KPI VV hoàn thành | Đếm `HOAN_THANH` + `DA_DANH_GIA`, theo thời gian hoàn thành và đơn vị |
| FR-08.6 Sửa phân công | Có, khi còn `PHAN_CONG`; UI đã mô tả editable |
| FR-08.7 Mục tiêu | Bắt buộc |
| FR-12.1 Cron 2 ngày | QA nên dùng mock/trigger job, không chờ thật |
| HĐ TV.1 Route standalone | Không public/menu; route ẩn có guard hoặc redirect theo ngữ cảnh |
