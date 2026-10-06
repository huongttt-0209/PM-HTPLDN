# BA confirmation needed — Tổng hợp các điểm cần BA chốt phát sinh ngày 2026-08-06 — 2026-08-06

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `bug-report-*.md`).

> **2 dạng case — mỗi mục dưới đây đã chọn sẵn đúng bộ mục:**
> - **Dạng A — QA đã có kết luận, cần BA phản hồi đối tác.** Bộ mục: *Bối cảnh testcase → Đối chiếu SRS → Citation → Kết quả verify UI hiện tại → Kết luận QA → Nội dung đề xuất BA phản hồi đối tác*.
> - **Dạng B — SRS tự mâu thuẫn, QA không tự chốt được.** Bộ mục: *Bối cảnh testcase → Kết quả verify UI hiện tại → Điểm mâu thuẫn trong SRS v3.5 → Câu hỏi cần BA xác nhận → Đề xuất QA tạm thời*.
> - **Biến thể B′ — đặc tả IM LẶNG** (SRS không có dòng nào về điểm đang xét, khác với "hai chỗ nói ngược nhau"). Giữ nguyên bộ mục và thứ tự của Dạng B, chỉ đổi tên mục thứ ba thành *Điểm đặc tả im lặng / chưa rõ trong SRS v3.5* — gọi "im lặng" là "mâu thuẫn" sẽ khiến BA đi tìm chỗ mâu thuẫn không tồn tại.

> **Quy tắc citation (BẮT BUỘC):** mọi khẳng định SRS đều trỏ `path/tới/file-srs.md:LINE` — đã mở file đọc từng dòng, KHÔNG lấy số dòng từ trí nhớ.
> - **Nguồn DUY NHẤT được quote số dòng (chốt 2026-07-25):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.
> - **KHÔNG quote số dòng từ `input/srs-update-2026-5-5/`** — bản đó lệch cả số dòng lẫn nội dung; quote nhầm bản → BA-question invalid.

> **Môi trường đo chung:** `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng **HTPLDN · V1.0.8**. Đối tác đo trên `htpldn-uat.ospgroup.vn` (V1.0 → V1.0.3), khác bộ dữ liệu — mọi kết luận dưới đây chỉ dựa vào *tệp/màn có khớp nhau trong chính lượt đo này hay không*, không đối chiếu số tuyệt đối với đối tác.
>
> Trong ngày 06/08 có **2 lần triển khai** xen giữa: bó mã FE `assets/index-CNwX9JjX.js` (`last-modified 06/08/2026 09:51:16`) và `assets/index-DIABnbIr.js` (`last-modified 06/08/2026 14:13:15`) — mỗi mục đã ghi rõ bó mã của chính lượt đo.

---

## Quan hệ với 3 file ĐÃ GỬI BA

**3 file đã gửi (không đụng vào, không lặp lại nội dung ở đây):**

| # | File đã gửi | Nội dung |
|---|---|---|
| 1 | [`ba-confirmation-needed-LKHDG-2026-08-06.md`](ba-confirmation-needed-LKHDG-2026-08-06.md) | `LKHDG_16` — bảng thành phần form đợt đánh giá là danh sách ĐÓNG hay MỞ |
| 2 | [`ba-confirmation-needed-QLNDTVVCG-2026-08-06.md`](ba-confirmation-needed-QLNDTVVCG-2026-08-06.md) | `QLNDTVVCG_24` kênh thông báo · `QLNDTVVCG_26` điều hướng sau khi CG từ chối · `QLNDTVVCG_24` (phụ) giao cho CG hay cả CG/TVV |
| 3 | [`cau-hoi-BA.md`](cau-hoi-BA.md) | Vai trò **QTHT** có được **xuất tệp** báo cáo không (5 phiếu `VVDHTHT_06` · `VVTDVQL_06` · `VVTLV_05` · `VVTLHDN_05` · `VVTTGCT_05`) |

**4 câu đã XOÁ khỏi file này vì trùng câu đã gửi** — BA trả lời **một lần** ở file số 3 là đủ cho tất cả:

| Câu bị xoá | Nằm ở file gốc nào | Trùng với |
|---|---|---|
| `VVDTN_06` — QTHT xem được "BC Vụ việc đã tiếp nhận" nhưng bấm [Xuất Excel] bị 403 `ERR-PERM-SYS-00-01` `Forbidden` | [`../../reverify-bug-devfix-2026-08-06/ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md`](../../reverify-bug-devfix-2026-08-06/ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md) | File đã gửi số 3 |
| `VVDHT_06` — như trên, màn "BC Vụ việc đã hỗ trợ" | nt | File đã gửi số 3 |
| `VVTTG_05` — như trên, màn "BC Vụ việc theo thời gian" | nt | File đã gửi số 3 |
| Mục 2 — như trên, 7 màn nhóm BC Chương trình / CG-TVV / Đánh giá / Đào tạo (`SLCTHT_06` · `CTTDVQL_04` · `CTTLV_05` · `CTTTG_04` · `CGTVPL_06` · `DGHQHTPL_06` · `CLDTBDPL_06`) | [`../../thu-QLTLPLCVV_15-2026-08-06/cau-hoi-BA.md`](../../thu-QLTLPLCVV_15-2026-08-06/cau-hoi-BA.md) §Mục 2 | File đã gửi số 3 |

> **Cả 4 câu đều cùng một hiện tượng, cùng một bộ căn cứ đặc tả** (`srs-fr-11-bao-cao.md:62` + `:889` liệt kê vai trò nhưng không cấm QTHT · `:1268` BR-AUTH-08 ghi *"QTHT bypass"* áp *"Toàn bộ FR-IX"* · `:79` bắt kiểm quyền ngay đầu luồng) và cùng một endpoint `POST /api/v1/bao-cao/export`. Xoá ở đây để BA không phải đọc lại 4 lần — **không** phải vì đã có kết luận.
>
> Một điểm phụ đi kèm **không** trùng và **không** cần BA: câu từ chối trả `Forbidden` / `ERR-PERM-SYS-00-01` là trái `srs-fr-11-bao-cao.md:117` — đã tách thành phiếu lỗi riêng, **không** hỏi BA.

**1 câu trùng NGUYÊN TẮC (giữ lại, có ghi chú):** mục `1.4` của [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) — *bảng Biểu mẫu có 2 cột `Ngày tạo` + `Sync Cổng` ngoài đặc tả* — hỏi đúng nguyên tắc của **file đã gửi số 1** (`LKHDG_16`: bảng thành phần trong SRS là danh sách ĐÓNG hay MỞ), chỉ khác màn hình. **Đã xoá khỏi phần thân file này**; nếu BA chốt `LKHDG_16` theo hướng "danh sách MỞ" thì mục `1.4` tự có lời giải, không cần trả lời riêng.

---

## Nguồn gộp

Bản gốc của từng lô **giữ nguyên tại chỗ**, không xoá — file này chỉ là bản gom để gửi BA một lần.

| Lô | File gốc | Mục gốc | Vào file này |
|---|---|---|---|
| B1 — BC thống kê vụ việc | [`../../reverify-bug-devfix-2026-08-06/ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md`](../../reverify-bug-devfix-2026-08-06/ba-confirm/ba-confirmation-needed-BCTK-B1-2026-08-06.md) | 4 | **1** (3 mục trùng → xoá) |
| B5 — Tư vấn chuyên sâu + BC Chương trình | [`../../thu-QLTLPLCVV_15-2026-08-06/cau-hoi-BA.md`](../../thu-QLTLPLCVV_15-2026-08-06/cau-hoi-BA.md) | 5 | **4** (Mục 2 trùng → xoá) |
| B6 — Vụ việc HTPL | [`../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/cau-hoi-BA.md`](../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/cau-hoi-BA.md) | 8 | **8** |
| B7 — Mạng lưới Tư vấn viên | [`../../batch-B7-tuvan-mangluoi-2026-08-06/cau-hoi-BA.md`](../../batch-B7-tuvan-mangluoi-2026-08-06/cau-hoi-BA.md) | 1 | **1** |
| FLOW 04 — Chi trả chi phí | [`../../flowtest-kiemdinh/cau-hoi-BA.md`](../../flowtest-kiemdinh/cau-hoi-BA.md) | 1 | **1** |
| Tuần 5 — Biểu mẫu + Hồ sơ pháp lý DN | [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) | 8 ghi nhận | **6** (1.4 trùng nguyên tắc → xoá · 1.7 không có câu hỏi → Phụ lục B) |

**23 mục gốc → 21 mục ở đây** (4 xoá vì trùng · 1 chuyển Phụ lục B · 3 mục QTHT của B1 gộp chung khi xoá).

---

## Mục lục

| # | Mã TC | Câu hỏi | Dạng | Có treo verdict? |
|---|---|---|---|---|
| 1 | `VVDTN_04` | "BC Vụ việc đã tiếp nhận" có phải có **biểu đồ tròn** theo lĩnh vực không? | A | ✅ |
| 2 | `QLTLPLCVV_15` (ngoài phạm vi) | Bảng Error Handling áp cho **cả máy chủ** hay chỉ lớp người dùng nhìn thấy? | B′ | ❌ (đã Pass) |
| 3 | `SLCTHT_06` (ngoài phạm vi) | Bộ lọc *Trạng thái chương trình* có **2** hay **3** giá trị? | B | ❌ (Reopen do lý do khác) |
| 4 | `CTTDVQL_04` (ngoài phạm vi) | Nhãn kỳ trong tệp xuất: chữ tiếng Việt hay **mã nội bộ** (`KHOANG`)? | B′ | ❌ |
| 5 | `CTTTG_04` (ngoài phạm vi) | *BC Chương trình theo thời gian* có thống kê **ngân sách** không? | B′ | ❌ |
| 6 | `KTHSYCHTPL_11` | Nhãn "Đạt — chuyển sang phân công" có cần đổi chữ không? | B′ | ❌ (đã Pass) |
| 7 | `TKHSYCHTPL_03` | Mã của mức "Sắp hết hạn": `SAP_HET` hay `SAP_HET_HAN`? | B | ❌ (đã Pass) |
| 8 | `TKHSYCHTPL_03` | Bộ lọc `SCR-V.I-01` lọc ngay khi đổi giá trị, hay chờ bấm [Tìm kiếm]? | B | ❌ (đã Pass) |
| 9 | `TKHSYCHTPL_03` | Hồ sơ **chưa có thời hạn xử lý** có thuộc nhóm "Bình thường" không? | B′ | ❌ (đã Pass) |
| 10 | `CNKQHT_07` | Chữ thông báo: "Đã cập nhật kết quả" hay "…kết quả hỗ trợ"? | B′ | ❌ (đã Pass) |
| 11 | `CNKQHT_07` | Cập nhật lần sau không đính tệp thì tệp lần trước còn hay mất? | B′ | ❌ (đã Pass) |
| 12 | `DGKQHTVV_01` | Vụ việc đã ở "Đã đánh giá" thì **cán bộ** còn được chấm không? | B | ❌ (verdict Reopen do lý do khác) |
| 13 | `DGKQHTVV_01` | Đánh giá vụ việc xong thì điểm trung bình của TVV có cập nhật không? | B | ❌ |
| 14 | `QLTVV_02` | Danh sách `SCR-IV-01` mặc định **sắp xếp theo tiêu chí nào**? | B′ | ✅ |
| 15 | `QLHSDNHTCP_03` | Cột "SLA" hiển thị gì khi hồ sơ **đã kết thúc**? | B′ | ✅ |
| 16 | `QLBMHD_02` (ghi nhận) | 4 ô lọc màn Biểu mẫu có bắt buộc **nhãn chữ** không? | B′ | ❌ (đã Pass) |
| 17 | `QLBMHD_02` (ghi nhận) | Bộ lọc `SCR-VII-02` lọc ngay khi chọn, hay giữ nút [Tìm kiếm]? | B | ❌ (đã Pass) |
| 18 | `QLBMHD_02` (ghi nhận) | Ô chọn Thư mục có phải **lọc theo đơn vị** người đăng nhập không? | B′ | ❌ (đã Pass) |
| 19 | `QLHSPLDN_06` (ghi nhận) | Nhật ký hệ thống xếp `HO_SO_PHAP_LY_DN` vào nhóm **"Tư vấn"** — sai nhóm hay sửa đặc tả? | B | ❌ (đã Pass) |
| 20 | `QLHSPLDN_07` (ghi nhận) | "Cập nhật bản ghi" có bao gồm **thay đổi tệp đính kèm** không? | B′ | ❌ (đã Pass) |
| 21 | `QLBMHD_02` (ghi nhận) | Biểu tượng **ngoài** cột Hành động có phải có nhãn trợ năng tiếng Việt không? | B′ | ❌ (đã Pass) |

> **Câu hỏi phát sinh sau file này (2026-08-07), để ở file riêng — không lặp nội dung ở đây:**
> `QLHSPLDN_15` (dòng 297) — *xuất Excel hồ sơ pháp lý DN khi bộ lọc ra **0 bản ghi**: chặn xuất kèm thông báo,
> hay cho tải tệp rỗng?* Dạng B′ (đặc tả im lặng), **đang treo verdict**. Toàn văn:
> [`ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md`](ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md).

**Tóm tắt cho BA:** **18/21 mục không treo verdict phiếu nào** — trả lời để lượt kiểm thử sau không chấm sai và dev không "dọn dẹp" nhầm. **3 mục đang treo verdict, ưu tiên trả lời trước:** Mục 1 · Mục 14 · Mục 15. (Câu về quyền xuất tệp của QTHT — treo 8 phiếu — nằm ở **file đã gửi số 3**, không lặp ở đây.)

---
<!-- ========================= MỤC 1 — DẠNG A ========================= -->

## `VVDTN_04` — Biểu đồ tròn theo lĩnh vực trên "BC Vụ việc đã tiếp nhận"

**Bối cảnh testcase**

- Dòng Excel: 178, mã TC `VVDTN_04`.
- Nội dung kiểm tra: vai trò **Quản trị viên QTHT** mở màn Báo cáo thống kê → loại BC **"BC Vụ việc đã tiếp nhận"**, Kỳ `Năm` 01/01/2026–31/12/2026, Đơn vị `Cục Bổ trợ tư pháp – BTP·TW`.
- Expected trong file UAT — đối tác nêu **2 vế**:
  - **(a)** phải hiển thị **biểu đồ tròn** theo lĩnh vực;
  - **(b)** bảng tổng hợp **thiếu các cột: Theo kênh, Theo lĩnh vực**.
- Actual đối tác ghi: chỉ thấy biểu đồ cột theo kênh + biểu đồ đường theo thời gian, không có vùng nào theo lĩnh vực.

**Đối chiếu SRS v3.5**

- Về **dữ liệu**: FR-IX-02 (UC125) khai `theo_kenh[]` và `theo_linh_vuc[]` là output điều kiện **"Luôn"** — hai chiều này bắt buộc phải có trong mọi lần tạo báo cáo. Vế (b) của đối tác **có cơ sở đặc tả**.
- Về **dạng biểu đồ**: bảng "Mapping 23 loại BC" của `SCR-IX-01` gán cho UC125 dạng **"Bar + Trend"**. Cùng bảng đó gán `Donut + Trend` cho UC124 và `Bar + Donut` cho UC127 ⇒ đặc tả **có** khái niệm biểu đồ tròn và **cố ý không** gán cho UC125. Đây **không** phải chỗ đặc tả im lặng.
- Đặc tả **im lặng** về: chiều lĩnh vực phải trình bày bằng *biểu đồ* hay bằng *bảng* — chỉ đòi có dữ liệu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:214` — `| 2 | theo_kenh[] | structured | Luôn | {kenh, so_luong} |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:215` — `| 3 | theo_linh_vuc[] | structured | Luôn | {linh_vuc, ten, so_luong} |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1065` — `| **Vụ việc** | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | **Bar + Trend** |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1064` / `:1067` — UC124 `Donut + Trend`, UC127 `Bar + Donut` (đối chứng: Donut được gán có chủ đích cho UC khác)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:203` — công thức FR-IX-02 *"Đếm số vụ việc đã tiếp nhận (trừ từ chối)"*

**Kết quả verify UI hiện tại**

- Verify 06/08/2026 12:51–13:12 qua Chrome DevTools MCP, bản dựng **V1.0.8**, tài khoản `cbnv_tw` (`CB_NV_TW` — đúng tác nhân `:192`); đối chứng thêm chính vai trò đối tác `admin`/**QTHT**.
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- **Vế (b) — không còn tái hiện.** Màn hiện đủ cả hai chiều:
  - Bảng **"Kênh tiếp nhận / Số lượng"**: Trực tiếp 41 · Doanh nghiệp 3 (lọc Toàn quốc).
  - Bảng **"Thống kê theo lĩnh vực pháp luật"**: Thương mại 16 · Dân sự 13 · Lao động 12 · Thuế 3, kèm cột Tỷ lệ.
  - Cả hai chiều **cộng khớp** tổng 44; đối chiếu đường thứ hai `GET /api/v1/vu-viecs` (45 bản ghi − 1 `TU_CHOI` = 44, đúng công thức `:203`) ra **y hệt** từng con số ⇒ số liệu đúng, không phải trùng/thiếu.
  - Vai trò QTHT gọi `GET /api/v1/bao-cao/vu-viec-tiep-nhan` cũng nhận đủ `theoKenh` + `theoLinhVuc`.
- **Vế (a) — hiện trạng: không có biểu đồ tròn.** Màn render đúng 2 biểu đồ: **cột** theo kênh tiếp nhận và **đường xu hướng** theo kỳ — khớp `Bar + Trend` của `:1065`. Chiều lĩnh vực được trình bày bằng **bảng**.
- **Đo lại 13:36 bằng CHÍNH vai trò đối tác** (`admin` / QTHT, BTP·TW), đúng bộ lọc đối tác — **không khác**: `Tổng vụ việc = 34`; bảng "Kênh tiếp nhận" (Trực tiếp 34); bảng "Thống kê theo lĩnh vực pháp luật" (Dân sự 13 · Lao động 9 · Thương mại 9 · Thuế 3 = 34, có cột Tỷ lệ); hai biểu đồ là **cột** + **đường**, **không có biểu đồ tròn**. Vai trò không làm đổi kết luận của cả hai vế.
- Evidence:
  - `../../reverify-bug-devfix-2026-08-06/bug-reports/image/VVDTN_04-04-QTHT-bieu-do-cot-va-duong-khong-co-tron.png` — vai trò QTHT, tổng 34, biểu đồ cột + đường
  - `../../reverify-bug-devfix-2026-08-06/bug-reports/image/VVDTN_04-05-QTHT-bang-kenh-va-bang-linh-vuc.png` — vai trò QTHT, bảng kênh + bảng lĩnh vực
  - `../../reverify-bug-devfix-2026-08-06/bug-reports/image/VVDTN_04-01-btptw-bang-kenh-va-linhvuc.png` · `…/VVDTN_04-02-btptw-tong-va-bieu-do-cot-theo-kenh.png` · `…/VVDTN_04-03-toanquoc-2kenh-4linhvuc-4donvi.png`

**Kết luận QA**

- **Vế (b) không còn là lỗi trên bản V1.0.8**: hai chiều "theo kênh" và "theo lĩnh vực" đều hiển thị được và số liệu khớp hai đường đo độc lập. (Đặc tả không quy định nhãn cột phải đúng chữ "Theo kênh"/"Theo lĩnh vực", nên không chấm lỗi vì tên cột.)
- **Vế (a) QA không tự chốt được — kỳ vọng đối tác ngược với đặc tả nói rõ.** Đối tác đòi biểu đồ tròn; `:1065` chốt UC125 = `Bar + Trend`. QA không tự bác đối tác nên không chấm Pass/Fail vế này.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt 1 trong 2 hướng cho `VVDTN_04`:

- **Hướng 1 — giữ đặc tả:** trả lời đối tác rằng UC125 theo thiết kế chỉ có **Bar + Trend**; chiều lĩnh vực đã được trình bày bằng **bảng có cột Tỷ lệ**, đủ thông tin. Khi đó cập nhật lại expected của `VVDTN_04` và đóng case.
- **Hướng 2 — đổi đặc tả:** nếu nghiệp vụ thực sự cần biểu đồ tròn theo lĩnh vực, cần sửa `:1065` (UC125 → `Bar + Donut + Trend` hoặc tương đương) rồi mới giao Dev FE bổ sung.
- Verdict QA đề xuất: **Cần BA xác nhận** (vế a), **không gửi Dev** cho tới khi có hướng chốt. Vế (b) không gửi Dev.

---

<!-- ========================= MỤC 2 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `QLTLPLCVV_15` (ghi nhận ngoài phạm vi) — Tệp đính kèm vượt 20MB: giao diện báo đúng tiếng Việt, máy chủ trả câu tiếng Anh không nêu ngưỡng

**Bối cảnh testcase**

- Dòng Excel: **299**, tab `bug`, mã TC `QLTLPLCVV_15`. Phát sinh trên màn *Tư liệu pháp lý liên kết* của nội dung Tư vấn chuyên sâu, widget **"File đính kèm"**.
- **Đối tác KHÔNG nêu điểm này** — không thuộc case nào của bảng theo dõi, **không** kéo verdict của `QLTLPLCVV_15` (đã **Pass** theo đúng các vế đối tác nêu).
- Vai trò đo: `cbnv_tw` (CB_NV_TW, cấp TW). Bản dựng **V1.0.8**.

**Kết quả verify UI hiện tại**

Hai đường đo cho ra **hai kết quả khác nhau**:

| Đường đo | Quan sát |
|---|---|
| **Giao diện** — chọn tệp PDF sạch 23.069.772 B (≈22MB) qua widget "File đính kèm" | Bị chặn **ngay tại trình duyệt** (0 request gửi lên máy chủ). Thông báo tiếng Việt: `C-pdf-sach-vuot-20mb.pdf: Kích thước vượt quá giới hạn 20MB.` → **đúng nghĩa, người dùng hiểu được** |
| **Máy chủ** — gọi thẳng cùng hành động với tệp 22.000.099 B | HTTP **413**, `{"code":"ERR-SYS-00-00-01","message":"File too large"}` → **tiếng Anh**, mã lỗi hệ thống chung, **không nêu ngưỡng 20MB** |

- Đối chứng loại trừ lỗi môi trường: cùng widget, tệp chứa mã độc trả **đúng** mã riêng `ERR-TLPL-04` kèm câu tiếng Việt đầy đủ ⇒ cơ chế "trả mã lỗi riêng theo tình huống" **vẫn chạy được** trên chính endpoint này.
- Bằng chứng: [`../../thu-QLTLPLCVV_15-2026-08-06/image/A-02-thong-bao-va-phan-hoi-may-chu.txt`](../../thu-QLTLPLCVV_15-2026-08-06/image/A-02-thong-bao-va-phan-hoi-may-chu.txt) mục 3 và mục 4.

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

Đặc tả **có** quy định riêng cho tình huống tệp vượt 20MB, nhưng **không nói bảng Error Handling áp cho lớp nào** — giao diện, máy chủ, hay cả hai.

Citation:

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:871`
  — `| 2 | Kiểm tra file: max 20MB, định dạng cho phép | EC-FILE-01 |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:968`
  — `| E3 | File vượt 20MB | ERR-TLPL-03 | "File tối đa 20MB" | ERROR |`

**Câu hỏi cần BA xác nhận**

Bảng Error Handling của đặc tả áp dụng cho **cả hai lớp** (giao diện *và* máy chủ), hay chỉ **lớp mà người dùng cuối nhìn thấy**?

1. **Nếu chỉ tính lớp người dùng nhìn thấy:** hiện trạng **đạt** — giao diện đã chặn và báo đúng nghĩa bằng tiếng Việt trước khi request rời trình duyệt; người dùng trên giao diện không bao giờ gặp câu tiếng Anh. ⇒ Không mở phiếu, đóng ghi nhận này.
2. **Nếu tính cả lớp máy chủ** (vì còn các bên tích hợp gọi thẳng API, không đi qua giao diện): hiện trạng **chưa đạt** — máy chủ cần trả phản hồi nêu rõ tệp vượt ngưỡng 20MB bằng tiếng Việt như các tình huống lỗi khác của cùng endpoint. ⇒ Mở phiếu mức **Minor**, owner **Dev BE**.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi cho tới khi BA chọn hướng — vì hai đường đo cho kết quả khác nhau và hướng (1) là kết luận "không phải lỗi".
- Verdict `QLTLPLCVV_15` **không** phụ thuộc vào ghi nhận này.
- Nếu BA chọn hướng (2), QA mở dòng mới trên tab `bug` theo quy tắc mã `QLTLPLCVV_QA01` trong đợt kế tiếp.

---

<!-- ========================= MỤC 3 — DẠNG B ========================= -->

## `SLCTHT_06` (ghi nhận ngoài phạm vi) — Bộ lọc "Trạng thái chương trình" có 3 giá trị, đặc tả chỉ liệt kê 2

**Bối cảnh testcase**

- Dòng Excel: **267**, tab `bug`, mã TC `SLCTHT_06`. Màn *Báo cáo thống kê → **BC Số lượng chương trình hỗ trợ*** (FR-IX-20/UC143).
- **Đối tác KHÔNG nêu điểm này** — không thuộc case nào của bảng theo dõi, **không** kéo verdict của `SLCTHT_06` (đã **Reopen** theo đúng vế đối tác nêu).
- Đo 2026-08-06 12:32, bản dựng **V1.0.8**.

**Kết quả verify UI hiện tại**

- Dropdown *Trạng thái chương trình* trên màn có **3** lựa chọn: **Đã phê duyệt · Đang thực hiện · Hoàn thành**.
- Tệp xuất cũng có mục *Theo trạng thái* liệt kê đúng 3 nhóm đó — ở dạng không lọc: *Đã phê duyệt 5 · Đang thực hiện 1 · Hoàn thành 1*, **cộng bằng tổng 7**.

**Điểm mâu thuẫn trong SRS v3.5**

Hai chỗ trong chính đặc tả nói khác nhau:

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:897` — Input đặc thù FR-IX-20:
  `| 1 | trang_thai_ct | text | N | DANG_THUC_HIEN / HOAN_THANH | — | Chọn |` ⇒ chỉ **2** giá trị.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:82` — Processing chung bước 4: *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* ⇒ tập dữ liệu vào báo cáo **có** nhóm *đã duyệt*.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:907` — `| 1 | tong_ct | number | Luôn | Tổng số CT |` ⇒ muốn tổng khớp thì phải đếm cả nhóm *đã duyệt*.

**Câu hỏi cần BA xác nhận**

Bộ lọc *Trạng thái chương trình* của báo cáo này đúng ra có **2** hay **3** giá trị? Nếu là **2**, thì `tong_ct` (`:907`) có còn bao gồm các chương trình *Đã phê duyệt* không — vì hiện tổng **7** lớn hơn hẳn tổng của 2 nhóm còn lại (1 + 1 = 2)?

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi, vì đây là hai chỗ trong chính đặc tả nói khác nhau chứ không phải phần mềm làm sai một quy định rõ ràng.
- Nếu BA chốt là lỗi phần mềm, QA mở dòng mới trên tab `bug` theo quy tắc mã `SLCTHT_QA01` trong đợt kế tiếp.

---

<!-- ========================= MỤC 4 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `CTTDVQL_04` (ghi nhận ngoài phạm vi) — Nhãn kỳ báo cáo trong tệp Excel in mã nội bộ (`KHOANG`) thay vì chữ tiếng Việt như trên màn

**Bối cảnh testcase**

- Dòng Excel: **272**, tab `bug`, mã TC `CTTDVQL_04`. Màn *Báo cáo thống kê → **BC Chương trình theo đơn vị*** (FR-IX-21/UC144), khi kiểm chức năng Xuất Excel.
- **Đối tác KHÔNG nêu điểm này** — không thuộc case nào của bảng theo dõi, **không** kéo verdict của `CTTDVQL_04`.
- Đo 2026-08-06 13:02–13:03, bản dựng **V1.0.8**, tài khoản `cbnv_tw_04`.

**Kết quả verify UI hiện tại**

Dòng thứ hai trong tệp Excel xuất ra:

| Kỳ báo cáo chọn trên màn | Màn hiển thị | Dòng thứ hai trong tệp Excel |
|---|---|---|
| Năm | *Kỳ: Năm* | *Kỳ báo cáo: **Năm** (từ 01/01/2026 đến 31/12/2026)* ✔ |
| Khoảng tùy chọn | *Kỳ: Khoảng* | *Kỳ báo cáo: **KHOANG** (từ 01/02/2026 đến 31/12/2026)* ✖ |

Tức cùng một tệp, cùng một chỗ, khi thì in nhãn tiếng Việt khi thì in **mã nội bộ viết hoa không dấu**. Tệp này là bản người dùng gửi ra ngoài (đính kèm báo cáo, nộp lên cấp trên) nên chữ trong đó là chữ đối ngoại.

- Bằng chứng: nội dung đầy đủ 3 tệp xuất ở [`../../thu-QLTLPLCVV_15-2026-08-06/image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt`](../../thu-QLTLPLCVV_15-2026-08-06/image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt)
  · tệp gốc [`../../thu-QLTLPLCVV_15-2026-08-06/testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx`](../../thu-QLTLPLCVV_15-2026-08-06/testfiles/BaoCaoCtTheoDonVi_20260806_1303.xlsx) (kỳ Khoảng) và [`../../thu-QLTLPLCVV_15-2026-08-06/testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx`](../../thu-QLTLPLCVV_15-2026-08-06/testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx) (kỳ Năm)
  · ảnh màn lúc chọn kỳ Khoảng: [`../../thu-QLTLPLCVV_15-2026-08-06/image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png`](../../thu-QLTLPLCVV_15-2026-08-06/image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png).

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1092` — nội dung phần đầu tệp xuất: chỉ đòi *"chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"*, **không** nói nhãn kỳ phải là nhãn tiếng Việt hay mã.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:95` — Output chung: `| 2 | ky_bao_cao | text | Luôn | Kỳ đã chọn |` — đọc theo nghĩa thường thì *"Kỳ đã chọn"* là **cái người dùng đã chọn trên màn** (tức *"Khoảng"*), nhưng câu chữ không đủ dứt khoát để chấm phần mềm sai.

⇒ Đặc tả **im lặng**, không đủ căn cứ kết luận phần mềm vi phạm một quy định rõ ràng.

**Câu hỏi cần BA xác nhận**

Nhãn kỳ báo cáo in trong tệp Excel/PDF phải là **nhãn tiếng Việt như trên màn** (*Năm · Quý · Tháng · Khoảng*) hay chấp nhận in **mã nội bộ** (`NAM` · `QUY` · `THANG` · `KHOANG`)? Nếu chốt là nhãn tiếng Việt thì cần áp cho **mọi** loại báo cáo dùng chung chức năng xuất, không riêng màn này.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi của đối tác.
- Nếu BA chốt phải là nhãn tiếng Việt, QA mở dòng mới trên tab `bug` theo quy tắc mã `CTTDVQL_QA01` trong đợt kế tiếp.

---

<!-- ========================= MỤC 5 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `CTTTG_04` (ghi nhận ngoài phạm vi) — "BC Chương trình theo thời gian" có thống kê ngân sách không?

**Bối cảnh testcase**

- Dòng Excel: **281**, tab `bug`, mã TC `CTTTG_04`. Màn *Báo cáo thống kê → **BC Chương trình theo thời gian*** (FR-IX-23/UC146).
- **Đối tác KHÔNG nêu điểm này** — không thuộc case nào của bảng theo dõi, **không** kéo verdict của `CTTTG_04`.
- Đo 2026-08-06 14:30–14:36, bản dựng **V1.0.8** — bó mã `assets/index-DIABnbIr.js`, tài khoản `cbnv_tw_04`.

**Kết quả verify UI hiện tại**

- Báo cáo hiện **3 thẻ**: *Tổng chương trình toàn kỳ = 6* · *Tổng DN toàn kỳ = 0* · **Tổng ngân sách toàn kỳ = 250.000.000**.
- Biểu đồ có thêm đường *Tổng ngân sách*; bảng *Theo kỳ* có cột *Tổng ngân sách*; tệp Excel xuất ra cũng có khối *Tổng ngân sách toàn kỳ* và cột *Tổng ngân sách (₫)*.
- Bằng chứng: ảnh màn [`../../thu-QLTLPLCVV_15-2026-08-06/image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png`](../../thu-QLTLPLCVV_15-2026-08-06/image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png)
  · nội dung đầy đủ các tệp xuất ở [`../../thu-QLTLPLCVV_15-2026-08-06/image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt`](../../thu-QLTLPLCVV_15-2026-08-06/image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt)
  · tệp gốc [`../../thu-QLTLPLCVV_15-2026-08-06/testfiles/CTTTG_04-dang1-bandung-moi-DIABnbIr.xlsx`](../../thu-QLTLPLCVV_15-2026-08-06/testfiles/CTTTG_04-dang1-bandung-moi-DIABnbIr.xlsx).

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1016`–`:1020` — Output đặc thù của FR-IX-23 chỉ liệt kê **3** mục: `trend_data[]` `{ky_label, so_ct}` · `chart_type = LINE` · `tong_ct`. **Không** có mục ngân sách.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1018` cho thấy khi BA muốn **bỏ** một mục thì có ghi rõ: *"[CTTLV_04 chốt 2026-07-24: **bỏ so_dn** …]"*. Với ngân sách thì **không có câu nào** như vậy.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:944` — loại BC anh em **FR-IX-21** (*BC Chương trình theo đơn vị*) **có** `tong_ngan_sach` trong danh sách đầu ra.

⇒ Đặc tả **im lặng** cho riêng loại BC này: không liệt kê, nhưng cũng không bỏ.

**Câu hỏi cần BA xác nhận**

*BC Chương trình theo thời gian* có thống kê **ngân sách** không?

1. Nếu **có** → bổ sung `tong_ngan_sach` (và cột ngân sách theo kỳ) vào danh sách đầu ra `:1016`–`:1020` để đặc tả khớp phần mềm.
2. Nếu **không** → phần mềm đang hiện thừa; cần ghi câu bỏ vào `:1016`–`:1020` giống cách đã làm với `so_dn` ở `:1018`, rồi Dev FE gỡ khỏi thẻ + biểu đồ + bảng + tệp xuất.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi và **chưa** thêm dòng mới trên bảng theo dõi của đối tác. Nếu BA chốt là hiện thừa, QA mở dòng mới trên tab `bug` theo quy tắc mã `CTTTG_QA01` trong đợt kế tiếp.
- **Không** đưa vào file này 2 điểm khác trên cùng màn vì đã đủ căn cứ đặc tả nên thuộc diện mở phiếu lỗi: (a) báo cáo vẫn thống kê *Số DN* dù `:1018` đã chốt bỏ `so_dn`; (b) AC `:1023` (*"chọn 12 tháng → hiển thị biểu đồ trend"*) không với tới được bằng giao diện. Chi tiết ở [`../../thu-QLTLPLCVV_15-2026-08-06/tieuchi/CTTTG_04.md`](../../thu-QLTLPLCVV_15-2026-08-06/tieuchi/CTTTG_04.md) mục 7.

---

<!-- ========================= MỤC 6 — DẠNG B′ ========================= -->

## `KTHSYCHTPL_11` — Nhãn lựa chọn kết luận "Đạt — chuyển sang phân công" hứa một việc mà hệ thống cố ý không làm

**Bối cảnh testcase**

- Dòng Excel: **45**, tab `bug`, mã TC `KTHSYCHTPL_11`. Verdict của case là **Pass** — mục này **không** làm đổi verdict, nêu riêng vì đặc tả im lặng. Điểm này **phát sinh khi verify**, đối tác KHÔNG nêu.
- Nội dung kiểm tra: cán bộ nghiệp vụ mở chi tiết vụ việc → phiếu **"Kiểm tra hồ sơ"** → ô **Kết luận**.
- **Vì sao đáng hỏi:** đây đúng là điều đối tác đã hiểu nhầm — kỳ vọng ghi trong phiếu UAT của `KTHSYCHTPL_11` là *"Hệ thống chuyển trạng thái hồ sơ: Đang kiểm tra → Đã phân công"*. BA đã chốt ngày **2026-07-16** rằng kỳ vọng đó không đúng (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:22`). Nhưng nhãn trên màn hiện **vẫn đang nói y như kỳ vọng đã bị bác**, nên người dùng tiếp theo rất dễ hiểu nhầm lại và mở phiếu lỗi lặp lại.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, Chrome DevTools MCP, tài khoản `cbnv_dp_01` (vai trò **CB_NV_DP**, cấp Địa phương), bó mã FE `assets/index-CNwX9JjX.js`.
- Ô Kết luận có đúng 3 lựa chọn: **"Đạt — chuyển sang phân công"** · "Không đạt — từ chối hồ sơ" · "Yêu cầu bổ sung".
- Chọn "Đạt" rồi Xác nhận → hệ thống **giữ nguyên** trạng thái **"Đang kiểm tra"** (đúng đặc tả), và thông báo hiện lên lại ghi **"Kiểm tra hồ sơ đạt — sẵn sàng phân công"** — tức **thông báo nói đúng**, chỉ có **nhãn trong ô chọn** là nói "chuyển sang phân công".
- Vụ việc chỉ sang "Đã phân công" sau khi cán bộ bấm [Phân công], chọn người xử lý và xác nhận.
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/KTHSYCHTPL_11-02-phieu-kiem-tra-6-hang-muc-3-lua-chon-ket-luan.png` (ô Kết luận bung ra đủ 3 lựa chọn) · `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/KTHSYCHTPL_11-03-ngay-sau-luu-Dat-badge-van-Dang-kiem-tra.png` (ngay sau khi lưu Đạt, badge vẫn "Đang kiểm tra")

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. Đặc tả chỉ quy định **giá trị** của trường kết luận (`DAT` / `KHONG_DAT` / `YEU_CAU_BO_SUNG`), **không** quy định chữ hiển thị của từng lựa chọn trên màn.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:522`

2. Đặc tả quy định rõ **hành vi**: kết luận Đạt làm vụ việc *sẵn sàng phân công* nhưng **vẫn giữ** "Đang kiểm tra"; chỉ chuyển "Đã phân công" khi đã chọn người/tổ chức xử lý. Hệ thống **làm đúng hành vi**, nhưng **nhãn lựa chọn** lại mô tả một việc khác với việc nó làm.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:541`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:564`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2288`

⇒ Không có dòng nào chốt chữ cho nhãn này, QA không tự kết luận đúng/sai được.

**Câu hỏi cần BA xác nhận**

Nhãn lựa chọn kết luận Đạt **có cần đổi chữ** cho khớp hành vi đã chốt hay không?

1. **Hướng 1 — đổi nhãn:** BA chốt giúp chữ chuẩn (gợi ý theo đúng ngôn ngữ đặc tả `:541` và đúng chữ thông báo hệ thống đang dùng: **"Đạt — sẵn sàng phân công"**).
2. **Hướng 2 — giữ nguyên nhãn hiện tại:** xin xác nhận để QA ghi thành **quy ước đã chốt**, các vòng UAT sau không mở lại phiếu ở điểm này.

**Đề xuất QA tạm thời**

- Chưa có trả lời của BA: QA **không** log thành lỗi (đặc tả im lặng về chữ nhãn), giữ verdict `KTHSYCHTPL_11` = **Pass**.
- Nếu BA chốt **đổi nhãn** → mở 1 dòng lỗi mới mức **Minor**, owner **Dev FE**, chỉ sửa chữ hiển thị, không đụng hành vi.
- Nếu BA chốt **giữ nhãn** → ghi vào tiêu chí case như một mục "không được chấm Fail vì", đóng lại vĩnh viễn.

---

<!-- ========================= MỤC 7 — DẠNG B ========================= -->

## `TKHSYCHTPL_03` — Mã của mức "Sắp hết hạn": `SAP_HET` hay `SAP_HET_HAN`?

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case là **Pass** — mục này **không** làm đổi verdict.
- Nội dung kiểm tra: cán bộ nghiệp vụ (`CB_NV_TW`) đặt ô lọc **"Mức SLA" = "Sắp hết hạn"** trên màn **Vụ việc HTPL / Danh sách** (`SCR-V.I-01`) rồi bấm [Tìm kiếm].
- Điểm phát sinh: cùng **một** mức cảnh báo đang được đặt **hai mã khác nhau** ở hai chỗ trong bộ đặc tả.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, Chrome DevTools MCP, tài khoản `cbnv_tw_01` (vai trò **CB_NV_TW**, cấp TW), bản dựng `HTPLDN · V1.0.8`.
- Ô lọc bung ra **đúng 4 lựa chọn**; chọn "Sắp hết hạn" → giao diện gửi lên **`mucSla=SAP_HET`**, máy chủ trả **HTTP 200** và **2 bản ghi**, không có thông báo lỗi nào.
- Gọi thẳng máy chủ bằng mã còn lại: `mucSla=SAP_HET_HAN` → **HTTP 422**, `ERR-VAL-SYS-00-01`, nội dung *"mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG"* ⇒ Máy chủ hiện chỉ chấp nhận `SAP_HET`.
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/TKHSYCHTPL_03-01-dropdown-Muc-SLA-4-lua-chon.png` · `…/image/TKHSYCHTPL_03-03-Sap-het-han-lan1-ra-2-ket-qua-khong-loi.png` · `…/image/TKHSYCHTPL_03-04-Sap-het-han-cot-Canh-bao-thoi-han-dung-muc.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Nhóm **Vụ việc** ghi mã là **`SAP_HET`**:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1644` — ô lọc "Mức SLA": `BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2031` — ràng buộc thực thể: `CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG')`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1516` — bảng ánh xạ: `` `SAP_HET` | Sắp hết hạn | Vàng ``

2. Nhóm **Báo cáo**, nhóm **Hỏi đáp** và **bản ghi quyết định của BA** lại ghi **`SAP_HET_HAN`**:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:245` — tham số `muc_sla`: `BINH_THUONG / SAP_HET_HAN / QUA_HAN / QUA_HAN_NGHIEM_TRONG`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:979` — bảng mức cảnh báo: `SAP_HET_HAN | <= 50% còn lại | Vàng | Thông báo CB NV`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1043` và `:1107` — cột và nhãn cảnh báo thời hạn, cùng dùng `SAP_HET_HAN`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:1317` — mục sửa đổi **BR-SLA-02**, ghi rõ **cite BA 2026-05-04**: bốn mức mang mã `BINH_THUONG/SAP_HET_HAN/QUA_HAN/QUA_HAN_NGHIEM_TRONG`

**Câu hỏi cần BA xác nhận**

Mức cảnh báo **"Sắp hết hạn"** phải mang mã chuẩn nào trên toàn hệ thống?

1. **Hướng 1 — `SAP_HET`** (theo nhóm Vụ việc): giữ nguyên hiện trạng của màn Vụ việc; phải rà lại nhóm Báo cáo và nhóm Hỏi đáp cùng bản ghi quyết định `BR-SLA-02` cho khớp.
2. **Hướng 2 — `SAP_HET_HAN`** (theo `BR-SLA-02` bản BA chốt 2026-05-04, nhóm Báo cáo và nhóm Hỏi đáp): phải sửa nhóm Vụ việc (cả ô lọc, ràng buộc thực thể lẫn dữ liệu đang lưu).

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: dù BA chọn mã nào, cả hai bản đặc tả đều đòi ô lọc phải **trả danh sách theo mức đã chọn**, và **cả hai** bảng Error Handling của màn này (`srs-fr-05-vu-viec.md:149` và `:692-693`) đều **không có** mục lỗi nào cho giá trị mức SLA. Hiện trạng đã đáp ứng yêu cầu nghiệp vụ đó ⇒ giữ **Pass**.
- QA **không tự đề xuất đổi mã**: đổi theo hướng 1 thì bộ lọc bên Báo cáo và Hỏi đáp lệch theo; đổi theo hướng 2 thì phải chuyển đổi dữ liệu đang lưu của Vụ việc. Đây là quyết định phạm vi hệ thống, thuộc BA.
- Sau khi BA chốt: hướng 2 → mở phiếu riêng cho việc đồng bộ mã + chuyển đổi dữ liệu, owner `Dev BE`; hướng 1 → mở phiếu sửa đặc tả, owner `BA`.

---

<!-- ========================= MỤC 8 — DẠNG B ========================= -->

## `TKHSYCHTPL_03` — Bộ lọc chỉ chạy khi bấm [Tìm kiếm], trong khi đặc tả ghi "change → filter"

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case là **Pass** — mục này **không** làm đổi verdict. Điểm này **phát sinh khi verify**, đối tác KHÔNG nêu.
- Nội dung kiểm tra: thanh bộ lọc trên màn **Vụ việc HTPL / Danh sách** (`SCR-V.I-01`).
- Điểm phát sinh: hai hàng **trong cùng một bảng thành phần màn hình** mô tả hai cách kích hoạt lọc khác nhau.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, tài khoản `cbnv_tw_01`, bản dựng `HTPLDN · V1.0.8`.
- Chọn xong một mức trong ô "Mức SLA" mà **chưa** bấm [Tìm kiếm]: đếm được **0** yêu cầu danh sách gửi đi, bảng vẫn giữ nguyên 52 bản ghi chưa lọc. Đo lại bằng **hai cách thao tác khác nhau** (chuột và bàn phím) đều cho cùng kết quả.
- Chỉ khi bấm **[Tìm kiếm]** thì mới có **đúng 1** yêu cầu `GET /api/v1/vu-viecs?mucSla=…` và bảng mới đổi.
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/TKHSYCHTPL_03-02-da-chon-Sap-het-han-truoc-khi-bam-Tim-kiem.png` (đã chọn mức, bảng chưa đổi) · `…/image/TKHSYCHTPL_03-09-lan2-sau-tai-lai-da-chon-Sap-het-han-bang-ban-phim.png` (chọn bằng bàn phím, bảng vẫn chưa đổi) · `…/image/TKHSYCHTPL_03-03-Sap-het-han-lan1-ra-2-ket-qua-khong-loi.png` (sau khi bấm [Tìm kiếm] thì bảng đổi)

**Điểm mâu thuẫn trong SRS v3.5**

1. Hàng 9 của bảng thành phần đặt hành vi ô "Mức SLA" là **`change → filter`** — đổi giá trị là lọc ngay. Bảy hàng khác của cùng thanh lọc (`:1639` → `:1645`) cũng ghi `change → filter`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1644`

2. Nhưng hàng 11 của **chính bảng đó** lại liệt kê một thành phần riêng — **"Nút Tìm kiếm / Xóa bộ lọc"** — với hành vi **`click → query / reset`**, điều kiện hiển thị **"Luôn"**. Nếu mọi ô đã lọc ngay khi đổi giá trị thì nút này không còn việc gì làm.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1646`

**Câu hỏi cần BA xác nhận**

Trên thanh lọc của `SCR-V.I-01`, đổi giá trị một ô lọc thì danh sách phải **lọc ngay**, hay phải **chờ cán bộ bấm [Tìm kiếm]**?

1. **Hướng 1 — lọc ngay khi đổi giá trị** (theo hàng 9): hiện trạng đang **thiếu** hành vi này; nút [Tìm kiếm] chỉ còn vai trò chạy lại.
2. **Hướng 2 — chờ bấm [Tìm kiếm]** (theo hàng 11): hiện trạng **đúng**; cần sửa cột "Hành vi" của các hàng ô lọc trong đặc tả cho khớp, tránh vòng UAT sau lại mở phiếu ở điểm này.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: đối tác không nêu vế này, và chính đối tác cũng thao tác theo hướng 2 (chọn mức rồi bấm [Tìm kiếm]) nên phép đo của case không bị ảnh hưởng.
- Nếu BA chọn hướng 1 → mở 1 phiếu mức **Medium**, owner `Dev FE`.
- Nếu BA chọn hướng 2 → cập nhật cột "Hành vi" của các hàng ô lọc trong `SCR-V.I-01`, owner `BA`.
- **Lưu ý phạm vi:** cùng hiện tượng đã ghi nhận ở màn **Biểu mẫu** (`SCR-VII-02`) — nay là **Mục 17** của chính file này mục 1.2. Nếu BA chốt, nên chốt **một quy ước chung cho mọi thanh lọc** thay vì từng màn.

---

<!-- ========================= MỤC 9 — DẠNG B′ ========================= -->

## `TKHSYCHTPL_03` — Hồ sơ chưa có thời hạn xử lý vẫn lọt bộ lọc "Bình thường" và hiện dấu "—"

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case là **Pass** — mục này **không** làm đổi verdict. Điểm này **phát sinh khi verify**, đối tác KHÔNG nêu.
- Nội dung kiểm tra: cột **"Cảnh báo thời hạn"** và ô lọc **"Mức SLA"** trên màn **Vụ việc HTPL / Danh sách**.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, tài khoản `cbnv_tw_01`, bản dựng `HTPLDN · V1.0.8`.
- Lọc "Mức SLA" = **"Bình thường"** trả **38** bản ghi. Trong đó **2** bản ghi — `VV-BTP-TW-20260731-002` và `VV-BTP-TW-20260712-002` — đều ở trạng thái **Mới tạo**, **chưa có ngày tiếp nhận** nên **chưa có thời hạn xử lý**, và cột "Cảnh báo thời hạn" hiện dấu **"—"** thay vì một trong bốn nhãn.
- Đọc lại từ máy chủ: hai bản ghi này mang `mucDoCanhBao = BINH_THUONG` (đúng **giá trị mặc định** của trường theo đặc tả), `deadline = null`, `ngayTiepNhan = null` ⇒ giao diện và máy chủ **khớp nhau**, việc chúng lọt bộ lọc "Bình thường" là **nhất quán với dữ liệu đang lưu**, không phải lỗi hiển thị.
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/TKHSYCHTPL_03-05-Binh-thuong-trang1-20-dong-tren-38.png` · `…/image/TKHSYCHTPL_03-06-Binh-thuong-trang2-18-dong-21-38.png`

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. Trường mức cảnh báo có cột "Bắt buộc" = **`N`** và **mặc định `'BINH_THUONG'`** ⇒ đặc tả **cho phép** bản ghi chưa được tính mức, và tự động gán nó vào nhóm "Bình thường".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2031`

2. Công việc tự động **chỉ quét vụ việc đang hoạt động** (`DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `DA_PHAN_CONG`, `DANG_XU_LY`, `CHO_PHE_DUYET`) ⇒ hồ sơ **Mới tạo** không nằm trong diện được tính mức.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1436`

3. Mô tả cột này chỉ có **4 mức**, không nói hồ sơ chưa tính được mức thì hiện gì và thuộc nhóm lọc nào.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1656`

⇒ Đặc tả **không có dòng nào** chốt: hồ sơ chưa có thời hạn xử lý thì (i) hiện gì ở cột cảnh báo và (ii) có được coi là "Bình thường" khi lọc hay không.

**Câu hỏi cần BA xác nhận**

Hồ sơ **chưa có thời hạn xử lý** (chưa tiếp nhận) phải được đối xử thế nào trên màn danh sách?

1. **Hướng 1 — coi là "Bình thường"**: giữ nguyên hiện trạng — lọt bộ lọc "Bình thường", cột cảnh báo hiện "—".
2. **Hướng 2 — đứng ngoài 4 mức**: không lọt bất kỳ mức nào của bộ lọc "Mức SLA"; cột cảnh báo vẫn hiện "—".

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: đặc tả im lặng, và tiêu chí chấm của case đã chốt trước khi đo là không lấy điểm này để chấm Fail.
- Nếu BA chọn hướng 2 → mở 1 phiếu mức **Minor**, owner `Dev BE` (loại hồ sơ chưa có thời hạn khỏi bộ lọc mức).
- Nếu BA chọn hướng 1 → ghi thành quy ước đã chốt để các vòng UAT sau không mở lại phiếu ở điểm này.

---

<!-- ========================= MỤC 10 — DẠNG B′ ========================= -->

## `CNKQHT_07` — Chữ trên thông báo sau khi cập nhật kết quả: "Đã cập nhật kết quả" hay "Đã cập nhật kết quả hỗ trợ"?

**Bối cảnh testcase**

- Dòng Excel: **62**, tab `bug`, mã TC `CNKQHT_07`. Verdict của case là **Pass** — mục này **không** làm đổi verdict.
- Nội dung kiểm tra: người được phân công bấm **[Cập nhật kết quả]** trên màn chi tiết vụ việc.
- Ô "Kết quả mong đợi" của phiếu UAT ghi **"Đã cập nhật kết quả hỗ trợ"**.
- Đối tác chỉ phản ánh vế **thông báo cho cán bộ nghiệp vụ**; chữ trên màn thuộc vế đối tác **không** nêu.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026** trên bản dựng `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified 06/08/2026 14:13:15` giờ VN.
- Sau khi bấm [Cập nhật kết quả], thông báo trên màn hiện đúng **1 khung · 1 mốc giờ**, nguyên văn: **"Đã cập nhật kết quả"**. Lặp lại giống hệt ở cả **4 lần bấm, trên 3 hồ sơ khác nhau**.
- So với phiếu UAT: lệch 1 chữ ("hỗ trợ").
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/cnkqht07-04-d1-nhom6-sau-cap-nhat-15h45.png` · `…/image/cnkqht07-15-d1b-form-khong-tep-khong-ghichu-truoc-khi-bam.png`

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. FR-V.I-15 §Processing và §Postconditions **không có dòng nào** quy định chữ hiển thị trên màn sau khi lưu kết quả.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1100-1114`

2. Bảng "Thông báo riêng `SCR-V.I-03`" **không có dòng** cho thao tác "Cập nhật kết quả hỗ trợ"; dòng gần nhất (`:1782`) thuộc FR-V.I-16 — một chức năng khác.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1773-1785`

⇒ Không có căn cứ đặc tả để chấm chữ hiện tại là đúng hay sai.

**Câu hỏi cần BA xác nhận**

Chữ trên thông báo sau khi cập nhật kết quả hỗ trợ nên chốt theo hướng nào?

1. **Hướng 1 — giữ nguyên "Đã cập nhật kết quả"**: coi ô Kết quả mong đợi của phiếu UAT là diễn đạt tự do, không phải yêu cầu.
2. **Hướng 2 — đổi thành "Đã cập nhật kết quả hỗ trợ"** cho khớp phiếu UAT và khớp tên hộp thoại *"Cập nhật kết quả hỗ trợ"*.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `CNKQHT_07`.
- Nếu BA chọn hướng 2 → mở 1 phiếu mức **Trivial**, owner `Dev FE` (sửa chuỗi hiển thị).
- Nếu BA chọn hướng 1 → ghi thành quy ước để các vòng UAT sau không mở lại phiếu ở điểm này.

---

<!-- ========================= MỤC 11 — DẠNG B′ ========================= -->

## `CNKQHT_07` — Cập nhật kết quả lần sau mà không đính tệp thì tệp của lần trước còn hay mất?

**Bối cảnh testcase**

- Dòng Excel: **62**, tab `bug`, mã TC `CNKQHT_07`. Verdict của case là **Pass** — mục này **không** làm đổi verdict. Điểm này **phát sinh khi verify**, đối tác KHÔNG nêu (đây là vế "lưu nội dung, tệp và ghi chú").
- Nội dung kiểm tra: cập nhật kết quả **nhiều lần** cho cùng một vụ việc.
- Cùng bản dựng và cùng phép đo với Mục 10.

**Kết quả verify UI hiện tại**

- Vụ việc `VV-BTP-TW-20260806-003` được cập nhật kết quả **2 lần**: lần đầu có đính 1 tệp, lần sau chỉ nhập nội dung và **không** đính tệp nào.
- Sau lần sau, Nhóm 6 hiện **nội dung mới** nhưng **vẫn giữ tệp của lần đầu**. Không có thông báo nào cho người thao tác biết tệp cũ được giữ lại.
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/cnkqht07-16-d1b-nhom6-sau-cap-nhat-khong-tep-16h06.png`

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. Tệp kết quả chỉ được khai là đầu vào **tùy chọn**; không nói lần cập nhật sau mà bỏ trống thì tệp cũ bị thay, bị xóa hay được giữ.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1094-1096`

2. Các bước *"Tạo/cập nhật `KET_QUA_VU_VIEC`"* và *"Lưu tài liệu kết quả"* cũng không mô tả nhánh "không có tệp mới".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1104-1105`

⇒ Đặc tả không chốt hành vi giữ/thay/xóa tệp khi cập nhật nhiều lần.

**Câu hỏi cần BA xác nhận**

Khi người được phân công cập nhật kết quả lần thứ hai trở đi mà **không đính tệp mới**, hệ thống nên:

1. **Hướng 1 — giữ nguyên tệp cũ** (hiện trạng).
2. **Hướng 2 — bỏ tệp cũ** để hồ sơ luôn khớp đúng lần cập nhật mới nhất.
3. **Hướng 3 — giữ cả hai** dưới dạng danh sách nhiều tệp có mốc thời gian.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `CNKQHT_07`.
- Nếu BA chọn hướng 2 hoặc 3 → mở 1 phiếu mức **Minor**, owner `Dev BE` + `Dev FE`.
- Nếu BA chọn hướng 1 → ghi thành quy ước đã chốt.

---

<!-- ========================= MỤC 12 — DẠNG B ========================= -->

## `DGKQHTVV_01` — Vụ việc đã ở "Đã đánh giá" thì cán bộ nghiệp vụ còn được vào đánh giá không?

**Bối cảnh testcase**

- Dòng Excel: **64**, tab `bug`, mã TC `DGKQHTVV_01`. Verdict của case là **Reopen** vì nhánh doanh nghiệp không có đường vào chức năng đánh giá — mục này **không** làm đổi verdict đó, và cũng **không** phải căn cứ của verdict.
- Nội dung kiểm tra: đánh giá kết quả hỗ trợ vụ việc (Nhóm 8 trên màn chi tiết vụ việc), `FR-V.I-17 / UC67`.
- Đặc tả cho phép **hai loại người đánh giá độc lập nhau** — cán bộ nghiệp vụ và doanh nghiệp — mỗi loại chấm đúng 1 lần cho 1 vụ việc. Lần chấm đầu tiên đẩy vụ việc sang **"Đã đánh giá"**. Vậy **bên còn lại** vào chấm khi vụ việc **đang ở "Đã đánh giá"** thì có được không?
- Bản dựng đã đo cho case này: `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `last-modified 06/08/2026 14:13:15` giờ VN (**khác bó mã đầu lô** — có triển khai mới xen giữa).

**Kết quả verify UI hiện tại**

- Vụ việc `VV-QA-008` đang mang nhãn **"Đã đánh giá"** nhưng **không kèm bản ghi đánh giá nào**; cán bộ nghiệp vụ mở chi tiết ra thì **không thấy đường vào đánh giá**, Nhóm 8 vẫn ở trạng thái rỗng ⇒ hệ thống đang chạy theo hướng **`:1751`** (chỉ mở ở "Hoàn thành").
- **Chưa dựng được** đúng tình huống "một bên chấm trước, bên còn lại vào chấm": muốn có nó phải có đánh giá của phía doanh nghiệp, mà phía doanh nghiệp đang bị chặn hoàn toàn (đã log ở [`../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md`](../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md) — `BUG-VV-DGKQHTVV-01`).
- Evidence: `../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/DGKQHTVV_01-10-D3-VV-QA-008-trang-thai-Da-danh-gia-khong-co-nut-Danh-gia.png`

**Điểm mâu thuẫn trong SRS v3.5**

> Màn chi tiết vụ việc `SCR-V.I-03` có **2 chế độ** — *chế độ cán bộ* và *chế độ doanh nghiệp* (`:1791`). Phải tách hai chế độ ra mới thấy mâu thuẫn nằm ở đâu: **phía doanh nghiệp đặc tả nói nhất quán, mâu thuẫn nằm gọn trong phía cán bộ.**

1. **Cấp use case (áp cho CẢ HAI vai trò) — nói ĐƯỢC.** `PRE-02` cho phép vụ việc ở `HOAN_THANH` **hoặc `DA_DANH_GIA``; `PRE-03` khai `Role ∈ {CB_NV, DN}`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1197` — `| PRE-02 | VV ở trạng thái HOAN_THANH hoặc DA_DANH_GIA |`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1198` — `| PRE-03 | Role ∈ {CB_NV, DN} (theo CSV UC67) |`

2. **Bảng thành phần chế độ cán bộ — nói ĐƯỢC.** Accordion 8 có điều kiện hiển thị *"Khi VV ở HOAN_THANH hoặc DA_DANH_GIA"*, tác nhân *"CB NV/DN nhập trực tiếp"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1734`

3. **Nhưng bảng NÚT hành động theo trạng thái của chính chế độ cán bộ (#13) — nói KHÔNG.** Bảng này liệt kê từng trạng thái, và chỉ có **một** dòng cho chức năng đánh giá: `| HOAN_THANH | [Đánh giá] (gộp MH-05.9) | CB NV/DN | Mở Accordion 8. Gửi → DA_DANH_GIA |`. **Không có** dòng nào cho trạng thái `DA_DANH_GIA` ⇒ ở `DA_DANH_GIA` cán bộ **không có nút nào để mở Accordion 8**, dù mục 2 nói accordion phải hiện.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1751`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1740-1754` (toàn bảng, để BA thấy không sót dòng nào)

4. **Đối chứng — phía doanh nghiệp KHÔNG mâu thuẫn.** Bảng *"Quy tắc chế độ doanh nghiệp"* nói rõ cả hai vế theo cùng một hướng: Nhóm 8 *"Cho phép nhập khi vụ việc ở 'Hoàn thành' / 'Đã đánh giá' + DN chưa đánh giá"*, và Thanh thao tác có *"**[Đánh giá]** (khi trạng thái = 'Hoàn thành' / 'Đã đánh giá' + chưa đánh giá)"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1791` — *"SCR-V.I-03 có 2 chế độ — chế độ cán bộ … và chế độ doanh nghiệp"*
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1809` — Nhóm 8 ở chế độ DN
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1811` — Thanh thao tác ở chế độ DN

5. **Ràng buộc dữ liệu dự trù ĐỦ 2 đánh giá cho mỗi vụ việc** — *"Mỗi VV có tối đa 1 đánh giá từ CB NV và 1 từ DN — UNIQUE (vu_viec_id, loai_nguoi_danh_gia)"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2108`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2116`

⇒ **Kịch bản hỏng cụ thể:** doanh nghiệp chấm **trước** → vụ việc sang `DA_DANH_GIA` → cán bộ **mất đường vào** theo `:1751`, dù `:1197` và `:1734` cho phép và dù ràng buộc `:2108` còn chỗ trống cho đánh giá của cán bộ. Chiều ngược lại (cán bộ chấm trước) thì doanh nghiệp vẫn vào được theo `:1810`/`:1811`. Hiện trạng đo được (`VV-QA-008`) đang chạy đúng theo `:1751`.

**Câu hỏi cần BA xác nhận**

Khi vụ việc **đã ở "Đã đánh giá"** vì doanh nghiệp đã chấm, **cán bộ nghiệp vụ** vào chấm phần của mình thì:

1. **Hướng 1 — vẫn được chấm** (theo `:1197` / `:1734`, và để ràng buộc `:2108` dùng được): `:1751` **thiếu một dòng** cho trạng thái `DA_DANH_GIA` và cần bổ sung — nút [Đánh giá] phải hiện khi vụ việc ở `DA_DANH_GIA` **và** người đang xem chưa đánh giá.
2. **Hướng 2 — không được chấm** (theo `:1751`): khi đó `:1197` và `:1734` cần bỏ trạng thái `DA_DANH_GIA` **ở phía cán bộ**, và cần chốt lại ý nghĩa của ràng buộc `:2108` — vì trên thực tế mỗi vụ việc sẽ chỉ nhận được **1** đánh giá (của bên chấm trước), phần còn lại của ràng buộc không bao giờ dùng tới.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `DGKQHTVV_01`: đây là điểm đặc tả tự mâu thuẫn, không phải sai lệch so với một yêu cầu đã chốt.
- Nếu BA chọn hướng 1 → mở 1 phiếu mức **Major**, owner `Dev BE` + `Dev FE`, và ghép luôn vào lần fix `BUG-VV-DGKQHTVV-01` (cùng vùng chức năng).
- Nếu BA chọn hướng 2 → cần chốt lại luôn ý nghĩa của ràng buộc "tối đa 2 đánh giá / vụ việc", vì hướng 2 làm ràng buộc đó không bao giờ dùng tới.

---

<!-- ========================= MỤC 13 — DẠNG B ========================= -->

## `DGKQHTVV_01` — Đánh giá vụ việc xong thì điểm trung bình của tư vấn viên có phải cập nhật không?

**Bối cảnh testcase**

- Dòng Excel: **64**, tab `bug`, mã TC `DGKQHTVV_01`. Cùng chức năng `FR-V.I-17 / UC67`, cùng bản dựng và cùng đợt đo với Mục 12.
- Nội dung kiểm tra: điểm trung bình của tư vấn viên sau khi một vụ việc được đánh giá.
- Điểm phát sinh khi đọc đặc tả để dựng thước đo, **không** phải do đối tác phản ánh.

**Kết quả verify UI hiện tại**

- QA **cố ý không chấm** điểm này trong vòng verify: hai dòng đặc tả ngược nhau nên không có thước đo hợp lệ. Đã ghi thẳng vào thước đo của case là **cấm chấm Fail** vì "điểm tư vấn viên không đổi".
- Vòng này đã tạo **2 bản ghi đánh giá** hợp lệ (`VV-BTP-TW-20260806-003` và `-004`, cùng bộ điểm 9 · 8 · 10) — dữ liệu sẵn sàng để đo lại ngay khi BA chốt hướng.

**Điểm mâu thuẫn trong SRS v3.5**

1. Mục *Postconditions* của use case ghi: *"- Điểm TVV được cập nhật"* ⇒ đánh giá vụ việc **có** làm đổi điểm tư vấn viên.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1233`

2. Nhưng bảng *Processing* bước 9 của **chính use case đó** ghi: *"…nguồn dữ liệu là `DANH_GIA_SAU_VU_VIEC` (đối tượng do FR-IV quản lý), **không phải** `DANH_GIA_VU_VIEC`. **UC67 chỉ tạo `DANH_GIA_VU_VIEC`; trigger cập nhật điểm TVV nằm ở module FR-IV**"* ⇒ đánh giá vụ việc **không** làm đổi điểm tư vấn viên.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1223`

**Câu hỏi cần BA xác nhận**

Sau khi đánh giá kết quả hỗ trợ **một vụ việc**, điểm trung bình của tư vấn viên phụ trách:

1. **Hướng 1 — phải cập nhật ngay**: khi đó `:1223` cần bỏ câu *"UC67 chỉ tạo `DANH_GIA_VU_VIEC`"*, và cần chốt luôn công thức lấy từ nguồn nào.
2. **Hướng 2 — không cập nhật**: điểm tư vấn viên chỉ do đợt đánh giá của nhóm chức năng khác quyết định; khi đó `:1233` cần bỏ dòng *"Điểm TVV được cập nhật"*.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `DGKQHTVV_01`.
- BA chốt xong → bổ sung đúng **một** tiêu chí đo được vào thước đo của chức năng này cho các vòng sau (hiện đang bỏ trống có chủ ý).

---

<!-- ========================= MỤC 14 — DẠNG B′ ========================= -->

## `QLTVV_02` — Danh sách Tư vấn viên / Chuyên gia mặc định sắp xếp theo tiêu chí nào?

**Bối cảnh testcase**

- Dòng Excel: **32**, tab `bug`, mã TC `QLTVV_02` — *"Kiểm tra hiển thị bảng danh sách"*.
- Nội dung kiểm tra: vai trò **CB_NV_TW** mở **Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia** (`SCR-IV-01`), tab mặc định *"Đang hoạt động"*.
- Expected trong file UAT: *"Mặc định: hệ thống **sắp xếp theo ngày công nhận mới nhất trước**, 20 bản ghi mỗi trang"*.
- Actual đối tác ghi (vòng 1, 07/07): *"Hệ thống không mặc định sắp xếp theo ngày công nhận mới nhất"*.
- Case gộp **5 vế**. **4 vế đã hết lỗi** sau lượt đo 06/08 (không tràn/đè · hiển thị điểm đã đồng nhất · nút thao tác không xuống dòng · mặc định 20 mục/trang). Mục hỏi BA này là **vế thứ 5**, và nó chính là thứ đang giữ verdict của case ở mức **cần BA** thay vì Pass.
- Bản dựng đã đo: `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified 06/08/2026 14:13:15` giờ VN.

**Kết quả verify UI hiện tại**

- Tài khoản `cbnv_tw_02` — vai trò **CB_NV_TW**, cấp **TW** (trùng khít vai trò + cấp trên ảnh của đối tác).
- Đọc cột **"Ngày công nhận" của toàn bộ 6/6 hàng** trang 1 (không dừng ở vài hàng đầu), thứ tự hiển thị: `—` · `17/07/2026` · `12/07/2026` · `—` · `—` · `—` ⇒ **không giảm dần**, và hàng trống cũng không dồn về một phía.
- Đối chiếu bằng đường thứ hai — đọc lại chính lời gọi danh sách mà giao diện dùng: thứ tự máy chủ trả về **trùng khít** thứ tự trên màn (nên không phải giao diện xáo), và trường **ngày tạo** của dãy đó **giảm dần tuyệt đối**: `05/08/2026` → `12/07/2026 09:55` → `12/07/2026 00:11` → `30/06/2026` → `01/03/2026` → `01/02/2024`.
- ⇒ Danh sách đang sắp theo **ngày tạo bản ghi, mới nhất trước** — một tiêu chí khác với ngày công nhận.
- Evidence: `../../batch-B7-tuvan-mangluoi-2026-08-06/image/QLTVV_02-03-1920-toan-bang-cot-NgayCongNhan-khong-giam-dan.png` (toàn bảng, đọc được cả cột Ngày công nhận lẫn chân bảng) · `../../batch-B7-tuvan-mangluoi-2026-08-06/image/QLTVV_02-01-1440-cuon-phai-DiemDG-TrangThai-Ngay-HanhDong.png` · số đo đầy đủ ở [`../../batch-B7-tuvan-mangluoi-2026-08-06/ketqua-QLTVV_02.txt`](../../batch-B7-tuvan-mangluoi-2026-08-06/ketqua-QLTVV_02.txt) mục D · phản hồi máy chủ nguyên bản ở [`../../batch-B7-tuvan-mangluoi-2026-08-06/tvv-list.network-response`](../../batch-B7-tuvan-mangluoi-2026-08-06/tvv-list.network-response)

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. Đã tra **toàn bộ** `srs-fr-04-chuyen-gia-tvv.md` bằng `sắp xếp` / `sort` / `ORDER BY` / `DESC` / `mới nhất trước` → **0 kết quả**.

2. FR-IV-02 §Processing chỉ có: kiểm quyền → kết hợp điều kiện AND → **phân trang (mặc định 20/trang)**. **Không có bước sắp xếp.**

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:243-247`

3. Bảng thành phần `SCR-IV-01` (liệt kê đóng 29 thành phần) mô tả từng cột và phần phân trang, **không nói cột nào là cột sắp xếp mặc định**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1440-1457`

4. `BR-DATA-07` chỉ quy định *"Mọi danh sách sử dụng phân trang. Default: 20 rows/page, max: 100 rows/page"* — **không nói thứ tự**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2392-2394`

5. Đối chiếu cho thấy đây là chỗ **bỏ trống riêng của nhóm IV**, không phải nằm ở tài liệu khác: các nhóm khác **có** quy định thứ tự.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:904`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1132`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1665`

⇒ Không có căn cứ đặc tả để chấm phần mềm đúng hay sai ở vế này.

**Câu hỏi cần BA xác nhận**

Danh sách `SCR-IV-01` khi mở lần đầu (chưa đụng bộ lọc, chưa bấm tiêu đề cột) phải sắp theo tiêu chí nào?

1. **Hướng 1 — ngày công nhận mới nhất trước** (đúng kỳ vọng đối tác ghi trong phiếu): phải bổ sung quy định vào `FR-IV-02 §Processing` **và** nói rõ **bản ghi chưa có ngày công nhận thì xếp ở đâu** — trên màn hiện có 4/6 bản ghi bỏ trống cột này, nên nếu không chốt chỗ đứng của nhóm trống thì vòng UAT sau vẫn tranh cãi.
2. **Hướng 2 — ngày tạo mới nhất trước** (đúng hiện trạng): xin xác nhận để QA ghi thành **quy ước đã chốt** và bổ sung một dòng vào đặc tả, các vòng UAT sau không mở lại phiếu ở điểm này.
3. **Hướng 3 — tiêu chí khác** (vd theo mã tư vấn viên, theo tên): BA chốt giúp tiêu chí và chiều sắp xếp.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi: đặc tả im lặng, không có dòng nào để đối chiếu đúng/sai. Verdict case `QLTVV_02` để ở **cần BA** (4 vế còn lại đã hết lỗi, không vế nào đang lỗi).
- Nếu BA chọn **hướng 1** → mở 1 phiếu mức **Minor**, owner `Dev BE` (thêm mệnh đề sắp xếp vào truy vấn danh sách) + `BA` bổ sung dòng đặc tả kèm quy tắc cho bản ghi trống ngày công nhận.
- Nếu BA chọn **hướng 2** → owner `BA`, chỉ bổ sung một dòng vào `FR-IV-02 §Processing`; không đụng phần mềm.

---

<!-- ========================= MỤC 15 — DẠNG B′ ========================= -->

## `QLHSDNHTCP_03` — Cột cảnh báo thời hạn hiển thị gì khi hồ sơ đã kết thúc?

**Bối cảnh testcase**

- Dòng bảng: **72**, mã TC `QLHSDNHTCP_03`.
- Nội dung kiểm tra: màn **Chi trả chi phí → Danh sách** (`/chi-tra/danh-sach`, `SCR-V.II-01`), cột **"SLA"** (thành phần #16).
- Expected trong file UAT: đối tác **không** phản ánh điểm này. Cả 2 vòng của họ chỉ nói về (a) cột không giống thiết kế và (b) dữ liệu tràn sang cột "Ngày nộp" — **cả hai vế nay đều đã hết lỗi** trên bản dựng V1.0.8. Đây là điểm QA gặp khi đo, nằm trong đúng cột đang tranh chấp nên đưa ra để BA chốt, **không phải phản ánh mới của đối tác**.

**Kết quả verify UI hiện tại**

- Cột "SLA" hiện **5 loại nhãn**, trong khi mô hình cảnh báo chỉ có **4 mức**:

| Nhãn đang hiện | Số dòng | Trạng thái hồ sơ | Giá trị mức cảnh báo trong dữ liệu |
|---|---|---|---|
| "Bình thường · còn 10 ngày LV" | 1 | Đang kiểm tra | `BINH_THUONG` |
| "Sắp hết hạn · còn 6 ngày LV" | 1 | Đang kiểm tra | `SAP_HET_HAN` |
| "Quá hạn · 6 / 9 ngày LV" | 2 | Chờ tiếp nhận, Đang kiểm tra | `QUA_HAN` |
| "Quá hạn nghiêm trọng · 11…53 ngày LV" | 6 | Đang kiểm tra, Yêu cầu bổ sung, Đang đánh giá, Đã duyệt, Đang thẩm định ×2 | `QUA_HAN_NGHIEM_TRONG` |
| **"Đã hoàn thành"** ← nhãn thứ 5 | **4** | **Đã thanh toán ×2, Từ chối, Hủy** | **`BINH_THUONG`** |

- Điểm đáng chú ý: 4 dòng cuối mang nhãn **"Đã hoàn thành"** trên giao diện, nhưng dữ liệu của chính 4 bản ghi đó lại là `BINH_THUONG` — tức **giao diện không hiển thị giá trị mà dữ liệu đang mang**. Bản ghi: `CT-QAW7-CLOSED`, `CT-SEED-108` (Đã thanh toán), `CT-SEED-109` (Từ chối), `CT-SEED-110` (Hủy).
- Evidence:
  - `../../flowtest-kiemdinh/image/QLHSDNHTCP_03-danhsach-SLA-NgayNop-V108-2026-08-06.png` — 5 dòng đầu, thấy nhãn "Bình thường", "Sắp hết hạn", **"Đã hoàn thành"** (dòng `CT-QAW7-CLOSED`, trạng thái *Đã thanh toán*), "Quá hạn nghiêm trọng".
  - `../../flowtest-kiemdinh/image/QLHSDNHTCP_03-vaitro-CBPD-SLA-NgayNop-V108-2026-08-06.png` — 9 dòng cuối, thấy **3 dòng "Đã hoàn thành"** ứng với `CT-SEED-108` (*Đã thanh toán*), `CT-SEED-109` (*Từ chối*), `CT-SEED-110` (*Hủy*).

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

1. `BR-SLA-02` định nghĩa **đúng 4 mức**: `BINH_THUONG` "Bình thường" (còn >50%) · `SAP_HET` "Sắp hết hạn" (còn <50%) · `QUA_HAN` "Quá hạn" (trễ >100%) · `QUA_HAN_NGHIEM_TRONG` "Quá hạn nghiêm trọng" (trễ >200%). Câu cuối: *"Nếu không thỏa điều kiện nào thì hiển thị **'Bình thường'**"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1514-1523`

2. `SCR-V.II-01` thành phần #16 — *"4 mức cảnh báo theo BR-SLA-02: Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng"*, điều kiện hiển thị **"Luôn"**. Ràng buộc của trường `muc_do_canh_bao` cũng chỉ nhận **4 giá trị** trên.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1058`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-06-chi-tra.md:1311`

3. **Đặc tả IM LẶNG** về việc cột này hiển thị gì khi hồ sơ đã ở trạng thái kết thúc (`DA_THANH_TOAN`, `TU_CHOI`, `HUY`) — không dòng nào nói tới. Đọc thẳng `BR-SLA-02` thì 4 dòng đó phải ghi **"Bình thường"**, nhưng ghi "Bình thường" cho một hồ sơ **đã Từ chối** hoặc **đã Hủy** thì không có nghĩa về nghiệp vụ.

4. Quyết định **BA ngày 2026-07-24** cho chính mã TC này chỉ chốt: tên cột "SLA" là đúng, và phần mềm phải hiện 4 nhãn rời + số ngày. **Không nhắc tới hồ sơ đã kết thúc.**

**Câu hỏi cần BA xác nhận**

1. Với hồ sơ đã ở trạng thái kết thúc (**Đã thanh toán / Từ chối / Hủy**), cột "SLA" nên hiển thị gì:
   - **(a)** giữ nhãn **"Đã hoàn thành"** như phần mềm đang làm;
   - **(b)** hiện đúng mức cảnh báo lưu trong dữ liệu (hiện là "Bình thường");
   - **(c)** để trống / dấu "—" vì cảnh báo thời hạn không còn ý nghĩa;
   - **(d)** phương án khác?
2. Nếu chọn **(a)**: xin bổ sung nhãn thứ 5 này vào `BR-SLA-02` và vào thành phần #16 của `SCR-V.II-01` để lần sau QA có căn cứ chấm, và nói rõ nhãn này áp cho **những trạng thái nào**.
3. **Câu hỏi liên đới:** 4 hồ sơ đã kết thúc đó đang mang `muc_do_canh_bao = BINH_THUONG` trong dữ liệu — giá trị này có **đúng** không, hay khi hồ sơ kết thúc thì mức cảnh báo cần được chốt lại / để trống? (Nếu BA chọn phương án **(b)** ở câu 1 thì giá trị trong dữ liệu sẽ hiện thẳng ra giao diện, nên cần đúng.)

**Đề xuất QA tạm thời**

- Verdict `QLHSDNHTCP_03` = **cần BA**. Không chấm Pass vì cột đang tranh chấp có 1 nhãn nằm ngoài đặc tả; không chấm Reopen vì **cả 2 vế đối tác phản ánh đều đã hết lỗi** và đặc tả không quy định điểm này — chưa có việc gì để chuyển cho dev cho tới khi BA chốt.
- **Ghi chú chéo — cùng vấn đề với Mục 7, thêm một dữ kiện mới:** `BR-SLA-02` trong chính `srs-fr-06-chi-tra.md:1514-1523` ghi mã là **`SAP_HET`**, nhưng **dữ liệu chạy thật của nhóm Chi trả lại trả `SAP_HET_HAN`** (xem bảng trên, dòng "Sắp hết hạn"). Trong khi đó máy chủ nhóm Vụ việc chỉ chấp nhận `SAP_HET` và trả 422 cho `SAP_HET_HAN`. ⇒ hai nhóm đang chạy hai mã khác nhau cho cùng một mức. BA chốt **một lần cho cả hệ thống** ở Mục 7; khi chốt xong cần rà cả nhóm Chi trả, không chỉ nhóm Vụ việc và Báo cáo/Hỏi đáp.

<!-- ========================= MỤC 16 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `QLBMHD_02` (ghi nhận) — 4 ô lọc trên màn Biểu mẫu không có nhãn chữ, cả 4 đều chỉ hiện "Tất cả"

**Bối cảnh testcase**

- Dòng Excel: **138**, tab `bug`, mã TC `QLBMHD_02`. Màn *Biểu mẫu hợp đồng* `SCR-VII-02`.
- **Đối tác KHÔNG nêu điểm này** — phát sinh trong lúc verify, **không** kéo verdict của `QLBMHD_02` (đã **Pass**).
- Bản dựng **V1.0.8**, bó mã `assets/index-DIABnbIr.js`, tài khoản `cbnv_tw`.

**Kết quả verify UI hiện tại**

- Thanh lọc có **4 ô** nhưng **không ô nào có nhãn chữ** — cả 4 chỉ hiện chữ `Tất cả`. Phải mở từng ô mới biết ô nào là *Thư mục / Lĩnh vực / Loại hình / Định dạng*.
- Ảnh: [`../image/QLBMHD_02-thanh-loc-4-o-khong-nhan.png`](../image/QLBMHD_02-thanh-loc-4-o-khong-nhan.png)

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:654` — khai thành phần *"Lọc lĩnh vực / loại hình / thư mục / định dạng"*, kiểu `select`, nhưng **im lặng** về **nhãn hiển thị** của từng ô.

⇒ Đặc tả gọi tên 4 bộ lọc nhưng không nói người dùng phải nhìn thấy tên đó ở đâu.

**Câu hỏi cần BA xác nhận**

Mỗi ô lọc có **bắt buộc** phải có nhãn chữ (hoặc placeholder mang tên bộ lọc, ví dụ *"Tất cả lĩnh vực"* thay vì *"Tất cả"*) không? Nếu **có**, đây là quy ước dùng chung cho **mọi** thanh lọc trong phần mềm hay chỉ riêng màn này?

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi. Nếu BA chốt là bắt buộc, QA mở dòng mới trên tab `bug` theo quy tắc mã `QLBMHD_QA01`, owner **Dev FE**, và đề nghị BA bổ sung một dòng quy ước vào Phụ lục E §H để áp chung.

---

<!-- ========================= MỤC 17 — DẠNG B ========================= -->

## `QLBMHD_02` (ghi nhận) — Bộ lọc màn Biểu mẫu chỉ chạy khi bấm [Tìm kiếm], trong khi đặc tả ghi "change → filter"

**Bối cảnh testcase**

- Dòng Excel: **138**, tab `bug`, mã TC `QLBMHD_02`. Màn *Biểu mẫu hợp đồng* `SCR-VII-02`. Cùng lượt đo với Mục 16.
- **Đối tác KHÔNG nêu điểm này**, **không** kéo verdict (đã **Pass**).

**Kết quả verify UI hiện tại**

- Chọn giá trị ở ô lọc **không tự lọc** — danh sách giữ nguyên **27** kết quả cho tới khi bấm nút **[Tìm kiếm]**; khi đó mới phát `GET /api/v1/bieu-maus?dinhDang=XLSX…`.
- Bản dựng đang **có** nút [Tìm kiếm] và [Xóa bộ lọc].
- Bằng chứng: [`../note/resp-bieu-maus-loc-xlsx.network-response`](../note/resp-bieu-maus-loc-xlsx.network-response) · ảnh [`../image/QLBMHD_02-veB1-loc-XLSX-3-ket-qua.png`](../image/QLBMHD_02-veB1-loc-XLSX-3-ket-qua.png)

**Điểm mâu thuẫn trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:653` — `| 2 | filter-bar | Ô tìm kiếm | search-box | Từ khóa (tên, mô tả). Full-text | change → filter | luôn hiển thị |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:654` — dòng bộ lọc cũng ghi hành vi **`change → filter`**.
- Cùng bảng thành phần `:650`–`:673` **không khai** nút `Tìm kiếm` / `Xóa bộ lọc` — tức đặc tả vừa đòi lọc-ngay, vừa không cho phép tồn tại nút mà phần mềm đang có.

**Câu hỏi cần BA xác nhận**

Giữ nút **[Tìm kiếm]** (⇒ cập nhật `:653`–`:654` thành *"bấm Tìm kiếm → filter"* và bổ sung 2 dòng nút vào bảng thành phần), hay đổi sang **lọc ngay khi chọn** (⇒ Dev FE sửa mã, gỡ nút)?

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi. Đây là hai chỗ trong chính đặc tả nói khác nhau.
- **Lưu ý phạm vi:** cùng hiện tượng đã ghi ở **Mục 8** cho màn *Tra cứu hồ sơ yêu cầu HTPL* (`SCR-V.I-01`). Hai màn khác nhau, hai dòng đặc tả khác nhau, nhưng **cùng một quyết định thiết kế** — đề nghị BA chốt **một lần cho toàn hệ thống** rồi rà lại từng màn, thay vì chốt lẻ từng chỗ.

---

<!-- ========================= MỤC 18 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `QLBMHD_02` (ghi nhận) — Ô chọn Thư mục ở form Thêm biểu mẫu liệt kê cả thư mục của đơn vị khác

**Bối cảnh testcase**

- Dòng Excel: **138**, tab `bug`, mã TC `QLBMHD_02`. Form *Thêm biểu mẫu* của màn `SCR-VII-02`.
- **Đối tác KHÔNG nêu điểm này**, **không** kéo verdict (đã **Pass**).
- Điểm này **đã ghi nhận từ 25/07** ở [`../../reverify-week-3/dev-fix-reverify-round-7-2026-07-25/phat-hien-them.md`](../../reverify-week-3/dev-fix-reverify-round-7-2026-07-25/phat-hien-them.md) §5; tester khi đó quyết **không mở phiếu**. Nêu lại vì lặp lại trên bản dựng mới.

**Kết quả verify UI hiện tại**

- Ô chọn **Thư mục** liệt kê cả thư mục thuộc **đơn vị khác**. Chọn xong bấm *Thêm mới* thì máy chủ từ chối `ERR-BM-05` — *"Thư mục biểu mẫu không tồn tại hoặc không thuộc đơn vị"*.
- Đo được **1 request ↔ 1 thông báo**, **có** hiện thông báo ra màn, không nuốt lỗi ⇒ phần chặn của máy chủ **đúng** `BR-AUTH-08`.
- Bằng chứng: [`../note/req-them-bieu-mau-422.network-request`](../note/req-them-bieu-mau-422.network-request) · [`../note/resp-them-bieu-mau-422.network-response`](../note/resp-them-bieu-mau-422.network-response)

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:357` — `| E5 | Thư mục không tồn tại | ERR-BM-05 | "Thư mục đích không tồn tại" | ERROR |`
  ⇒ đặc tả **chỉ** lường tình huống *thư mục không tồn tại*; câu chữ trên phần mềm nói thêm vế *"hoặc không thuộc đơn vị"*.
- Đặc tả **không có dòng nào** nói ô chọn Thư mục phải **lọc sẵn theo đơn vị** người đăng nhập.

**Câu hỏi cần BA xác nhận**

1. Ô chọn Thư mục ở form Thêm/Sửa biểu mẫu có phải **lọc sẵn** theo đơn vị người đăng nhập không (⇒ người dùng không bao giờ chọn được thứ sẽ bị từ chối), hay giữ nguyên "cho chọn rồi máy chủ chặn"?
2. Nếu giữ nguyên: câu chữ `ERR-BM-05` ở `:357` có cần cập nhật cho khớp phần mềm (*"…hoặc không thuộc đơn vị"*) không?

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi — phần bảo vệ dữ liệu đã đúng, đây là câu hỏi về trải nghiệm và về câu chữ đặc tả.
- Nếu BA chốt phải lọc theo đơn vị, owner **Dev FE** (lọc danh sách) hoặc **Dev BE** (lọc ở endpoint trả danh sách thư mục).

---

<!-- ========================= MỤC 19 — DẠNG B ========================= -->

## `QLHSPLDN_06` (ghi nhận) — Nhật ký hệ thống xếp thao tác trên Hồ sơ pháp lý DN vào nhóm "Tư vấn"

**Bối cảnh testcase**

- Tab `bug`, mã TC `QLHSPLDN_06`. Màn *Quản trị hệ thống → Nhật ký hệ thống*, cột **Module**.
- **Đối tác KHÔNG nêu điểm này**, **không** kéo verdict (đã **Pass**).
- Bản dựng **V1.0.8**, tài khoản `cbnv_tw`.

**Kết quả verify UI hiện tại**

- Các dòng nhật ký sinh ra từ thao tác trên **Hồ sơ pháp lý doanh nghiệp** (`HO_SO_PHAP_LY_DN`) hiển thị Module = **"Tư vấn"**.
- Bằng chứng: [`../note/snap-audit-log.txt`](../note/snap-audit-log.txt) · ảnh [`../image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png`](../image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png)

**Điểm mâu thuẫn trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1387` — bộ giá trị của ô lọc `module`:
  `| 4 | module | select | N | Hỏi đáp / Đào tạo / CG-TVV / Vụ việc / Chi trả / DN / Đánh giá / Biểu mẫu / Quản trị / Báo cáo / Tư vấn / … |`
  ⇒ danh sách có **cả** `DN` **lẫn** `Tư vấn` là hai nhóm **riêng biệt**. Hồ sơ pháp lý **doanh nghiệp** thuộc nhóm `DN` theo cách đọc thông thường, nhưng phần mềm đang gán `Tư vấn`.

**Câu hỏi cần BA xác nhận**

Thao tác trên **Hồ sơ pháp lý doanh nghiệp** thuộc Module nào trong bộ giá trị ở `:1387` — **`DN`** hay **`Tư vấn`**?

1. Nếu **`DN`** → phần mềm gán sai nhóm, owner **Dev BE** (chỗ ghi nhật ký).
2. Nếu **`Tư vấn`** → đặc tả cần ghi rõ ranh giới giữa 2 nhóm để lượt kiểm thử sau không chấm sai.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi — chưa có dòng đặc tả nào ánh xạ thực thể → nhóm Module, nên chưa đủ căn cứ nói phần mềm sai.
- Ảnh hưởng tới kiểm thử: mọi case dùng bộ lọc Module để tìm dấu vết thao tác trên hồ sơ DN đang phải chọn *"Tư vấn"* — đã ghi trong [`../tieuchi/QLHSPLDN_06.md`](../tieuchi/QLHSPLDN_06.md).

---

<!-- ========================= MỤC 20 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `QLHSPLDN_07` (ghi nhận) — Sửa hồ sơ mà chỉ thêm tệp thì `ngayCapNhat` / `version` của bản ghi không đổi

**Bối cảnh testcase**

- Tab `bug`, mã TC `QLHSPLDN_07`. Màn *Hồ sơ pháp lý doanh nghiệp* — thao tác Sửa, chỉ đính thêm tệp, không đụng trường nào khác.
- **Đối tác KHÔNG nêu điểm này**, **không** kéo verdict (đã **Pass**).
- Bản dựng **V1.0.8**, tài khoản `cbnv_tw`.

**Kết quả verify UI hiện tại**

- Thêm tệp rồi lưu: tệp **có** vào (tải lại trang vẫn thấy đủ), nhưng `ngayCapNhat` và `version` của bản ghi **giữ nguyên**.
- Vế **lưu vết đã đóng**: Nhật ký hệ thống **có** dòng đúng giây bấm ⇒ hệ thống không mất dấu thao tác.
- Bằng chứng: [`../image/QLHSPLDN_07-D5-luot3b-sau-tai-lai-trang-8-o-doi-3-tep.png`](../image/QLHSPLDN_07-D5-luot3b-sau-tai-lai-trang-8-o-doi-3-tep.png) · [`../image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png`](../image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png)

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- Đặc tả **không có dòng nào** định nghĩa thay đổi tệp đính kèm có tính là *"cập nhật bản ghi"* hay không — tức không nói `ngayCapNhat` / `version` có phải nhảy trong trường hợp này.

**Câu hỏi cần BA xác nhận**

Định nghĩa *"cập nhật bản ghi"* (mốc đẩy `ngayCapNhat` và tăng `version`) có bao gồm **thay đổi tệp đính kèm** không?

1. Nếu **có** → phần mềm đang bỏ sót, owner **Dev BE**. Cần chốt luôn cho **mọi** thực thể có tệp đính kèm, không riêng hồ sơ DN.
2. Nếu **không** → hiện trạng đạt; đề nghị BA ghi một dòng định nghĩa vào đặc tả để lượt kiểm thử sau không chấm sai.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi — vế quan trọng nhất (lưu vết thao tác) đã đảm bảo bằng Nhật ký hệ thống.
- Chi tiết phép đo ở [`../tieuchi/QLHSPLDN_07.md`](../tieuchi/QLHSPLDN_07.md).

---

<!-- ========================= MỤC 21 — DẠNG B′ (đặc tả im lặng) ========================= -->

## `QLBMHD_02` (ghi nhận) — Biểu tượng cột `Loại TL` không có nhãn trợ năng tiếng Việt

**Bối cảnh testcase**

- Dòng Excel: **138**, tab `bug`, mã TC `QLBMHD_02`. Màn *Biểu mẫu hợp đồng* `SCR-VII-02`, **cột `Loại TL`** — cột dữ liệu, **không phải** cột Hành động.
- **Đối tác KHÔNG nêu điểm này**, **không** kéo verdict (đã **Pass**).

**Kết quả verify UI hiện tại**

- Cột `Loại TL` phân biệt định dạng **chỉ bằng biểu tượng**: `file-excel` (xanh lá) cho XLSX ↔ `file-word` (xanh dương) cho DOCX.
- Ô của cột **rỗng chữ** (`innerText = ""`), **không** `title`, **không** tooltip. Tên đọc được duy nhất là chuỗi kỹ thuật tiếng Anh `file-excel` / `file-word`.
- Chi tiết phép đo ở [`../bug-report.md`](../bug-report.md) mục **(b1)** và **(b2)** · [`../tieuchi/QLBMHD_02.md`](../tieuchi/QLBMHD_02.md)

**Điểm đặc tả im lặng / chưa rõ trong SRS v3.5**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6714` — Phụ lục E **§H6**: *"**Cột Hành động** trong mọi bảng dùng icon (Mắt = Xem, Bút = Sửa, Thùng rác = Xóa, …) thay cho nhãn text. **Mỗi icon BẮT BUỘC có `aria-label` và tooltip hover** mô tả hành động… Đáp ứng WCAG 4.1.2 — không icon-only."*
- Phạm vi của §H6 **chỉ là cột Hành động**. Grep toàn bộ SRS v3.5: `aria-label` chỉ xuất hiện đúng **1 lần** — tại chính `:6714` này. **Không có dòng nào** quy định biểu tượng ở các cột **dữ liệu** như `Loại TL`.

> **Đính chính so với bản ghi gốc:** mục `1.8` của [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) viết *"Phụ lục E §H6 tự mâu thuẫn"*. Đã mở `srs-v3.5.md:6714` đọc lại: §H6 **không** tự mâu thuẫn — nó chỉ **không phủ** trường hợp đang xét. Đây là **đặc tả im lặng** (Dạng B′), không phải mâu thuẫn (Dạng B).

**Câu hỏi cần BA xác nhận**

Yêu cầu *"biểu tượng phải có `aria-label` + tooltip, không icon-only"* của §H6 có mở rộng cho **biểu tượng ở các cột dữ liệu** (như `Loại TL`) không, hay chỉ giới hạn ở **cột Hành động** đúng như câu chữ hiện tại?

1. Nếu **mở rộng** → cần sửa câu §H6 cho rõ phạm vi, rồi Dev FE bổ sung nhãn tiếng Việt (*"Tệp Excel"* / *"Tệp Word"*) cho biểu tượng.
2. Nếu **giữ nguyên phạm vi cột Hành động** → hiện trạng đạt về mặt đặc tả; QA ghi nhận và không chấm điểm này ở các lượt sau.

**Đề xuất QA tạm thời**

- **Chưa** mở phiếu lỗi — đặc tả không phủ trường hợp này nên chưa có quy định để chấm vi phạm.
- Nếu BA chọn (1) thì đây là quy ước dùng chung, cần rà **mọi** bảng có biểu tượng ở cột dữ liệu, không riêng màn Biểu mẫu.

---

## Phụ lục A — Điểm chỉ GHI NHẬN, không cần BA trả lời

| Điểm | Nguồn | Vì sao không hỏi |
|---|---|---|
| Vài dòng Nhật ký hệ thống hiện `Dữ liệu cũ: —` | [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) mục `1.7` | Đặc tả không bắt buộc chụp trạng thái trước với **mọi** loại thao tác ⇒ không có quy định để chấm vi phạm, cũng không có gì để BA chốt. Ghi lại để lượt sau không log nhầm thành lỗi |
| `QLBMHD_02` — đối tác đòi cột *"Định dạng"* | [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) §0 | **BA đã sửa đặc tả cho đúng phiếu này**, đánh dấu `[STT12]` ở 5 chỗ (`srs-fr-09-bieu-mau.md:315` · `:482` · `:671` · `:672` · `:796`) và cả 5 đều là *Cơ quan ban hành*; phần định dạng BA đã phân xử ở mục `TKBMHD_03`. Bản sửa đặc tả là **ý chí sau cùng** ⇒ đã có câu trả lời, không hỏi lại |
| `QLBMHD_02` — điểm phụ **ô tích chọn** | [`cau-hoi-ba-tuan-5.md`](cau-hoi-ba-tuan-5.md) §0 | BA đã chốt **2026-07-24: Loại 3 — không sửa**. Câu trả lời cho đối tác đã nằm sẵn trong ô *DEV phản hồi lần 1* của dòng 138 |

## Phụ lục B — Điểm đã đủ căn cứ đặc tả nên KHÔNG hỏi BA mà mở phiếu lỗi

| Điểm | Xử lý |
|---|---|
| Câu từ chối khi QTHT bấm xuất tệp trả `Forbidden` / `ERR-PERM-SYS-00-01` (tiếng Anh, mã ngoài bộ mã báo cáo) | Trái `srs-fr-11-bao-cao.md:117` — đã tách phiếu riêng `BUG-BCTK-QA01` / `VVDTN_QA01` tại [`../../reverify-bug-devfix-2026-08-06/bug-reports/bug-report-BCTK.md`](../../reverify-bug-devfix-2026-08-06/bug-reports/bug-report-BCTK.md). **Độc lập** với việc BA chốt QTHT có được xuất hay không |
| *BC Chương trình theo thời gian* vẫn thống kê *Số DN* dù `srs-fr-11-bao-cao.md:1018` đã chốt bỏ `so_dn` | Đủ căn cứ ⇒ mở phiếu lỗi, không hỏi BA |
| AC `srs-fr-11-bao-cao.md:1023` (*"chọn 12 tháng → hiển thị biểu đồ trend"*) không với tới được bằng giao diện | Đủ căn cứ ⇒ ghi ở [`../../thu-QLTLPLCVV_15-2026-08-06/tieuchi/CTTTG_04.md`](../../thu-QLTLPLCVV_15-2026-08-06/tieuchi/CTTTG_04.md) mục 7 |
