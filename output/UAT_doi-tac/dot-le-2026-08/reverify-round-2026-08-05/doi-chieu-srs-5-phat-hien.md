# Đối chiếu đặc tả — 5 phát hiện ngoài phạm vi (re-verify 05/08/2026)

**Nguồn đặc tả duy nhất dùng cho toàn bộ file này:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
(các bản `input/srs-update-2026-5-5/`, `input/srs-v3/`, thư mục tên `srs-v4` **không** được dùng — lệch cả số dòng lẫn nội dung).

**Cách làm:** với mỗi phát hiện, mở phần đặc tả **màn hình (SCR-*)** của chính màn đó trước, rồi mới đọc FR / entity / business rule / quy ước chung. Mọi trích dẫn đều mở file đọc trực tiếp, ghi `<file>:<dòng>`.

**Đã tra `tasks/srs-contradictions.md`:** 10 entry hiện có (SRS-C-001 → SRS-C-010) **không** entry nào chạm 5 chủ đề dưới đây → không phải ghi "depends on BA decision".

---

## PH-1 — Ngày tiếp nhận mặc định bị chính hệ thống từ chối

**Màn hình / chức năng:** Nhu cầu / Yêu cầu hỗ trợ — biểu mẫu Thêm mới / Nhập thủ công hồ sơ vụ việc (nhóm "Thông tin tiếp nhận").

### Kết luận: **LÀ LỖI**

### Căn cứ

**1) Đặc tả màn hình quy định rõ giá trị mặc định của ô — và ô là bắt buộc:**

`srs-fr-05-vu-viec.md:1698`
> | 19 | accordion-4 | ngay_tiep_nhan | C11 DatePicker | Bắt buộc. Mặc định: ngày hiện tại. Common Approval Fields §3.2.0.8 | — | Luôn |

**2) Nhóm trường dùng chung mà dòng trên trỏ tới cũng nói đúng như vậy, kèm "cho phép sửa":**

`srs-v3.5.md:936`
> | ngay_tiep_nhan | datetime | Yes | Mặc định ngày hiện tại, cho phép sửa | Ngày CB NV tiếp nhận |

**3) Đặc tả dữ liệu KHÔNG có ràng buộc nào về ngày tương lai / ngày hiện tại cho trường này** (cột "Ràng buộc nghiệp vụ" để trống):

`srs-fr-05-vu-viec.md:2023`
> | ngay_tiep_nhan | datetime | N | | | Ngày tiếp nhận |

**4) Bảng lỗi của chính chức năng nhập thủ công chỉ có 4 tình huống lỗi, không có tình huống nào về ngày:**

`srs-fr-05-vu-viec.md:358-362` — E1 "Nội dung yêu cầu là bắt buộc" (ERR-NH-01) · E2 "Mã số thuế không hợp lệ" (ERR-NH-02) · E3 file vi phạm (ERR-NH-03) · E5 thiếu lý do ưu tiên (ERR-NH-05). E4 đã bị bỏ. **Không có mã lỗi nào về ngày tiếp nhận.**

**5) Đặc tả có thói quen viết rõ ràng buộc "không được ở tương lai" khi thực sự muốn — và đã KHÔNG viết cho ô này.** Hai ví dụ ràng buộc cùng dạng ở nhóm khác:

`srs-fr-04-chuyen-gia-tvv.md:140`
> | 4 | ngay_sinh | date | Y | ≤ ngày hiện tại | — | Người dùng |

`srs-fr-04-chuyen-gia-tvv.md:1053`
> | 7 | ngay_cap_dkhd | date | **Y** | Bắt buộc, ≤ ngày hiện tại `[BA chốt 2026-08-04]` | — | Người dùng |

Đã rà toàn bộ 16 file FR của bản v3.5 với các từ khóa "tương lai", "quá khứ", "ngày hiện tại", "không được lớn hơn": **không có dòng nào đặt ràng buộc tương lai cho ngày tiếp nhận vụ việc.**

**6) Hệ quả nghiệp vụ — sai mốc tính thời hạn:**

`srs-fr-05-vu-viec.md:343`
> | 8 | Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1) | BR-SLA-01 |

Ghi lùi ngày tiếp nhận 1 ngày ⇒ ngày tiếp nhận lưu sai so với thực tế **và** thời hạn xử lý 15 ngày làm việc bị lệch 1 ngày so với mốc luật định.

> **Không phải "spec mâu thuẫn":** đặc tả chỉ nói một điều (mặc định = ngày hiện tại, bắt buộc, không cấm). Mâu thuẫn nằm ở phần mềm — tự điền một giá trị rồi tự từ chối chính giá trị đó.

### Câu mô tả để ghi lên sheet

- Biểu mẫu tạo hồ sơ vụ việc điền sẵn ô "Ngày tiếp nhận" bằng ngày hôm nay; giữ nguyên giá trị mặc định đó rồi bấm Lưu thì hệ thống chặn với lý do ngày không được ở tương lai, phải lùi lại một ngày mới lưu được.
- Theo đặc tả màn hình nhập hồ sơ (`srs-fr-05-vu-viec.md:1698`) và nhóm trường tiếp nhận dùng chung (`srs-v3.5.md:936`), ô này là **bắt buộc** và **mặc định bằng ngày hiện tại**; đặc tả dữ liệu (`srs-fr-05-vu-viec.md:2023`) và bảng lỗi của chức năng (`srs-fr-05-vu-viec.md:358-362`) **không** đặt ràng buộc nào cấm ngày tiếp nhận bằng ngày hiện tại.
- Yêu cầu nghiệp vụ: khi cán bộ mở biểu mẫu và giữ nguyên ngày tiếp nhận mặc định, hệ thống phải lưu được hồ sơ ngay trong ngày làm việc.
- Ảnh hưởng: cán bộ buộc phải ghi lùi ngày tiếp nhận so với thực tế, kéo theo thời hạn xử lý 15 ngày làm việc (tính từ ngày tiếp nhận, `srs-fr-05-vu-viec.md:343`) bị lệch so với mốc luật định.

### Mức độ đề xuất: **Major**

Mọi hồ sơ nhập trong ngày đều bị ghi sai ngày tiếp nhận và sai mốc thời hạn xử lý; đây là mốc có căn cứ pháp lý (NĐ 55/2019 Điều 8 Khoản 1), không phải vấn đề thẩm mỹ giao diện.

---

## PH-2 — 19/41 hồ sơ trống cột "Cảnh báo thời hạn"

**Màn hình / chức năng:** Thống kê / Danh sách hồ sơ yêu cầu hỗ trợ pháp lý (màn danh sách vụ việc HTPL).

### Kết luận: **LÀ LỖI** — nhưng lỗi nằm ở **dữ liệu nền thiếu thời hạn xử lý**, KHÔNG nằm ở cột "Cảnh báo thời hạn"

Nói cách khác: **để trống cột cảnh báo khi hồ sơ chưa có thời hạn xử lý là hành vi chấp nhận được**; cái sai là những hồ sơ **đã qua bước tiếp nhận** mà vẫn không có thời hạn xử lý (và không có tên doanh nghiệp).

### Căn cứ

**1) Cột cảnh báo được đặc tả với 4 mức, điều kiện hiển thị "Luôn":**

`srs-fr-05-vu-viec.md:1656`
> | 21 | table | Cảnh báo thời hạn | C07 | 4 mức màu: 🟢 BINH_THUONG / 🟡 SAP_HET / 🔴 QUA_HAN / ⚫ QUA_HAN_NGHIEM_TRONG (80px) | — | Luôn |

**2) Mức cảnh báo là đại lượng dẫn xuất từ thời hạn xử lý — thiếu thời hạn thì không tính được:**

`srs-fr-05-vu-viec.md:1664`
> - SLA cảnh báo tính realtime: >50% thời hạn còn lại = 🟢, ≤50% = 🟡, >100% quá hạn = 🔴, >200% = ⚫. Ngưỡng cấu hình qua MH-10.7 tab SLA (UC108)

`srs-fr-05-vu-viec.md:2456` (BR-CALC-03)
> Mức cảnh báo tính theo công thức `(NOW() - ngay_tiep_nhan) / deadline * 100`. Scheduled job CROSS-01 chạy mỗi 30 phút để cập nhật mức cảnh báo VU_VIEC theo BR-SLA-02.

**3) Đặc tả nhóm Vụ việc KHÔNG quy định hiển thị gì khi thiếu thời hạn xử lý.** Hai căn cứ gián tiếp cho thấy để trống là hợp lệ:

- Quy ước dữ liệu chung — `srs-v3.5.md:957`
  > | DG-03 | Cột trống | Hiển thị `_` (gạch dưới) |
- Module tương đương (Hỏi đáp) đặc tả thẳng hành vi này — `srs-fr-02-hoi-dap.md:1043`
  > … Nếu `han_xu_ly = NULL` → "—". … | khi có thời hạn xử lý |

**4) Nhưng theo đặc tả, hồ sơ đã vào luồng xử lý BẮT BUỘC phải có thời hạn xử lý.** Thời hạn được tính tự động ngay khi hồ sơ vào trạng thái "Chờ tiếp nhận", ở mọi kênh:

`srs-fr-05-vu-viec.md:2284-2285` (bảng chuyển trạng thái SM-VUVIEC)
> | MOI_TAO | CHO_TIEP_NHAN | Auto hoặc CB NV xử lý | — | **Tính deadline**, audit | FR-V.I-03/04/05 | BR-SLA-01 |
> | [*] | CHO_TIEP_NHAN | DVC/HT khác/Trực tiếp | — | Tạo VV, sinh mã, **tính deadline** | FR-V.I-03/04/05 | BR-SLA-01 |

`srs-fr-05-vu-viec.md:343` + Postconditions `:351`
> | 8 | Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1) | BR-SLA-01 |
> - Deadline SLA được tính tự động

⇒ Hồ sơ ở "Đã duyệt" / "Hoàn thành" / "Đã đánh giá" (11/19 hồ sơ quan sát được là hồ sơ đã đóng) **chắc chắn đã đi qua "Chờ tiếp nhận"**, nên theo đặc tả phải có thời hạn xử lý. Việc cả cột "Thời hạn xử lý" lẫn cột "Cảnh báo thời hạn" đều trống ở nhóm này là **lệch đặc tả**.

**5) Cột "Tên doanh nghiệp" trống cũng lệch đặc tả** (dữ liệu nền của cùng nhóm hồ sơ đó):

`srs-fr-05-vu-viec.md:1649`
> | 14 | table | Tên doanh nghiệp | text | ten_doanh_nghiep (200px, cắt 40 ký tự) | — | Luôn |

`srs-fr-05-vu-viec.md:2014` — `doanh_nghiep_id` là trường **bắt buộc (Y)** của hồ sơ vụ việc;
`srs-fr-05-vu-viec.md:2154` — `ten_doanh_nghiep` là trường **bắt buộc (Y)** của doanh nghiệp.
⇒ Theo đặc tả không tồn tại hồ sơ vụ việc hợp lệ mà không có tên doanh nghiệp.

**6) Phần "hồ sơ đã đóng giữ nguyên mức cảnh báo cũ" thì ĐÚNG đặc tả, không dính tới phát hiện này** (công việc tự động chỉ quét hồ sơ đang hoạt động):

`srs-fr-05-vu-viec.md:1436`
> | 2 | Lấy danh sách VV đang hoạt động (DA_TIEP_NHAN, DANG_KIEM_TRA, DA_PHAN_CONG, DANG_XU_LY, CHO_PHE_DUYET) | — |

### Câu mô tả để ghi lên sheet

- Trên danh sách 41 hồ sơ, có 19 hồ sơ để trống cột "Cảnh báo thời hạn"; đúng 19 hồ sơ đó cũng trống cột "Thời hạn xử lý" và cột "Tên doanh nghiệp" — trong đó 11 hồ sơ đã ở các trạng thái cuối (Đã duyệt / Hoàn thành / Đã đánh giá).
- Theo đặc tả (`srs-fr-05-vu-viec.md:2284-2285` và `:343`), thời hạn xử lý được tính tự động ngay khi hồ sơ vào trạng thái "Chờ tiếp nhận" ở mọi kênh; hồ sơ đã đi qua bước tiếp nhận thì phải có thời hạn xử lý. Tên doanh nghiệp cũng là thông tin bắt buộc của hồ sơ (`srs-fr-05-vu-viec.md:2014`, `:2154`) và cột này luôn hiển thị (`:1649`).
- Việc cột "Cảnh báo thời hạn" để trống ở nhóm hồ sơ này **không phải lỗi hiển thị** — mức cảnh báo là đại lượng tính từ thời hạn xử lý (`srs-fr-05-vu-viec.md:1664`, `:2456`), thiếu thời hạn thì không có mức để hiện; quy ước chung cho ô trống là hiển thị gạch (`srs-v3.5.md:957`).
- Yêu cầu nghiệp vụ: nhóm hồ sơ đã tiếp nhận nhưng thiếu thời hạn xử lý và tên doanh nghiệp cần được rà lại để khôi phục đủ dữ liệu nền, vì thiếu thời hạn thì hồ sơ nằm ngoài toàn bộ cơ chế cảnh báo và nhắc quá hạn.

### Mức độ đề xuất: **Major**

19/41 hồ sơ nằm ngoài cơ chế theo dõi thời hạn (không có mốc hạn ⇒ không cảnh báo, không nhắc quá hạn theo BR-SLA-03).
*Ghi chú khi trao đổi với BA:* nếu xác định đây là nhóm hồ sơ cũ tạo trước khi có tính năng tính thời hạn (và hồ sơ tạo mới đều có đủ), có thể hạ xuống **Minor** và chuyển thành việc làm sạch dữ liệu thay vì sửa mã nguồn. Hồ sơ ở trạng thái "Mới tạo" (chưa tiếp nhận) trống cột này là **hợp lệ** — không tính vào phạm vi.

---

## PH-3 — Thông báo công bố kết quả thiếu số lượng học viên

**Màn hình / chức năng:** Đào tạo, tập huấn → Khóa học → thẻ "Công bố kết quả".

### Kết luận: **SPEC KHÔNG QUY ĐỊNH — cần BA xác nhận** (nghiêng về KHÔNG PHẢI LỖI)

### Căn cứ — đã tìm ở những chỗ sau và không thấy quy định nội dung câu thông báo

**1) Đặc tả màn hình — thẻ "Công bố kết quả" chỉ liệt kê thành phần, không có câu thông báo nào:**

`srs-fr-03-dao-tao.md:1932`
> 8. **Tab 8 — Công bố kết quả** … Nút "Công bố tất cả" + công tắc "Công bố lên Cổng PLQG (Cổng tự kéo)" + nút "Hủy công bố tất cả". Bảng HV có kết quả: Cột Chọn dòng · **Họ tên · Email · Số điện thoại · Đơn vị** · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động (Công bố/Hủy công bố cá nhân). Hộp thoại xác nhận hủy công bố yêu cầu lý do ≥10 ký tự (BR-FLOW-04). …

Màn hình này **không có mục "Thông báo riêng"** (khác với màn Chi tiết vụ việc — nơi đặc tả liệt kê từng câu toast một, `srs-fr-05-vu-viec.md:1771-1785`).

**2) Chức năng công bố kết quả (FR-III-19, `srs-fr-03-dao-tao.md:1370-1456`)** — đọc trọn: Preconditions, Inputs, Processing 6 bước (`:1407-1414`), Outputs, Postconditions (`:1435-1440`), Error Handling (`:1444-1449`), Acceptance Criteria (`:1451-1454`). **Không dòng nào quy định nội dung câu thông báo hiển thị cho cán bộ sau khi công bố.** Bốn mã lỗi có sẵn (ERR-CB-KQ-01/02/04/05) đều là tình huống chặn, không phải thông báo thành công.

**3) Điều duy nhất đặc tả có yêu cầu về "số lượng học viên" là dữ liệu trả về của thao tác, không phải câu chữ trên màn hình:**

`srs-fr-03-dao-tao.md:1431`
> | 2 | so_hv_cong_bo | number | Số học viên đã công bố |

**4) Bộ mẫu thông báo công khai dùng chung toàn hệ thống cũng không kèm số lượng:**

`srs-v3.5.md:6726` (Phụ lục E.I.1)
> | Công khai thành công | Toast success (auto-dismiss 4s) | "Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp luật Quốc gia." | `ten_doi_tuong` …; `ma_hoac_ten` |

**5) Đã grep toàn bộ thư mục v3.5** với `{số lượng}`, `{so_luong}`, `{N} học viên`, `Đã công bố` — chỉ khớp `so_hv_cong_bo` ở dòng 1431 nêu trên và các nội dung không liên quan. **Câu "…cho {số lượng} học viên" là cách diễn đạt trong phần mô tả của phiếu, không có trong đặc tả.**

**6) Phần nội dung hiện có của thông báo thì đúng mô hình đã chốt:** "Cổng PLQG sẽ lấy dữ liệu ở lần đồng bộ kế tiếp" khớp mô hình KÉO (`srs-v3.5.md:6748` — Cổng tự kéo, phần mềm không đẩy).

### Câu mô tả để ghi lên sheet

- Sau khi công bố kết quả, hệ thống hiện thông báo "Đã công bố kết quả. Cổng PLQG sẽ lấy dữ liệu ở lần đồng bộ kế tiếp." — không kèm số lượng học viên như câu mô tả trong phiếu.
- Đặc tả màn hình "Công bố kết quả" (`srs-fr-03-dao-tao.md:1932`) và toàn bộ chức năng công bố kết quả đào tạo (`srs-fr-03-dao-tao.md:1370-1456`) **không quy định nội dung câu thông báo sau khi công bố**, cũng không yêu cầu kèm số lượng học viên; bộ mẫu thông báo công khai dùng chung (`srs-v3.5.md:6726`) cũng không có tham số số lượng.
- Đặc tả chỉ yêu cầu thao tác công bố trả về "số học viên đã công bố" như một dữ liệu kết quả (`srs-fr-03-dao-tao.md:1431`), không nói dữ liệu đó phải nằm trong câu thông báo.
- Đề nghị BA xác nhận: có bổ sung số lượng học viên vào thông báo sau khi công bố hay giữ nguyên câu hiện tại. Nếu chốt bổ sung thì là yêu cầu cải tiến kèm cập nhật đặc tả, không phải lỗi so với bản đặc tả hiện hành.

### Mức độ đề xuất: **Minor** (đề xuất cải tiến, không phải sai đặc tả)

---

## PH-4 — Nút "Xem" tệp đính kèm mở thẻ trình duyệt mới

**Màn hình / chức năng:** Quản lý hồ sơ vụ việc → Chi tiết vụ việc → nhóm "Tài liệu đính kèm".

### Kết luận: **SPEC KHÔNG QUY ĐỊNH — cần BA xác nhận** (nghiêng về KHÔNG PHẢI LỖI)

### Căn cứ — đã tìm ở những chỗ sau

**1) Đặc tả màn hình Chi tiết vụ việc chỉ nói "có nút [Xem] [Tải]", cột "Hành vi" bỏ trống:**

`srs-fr-05-vu-viec.md:1729`
> | 6 | content | Accordion 3 — Tài liệu Đính kèm | C23 | Danh sách file: tên file, loại, kích thước, ngày upload, nút [Xem] [Tải]. Nút [+ Thêm tài liệu] | — | Luôn. [+ Thêm] chỉ khi trạng thái cho phép sửa |

Cột "Hành vi" của dòng này là `—` (theo quy ước đọc bảng tại `srs-fr-05-vu-viec.md:1487`, cột này là nơi ghi "sự kiện khi user thao tác"). ⇒ **Đặc tả yêu cầu có nút Xem, không quy định mở ở đâu.**

**2) Chức năng quản lý hồ sơ vụ việc (FR-V.I-07, `srs-fr-05-vu-viec.md:570-632`)** — đọc trọn Inputs / Processing / Outputs / Acceptance Criteria: chỉ có `tai_lieu | FILE[] | Danh sách tài liệu` ở Outputs (`:615`). Không mô tả hành vi xem tệp.

**3) Chế độ doanh nghiệp của cùng màn hình còn nhẹ hơn — chỉ yêu cầu nút tải:**

`srs-fr-05-vu-viec.md:1804`
> | Nhóm 3 — Tài liệu | Chỉ đọc + nút [Tải về] cho từng tệp |

**4) Đặc tả CÓ chỗ yêu cầu xem trước rõ ràng — nhưng ở nhóm chức năng khác, không áp cho vụ việc:**

- Biểu mẫu — `srs-fr-09-bieu-mau.md:50` "Ưu tiên xem trực tuyến (preview) trước khi tải về"; `:331-338` Processing "Xem trực tuyến (preview)"; `:382` AC "chọn 'Xem trước' → hiển thị preview".
- Bài giảng — `srs-fr-03-dao-tao.md:1978` "Slide/PDF xem trực tiếp trong trình duyệt".
- Tư vấn chuyên sâu — `srs-fr-12-tv-chuyen-sau.md:981` "CB NV xem file trực tuyến → hiển thị preview".

Cả ba chỗ đều **không** đặt ràng buộc "phải mở trong cùng trang, không được mở thẻ mới". Nhóm Vụ việc thì hoàn toàn không có dòng nào tương đương.

**5) Quy ước giao diện dùng chung (Phụ lục E §H, `srs-v3.5.md:6706-6714`, H1→H7)** — không có quy ước nào về nơi mở tệp đính kèm. `srs-v3.5.md:6713` (H6) nói về icon cột Hành động của bảng bản ghi, không phải nút xem tệp.

### Câu mô tả để ghi lên sheet

- Bấm "Xem" trên hàng tệp đính kèm ở màn chi tiết hồ sơ vụ việc thì tệp mở ở thẻ mới của trình duyệt thay vì khung xem trước ngay trong trang; tệp vẫn mở và đọc được bình thường.
- Đặc tả màn chi tiết vụ việc (`srs-fr-05-vu-viec.md:1729`) chỉ yêu cầu hàng tệp có nút "Xem" và nút "Tải", **không quy định tệp phải được xem trước ngay trong trang hay mở ở thẻ mới**; chức năng quản lý hồ sơ vụ việc (`srs-fr-05-vu-viec.md:570-632`) cũng không mô tả hành vi này.
- Các nhóm chức năng khác có yêu cầu xem trực tuyến (thư viện biểu mẫu, bài giảng, tư liệu tư vấn) đều là đặc tả riêng của nhóm đó, không áp sang hồ sơ vụ việc.
- Đề nghị BA xác nhận cách trình bày mong muốn cho hồ sơ vụ việc. Nếu chốt phải xem trước ngay trong trang thì là yêu cầu cải tiến kèm cập nhật đặc tả, không phải lỗi so với bản đặc tả hiện hành.

### Mức độ đề xuất: **Minor** (đề xuất cải tiến / xác nhận cách trình bày)

---

## PH-5 — Mức ưu tiên chỉ hiện con số; danh sách không lọc/sắp xếp theo mức

**Màn hình / chức năng:** Nhu cầu / Yêu cầu hỗ trợ — màn Chi tiết hồ sơ vụ việc (ý 1) và màn Danh sách hồ sơ vụ việc (ý 2).

### Kết luận: tách làm 2 ý — **ý 1: LÀ LỖI (Minor)** · **ý 2: SPEC KHÔNG QUY ĐỊNH — cần BA xác nhận**

> **Về nhận định BA chốt 04/08/2026 "hiện con số là đúng đặc tả": đúng nhưng chưa đủ.** Chính dòng đặc tả nói "giá trị hiển thị là con số" cũng nói con số phải có **chú giải kèm theo** và bảng ngay dưới nó có cột **"Chú giải hiển thị"** + cột **"Màu badge"**. Hiện màn chi tiết chỉ có con số trần, không chú giải, không huy hiệu màu.

### Căn cứ — ý 1 (màn chi tiết chỉ hiện con số)

**1) Dòng chốt của BA nằm trong mục "Bảng ánh xạ mã DB → nhãn hiển thị tiếng Việt" của phần Màn hình chức năng — tức là quy ước RENDER GIAO DIỆN, không phải chú giải trong tài liệu:**

`srs-fr-05-vu-viec.md:1492` (câu mở đầu của chính mục đó)
> Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt theo bảng dưới. Mã DB **không bao giờ** xuất hiện trên giao diện người dùng.

**2) Dòng chốt 04/08/2026 — đọc nguyên văn:**

`srs-fr-05-vu-viec.md:1520-1522`
> **Mức ưu tiên (`VU_VIEC.uu_tien`):**
>
> > Thang số 1–5 (auto-calc theo BR-CALC-07; CB NV có thể nâng mức kèm `ly_do_uu_tien`). **Giá trị hiển thị trên giao diện là con số**; bảng dưới là **chú giải kèm theo, không thay thế con số**. `[BA chốt 2026-08-04]`

**3) Bảng ngay dưới có 2 cột đều là thuộc tính giao diện — "Chú giải hiển thị" và "Màu badge":**

`srs-fr-05-vu-viec.md:1524-1530`
> | Giá trị | Chú giải hiển thị | Màu badge |
> |---------|-------------------|-----------|
> | `1` | Mức thường — xét theo thứ tự nộp hồ sơ | Xám nhạt |
> | `2` | DN có từ 30% lao động là người khuyết tật | Xám nhạt |
> | `3` | DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ | Xanh lá |
> | `4` | Cán bộ nâng mức, kèm lý do | Cam |
> | `5` | Cán bộ nâng mức khẩn, kèm lý do | Đỏ |

Ba bảng khác trong **cùng mục** (trạng thái vụ việc `:1496-1509`, mức cảnh báo thời hạn `:1513-1518`, kênh tiếp nhận `:1534-1540`) đều là quy ước render giao diện với cột màu badge tương tự — không có lý do đọc riêng bảng mức ưu tiên theo nghĩa khác.

⇒ **Yêu cầu nghiệp vụ:** khi hiển thị mức ưu tiên, hệ thống phải hiện con số **kèm** chú giải bằng chữ và huy hiệu màu tương ứng. "Kèm theo, không thay thế" nghĩa là cả hai cùng có mặt — hiện chỉ có con số là **thiếu vế chú giải**.

*Ghi chú:* biểu mẫu nhập hồ sơ đã làm đúng vế này (ô "Độ ưu tiên" hiện "4 — Cán bộ nâng mức, kèm lý do" / "5 — Cán bộ nâng mức khẩn, kèm lý do"), nên thiếu sót chỉ còn ở màn chi tiết (và mọi chỗ khác hiện con số trần).

### Căn cứ — ý 2 (danh sách không có cột / bộ lọc / sắp xếp theo mức ưu tiên)

**1) Đặc tả màn Danh sách hồ sơ vụ việc liệt kê ĐỦ 13 cột bảng — không có cột mức ưu tiên:**

`srs-fr-05-vu-viec.md:1647-1657` — Checkbox · Mã vụ việc · Tên doanh nghiệp · Lĩnh vực pháp luật · Kênh tiếp nhận · Trạng thái · Người xử lý/Tổ chức · Ngày tiếp nhận · Thời hạn xử lý · Cảnh báo thời hạn · Hành động. **Không có "Mức ưu tiên".**

**2) Thanh bộ lọc cũng liệt kê đủ — không có bộ lọc theo mức ưu tiên:**

`srs-fr-05-vu-viec.md:1639-1646` — Ô tìm kiếm · Lĩnh vực pháp luật · Đơn vị (chỉ cấp TW) · Trạng thái · Kênh tiếp nhận · Mức SLA · Bộ chọn ngày · Nút Tìm kiếm/Xóa bộ lọc. **Không có "Mức ưu tiên".**

**3) Chức năng tìm kiếm hồ sơ (FR-V.I-08) — 7 tham số đầu vào, không có mức ưu tiên:**

`srs-fr-05-vu-viec.md:651-659` — `tu_khoa`, `linh_vuc_id`, `trang_thai`, `kenh_tiep_nhan`, `tu_ngay`, `den_ngay`, `don_vi_id`. Outputs `:672-684` cũng không trả mức ưu tiên.

**4) Chức năng quản lý hồ sơ (FR-V.I-01) — Outputs `srs-fr-05-vu-viec.md:129-141`** cũng không có mức ưu tiên.

**5) Quy tắc sắp xếp gắn với các cột đang có:**

`srs-fr-05-vu-viec.md:1665`
> - Sắp xếp mặc định: ngày cập nhật DESC. Hỗ trợ sort theo từng cột

⇒ Không có cột mức ưu tiên thì cũng không phát sinh yêu cầu sắp xếp theo mức ưu tiên. **Đặc tả không quy định cột / bộ lọc / sắp xếp theo mức ưu tiên ở màn danh sách** — hiện trạng khớp đặc tả.

*(Lưu ý: mức ưu tiên vẫn được dùng để xếp thứ tự ở bảng gợi ý phân công — `srs-fr-05-vu-viec.md:735-737` — nhưng đó là màn phân công, không phải màn danh sách hồ sơ.)*

### Câu mô tả để ghi lên sheet

- Màn chi tiết hồ sơ vụ việc chỉ hiện con số mức ưu tiên (ví dụ "3"), không kèm chú giải bằng chữ và không có huy hiệu màu; cán bộ không tra bảng thì không biết con số đó nghĩa là gì.
- Theo đặc tả (`srs-fr-05-vu-viec.md:1520-1530`, chốt 04/08/2026): giá trị hiển thị **là con số**, còn bảng chú giải là phần **"kèm theo, không thay thế con số"**, với cột "Chú giải hiển thị" và cột "Màu badge" cho từng mức 1–5. Tức yêu cầu là con số **đi kèm** chú giải và màu, chứ không phải con số đứng một mình — hiện đang thiếu vế chú giải ở màn chi tiết. Biểu mẫu nhập hồ sơ đã hiển thị đúng dạng "số — chú giải", có thể lấy làm chuẩn.
- Về việc màn danh sách không có cột mức ưu tiên nên không lọc / sắp xếp theo mức được: đặc tả màn danh sách (`srs-fr-05-vu-viec.md:1639-1657`) và chức năng tìm kiếm hồ sơ (`srs-fr-05-vu-viec.md:651-684`) **không quy định** cột, bộ lọc hay tiêu chí sắp xếp theo mức ưu tiên — hiện trạng đúng đặc tả.
- Nếu nghiệp vụ muốn theo dõi hồ sơ ưu tiên ngay trên danh sách, đề nghị BA xác nhận để mở yêu cầu cải tiến kèm cập nhật đặc tả.

### Mức độ đề xuất

- **Ý 1 (thiếu chú giải + huy hiệu màu ở màn chi tiết): Minor** — không chặn thao tác, nhưng dễ đọc sai mức ưu tiên.
- **Ý 2 (cột / bộ lọc / sắp xếp ở màn danh sách): không phải lỗi** — nếu muốn thì mở phiếu cải tiến riêng.

---

## Bảng tổng hợp

| Mã tạm | Màn hình | Kết luận | Mức độ |
|---|---|---|---|
| PH-1 | Nhu cầu / Yêu cầu hỗ trợ — biểu mẫu nhập hồ sơ vụ việc (ô "Ngày tiếp nhận") | **LÀ LỖI** — đặc tả quy định ô bắt buộc, mặc định = ngày hiện tại và không có ràng buộc cấm ngày hiện tại; phần mềm từ chối chính giá trị mặc định của mình | **Major** |
| PH-2 | Thống kê / Danh sách hồ sơ yêu cầu hỗ trợ pháp lý | **LÀ LỖI** — nhưng ở dữ liệu nền: hồ sơ đã qua tiếp nhận mà thiếu thời hạn xử lý (và tên doanh nghiệp) là lệch đặc tả; riêng việc để trống cột cảnh báo khi chưa có thời hạn thì không sai | **Major** (hạ **Minor** nếu BA xác nhận chỉ là nhóm hồ sơ cũ) |
| PH-3 | Đào tạo, tập huấn → Khóa học → thẻ "Công bố kết quả" | **SPEC KHÔNG QUY ĐỊNH — cần BA xác nhận** — đặc tả không quy định nội dung câu thông báo sau khi công bố, không đòi kèm số lượng học viên | **Minor** (đề xuất cải tiến) |
| PH-4 | Quản lý hồ sơ vụ việc → Chi tiết → nhóm "Tài liệu đính kèm" | **SPEC KHÔNG QUY ĐỊNH — cần BA xác nhận** — đặc tả chỉ yêu cầu có nút "Xem"/"Tải", không nói xem trước trong trang hay mở thẻ mới | **Minor** (đề xuất cải tiến) |
| PH-5 | Nhu cầu / Yêu cầu hỗ trợ — màn Chi tiết (ý 1) và màn Danh sách (ý 2) hồ sơ vụ việc | Ý 1 **LÀ LỖI** — đặc tả yêu cầu con số **kèm** chú giải + huy hiệu màu, hiện chỉ có con số trần · Ý 2 **SPEC KHÔNG QUY ĐỊNH** — danh sách không có cột/bộ lọc/sắp xếp theo mức ưu tiên trong đặc tả | Ý 1 **Minor** · Ý 2 **không phải lỗi** |
