# Audit 44 FAIL — Hợp đồng tư vấn vs SRS 3.5

Nguồn testcase: `output/bao-cao-tong-hop-qa/report-dot-3.xlsx`, sheet `17. Hợp đồng tư vấn`

Nguồn SRS mới nhất: `input/srs-update-2026-5-5/srs-fr-14-hop-dong-tv.md`, `input/srs-update-2026-5-5/srs-v3.5.md`

Ngày audit: 2026-06-25

## Kết luận nhanh

| Nhóm | Số case | Kết luận |
|---|---:|---|
| FAIL đúng theo SRS mới | 25 | Giữ FAIL. Đây là lỗi implementation/behavior hiện tại. |
| FAIL chưa đủ căn cứ / cần chạy lại đúng ngữ cảnh hoặc seed đúng data | 15 | Không nên coi là bug cuối cùng nếu chưa rerun. |
| Testcase kỳ vọng vượt SRS hoặc SPEC-CLARIFY | 4 | Không nên để FAIL; cần đổi thành clarify/blocked hoặc sửa expected. |

## Căn cứ SRS chính

- SRS FR-X.3-01 quy định CRUD HĐ tư vấn gồm thông tin chung, mốc tiến độ, thanh toán giai đoạn, liên kết vụ việc. CB NV TW/BN/ĐP có CRUD đầy đủ theo đơn vị; TVV/CG chỉ xem theo nhân thân.
- Input bắt buộc: `ten_hop_dong`, `ben_a`, `ben_b`, `gia_tri_hop_dong`, `thoi_han_bat_dau`, `thoi_han_ket_thuc`.
- Mốc tiến độ có `ten_moc`, `ngay_du_kien`, `trang_thai_moc`; default `CHUA_BAT_DAU`.
- Thanh toán giai đoạn có `giai_doan`, `so_tien`, `trang_thai_tt`; default `CHUA_THANH_TOAN`.
- Processing yêu cầu tạo/cập nhật HĐ + mốc + thanh toán, liên kết VV many-to-many, audit thao tác.
- Xuất Excel áp dụng filter hiện tại nhưng template còn GAP-X.3-02.
- FR-X.3-02 yêu cầu search theo keyword trên tên HĐ, mã HĐ, bên B; TVV; khoảng ngày; AND logic; phân trang.
- SRS v2.1/BA 2026-05-11: HĐ tư vấn không còn menu/route standalone public. Luồng chính là từ chi tiết Vụ việc hoặc TVV; route standalone nếu có chỉ là route ẩn/guard.

## Phân loại 44 FAIL

| Row | ID | Verdict | Nguyên nhân |
|---:|---|---|---|
| 44 | TC-HDTV-004 | Cần rerun/sửa TC | SRS mới không coi `/hop-dong-tv/danh-sach` là route public. Danh sách/phân trang vẫn hợp lệ nhưng phải verify trong ngữ cảnh VV/TVV/drawer, không phải endpoint no-context trả 403. |
| 47 | TC-HDTV-010 | FAIL đúng SRS | SRS yêu cầu `ERR-HDTV-01` + message tiếng Việt. Evidence trả `422 ERR-VAL-SYS-00-01`, message tiếng Anh `tenHopDong should not be empty`. |
| 55 | TC-HDTV-023 | Chưa đủ căn cứ | SRS yêu cầu `ben_a` auto theo đơn vị. Evidence dùng CB_DP nhưng TVV seed thuộc TW nên POST trả lỗi validation chủ thể; chưa chứng minh `ben_a` DP sai. Cần seed TVV/CG thuộc AG rồi rerun. |
| 58 | TC-HDTV-026 | SPEC-CLARIFY / expected vượt SRS | SRS chỉ ghi `file_dinh_kem=file[]`, upload nhiều file. Không quy định extension/size. Kỳ vọng reject `.exe`/`>20MB` là hợp lý bảo mật nhưng chưa có trong FR-14. |
| 60 | TC-HDTV-028 | Chưa đủ căn cứ | SRS yêu cầu Export Excel theo filter/scope, nhưng evidence hiện chưa chạy được export trong đúng ngữ cảnh. Cần test UI/drawer hoặc endpoint export thực tế. |
| 61 | TC-HDTV-029 | Chưa đủ căn cứ | Tương tự row 60. SRS có `Áp dụng filter hiện tại`, nhưng chưa có evidence export file với filter TVV + ngày. |
| 66 | TC-HDTV-034 | SPEC-CLARIFY | SRS ghi `ghi_chu` text long nhưng không quy định max. Actual reject 5000 ký tự với max 2000. Không thể FAIL nếu expected là "lưu OK"; cần BA chốt max length. |
| 67 | TC-MTD-001 | FAIL đúng SRS | SRS yêu cầu mốc tiến độ lưu được. PATCH trả 200 nhưng `GET final` vẫn `mocTienDos=[]`, tức không persist. |
| 68 | TC-MTD-002 | FAIL đúng SRS | SRS yêu cầu cập nhật trạng thái mốc + ngày thực tế. Actual không persist mốc. |
| 69 | TC-MTD-003 | FAIL đúng SRS | SRS yêu cầu quản lý mốc trong JSON array. Actual array không persist nên không có cơ sở xóa/cập nhật đúng. |
| 70 | TC-MTD-010 | FAIL đúng SRS | SRS yêu cầu `ten_moc` bắt buộc. Actual PATCH với `tenMoc=""` trả 200 và không báo lỗi nghiệp vụ. |
| 71 | TC-MTD-011 | FAIL đúng SRS | SRS yêu cầu `ngay_du_kien` bắt buộc. Cần reject khi trống; implementation hiện không có evidence validate/persist đúng. |
| 72 | TC-MTD-020 | FAIL đúng SRS | SRS default `trang_thai_moc=CHUA_BAT_DAU`. Actual không persist mốc nên default không kiểm chứng được. |
| 73 | TC-MTD-021 | FAIL đúng SRS | SRS không cấm hoàn thành sớm; mốc phải lưu. Actual mốc không persist. |
| 74 | TC-MTD-022 | FAIL đúng SRS | SRS enum mốc chỉ gồm `CHUA_BAT_DAU/DANG_THUC_HIEN/HOAN_THANH`. Actual `trangThaiMoc=HUY` trả 200, không reject enum invalid. |
| 75 | TC-MTD-023 | FAIL đúng SRS | SRS yêu cầu mốc là JSON array; thứ tự chỉ verify được khi persist. Actual không persist. |
| 76 | TC-TTGD-001 | FAIL đúng SRS | SRS yêu cầu thêm thanh toán giai đoạn. PATCH trả 200 nhưng `GET final` vẫn `thanhToans=[]`. |
| 77 | TC-TTGD-002 | FAIL đúng SRS | SRS cho phép tổng thanh toán <= giá trị HĐ. Actual thanh toán không persist. |
| 78 | TC-TTGD-003 | FAIL đúng SRS | SRS progress = SUM đã thanh toán / giá trị. Actual patch paid trả 200 nhưng `tienDoTt=0`, `thanhToans=[]`. |
| 79 | TC-TTGD-010 | FAIL đúng SRS | SRS yêu cầu reject tổng thanh toán > giá trị HĐ với `ERR-HDTV-03`. Actual over value trả 200. |
| 80 | TC-TTGD-011 | FAIL đúng SRS | `so_tien` là money bắt buộc; zero/invalid cần block theo logic thanh toán. Actual `soTien=0` trả 200. |
| 81 | TC-TTGD-012 | FAIL đúng SRS | SRS yêu cầu `giai_doan` bắt buộc. Actual `giaiDoan=""` trả 200. |
| 82 | TC-TTGD-020 | FAIL đúng SRS | SRS yêu cầu progress bar 100% khi all paid và tổng = giá trị. Actual thanh toán không persist/progress không đổi. |
| 83 | TC-TTGD-021 | FAIL đúng SRS | SRS yêu cầu quản lý thanh toán giai đoạn trong JSON array. Actual không persist array. |
| 84 | TC-TTGD-022 | FAIL đúng SRS | SRS yêu cầu tổng thanh toán <= giá trị HĐ. Khi giảm giá trị xuống dưới tổng phải reject. Actual không enforce được theo evidence. |
| 85 | TC-TTGD-023 | FAIL đúng SRS | Boundary tổng = giá trị cần PASS, nhưng actual không persist thanh toán/progress. |
| 86 | TC-TTGD-024 | FAIL đúng SRS | SRS yêu cầu progress chỉ tính DA_THANH_TOAN. Actual progress không update do thanh toán không persist. |
| 88 | TC-LVV-002 | Chưa đủ căn cứ | SRS yêu cầu liên kết VV many-to-many. Case hợp lệ, nhưng chưa có evidence live cho 1 VV link nhiều HĐ. Cần seed 2 HĐ + 1 VV rồi rerun. |
| 89 | TC-LVV-003 | Chưa đủ căn cứ | SRS có accordion VV liên kết + bỏ liên kết. Chưa có evidence live unlink 1 VV khỏi HĐ. |
| 92 | TC-LVV-020 | Chưa đủ căn cứ | Idempotent/unique junction hợp lý theo N:N, nhưng SRS không ghi rõ UI disabled/UPSERT. Cần rerun hoặc clarify mức expected. |
| 93 | TC-LVV-021 | Chưa đủ căn cứ | SRS có audit cho liên kết VV, nhưng chưa có evidence unlink audit riêng. Case hợp lệ để test, chưa đủ chứng minh FAIL. |
| 94 | TC-LVV-022 | Chưa đủ căn cứ | SRS có soft delete và BR-DATA-01, nhưng case cascade VV soft-delete -> hide khỏi HĐ cần seed VV soft-deleted. Chưa có evidence trực tiếp. |
| 97 | TC-LVV-025 | SPEC-CLARIFY | Testcase tự ghi rõ chưa rõ scope: theo VV owner hay HĐ owner. SRS nói BR-AUTH-08 theo `don_vi_id`, nhưng không nói rõ với back-ref VV có nhiều HĐ khác đơn vị. Cần BA chốt trước khi FAIL. |
| 98 | TC-HDTV-HDTK-001 | FAIL đúng SRS | SRS yêu cầu keyword tìm trên tên/mã/bên B. Evidence keyword context trả total không đổi, keyword không lọc đúng. |
| 100 | TC-HDTV-HDTK-003 | Chưa đủ căn cứ | SRS yêu cầu lọc khoảng ngày nhưng testcase còn tự ghi rõ chưa rõ lọc theo ngày nào. Probe date-combo hết session 401. Cần rerun + BA chốt trường ngày nếu cần. |
| 102 | TC-HDTV-HDTK-011 | FAIL đúng SRS | SRS yêu cầu no-result hiển thị `INF-HDTV-TK-01`. Evidence `keyword=ZZZ_NOT_EXIST` vẫn trả 3 records. |
| 103 | TC-HDTV-HDTK-020 | Chưa đủ căn cứ | SRS yêu cầu ĐP chỉ thấy dữ liệu đơn vị mình. Evidence DP query TVV TW trả 0, phù hợp isolation; chưa seed HĐ AG để chứng minh danh sách AG đúng. |
| 104 | TC-HDTV-HDTK-021 | Chưa đủ căn cứ | SRS yêu cầu AND logic. Evidence keyword đang fail, date-combo 401. Cần rerun combo sau khi token mới và data đủ. |
| 105 | TC-HDTV-HDTK-022 | Chưa đủ căn cứ | SRS yêu cầu pagination 20/page, nhưng data context chỉ có 3 records. Không đủ để fail boundary 21+ records. |
| 106 | TC-HDTK-023 | FAIL đúng SRS | SRS yêu cầu keyword theo tên HĐ, mã HĐ, bên B. Evidence keyword không lọc, total không đổi. |
| 107 | TC-HDTK-024 | FAIL đúng SRS | SQL payload phải được xử lý như literal và không return all rows. Evidence payload vẫn trả total=3 như all context records. |
| 108 | TC-HDTK-025 | SPEC-CLARIFY | SRS không chốt collation có dấu/không dấu. Có thể test Unicode có dấu, nhưng phần expected không dấu cần BA chốt. |
| 110 | TC-HDTV-PERM-001 | Chưa đủ căn cứ | SRS mới không dùng route/menu standalone public. API create TW có evidence PASS, nhưng UI button trong drawer chưa verify. Không nên giữ FAIL từ route standalone. |
| 122 | TC-PERM-023 | Chưa đủ căn cứ | SRS cho CB_NV_BN CRUD scope BN. Evidence dùng TVV TW nên POST BN trả validation 404; thiếu TVV/CG BN để test đúng. |

## Bug thật nên giữ ưu tiên

1. Mốc tiến độ và thanh toán giai đoạn không persist dù PATCH trả 200.
2. Validation nested array thiếu: mốc trống/enum invalid, thanh toán vượt giá trị, zero amount, giai đoạn trống.
3. Keyword search không lọc trong ngữ cảnh TVV, no-result và SQL payload đều trả records.
4. Error code/message tên HĐ trống không đúng SRS.

## Case nên chỉnh lại trong Excel/testcase

- Các case route/list/permission dùng "truy cập Quản lý HĐ tư vấn" cần ghi rõ ngữ cảnh: từ chi tiết Vụ việc hoặc chi tiết TVV, không dùng route public standalone.
- Các case DP/BN cần seed TVV/CG cùng đơn vị trước khi tạo HĐ.
- Các case export cần chạy UI hoặc endpoint export đúng ngữ cảnh, vì SRS vẫn yêu cầu export theo filter nhưng template là GAP-X.3-02.
- Các case file upload, ghi chú long, collation, scope back-ref multi-unit cần chuyển sang SPEC-CLARIFY nếu BA chưa chốt.
