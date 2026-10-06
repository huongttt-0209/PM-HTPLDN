# Kế Hoạch Kiểm Thử — Đợt cập nhật SRS `CR-GY-2026-09-13` (phiếu góp ý cải tiến 08/09/2026)

> **Phiên bản**: 1.0
> **Ngày tạo**: 2026-09-14
> **Chế độ**: BMAD test-design, mức epic (tạo mới)
> **Nguồn dữ liệu**: LOCAL — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (commit `81b74c6` — đã gồm mọi quyết định BA chốt; mọi số dòng trong file theo bản này). Phạm vi theo `docs/phuong-an-cap-nhat-srs-2026-09-10.md`. Không lấy số dòng từ `input/srs-update-2026-5-5/`.
> **SRS Reference**: FR-II-11, FR-II-12, FR-V.I-18, FR-VIII-33, KPI-S-03 (mới) · FR-II-01, FR-II-03, FR-V.I-05, FR-V.I-06, FR-V.I-12, FR-IV-01, FR-IV-03, FR-IV-04, FR-IX-01, FR-IX-13, FR-IX-18, FR-VIII-07 (sửa) · BR-FLOW-11, BR-RPT-02
> **Chưa có giao diện**: bỏ mọi kiểm tra UI — tab, stepper, nhãn, màu, huy hiệu, vị trí khối, tùy chọn bộ lọc (quyết định 14/09/2026). Mục A của từng file ghi "Hoãn" kèm danh sách SCR để bổ sung khi có bản dựng.
> **BA sign-off**: **đủ** — mọi câu hỏi của đợt (Q01–Q25, phiếu Dev BA-R1, BA-R2, A1–A4, D1–D29 trừ D9, D27) BA đã chốt và đã vào SRS `81b74c6`. Không TC nào chờ BA; 9 TC chờ CĐT (H1, A5, T8 — §5.1). Chỗ SRS còn chưa khớp ghi ở mục Ghi nhận SRS cuối từng file, không làm treo TC nào.

---

## 0. Quy ước đọc

### 0.1 Trích dẫn rút gọn

| Viết trong TC | Nghĩa là |
|---|---|
| `fr-NN:LINE` | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-NN-<tên>.md:LINE` |
| `v35:LINE` | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:LINE` |
| `:LINE` | Cùng tệp với trích dẫn đứng gần nhất phía trước, **trên cùng dòng** |

| `fr-NN` | Tệp |
|---|---|
| `fr-01` | `srs-fr-01-dashboard.md` |
| `fr-02` | `srs-fr-02-hoi-dap.md` |
| `fr-04` | `srs-fr-04-chuyen-gia-tvv.md` |
| `fr-05` | `srs-fr-05-vu-viec.md` |
| `fr-06` | `srs-fr-06-chi-tra.md` |
| `fr-07` | `srs-fr-07-doanh-nghiep.md` |
| `fr-10` | `srs-fr-10-quan-tri.md` |
| `fr-11` | `srs-fr-11-bao-cao.md` |
| `fr-13` | `srs-fr-13-tv-nhanh.md` |
| `fr-16` | `srs-fr-16-api.md` |

File hỏi BA dùng đường dẫn đầy đủ, không dùng dạng rút gọn.

### 0.2 Nhãn và cách ghi kết quả

| Ký hiệu | Nghĩa | Tính vào tỷ lệ đạt? |
|---|---|---|
| `⏸ chờ CĐT – H1 / A5 / T8` | Phụ thuộc điểm CĐT hoãn. Không hỏi BA | Không |
| `⏸ chờ CĐT` ở một ý trong cột Kết quả, cột Tên không có nhãn | Kết quả chính chắc chắn; một ý phụ còn chờ | Có (ý phụ không chấm) |
| **SRS Gap** | SRS không định nghĩa (mã lỗi, câu thông báo, cách xử lý). Không tự nghĩ câu chữ | Lớp đó không chấm; ghi hành vi thực tế |

Cột Kết quả mong đợi chia 3 nhóm:

- **(1) Dữ liệu** — mở lại bản ghi, so từng trường với giá trị nêu. Không kết luận Đạt chỉ vì hệ thống báo thành công.
- **(2) Thông báo** — câu hệ thống trả cho người thao tác, chép nguyên văn SRS. SRS chưa có câu → ghi **SRS Gap** và chép câu thực tế vào cột Kết quả thực tế.
- **(3) Kiểm tra chéo** — nơi khác phải phản ánh thay đổi: danh sách (đếm trước và sau), lịch sử xử lý, thông báo tới người khác, nhật ký hệ thống. TC bị chặn phải đếm lại để chứng minh không sinh bản ghi.

**Quy ước viết nhóm (3)**:

- Mỗi ý là một phép kiểm chấm được: mở đầu bằng "bước N —" trỏ tới bước quan sát trong cột Các bước, kèm giá trị phải thấy (số đếm, số dòng lịch sử, trạng thái, người, thời điểm). Chưa có bước quan sát thì thêm bước, không viết ý.
- TC bị chặn: ý "đếm lại vẫn = N" đặt ở (3); (1) chỉ giữ trạng thái bản ghi.
- Số mốc (N, H, L, P…) đo ở một bước trong cột Các bước (bước "0." nếu phải đo trước mọi thao tác), không ghi ở tiền đề — tiền đề chỉ nêu trạng thái phải có.
- TC chỉ đọc ghi "— thao tác chỉ đọc"; TC ghi mà không có nơi khác phản ánh ghi "— không có bản ghi khác đổi".
- Ba loại dòng **không chấm**, tách khỏi (3) và đặt ngay sau: `*Kiểm tiếp ở:* TC-…` (phép kiểm nằm ở TC khác), `**Ghi lại (không chấm)**:` (giá trị cần ghi vì SRS chưa nói), `**⏸ chờ CĐT – …** (không chấm, không hỏi BA):` (ý phụ còn chờ). `*Ghi chú:*` dùng cho giải thích ngắn.
- Không viết vào (3): phép tính giải thích số, nhận xét về SRS, câu "như TC-…".

Dòng **Căn cứ** cuối ô là dòng SRS dùng để kết luận.

**Cột Kết quả thực tế** (file 01–11) — người chạy điền; trong ô xuống dòng bằng `<br>`, không dùng dấu `|`:

- Dòng đầu: trạng thái, ngày chạy, tài khoản thay thế nếu có. Trạng thái: ✅ Đạt · ⚠️ Sai spec · ❌ Lỗi · 🚫 Không test được · ⏭ Hoãn · 🤷 Không xác định.
- Tiếp theo ghi theo ba nhóm của cột Kết quả mong đợi, mỗi ý một dòng, mở đầu bằng số bước:
  - (1): giá trị đọc được của từng trường. Không ghi "đúng", "khớp".
  - (2): chép nguyên văn mã và câu hệ thống trả.
  - (3): **trước → sau** và nơi đọc. Ví dụ: `bước 4 — Từ chối STP-AG 12 → 13 (API danh sách); lịch sử VV-KT-20 5 → 6, dòng mới KIEM_TRA / CB_NV`.
- Ý không có số hoặc giá trị (chỉ "OK", "khớp", "đã kiểm") là 🤷, không tính Đạt.
- Ý không làm được: 🚫 kèm nhóm A–F và lý do. Không thay bằng phép kiểm khác rồi chấm ✅.
- Dòng Ghi lại: chép giá trị thấy được. TC nhãn ⏸: ghi hệ thống đi theo hướng nào, kèm giá trị. Cả hai không chấm.
- Trạng thái TC theo ý xấu nhất trong các ý chấm được: ❌ > 🚫 > 🤷 > ⚠️ > ✅. Lớp SRS Gap không tính (§9).

### 0.3 Cách chạy khi chưa có giao diện

- Mỗi bước ghi **tài khoản** thực hiện và **tên chức năng nghiệp vụ** (ví dụ "Chuyển sang Vụ việc"). Bước không ghi tài khoản thì dùng tài khoản của bước liền trước. Người chạy tra endpoint tương ứng trong `/api/docs-json` của môi trường, đăng nhập bằng tài khoản ghi ở bước, gọi API bằng phiên đó.
- Bước tra bảng (ví dụ `THONG_BAO`) hoặc bản ghi đã xóa mà tiền đề ghi "qua CSDL hoặc API quản trị": dùng quyền đọc CSDL của môi trường, hoặc API quản trị nếu `/api/docs-json` có. Không có quyền → mọi ý dựa vào bước đó ghi 🚫 nhóm F (cần DBA); không lấy vài hộp Thông báo của tôi thay vào rồi chấm ✅.
- "Mở chi tiết X" = gọi API xem chi tiết bản ghi X, đọc các trường nêu ở cột Kết quả mong đợi.
- "Đếm …" = gọi API danh sách với bộ lọc nêu ở bước, đọc tổng số bản ghi. Chạy bước đếm khi không ai khác đang tạo bản ghi cùng loại ở cùng đơn vị, nếu không số đếm sẽ lệch.
- Thư điện tử gửi đi đọc ở MailHog `http://103.172.236.130:8025`.
- Khi có giao diện, các bước giữ nguyên, chỉ đổi cách thao tác.

### 0.4 Thuật ngữ

| Viết tắt | Nghĩa |
|---|---|
| CB NV | Cán bộ nghiệp vụ |
| CB PD | Cán bộ phê duyệt |
| NHT | Người hỗ trợ pháp lý |
| DN | Doanh nghiệp |
| STP-AG, STP-BG | Sở Tư pháp An Giang, Sở Tư pháp Bắc Giang |
| BTP-TW | Cục Bổ trợ tư pháp — Bộ Tư pháp (cấp Trung ương) |
| Ngày làm việc | Thứ Hai đến Thứ Sáu, trừ ngày lễ đã cấu hình |

---

## 1. Phạm vi kiểm thử

### 1.1 Tóm tắt

- **292 TC trong 11 file**, chia hai phần theo yêu cầu: **Phần 1** — chức năng mới và chức năng đã sửa (file 01–09, 245 TC); **Phần 2** — chức năng cũ dùng trường, trạng thái, danh mục vừa đổi (file 10–11, 47 TC).
- **283 TC chạy được ngay**, 9 TC chờ CĐT (không P0 nào).
- Mọi căn cứ là dòng SRS `81b74c6` — không TC nào chấm theo thư phản hồi của BA; SRS đã gồm mọi quyết định BA chốt (§5.3).
- Bảy nhóm thay đổi T1–T7 theo file phạm vi §1; T8 không thi hành.

### 1.2 Phần 1 — chức năng mới và đã sửa

| # | Nhóm | Mã FR | Mới / sửa | Tên chức năng | Entity | File |
|---|---|---|---|---|---|---|
| 1 | T1 | FR-II-11 | Mới | Chuyển hồ sơ hỏi đáp sang vụ việc | HOI_DAP, VU_VIEC | `01-TC-chuyen-hoi-dap-sang-vu-viec.md` |
| 2 | T1 | FR-V.I-18 (+ FR-V.I-12 trường 3, FR-V.I-05 bước 5a, FR-II-11 §Hoàn tác) | Mới | Tiếp nhận hồ sơ chuyển từ Hỏi đáp; thông báo từ chối có hướng dẫn gửi lại; xóa vụ việc cầu nối và hoàn tác chuyển luồng | VU_VIEC, HOI_DAP | `02-TC-tiep-nhan-vu-viec-tu-hoi-dap.md` |
| 3 | T2 | FR-V.I-06 | Sửa | Kiểm tra hồ sơ 7 hạng mục, loại lý do từ chối; quy tắc chuyển tiếp cho hồ sơ kiểm tra theo danh mục 6 hạng mục | VU_VIEC | `03-TC-kiem-tra-ho-so-7-hang-muc.md` |
| 4 | T3 + lỗi (f) | FR-II-01 trường 12–14, FR-II-03 | Sửa | Ba trường phân loại ảnh chụp; lĩnh vực ở bước tiếp nhận | HOI_DAP | `04-TC-truong-phan-loai-hoi-dap.md` |
| 5 | T7 | FR-II-12 | Mới | Gợi ý câu hỏi đã xử lý tương tự | KHO_CAU_HOI, HOI_DAP | `05-TC-goi-y-cau-hoi-tuong-tu.md` |
| 6 | T3 + QĐ 7 + lỗi (b) | FR-VIII-33, FR-V.III-01 trường 7a, FR-VIII-07 | Mới + sửa | Danh mục Hình thức tổ chức; cột hình thức trên DN; nhãn "Quy mô doanh nghiệp" | DANH_MUC, DOANH_NGHIEP | `06-TC-danh-muc-hinh-thuc-to-chuc.md` |
| 7 | T6 | FR-IV-01, FR-IV-03, FR-IV-04 | Sửa | Thẻ hành nghề bắt buộc với TVV (cả khi CB NV thêm / sửa), minh chứng năng lực, không hồi tố | TU_VAN_VIEN, HO_SO_TU_VAN_VIEN | `07-TC-the-hanh-nghe-tvv.md` |
| 8 | T4 + BR-RPT-02 | FR-IX-01 | Sửa | Báo cáo hỏi đáp: nhóm thứ ba, mẫu số tỷ lệ, chiều địa bàn | HOI_DAP | `08-TC-bao-cao-hoi-dap-FR-IX-01.md` |
| 9 | T5 | KPI-S-03 | Mới | Thời gian xử lý toàn trình | VU_VIEC, HOI_DAP | `09-TC-kpi-thoi-gian-toan-trinh.md` |

### 1.3 Phần 2 — chức năng cũ bị ảnh hưởng

| Thay đổi ở tầng dữ liệu | Chức năng cũ đọc / kiểm nó | TC |
|---|---|---|
| Trạng thái thứ 10 `DA_CHUYEN_LUONG` của hỏi đáp (`v35:1544`) | FR-II-01 sửa / xóa / hủy; FR-II-02 tìm kiếm; FR-II-03 tiếp nhận; FR-II-04 cập nhật thời hạn; FR-II-05 tìm kiếm hồ sơ đã tiếp nhận; FR-II-06 phân công, khối lượng việc của NHT; FR-II-07 soạn phản hồi; FR-II-08 phê duyệt / từ chối / công khai / đóng hồ sơ, kể cả **hàng loạt**; FR-II-10 câu hỏi đã xử lý; BR-SLA-03 cảnh báo thời hạn; xuất Excel; quyền NHT; FR-XII-19 Cổng gửi lại hồ sơ đã chuyển | TC-HQHD-001 … -010, -020 … -024 |
| FR-II-03 thêm bước 2a / 2b (`fr-02:355`, `:356`) | Tính thời hạn 30 ngày cho hồ sơ phức tạp | TC-HQHD-011 |
| Kênh `CONG_PLQG` và cột `hoi_dap_goc_id` của vụ việc (`v35:1601`, `:1602`) | FR-V.I-04 lập tay; FR-V.I-05 hồ sơ từ hệ thống khác; FR-V.I-01 xóa, **xóa hàng loạt**; FR-V.I-07 cập nhật vụ việc; FR-V.I-03 thời hạn DVC; FR-V.I-12 đồng bộ LGSP; lọc / tìm theo kênh, xuất Excel | TC-HQHD-012 … -019, -025, -026 |
| BR-RPT-02 và vụ việc cầu nối | Dashboard KPI-01, KPI-02, KPI-04 (kể cả vụ việc `DA_DANH_GIA`), KPI-S-02; FR-IX-01 | TC-HQBC-001 … -004, -015 |
| Kênh `CONG_PLQG` | FR-IX-02 báo cáo vụ việc đã tiếp nhận theo kênh; vụ việc của DN chưa có quy mô | TC-HQBC-005, -017 |
| Nhãn "Quy mô doanh nghiệp", cột `hinh_thuc_to_chuc_id` trên DN (`v35:1748`, `:1749`); `loai_dn_id` không bắt buộc ở kênh cán bộ (`fr-07:695`) | FR-IX-13 (kể cả cấp Trung ương tách theo đơn vị), FR-IX-18 (kể cả xuất XLSX / PDF); FR-V.III-01 sửa DN lập trước ngày áp dụng; FR-VIII-22 DN tự đăng ký (thiếu quy mô); FR-V.III-NEW-02 DN tự cập nhật (hai tiêu chí lệch mức) | TC-HQBC-006 … -011, -014, -016 … -020 |
| Thẻ hành nghề bắt buộc ở FR-IV-03 / FR-IV-04 | FR-IV-06 thẩm định, FR-IV-07 phê duyệt / từ chối hồ sơ nộp trước ngày áp dụng | TC-HQBC-012, -013, -021 |

### 1.4 Ngoài phạm vi

| Nội dung | Lý do | Xử lý trong bộ TC |
|---|---|---|
| T8 — hộ kinh doanh, hợp tác xã là đối tượng thụ hưởng | Không thi hành (`v35:131`) | TC-HTTC-012 gắn `chờ CĐT – T8`, chỉ kiểm danh mục không làm đổi đối tượng |
| H1 — ai nhập ba trường phân loại | Tầng thao tác chờ CĐT | TC-PL-012 … -016, -020 gắn `chờ CĐT – H1` |
| V1, V3 | CĐT hoãn | Không có TC |
| A5 — chiều quy mô, hình thức ở FR-IX-01 | CĐT chưa chốt | TC-BC01-011, -015 gắn `chờ CĐT – A5`; TC-BC01-016, -020 một ý |
| Toàn bộ UI | Chưa có bản dựng | Mục A mỗi file ghi "Hoãn" |
| Danh sách kênh do hai cơ chế cùng quản | Điểm treo có chủ đích (`v35:3228`) | Không có TC |
| Hiệu năng tra cứu gợi ý (FR-II-12) | SRS không có NFR cho chức năng này | Ghi rủi ro R-11, không có TC |

### 1.5 Tài khoản

| Role | Đơn vị | Username | Dùng cho |
|---|---|---|---|
| CB_NV_DP | STP-AG | `cb_nv_dp_01` | Tài khoản chính của hầu hết TC |
| CB_NV_DP | STP-AG | `cb_nv_dp_04` | Phiên song song (TC-CL-019); người nhận thông báo (TC-CL-013) |
| CB_NV_DP | STP-BG | `cb_nv_dp_02` | Khác đơn vị, đơn vị thụ lý khác; tạo bản ghi kho STP-BG (file 05); dựng hồ sơ STP-BG của file 08, 09 |
| CB_NV_DP | STP-BNI | `cb_nv_dp_03` | Dựng bộ HD-BC-S01 … S10 ở STP-BNI (file 08) |
| CB_NV_TW | BTP-TW | `cb_nv_tw_01` | Phạm vi TW, báo cáo toàn quốc; tạo bản ghi kho TW (file 05) |
| CB_PD_DP | STP-AG | `cb_pd_dp_01` | Vai trò không phải CB NV; đưa hồ sơ hỏi đáp tới các trạng thái phê duyệt; báo cáo |
| CB_PD_DP | STP-BG | `cb_pd_dp_02` | Duyệt bản ghi kho STP-BG (file 05) |
| CB_PD_DP | STP-BNI | `cb_pd_dp_03` | Phê duyệt, công khai hồ sơ hỏi đáp STP-BNI (file 08) |
| CB_PD_TW | BTP-TW | `cb_pd_tw_01` | Duyệt bản ghi kho TW (file 05) |
| NHT | STP-AG | `nht_01` | Đăng ký / cập nhật TVV, NHT được phân công hỏi đáp |
| NHT | STP-DN | `nht_02` | NHT khác đơn vị |
| QTHT | — | `qtht_01` | Danh mục; nhật ký hệ thống; vai trò bị chặn (chuyển luồng, báo cáo) |
| DN | — | `9999999990` | Tài khoản doanh nghiệp đăng nhập: bổ sung hồ sơ, nhận thông báo (file 01, 02, 03, 10). MST `9999999991` chỉ dùng làm hồ sơ doanh nghiệp DN-CL-02 ở file 01, không đăng nhập. File 11 tạo tài khoản DN riêng (Chuẩn bị dữ liệu mục 3) |
| TVV | STP-AG | `tvv_cu_02` (tên gọi tạm) | TVV tự sửa hồ sơ (file 07). **Không có sẵn** trong `users.csv` — tạo theo file 07 "Chuẩn bị dữ liệu" mục 4, ghi lại tên đăng nhập thực |

> Nguồn: `input/users.csv` (trừ `tvv_cu_02`). Fallback theo Rule 7 của CLAUDE.md — chỉ cùng role, cùng đơn vị. Cán bộ phê duyệt chỉ duyệt kho của đơn vị mình (`v35:1325`, `:1375`), nên mỗi đơn vị có bản ghi kho cần người duyệt của chính đơn vị đó.

---

## 2. Quy tắc nghiệp vụ trích từ SRS

### 2.1 Business Rules

| Mã | Quy tắc | Nguồn | Áp dụng | Ngoại lệ SRS-quoted | TC áp dụng |
|---|---|---|---|---|---|
| BR-FLOW-11 | Chuyển luồng giữa các nhóm hỗ trợ: bản ghi đích mới, vào chờ tiếp nhận, không miễn kiểm tra hồ sơ | `v35:5744` | ✅ | Đợt này chỉ mở chiều Hỏi đáp → Vụ việc (`v35:131`, mục V3) | File 01, 02 |
| BR-RPT-02 | Mỗi yêu cầu chỉ tính hoàn thành một lần, tại nhóm đích | `v35:5847` | ✅ | — | File 08; TC-HQBC-001 … -004; TC-VVCL-018 |
| BR-SLA-01 | SLA vụ việc mặc định 15 ngày làm việc | `v35:5780` | ✅ | — | TC-VVCL-007, TC-HQHD-016 |
| BR-SLA-05 | Tỷ lệ tuân thủ SLA | `v35:5784` | ✅ | KPI-S-03 không vào công thức (`fr-01:666`) | TC-KPI3-003 |
| BR-CALC-03 | Deadline = ngày tiếp nhận + N ngày làm việc; hỏi đáp 15 / 30 ngày theo độ phức tạp | `v35:5756` | ✅ | — | TC-HQHD-011; cách đếm ngày file 09, 11 |
| BR-CALC-05 | Xác định quy mô DNNVV | `v35:5758` | ✅ | Hộ kinh doanh, HTX chỉ để ghi nhận (`fr-10:1653`) | TC-HTTC-012, TC-HQBC-011 |
| BR-AUTH-03 | Ngang cấp không thấy nhau | `v35:5674` | ✅ | QTHT thấy tất cả | TC-CL-023, TC-VVCL-004/-005/-019, TC-BC01-013 |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` | `v35:5683` | ✅ | — | Như trên; TC-KPI3-005 |
| BR-NOTIF-01 | Thông báo sự kiện workflow | `v35:5812` | ✅ | — | TC-CL-013, -027, -028, TC-HQBC-011 |
| BR-DATA-05 | Nhật ký mọi thao tác thêm / sửa / xóa | `v35:5723` | ✅ | — | TC-CL-012, TC-KT-014, TC-HTTC-002 |
| BR-DATA-01 | Xóa mềm | `v35:5719` | ✅ | — | TC-HTTC-009, TC-VVCL-006, TC-KPI3-009 |
| BR-EC-01 | Khóa lạc quan khi sửa / xóa | `v35:5855` | ✅ | — | TC-CL-019 (hai phiên chuyển cùng lúc); TC-CL-034 (chuyển ↔ gửi phản hồi cùng lúc); TC-VVCL-028 (xóa ↔ tiếp nhận vụ việc cầu nối cùng lúc) |

### 2.2 Mã lỗi mới của đợt

| Mã | Điều kiện | Câu thông báo (nguyên văn) | Mức | Nguồn |
|---|---|---|---|---|
| ERR-CL-01 | Hồ sơ đã chuyển trước đó | "Hồ sơ này đã được chuyển sang vụ việc {ma_vu_viec}. Mỗi hồ sơ hỏi đáp chỉ chuyển được một lần" | ERROR | `fr-02:1038` |
| ERR-CL-02 | Chưa xác định được doanh nghiệp | "Vui lòng gắn hồ sơ doanh nghiệp trước khi chuyển sang vụ việc" | ERROR | `fr-02:1039` |
| ERR-CL-03 | Trạng thái không cho chuyển | "Chỉ chuyển được hồ sơ đang ở trạng thái Tiếp nhận hoặc Đang xử lý" | ERROR | `fr-02:1040` |
| ERR-CL-04 | Chưa chọn loại hình hỗ trợ | "Vui lòng chọn loại hình hỗ trợ cho vụ việc" | ERROR | `fr-02:1041` |
| ERR-AUTH-CL-01 | Khác đơn vị với hồ sơ | "Bạn không có quyền chuyển hồ sơ của đơn vị khác" | ERROR | `fr-02:1042` |
| ERR-CL-VV-01 | Hồ sơ hỏi đáp gốc không tồn tại / đã xóa mềm | "Không mở được hồ sơ hỏi đáp gốc. Vui lòng liên hệ quản trị hệ thống" | WARNING | `fr-05:1402` |
| WRN-GY-01 | Chỉ mục tìm kiếm không phản hồi | "Chưa tra cứu được câu hỏi tương tự. Bạn vẫn tiếp tục xử lý bình thường" | WARNING | `fr-02:1148` |
| ERR-DK-10 | Đăng ký TVV thiếu số thẻ hoặc tệp thẻ | "Hồ sơ tư vấn viên phải có số thẻ hành nghề và bản chụp thẻ (Điều 20 Nghị định 77/2008/NĐ-CP)" | ERROR | `fr-04:363` |
| ERR-NL-06 | Cập nhật TVV thiếu số thẻ hoặc tệp thẻ | "Hồ sơ tư vấn viên phải có số thẻ hành nghề và bản chụp thẻ. Vui lòng bổ sung trước khi lưu" | ERROR | `fr-04:466` |
| ERR-TVV-10 | CB NV thêm / sửa TVV loại Tư vấn viên thiếu số thẻ hoặc tệp thẻ | "Hồ sơ tư vấn viên phải có số thẻ hành nghề và bản chụp thẻ (Điều 20 Nghị định 77/2008/NĐ-CP)" | ERROR | `fr-04:211` |
| ERR-KT-03 | Chọn Đạt hoặc Yêu cầu bổ sung khi hạng mục 1 không đạt | "Vụ việc không thuộc phạm vi hỗ trợ. Kết luận chỉ có thể là Không đạt" | ERROR | `fr-05:641` |
| ERR-INTG-06 | Xóa vụ việc cầu nối đã tiếp nhận | "Vụ việc đã được tiếp nhận, không xóa được. Để dừng xử lý, sử dụng chức năng kiểm tra hồ sơ và kết luận từ chối" | ERROR | `fr-05:494` |
| ERR-HD-05 | Cán bộ nhập tay kênh `CONG_PLQG` hoặc `TVN_BRIDGE` | "Hai kênh này do hệ thống tự đặt, không nhập tay được" | ERROR | `fr-02:230` |
| ERR-TN-03 | Tiếp nhận: lĩnh vực không thuộc danh mục đang hiệu lực | "Lĩnh vực pháp luật không hợp lệ" | ERROR | `fr-02:367` |
| ERR-TN-04 | Tiếp nhận: một trong ba trường phân loại trỏ sai loại danh mục | "Giá trị phân loại không thuộc danh mục tương ứng" | ERROR | `fr-02:368` |
| ERR-TN-05 | Tiếp nhận: chưa tích ô đối chiếu địa bàn doanh nghiệp | "Vui lòng đối chiếu và xác nhận địa bàn của doanh nghiệp" | ERROR | `fr-02:369` |
| ERR-CL-05 | Tiêu đề hoặc mô tả bị xóa trắng trong hộp thoại chuyển | "Tiêu đề và mô tả không được để trống" | ERROR | `fr-02:1043` |
| ERR-CL-06 | Ghi chú chuyển luồng quá 2.000 ký tự | "Ghi chú chuyển luồng tối đa 2.000 ký tự" | ERROR | `fr-02:1044` |
| ERR-CL-07 | Loại hình hỗ trợ không thuộc danh mục đang hiệu lực | "Loại hình hỗ trợ không hợp lệ" | ERROR | `fr-02:1045` |
| ERR-CL-08 | Chuyển: chưa tích ô đối chiếu địa bàn doanh nghiệp | "Vui lòng đối chiếu và xác nhận địa bàn của doanh nghiệp" | ERROR | `fr-02:1046` |
| ERR-AUTH-CL-02 | Vai trò không phải CB NV gọi chuyển | "Chỉ Cán bộ Nghiệp vụ được chuyển hồ sơ sang vụ việc" | ERROR | `fr-02:1047` |
| ERR-AUTH-GY-01 | Vai trò không phải CB NV gọi gợi ý | "Bạn không có quyền xem gợi ý câu hỏi" | ERROR (403) | `fr-02:1149` |
| ERR-DK-11 | Số thẻ hành nghề quá 50 ký tự | "Số thẻ hành nghề tối đa 50 ký tự" | ERROR | `fr-04:212` |
| ERR-DK-12 | Tệp thẻ hành nghề không phải PDF | "Tệp thẻ hành nghề phải là PDF" | ERROR | `fr-04:213` |
| ERR-DK-13 | Một ô minh chứng vượt 10 tệp | "Mỗi ô tối đa 10 tệp" | ERROR | `fr-04:214` |
| ERR-DK-14 | Số vụ việc tự kê khai là số âm | "Số vụ việc đã tham gia không được là số âm" | ERROR | `fr-04:215` |
| ERR-AUTH-DK-01 | Tư vấn viên tự sửa hồ sơ năng lực của mình | "Hồ sơ năng lực do Người hỗ trợ pháp lý hoặc Cán bộ Nghiệp vụ cập nhật" | ERROR (403) | `fr-04:216` |
| ERR-INTG-07 | Phía gửi tự đặt `hoi_dap_goc_id` khi lập vụ việc | "Liên kết truy nguồn do hệ thống đặt khi chuyển luồng, không nhận từ bên ngoài" | ERROR | `fr-05:492` |
| ERR-KT-04 | Lý do kiểm tra dưới 10 hoặc trên 5.000 ký tự | "Lý do phải từ 10 đến 5.000 ký tự" | ERROR | `fr-05:642` |
| ERR-KT-05 | Phía gửi tự đặt loại lý do từ chối do hệ thống xác định | "Loại lý do từ chối do hệ thống xác định theo kết quả kiểm tra" | ERROR | `fr-05:643` |

Mã có sẵn mở rộng cho `DA_CHUYEN_LUONG`: `ERR-HD-04` khi sửa hoặc xóa đơn lẻ (`fr-02:154`, `:164`), câu "Không thể sửa hoặc xóa hồ sơ đã đóng" (`fr-02:229`); `ERR-DELETE-STATE` khi xóa hàng loạt (`fr-02:232`).

> Kiểm negative phải khớp nguyên văn. Mã lỗi có sẵn dùng lại trong TC (ERR-KT-01/02 `fr-05:639`–`:640`; ERR-DM-01/02/03/05 `fr-10:160`–`:164`; ERR-PH-02 `fr-02:654`; ERR-PC-02 `fr-02:578`; ERR-TN-01 `fr-02:365`; ERR-TH-03 `fr-02:481`; ERR-VV-01 `fr-05:498`; WRN-TB-02 `fr-05:1044`; ERR-RPT-05/08 `fr-11:117`, `:120`; ERR-DN-OWN-02 `fr-07:395`; ERR-DK-05 `fr-04:358` — giới hạn 50 MB tính trên từng ô) có câu nguyên văn trong từng TC.

### 2.3 Phân quyền thao tác mới

| Thao tác | Được làm | Không được | Nguồn |
|---|---|---|---|
| Chuyển hồ sơ hỏi đáp sang vụ việc | CB NV cùng đơn vị hồ sơ | DN, NHT, CB PD, QTHT; CB NV khác đơn vị | `fr-02:939`, `:1843`, `:1042` |
| Tiếp nhận vụ việc cầu nối | CB NV đơn vị thụ lý | CB NV khác đơn vị | `fr-05:2468` |
| Đọc gợi ý câu hỏi tương tự | CB NV | NHT, DN (ô `R` của DN ở ma trận chỉ là quyền đọc dữ liệu) | `fr-02:1083`, `:1093`, `v35:1375`, `:1327` |
| Thêm / sửa / xóa danh mục Hình thức tổ chức | QTHT | Mọi vai trò khác | `fr-10:1631` |
| Đăng ký, cập nhật năng lực TVV | NHT cùng đơn vị | NHT khác đơn vị; TVV tự sửa | `fr-04:300`, `:396`, `:461`, `:394` |
| Thêm / sửa TVV trực tiếp | CB NV | — | `fr-04:126`; loại Tư vấn viên phải có số thẻ và tệp thẻ (`fr-04:149`–`:150`, `:211`, `:221`–`:224`) |
| Báo cáo FR-IX-01 | CB NV, CB PD theo cấp | Vai trò khác, kể cả QTHT | `fr-11:117`, `:120` |

> Chuyển luồng khác đơn vị: hai bên chỉ thấy năm ô thông tin chuyển (mã, trạng thái, ngày chuyển, người chuyển, lý do), không mở được nội dung, tệp, lịch sử hồ sơ của bên kia; cán bộ Trung ương và QTHT mở được cả hai (`fr-02:1024`, `:1028`–`:1032`; `fr-05:1371`–`:1373`, `:1384`; `v35:1564`, `:1602`).

### 2.4 UI Layout

**Hoãn — chưa có giao diện (quyết định 14/09/2026).** Danh sách SCR để bổ sung khi có bản dựng nằm ở mục A từng file.

### 2.5 Máy trạng thái và dữ liệu đổi

**SM-HOIDAP** — thêm `DA_CHUYEN_LUONG` vào enum (`v35:1544`). Hai lối vào: `TIEP_NHAN → DA_CHUYEN_LUONG` (`fr-02:1843`), `DANG_XU_LY → DA_CHUYEN_LUONG` (`fr-02:1844`). Một lối ra: `DA_CHUYEN_LUONG → TIEP_NHAN` — hoàn tác khi vụ việc đích bị xóa lúc còn Chờ tiếp nhận (`fr-02:1804`, `:1845`, `:1049`–`:1062`). Hồ sơ đã chuyển là trạng thái kết thúc về thời hạn (Q13): lúc chuyển xóa mức cảnh báo, bộ đếm dừng; hoàn tác khôi phục thời hạn và mức cảnh báo từ ảnh chụp (`fr-02:1007`, `:1059`; `v35:1553`).

**SM-VUVIEC** — vụ việc cầu nối khởi tạo `CHO_TIEP_NHAN` (`fr-02:1004`), không tính thời hạn lúc tạo (`fr-05:2467`); thời hạn tính từ lúc tiếp nhận (`fr-05:1374`).

**Kênh vụ việc** — thêm `CONG_PLQG` (`v35:1601`); kênh tự động, không có trong ô nhập tay (`v35:1612`).

| Entity | Trường / giá trị mới | Nguồn |
|---|---|---|
| HOI_DAP | `quy_mo_dn_id`, `hinh_thuc_to_chuc_id`, `tinh_thanh_dn_id` — ảnh chụp lúc tiếp nhận | `v35:1541`–`:1543` |
| HOI_DAP | `vu_viec_dich_id` (UNIQUE), `ngay_chuyen_luong`, `deadline_luc_chuyen`, `muc_do_canh_bao_luc_chuyen` | `v35:1564`–`:1567` |
| VU_VIEC | `hoi_dap_goc_id` (UNIQUE) — dấu hiệu duy nhất nhận biết hồ sơ chuyển luồng | `v35:1602` |
| VU_VIEC | `loai_ly_do_tu_choi` — `NGOAI_PHAM_VI` / `THIEU_TAI_LIEU` / `KHAC` (lưu trên vụ việc cùng kết quả kiểm tra từng hạng mục — `v35:1599`–`:1600`, Q09); `huong_dan_gui_lai` | `fr-05:550`, `:1019` |
| DOANH_NGHIEP | `hinh_thuc_to_chuc_id`; `loai_dn_id` đổi nhãn "Quy mô doanh nghiệp", là cột lưu duy nhất của quy mô | `v35:1749`, `:1748` |
| HO_SO_TU_VAN_VIEN | `so_the_hanh_nghe`, `file_the_hanh_nghe`, `file_minh_chung_kinh_nghiem`, `so_vu_viec_tu_ke_khai`, `file_minh_chung_vu_viec` | `v35:2827`–`:2831` |
| DANH_MUC | Loại `HINH_THUC_TO_CHUC`, 7 giá trị mồi; `LOAI_DOANH_NGHIEP` thống nhất tên mã | `v35:3236`, `:3219` |
| FR-IX-01 | Chỉ số `da_chuyen_luong`; mẫu số `ty_le_tra_loi` = tổng − đã chuyển | `fr-11:222`, `:221` |
| Dashboard | KPI-S-03 | `fr-01:632` |

---

## 3. Rủi ro

Điểm = Xác suất × Tác động (mỗi thang 1–3). **≥ 6 là rủi ro cao.** Loại: TECH kỹ thuật · SEC bảo mật · PERF hiệu năng · DATA dữ liệu · BUS nghiệp vụ · OPS vận hành kiểm thử.

| ID | Loại | Rủi ro | P | I | Điểm | Giảm thiểu / TC |
|---|---|---|:-:|:-:|:-:|---|
| **R-01** | DATA | Chuyển luồng không nguyên tử: hai phiên cùng chuyển, hoặc lỗi giữa chừng để lại vụ việc mồ côi / hồ sơ mở mà đã có vụ việc | 2 | 3 | **6** | TC-CL-018, -019 (P0), -034; Edge file 01 |
| **R-02** | BUS | Đếm hoàn thành hai lần (hỏi đáp gốc + vụ việc đích) trên Dashboard / báo cáo | 2 | 3 | **6** | TC-BC01-001, -002 (P0), -007; TC-HQBC-003 (P0), -001; TC-VVCL-018 (P0) |
| **R-03** | BUS | Thời hạn vụ việc cầu nối tính sai mốc (từ lúc chuyển thay vì lúc tiếp nhận) | 2 | 3 | **6** | TC-VVCL-007 (P0), -008, -009; TC-HQHD-016, -017; TC-HQBC-004 |
| **R-04** | BUS | Hồ sơ `DA_CHUYEN_LUONG` vẫn sửa / xóa / trả lời / phân công được — kể cả qua lô hàng loạt hay Cổng gửi lại | 3 | 2 | **6** | TC-HQHD-003 (P0), -004, -005, -020; TC-HQHD-001, -002, -021, -022, -024 |
| R-05 | SEC | Lộ dữ liệu khi đơn vị thụ lý khác đơn vị gốc | 2 | 2 | 4 | TC-CL-005, -023; TC-VVCL-004, -005, -019; TC-BC01-013 |
| **R-06** | TECH | Vụ việc cầu nối kênh `DVC` không có mã hồ sơ DVC → đồng bộ LGSP lỗi hoặc gửi sai | 2 | 3 | **6** | TC-VVCL-016; TC-HQHD-017, -018 |
| **R-07** | BUS | Hệ thống suy loại lý do từ chối sai, hoặc nhận loại lý do do phía gửi đặt | 2 | 3 | **6** | TC-KT-003, -004 (P0), -005, -010, -011, -012, -017, -018 |
| R-08 | DATA | Ba trường ảnh chụp bị đọc động từ hồ sơ DN | 2 | 2 | 4 | TC-PL-007 (P0), -011; TC-BC01-008 (P0); TC-CL-014 |
| **R-09** | BUS | FR-IX-01 xếp trạng thái vào nhóm sai, hoặc xếp hồ sơ vào sai kỳ khi ngày tạo và ngày chuyển khác tháng → tổng / tỷ lệ sai | 3 | 2 | **6** | TC-BC01-001 … -004; TC-BC01-019 (biên giờ đầu / cuối kỳ), -025 |
| R-10 | TECH | Lỗi tra cứu gợi ý chặn tiếp nhận / trả lời | 2 | 2 | 4 | TC-GY-008, -010 (P0) |
| R-11 | PERF | Tra cứu gợi ý chậm, SRS không có NFR | 2 | 1 | 2 | Không có TC; ghi thời gian phản hồi khi chạy TC-GY-001 |
| R-12 | DATA | Xóa / tắt giá trị Hình thức tổ chức đang dùng | 1 | 2 | 2 | TC-HTTC-007 (P0), -008, -010 |
| **R-13** | BUS | CB NV thêm TVV không có thẻ qua FR-IV-01 | 2 | 3 | **6** | TC-THN-022, -023, -026 |
| **R-14** | BUS | Quy tắc không hồi tố áp quá tay: TVV đã duyệt thiếu thẻ bị chặn nhận vụ việc | 2 | 3 | **6** | TC-THN-012, -013, -014 (P0), -025; TC-HQBC-012 |
| R-15 | BUS | KPI-S-03 lọt vào công thức tỷ lệ tuân thủ SLA | 1 | 3 | 3 | TC-KPI3-003 (P0) |
| R-16 | DATA | Dữ liệu cũ còn mã `LOAI_DN` sau khi thống nhất tên mã | 1 | 3 | 3 | TC-HTTC-017, -001 |
| R-17 | BUS | Hồ sơ TVV nộp trước ngày áp dụng, chưa duyệt xong, đi qua thẩm định / phê duyệt mà không bị chặn thiếu thẻ | 2 | 2 | 4 | TC-HQBC-012, -013 |
| **R-18** | OPS | Dữ liệu thử cần ngày tạo / tiếp nhận / hoàn thành cố định (kỳ 07–12/2026) mà API không cho đặt ngày | 3 | 2 | **6** | §7.3 — cần quyền sửa CSDL hoặc chỉnh đồng hồ máy chủ; nếu không có, file 08, 09, 11 chỉ chạy được phần không phụ thuộc ngày. File 11 mục 6 cho chọn DBA chèn thẳng ba hồ sơ chi trả thay cho đi hết luồng chi trả |
| R-19 | OPS | Chỉ kiểm qua API, chưa kiểm được giao diện | 3 | 1 | 3 | Mục A từng file liệt kê SCR để bổ sung |
| R-20 | BUS | Thông báo chuyển luồng gửi thiếu / thừa người nhận | 2 | 2 | 4 | TC-CL-013, -027, -028, -029; TC-HQHD-010 |
| **R-21** | OPS | Dữ liệu SRS không có đường tạo, phải nhờ DBA sửa CSDL: hồ sơ hỏi đáp thiếu lĩnh vực (mọi đường tạo đều bắt buộc lĩnh vực — `fr-02:103`, `fr-16:1168`, `:1183`); bản ghi kho `HET_HIEU_LUC` (không thao tác nào chuyển tới); hồ sơ tư vấn viên thiếu thẻ khi môi trường không còn hồ sơ cũ phù hợp (từ ngày áp dụng, đăng ký và cập nhật năng lực đều bắt buộc thẻ — `fr-04:326`, `:327`, `:466`) | 2 | 3 | **6** | File 04 mục 5 dựng HD-PL-01 cho TC-PL-001, -002, -004; file 05 dựng HD-GY-03 (TC-GY-012) và KQ-X3 (TC-GY-003 bỏ bản ghi này nếu không dựng được); file 02 xóa mềm hồ sơ gốc của VV-VVCL-06a (TC-VVCL-006, nhánh dữ liệu hỏng); file 07 mục 4 và file 11 mục 7 ưu tiên hồ sơ cũ có sẵn, chỉ khi thiếu mới xóa trắng hai trường thẻ (TC-THN-011 … -014, -016, -017, -023 … -025, trong đó ba P0 -012, -013, -014; TC-HQBC-012, -013). Không có DBA → ghi "không dựng được", báo riêng; khi đó ba P0 của file 07 chặn cổng đạt nếu môi trường không có hồ sơ cũ thiếu thẻ |
| **R-22** | DATA | Hoàn tác chuyển luồng sai: hồ sơ gốc không mở lại (kể cả khi xóa **hàng loạt** vụ việc — hồ sơ kẹt vĩnh viễn ở `DA_CHUYEN_LUONG`), thời hạn tính lại từ đầu thay vì khôi phục ảnh chụp, liên kết cũ chặn lần chuyển sau, hoặc xóa được vụ việc cầu nối đã tiếp nhận | 2 | 3 | **6** | TC-VVCL-017, -021, -022, -023, -024, -028, -029, -030; TC-BC01-017, -026; TC-HQHD-005, -014, -026 |
| R-23 | DATA | Hồ sơ kiểm tra theo danh mục 6 hạng mục: mất kết quả cũ, bị bắt tích lại, hệ thống tự điền hạng mục 1, hoặc hồ sơ đã phân công bị chặn | 2 | 2 | 4 | TC-KT-016, -019 |
| **R-24** | OPS | SRS `81b74c6` còn chỗ chưa khớp (FR-II-09 và tab Hoàn thành chưa có `DA_CHUYEN_LUONG` — `fr-02:841`, `:1327`; Chỉnh sửa bước 1 chưa có `CONG_KHAI` — `:154`; hậu điều kiện Xóa của FR-V.I-05 — `fr-05:484`): dev làm theo một chỗ, TC chấm theo chỗ khác → tranh cãi bug | 3 | 2 | **6** | TC chấm theo chỗ SRS ghi rõ nhất, chỗ mâu thuẫn chỉ ghi lại; danh sách ở mục Ghi nhận SRS cuối từng file |

**13 rủi ro cao** (R-01, -02, -03, -04, -06, -07, -09, -13, -14, -18, -21, -22, -24). Không TC nào của các rủi ro này phải chờ BA hay CĐT.

---

## 4. Số lượng test case

| File | Happy | Negative | Edge | Tổng | Chạy ngay |
|---|--:|--:|--:|--:|--:|
| 01 — Chuyển hỏi đáp sang vụ việc | 19 | 9 | 8 | 36 | 36 |
| 02 — Tiếp nhận vụ việc từ hỏi đáp | 12 | 10 | 11 | 33 | 33 |
| 03 — Kiểm tra hồ sơ 7 hạng mục | 9 | 11 | 9 | 29 | 29 |
| 04 — Trường phân loại hỏi đáp | 9 | 6 | 6 | 21 | 15 |
| 05 — Gợi ý câu hỏi tương tự | 7 | 7 | 6 | 20 | 20 |
| 06 — Danh mục hình thức tổ chức | 12 | 12 | 4 | 28 | 27 |
| 07 — Thẻ hành nghề TVV | 14 | 15 | 6 | 35 | 35 |
| 08 — Báo cáo hỏi đáp FR-IX-01 | 15 | 3 | 8 | 26 | 24 |
| 09 — KPI thời gian toàn trình | 6 | 4 | 7 | 17 | 17 |
| 10 — Hồi quy Hỏi đáp, Vụ việc | 4 | 14 | 8 | 26 | 26 |
| 11 — Hồi quy báo cáo, DN, TVV | 12 | 3 | 6 | 21 | 21 |
| **TỔNG** | **119** | **94** | **79** | **292** | **283** |

| Priority | Tổng | Chạy ngay | Chờ CĐT | % tổng |
|---|--:|--:|--:|--:|
| P0 | 53 | 53 | 0 | 18% |
| P1 | 120 | 117 | 3 | 41% |
| P2 | 109 | 104 | 5 | 37% |
| P3 | 10 | 9 | 1 | 3% |

Số đếm theo cột cuối (Loại · Ưu tiên) của từng file.

---

## 5. Nhãn chờ

### 5.1 TC gắn nhãn ở cột Tên — 9 TC không chấm, đều chờ CĐT

Không TC nào chờ BA. 9 TC chờ CĐT:

| Câu | TC | Tình trạng |
|---|---|---|
| H1 (CĐT) | TC-PL-012 … -016, -020 | — |
| A5 (CĐT) | TC-BC01-011, -015 | — |
| T8 (CĐT) | TC-HTTC-012 | — |

### 5.2 Kết quả chính chắc chắn, một ý phụ còn chờ

| Câu | TC | Ý còn chờ |
|---|---|---|
| A5 (CĐT) | TC-BC01-016, -020 | Chiều quy mô, hình thức tổ chức của hồ sơ ẩn danh đã chuyển; nhóm "Không xác định" tính theo từng chiều |

TC-BC01-011 và TC-BC01-015 gắn nhãn A5 ở 5.1 nên không vào bảng này.

### 5.3 Quyết định BA đã vào SRS `81b74c6`

TC chấm theo dòng SRS ở cột ba, không theo thư phản hồi.

| Câu | SRS chốt | Dòng SRS | TC |
|---|---|---|---|
| A1, A2, Q11 | Nhãn `DVC` của hỏi đáp chỉ là nhãn nguồn, không có mã hồ sơ DVC; gửi trạng thái ra ngoài khi và chỉ khi hồ sơ có mã hồ sơ DVC — vụ việc cầu nối không đồng bộ | `fr-02:992`; `fr-05:1029`, `:1048`–`:1049`, `:2468`; `v35:5744` | TC-VVCL-016; TC-HQHD-017 |
| A3, A4 | Hỏi đáp 15 / 30 ngày làm việc; một dòng cấu hình `HOI_DAP` hai cột thời hạn, chọn cột theo `muc_do_phuc_tap` | `fr-10:541`, `:547`, `:549`; `fr-02:147`, `:358` | TC-HQHD-011 |
| Q01 | Vụ việc không giữ ba trường phân loại, tra qua hồ sơ doanh nghiệp; câu hỏi ẩn danh được ghi doanh nghiệp và ba trường vào **chính hồ sơ hỏi đáp gốc** lúc chuyển | `fr-02:982`–`:984`, `:1006`; `fr-05:1382` | TC-CL-014, -016; TC-BC01-016 |
| Q02 | Hồ sơ đã chuyển không sửa, không xóa — xóa đơn lẻ `ERR-HD-04`, xóa hàng loạt `ERR-DELETE-STATE` | `fr-02:164`, `:232`, `:1347`, `:1938`; `v35:1451` | TC-HQHD-001, -002, -021; TC-VVCL-003, -006; TC-KPI3-009 |
| Q03 | Vụ việc cầu nối còn Chờ tiếp nhận xóa được và kéo theo hoàn tác: hồ sơ gốc về `TIEP_NHAN`, bỏ phân công, xóa liên kết, khôi phục thời hạn từ ảnh chụp, giữ doanh nghiệp và ba trường, gửi thông báo đính chính. Đã tiếp nhận thì chặn `ERR-INTG-06`. Chuyển lại được. Xóa ở màn danh sách vụ việc (FR-V.I-01), nhận biết theo liên kết truy nguồn; xóa hàng loạt xử lý từng dòng, không chặn cả lô | `fr-05:127`–`:147`, `:453`–`:454`, `:494`, `:1767`; `fr-02:1049`–`:1062`, `:1072`–`:1074`, `:1804`, `:1845`; `v35:1602` | TC-VVCL-017, -021, -022, -023, -024, -033; TC-BC01-017; TC-HQHD-005, -014, -026 |
| Q04 | (a) Hạng mục 1 không đạt → chỉ còn Không đạt, chọn sai `ERR-KT-03`. (b) Bảy hạng mục đạt mà Không đạt → loại `KHAC`, bắt buộc ghi nội dung. Loại lý do do hệ thống xác định theo thứ tự ưu tiên | `fr-05:550`, `:594`–`:595`, `:641` | TC-KT-010, -011, -012, -017, -018 |
| Q05 | Hạng mục 1 cố định trong hệ thống, không nằm trong UC106; QTHT không thêm / sửa / xóa / đổi thứ tự | `fr-05:590`; `fr-10:437`–`:441` | TC-KT-001, -015 |
| Q06 | `loai_dn_id` là cột lưu và ô nhập duy nhất của quy mô, bỏ cột `quy_mo`; FR-IX-18 gom theo `DOANH_NGHIEP.loai_dn_id` | `fr-07:120`, `:571`, `:695`; `fr-10:1066`, `:1069`; `v35:1748`; `fr-05:2337`; `fr-11:876` | TC-PL-006; TC-HQBC-007, -010, -016 |
| Q07 | FR-IV-01: loại Tư vấn viên bắt buộc số thẻ và tệp thẻ (`ERR-TVV-10`); Chuyên gia không bắt; sửa hồ sơ đã duyệt thiếu thẻ phải bổ sung thẻ, không hồi tố. FR-IV-11 không kiểm thẻ | `fr-04:149`–`:150`, `:211`, `:221`–`:224`, `:427` | TC-THN-022, -023, -025, -026 |
| Q08 | Bảng ba nhóm người nhận thông báo chuyển luồng; chống gửi trùng, ưu tiên vai người được phân công | `fr-02:192`–`:204`, `:1010` | TC-CL-013, -027, -029; TC-HQHD-010 |
| Q09 | Lưu loại lý do từ chối và kết quả kiểm tra từng hạng mục; màn chi tiết hiển thị chỉ đọc | `v35:1599`–`:1600`; `fr-05:1908` | TC-VVCL-012; TC-KT-003, -004, -005, -012, -014, -018, -019 |
| Q10 | (a) Khác đơn vị: hai bên chỉ thấy năm ô thông tin chuyển, không mở hồ sơ bên kia; cùng đơn vị mở chỉ đọc; Trung ương, QTHT mở cả hai. (b) Chọn đơn vị thụ lý trong toàn bộ đơn vị (Trung ương, Bộ ngành, Địa phương) | `fr-02:966`, `:1024`–`:1032`; `fr-05:1371`–`:1373`, `:1378`–`:1384`, `:1854`; `v35:1564`, `:1602` | TC-VVCL-004, -005; TC-CL-005 |
| Q12 | Tập vụ việc `HOAN_THANH` và `DA_DANH_GIA` có ngày hoàn thành trong kỳ, cho cả KPI-S-02 và KPI-S-03; làm tròn một chữ số thập phân; không gồm vụ việc từ chối | `fr-01:615`, `:640`, `:659`, `:662` | TC-KPI3-004, -006, -007, -008, -013; TC-HQBC-004, -015 |
| Q13 | Đã chuyển luồng là trạng thái kết thúc về thời hạn: xóa mức cảnh báo, không gửi thông báo; vào tập "câu hỏi đã xử lý" | `fr-02:897`, `:1007`, `:1059`; `v35:1553` | TC-HQHD-007, -008; TC-CL-011, -036 |
| Q14 | `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH` → Đã trả lời; `MOI` … `CHO_PHE_DUYET` → Chờ trả lời; `DA_CHUYEN_LUONG` → nhóm thứ ba; `HUY` không vào tổng | `fr-11:159`, `:170` | TC-BC01-001 … -004, -006, -007, -009, -012, -013, -017; TC-HQBC-003 |
| Q15 | Mốc bắt đầu = ngày tạo bản ghi vụ việc | `fr-01:668` | TC-KPI3-002, -004, -005, -007, -010 |
| Q16 | FR-IX-02, FR-IX-13 đếm cả vụ việc đã tiếp nhận chưa hoàn thành; mốc "trong kỳ" = ngày tiếp nhận | `fr-11:264`, `:714`, `:729`; `v35:5846` | TC-HQBC-005, -006, -017, -018 |
| Q17 | Nhóm Pháp lý không đạt chỉ khóa Đạt, nhận Yêu cầu bổ sung | `fr-04:1633` | TC-HQBC-012 |
| Q18 | Tổng chi phí = tổng số tiền thực trả; trần = tổng trần của các doanh nghiệp khác nhau trong dòng, theo cấu hình mức hỗ trợ đang áp dụng; chênh lệch = hiệu | `fr-11:897`–`:905`, `:918` | TC-HQBC-008, -019 |
| Q19 | Cả hai biểu mẫu tạo doanh nghiệp nhận Hình thức tổ chức, tùy chọn | `fr-07:287`, `:572`; `fr-10:1067` | TC-HQBC-010; TC-HTTC-002, -013, -016 |
| Q20 | 50 MB tính trên từng ô tệp | `fr-04:325`, `:330`, `:332`, `:358` | TC-THN-008 |
| Q21 | Gợi ý chỉ lấy kho câu hỏi của đơn vị cán bộ; phạm vi toàn quốc là điểm treo | `fr-02:1108`, `:1113`, `:1128` | TC-GY-004, -018 |
| Q22 | Giữ ô lĩnh vực làm đường dự phòng cho hồ sơ ngoại lệ (di trú, dữ liệu lỗi) | `fr-02:337` | TC-PL-001, -002, -004; TC-GY-012 |
| Q23 | Ba trường ảnh chụp tự điền lúc hồ sơ lần đầu xác định được doanh nghiệp, chỉ lấy một lần | `fr-02:116`, `:156` | TC-PL-021 |
| Q24 | Số thẻ hành nghề không ràng buộc duy nhất (lệch có chủ đích; điểm treo) | `fr-04:2188` | TC-THN-027 |
| Q25 | Kỳ theo ngày tạo hồ sơ hỏi đáp; nhóm theo trạng thái lúc chạy báo cáo | `fr-11:172` | TC-BC01-025 |
| Phiếu Dev BA-R2 | Hồ sơ kiểm tra theo danh mục 6 hạng mục: đi vào bước kiểm tra thì bổ sung hạng mục thiếu ở trạng thái chưa tích, giữ kết quả cũ; không đi vào thì giữ nguyên, hiện "Không áp dụng", không chặn xử lý tiếp | `fr-05:591`, `:603`–`:626`, `:1906` | TC-KT-016, -019 |
| D1–D29 (trừ D9, D27) | Sửa tài liệu, BA tiếp nhận toàn bộ | Dấu `[CR-QA-2026-09-15]` trong SRS | D7, D10, D16: mã lỗi và câu ở §2.2; D16: TC-HQHD-001, -002, TC-KPI3-009; D22: TC-KT-029 |

---

## 6. Chiến lược thực thi

**Cách kiểm.** Gọi thao tác qua API bằng phiên cookie của tài khoản test; đọc lại bản ghi qua API chi tiết / danh sách; lớp THÔNG BÁO đối chiếu trong phản hồi API. Nhật ký và thông báo đọc qua API tương ứng.

**Điều kiện vào.**
1. Bản dựng có đợt `CR-GY-2026-09-13`: tra `/api/docs-json` thấy thao tác chuyển luồng (FR-II-11), gợi ý (FR-II-12), danh mục `HINH_THUC_TO_CHUC` (FR-VIII-33). Thiếu → dừng, báo dev.
2. Dữ liệu §7 đã dựng và kiểm theo từng bộ lọc.
3. Cấu hình ngày lễ cho file 09 (02/09, 03/09/2026).

**Thứ tự chạy** — theo phụ thuộc dữ liệu, ưu tiên P0 trước:

| Đợt | Nội dung | Số TC |
|---|---|--:|
| 0 | Dựng dữ liệu §7, kiểm từng bộ lọc | — |
| 1 | P0 theo thứ tự file: 06 → 04 → 05 → 01 → 02 → 03 → 07 → 10 → 08 → 09 → 11 | 53 |
| 2 | P1 chạy được, cùng thứ tự | 117 |
| 3 | P2 / P3 chạy được | 113 |
| 4 | TC chờ CĐT, sau khi CĐT quyết | 9 |

Phụ thuộc chính: file 06 dựng danh mục cho 04, 08, 11; file 01 sinh vụ việc cầu nối cho 02 và 10; file 08, 09, 11 cần kỳ riêng (§7.3). File 05 và 07 độc lập, chạy song song được.

---

## 7. Dữ liệu thử

### 7.1 Yêu cầu theo bộ lọc

Nghiệm thu dữ liệu **theo từng bộ lọc**, không theo tổng số bản ghi (quy tắc seed trong CLAUDE.md).

| Entity | Bộ lọc | Tối thiểu | Dùng ở |
|---|---|---|---|
| HOI_DAP (gắn DN) | Mỗi trạng thái trong 10 trạng thái | ≥ 1 mỗi trạng thái | File 01 (HD-CL-20a … 20g, STP-AG); file 08 (HD-BC-S01 … S10 ở **STP-BNI**, dựng theo bảng nhóm Q14 — `fr-11:159`) |
| HOI_DAP kỳ 10/2026 và 11/2026 | STP-AG 9 hồ sơ (HD-BC-01 … 08, 10), STP-BG 1 (HD-BC-09) ở kỳ 10; HD-BC-11, 12 (STP-AG) và HD-BC-13 (STP-BG, ẩn danh lúc tạo, chuyển rồi hoàn tác) ở kỳ 11. Mỗi hồ sơ có lĩnh vực, doanh nghiệp DN-BC-01 … 06, kênh, trạng thái đúng bảng của file 08 | đúng từng dòng bảng — số báo cáo tính tay từ bảng này | File 08 |
| HOI_DAP (STP-AG) | `DA_CHUYEN_LUONG` theo lối vào: từ `TIEP_NHAN` (HD-DCL-02, 04); từ `DANG_XU_LY` (HD-DCL-01, 03) — hồ sơ mà TC có thể sửa / xóa được có bản riêng | 2 mỗi lối | File 10 |
| HOI_DAP (STP-AG, `DANG_XU_LY`, gắn DN) | Mỗi kênh: `DVC`, `HE_THONG_KHAC`, `TRUC_TIEP`, `CONG_PLQG`, `TVN_BRIDGE` | ≥ 1 mỗi kênh | File 01 (HD-CL-06a, 06b, 06c, 07, 08) |
| HOI_DAP | Ẩn danh (chưa gắn DN) | ≥ 1 ở `DANG_XU_LY`, ≥ 1 ở `MOI` | File 01, 04, 08 |
| VU_VIEC cầu nối (`CHO_TIEP_NHAN`) | Kênh `DVC` (VV-CL-01, VV-VVCL-16, VV-HQ-DVC); `HE_THONG_KHAC` (VV-CL-03, VV-VVCL-17, VV-VVCL-23 — hồ sơ gốc ẩn danh, VV-HQ-HTK); `CONG_PLQG` (VV-CL-02); `TRUC_TIEP` (VV-CL-05 thụ lý STP-BG; VV-VVCL-06a, 06b, 18, 24). Đã tiếp nhận: VV-VVCL-22 (`HE_THONG_KHAC`) | ≥ 1 mỗi kênh; TC làm đổi trạng thái có vụ việc riêng | File 02, 10 |
| VU_VIEC không cầu nối | `TRUC_TIEP` lập tay (VV-TT-01); DVC thật có `ma_ho_so_dvc` (VV-DVC-01); từ hệ thống khác ở `CHO_TIEP_NHAN` (VV-HTK-01a) và `DA_TIEP_NHAN` (VV-HTK-01b) | 1 mỗi loại | File 02, 10 |
| VU_VIEC nhập thủ công (STP-AG, DN `9999999990`, Thuế) | `DA_TIEP_NHAN`: VV-KT-01, 15. `DANG_KIEM_TRA`: VV-KT-03, 04, 05, 07a, 07b, 08, 09, 10, 11, 12, NEG — mỗi TC làm đổi trạng thái có vụ việc riêng | 2 và 11 | File 03 |
| VU_VIEC (STP-AG) | `CHO_TIEP_NHAN`, `DA_PHAN_CONG`, `TU_CHOI`, `YEU_CAU_BO_SUNG`, `HOAN_THANH` (VV-KT-S1 … S5) | 1 mỗi trạng thái | File 03 (TC-KT-013) |
| VU_VIEC kiểm tra theo danh mục 6 hạng mục | `YEU_CAU_BO_SUNG` (VV-KT-16), `DA_PHAN_CONG` giao `nht_01` (VV-KT-19a), `TU_CHOI` (VV-KT-19b) — dựng **trước khi nâng cấp**; không có thì DBA bỏ phần tử hạng mục 1 khỏi kết quả kiểm tra (`fr-05:626`) | 1 mỗi trạng thái | File 03 (TC-KT-016, -019) |
| NHT `nht_01` | Đang hoạt động, có lĩnh vực Thuế | — | File 03 (phân công) |
| KHO_CAU_HOI (Thuế, STP-AG, cùng ý với mẫu M1) | `DA_DUYET` 4, `CONG_KHAI` 3, còn hiệu lực (KQ-T1 … T7) — hơn 5 để danh sách gợi ý luôn đầy | 7 | File 05 |
| KHO_CAU_HOI (M1, STP-AG) — phải bị loại khỏi gợi ý | `NHAP`, `CHO_DUYET`, `HET_HIEU_LUC` (DBA — R-21), `DA_DUYET` tắt hiệu lực, `CONG_KHAI` tắt hiệu lực (KQ-X1 … X5) | 1 mỗi bộ | File 05 (TC-GY-003) |
| KHO_CAU_HOI khác | Lĩnh vực Lao động (KQ-L1); mẫu M2 ở **STP-BG** và **BTP-TW** (KQ-Q1, Q2); mẫu M3 chỉ khớp câu trả lời / từ khóa (KQ-A1, K1) | 1 mỗi bộ | File 05 |
| DANH_MUC Lĩnh vực pháp lý | Lĩnh vực LV0: chưa có bản ghi kho dùng được trên toàn quốc | 1 | File 05 (TC-GY-008) |
| DANH_MUC `HINH_THUC_TO_CHUC` | 7 giá trị mồi; một giá trị chỉ hỏi đáp dùng; một giá trị không ai dùng | đủ 7 + 2 | File 06 |
| DOANH_NGHIEP | Quy mô `SIEU_NHO`, `NHO`, `VUA`; hình thức trống (DN lập trước ngày áp dụng) | ≥ 1 mỗi quy mô; ≥ 1 trống | File 04, 06, 08, 11 |
| Bộ kỳ 12/2026 của STP-AG | DN-X, DN-Y (`NHO`), DN-Z (`VUA`), DN-OLD (lập trước ngày áp dụng, hình thức trống), DN-Q (DN tự đăng ký, `VUA`); HD-B1 … B5 (3 đã chuyển, 1 đang xử lý, 1 hoàn thành); VV-B1 … B4 (3 hoàn thành, 1 chờ tiếp nhận); hồ sơ chi trả CT-X, CT-Y, CT-Z `DA_THANH_TOAN` | đúng từng dòng bảng — số Dashboard và báo cáo tính tay từ bảng này | File 11 |
| TU_VAN_VIEN / HO_SO_TU_VAN_VIEN (STP-AG) | `HOAT_DONG` loại TVV thiếu thẻ (TVV-CU-01, 04; TVV-CU-03 đã công khai, có tài khoản); `HOAT_DONG` đủ thẻ, có tài khoản `tvv_cu_02` (TVV-CU-02); CG không thẻ (CG-CU-01); `YEU_CAU_BO_SUNG` thiếu thẻ (TVV-YCBS-01, 02); `TU_CHOI` thiếu thẻ (TVV-TC-01); `MOI_DANG_KY` thiếu thẻ, do `nht_01` nộp (TVV-DD-01, 02) | 1 mỗi mã; ưu tiên hồ sơ nộp trước ngày áp dụng, thiếu thì DBA xóa trắng hai trường thẻ (R-21) | File 07 mục 4; file 11 mục 7 |

Chi tiết từng bản ghi ở phần "Chuẩn bị dữ liệu" của từng file.

**Bản ghi bổ sung theo file** — chi tiết ở "Chuẩn bị dữ liệu" từng file:

| File | Dữ liệu thêm |
|---|---|
| 01 | DN-CL-05 (`9990010005`, xóa mềm); HD-CL-31 … 36 (chưa phân công, hồ sơ thuộc đơn vị khác, 10 tệp × 20 MB, quá hạn, FK không hợp lệ, chuyển ↔ gửi phản hồi cùng lúc) |
| 02 | VV-VVCL-25, 27, 28, 29, 31, 32; sửa VV-CL-02 và VV-VVCL-17; mục 5 thêm thứ tự chạy |
| 03 | VV-KT-20, 23 … 28; tài khoản thêm `cb_nv_dp_04`, `cb_nv_dp_02`, `cb_nv_tw_01`, `cb_pd_dp_01`; nhóm E mới (vòng bổ sung, giới hạn `so_ngay_bo_sung_toi_da`, quá hạn, đồng thời) |
| 04 | DN-PL-06 (`9990040006`, không quy mô, không hình thức); HD-PL-17 … 21 |
| 05 | Mẫu M4, câu A16, KQ-AUTO (bản ghi kho sinh tự động khi duyệt); HD-GY-16a, 16b, 19, 20a, 20b, 20c |
| 06 | HT-MD, HT-SUA; DN-HT-22 (`9990060022`), DN-HT-25 (`9990060025`) |
| 07 | F-THE-2 (tệp thẻ thứ hai); UV-27 (số thẻ trùng TVV-CU-02 — Q24); TVV-CU-05, -06 (R-21) |
| 08 | Bộ BTP-TW: HD-BC-14a, 14b, 16 (P10), HD-BC-15 (P11); DN-BC-07 (`9990080007`); kỳ Q4 và khoảng P10+P11 (TC-BC01-018); HD-BC-04 chuyển ở P11 sau cùng (TC-BC01-025 — Q25) |
| 09 | STP-BG kỳ 07–09: VV-K7, K8a, K8b, K9, K10 (do `cb_nv_dp_02`); vụ việc lạ của mục 2 dời sang 12/2025 để Tháng "Tất cả" của 2026 sạch. `users.csv` không có NHT của STP-BG — mục 3a dùng `nht_01` (FR-V.I-09 chọn theo lĩnh vực); bản dựng chỉ cho cùng đơn vị thì `qtht_01` tạo tài khoản NHT STP-BG |
| 10 | HD-DCL-05 … 07 (+ VV-DCL-05 … 07, VV-DCL-07 đã tiếp nhận), HD-WL-01/02, HD-PD-22 (Chờ phê duyệt), HD-CPQ-24 qua API nhận hỏi đáp — cần chứng thư mTLS (R-19); mục chuẩn bị 2f, 2g |
| 11 | DN-DK3 (`9990110016`, tự đăng ký trong TC), DN-NQ (`9990110017`, `loai_dn_id` trống — cách 5), VV-NQ (28/12 → 30/12, 2 ngày làm việc; lập trong TC-HQBC-017, làm đổi KPI-02 / KPI-04 / KPI-S-02 nên chạy sau các TC báo cáo khác), TVV-DD-03 (`CHO_PHE_DUYET`, thiếu thẻ) |

### 7.2 Phân kỳ báo cáo — tránh chồng số liệu

| File | Kỳ | Ghi chú |
|---|---|---|
| 09 | 09/2026 (STP-AG); 07–09/2026 (STP-BG) | Kỳ 07/2026 của STP-AG phải rỗng (TC-KPI3-006). Kỳ 08/2026 STP-AG chỉ chứa VV-K6 (kỳ trước của TC-KPI3-008; TC-KPI3-009). STP-BG mỗi kỳ 07, 08, 09 một vụ việc (VV-K7 … K10, TC-KPI3-012 … -015). Ngày lễ 02/09, 03/09. Chỉ đọc kỳ 09 khi ngày máy chủ đã từ 01/10/2026 — tháng hiện tại lấy mốc cuối là thời điểm hiện tại (`fr-01:194`) |
| 08 | 10/2026; 11/2026; Q4/2026 | 11/2026 cho TC-BC01-005 (STP-AG), TC-BC01-016, -017, -026 (STP-BG, HD-BC-13) và HD-BC-15 (BTP-TW). BTP-TW có bộ riêng HD-BC-14a, 14b, 16 ở P10 (TC-BC01-018 … -020, Bảng C). Kỳ Q4 và khoảng P10+P11 chỉ đọc (TC-BC01-018). Trước khi dựng: báo cáo cả hai kỳ của STP-AG, STP-BG, STP-BNI, BTP-TW phải trống |
| 11 | 12/2026 | Không cấu hình ngày lễ trong tháng |

### 7.3 Ngày của dữ liệu

Kỳ 07–08/2026 đã qua; kỳ 10–12/2026 chưa tới (ngày viết 14/09/2026). Hầu hết API tạo bản ghi lấy ngày hiện tại, nên muốn dựng đúng ngày tạo, tiếp nhận, hoàn thành phải: (a) chỉnh ngày trong CSDL sau khi tạo, hoặc (b) chỉnh đồng hồ máy chủ môi trường test, hoặc (c) chạy khi tới kỳ. Chưa có cách nào → file 08, 09, 11 chỉ chạy phần không phụ thuộc ngày (R-18). Cần DBA / Infra xác nhận trước đợt 1.

Báo cáo có thể trả số cũ do cache phía máy chủ — kiểm "Thời điểm tạo" của báo cáo trước khi so số.

---

## 8. Ước lượng

Ước lượng theo khoảng, gồm đọc lại bản ghi và ghi kết quả; chưa gồm log bug.

| Hạng mục | Số lượng | Giờ / TC | Tổng giờ |
|---|--:|---|---|
| Dựng và kiểm dữ liệu §7 (kể cả chỉnh ngày; bộ STP-BG kỳ 07–09, BTP-TW, kho tự sinh) | — | — | 14–24 |
| P0 | 53 | 0,5–1,0 | 27–53 |
| P1 chạy được | 117 | 0,4–0,8 | 47–94 |
| P2 / P3 chạy được | 113 | 0,25–0,5 | 28–57 |
| TC chờ CĐT (sau khi CĐT quyết, gồm viết lại kết quả) | 9 | 0,5–1,0 | 5–9 |
| **Tổng** | | | **121–237 giờ ≈ 15–30 ngày công** |

Ẩn số lớn nhất: cách chỉnh ngày dữ liệu (§7.3); ba điểm treo BA để quyết sau có thể đổi kết quả khi được quyết (Q21 phạm vi kho gợi ý — TC-GY-004; Q24 số thẻ trùng — TC-THN-027; A3 hai dòng thời hạn `VU_VIEC`, `HO_SO_CHI_TRA` còn lệch giữa hai tệp SRS).

---

## 9. Tiêu chí đạt / không đạt

> Tham chiếu: `output/test-strategy.md` §10.

- ✅ **ĐẠT**: 100% P0 đạt (53 / 53) **và** P1 đạt ≥ 90% trên số chạy được (≥ 106 / 117) **và** không còn bug Critical / Major mở trên TC của rủi ro cao (§3).
- ❌ **KHÔNG ĐẠT**: bất kỳ P0 nào không đạt, hoặc P1 dưới 90%.
- TC gắn `⏸ chờ CĐT` **không vào mẫu số**; báo riêng số lượng.
- Lớp ghi **SRS Gap** không chấm đạt / không đạt — ghi hành vi thực tế vào báo cáo để BA chốt. Hệ thống lỗi 5xx ở lớp đó vẫn là bug.
- Khi CĐT quyết và SRS được sửa: TC chuyển sang chạy được, cộng vào mẫu số, tính lại cổng.

---

## 10. SRS Gap và ghi nhận SRS

### 10.1 TC có lớp SRS Gap — 79 TC

Lớp ghi SRS Gap không chấm (§9); chỗ thiếu và câu cần chép ghi ở dòng SRS Gap của từng TC. Các loại gặp: thiếu mã / câu lỗi khi dữ liệu đầu vào sai; thiếu câu từ chối do phân quyền; thiếu câu báo thành công; thiếu câu mẫu cho nội dung thông báo; đồng thời / nguyên tử; định dạng số liệu báo cáo; quy trình SRS chưa nói.

| File | Số TC | TC |
|---|--:|---|
| 01 | 9 | TC-CL-013, -019, -027, -028, -029, -031, -032, -033, -034 |
| 02 | 18 | TC-VVCL-004, -007, -010, -012, -014, -015, -016, -017, -020, -021, -023, -024, -025, -028, -029, -030, -032, -033 |
| 03 | 9 | TC-KT-003, -004, -009, -012, -015, -021, -023, -026, -029 |
| 04 | 14 | TC-PL-001, -002, -003, -005, -006, -007, -008, -011, -012, -014, -015, -016, -017, -021 |
| 05 | 3 | TC-GY-012, -015, -018 |
| 06 | 7 | TC-HTTC-007, -008, -010, -014, -019, -023, -025 |
| 07 | 1 | TC-THN-008 |
| 08 | 6 | TC-BC01-002, -005, -021, -023, -024, -026 |
| 09 | 1 | TC-KPI3-017 |
| 10 | 9 | TC-HQHD-005, -010, -011, -012, -013, -016, -017, -018, -026 |
| 11 | 2 | TC-HQBC-011, -016 |
| **Tổng** | **79** | |

### 10.2 Ghi nhận SRS — không cần BA quyết định

| Ghi nhận | Nguồn | Xử lý trong TC |
|---|---|---|
| TPL-DM-CRUD liệt kê phạm vi không có FR-VIII-33, nhưng FR-VIII-33 tự khai dùng template này | `fr-10:67`, `:1627` | Coi như áp dụng (Edge file 06) |
| `trang_thai` của template là 1 / 0, ràng buộc xóa FR-VIII-33 gọi `VO_HIEU_HOA` | `fr-10:83`, `:1647` | Cùng một ý, không ảnh hưởng kết quả |
| Sót giao diện: ô "Loại hình doanh nghiệp" ở SCR-VIII-08; danh sách tab SCR-VIII-01 vẫn 16 tab | `fr-10:1973`; `fr-10:1682` so với `:1626` | Để lại tới khi có UI |
| Danh sách kênh do hai cơ chế cùng quản | `v35:3228` | Điểm treo có chủ đích, không có TC |
| FR-II-11 trường 3 nêu "Tư vấn / Đại diện / Hỗ trợ khác", danh mục Loại hình hỗ trợ không có "Hỗ trợ khác" | `fr-02:965`; `fr-05:203`; `fr-10:239` | File 01 dùng giá trị có trong danh mục |
| Mã vụ việc `VV-{TINH}-…`: SRS không định nghĩa `{TINH}` cho mọi vụ việc, không riêng vụ việc chuyển sang | `fr-02:1017`; `fr-05:217`; `v35:5722` | Không TC nào kiểm phần `{TINH}` |
| Đầu ra danh sách vụ việc (FR-V.I-01) không có trường cho biết hồ sơ đến từ Hỏi đáp, trong khi huy hiệu "Từ Hỏi đáp" căn theo `hoi_dap_goc_id` *(đợt này)* | `fr-05:153`–`:163`, `:1823`, `:1369` | TC-VVCL-001, -002 kiểm ở chi tiết vụ việc |
| Thông báo khi doanh nghiệp bổ sung hồ sơ gửi "CB NV phụ trách" — SRS không nói người phụ trách là ai *(có từ trước)* | `fr-05:1455` | TC-VVCL-020 dùng người vừa tiếp nhận vừa kiểm tra; người nhận khác thì ghi lại |
| Thời điểm tính hạn xử lý hỏi đáp: FR-II-01 tính khi tạo, FR-II-03 chỉ tính "nếu chưa tính", tiêu chí chấp nhận và bảng thuộc tính lấy ngày tiếp nhận *(có từ trước)* | `fr-02:147`, `:358`, `:387`; `v35:1552` | File 04, 10 tạo và tiếp nhận trong cùng ngày |
| Kho câu hỏi: không thao tác nào đưa bản ghi vào `HET_HIEU_LUC` *(có từ trước)* | `fr-13:103`, `:118`, `:538`, `:699` | KQ-X3 dựng bằng DBA (R-21) |
| Bộ đếm `so_vu_viec_da_xu_ly` không FR nào nói tăng khi nào *(có từ trước)* | `fr-04:2113`; `v35:1842`; `fr-04:331`, `:1571` | TC-THN-010 chỉ kiểm hai số lưu tách nhau |
| FR-IX-01: chỉ ô lọc lĩnh vực có tiêu chí chấp nhận; ô lọc 2–5 không có *(đợt này)* | `fr-11:151`–`:155`, `:238` | File 08 áp cùng cách hiểu cho mọi ô lọc |
| Hai cách viết BR-SLA-05: bản chung chỉ lấy vụ đã hoàn thành ở mẫu số, bản Dashboard thêm vụ đang xử lý đã quá hạn *(có từ trước)* | `v35:5784`; `fr-01:1211` | TC-KPI3-003 chọn dữ liệu cho cùng một số ở cả hai cách |
| FR-I-08 có điều kiện "có kết quả đánh giá đã chấm trong kỳ" — tỷ lệ tuân thủ thời hạn có thể không hiện *(có từ trước)* | `fr-01:431`, `:448` | TC-KPI3-003 ghi "không chạy được" cho bước đọc tỷ lệ nếu gặp |
| Ô lọc trạng thái SCR-II-01 và bảng trạng thái SM-HOIDAP chưa có `DA_CHUYEN_LUONG` *(đợt này)* | `fr-02:1330`, `:1818`–`:1827`, `:1852`; `v35:1544` | TC-HQHD-006 lọc qua API |
| FR-II-08 Từ chối: bước xử lý không kiểm trạng thái, chỉ tiền điều kiện đòi `CHO_PHE_DUYET` *(có từ trước)* | `fr-02:747`–`:749`, `:695`, `:740` | TC-HQHD-020 kiểm Từ chối trên hồ sơ đã chuyển bị chặn |
| FR-V.III-NEW-02 đòi doanh nghiệp đăng nhập VNeID; FR-VIII-22 cho đăng nhập bằng MST + mật khẩu và dùng đủ chức năng *(có từ trước)* | `fr-07:356`; `fr-10:1130` | TC-HQBC-011 chạy bằng MST + mật khẩu; bị chặn vì chưa có VNeID thì ghi Không test được |
| Báo cáo hỏi đáp dùng ảnh chụp lúc hồ sơ lần đầu xác định được doanh nghiệp (Q23), còn báo cáo vụ việc (FR-IX-13, FR-IX-18) đọc quy mô **hiện tại** của doanh nghiệp — lý do đặt ảnh chụp (doanh nghiệp lớn lên làm sai thống kê kỳ cũ) không áp cho vụ việc. BA đã tự nêu chỗ khác mốc này *(đợt này)* | `fr-11:204`, `:876`; `fr-02:126`, `:984` | TC-HQBC-014 chấm theo quy mô hiện tại, kể cả kỳ đã khép |

Bảng trên gom các điểm chung; danh sách đủ ở mục Ghi nhận SRS cuối từng file. Không điểm nào cần BA quyết định: TC chấm theo chỗ SRS quy định rõ, chọn dữ liệu chấm được với mọi cách hiểu, hoặc chỉ ghi lại giá trị thực tế.

---

## 11. Cấu trúc thư mục

```
output/Update_cai-tien/
├── BA_confirm/
│   ├── ba-confirmation-needed-cr-gy-2026-09-14.md          ← Q01–Q08, G1–G3 (BA đã trả lời)
│   ├── ba-confirmation-needed-cr-gy-2026-09-14-bo-sung.md  ← hỏi thêm Q03 / Q06 / Q07, Q09–Q25, D1–D29 trừ D9, D27 (BA đã trả lời)
│   ├── phan-hoi-cau-hoi-qa-2026-09-14.md                   ← BA trả lời Q01–Q08 (đã vào SRS)
│   ├── phan-hoi-cau-hoi-dev-2026-09-14.md                  ← BA trả lời BA-R1, BA-R2 của Dev (đã vào SRS)
│   └── phan-hoi-phieu-dev-qa-2026-09-15.md                 ← BA chốt A1–A4 và mọi câu còn lại của file bổ sung (đã vào SRS `81b74c6`)
└── Testcase/
    ├── 00-test-plan-overview.md                  ← File này
    ├── 01-TC-chuyen-hoi-dap-sang-vu-viec.md      ← Phần 1 · T1 · FR-II-11
    ├── 02-TC-tiep-nhan-vu-viec-tu-hoi-dap.md     ← Phần 1 · T1 · FR-V.I-18
    ├── 03-TC-kiem-tra-ho-so-7-hang-muc.md        ← Phần 1 · T2 · FR-V.I-06
    ├── 04-TC-truong-phan-loai-hoi-dap.md         ← Phần 1 · T3 · FR-II-01, FR-II-03
    ├── 05-TC-goi-y-cau-hoi-tuong-tu.md           ← Phần 1 · T7 · FR-II-12
    ├── 06-TC-danh-muc-hinh-thuc-to-chuc.md       ← Phần 1 · T3 · FR-VIII-33, FR-V.III-01
    ├── 07-TC-the-hanh-nghe-tvv.md                ← Phần 1 · T6 · FR-IV-01, FR-IV-03, FR-IV-04
    ├── 08-TC-bao-cao-hoi-dap-FR-IX-01.md         ← Phần 1 · T4 · FR-IX-01
    ├── 09-TC-kpi-thoi-gian-toan-trinh.md         ← Phần 1 · T5 · KPI-S-03
    ├── 10-TC-hoi-quy-hoi-dap-vu-viec.md          ← Phần 2 · Hỏi đáp, Vụ việc
    └── 11-TC-hoi-quy-bao-cao-danh-muc-tvv.md     ← Phần 2 · Dashboard, báo cáo, DN, TVV
```

Mỗi file TC kết thúc bằng mục **Edge Case Hunter** (🔴 cao · 🟡 vừa · 🟢 thấp) — ca biên chưa thành TC, kèm lý do.

---

## 12. Tham chiếu

- `docs/phuong-an-cap-nhat-srs-2026-09-10.md` — phạm vi đợt cập nhật
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — SRS chốt, commit `81b74c6`; grep `CR-GY-2026-09-13` (đợt góp ý), `CR-QA-2026-09-14` (BA trả lời phiếu QA), `CR-DEV-2026-09-14` (BA trả lời phiếu Dev), `CR-QA-2026-09-15` / `CR-DEV-2026-09-15` (BA chốt 15/09) để thấy chỗ đổi
- [output/template/test-case-template.md](../../template/test-case-template.md) — template TC
- [output/template/test-plan-overview-template.md](../../template/test-plan-overview-template.md) — template file này
- [output/test-strategy.md](../../test-strategy.md) — chiến lược tổng thể, cổng đạt
- [output/permission-matrix.md](../../permission-matrix.md) — ma trận phân quyền
- [input/users.csv](../../../input/users.csv) — tài khoản test
- [BA_confirm/](../BA_confirm/) — câu hỏi BA và ba bản phản hồi (phiếu QA, phiếu Dev 14/09; quyết định chốt 15/09)
