# PDKHDTTH_04 — Cổng 3 (đối chiếu SRS)

> **Case đối tác:** Tuần 2, log row 360 — *"Cán bộ phê duyệt khác cấp với người lập"*.
> **Đối tác báo:** *"Cán bộ khác cấp phê duyệt: hệ thống không hiển thị thông báo lý do từ chối."*
> **Kỳ vọng đối tác:** hệ thống từ chối + hiển thị thông báo *"Không có quyền phê duyệt kế hoạch này"*.
> **Nguồn SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).

---

## Mục SRS liên quan

### A. FR-III-15 — Phê duyệt kế hoạch (UC34)

Toàn bộ FR nằm ở `srs-fr-03-dao-tao.md:1208`–`:1229`. Trích nguyên văn:

**`:1211`**
> **Màn hình:** SCR-III-01 (workflow actions)

> ⚠️ **Cảnh báo trích dẫn:** dòng `:1211` ghi SCR-III-01 (màn Chương trình đào tạo), nhưng màn liệt kê hành động Phê duyệt/Từ chối cho **Kế hoạch đào tạo năm** là **SCR-III-00** (`:1774`, cột Hành động). Cùng lỗi này đã được BA sửa cho FR-III-16 ngày 2026-08-01 — xem `:1236`: *"`[sửa 2026-08-01 — AI_TIEN-002: trước ghi SCR-III-01 là màn Chương trình đào tạo, trong khi SCR-III-00 §FR sử dụng mới là màn liệt kê FR-III-16]`"*. FR-III-15 **chưa được sửa tương tự**. Khi log bug hãy dẫn `:1745` (*"FR sử dụng: FR-III-14, FR-III-15, FR-III-16"* của SCR-III-00) + `:1774`, đừng dẫn `:1211`.

**`:1213`**
> **Mô tả:** CB PD phê duyệt hoặc từ chối kế hoạch đào tạo.

**`:1215`** — dòng quy định thẩm quyền:
> **Tác nhân:** **CB PD (cùng đơn vị, BR-FLOW-03)**

**`:1217`**
> **Preconditions:** CB PD đã đăng nhập, KH ở CHO_DUYET, **CB PD cùng đơn vị**.

**`:1219`**
> **Inputs:** ke_hoach_id (identifier, Y), quyet_dinh (text, Y: PHE_DUYET/TU_CHOI), ly_do (text, Cond: bắt buộc nếu TU_CHOI).

**`:1221`**
> **Processing:** **Kiểm tra quyền + cùng đơn vị** → Duyệt/Từ chối → Thông báo CB NV → Ghi nhật ký.

**`:1223`**
> **Outputs:** ke_hoach_id, trang_thai (DA_DUYET/TU_CHOI), ly_do.

**`:1227`**–**`:1229`** — Acceptance Criteria (nguyên văn, đầy đủ, chỉ có 2 dòng):
> - **Given** CB PD phê duyệt **When** xác nhận **Then** trạng thái → DA_DUYET
> - **Given** CB PD từ chối **When** nhập lý do **Then** trạng thái → TU_CHOI

→ **FR-III-15 KHÔNG có mục "Error Handling".** Không mã `ERR-` nào, không mẫu thông báo nào cho ca "cán bộ khác đơn vị/khác cấp bấm phê duyệt". Không AC nào phủ ca này.

> ⚠️ **Lệch mã BR trong chính SRS:** `:1215` viện dẫn **BR-FLOW-03** cho ràng buộc "cùng đơn vị", nhưng BR-FLOW-03 (`srs-v3.5.md:5536`) là *"Không sửa/xóa sau phê duyệt"* — không liên quan thẩm quyền. Quy tắc đúng là **BR-AUTH-05**, và chính bảng BR nhóm III (`srs-fr-03-dao-tao.md:2213`) đã ánh xạ đúng: *"| BR-AUTH-05 | Phê duyệt cùng đơn vị | FR-III-01 (CTDT phê duyệt — Thay đổi 2), **FR-III-15**, FR-III-18 |"*. **Khi log bug phải quote BR-AUTH-05**, không quote BR-FLOW-03 theo `:1215`.

### B. BR-AUTH-05 — quy tắc thẩm quyền phê duyệt (nguồn chuẩn)

**`srs-v3.5.md:5480`** — nguyên văn (phần đầu):

> | BR-AUTH-05 | **Phê duyệt cùng đơn vị (strict).** CB PD chỉ duyệt bản ghi do CB NV **cùng đơn vị** tạo (`user.don_vi_id = record.don_vi_id`). **KHÔNG cho phép cấp trên duyệt cấp dưới hoặc duyệt chéo giữa các đơn vị cùng cấp.** Áp dụng cho mọi action duyệt: phê duyệt, từ chối, công khai, hủy công khai, đóng hồ sơ. […] | PRD A4, biên bản b3, NĐ 55/2019 Điều 10, NĐ 121/2025 Điều 39-40 | FR-II-08, FR-III-01 (CTDT phê duyệt), **FR-III-15/18/21**, FR-IV-07, FR-IV-NEW-04, FR-V.I-13, FR-V.II-12, FR-VI-04/09, FR-XI-04 | — | **Test (1) CB PD Bộ Tài chính KHÔNG duyệt được bản ghi của Bộ TN&MT (cùng cấp BN khác đơn vị); (2) CB PD Bộ Tư pháp (TW) KHÔNG duyệt được bản ghi của Sở TP HN (ĐP); (3) CB PD Sở TP HN duyệt được bản ghi của Sở TP HN.** |

→ Cột "Cách kiểm thử" của BR-AUTH-05 **đã bao trùm đúng kịch bản của case này** (test case số 2: TW không duyệt được bản ghi của ĐP). Cột "Ngoại lệ" là `—`, tức **không có ngoại lệ**.

### C. Máy trạng thái — guard của chuyển tiếp phê duyệt kế hoạch

**`srs-v3.5.md:6380`** — SM-KH-DAO-TAO (nguyên văn):

> | CHO_DUYET | DA_DUYET | CB PD duyệt | **Cùng đơn vị (BR-AUTH-05)** | Ghi thoi_gian_duyet + nguoi_duyet, audit | FR-III-15 | BR-AUTH-05, BR-FLOW-03 |

→ "Cùng đơn vị" là **điều kiện canh cổng (guard) của chuyển tiếp trạng thái**, không phải gợi ý giao diện. Không thoả guard thì chuyển tiếp **không được xảy ra**.

### D. Màn hình — nút Phê duyệt/Từ chối hiển thị theo điều kiện nào

**`srs-fr-03-dao-tao.md:1774`** — cột Hành động của bảng Kế hoạch (nguyên văn):

> | Hành động | Xem · Sửa (chỉ Bản nháp / Bị từ chối) · Xóa (chỉ Bản nháp + chưa có CTDT con) · Gửi phê duyệt (Bản nháp / Bị từ chối) · **Phê duyệt + Từ chối (Chờ duyệt — CB PD)** · Công khai (Đã duyệt) · Hủy công khai (Đã công khai) |

→ Điều kiện hiển thị chỉ ghi theo **trạng thái + vai trò**, **không ghi điều kiện đơn vị**. SRS không nói rõ nút phải bị ẩn với CB PD khác đơn vị.

**`srs-v3.5.md:683`** — quy ước giao diện M-05 (nguyên văn):

> | M-05 | **Hiển thị theo quyền** — menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. **Ẩn (không disable) nếu không có quyền** | NF-Security |

→ Quy ước này áp cho **mục menu**, nhưng cho thấy khuynh hướng thiết kế của hệ thống là **ẩn** khi không có quyền, chứ không phải hiện rồi báo lỗi. Đây là lý do "không thấy thông báo" **có thể** là hành vi đúng.

### E. Đã tìm và KHÔNG có — mẫu thông báo từ chối quyền phê duyệt

Đã grep toàn bộ SRS v3.5 các chuỗi *"Không có quyền"*, *"không có quyền"*, *"403"*:

- **`srs-v3.5.md:6723`** (Phụ lục E.I.1) — nguyên văn:
  > | Phạm vi đơn vị không hợp lệ | Toast error (auto-dismiss 6s) | **"Bạn không có quyền công khai {ten_doi_tuong} của đơn vị khác."** | `ten_doi_tuong` |

  → Đây là mẫu duy nhất trong SRS cho ca "sai phạm vi đơn vị", **nhưng chỉ áp cho luồng CÔNG KHAI lên Cổng PLQG**. Phạm vi ghi ở `:6715`: *"Áp dụng cho mọi luồng công khai/hủy công khai lên Cổng Pháp luật Quốc gia: FR-III-16 Kế hoạch ĐT, FR-V Vụ việc, …"* — **không có FR-III-15**.

- **`srs-fr-10-quan-tri.md:158`** — nguyên văn:
  > | E1 | User không có quyền QTHT | ERR-AUTH-01 | "Bạn không có quyền thực hiện chức năng này" | ERROR |

  → Nằm trong bảng *"Error Handling chung"* của FR quản lý **danh mục dùng chung** (QTHT), **không** được SRS tuyên bố là quy ước toàn hệ thống, và **không** được FR-III-15 tham chiếu.

- **Chuỗi *"Không có quyền phê duyệt kế hoạch này"* mà đối tác kỳ vọng: KHÔNG tồn tại ở bất kỳ dòng nào của SRS v3.5.**

---

## UC Reference

| Mục SRS | UC Reference | Dòng |
|---|---|---|
| **FR-III-15 Phê duyệt kế hoạch** | **UC 34** | `srs-fr-03-dao-tao.md:1210` — *"**UC Reference:** UC 34 \| **Priority:** Essential \| **Stability:** High"* |
| FR-III-14 Lập kế hoạch đào tạo năm (luồng Gửi phê duyệt, `:1155`–`:1164`) | UC 33 | `srs-fr-03-dao-tao.md:1069` |
| FR-III-18 Phê duyệt kết quả (cùng áp BR-AUTH-05) | UC 37 | `srs-fr-03-dao-tao.md:1322` (heading) |
| **SCR-III-00 Kế hoạch đào tạo năm** — màn thực tế chứa nút Phê duyệt/Từ chối | **KHÔNG có dòng `UC Reference`** — mục đặc tả màn hình không mang trường này. Thay thế: `srs-fr-03-dao-tao.md:1742` (heading) + `:1745` — *"**FR sử dụng:** FR-III-14, FR-III-15, FR-III-16"* + `:1774` (cột Hành động) | 1742 / 1745 / 1774 |
| **BR-AUTH-05** | Không phải UC — là Business Rule, `srs-v3.5.md:5480` | 5480 |

---

## Bảng Cổng 3 (khung, chưa điền cột thực tế web)

**Trước khi điền — ghi rõ điều kiện dựng:** tài khoản người lập `________` (đơn vị/cấp `________`) · tài khoản người bấm phê duyệt `________` (đơn vị/cấp `________`) · mã kế hoạch `________` · trạng thái trước thao tác `________`

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| Kế hoạch đang ở trạng thái **Chờ duyệt** trước khi thử (`srs-fr-03:1217`) | | |
| Người bấm phê duyệt là **CB PD** nhưng **khác đơn vị** với người lập (`:1215`, `srs-v3.5.md:5480`) — ghi rõ đơn vị hai bên | | |
| **Trạng thái kế hoạch KHÔNG chuyển sang "Đã duyệt"** sau thao tác (`srs-v3.5.md:6380` — guard "Cùng đơn vị"; `:5480` — *"KHÔNG cho phép cấp trên duyệt cấp dưới"*) | | |
| Kiểm lại **sau khi tải lại trang**: trạng thái vẫn là Chờ duyệt, không âm thầm đổi (`srs-v3.5.md:6380`) | | |
| Kiểm bằng **phương pháp thứ hai** (gọi trực tiếp thao tác phê duyệt qua tầng dữ liệu) → cũng bị từ chối, không chỉ chặn ở giao diện (`srs-v3.5.md:5480` — quy tắc nghiệp vụ, không phải quy tắc hiển thị) | | |
| Nhật ký thao tác **không** ghi nhận một lần duyệt thành công (`:1221` — *"Ghi nhật ký"*) | | |
| CB NV người lập **không** nhận thông báo "đã được duyệt" (`:1221` — *"Thông báo CB NV"*) | | |
| **[SRS chưa quy định — chỉ ghi nhận]** Nút "Phê duyệt"/"Từ chối" có **hiển thị** với CB PD khác đơn vị không (`:1774` chỉ nêu điều kiện trạng thái + vai trò) | | — |
| **[SRS chưa quy định — chỉ ghi nhận]** Sau khi bấm, hệ thống có hiện thông báo nào không — chép **nguyên văn** chuỗi hiển thị, kể cả khi chỉ là lỗi chung | | — |
| **[SRS chưa quy định — chỉ ghi nhận]** Nếu không hiện gì trên màn hình: phản hồi của yêu cầu là gì (mã trạng thái + mã lỗi nội bộ nếu có) | | — |
| **[Đối chứng]** Cùng thao tác với CB PD **đúng đơn vị** → duyệt thành công, trạng thái → Đã duyệt (`:1228`, `srs-v3.5.md:5480` test case 3) | | |

> **Ghi chú cho người verify — thứ tự kiểm quyết định kết luận:**
> 1. **Trước hết kiểm trạng thái**, không kiểm thông báo. Nếu kế hoạch **đã chuyển sang "Đã duyệt"** → vi phạm BR-AUTH-05, mức nghiêm trọng cao, hướng `Open` ngay — chuyện có thông báo hay không trở thành thứ yếu.
> 2. Chỉ khi hệ thống **đã chặn đúng** (trạng thái không đổi) thì phần "không hiển thị thông báo" mới là vấn đề còn lại — và phần đó SRS không quy định.
> 3. Bắt buộc kiểm bằng phương pháp thứ hai (gọi thẳng thao tác, không qua nút) — nếu giao diện ẩn nút nhưng tầng dữ liệu vẫn cho duyệt thì đó mới là lỗi thật.

---

## SRS có/không quy định

**Kết luận: tách làm hai vế, hai vế cho hai hướng khác nhau.**

**Vế 1 — Thẩm quyền (hệ thống có được phép cho duyệt không): (a) SRS quy định RÕ.**
- `srs-v3.5.md:5480` — *"KHÔNG cho phép cấp trên duyệt cấp dưới hoặc duyệt chéo giữa các đơn vị cùng cấp"*, ngoại lệ `—`, và cột kiểm thử nêu đúng kịch bản TW-duyệt-ĐP.
- `srs-fr-03-dao-tao.md:1217` — điều kiện tiên quyết *"CB PD cùng đơn vị"*.
- `srs-fr-03-dao-tao.md:1221` — bước xử lý *"Kiểm tra quyền + cùng đơn vị"*.
- `srs-v3.5.md:6380` — guard của chuyển tiếp `CHO_DUYET → DA_DUYET` là *"Cùng đơn vị (BR-AUTH-05)"*.

→ **Nếu verify cho thấy kế hoạch chuyển sang "Đã duyệt" bởi cán bộ khác đơn vị/khác cấp → hướng `Open`, mức nghiêm trọng cao** (lỗ hổng phân quyền, không phải lỗi giao diện).

**Vế 2 — Thông báo từ chối (hệ thống có phải báo cho người dùng biết vì sao không): (c) SRS SILENT → hướng `BA confirm`.**
- FR-III-15 **không có mục Error Handling** — không mã lỗi, không mẫu câu (`:1208`–`:1229`).
- Không AC nào phủ ca sai đơn vị (`:1227`–`:1229` chỉ có 2 dòng, đều là ca thành công).
- Mẫu duy nhất trong SRS cho "sai phạm vi đơn vị" (`srs-v3.5.md:6723`) **chỉ áp cho luồng công khai**, phạm vi liệt kê tại `:6715` không có FR-III-15.
- `ERR-AUTH-01` (`srs-fr-10-quan-tri.md:158`) thuộc bảng lỗi chung của FR quản lý danh mục QTHT, không được tuyên bố áp toàn hệ thống.
- Chuỗi đối tác kỳ vọng — *"Không có quyền phê duyệt kế hoạch này"* — **không có trong SRS**.
- Ngược lại, quy ước M-05 (`srs-v3.5.md:683`) cho thấy hệ thống có khuynh hướng **ẩn** thay vì báo lỗi. Nếu app ẩn nút Phê duyệt với CB PD khác đơn vị thì "không có thông báo" là **hệ quả tự nhiên của thiết kế đúng**, không phải thiếu sót.

→ **Nếu verify cho thấy hệ thống đã chặn đúng (trạng thái không đổi) và chỉ thiếu thông báo → hướng `BA confirm`, KHÔNG log `Open`.**

**Lưu ý cách viết nếu phải log bug:** mô tả theo yêu cầu nghiệp vụ, không kê đơn cách làm. Viết *"Theo BR-AUTH-05 (`srs-v3.5.md:5480`) và điều kiện tiên quyết FR-III-15 (`srs-fr-03-dao-tao.md:1217`), khi CB PD khác đơn vị thực hiện phê duyệt, hệ thống phải từ chối và giữ nguyên trạng thái Chờ duyệt"* — **đừng** viết *"phải trả mã 403"* hay *"phải hiện toast ERR-XXX"*.

---

## Câu hỏi cho BA

*(áp dụng cho vế 2 — chỉ hỏi khi verify xác nhận hệ thống đã chặn đúng)*

1. Khi cán bộ phê duyệt **khác đơn vị/khác cấp** với người lập kế hoạch, hệ thống có **bắt buộc hiển thị thông báo giải thích** cho người dùng không, hay chỉ cần **ẩn nút Phê duyệt/Từ chối** là đạt (theo khuynh hướng của quy ước M-05, `srs-v3.5.md:683`)? (bắt buộc có thông báo / ẩn nút là đủ)
2. Nếu **bắt buộc có thông báo** — mẫu thông báo chuẩn cho luồng **phê duyệt** là gì? Có tái dùng mẫu của luồng công khai (`srs-v3.5.md:6723` — *"Bạn không có quyền công khai {ten_doi_tuong} của đơn vị khác."*) bằng cách đổi động từ, hay cần mẫu riêng + mã lỗi riêng cho FR-III-15? (tái dùng / mẫu riêng)
3. FR-III-15 hiện **không có mục Error Handling** nào — BA có bổ sung bảng mã lỗi cho FR này (ít nhất 2 ca: sai đơn vị, kế hoạch không ở trạng thái Chờ duyệt) không? Nếu có thì áp luôn cho FR-III-18 (Phê duyệt kết quả) vì cùng khuôn không? (có/không)
4. Dòng `srs-fr-03-dao-tao.md:1215` đang viện dẫn **BR-FLOW-03** cho ràng buộc "cùng đơn vị", trong khi quy tắc đúng là **BR-AUTH-05** (bảng BR nhóm III `:2213` đã ánh xạ đúng). BA xác nhận `:1215` viết nhầm mã và cần sửa? (có/không)
5. Dòng `srs-fr-03-dao-tao.md:1211` ghi màn hình của FR-III-15 là **SCR-III-01**, trong khi nút Phê duyệt/Từ chối kế hoạch nằm ở **SCR-III-00** (`:1774`) — cùng lỗi đã sửa cho FR-III-16 ngày 2026-08-01 (`:1236`). BA xác nhận sửa nốt cho FR-III-15? (có/không)
