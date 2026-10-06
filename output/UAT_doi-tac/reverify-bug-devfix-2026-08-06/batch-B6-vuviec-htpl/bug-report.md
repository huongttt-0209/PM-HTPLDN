# Bug Report — Vụ việc HTPL (lô B6 · verify bug dev đã fix)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Môi trường** | https://18.143.165.120.nip.io — **env nội bộ**, KHÔNG phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`) |
| **Bản dựng** | Đo lại đầu **mỗi** case. **Đã đổi giữa lô** — có triển khai mới xen giữa: <br>• Case KTHSYCHTPL_11 + TKHSYCHTPL_03: `HTPLDN · V1.0.8` · bó mã FE `assets/index-CNwX9JjX.js` · `GET /` `last-modified: 06/08/2026 02:51:16 GMT` (09:51:16 giờ VN) · `etag "6a73f6a4-428"`. <br>• Case XNTGHTVV_03 + CNKQHT_07: `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified: 06/08/2026 07:13:15 GMT` (14:13:15 giờ VN) · `etag "6a74340b-428"`. <br>• Case DGKQHTVV_01: `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified: 06/08/2026 07:13:15 GMT` (14:13:15 giờ VN) · `etag "6a74340b-428"` — **trùng bó mã với XNTGHTVV_03 + CNKQHT_07**, tự đo lại lúc 16:20. <br>• **Vòng re-verify R3 2026-08-07 (XNTGHTVV_03 + DGKQHTVV_01):** `HTPLDN · V1.0.10` · bó mã FE `assets/index-B2W2Krcs.js` · `GET /` `last-modified: Thu, 06 Aug 2026 17:39:54 GMT` · `etag W/"6a74c6ea-428"` — **trùng cả 4 dấu ở cả hai case**, không có triển khai mới xen giữa. <br>API `info.version 1.0.0` ở cả ba lần đo. |
| **Người test** | QA (Chrome DevTools MCP) |
| **Ngày** | 2026-08-07 02:15:00 |
| **Loại test** | Verify bug dev đã fix (flow `flows/04-verify-bug-dev-fix-khong-ho-so.md`) |
| **Round** | Lô B6 — vòng verify 2026-08-06 |
| **Tài liệu tham chiếu** | [BATCH-PLAN.md](BATCH-PLAN.md) · [tieuchi/KTHSYCHTPL_11.md](tieuchi/KTHSYCHTPL_11.md) · [tieuchi/TKHSYCHTPL_03.md](tieuchi/TKHSYCHTPL_03.md) · [tieuchi/XNTGHTVV_03.md](tieuchi/XNTGHTVV_03.md) · [tieuchi/CNKQHT_07.md](tieuchi/CNKQHT_07.md) · [tieuchi/DGKQHTVV_01.md](tieuchi/DGKQHTVV_01.md) · [cau-hoi-BA.md](cau-hoi-BA.md) · SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` |

---

## Tổng hợp

Lô B6 đã chạy **5/5 case**. **KTHSYCHTPL_11** (dòng 45): `N = 3` × `M = 3/3`, 0/5 GAP ⇒ **Pass**.
**TKHSYCHTPL_03** (dòng 50): `N = 52` × `M = 4/4`, 0/5 GAP, không seed ⇒ **Pass**.
**XNTGHTVV_03** (dòng 51): **re-verify R3 2026-08-07 trên bản dựng `V1.0.10`** — `N = 3` × `M = 3/3`, 0/5 GAP; vế lưu vết **đã hết lỗi** (nhật ký có lý do khớp từng chữ + cán bộ đọc được trên Dòng thời gian, hai đường đo trùng khít) ⇒ **Pass**.
**CNKQHT_07** (dòng 62): `N = 3` bản ghi × 4 lần bấm × `M = 3/3` dạng, 0/5 GAP — thông báo tới đúng cán bộ
nghiệp vụ liên quan trên **cả 2 kênh**, kể cả lần bấm không đính tệp; chứng dương và chứng âm đều đạt ⇒ **Pass**.
**DGKQHTVV_01** (dòng 64): **re-verify R3 2026-08-07 trên bản dựng `V1.0.10`, ra verdict bằng tài khoản doanh nghiệp** — `N = 10`
bản ghi × `M = 2/4` dạng (2/5 GAP: D1 hồi quy chưa chạy lại, D3 vẫn không dựng được). Máy chủ **đã mở quyền** đánh giá cho doanh
nghiệp và phần kết quả xử lý đã đọc được, nhưng **màn chi tiết vẫn đẩy doanh nghiệp sang trang không có quyền** khi mở vụ việc của
chính mình (2 doanh nghiệp × 2 đường vào) ⇒ **0 phần tử** dẫn tới việc đánh giá ⇒ **Reopen**. Chứng âm phạm vi + kiểm trùng đạt.
Ngoài phạm vi các case: **1 lỗi** đang mở ở Dòng thời gian vụ việc.
**Lỗi ngoài phạm vi KHÔNG kéo verdict của case đang verify.** Mọi Pass/Reopen chỉ có hiệu lực cho env nội bộ
+ bản dựng đã ghi ở đầu file.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 6    | 0        | 4     | 0      | 2     | 0       | 4      | 2    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-VV-KTHSYCHTPL-11~~ | Minor | P3 | Workflow | KTHSYCHTPL_11 (dòng 45) | `FR-V.I-06 §Processing bước 5` (`srs-fr-05-vu-viec.md:541`) · `§AC` (:564) · `SCR-V.I-03 Accordion 4` (:1730) · bảng nút (:1744) · bảng chuyển trạng thái (:2288) | Kết luận kiểm tra "Đạt" — lối vào phiếu kiểm tra, ghi nhận người kiểm tra + thời điểm kiểm tra, và mốc chuyển trạng thái | **Closed** |
| ~~BUG-VV-TKHSYCHTPL-03~~ | Major | P1 | Happy | TKHSYCHTPL_03 (dòng 50) | `SCR-V.I-01 Thành phần màn hình hàng 9` (`srs-fr-05-vu-viec.md:1644`) · `bảng mức cảnh báo` (:1513-1518) · `FR-V.I-01 §Error Handling` (:149) · `FR-V.I-08 §Error Handling` (:692-693) · `§AC` (:154, :697-698) · `BR-DATA-07` (:2394) · `SCR-V.I-01 hàng 24` (:1659) | Bộ lọc "Mức SLA" = "Sắp hết hạn" bị hệ thống từ chối, không trả danh sách | **Closed** |
| ~~BUG-VV-CNKQHT-07~~ | Major | P2 | Workflow | CNKQHT_07 (dòng 62) | `FR-V.I-15 §Processing bước 5` (`srs-fr-05-vu-viec.md:1106`) · `§Postconditions` (:1114) · `§AC` (:1125) · `BR-NOTIF-01` (:2480) · `Applied in` (:2482) · `INT-06 SLA email ≤ 5 phút` (`srs-v3.5.md:739`) · `/thong-baos` xếp mới nhất trước (`srs-v3.5.md:721`) | Cập nhật kết quả hỗ trợ: cán bộ nghiệp vụ không nhận được thông báo | **Closed** |
| ~~BUG-VV-XNTGHTVV-03~~ | Minor | P3 | Data | XNTGHTVV_03 (dòng 51) | `FR-V.I-10 §Processing bước 6-7` (`srs-fr-05-vu-viec.md:826-827`) · `LICH_SU_VU_VIEC` (:2129) · trường `ly_do` (:2142) · `SCR-V.I-03 thành phần #12` (:1735) | Từ chối tham gia hỗ trợ: nhật ký vụ việc không lưu lý do từ chối | **Closed** |
| BUG-VV-LICHSU-THEO-NGUOI | Major | P2 | Data | — (QA phát hiện ngoài phạm vi, phát sinh khi verify KTHSYCHTPL_11) | `SCR-V.I-03 thành phần #12` (`srs-fr-05-vu-viec.md:1735`) · `FR-V.I-05 §AC` (:629) | Dòng thời gian vụ việc chỉ hiện sự kiện do chính người đang đăng nhập thực hiện; cán bộ khác mở cùng vụ việc thấy "Chưa có lịch sử hoạt động" | **Open** |
| BUG-VV-DGKQHTVV-01 | Major | P1 | Permission | DGKQHTVV_01 (dòng 64) | `FR-V.I-17 / UC67 §Mô tả` (`srs-fr-05-vu-viec.md:1190`) · `PRE-03` (:1198) · `§Processing bước 1-2` (:1215-1216) · `DANH_GIA_VU_VIEC.loai_nguoi_danh_gia` (:2116) · `SCR-V.I-03 chế độ DN — Nhóm 8` (:1809) · `Thanh thao tác chế độ DN` (:1811) · `địa chỉ chế độ DN` (:1792) | Đánh giá kết quả hỗ trợ vụ việc: doanh nghiệp chủ vụ việc vẫn không mở được chi tiết vụ việc của chính mình nên không có đường vào đánh giá (máy chủ đã mở quyền đánh giá; màn chi tiết vẫn chặn cả trang vì 2 nguồn dữ liệu nội bộ) | **Open** |

---

## ~~BUG-VV-KTHSYCHTPL-11~~ [CLOSED] — Kết luận kiểm tra "Đạt": lối vào phiếu kiểm tra, ghi người kiểm tra + thời điểm, và mốc chuyển trạng thái

> **Re-test:** 2026-08-06 13:36:00 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-CNwX9JjX.js` / `last-modified 06/08/2026 09:51:16` giờ VN · **N = 3 bản ghi** (`VV-STP-AG-20260806-001` · `-002` · `-003`) · **M = 3/3 dạng** (D1 kiểm tra lần đầu kết luận Đạt · D2 kiểm tra lại ghi đè bằng tài khoản khác · D3 kết luận Yêu cầu bổ sung) · **dữ liệu seed:** 3 vụ việc QA do QA tự tạo mới bằng luồng "Nhập thủ công" trên doanh nghiệp `DN-AGG-0001 — Cong ty QA UAT An Giang`, không đụng dữ liệu sẵn có. Đo bằng `cbnv_dp_01` (ra verdict) + `cbnv_dp_02` (dựng dạng D2). **Pass chỉ có hiệu lực cho env + bản dựng nêu trên; phải re-verify khi bản dựng này lên env nghiệm thu `htpldn-uat.ospgroup.vn`.**

### Mô tả

Đối tác phản ánh 3 vế trên màn chi tiết vụ việc ở trạng thái "Đang kiểm tra": (a) kết luận Đạt phải chuyển
hồ sơ sang "Đã phân công"; (b) hệ thống phải ghi người kiểm tra và thời điểm kiểm tra; (c) màn không hiển
thị nút "Hoàn tất kiểm tra" mà chỉ có "Kiểm tra lại".

Đo lại bằng thao tác thật trên bản dựng V1.0.8: vế (b) và (c) **không còn lỗi**. Vế (a) không phải lỗi —
BA đã chốt ngày 2026-07-16 rằng kết luận Đạt **giữ nguyên** "Đang kiểm tra", chỉ chuyển "Đã phân công" khi
cán bộ phân công người xử lý.

### Các bước tái hiện

1. Đăng nhập `cbnv_dp_01` — vai trò **CB_NV_DP**, cấp Địa phương, đơn vị `00000000-0000-4000-8002-000000000006`
   (quyền `kiem-tra_vu_viec` theo `GET /api/v1/auth/me`). Tải lại trang để chắc chắn chạy bản dựng mới.
2. Vụ việc HTPL → **Nhập thủ công** → chọn doanh nghiệp `DN-AGG-0001` → **Lưu & Tiếp nhận**
   → sinh `VV-STP-AG-20260806-001`, trạng thái "Đã tiếp nhận".
3. Mở chi tiết vụ việc → bấm nút mở phiếu kiểm tra ở thanh hành động.
4. Đánh dấu **6/6 hạng mục Đạt** → chọn kết luận **Đạt** → **Xác nhận**. Ghi đồng hồ máy trước khi bấm: **13:23:05**.
5. **Tải lại trang**, mở vùng "Kết quả kiểm tra" đọc kết luận / người kiểm tra / ngày kiểm tra.
6. Bấm **[Phân công]** → chọn người xử lý → **Xác nhận** → tải lại trang, đọc badge trạng thái.
7. Lặp cho 2 dạng còn lại: `VV-STP-AG-20260806-002` kết luận **Yêu cầu bổ sung**;
   `VV-STP-AG-20260806-003` lưu kết luận Đạt bằng `cbnv_dp_01` rồi đăng nhập `cbnv_dp_02`
   (cùng vai trò, **cùng đơn vị**) bấm **[Kiểm tra lại]** lưu lại kết luận Đạt.

### Kết quả mong đợi

- Theo `srs-fr-05-vu-viec.md:1730` (SCR-V.I-03 Accordion 4), sau khi vụ việc đã qua "Đang kiểm tra", màn
  chi tiết phải đọc được checklist 6 hạng mục + kết luận + lý do + **người kiểm tra** + **ngày**.
- Theo `srs-fr-05-vu-viec.md:541` và `:564`, khi kết luận **Đạt** thì vụ việc **sẵn sàng phân công nhưng
  vẫn giữ trạng thái "Đang kiểm tra"**; theo `:2288` chỉ chuyển "Đã phân công" khi đã chọn được người/tổ
  chức xử lý hợp lệ.
- Theo `srs-fr-05-vu-viec.md:1744`, ở trạng thái "Đang kiểm tra" cán bộ nghiệp vụ phải có đường vào để ghi
  hoặc sửa lại kết quả kiểm tra đã lưu.
- Theo `srs-fr-05-vu-viec.md:523`, lý do chỉ bắt buộc khi kết luận Không đạt hoặc Yêu cầu bổ sung.

### Kết quả thực tế

Khớp đầy đủ các yêu cầu trên:

- **Lối vào (vế c):** ở "Đã tiếp nhận" thanh hành động có nút **[Kiểm tra hồ sơ]**; sau khi đã lưu kết quả,
  ở "Đang kiểm tra" nút đổi thành **[Kiểm tra lại]**. Cả hai mở **cùng một phiếu** "Kiểm tra hồ sơ" gồm
  **6 hạng mục C01→C06** và ô kết luận có **đúng 3 lựa chọn** (`Đạt — chuyển sang phân công`,
  `Không đạt — từ chối hồ sơ`, `Yêu cầu bổ sung`), lưu được bình thường. Trạng thái đối tác chụp trong ảnh
  (chỉ còn [Phân công] + [Kiểm tra lại]) chính là **trạng thái sau khi kiểm tra đã lưu thành công**.
- **Ghi người + thời điểm (vế b):** sau khi tải lại trang, vùng "Kết quả kiểm tra" hiện
  **Kết luận: Đạt** · **Người kiểm tra: CB Nghiệp vụ - Địa phương #01** · **Ngày kiểm tra: 06/08/2026 13:23**
  — đúng tài khoản vừa lưu, lệch **4 giây** so với đồng hồ ghi trước khi bấm (13:23:05), không rỗng,
  không `null`, không chuỗi giữ chỗ, còn nguyên sau khi tải lại.
- **Cập nhật theo lần lưu mới nhất:** trên `-003`, sau khi `cbnv_dp_02` bấm [Kiểm tra lại] và lưu lại,
  vùng này đổi sang **"CB Nghiệp vụ - Địa phương #02" / 06/08/2026 13:32** (trước đó là #01 / 13:31) —
  không đóng băng ở lần lưu đầu.
- **Nhánh khác Đạt:** trên `-002` kết luận **Yêu cầu bổ sung** + lý do, vùng "Kết quả kiểm tra" vẫn ghi đủ
  **Người kiểm tra** + **Ngày kiểm tra** (06/08/2026 13:28) → 2 trường này không chỉ tồn tại ở nhánh Đạt.
- **Mốc chuyển trạng thái (vế a):** ngay sau khi lưu kết luận Đạt, badge vẫn là **"Đang kiểm tra"**, thanh
  tiến trình dừng ở bước 4. Chỉ sau khi bấm [Phân công] → chọn người xử lý → Xác nhận thì badge mới đổi
  **"Đã phân công"** (bước 5). Đây đúng bằng quyết định BA ngày **2026-07-16**.
- **Thông báo:** mỗi lần lưu đo được đúng **1 request + 1 khung thông báo + 1 mốc giờ** (không lặp):
  Đạt → *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*; Yêu cầu bổ sung → *"Đã yêu cầu bổ sung"*;
  Phân công → *"Đã phân công vụ việc cho QA NHT An Giang UAT2. Hệ thống đã gửi thông báo."*

**Ghi chú (không phải lỗi):** nút mở phiếu không mang đúng chữ "Hoàn tất kiểm tra" như `:1744` liệt kê, mà
là [Kiểm tra hồ sơ] / [Kiểm tra lại]. Nhãn là cách hiện thực; yêu cầu nghiệp vụ "có đường vào để cán bộ
nghiệp vụ ghi và sửa kết luận kiểm tra" đã được đáp ứng.

### Bằng chứng

**1. Ảnh chụp**

![BUG-VV-KTHSYCHTPL-11 — VV-STP-AG-20260806-001 vừa tạo: badge "Đã tiếp nhận", thanh tiến trình dừng bước 3, thanh hành động chỉ có nút [Kiểm tra hồ sơ]; chân sidebar ghi "HTPLDN · V1.0.8"](image/KTHSYCHTPL_11-01-VV1-da-tiep-nhan-truoc-kiem-tra.png)

![BUG-VV-KTHSYCHTPL-11 — Phiếu "Kiểm tra hồ sơ" mở ra: các hạng mục C01→C06 mỗi mục có cặp radio Đạt/Không đạt (đang chọn Đạt), ô Kết luận bung ra đúng 3 lựa chọn "Đạt — chuyển sang phân công" / "Không đạt — từ chối hồ sơ" / "Yêu cầu bổ sung", cuối phiếu có nút Hủy và Xác nhận](image/KTHSYCHTPL_11-02-phieu-kiem-tra-6-hang-muc-3-lua-chon-ket-luan.png)

![BUG-VV-KTHSYCHTPL-11 — Ngay sau khi lưu kết luận Đạt: badge vẫn "Đang kiểm tra", tiến trình dừng bước 4, thanh hành động đổi thành [Phân công] + [Kiểm tra lại], xuất hiện thêm nhóm "Kết quả kiểm tra"; Dòng thời gian ghi "Kiểm tra 06/08/2026 13:23 CB Nghiệp vụ - Địa phương #01"](image/KTHSYCHTPL_11-03-ngay-sau-luu-Dat-badge-van-Dang-kiem-tra.png)

![BUG-VV-KTHSYCHTPL-11 — Sau khi tải lại trang, nhóm "Kết quả kiểm tra" bung ra: bảng Mã / Hạng mục / Đạt / Không đạt / Ghi chú, các dòng C01→C04 đều có dấu ✓ ở cột "Đạt" và dấu "—" ở cột "Ghi chú"](image/KTHSYCHTPL_11-04-sau-tai-lai-ket-qua-kiem-tra-Dat-nguoi-kiem-tra-ngay-kiem-tra.png)

![BUG-VV-KTHSYCHTPL-11 — Cuộn xuống hết nhóm "Kết quả kiểm tra" sau khi tải lại trang: đủ 6 dòng C01→C06 đều ✓ cột Đạt, bên dưới là Kết luận "Đạt" (thẻ xanh), Người kiểm tra "CB Nghiệp vụ - Địa phương #01", Ngày kiểm tra "06/08/2026 13:23", nhãn "Lần BS 0/3"](image/KTHSYCHTPL_11-05-vung-ket-luan-Dat-nguoi-kiem-tra-ngay-kiem-tra-13h23.png)

![BUG-VV-KTHSYCHTPL-11 — Sau khi bấm [Phân công] chọn NHT và Xác nhận rồi tải lại trang: badge đổi thành "Đã phân công", tiến trình sang bước 5, xuất hiện nhóm "Phân công Người hỗ trợ / Tư vấn viên" ghi NHT/TVV phụ trách "QA NHT An Giang UAT2" và Ngày phân công 06/08/2026 13:25](image/KTHSYCHTPL_11-06-sau-phan-cong-badge-doi-thanh-Da-phan-cong.png)

![BUG-VV-KTHSYCHTPL-11 — Dạng D3 trên VV-STP-AG-20260806-002: C03 mang dấu ✗ ở cột "Không đạt", Kết luận "Yêu cầu bổ sung", có Lý do, và vẫn ghi đủ Người kiểm tra "CB Nghiệp vụ - Địa phương #01" + Ngày kiểm tra "06/08/2026 13:28", nhãn "Lần BS 1/3"](image/KTHSYCHTPL_11-07-D3-yeu-cau-bo-sung-van-ghi-nguoi-va-ngay-kiem-tra.png)

![BUG-VV-KTHSYCHTPL-11 — Dạng D2 trên VV-STP-AG-20260806-003 sau khi cbnv_dp_02 bấm [Kiểm tra lại] và lưu lại kết luận Đạt: góc phải header là "CB Nghiệp vụ - Địa phương #02", vùng Kết quả kiểm tra đổi sang Người kiểm tra "CB Nghiệp vụ - Địa phương #02" và Ngày kiểm tra "06/08/2026 13:32" (lần lưu đầu là #01 / 13:31)](image/KTHSYCHTPL_11-08-D2-kiem-tra-lai-nguoi-va-ngay-cap-nhat-sang-CB02-13h32.png)

**2. Đối chứng bằng đường thứ hai — đọc lại bản ghi từ máy chủ**

`GET /api/v1/vu-viecs/{id}/ket-qua-kiem-tra` (dạng D1, `VV-STP-AG-20260806-001`):

```json
{
  "items": [
    {"ma": "C01", "ket_qua": "DAT"}, {"ma": "C02", "ket_qua": "DAT"},
    {"ma": "C03", "ket_qua": "DAT"}, {"ma": "C04", "ket_qua": "DAT"},
    {"ma": "C05", "ket_qua": "DAT"}, {"ma": "C06", "ket_qua": "DAT"}
  ],
  "boSungCount": 0,
  "ketLuan": "DAT",
  "lyDo": null,
  "nguoiKiemTraId": "e81aa51b-e132-49a4-8831-fd404512af40",
  "nguoiKiemTraTen": "CB Nghiệp vụ - Địa phương #01",
  "ngayKiemTra": "2026-08-06T06:23:09.360Z"
}
```

Trạng thái vụ việc đọc lại ở cùng thời điểm: `"trangThai": "DANG_KIEM_TRA"` — sau khi phân công mới thành
`"trangThai": "DA_PHAN_CONG"`. Dạng D2 (`-003`) sau lần lưu thứ hai: `nguoiKiemTraId` đổi thành
`7a4e1b00-4232-41e5-b320-4ae4a91568d1` (`cbnv_dp_02`), `ngayKiemTra` `2026-08-06T06:32:53.887Z`.
Giao diện và máy chủ **khớp nhau ở cả 3 dạng**, không có mâu thuẫn.

---

## ~~BUG-VV-TKHSYCHTPL-03~~ [CLOSED] — Bộ lọc "Mức SLA" = "Sắp hết hạn" bị hệ thống từ chối, không trả danh sách

> **Re-test:** 2026-08-06 14:05:47 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-CNwX9JjX.js` / `last-modified 06/08/2026 09:51:16` giờ VN / `etag W/"6a73f6a4-428"` · **N = 52 bản ghi** trong phạm vi tài khoản (72 dòng đã đọc qua các phép đo) · **M = 4/4 dạng** (4 mức của ô lọc: Bình thường 38 · Sắp hết hạn 2 · Quá hạn 6 · Quá hạn nghiêm trọng 6) + 1 phép baseline không chọn mức + 1 phép ép 0 kết quả · **dữ liệu seed: KHÔNG có** — cả 4 mức đều đã sẵn bản ghi thật nên không tạo, sửa, xóa bản ghi nào; toàn bộ phép đo chỉ dùng lệnh đọc. Đo bằng `cbnv_tw_01` (vai trò `CB_NV_TW`, cấp TW). **Pass chỉ có hiệu lực cho env + bản dựng nêu trên; phải re-verify khi bản dựng này lên env nghiệm thu `htpldn-uat.ospgroup.vn`.**

### Mô tả

Đối tác phản ánh 3 vế trên màn danh sách vụ việc: (a) chọn ô lọc "Mức SLA" = "Sắp hết hạn" rồi bấm
[Tìm kiếm] thì hệ thống hiện thông báo lỗi thay vì lọc; (b) bảng không ra kết quả; (c) danh sách phải
phân trang 20 bản ghi mỗi trang.

Đo lại bằng thao tác thật trên bản dựng V1.0.8: **cả 3 vế đều không còn lỗi**. Bộ lọc chạy đủ 4/4 mức,
không mức nào sinh thông báo lỗi, và phân trang cắt đúng 20 dòng mỗi trang.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_01` — vai trò **CB_NV_TW**, cấp Trung ương, đơn vị
   `00000000-0000-4000-8000-000000000001` (đọc từ `GET /api/v1/auth/me`; cấp TW xem phạm vi toàn quốc
   theo `srs-fr-05-vu-viec.md:1663`). Vào màn bằng **bấm menu** "Vụ việc HTPL", rồi **tải lại trang bỏ
   nhớ đệm** để chắc chắn đang chạy bản dựng mới.
2. Trên màn `/vu-viec/danh-sach`, giữ nguyên tab **"Tất cả"**, khối "Bộ lọc nâng cao (3)" **thu gọn**,
   mọi ô lọc khác (từ khóa · Lĩnh vực PL · Đơn vị · Kênh tiếp nhận) **để trống**.
3. Ghi số baseline khi chưa chọn mức nào: đếm số dòng trên bảng và đọc chân bảng.
4. Mở ô **"Mức SLA"**, đếm số lựa chọn trong danh sách bung ra.
5. Chọn **"Sắp hết hạn"** → bấm **[Tìm kiếm]**. Bộ bắt thông báo dùng chung
   (`output/UAT_doi-tac/tools/toast-capture.js`) được cài **trước** khi bấm, tự kiểm
   `soObserverDangSong = 1`, không lọc trùng, đọc chữ bằng `innerText`.
6. Đọc: địa chỉ trên thanh URL · số khung thông báo bắt được trong 3 giây · số dòng thô trên bảng ·
   cột "Cảnh báo thời hạn" của từng dòng · nhãn chân bảng.
7. Lặp bước 5-6 cho **3 mức còn lại**: "Bình thường", "Quá hạn", "Quá hạn nghiêm trọng".
8. Lặp riêng mức **"Sắp hết hạn"** thêm **1 lần nữa sau khi tải lại trang bỏ nhớ đệm**, lần này chọn mức
   bằng **bàn phím** (mũi tên xuống + Enter) thay vì chuột.
9. Phân trang: với tập đã lọc "Bình thường" (tổng 38), đếm tay số dòng trang 1, bấm sang **trang 2**,
   đếm lại và đối chiếu mã vụ việc hai trang xem có trùng nhau không.
10. Ép tập kết quả về 0: đặt "Mức SLA" = "Sắp hết hạn" **kèm** từ khóa `ZZZKHONGTONTAI` → [Tìm kiếm].
11. Đối chứng bằng đường thứ hai: gọi thẳng `GET /api/v1/vu-viecs?mucSla=<mã>&page=1&pageSize=100`
    (chống nhớ đệm) cho từng mức, so tổng của máy chủ với số đo trên màn.

### Kết quả mong đợi

- Theo `srs-fr-05-vu-viec.md:1644` (SCR-V.I-01, hàng 9), ô lọc "Mức SLA" là thành phần **luôn hiển thị**
  với **đúng 4** mức, và chọn một mức phải dẫn tới **lọc danh sách**, không phải từ chối yêu cầu.
- Theo `srs-fr-05-vu-viec.md:1515-1518`, nhãn "Sắp hết hạn" là **một trong 4 mức hợp lệ** của cột cảnh báo
  thời hạn ⇒ cán bộ chọn mức này là thao tác đúng.
- Theo `srs-fr-05-vu-viec.md:149` (FR-V.I-01 §Error Handling — **toàn bảng chỉ 1 hàng**) và `:692-693`
  (FR-V.I-08 §Error Handling — **toàn bảng chỉ 2 hàng**), tình huống duy nhất ở mức ERROR trên màn này là
  ngày bắt đầu sau ngày kết thúc; **không có** mục xử lý lỗi nào cho giá trị mức SLA. Vì vậy khi cán bộ
  chọn một mức trên chính ô lọc đó, hệ thống phải trả **danh sách**, hoặc **màn rỗng mức INFO**
  "Không tìm thấy hồ sơ phù hợp" nếu không có bản ghi nào — chứ không được hiện thông báo lỗi kỹ thuật.
- Theo `srs-fr-05-vu-viec.md:154` và `:697-698` (§AC), áp bộ lọc phải cho ra kết quả lọc tương ứng.
- Theo `srs-fr-05-vu-viec.md:125`, `:668`, `:1659` và `:2394` (BR-DATA-07), danh sách phân trang
  **mặc định 20 dòng/trang**, chân bảng cho biết đang xem khoảng nào trên tổng bao nhiêu kết quả.

### Kết quả thực tế

Khớp đầy đủ các yêu cầu trên. Đo đủ **4/4 mức**, mỗi mức một phép riêng — **không suy từ mức này sang mức khác**:

| Phép đo | Giá trị giao diện gửi lên | Khung thông báo lỗi | Số dòng thô trên bảng | Chân bảng | Cột "Cảnh báo thời hạn" |
|---|---|:-:|:-:|---|---|
| Baseline — không chọn mức | *(không có tham số mức)* | **0** | 20 | "Hiển thị 1-20 / 52 kết quả" | đủ 4 mức lẫn lộn |
| **Sắp hết hạn** — lần 1 (vào bằng bấm menu) | `mucSla=SAP_HET` | **0** | 2 | "Hiển thị 1-2 / 2 kết quả" | 2/2 dòng = "Sắp hết hạn" |
| **Sắp hết hạn** — lần 2 (sau khi tải lại trang bỏ nhớ đệm, chọn bằng bàn phím) | `mucSla=SAP_HET` | **0** | 2 | "Hiển thị 1-2 / 2 kết quả" | 2/2 dòng = "Sắp hết hạn" |
| Bình thường | `mucSla=BINH_THUONG` | **0** | 20 (trang 1) | "Hiển thị 1-20 / 38 kết quả" | 19 dòng "Bình thường" + 1 dòng "—" |
| Quá hạn | `mucSla=QUA_HAN` | **0** | 6 | "Hiển thị 1-6 / 6 kết quả" | 6/6 dòng = "Quá hạn · 4 ngày LV" |
| Quá hạn nghiêm trọng | `mucSla=QUA_HAN_NGHIEM_TRONG` | **0** | 6 | "Hiển thị 1-6 / 6 kết quả" | 6/6 dòng = "Quá hạn nghiêm trọng" |
| "Sắp hết hạn" + từ khóa `ZZZKHONGTONTAI` (ép 0 kết quả) | `mucSla=SAP_HET&keyword=…` | **0** | 0 | *(không có chân bảng)* | màn rỗng "Không tìm thấy hồ sơ phù hợp" |

- **Vế (a) — bộ lọc không còn bị từ chối.** Ô "Mức SLA" bung ra **đúng 4 lựa chọn** — "Bình thường",
  "Sắp hết hạn", "Quá hạn", "Quá hạn nghiêm trọng" — khớp `:1644` và bảng nhãn `:1515-1518`. Với **cả 4
  mức**, bộ bắt thông báo đếm được **0 khung thông báo** trong 3 giây kể từ lúc bấm (`soObserverDangSong = 1`
  trước mỗi loạt đo, đếm theo **mốc giờ khác nhau**, không lọc trùng, đọc bằng `innerText`), và trên màn
  không có phần tử nào thuộc nhóm khung lỗi. Mỗi lần bấm [Tìm kiếm] sinh **đúng 1** yêu cầu danh sách.
- **Giá trị giao diện gửi lên đã nằm trong tập của đặc tả.** Thanh địa chỉ sau khi bấm là
  `…/vu-viec/danh-sach?mucSla=SAP_HET&page=1`, và yêu cầu gửi đi là
  `GET /api/v1/vu-viecs?mucSla=SAP_HET&page=1&pageSize=20` → `SAP_HET` thuộc đúng tập 4 mã ở `:1644`
  và `:2031`, **không** còn là biến thể `SAP_HET_HAN` như bản đối tác quay.
- **Vế (b) — danh sách ra kết quả đúng.** Mức "Sắp hết hạn" trả **2 dòng**
  (`VV-BTP-TW-20260712-006` trạng thái Từ chối, `VV-BTP-TW-20260712-005` trạng thái Hoàn thành), cả hai
  mang đúng nhãn **"Sắp hết hạn"** ở cột "Cảnh báo thời hạn"; số dòng đếm tay **bằng đúng** con số hệ
  thống tự báo ở chân bảng ("Hiển thị 1-2 / **2** kết quả") và lặp lại y hệt sau khi tải lại trang.
  Ba mức còn lại cũng chỉ trả về dòng đúng mức đã lọc: **0 dòng lệch mức**.
- **Nhánh 0 kết quả không sinh khung lỗi.** Ép tập về rỗng bằng từ khóa không tồn tại: màn hiện đúng
  **"Không tìm thấy hồ sơ phù hợp"** (`:149`, `:692`), **0** khung thông báo lỗi. Đây chính là hình dạng
  màn rỗng hợp lệ, khác hẳn tình huống yêu cầu bị từ chối.
- **Vế (c) — phân trang 20 dòng/trang.** Khi chưa đụng vào bộ chọn kích thước trang (đang là "20 / trang"):
  tập baseline (T = 52) trang 1 đếm tay **đúng 20** dòng, chân bảng "Hiển thị 1-20 / 52 kết quả";
  tập đã lọc "Bình thường" (T = 38) trang 1 **đúng 20** dòng, sang **trang 2** còn **18** dòng
  = `min(20, 38−20)`, chân bảng đổi thành "Hiển thị 21-38 / 38 kết quả", và **0/18 mã vụ việc trùng**
  với trang 1. Ba tập có T ≤ 20 (2 / 6 / 6) hiện đúng T dòng trên 1 trang, không cắt trang.
- **Ghi nhận thêm (không dùng để chấm).** Trong tập lọc "Bình thường" có **2 bản ghi** hiện dấu **"—"** ở
  cột "Cảnh báo thời hạn": `VV-BTP-TW-20260731-002` và `VV-BTP-TW-20260712-002`, đều ở trạng thái
  **Mới tạo**, chưa có ngày tiếp nhận nên chưa tính được thời hạn; giá trị lưu của chúng là giá trị mặc
  định `BINH_THUONG` theo `:2031`, nên lọt bộ lọc "Bình thường" là **nhất quán với dữ liệu đã lưu**.
  Đặc tả không nói bản ghi chưa có mức cảnh báo thì rơi vào nhóm lọc nào ⇒ ghi nhận và đưa BA
  (xem [cau-hoi-BA.md](cau-hoi-BA.md)), **không** chấm Fail.
- **Số liệu cộng khớp tổng.** 38 + 2 + 6 + 6 = **52** = đúng tổng baseline ⇒ không có bản ghi nào rơi ra
  ngoài 4 mức, phép đo không thiếu hụt.

### Bằng chứng

**1. Ảnh chụp**

![BUG-VV-TKHSYCHTPL-03 — Baseline chưa chọn mức nào: chân thanh điều hướng ghi "HTPLDN · V1.0.8", góc phải header là "CB Nghiệp vụ - Trung ương #01" + "BTP · TW", tab "Tất cả 52" đang chọn, ô "Mức SLA" còn trống, khối "Bộ lọc nâng cao (3)" thu gọn](image/TKHSYCHTPL_03-00-baseline-khong-loc-52-ket-qua.png)

![BUG-VV-TKHSYCHTPL-03 — Ô "Mức SLA" bung ra đúng 4 lựa chọn "Bình thường" / "Sắp hết hạn" / "Quá hạn" / "Quá hạn nghiêm trọng", bảng bên dưới vẫn là danh sách chưa lọc](image/TKHSYCHTPL_03-01-dropdown-Muc-SLA-4-lua-chon.png)

![BUG-VV-TKHSYCHTPL-03 — Đã chọn xong "Sắp hết hạn" trong ô "Mức SLA" nhưng CHƯA bấm [Tìm kiếm]: bảng vẫn còn 52 bản ghi cũ, chưa có khung thông báo nào trên màn](image/TKHSYCHTPL_03-02-da-chon-Sap-het-han-truoc-khi-bam-Tim-kiem.png)

![BUG-VV-TKHSYCHTPL-03 — Lần 1 sau khi bấm [Tìm kiếm] với mức "Sắp hết hạn": bảng trả 2 dòng VV-BTP-TW-20260712-006 (Từ chối) và VV-BTP-TW-20260712-005 (Hoàn thành), chân bảng "Hiển thị 1-2 / 2 kết quả", tab đổi thành "Tất cả 2 · Hoàn thành 1 · Từ chối 1", KHÔNG có khung thông báo lỗi nào](image/TKHSYCHTPL_03-03-Sap-het-han-lan1-ra-2-ket-qua-khong-loi.png)

![BUG-VV-TKHSYCHTPL-03 — Cùng kết quả trên, cuộn bảng sang phải để đọc cột "Cảnh báo thời hạn": cả 2 dòng đều mang thẻ vàng "Sắp hết hạn", đúng bằng mức đã lọc](image/TKHSYCHTPL_03-04-Sap-het-han-cot-Canh-bao-thoi-han-dung-muc.png)

![BUG-VV-TKHSYCHTPL-03 — Mức "Bình thường", trang 1: chân bảng "Hiển thị 1-20 / 38 kết quả", các thẻ xanh "Bình thường · còn N ngày LV"; riêng dòng VV-BTP-TW-20260731-002 trạng thái "Mới tạo" hiện dấu "—" vì chưa có thời hạn xử lý](image/TKHSYCHTPL_03-05-Binh-thuong-trang1-20-dong-tren-38.png)

![BUG-VV-TKHSYCHTPL-03 — Vẫn mức "Bình thường", đã bấm sang trang 2: chân bảng đổi thành "Hiển thị 21-38 / 38 kết quả", ô số 2 được tô đậm, bảng là tập mã vụ việc hoàn toàn khác trang 1](image/TKHSYCHTPL_03-06-Binh-thuong-trang2-18-dong-21-38.png)

![BUG-VV-TKHSYCHTPL-03 — Mức "Quá hạn": ô lọc hiện "Quá hạn", bảng trả 6 dòng, tất cả mang thẻ đỏ "Quá hạn · 4 ngày LV", chân bảng "Hiển thị 1-6 / 6 kết quả", không có khung thông báo lỗi](image/TKHSYCHTPL_03-07-Qua-han-6-ket-qua-khong-loi.png)

![BUG-VV-TKHSYCHTPL-03 — Mức "Quá hạn nghiêm trọng": ô lọc hiện "Quá hạn nghiêm trọng", bảng trả 6 dòng với thẻ đen "Quá hạn nghiêm trọng · N ngày LV", chân bảng "Hiển thị 1-6 / 6 kết quả", không có khung thông báo lỗi](image/TKHSYCHTPL_03-08-Qua-han-nghiem-trong-6-ket-qua-khong-loi.png)

![BUG-VV-TKHSYCHTPL-03 — Lần 2 sau khi tải lại trang bỏ nhớ đệm: đã chọn "Sắp hết hạn" bằng bàn phím, bảng vẫn đang là 52 bản ghi chưa lọc (chọn mức không tự lọc, phải bấm [Tìm kiếm])](image/TKHSYCHTPL_03-09-lan2-sau-tai-lai-da-chon-Sap-het-han-bang-ban-phim.png)

![BUG-VV-TKHSYCHTPL-03 — Lần 2 sau khi bấm [Tìm kiếm]: kết quả lặp lại y hệt lần 1 — 2 dòng, cả 2 mang thẻ vàng "Sắp hết hạn", chân bảng "Hiển thị 1-2 / 2 kết quả", không có khung thông báo lỗi](image/TKHSYCHTPL_03-10-Sap-het-han-lan2-sau-tai-lai-van-2-ket-qua-khong-loi.png)

![BUG-VV-TKHSYCHTPL-03 — Ép tập kết quả về 0 bằng "Sắp hết hạn" + từ khóa ZZZKHONGTONTAI: màn hiện ảnh hộp trống và chữ "Không tìm thấy hồ sơ phù hợp", nút [Xuất Excel] chuyển mờ, số đếm trên 6 tab biến mất — và KHÔNG có khung thông báo lỗi nào](image/TKHSYCHTPL_03-11-Sap-het-han-0-ket-qua-man-rong-INFO-khong-loi.png)

**2. Đối chứng bằng đường thứ hai — gọi thẳng máy chủ, giao diện và máy chủ khớp nhau**

`GET /api/v1/vu-viecs?mucSla=<mã>&page=1&pageSize=100` (chống nhớ đệm), cùng phiên đăng nhập `cbnv_tw_01`:

```
(không lọc)            HTTP 200  meta.total = 52  · phân bố mức: BINH_THUONG 38 · SAP_HET 2 · QUA_HAN 6 · QUA_HAN_NGHIEM_TRONG 6
mucSla=BINH_THUONG     HTTP 200  meta.total = 38  · 38/38 bản ghi mang mucDoCanhBao = BINH_THUONG
mucSla=SAP_HET         HTTP 200  meta.total =  2  ·  2/2  bản ghi mang mucDoCanhBao = SAP_HET
mucSla=QUA_HAN         HTTP 200  meta.total =  6  ·  6/6  bản ghi mang mucDoCanhBao = QUA_HAN
mucSla=QUA_HAN_NGHIEM_TRONG  HTTP 200  meta.total = 6 · 6/6 bản ghi mang mucDoCanhBao = QUA_HAN_NGHIEM_TRONG
```

Tổng 4 mức = 38 + 2 + 6 + 6 = **52** = đúng `meta.total` của baseline. Con số máy chủ **trùng khít** số dòng
đếm tay trên bảng và nhãn chân bảng ở cả 5 phép đo ⇒ hai đường đo **không mâu thuẫn**.

Giá trị cũ mà bản dựng đối tác từng gửi lên vẫn bị máy chủ từ chối (đây là lý do bản cũ hiện thông báo lỗi,
và cũng là bằng chứng cho thấy giao diện lần này đã gửi giá trị khác):

```json
GET /api/v1/vu-viecs?mucSla=SAP_HET_HAN&page=1&pageSize=20   ->  HTTP 422
{
  "success": false,
  "error": {
    "code": "ERR-VAL-SYS-00-01",
    "field": "mucSla",
    "message": "mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG",
    "timestamp": "2026-08-06T07:01:11.932Z"
  }
}
```

**Lưu ý về mã của mức "Sắp hết hạn":** hai nơi trong bộ đặc tả đang ghi mã khác nhau cho cùng một mức
(`srs-fr-05-vu-viec.md:1644` và `:2031` ghi `SAP_HET`; `srs-fr-11-bao-cao.md:245`, `srs-fr-02-hoi-dap.md:979`
và `CHANGELOG-v3-to-v3.5.md:1317` — BR-SLA-02, cite BA 2026-05-04 — ghi `SAP_HET_HAN`). Việc chọn mã chuẩn
thuộc thẩm quyền BA, đã tách thành một mục riêng trong [cau-hoi-BA.md](cau-hoi-BA.md); mục đó **không** kéo
verdict của phiếu này, vì dù chọn mã nào thì cả hai bản đặc tả đều đòi bộ lọc phải trả danh sách chứ không
được từ chối yêu cầu, và cả hai bảng Error Handling (`:149`, `:692-693`) đều không có mục lỗi nào cho
giá trị mức SLA.

**Hoàn nguyên dữ liệu:** phép đo của phiếu này **chỉ dùng lệnh đọc** (`GET`) và thao tác lọc trên giao diện —
không tạo, không sửa, không xóa bản ghi nào, nên không có gì phải hoàn nguyên.

---

## ~~BUG-VV-CNKQHT-07~~ [CLOSED] — Cập nhật kết quả hỗ trợ: cán bộ nghiệp vụ không nhận được thông báo

> **Re-test:** 2026-08-06 16:08:00 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.8` / bó mã `assets/index-DIABnbIr.js` / `last-modified 06/08/2026 14:13:15` giờ VN / `etag "6a74340b-428"` · **N = 3 bản ghi, 4 lần bấm** (`VV-BTP-TW-20260806-003` bấm 2 lần · `VV-BTP-TW-20260806-004` · `VV-STP-AG-20260806-005`) · **M = 3/3 dạng** (D1 người kỳ vọng nhận tự tạo trọn vụ việc · D2 người khác tạo, người kỳ vọng nhận chỉ phân công · D3 doanh nghiệp tự gửi, không cán bộ nào là người tạo) **+ 1 lần đo bổ sung D1B không đính tệp, không ghi chú** · **dữ liệu seed:** 3 vụ việc QA tự dựng mới bằng luồng chuẩn trên doanh nghiệp `Cong ty TNHH QA UAT Kiem Thu` (TW) và DN `0209888006` (An Giang), thêm 1 tệp `qa-cnkqht07-ket-qua.pdf` 641 byte tự tạo; không đụng dữ liệu sẵn có. Đo bằng `qa_tvvseed28` + `nht_ag_uat2` (người bấm) và `cbnv_tw_01`, `cbnv_tw_02`, `cbnv_dp_01` (người nhận). **Pass chỉ có hiệu lực cho env + bản dựng nêu trên; phải re-verify khi bản dựng này lên env nghiệm thu `htpldn-uat.ospgroup.vn`.**

### Mô tả

Đối tác phản ánh: người được phân công bấm **[Cập nhật kết quả]** trên vụ việc đang ở trạng thái "Đang xử lý"
thì **cán bộ nghiệp vụ không nhận được thông báo**.

Đo lại trên bản dựng V1.0.8 bằng ba bộ dữ liệu tự dựng: thông báo **có** được gửi, tới đúng cán bộ nghiệp vụ
gắn với vụ việc, trên **cả hai kênh** (trong ứng dụng và hộp thư), cách lúc bấm **4-6 giây** ở ba dạng đầu và
**dưới 1 giây** ở lần bấm không đính tệp.

Bằng chứng của đối tác không cho biết tài khoản mở chuông có phải cán bộ phụ trách của chính vụ việc đó không:
hộp thư dùng để đăng nhập trong video thuộc miền `@htpldn.gov.vn`, trong khi thư hệ thống trước đó **của cùng
vụ việc ấy** lại gửi tới một địa chỉ miền `@htpldn.test`. Vì vậy lần đo này **tự dựng tiền đề** để biết chắc ai
là người tạo · người tiếp nhận · người phân công, thay vì suy đoán.

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_01` (CB_NV_TW, `Test@1234`). Tải lại trang để chắc chắn đang chạy bản dựng mới.
   Đọc địa chỉ hộp thư **thật** của tài khoản từ hồ sơ tài khoản trong phần mềm: `cbnv_tw_01@htpldn.test`.
2. Vẫn bằng `cbnv_tw_01`: nhập thủ công vụ việc `VV-BTP-TW-20260806-003` → kiểm tra hồ sơ kết luận **Đạt**
   → **Phân công** cho `qa_tvvseed28`.
3. Đăng nhập `qa_tvvseed28` → **Chấp nhận** phân công; vụ việc chuyển **"Đang xử lý"**.
   (Bước này đồng thời là **nhóm chứng dương**: FR-V.I-10 cũng đòi gửi thông báo cho cán bộ nghiệp vụ.)
4. Trước khi bấm: đăng nhập `cbnv_tw_01`, mở **`/thong-baos`**, đếm **thô** tổng số mục (**76**) và xác nhận
   chưa có mục nào nhắc mã vụ việc sắp thao tác. Ghi mốc giờ. Ghi tổng số thư trên máy chủ hộp thư (**1651**).
5. Đăng nhập `qa_tvvseed28` → mở vụ việc → **Nhóm 6 — Kết quả hỗ trợ** → **[Cập nhật kết quả]** → nhập nội dung
   mang chuỗi nhận dạng riêng + đính **1 tệp .pdf** + ghi chú → **Xác nhận** (15:45:43).
   Bộ bắt thông báo được cài **trước** khi bấm, tự kiểm cho đúng **1** bộ đang sống.
6. Lặp cho **dạng 2** — `VV-BTP-TW-20260806-004`: `cbnv_tw_02` tạo + tiếp nhận + kiểm tra, **`cbnv_tw_01` phân công**,
   `qa_tvvseed28` chấp nhận rồi cập nhật kết quả (15:46:55).
7. Lặp cho **dạng 3** — `VV-STP-AG-20260806-005`: doanh nghiệp `0209888006` tự gửi yêu cầu, `cbnv_dp_01` tiếp nhận
   + kiểm tra + phân công, `nht_ag_uat2` chấp nhận rồi cập nhật kết quả (15:49:28).
8. **Lần bấm thứ tư (D1B)** trên chính `VV-BTP-TW-20260806-003`: chỉ nhập nội dung, **không đính tệp, không ghi chú**
   — đúng bộ nhập trong bằng chứng đối tác (16:06:33).
9. Sau mỗi lần bấm: đăng nhập **chính tài khoản cán bộ nghiệp vụ kỳ vọng nhận**, mở `/thong-baos` đếm lại;
   mở hộp thư của **đúng địa chỉ** đó; đọc lại danh sách thông báo qua đường máy chủ **trong phiên của chính
   tài khoản đó** để đối chứng.

### Kết quả mong đợi

Theo `srs-fr-05-vu-viec.md:1106` — Processing bước 5 `| 5 | Gửi thông báo CB NV | — |`, `:1114` Postconditions
`- CB NV nhận thông báo để review`, và `:1125` — *"**Given** người được phân công nhập nội dung + upload tài liệu
**When** lưu **Then** cập nhật, thông báo CB NV"*: sau khi người được phân công lưu kết quả hỗ trợ, hệ thống phải
gửi thông báo cho cán bộ nghiệp vụ để người này xem xét và chuẩn bị trình phê duyệt.

Theo `srs-fr-05-vu-viec.md:2480` (BR-NOTIF-01) và dòng **Applied in** `:2482` có FR-V.I-15: thông báo phải đi
**đủ 2 kênh** — trong ứng dụng (`THONG_BAO`) và email. Email có mốc **≤ 5 phút** (`srs-v3.5.md:739`, INT-06).
Danh sách `/thong-baos` xếp **mới nhất trước** (`srs-v3.5.md:721`).

Đặc tả **không** nói cụ thể "CB NV" là ai (người tạo / người tiếp nhận / người phân công / mọi cán bộ cùng đơn vị),
cũng **không** quy định câu chữ của thông báo — nên hai điểm này không được dùng để chấm trượt.

### Kết quả thực tế

**Thông báo được gửi đủ ở cả 4 lần bấm, trên cả 2 kênh, tới đúng cán bộ nghiệp vụ gắn với vụ việc:**

| Lần bấm | Vụ việc | Người bấm | Người nhận đo được | Trong ứng dụng (đếm thô trước → sau) | Mốc mục mới | Thư gửi tới | Độ trễ |
|---|---|---|---|---|---|---|---|
| D1 15:45:43 | `-003` | `qa_tvvseed28` | `cbnv_tw_01` (tạo = tiếp nhận = phân công) | 76 → 78 | 15:45:49 | `cbnv_tw_01@htpldn.test` | ~6 giây |
| D2 15:46:55 | `-004` | `qa_tvvseed28` | `cbnv_tw_02` (tạo + tiếp nhận) | 41 → 43 | 15:46:59 | `cbnv_tw_02@htpldn.test` | ~4 giây |
| D3 15:49:28 | `-005` | `nht_ag_uat2` | `cbnv_dp_01` (tiếp nhận + phân công) | 7 → 9 | 15:49:32 | `cbnv_dp_01@htpldn.test` | ~4 giây |
| D1B 16:06:33 | `-003` | `qa_tvvseed28` | `cbnv_tw_01` | 79 → 80 | 16:06:33 | `cbnv_tw_01@htpldn.test` | 0,2 giây |

*(Mức tăng 2 mục ở D1/D2/D3 gồm 1 mục của bước Chấp nhận phân công — nhóm chứng dương — và 1 mục của lần cập nhật
kết quả. Số đếm là **thô**, không lọc trùng, không gộp.)*

**Nội dung thông báo — nguyên văn:** tiêu đề `Kết quả hỗ trợ đã được cập nhật - {mã vụ việc}`, loại `PHAN_CONG`;
nội dung *"Người được phân công đã cập nhật kết quả hỗ trợ vụ việc: - Mã vụ việc: {mã} - Doanh nghiệp: {tên DN}
Vui lòng đăng nhập hệ thống để xem xét và chuẩn bị trình phê duyệt."* — mô tả **đúng** thao tác vừa làm, có
**đúng mã vụ việc**, và nói rõ việc cần làm tiếp là xem xét, chuẩn bị trình phê duyệt.

**Vị trí:** tại thời điểm đo, mục mới nằm **đầu** danh sách `/thong-baos`. Trong ảnh chụp sau đó nó tụt xuống thứ hai
vì lần đăng nhập lại của chính QA sinh ra một mục "Tài khoản vừa đăng nhập ở nơi khác" mới hơn — không phải sai thứ tự.

**Nhóm chứng dương (để phân biệt "FR-V.I-15 không gửi" với "thông báo hỏng cho tài khoản này"):** bước Chấp nhận
phân công (FR-V.I-10) sinh thông báo trên **cả ba** hộp — `cbnv_tw_01` 15:43:13, `cbnv_tw_02` 15:43:33,
`cbnv_dp_01` 15:48:49 — kèm thư tương ứng. Vậy hạ tầng thông báo của ba tài khoản này đều sống.

**Nhóm chứng âm — gửi có địa chỉ, không phát tán:**
- Người vừa bấm không nhận: `qa_tvvseed28` giữ nguyên 44 mục qua D1 và D2; `nht_ag_uat2` giữ nguyên 5 mục qua D3.
- Cán bộ chỉ **phân công** mà không tạo/tiếp nhận thì **không** nhận: `cbnv_tw_01` không có mục nào cho `-004`
  — vụ việc mà chính tài khoản này đã phân công.
- Ở lần D1B, toàn máy chủ hộp thư chỉ phát sinh **đúng 1 thư** sau mốc bấm, gửi tới đúng `cbnv_tw_01@htpldn.test`.

**Trục người nhận đo được:** thông báo đi tới cán bộ **tiếp nhận/tạo** vụ việc, **không** đi theo trục người phân công.
Đặc tả không định nghĩa "CB NV" là vai nào (mục 2 §IM LẶNG #1 của tiêu chí), người nhận đo được **là cán bộ có liên
quan thật sự tới vụ việc**, nên đây là ghi nhận, không phải lỗi.

**Vế (a) — ngoài phạm vi phản ánh, ghi nhận không chấm:** mỗi lần bấm đo được đúng **1 khung thông báo trên màn ·
1 mốc giờ · 2 request ghi** (`POST …/upload` rồi `POST …/cap-nhat-ket-qua`) ở ba lần có tệp, và **1 khung · 1 mốc ·
1 request** ở lần không tệp — không lặp. Chữ trên khung là **"Đã cập nhật kết quả"**, thiếu chữ "hỗ trợ" so với ô
Kết quả mong đợi của đối tác; đặc tả im lặng về câu chữ này nên không log thành lỗi.

### Bằng chứng

**1. Ảnh chụp**

![BUG-VV-CNKQHT-07 — Trang Thông báo của cbnv_tw_01 chụp TRƯỚC toàn bộ thao tác lúc 15:26: mục đầu danh sách là "Tài khoản vừa đăng nhập ở nơi khác", không có mục nào nhắc VV-BTP-TW-20260806-003](image/cnkqht07-00-thongbao-cbnv_tw_01-truoc-toan-bo-15h26.png)

![BUG-VV-CNKQHT-07 — Vụ việc VV-BTP-TW-20260806-003 vừa được cbnv_tw_01 nhập thủ công, badge "Đã tiếp nhận"](image/cnkqht07-01-d1-tao-vv-BTP-TW-20260806-003-boi-cbnv_tw_01.png)

![BUG-VV-CNKQHT-07 — Cùng vụ việc sau khi kiểm tra Đạt và phân công cho qa_tvvseed28: badge "Đã phân công", nhóm Phân công ghi người hỗ trợ](image/cnkqht07-02-d1-da-phan-cong-qa_tvvseed28.png)

![BUG-VV-CNKQHT-07 — Hộp thoại "Cập nhật kết quả hỗ trợ" của dạng 1 đã điền đủ: nội dung mang chuỗi nhận dạng, 1 tệp .pdf đính kèm, ô Ghi chú có chữ — chụp ngay TRƯỚC khi bấm Xác nhận](image/cnkqht07-03-d1-form-cap-nhat-ket-qua-truoc-khi-bam.png)

![BUG-VV-CNKQHT-07 — Nhóm 6 "Kết quả hỗ trợ" của VV-BTP-TW-20260806-003 sau khi cập nhật lúc 15:45: hiện đúng chuỗi nhận dạng và tệp vừa đính](image/cnkqht07-04-d1-nhom6-sau-cap-nhat-15h45.png)

![BUG-VV-CNKQHT-07 — Nhóm 6 của VV-BTP-TW-20260806-004 (dạng 2) sau khi cập nhật lúc 15:46](image/cnkqht07-05-d2-nhom6-sau-cap-nhat-15h46.png)

![BUG-VV-CNKQHT-07 — Nhóm 6 của VV-STP-AG-20260806-005 (dạng 3, vụ việc do doanh nghiệp tự gửi) sau khi cập nhật lúc 15:49](image/cnkqht07-06-d3-nhom6-sau-cap-nhat-15h49.png)

![BUG-VV-CNKQHT-07 — Chuông thông báo của cbnv_tw_01 sau thao tác: có mục "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003"](image/cnkqht07-07-d1-chuong-cbnv_tw_01-co-thong-bao-VV003.png)

![BUG-VV-CNKQHT-07 — Trang Thông báo của cbnv_tw_01 SAU thao tác: mục "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003" ghi 06/08/2026 15:45, nhãn Phân công, nội dung mời đăng nhập để xem xét và chuẩn bị trình phê duyệt](image/cnkqht07-08-d1-thongbaos-cbnv_tw_01-sau-cap-nhat.png)

![BUG-VV-CNKQHT-07 — Trang Thông báo của cbnv_tw_02 (dạng 2) có mục cho VV-BTP-TW-20260806-004 lúc 15:46](image/cnkqht07-09-d2-thongbaos-cbnv_tw_02-sau-cap-nhat.png)

![BUG-VV-CNKQHT-07 — Trang Thông báo của cbnv_dp_01 (dạng 3) có mục cho VV-STP-AG-20260806-005 lúc 15:49](image/cnkqht07-10-d3-thongbaos-cbnv_dp_01-sau-cap-nhat.png)

![BUG-VV-CNKQHT-07 — Hộp thư lọc theo đúng địa chỉ cbnv_tw_01@htpldn.test: có thư "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003" và thư chứng dương "Người hỗ trợ đã xác nhận tham gia vụ việc" của cùng vụ việc](image/cnkqht07-11-mailhog-hopthu-cbnv_tw_01-co-mail-VV003.png)

![BUG-VV-CNKQHT-07 — Chi tiết thư của vụ việc -003: dòng To ghi đúng cbnv_tw_01@htpldn.test, tiêu đề "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003"](image/cnkqht07-12-mailhog-chitiet-mail-VV003-To-cbnv_tw_01.png)

![BUG-VV-CNKQHT-07 — Hộp thư lọc theo cbnv_tw_02@htpldn.test: có thư cho VV-BTP-TW-20260806-004](image/cnkqht07-13-mailhog-hopthu-cbnv_tw_02-co-mail-VV004.png)

![BUG-VV-CNKQHT-07 — Hộp thư lọc theo cbnv_dp_01@htpldn.test: có thư cho VV-STP-AG-20260806-005](image/cnkqht07-14-mailhog-hopthu-cbnv_dp_01-co-mail-VV005.png)

![BUG-VV-CNKQHT-07 — Lần bấm D1B: hộp thoại chỉ có nội dung (107/10000), vùng tệp đính kèm TRỐNG, ô Ghi chú TRỐNG — chụp ngay trước khi bấm Xác nhận](image/cnkqht07-15-d1b-form-khong-tep-khong-ghichu-truoc-khi-bam.png)

![BUG-VV-CNKQHT-07 — Nhóm 6 sau lần bấm D1B lúc 16:06: nội dung đổi sang chuỗi nhận dạng QA-CNKQHT07-D1B-160609](image/cnkqht07-16-d1b-nhom6-sau-cap-nhat-khong-tep-16h06.png)

![BUG-VV-CNKQHT-07 — Chuông của cbnv_tw_01 ngay sau lần bấm không đính tệp: mục "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003" ghi 2 phút trước](image/cnkqht07-17-d1b-chuong-cbnv_tw_01-co-thongbao-lan-khong-tep.png)

![BUG-VV-CNKQHT-07 — Trang Thông báo của cbnv_tw_01 hiện đủ cả hai lần cập nhật (16:06 lần không tệp và 15:45 lần có tệp) cùng mục chứng dương "Người hỗ trợ đã xác nhận tham gia vụ việc" lúc 15:43; chân sidebar ghi HTPLDN · V1.0.8](image/cnkqht07-18-d1b-thongbaos-cbnv_tw_01-2-lan-cap-nhat-16h06-va-15h45.png)

**2. Đối chứng bằng đường thứ hai — đọc lại danh sách thông báo trong phiên của chính người nhận**

`GET /api/v1/thong-baos?page=1&limit=6` bằng phiên của `cbnv_tw_01` (không phải phiên quản trị), đọc sau lần bấm D1B:

```json
{
  "meta": {"page": 1, "pageSize": 20, "total": 80, "totalPages": 4},
  "data": [
    {"ngayTao": "2026-08-06T09:06:33.804Z", "loai": "PHAN_CONG",
     "tieuDe": "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003"},
    {"ngayTao": "2026-08-06T08:50:56.026Z", "loai": "HE_THONG",
     "tieuDe": "Tài khoản vừa đăng nhập ở nơi khác"},
    {"ngayTao": "2026-08-06T08:45:49.326Z", "loai": "PHAN_CONG",
     "tieuDe": "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260806-003"},
    {"ngayTao": "2026-08-06T08:43:13.386Z", "loai": "PHAN_CONG",
     "tieuDe": "Người hỗ trợ đã xác nhận tham gia vụ việc - VV-BTP-TW-20260806-003"}
  ]
}
```

Lần bấm D1B ghi nhận lúc `09:06:33.621Z`; mục thông báo mang mốc `09:06:33.804Z` và thư mang mốc `09:06:33.857Z`
— tức **0,2-0,24 giây**. Số đếm hai đường **khớp nhau** (giao diện 80 mục ↔ máy chủ `total: 80`), không mâu thuẫn.

**3. Ghi nhận thêm khi đo, không phải lỗi của case này**

- Vụ việc do doanh nghiệp gửi (`VV-STP-AG-20260806-005`) sinh thông báo "Vụ việc mới từ doanh nghiệp" cho **toàn bộ**
  cán bộ nghiệp vụ của đơn vị (`cbnv_dp` và `cbnv_dp_01`…`_05`). Đó là hành vi của bước tiếp nhận, không thuộc FR-V.I-15.
- Bấm cập nhật lần thứ hai mà không đính tệp thì tệp của lần trước **vẫn còn** trong Nhóm 6. Đặc tả để ngỏ chuyện
  thay/giữ tệp cũ nên không log; ghi lại để lần sau khỏi hiểu nhầm.
- Dòng thời gian vụ việc lại chỉ hiện sự kiện của chính người đang đăng nhập — trùng lỗi đã mở
  **BUG-VV-LICHSU-THEO-NGUOI** ở dưới, không mở thêm mục mới.

---

## BUG-VV-LICHSU-THEO-NGUOI — Dòng thời gian vụ việc chỉ hiện sự kiện do chính người đang đăng nhập thực hiện

> **Vụ việc HTPL — QA phát hiện ngoài phạm vi (không thuộc case nào của bảng), phát sinh khi verify
> KTHSYCHTPL_11.** Lỗi này **không kéo verdict** của case KTHSYCHTPL_11.

### Mô tả

Khối "Dòng thời gian" trên màn chi tiết vụ việc chỉ liệt kê những sự kiện do **chính tài khoản đang đăng
nhập** thực hiện. Một cán bộ nghiệp vụ khác — kể cả cùng vai trò và **cùng đơn vị** — mở đúng vụ việc đó
sẽ thấy "Chưa có lịch sử hoạt động", dù vụ việc đã có nhiều sự kiện thật. Hệ quả: hồ sơ xử lý của vụ việc
không truy được khi bàn giao giữa hai cán bộ.

### Các bước tái hiện

1. Đăng nhập `cbnv_dp_01` — vai trò **CB_NV_DP**, cấp Địa phương, đơn vị `...8002-000000000006`
   (quyền `read_vu_viec` theo `GET /api/v1/auth/me`).
2. Tạo vụ việc `VV-STP-AG-20260806-001`, kiểm tra hồ sơ kết luận Đạt, rồi phân công người xử lý
   → vụ việc có **3 sự kiện thật**: Tạo vụ việc 13:20 · Kiểm tra 13:23 · Phân công 13:25.
3. Mở chi tiết vụ việc bằng chính `cbnv_dp_01` → Dòng thời gian hiện **đủ 3 mục**.
4. Đăng xuất, đăng nhập `cbnv_dp_02` — **cùng vai trò CB_NV_DP, cùng đơn vị** `...8002-000000000006`.
5. Mở đúng vụ việc đó → cuộn tới khối "Dòng thời gian".
6. Quan sát: hiện ảnh "Trống" + chữ **"Chưa có lịch sử hoạt động"**, trong khi nhóm "Phân công Người hỗ trợ
   / Tư vấn viên" ngay phía trên **vẫn hiện đủ dữ liệu** (Ngày phân công 06/08/2026 13:25).

### Kết quả mong đợi

- Theo `srs-fr-05-vu-viec.md:1735` (SCR-V.I-03, thành phần #12 "Dòng thời gian"), khối này lấy
  **lịch sử xử lý từ LICH_SU_VU_VIEC** của vụ việc và có điều kiện hiển thị là **"Luôn"** — tức nội dung
  phụ thuộc vụ việc đang xem, không phụ thuộc ai đang xem.
- Theo `srs-fr-05-vu-viec.md:629` (AC FR-V.I-05): *"Given CB NV xem chi tiết When chọn VV Then hiển thị
  thông tin + trạng thái + lịch sử xử lý"* — mọi cán bộ nghiệp vụ xem chi tiết đều phải đọc được lịch sử
  xử lý của vụ việc.
- SRS chỉ mô tả **một** trường hợp lọc bớt dòng thời gian, ở `:1810`, và đó là bản dành cho **doanh nghiệp**
  (lọc theo *loại sự kiện*, ẩn sự kiện nội bộ) — không phải lọc theo người thực hiện, và không áp cho
  cán bộ nghiệp vụ.

### Kết quả thực tế

Dòng thời gian được lọc theo **người thực hiện**, không phải theo vụ việc. Đo chéo hai chiều trên cùng
3 vụ việc:

| Vụ việc | Sự kiện thật | `cbnv_dp_01` đọc được | `cbnv_dp_02` đọc được |
|---|---|:-:|:-:|
| `VV-STP-AG-20260806-001` | 3 (Tạo · Kiểm tra · Phân công — đều do #01) | **3** (`PHAN_CONG`, `KIEM_TRA`, `TAO_VV`) | **0** → "Chưa có lịch sử hoạt động" |
| `VV-STP-AG-20260806-002` | 2 (Tạo · Yêu cầu bổ sung — đều do #01) | 2 | **0** |
| `VV-STP-AG-20260806-003` | 3 (Tạo 13:27 + Kiểm tra 13:31 do **#01**; Kiểm tra lại 13:32 do **#02**) | **2** — thiếu sự kiện 13:32 của #02 | **1** — chỉ sự kiện 13:32 của chính #02 |

Dòng `-003` là bằng chứng quyết định: **mỗi tài khoản chỉ thấy phần lịch sử của riêng mình**, không ai đọc
được toàn bộ lịch sử của vụ việc.

### Bằng chứng

**1. Ảnh chụp**

![BUG-VV-LICHSU-THEO-NGUOI — cbnv_dp_02 mở VV-STP-AG-20260806-001 (vụ việc do cbnv_dp_01 tạo, kiểm tra và phân công): nhóm "Phân công Người hỗ trợ / Tư vấn viên" vẫn hiện đủ dữ liệu với Ngày phân công 06/08/2026 13:25, nhưng khối "Dòng thời gian" phía dưới chỉ có ảnh "Trống" và chữ "Chưa có lịch sử hoạt động"](image/QA-ngoai-pham-vi-dong-thoi-gian-trong-khi-CB02-xem-vu-viec-CB01-thao-tac.png)

**2. Đo lại bằng đường thứ hai — gọi thẳng máy chủ, giao diện và máy chủ khớp nhau**

`GET /api/v1/vu-viecs/86495522-d5e9-4803-b0ea-f44fd9418309/lich-su` (vụ việc `VV-STP-AG-20260806-003`,
có 3 sự kiện thật) trả về **khác nhau theo phiên đăng nhập**:

```
# phiên cbnv_dp_02  -> 1 bản ghi
[{ "hanhDong": "KIEM_TRA", "nguoiThucHienId": "7a4e1b00-...", "thoiGian": "2026-08-06T06:32:53.903Z" }]

# phiên cbnv_dp_01  -> 2 bản ghi, KHÔNG có sự kiện 06:32:53 của cbnv_dp_02
[{ "hanhDong": "KIEM_TRA", "nguoiThucHien": "CB Nghiệp vụ - Địa phương #01",
   "nguoiThucHienId": "e81aa51b-...", "thoiGian": "2026-08-06T06:31:11.098Z" },
 { "hanhDong": "TAO_VV",   "nguoiThucHienId": "e81aa51b-..." }]
```

Cùng một `id` vụ việc, cùng endpoint, đổi phiên đăng nhập thì tập kết quả đổi theo → xác nhận bộ lọc nằm ở
phía máy chủ, không phải lỗi hiển thị của giao diện và không phải lỗi môi trường (cùng cơ chế đọc chi tiết
vụ việc / kết quả kiểm tra / phân công **vẫn trả đủ dữ liệu** cho cả hai tài khoản).

**Hoàn nguyên dữ liệu:** phép đo lỗi này chỉ dùng lệnh đọc (`GET`), không tạo/sửa/xóa bản ghi nào.

---

## ~~BUG-VV-XNTGHTVV-03~~ [CLOSED] — Từ chối tham gia hỗ trợ: nhật ký vụ việc không lưu lý do từ chối

> **Re-test:** 2026-08-07 01:30:00 R3 — ✅ PASS (Closed-verified). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.10` / bó mã `assets/index-B2W2Krcs.js` / `last-modified Thu, 06 Aug 2026 17:39:54 GMT` / `etag W/"6a74c6ea-428"` · **N = 3 bản ghi** (`VV-BTP-TW-20260806-001` · `VV-BTP-TW-20260806-002` · `VV-STP-AG-20260806-004`) · **M = 3/3 dạng** (① người tạo ≡ người phân công · ② người tạo ≠ người phân công · ③ người tạo là doanh nghiệp) · **dữ liệu seed:** phân công lại 3 hồ sơ tồn ở "Đã tiếp nhận" rồi thực hiện **3 thao tác từ chối MỚI** (07/08 01:22–01:24), không tạo/xóa bản ghi nào; cả 3 hồ sơ tự trở lại `DA_TIEP_NHAN` sau thao tác. Đo bằng `cbnv_tw_01` (ra verdict ①②, `userId` = `nguoiTiepNhanId`) + `cbnv_dp_01` (ra verdict ③); `cbnv_tw_02`/`cbnv_dp_02` chỉ phân công, `qa_tvvseed28`/`nht_ag_uat2` là người bấm Từ chối; **không dùng `admin`**. **Phép đo quyết định:** mục nhật ký `TU_CHOI_PHAN_CONG` mới nay mang trường `lyDo` khớp **từng chữ 52/52 ký tự** chuỗi đã nhập, **và** cán bộ phụ trách đọc được lý do ngay trên khối "Dòng thời gian" của màn chi tiết dù hồ sơ đã về "Đã tiếp nhận" và nhóm Phân công đã ẩn — hai đường đo trùng khít 3/3. Mục từ chối cũ (06/08) vẫn `lyDo=null` đúng bản chất dữ liệu đóng băng, đã loại khỏi phép đo. **Pass chỉ có hiệu lực cho env + bản dựng nêu trên; phải re-verify khi bản dựng này lên env nghiệm thu `htpldn-uat.ospgroup.vn`.**

### Mô tả

Trên màn chi tiết vụ việc ở trạng thái "Đã phân công", người được phân công bấm **[Từ chối]** → nhập lý do hợp lệ
→ **Xác nhận**. Thao tác được xử lý bình thường và lý do được lưu lại ở bản ghi phân công, nhưng **nhật ký xử lý
của vụ việc không lưu lý do từ chối** — mục nhật ký sinh ra cho thao tác này chỉ có tên hành động, người thực hiện
và thời điểm.

Năm vế còn lại mà đối tác nêu **đã hết lỗi** trên bản dựng này: thao tác không còn văng sang màn chặn quyền truy
cập; có thông báo thành công trên màn; hệ thống tự chuyển về màn danh sách; bản ghi phân công chuyển đúng sang
"Từ chối" kèm lý do; hồ sơ quay về đúng **"Đã tiếp nhận"** (không phải "Chờ phê duyệt"); và cán bộ nghiệp vụ đang
phụ trách hồ sơ **có** nhận thông báo **kèm nguyên văn lý do** trên **cả hai kênh** (chuông trong ứng dụng + thư).

### Các bước tái hiện

1. Đăng nhập `cbnv_tw_01` (Cán bộ Nghiệp vụ Trung ương, đơn vị `00000000-0000-4000-8000-000000000001`).
   Vụ việc HTPL → **Nhập thủ công** → doanh nghiệp `Cong ty TNHH QA UAT Kiem Thu` → **Lưu & Tiếp nhận**
   → sinh `VV-BTP-TW-20260806-002`.
2. Đăng nhập `cbnv_tw_02` (cùng đơn vị) → mở hồ sơ đó → **Kiểm tra hồ sơ**, 6/6 hạng mục Đạt, kết luận **Đạt**
   → **[Phân công]** → chọn `QA TVV Seed28 Active` → Xác nhận. Hồ sơ về **"Đã phân công"**, bản ghi phân công
   ở *Chờ xác nhận*.
3. Đăng nhập `qa_tvvseed28` — **chính là người được phân công** của hồ sơ này — mở chi tiết vụ việc.
4. Bấm **[Từ chối]** → nhập lý do
   `QA verify XNTGHTVV_03 batch B6 - tu choi tham gia ho tro - dang 2 nguoi phan cong khac nguoi tao`
   (96 ký tự, hợp lệ ≥ 10) → **Xác nhận**. Ghi lại thời điểm bấm: **2026-08-06T07:53:24.207Z**.
5. Đăng nhập lại bằng cán bộ nghiệp vụ đang phụ trách hồ sơ (`cbnv_tw_01`) → mở chi tiết vụ việc
   → cuộn tới khối **"Dòng thời gian"** → đọc mục ứng với thao tác từ chối.
6. Đối chứng bằng đường thứ hai: đọc lại nhật ký của chính vụ việc đó từ máy chủ
   (`GET /api/v1/vu-viecs/{id}/lich-su`) và so với bản ghi phân công (`.../phan-cong`).
7. Lặp cho 2 dạng còn lại: `VV-BTP-TW-20260806-001` (người tạo ≡ người phân công) và
   `VV-STP-AG-20260806-004` (hồ sơ do doanh nghiệp tự gửi, `nht_ag_uat2` là người được phân công).

### Kết quả mong đợi

- Theo `srs-fr-05-vu-viec.md:826-827` (FR-V.I-10 §Processing, bước 6 *"Ghi lịch sử"* và bước 7 *"Ghi nhật ký thao
  tác"*), thao tác từ chối tham gia hỗ trợ phải được lưu vết.
- Theo `srs-fr-05-vu-viec.md:2129`, `LICH_SU_VU_VIEC` là *"nhật ký toàn bộ thao tác trên VV — audit trail + nguồn
  hiển thị Timeline (SCR-V.I-03)"*, và `:2130` liệt kê **FR-V.I-10** trong các chức năng tham chiếu tới nó.
- Theo `srs-fr-05-vu-viec.md:2142`, trường `ly_do` của nhật ký là **bắt buộc khi hành động thuộc nhóm**
  *`('YEU_CAU_BO_SUNG','MO_LAI','TU_CHOI_PHAN_CONG','TU_CHOI_PD','HUY_CONG_KHAI')`* — tức **đúng nhóm chứa thao
  tác từ chối phân công của case này**.
- Theo `srs-fr-05-vu-viec.md:1735` (SCR-V.I-03, thành phần #12), khối "Dòng thời gian" có điều kiện hiển thị
  **"Luôn"** và lấy nội dung từ chính nhật ký này ⇒ cán bộ mở hồ sơ phải đọc được lý do vì sao người được phân
  công từ chối, ngay trên hồ sơ.

### Kết quả thực tế

Nhật ký **có** sinh mục cho thao tác từ chối, nhưng mục đó **không mang lý do**. Đo trên cả 3 hồ sơ, bằng cả
giao diện lẫn đường đọc thẳng máy chủ — hai đường **khớp nhau**, không mâu thuẫn:

| Hồ sơ | Mục nhật ký sinh ra | Tên hành động | Người thực hiện | Thời điểm | **Lý do trong nhật ký** |
|---|:-:|---|---|---|:-:|
| `VV-BTP-TW-20260806-001` | 1 | Từ chối phân công | QA TVV Seed28 Active | 2026-08-06T07:43:10.514Z | **không có** |
| `VV-BTP-TW-20260806-002` | 1 | Từ chối phân công | QA TVV Seed28 Active | 2026-08-06T07:53:24.373Z | **không có** |
| `VV-STP-AG-20260806-004` | 1 | Từ chối phân công | QA NHT An Giang UAT2 | 2026-08-06T08:02:58.196Z | **không có** |

- **Trên màn:** khối "Dòng thời gian" của `VV-BTP-TW-20260806-002` hiện đúng một dòng mới
  *"Từ chối phân công — 06/08/2026 14:53 — QA TVV Seed28 Active"*, khớp thời điểm bấm trong vòng vài giây,
  nhưng **không có chỗ nào trên màn chi tiết cho cán bộ đọc được lý do**: sau khi hồ sơ quay về "Đã tiếp nhận",
  nhóm "Phân công Người hỗ trợ / Tư vấn viên" (nơi có cột *Lý do từ chối*) **không còn hiển thị** trên màn.
- **Đọc thẳng máy chủ:** bản ghi nhật ký của thao tác này gồm các trường định danh, tên hành động, người thực
  hiện, thời điểm và ảnh dữ liệu trước/sau — **không có trường lý do**. Kiểm thêm bằng **tài khoản quản trị**
  (chỉ để điều tra, không dùng ra verdict) trên cùng 2 hồ sơ: vẫn **không có** lý do trong nhật ký ⇒ không phải
  vấn đề phạm vi đọc của tài khoản.
- **Không phải mất dữ liệu:** lý do vẫn được lưu **đầy đủ, khớp từng chữ** ở bản ghi phân công của vụ việc, và
  vẫn tới được cán bộ phụ trách qua **thông báo trong ứng dụng + thư**. Chỗ thiếu **chỉ nằm ở nhật ký vụ việc** —
  tức nơi đặc tả bắt buộc phải có, và cũng là nơi cán bộ tra lại hồ sơ về sau.
- **Không riêng thao tác từ chối:** đọc thêm nhật ký của các hành động khác cũng thuộc nhóm bắt buộc có lý do
  (`Yêu cầu bổ sung`) trên các hồ sơ khác — cũng **không** mang lý do. Ghi nhận để dev biết phạm vi sửa có thể
  rộng hơn một thao tác; **không** dùng để kéo verdict của case này.

### Bằng chứng

**1. Ảnh chụp**

![BUG-VV-XNTGHTVV-03 — Ngay sau khi bấm Xác nhận từ chối trên VV-BTP-TW-20260806-002: hệ thống về màn danh sách vụ việc, thông báo màu xanh dấu tích "Đã từ chối phân công" ở đỉnh màn, KHÔNG có màn chặn quyền truy cập; tab "Tất cả" còn 8 và bản ghi vừa từ chối không còn trong danh sách của người được phân công](image/XNTGHTVV_03-07-VV2-dang2-thong-bao-ngay-sau-khi-Xac-nhan-tu-choi.png)

![BUG-VV-XNTGHTVV-03 — ẢNH LỖI: cán bộ nghiệp vụ phụ trách (CB Nghiệp vụ - Trung ương #01) mở lại VV-BTP-TW-20260806-002 sau thao tác. Badge trạng thái đã đúng "Đã tiếp nhận" (chặng 3) và có nút [Phân công] để phân công lại; khối "Dòng thời gian" có dòng "Từ chối phân công 06/08/2026 14:53 QA TVV Seed28 Active" nhưng KHÔNG kèm lý do, và trên toàn màn không còn chỗ nào hiển thị lý do từ chối](image/XNTGHTVV_03-09-VV2-sau-tu-choi-trang-thai-Da-tiep-nhan-va-nhat-ky-Tu-choi-phan-cong.png)

![BUG-VV-XNTGHTVV-03 — Đối chứng vế thông báo (đã hết lỗi): chuông thông báo của cán bộ nghiệp vụ phụ trách có 2 tin mới "Người hỗ trợ đã từ chối tham gia vụ việc - ..." ứng với 2 hồ sơ vừa bị từ chối](image/XNTGHTVV_03-08-cbnv-tw-01-chuong-thong-bao-nhan-tu-choi-kem-ly-do.png)

![BUG-VV-XNTGHTVV-03 — Dạng ③ (hồ sơ do doanh nghiệp tự gửi) trước thao tác: VV-STP-AG-20260806-004 ở "Đã phân công", thanh hành động đủ [Chấp nhận] [Từ chối], tài khoản đang đăng nhập là QA NHT An Giang UAT2 — đúng người được phân công](image/XNTGHTVV_03-10-VV4-dang3-truoc-khi-tu-choi-nguoi-tao-la-doanh-nghiep.png)

![BUG-VV-XNTGHTVV-03 — Dạng ③ ngay sau khi từ chối: hệ thống về màn danh sách, KHÔNG có màn chặn quyền truy cập, và VV-STP-AG-20260806-004 không còn trong danh sách của người được phân công](image/XNTGHTVV_03-11-VV4-dang3-sau-tu-choi-ve-danh-sach-khong-co-man-403.png)

**1-bis. Bằng chứng vòng re-verify R3 (2026-08-07, bản dựng `V1.0.10`) — vế lưu vết ĐÃ HẾT LỖI**

![BUG-VV-XNTGHTVV-03 — R3: phiên cán bộ phụ trách CB Nghiệp vụ - Trung ương #01 mở VV-BTP-TW-20260806-001 sau thao tác từ chối MỚI. Hồ sơ đã về "Đã tiếp nhận" nên nhóm "Phân công Người hỗ trợ / Tư vấn viên" không hiển thị; khối "Dòng thời gian" có mục "Từ chối phân công 07/08/2026 01:22 QA TVV Seed28 Active" KÈM dòng "Lý do: QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1". Mục từ chối cũ 06/08/2026 14:43 ngay bên dưới vẫn KHÔNG có dòng Lý do — đúng bản chất dữ liệu ghi trước bản fix](image/XNTGHTVV_03-R3-02-VV001-cbnv-tw-01-dong-thoi-gian-hien-Ly-do-tu-choi.png)

![BUG-VV-XNTGHTVV-03 — R3 dạng ② (người tạo khác người phân công): cùng phiên cán bộ phụ trách mở VV-BTP-TW-20260806-002, Dòng thời gian có mục "Từ chối phân công 07/08/2026 01:23" kèm "Lý do: QA-XNTG-20260807-0130-tu-choi-tham-gia-ho-tro-dang-2"; mục cũ 06/08/2026 14:53 không có dòng Lý do](image/XNTGHTVV_03-R3-03-VV002-cbnv-tw-01-dong-thoi-gian-hien-Ly-do-tu-choi.png)

![BUG-VV-XNTGHTVV-03 — R3 dạng ③ (hồ sơ do doanh nghiệp tự gửi): phiên CB Nghiệp vụ - Địa phương #01 mở VV-STP-AG-20260806-004, Dòng thời gian có mục "Từ chối phân công 07/08/2026 01:24 QA NHT An Giang UAT2" kèm "Lý do: QA-XNTG-20260807-0140-tu-choi-tham-gia-ho-tro-dang-3", và mục gốc "Tạo vụ việc 06/08/2026 14:38 QA UAT DN An Giang" xác nhận người tạo là doanh nghiệp](image/XNTGHTVV_03-R3-04-VV004-cbnv-dp-01-dong-thoi-gian-hien-Ly-do-tu-choi-dang-DN-tao.png)

Đường đo thứ hai R3 — `GET /api/v1/vu-viecs/{id}/lich-su` bằng chính phiên cán bộ phụ trách, mục `TU_CHOI_PHAN_CONG` mới nay có thêm trường `lyDo`:

```
-001  2026-08-06T18:22:40.206Z  lyDo = QA-XNTG-20260807-0125-tu-choi-tham-gia-ho-tro-dang-1   (khop 52/52)
-002  2026-08-06T18:23:33.898Z  lyDo = QA-XNTG-20260807-0130-tu-choi-tham-gia-ho-tro-dang-2   (khop 52/52)
-004  2026-08-06T18:24:49.161Z  lyDo = QA-XNTG-20260807-0140-tu-choi-tham-gia-ho-tro-dang-3   (khop 52/52)
cac truong co: id - hanhDong - entityType - nguoiThucHienId - nguoiThucHien - thoiGian - lyDo - duLieuCu - duLieuMoi
```

> Phần **1** và **2** dưới đây là bằng chứng của vòng đo 06/08 (bản dựng `V1.0.8`) — giữ nguyên làm lịch sử đối chiếu.

**2. Đối chứng bằng đường thứ hai — đọc lại bản ghi từ máy chủ**

Nhật ký vụ việc `VV-BTP-TW-20260806-002` — mục ứng với thao tác từ chối (đọc bằng phiên `cbnv_tw_02`, đọc lại
bằng tài khoản quản trị cho cùng kết quả):

```
hành động      : TU_CHOI_PHAN_CONG
người thực hiện: QA TVV Seed28 Active
thời điểm      : 2026-08-06T07:53:24.373Z
các trường có  : id · entityType · hanhDong · nguoiThucHienId · nguoiThucHien · thoiGian · duLieuCu · duLieuMoi
trường lý do   : KHÔNG CÓ
```

Bản ghi phân công của **cùng vụ việc đó**, đọc ở cùng thời điểm — lý do **vẫn còn nguyên**:

```json
{
  "trangThai": "TU_CHOI",
  "lyDoTuChoi": "QA verify XNTGHTVV_03 batch B6 - tu choi tham gia ho tro - dang 2 nguoi phan cong khac nguoi tao",
  "ngayPhanCong": "2026-08-06T07:40:14.103Z",
  "ngayCapNhat":  "2026-08-06T07:53:24.351Z"
}
```

Trạng thái hồ sơ đọc lại ngay sau thao tác: `"trangThai": "DA_TIEP_NHAN"`, `"nguoiXuLyId": null`,
`"coPhanCongBiTuChoi": true` — **không** phải "Chờ phê duyệt". Lời gọi thực hiện thao tác từ chối trả về
**thành công** (`201`), **đúng 1 lời gọi** cho 1 lần bấm, **không** có mã 403 nào.

**3. Thông báo gửi cán bộ — nguyên văn (vế này đã hết lỗi)**

```
Tiêu đề : Người hỗ trợ đã từ chối tham gia vụ việc - VV-BTP-TW-20260806-002
Nội dung: Người được phân công đã từ chối tham gia hỗ trợ vụ việc:
          - Mã vụ việc: VV-BTP-TW-20260806-002
          - Doanh nghiệp: Cong ty TNHH QA UAT Kiem Thu
          - Lý do từ chối: QA verify XNTGHTVV_03 batch B6 - tu choi tham gia ho tro - dang 2 nguoi phan cong khac nguoi tao

          Vụ việc đã chuyển về trạng thái "Đã tiếp nhận" để phân công lại.
```

Người nhận đo được ở cả 3 dạng là **cán bộ nghiệp vụ đang phụ trách hồ sơ (người tiếp nhận)**, trên **cả hai
kênh**; ở dạng ③ (hồ sơ do doanh nghiệp tự gửi) thì **doanh nghiệp không nhận**, cán bộ tiếp nhận `cbnv_dp_01`
**có nhận** — đúng bằng *"cán bộ nghiệp vụ phụ trách"*.

**Hoàn nguyên dữ liệu:** 3 vụ việc QA tự tạo mới, không sửa/xóa bản ghi có sẵn nào. Ba hồ sơ này hiện ở
"Đã tiếp nhận" và có thể phân công lại bình thường; để nguyên làm dữ liệu tiền đề cho vòng verify sau.

### Cách verify sau khi fix

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản cán bộ nghiệp vụ đang phụ trách hồ sơ (ví dụ cbnv_tw_01) + màn chi tiết vụ việc /vu-viec/{id}, khối "Dòng thời gian".
  Cần 1 vụ việc ở "Đã phân công" mà người được phân công đã bấm Từ chối kèm lý do.
  Chưa có thì tạo mới bằng luồng chuẩn: cán bộ nhập hồ sơ thủ công -> tiếp nhận -> kiểm tra hồ sơ kết luận Đạt -> Phân công cho một tư vấn viên / người hỗ trợ -> đăng nhập chính người đó -> [Từ chối] -> nhập lý do >= 10 ký tự (ghi lại nguyên văn chuỗi đã nhập) -> Xác nhận.
1) Đăng nhập cán bộ nghiệp vụ phụ trách hồ sơ đó, mở chi tiết vụ việc, cuộn tới khối "Dòng thời gian".
2) Đọc mục ứng với thao tác từ chối phân công: phải thấy được lý do từ chối đã nhập ở bước dựng tiền đề.
3) Đo bằng đường thứ hai: đọc lại nhật ký của chính vụ việc đó từ máy chủ (GET /api/v1/vu-viecs/{id}/lich-su) và đối chiếu mục có hành động từ chối phân công.
✅ PASS khi: mục nhật ký của thao tác từ chối phân công mang lý do khác rỗng và khớp từng chữ chuỗi đã nhập, ĐỒNG THỜI cán bộ đọc được lý do đó ngay trên hồ sơ. Đúng ở cả hai đường đo, và lặp lại được trên ít nhất 2 hồ sơ khác nhau.
❌ FAIL nếu: nhật ký vẫn không có lý do; hoặc máy chủ đã có lý do nhưng màn hình không cho cán bộ đọc được (fix một phần vẫn là FAIL); hoặc lý do lệch so với chuỗi đã nhập.
⚠️ Đừng chấm FAIL vì cách trình bày dòng nhật ký (thứ tự, định dạng ngày giờ, chỗ đặt lý do) — đặc tả không quy định phần này.
⚠️ Đừng chấm PASS vì thấy lý do hiện trong thông báo gửi cán bộ hoặc trong bản ghi phân công — hai chỗ đó đã có sẵn từ trước và không thay cho nhật ký; phải đọc đúng mục nhật ký của vụ việc.
Ảnh lỗi lần này: output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/image/XNTGHTVV_03-09-VV2-sau-tu-choi-trang-thai-Da-tiep-nhan-va-nhat-ky-Tu-choi-phan-cong.png
```

**Owner:** Dev BE (bổ sung lý do vào nhật ký vụ việc cho thao tác từ chối phân công) + Dev FE (chỗ hiển thị lý do
trên màn chi tiết cho cán bộ, sau khi hồ sơ đã quay về "Đã tiếp nhận").
**Việc tiếp theo:** dev fix → QA re-verify theo đúng khối CÁCH VERIFY ở trên, trên ≥ 2 hồ sơ mới dựng.

---

## BUG-VV-DGKQHTVV-01 — Đánh giá kết quả hỗ trợ vụ việc: doanh nghiệp chủ vụ việc vẫn không mở được chi tiết vụ việc của chính mình nên không có đường vào đánh giá

> **Re-test:** 2026-08-07 02:15:00 R3 — 🔁 REOPEN (vế quyết định vẫn hỏng). Môi trường `https://18.143.165.120.nip.io` (env nội bộ) · bản dựng `HTPLDN · V1.0.10` / bó mã `assets/index-B2W2Krcs.js` / `last-modified Thu, 06 Aug 2026 17:39:54 GMT` / `etag W/"6a74c6ea-428"` — cả 4 dấu trùng, không có triển khai mới xen giữa 2 case. **Ra verdict bằng TÀI KHOẢN DOANH NGHIỆP** `0209888006` (*QA UAT DN An Giang*) và `0109998887` (*QA UAT Kiem Thu DN*), `Test@1234`, đăng nhập được ngay lần đầu — **không dùng `admin`, không dùng tài khoản cán bộ**. **N = 10 bản ghi** đọc từ máy chủ (8 vụ việc của DN #1 + 2 của DN #2), **3 vụ việc mở bằng giao diện**, **2 doanh nghiệp**. **M = 2/4 dạng** (**D2 doanh nghiệp × trạng thái đánh giá được — ❌ hỏng, dạng quyết định** · D4 kiểm trùng — ✅ đạt; D1 nhánh cán bộ chỉ để kiểm hồi quy, **chưa chạy lại vòng này**; D3 vẫn không dựng được — đã loại Đường A vì `VV-BTP-TW-20260806-003/-004` **không** nằm trong danh sách của `0109998887`). **Phép đo quyết định:** doanh nghiệp bấm mã vụ việc của **chính mình** trong danh sách của mình (`VV-STP-AG-20260806-005`, *Đã đánh giá*) → vẫn bị đẩy sang trang báo không có quyền; lặp lại y hệt khi mở thẳng bằng địa chỉ, và lặp lại trên doanh nghiệp thứ hai (`VV-STP-HN-20260806-001`) ⇒ **0 phần tử** dẫn tới việc đánh giá. **Đường đo thứ hai** (gọi thẳng nguồn dữ liệu bằng chính phiên DN, 10/10 bản ghi): hồ sơ chính **200** · kết quả **200** (*đã sửa được so với vòng trước*) · **phân công 403** · **kết quả kiểm tra 403**, mã `ERR-AUTH-DN-00-01` — giao diện bắt 403 rồi chặn cả trang thay vì ẩn 2 nhóm này theo `:1805` `:1806`. **Đã tiến bộ:** máy chủ **không còn** chặn thao tác đánh giá theo vai trò doanh nghiệp. **Đạt:** chứng âm phạm vi (404) và kiểm trùng (409, dữ liệu cũ không bị ghi đè). **Không tạo/sửa/xoá bản ghi nào** — 2 lời gọi ghi đều bị máy chủ từ chối. **Kết luận chỉ có hiệu lực cho env + bản dựng nêu trên.**

### Mô tả

Case này có hai vế. **Vế "gửi đánh giá xong đọc lại được ở Nhóm 8" đã hết lỗi ở nhánh cán bộ
nghiệp vụ**: đo trên 2 vụ việc riêng, sau khi **tải lại trang** Nhóm 8 hiển thị đủ 3 điểm vừa nhập,
điểm tổng bằng trung bình 3 điểm, đúng chuỗi nhận xét đã nhập, kèm người đánh giá và mốc giờ; trạng thái
vụ việc chuyển "Đã đánh giá"; nhật ký có thêm đúng một mục đánh giá; đường đo thứ hai (đọc lại bản ghi
từ máy chủ) trùng khít với những gì màn hình hiển thị.

**Vế "không có điểm vào thao tác đánh giá" còn nguyên ở nhánh doanh nghiệp.** Doanh nghiệp là chủ vụ
việc, vụ việc đang ở "Hoàn thành", chưa có đánh giá nào của loại doanh nghiệp — nhưng trên giao diện
**không đếm được phần tử nào** dẫn tới việc đánh giá, và bấm vào chính vụ việc của mình thì bị đẩy sang
trang báo không có quyền truy cập. Đây **không phải** chuyện thiếu một nút: đo bằng đường thứ hai, máy chủ
cũng từ chối chính thao tác đánh giá khi người gọi là doanh nghiệp, kèm mã `ERR-AUTH-DN-00-01`.

Hiện tượng lặp lại **giống hệt trên hai doanh nghiệp khác nhau**, mỗi doanh nghiệp trên vụ việc của chính
mình ⇒ không phải đặc thù một tài khoản hay một địa phương.

### Các bước tái hiện

**Tiền đề (tự dựng bằng luồng chuẩn trên dữ liệu QA):** doanh nghiệp `0209888006` gửi hồ sơ → `cbnv_dp_01`
tiếp nhận → kiểm tra hồ sơ kết luận Đạt → phân công người xử lý → cập nhật kết quả → trình phê duyệt →
`cbpd_dp_01` phê duyệt → cập nhật kết quả cuối → vụ việc `VV-STP-AG-20260806-005` ở **"Hoàn thành"**,
Nhóm 8 còn rỗng.

1. Đăng nhập tài khoản doanh nghiệp `0209888006` / `Test@1234` (tên đăng nhập của doanh nghiệp là mã số
   thuế), lấy mã OTP ở hộp thư thử nghiệm.
2. Mở danh sách vụ việc của doanh nghiệp, xác định dòng `VV-STP-AG-20260806-005` đang mang nhãn
   **"Đã hoàn thành"**. Đếm số phần tử tương tác dẫn tới việc đánh giá ngay trên dòng đó.
3. Bấm mở chi tiết chính vụ việc đó. Quan sát địa chỉ trang và nội dung hiển ra.
4. Đường đo thứ hai — bằng chính phiên đăng nhập của doanh nghiệp đó, gọi thẳng thao tác đánh giá vụ việc
   này với bộ điểm 9 · 8 · 10 và một chuỗi nhận xét mốc giờ duy nhất; đọc mã và thông điệp trả về.
5. Lặp lại bước 1-3 với doanh nghiệp `0109998887` trên vụ việc của chính doanh nghiệp đó
   (định danh `ac866cde-…`).
6. Để đối chiếu nhánh đã hết lỗi: đăng nhập `cbnv_tw_01`, mở `VV-BTP-TW-20260806-003` ở "Hoàn thành",
   đánh giá với bộ điểm 9 · 8 · 10 + nhận xét `QA-DGKQ-20260806-1634`, rồi **tải lại trang bằng địa chỉ**
   và đọc lại Nhóm 8. Lặp trên `VV-BTP-TW-20260806-004` với nhận xét `QA-DGKQ-20260806-1701`.

### Kết quả mong đợi

| Dòng đặc tả | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1190` | "**Mô tả:** CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc." |
| `srs-fr-05-vu-viec.md:1198` | "\| PRE-03 \| Role ∈ {CB_NV, DN} (theo CSV UC67) \|" |
| `srs-fr-05-vu-viec.md:1215` | "\| 1 \| Kiểm tra quyền: role ∈ {CB_NV, DN} \| BR-AUTH-01 \|" |
| `srs-fr-05-vu-viec.md:1216` | "\| 2 \| Validate scope theo role: nếu role='DN' → `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id`… \|" |
| `srs-fr-05-vu-viec.md:2116` | "\| 4 \| loai_nguoi_danh_gia \| text \| Y \| CHECK IN ('CB_NV','DN') \| — \| Loại người đánh giá (theo CSV UC67: chỉ CB Nghiệp vụ và Doanh nghiệp) \|" |
| `srs-fr-05-vu-viec.md:1809` | "\| Nhóm 8 — Đánh giá \| Cho phép nhập khi vụ việc ở "Hoàn thành" / "Đã đánh giá" + DN chưa đánh giá… \|" |
| `srs-fr-05-vu-viec.md:1811` | "\| Thanh thao tác \| Chỉ 2 nút DN được phép: **[Bổ sung hồ sơ]**…; **[Đánh giá]** (khi trạng thái = "Hoàn thành" / "Đã đánh giá" + chưa đánh giá)… \|" |
| `srs-fr-05-vu-viec.md:1792` | Đặc tả có hẳn **chế độ xem dành cho doanh nghiệp** của màn chi tiết vụ việc, kèm địa chỉ riêng |

⇒ Doanh nghiệp chủ vụ việc phải **mở được chi tiết vụ việc của chính mình** và phải **có đường vào để
đánh giá** khi vụ việc ở "Hoàn thành" hoặc "Đã đánh giá" và doanh nghiệp chưa đánh giá; đánh giá của doanh
nghiệp là một trong hai loại đánh giá hệ thống phải lưu được.

### Kết quả thực tế

**1. Nhánh doanh nghiệp — còn lỗi (vế quyết định verdict)**

| Đo gì | Kết quả |
|---|---|
| DN `0209888006` · danh sách vụ việc của chính mình | Thấy `VV-STP-AG-20260806-005` nhãn **"Đã hoàn thành"**; **0** phần tử tương tác dẫn tới việc đánh giá |
| DN `0209888006` · bấm mở chi tiết chính vụ việc đó | Bị đẩy sang **trang báo không có quyền truy cập**; không xem được Nhóm 8, không thấy thanh thao tác |
| Nguyên nhân đọc được tại chỗ | **3** lời gọi lấy dữ liệu của màn chi tiết bị từ chối vì vai trò (thông tin phân công · kết quả · kết quả kiểm tra), mỗi lời gọi trả `403`; giao diện bắt được lỗi này rồi chuyển thẳng sang trang không có quyền |
| Đường đo thứ hai — gọi thẳng thao tác đánh giá bằng phiên của chính DN đó | Bị từ chối: `403` · mã `ERR-AUTH-DN-00-01` · thông điệp *"Role không được phép truy cập endpoint CMS này"* ⇒ **không phải lỗi bề mặt giao diện**, máy chủ cũng không cho doanh nghiệp đánh giá |
| DN `0109998887` · vụ việc của chính mình (`ac866cde-…`) | **Cùng hiện tượng** — bị đẩy sang trang không có quyền |
| Địa chỉ chế độ xem dành cho doanh nghiệp (`:1792`) | Không tồn tại trên bản dựng này — mở ra trang "không tìm thấy"; bảng định tuyến của giao diện chỉ có danh sách vụ việc, tạo mới và chi tiết dùng chung cho mọi vai trò |

⇒ Đúng **F1** của file tiêu chí: vai trò đúng + vụ việc ở "Hoàn thành" + đúng phạm vi (doanh nghiệp là chủ
vụ việc) nhưng **không có bất kỳ phần tử nào** cho phép bắt đầu đánh giá.

**1-bis. Bằng chứng vòng re-verify R3 — 2026-08-07, bản dựng `V1.0.10` (đo lại bằng TÀI KHOẢN DOANH NGHIỆP)**

*Xác minh quyền sở hữu trước, không đoán:* gọi danh sách vụ việc bằng chính phiên doanh nghiệp — máy chủ cố định lọc theo doanh
nghiệp đăng nhập (`:1846`) nên mọi dòng trả về đều thuộc doanh nghiệp đó. DN `0209888006` có **8** vụ việc (cả 8 mang tên
*Cong ty QA UAT An Giang*), DN `0109998887` có **5** vụ việc.

| Cách mở | Tài khoản | Vụ việc | Kết quả |
|---|---|---|---|
| Mở thẳng bằng địa chỉ chi tiết | DN `0209888006` | `VV-STP-AG-20260806-005` — **"Đã đánh giá"** | ❌ bị đẩy sang trang báo không có quyền — *"Vai trò hiện tại: Doanh nghiệp"* |
| **Bấm mã vụ việc trong danh sách của chính doanh nghiệp** | DN `0209888006` | `VV-STP-AG-20260806-005` | ❌ **y hệt** — không phải chuyện gõ tay địa chỉ |
| Mở thẳng bằng địa chỉ chi tiết | DN `0109998887` | `VV-STP-HN-20260806-001` — "Đang kiểm tra" | ❌ **y hệt** ⇒ lặp trên doanh nghiệp thứ hai |
| Mở thẳng bằng địa chỉ chi tiết | DN `0209888006` | `VV-STP-AG-20260806-004` — "Đã tiếp nhận" | ✅ **mở được**, và **không** hiện phần kết quả kiểm tra / phân công / trao đổi nội bộ ⇒ đúng `:1805` `:1806` `:1808`, **không log thành lỗi** |

Trên màn danh sách, cột **Hành động** chỉ có **1** biểu tượng xem, **không có** đường vào đánh giá ⇒ đếm được **0** phần tử.

*Đường đo thứ hai — gọi thẳng nguồn dữ liệu bằng chính phiên doanh nghiệp, trên 10/10 bản ghi của 2 doanh nghiệp:*

| Nguồn dữ liệu màn chi tiết cần | DN `0209888006` (8/8) | DN `0109998887` (2/2) | Mã lỗi |
|---|---|---|---|
| Hồ sơ chính | **200** | **200** | — |
| Kết quả xử lý (Nhóm 6) | **200** | **200** | — · **đã sửa được so với vòng 06/08** |
| Phân công xử lý (Nhóm 5) | **403** | **403** | `ERR-AUTH-DN-00-01` — *"Role không được phép truy cập endpoint CMS này"* |
| Kết quả kiểm tra (Nhóm 4) | **403** | **403** | `ERR-AUTH-DN-00-01` |

Nhật ký trình duyệt lúc bị chặn: `[403] Yêu cầu bị từ chối: GET /vu-viecs/0dfb2b25-…/ket-qua-kiem-tra`. **Đã kiểm chéo:** 403 ở đây
**không phải** `GET /files/…` `ERR-PERM-FILE-03` của hồ sơ tư vấn viên, nên không nhầm sang lỗi đã log ở case khác.

⇒ Còn **2/3** nguồn dữ liệu bị từ chối, và giao diện vẫn **bắt lỗi rồi chuyển cả trang** sang trang không có quyền, thay vì **ẩn**
hai nhóm đó như `:1805` `:1806` yêu cầu. Bằng chứng ẩn đúng là làm được: chính `VV-STP-AG-20260806-004` mở ra bình thường và đã ẩn sạch.

*Phần đã tốt lên ở máy chủ:* thao tác đánh giá gọi bằng chính phiên doanh nghiệp **không còn** trả `403 ERR-AUTH-DN-00-01` như vòng
trước — nó đã vào tới tầng nghiệp vụ. Trên `VV-STP-AG-20260806-005` cũng đã tồn tại sẵn **một** bản ghi đánh giá loại doanh nghiệp
(`9 · 8 · 10`, điểm tổng `9`, nhận xét `DN danh gia tren 120 v1.0.9`, 06/08/2026 13:06). 🔴 **Không dùng bản ghi này để chấm Pass:**
không do QA tạo trong vòng đo này và được tạo trên bản dựng khác. Nó chỉ chứng minh **máy chủ đã mở quyền**; vế quyết định của phiếu
là **doanh nghiệp có đường vào trên giao diện hay không**, và vế đó vẫn hỏng.

*Hai bước bắt buộc còn lại — cả hai đạt:* chứng âm phạm vi (doanh nghiệp đọc và thử đánh giá vụ việc của doanh nghiệp khác) → bị từ
chối, mã `ERR-VAL-VI-03-02`, và vụ việc đó cũng không có trong danh sách của mình; kiểm trùng (đánh giá lần hai cùng vụ việc) → bị từ
chối kèm *"Vụ việc đã được đánh giá"*, đọc lại vẫn **đúng 1 bộ điểm**, nhận xét cũ **không bị ghi đè**.

*Chưa đo được, nói rõ:* **D1 nhánh cán bộ** (chỉ để kiểm hồi quy) **chưa chạy lại vòng này** — không ảnh hưởng verdict vì verdict do D2
quyết. **D3** vẫn không dựng được: đã xác minh `VV-BTP-TW-20260806-003/-004` **không** nằm trong danh sách của `0109998887` nên loại
đường A, còn đường B phụ thuộc đúng vế đang hỏng ⇒ ghi nhận + gửi BA, **không kéo verdict**. Tiền đề *"Hoàn thành, doanh nghiệp chưa
đánh giá"* cũng không dựng được vì vụ việc duy nhất khả dụng đã bị tiêu bởi lượt đánh giá tạo trên bản dựng cũ — **không dựng thêm** vì
nút thắt nằm ở bước mở màn chi tiết, đã chứng minh trên 10 bản ghi × 2 doanh nghiệp.

*Ghi nhận ngoài phạm vi, xếp **candidate**, **không** dùng làm căn cứ verdict:* (a) Dòng thời gian ở chế độ doanh nghiệp đang hiện cả
sự kiện nội bộ *Phân công* / *Từ chối phân công* kèm tên cán bộ, trong khi `:1810` yêu cầu ẩn sự kiện nội bộ — chưa chạy đường đo thứ
hai riêng cho vế này và màn hình liên quan đang là đối tượng của chính bug này; (b) danh sách của `0109998887` không trả 2 vụ việc mang
cùng mã doanh nghiệp (`VV-BTP-TW-20260806-003/-004`).

*Hoàn nguyên:* **không tạo, không sửa, không xoá** bản ghi nào trong vòng R3 — hai lời gọi ghi duy nhất là phép thử bắt buộc của bước
chứng âm và bước kiểm trùng, cả hai đều bị máy chủ từ chối. Đọc lại `VV-STP-AG-20260806-005` sau khi thử: điểm và nhận xét y nguyên.


**2. Nhánh cán bộ nghiệp vụ — đã hết lỗi (ghi để dev không sửa lại chỗ đã đúng)**

| Bản ghi | Điểm nhập | Nhận xét | Nhóm 8 **sau khi tải lại trang** | Trạng thái | Đường đo thứ hai |
|---|---|---|---|---|---|
| `VV-BTP-TW-20260806-003` | 9 · 8 · 10 | `QA-DGKQ-20260806-1634` | Đọc được 9/10 · 8/10 · 10/10 · **điểm tổng 9/10** · đúng chuỗi nhận xét · người đánh giá "CB Nghiệp vụ - Trung ương #01" · 06/08/2026 16:34 | **"Đã đánh giá"**, thanh tiến trình 10/10 | Trùng khít từng trường, kèm 1 mục nhật ký đánh giá |
| `VV-BTP-TW-20260806-004` | 9 · 8 · 10 | `QA-DGKQ-20260806-1701` | Đọc được đủ 3 điểm · điểm tổng 9/10 · đúng chuỗi nhận xét · 06/08/2026 16:57 | **"Đã đánh giá"** | Trùng khít |

Thông báo sau khi gửi (bộ bắt cài **trước** khi bấm, không lọc trùng, đếm theo mốc giờ khác nhau):
**1 khung · 1 mốc giờ · 1 lời gọi**, nguyên văn **"Đã đánh giá vụ việc"** — đúng loại, đúng hành động,
đúng kết cục ⇒ không chạm F7. (Lưu ý hồ sơ: chuỗi mốc giờ `…-1701` được soạn trước, thao tác thực hiện
lúc 16:57 — chuỗi vẫn duy nhất nên không ảnh hưởng phép đo, ghi ra để khắc phục được khi đối chiếu.)

**3. Hai ca biên đã đo (đều đạt)**

| Ca | Kết quả |
|---|---|
| Nhập điểm ngoài khoảng 0-10 (nhập **11**) | Giao diện chặn ngay, **0 lời gọi** gửi đi, ô báo lỗi tại chỗ và nhãn ô ghi rõ khoảng "(0-10)"; gọi thẳng máy chủ cũng bị từ chối kèm thông điệp nêu khoảng hợp lệ; đọc lại **không sinh bản ghi đánh giá nào** ⇒ không chạm F8 |
| Đánh giá **lần 2 cùng loại người** trên `VV-BTP-TW-20260806-003` | Giao diện không còn đường vào sau khi đã đánh giá; gọi thẳng máy chủ thì bị từ chối kèm thông điệp *"Vụ việc đã được đánh giá"*; đọc lại vẫn **đúng 1 bộ điểm**, không bị ghi đè ⇒ không chạm F6 |

**4. Dạng D3 (một bên đã chấm, bên còn lại vào chấm) — không dựng được**

Muốn có dạng này phải có đánh giá của phía doanh nghiệp, mà phía doanh nghiệp đang bị chặn hoàn toàn.
Quan sát gần nhất: vụ việc `VV-QA-008` đang ở **"Đã đánh giá"** nhưng **không kèm bản ghi đánh giá nào**;
cán bộ nghiệp vụ mở ra không thấy đường vào đánh giá và Nhóm 8 vẫn rỗng. Dạng này chạm điểm đặc tả
**chưa thống nhất** giữa `:1751` (bảng nút theo trạng thái, chỉ có dòng "Hoàn thành") và `:1197` / `:1734` /
`:1811` (đều bao gồm "Đã đánh giá") ⇒ **đã gửi BA**, không chấm Fail, **không kéo verdict case**
([cau-hoi-BA.md](cau-hoi-BA.md)).

**Hoàn nguyên dữ liệu:** không xóa/sửa bản ghi có sẵn nào của đối tác. Ba vụ việc QA đã đẩy tiếp bằng
luồng chuẩn để nguyên làm dữ liệu tiền đề cho vòng sau: `VV-BTP-TW-20260806-003` và `-004` đang ở
"Đã đánh giá" (mỗi vụ việc có 1 đánh giá loại cán bộ nghiệp vụ), `VV-STP-AG-20260806-005` đang ở
"Hoàn thành" và **chưa có đánh giá nào** — dùng lại được ngay cho lần verify sau.

### Bằng chứng

| Ảnh | Chụp gì |
|---|---|
| `image/DGKQHTVV_01-08-D2-DN-0209888006-mo-chi-tiet-VV-cua-chinh-minh-bi-403.png` | **Ảnh quyết định verdict** — doanh nghiệp `0209888006` bấm mở chi tiết vụ việc của chính mình thì ra trang báo không có quyền truy cập |
| `image/DGKQHTVV_01-09-D2-DN-0109998887-mo-chi-tiet-VV-cua-chinh-minh-cung-bi-403.png` | Doanh nghiệp thứ hai, vụ việc của chính mình — cùng hiện tượng |
| `image/DGKQHTVV_01-01-D1-truoc-khi-danh-gia-nhom8-Chua-co-thong-tin.png` | Nhóm 8 còn rỗng trước khi đánh giá (mốc so sánh) |
| `image/DGKQHTVV_01-02-D1-hop-thoai-Danh-gia-chat-luong-3-o-diem-1-o-nhan-xet.png` | Chỗ nhập đánh giá: đủ 3 ô điểm + 1 ô nhận xét |
| `image/DGKQHTVV_01-03-a3-nhap-diem-11-truoc-khi-bam-Xac-nhan.png` | Ca biên điểm ngoài khoảng: nhập 11, giao diện báo lỗi tại chỗ |
| `image/DGKQHTVV_01-04-D1-da-nhap-9-8-10-nhan-xet-QA-DGKQ-20260806-1634-truoc-khi-bam.png` | Bộ giá trị 9 · 8 · 10 + chuỗi nhận xét mốc giờ, ngay trước khi gửi |
| `image/DGKQHTVV_01-05-D1-thong-bao-ngay-sau-khi-bam-Xac-nhan.png` | Thông báo ngay sau khi gửi — nguyên văn "Đã đánh giá vụ việc" |
| `image/DGKQHTVV_01-06-D1-SAU-KHI-TAI-LAI-TRANG-nhom8-doc-du-3-diem-diem-tong-9-nhan-xet.png` | **Ảnh quyết định vế đã hết lỗi** — sau khi tải lại trang, Nhóm 8 đọc đủ 3 điểm + điểm tổng + nhận xét |
| `image/DGKQHTVV_01-07-D1-sau-tai-lai-nhan-Da-danh-gia-va-thanh-tien-trinh-10-buoc.png` | Sau khi tải lại: nhãn "Đã đánh giá" + thanh tiến trình 10/10 |
| `image/DGKQHTVV_01-10-D3-VV-QA-008-trang-thai-Da-danh-gia-khong-co-nut-Danh-gia.png` | Dạng D3: vụ việc ở "Đã đánh giá" nhưng không có đường vào đánh giá |
| `image/DGKQHTVV_01-11-D1b-VV004-thong-bao-ngay-sau-khi-bam-Xac-nhan.png` | Bản ghi thứ hai của nhánh cán bộ: thông báo ngay sau khi gửi |
| `image/DGKQHTVV_01-12-D1b-VV004-sau-tai-lai-nhom8-doc-du-3-diem-va-nhan-xet.png` | Bản ghi thứ hai, sau khi tải lại trang: Nhóm 8 đọc đủ |

**Ảnh vòng re-verify R3 (2026-08-07, bản dựng `V1.0.10`):**

| Ảnh | Chụp gì |
|---|---|
| `image/DGKQHTVV_01-R3-01-DN0209888006-mo-VV005-cua-chinh-minh-bi-day-sang-403.png` | **Ảnh quyết định verdict R3** — phiên *QA UAT DN An Giang · Doanh nghiệp*, chân sidebar `HTPLDN · V1.0.10`; mở `VV-STP-AG-20260806-005` của **chính mình** ra trang *"Bạn không có quyền truy cập trang này. Vai trò hiện tại: Doanh nghiệp"* |
| `image/DGKQHTVV_01-R3-02-DN0209888006-danh-sach-vu-viec-cua-minh-8-dong-khong-co-nut-Danh-gia.png` | Danh sách vụ việc của chính doanh nghiệp: **8 dòng đều là *Cong ty QA UAT An Giang*** (chứng minh quyền sở hữu); dòng đầu nhãn **"Đã đánh giá"**; cột Hành động chỉ có 1 biểu tượng xem, **không có** đường vào đánh giá |
| `image/DGKQHTVV_01-R3-03-DN0109998887-mo-vu-viec-cua-chinh-minh-cung-bi-day-sang-403.png` | Doanh nghiệp thứ hai (*QA UAT Kiem Thu DN*) mở vụ việc của **chính mình** — **cùng hiện tượng** ⇒ lặp lại được |

### Cách verify sau khi fix

```
── CÁCH VERIFY sau Dev fix ──
Precondition: tài khoản doanh nghiệp (tên đăng nhập là mã số thuế) + màn danh sách vụ việc và màn chi tiết vụ việc của chính doanh nghiệp đó.
  Cần >= 2 vụ việc DO CHÍNH doanh nghiệp đó gửi, đang ở "Hoàn thành" và chưa có đánh giá của loại doanh nghiệp, trên >= 2 doanh nghiệp khác nhau.
  Chưa có thì tạo mới bằng luồng chuẩn: doanh nghiệp gửi hồ sơ -> cán bộ nghiệp vụ cùng địa bàn tiếp nhận -> kiểm tra hồ sơ kết luận Đạt -> phân công người xử lý -> cập nhật kết quả -> trình phê duyệt -> cán bộ phê duyệt duyệt -> cập nhật kết quả cuối -> "Hoàn thành".
1) Đăng nhập bằng CHÍNH TÀI KHOẢN DOANH NGHIỆP (không dùng tài khoản cán bộ, không dùng tài khoản quản trị). Mở danh sách vụ việc, bấm mã vụ việc "Hoàn thành" của chính mình để mở chi tiết. Phải xem được nội dung hồ sơ, không bị đẩy sang trang báo không có quyền.
2) Đếm số phần tử tương tác dẫn tới việc đánh giá (nhìn thấy bằng mắt trong khung nhìn, không moi bằng công cụ nhà phát triển). Kích hoạt nó, nhập 9 · 8 · 10 và một chuỗi nhận xét mốc giờ duy nhất dạng QA-DGKQ-<YYYYMMDD-HHMM>, rồi gửi. Cài bộ bắt thông báo TRƯỚC khi bấm, đếm theo mốc giờ khác nhau và đếm số lời gọi song song.
3) Tải lại trang bằng địa chỉ (không dùng lại màn cũ), mở lại phần Đánh giá và đọc nội dung.
4) Đo bằng đường thứ hai: bằng chính phiên đăng nhập của doanh nghiệp, đọc lại bản ghi đánh giá của vụ việc đó từ máy chủ và đối chiếu từng trường với những gì màn hình hiển thị ở bước 3.
5) Lặp bước 1-4 trên vụ việc thứ hai của cùng doanh nghiệp, và trên 1 doanh nghiệp KHÁC với vụ việc của chính doanh nghiệp đó.
6) Kiểm phạm vi (chứng âm): cùng tài khoản doanh nghiệp đó, thử mở và thử đánh giá một vụ việc CỦA DOANH NGHIỆP KHÁC -> phải bị từ chối.
7) Kiểm trùng: doanh nghiệp đánh giá lần thứ hai cùng vụ việc -> phải bị từ chối, đọc lại vẫn đúng 1 bộ điểm của loại doanh nghiệp, nhận xét cũ không bị ghi đè.
✅ PASS khi: doanh nghiệp mở được chi tiết vụ việc của chính mình; đếm được >= 1 phần tử dẫn tới việc đánh giá; gửi xong thì SAU KHI TẢI LẠI TRANG đọc được đúng 3 điểm đã nhập + đúng chuỗi nhận xét + điểm tổng bằng trung bình 3 điểm; đường đo thứ hai trùng khít và ghi loại người đánh giá là doanh nghiệp; đúng trên >= 2 vụ việc và >= 2 doanh nghiệp; chứng âm bước 6 và kiểm trùng bước 7 đều bị từ chối.
❌ FAIL nếu: doanh nghiệp vẫn không mở được chi tiết vụ việc của chính mình; hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá; hoặc gửi được và báo thành công nhưng sau khi tải lại trang phần đánh giá vẫn rỗng / thiếu >= 1 trong 3 điểm / nhận xét khác chuỗi đã nhập / điểm tổng khác trung bình 3 điểm; hoặc hai đường đo lệch nhau (fix một phần vẫn là FAIL); hoặc doanh nghiệp đánh giá được vụ việc của doanh nghiệp khác.
⚠️ Đừng chấm FAIL vì: nhãn / vị trí / kiểu hiển thị của đường vào đánh giá (nút trên thanh hành động hay điều khiển ngay trong phần đánh giá; hộp thoại hay mở tại chỗ); nguyên văn chữ thông báo thành công; cách làm tròn / định dạng điểm tổng (9 vs 9.0 vs 9,0); không có chức năng sửa/xoá đánh giá đã gửi; thứ tự - màu - bố cục trình bày lại 3 điểm; không ai nhận được thông báo sau khi đánh giá. Doanh nghiệp KHÔNG được thấy phần phân công xử lý và phần kết quả kiểm tra — thiếu 2 phần này là ĐÚNG đặc tả, không phải lỗi.
⚠️ Đừng chấm PASS vì: thấy nhãn trạng thái đã đổi sang "Đã đánh giá", thấy nhật ký đã có mục đánh giá, hay thấy thông báo báo thành công — cả ba dấu hiệu này ĐÃ từng đúng trong khi lỗi còn nguyên. Cũng đừng chấm PASS vì hệ thống đã nhận được lệnh đánh giá gửi thẳng, vì bản ghi đánh giá có sẵn từ bản dựng cũ, hay vì nhánh cán bộ nghiệp vụ chạy được — phải đo lại ĐÚNG nhánh doanh nghiệp, đi từ bước 1.
```

**Owner:** Dev BE (mở quyền cho vai trò doanh nghiệp ở thao tác đánh giá vụ việc và ở các nguồn dữ liệu mà
màn chi tiết cần, giới hạn đúng phạm vi vụ việc của chính doanh nghiệp đó) + Dev FE (chế độ xem dành
cho doanh nghiệp của màn chi tiết vụ việc và đường vào đánh giá; không đẩy người dùng sang trang báo
không có quyền khi chỉ một phần dữ liệu ngoài quyền).
**Việc tiếp theo:** dev fix → QA re-verify đúng khối CÁCH VERIFY ở trên, trên **≥ 2 vụ việc** và
**≥ 2 doanh nghiệp**; nhánh cán bộ nghiệp vụ chạy lại 1 bản ghi để chắc không hỏng theo.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | https://18.143.165.120.nip.io (env **nội bộ**, không phải env nghiệm thu đối tác) |
| Bản dựng | KTHSYCHTPL_11 + TKHSYCHTPL_03: `HTPLDN · V1.0.8` · `assets/index-CNwX9JjX.js` · `assets/index-DVlgOkLg.css` · `last-modified 06/08/2026 02:51:16 GMT` · `etag "6a73f6a4-428"`. XNTGHTVV_03: `HTPLDN · V1.0.8` · `assets/index-DIABnbIr.js` · `last-modified 06/08/2026 07:13:15 GMT` · `etag "6a74340b-428"` (**triển khai mới xen giữa lô**). CNKQHT_07: cùng bó mã `assets/index-DIABnbIr.js` / `etag "6a74340b-428"`, đo lại lúc 15:26 và 16:05. DGKQHTVV_01: cùng bó mã `assets/index-DIABnbIr.js` / `etag "6a74340b-428"`, tự đo lại lúc 16:20 |
| Máy chủ | `nginx/1.27.5` · `via: 1.1 Caddy` · API `HTPLDN API` `info.version 1.0.0` |
| OTP login | MailHog http://18.143.165.120:8025 |
| Tài khoản đã dùng | KTHSYCHTPL_11: `cbnv_dp_01` (ra verdict) · `cbnv_dp_02` (dựng dạng D2). TKHSYCHTPL_03: `cbnv_tw_01` (ra verdict, không phải fallback). XNTGHTVV_03: `qa_tvvseed28` + `nht_ag_uat2` (ra verdict — người được phân công) · `cbnv_tw_01`, `cbnv_tw_02`, `cbnv_dp_01`, `cbnv_dp_02`, DN `0209888006` (dựng tiền đề + kiểm thông báo) · `admin` **chỉ để điều tra**, không ra verdict. Mật khẩu `Test@1234`. CNKQHT_07: `qa_tvvseed28` + `nht_ag_uat2` (người bấm cập nhật) · `cbnv_tw_01`, `cbnv_tw_02`, `cbnv_dp_01` (người kỳ vọng nhận — mở `/thong-baos` bằng chính tài khoản mình) · DN `0209888006` và `0109998887` (dựng tiền đề) · `admin` **chỉ để tra định danh**, không ra verdict. DGKQHTVV_01: `cbnv_tw_01` (ra verdict nhánh cán bộ) · DN `0209888006` và DN `0109998887` (ra verdict nhánh doanh nghiệp) · `cbpd_tw_01`, `cbnv_dp_01`, `cbpd_dp_01`, `cbnv_hn` **chỉ dựng tiền đề**, không ra verdict · **không dùng `admin`**. Không tài khoản nào phải đổi sang tài khoản thay thế |
| Xác thực | JWT + OTP qua email |
| Tool test | Chrome DevTools MCP · bộ bắt thông báo `output/UAT_doi-tac/tools/toast-capture.js` (tự kiểm `soObserverDangSong = 1` trước mỗi lần bấm) |

---

*Bug report generated: 2026-08-06 17:10:00 | QA via Claude Code*
