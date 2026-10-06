Mã case: VVDTN_04 (tab `bug` dòng 178)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (chân sidebar `HTPLDN · V1.0.8`;
gói `assets/index-CNwX9JjX.js`) — đo 06/08/2026 12:51–13:12

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có. Đợt này chưa từng qua vòng soát nội bộ,
không có bug entry cũ, không có khối CÁCH VERIFY. Chỉ đọc: dòng 178 tab `bug`, bằng chứng đối tác,
SRS v3.5 `srs-fr-11-bao-cao.md`.

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc đã tiếp nhận** (SCR-IX-01, `loai=vu-viec-tiep-nhan`). Tách 2 vế:

- **Vế (a)** — "Không hiển thị **biểu đồ tròn** theo lĩnh vực".
- **Vế (b)** — "Bảng tổng hợp **thiếu các cột: Theo kênh, Theo lĩnh vực**".

**Bằng chứng đã mở xem:**

| Tệp | Vòng | Đã xem tới | Thấy gì |
|---|---|---|---|
| `../partner-evidence/VVDTN_04.webm` (frame `../frames/VVDTN_04/t008.04s.jpg`) | Vòng 1 — 15/07/2026 16:31 | khoảnh khắc cuộn tới vùng biểu đồ | Bản dựng **V1.0**, vai trò **Quản trị viên QTHT** (BTP·TW). Có **1 biểu đồ cột** 2 mốc `Trực tiếp` (~27) / `Điện thoại` (~1) = theo **kênh tiếp nhận**; dưới là **1 biểu đồ đường** 1 điểm mốc `2026-01-01` (~28). **Không** thấy biểu đồ/vùng nào theo **lĩnh vực**. Không thấy vùng bảng dữ liệu trong frame đã trích. |
| `../partner-evidence/VVDTN_04_v2.jpg` | Vòng 2 — 31/07/2026 14:07 | ảnh tĩnh full-res | Bản dựng **V1.0.2**, vẫn vai trò **QTHT**. Ảnh chụp đúng vùng biểu đồ: cột theo kênh (`Trực tiếp` / `Điện thoại`) + đường theo thời gian. Vẫn **không** có vùng theo lĩnh vực. |

**Lệch giữa 2 vòng:** cùng vai trò (QTHT), cùng bộ lọc (Kỳ Năm 01/01/2026–31/12/2026, đơn vị
`00000000-0000-4000-8000-000000000001` = Cục Bổ trợ tư pháp – BTP·TW), **khác bản dựng** (V1.0 → V1.0.2).
Triệu chứng vòng 2 **thu hẹp** so với vòng 1: TKM 31/7 chỉ còn nhắc vế (a), không nhắc lại vế (b).
Vẫn đo **cả 2 vế** vì bảng chưa đóng vế (b).

---

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (SRS v3.5 — nguồn duy nhất).

**Về DỮ LIỆU phải trình bày** — FR-IX-02 (UC125), bảng "Output đặc thù":

- `:214` → `| 2 | theo_kenh[] | structured | Luôn | {kenh, so_luong} |`
- `:215` → `| 3 | theo_linh_vuc[] | structured | Luôn | {linh_vuc, ten, so_luong} |`
- `:216` → `| 4 | theo_don_vi[] | structured | Luôn | {don_vi, ten, so_luong} |`
- `:217` → `| 5 | theo_ky[] | structured | Luôn | {ky, so_luong} |`
- `:213` → `| 1 | tong_vu_viec | number | Luôn | Tổng số VV tiếp nhận |`

Điều kiện của cả 5 dòng là **"Luôn"** ⇒ đây là bảng liệt kê **đóng** một tập giá trị bắt buộc, KHÔNG phải
đặc tả im lặng.

- `:220` (AC bổ sung) → `**Given** CB chọn kỳ Tháng **When** tạo BC **Then** hiển thị tổng VV tiếp nhận, phân theo kênh + lĩnh vực`
- `:205` (Dimensions) → `Kỳ, Đơn vị, Kênh tiếp nhận, Lĩnh vực PL`

**Về DẠNG BIỂU ĐỒ** — SCR-IX-01 "Mapping 23 loại BC trong Dropdown":

- `:1065` → `| **Vụ việc** | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | **Bar + Trend** |`
- Đối chiếu: `:1064` UC124 = `Donut + Trend`, `:1067` UC127 = `Bar + Donut`. ⇒ đặc tả **có** khái niệm
  Donut và **cố ý** không gán Donut cho UC125.
- `:1054` (thành phần màn hình #10 Biểu đồ) → `Tùy loại BC: Line (trend) / Bar / Stacked bar / Donut / Radar. Toggle hiện/ẩn` · điều kiện hiển thị `Khi có dữ liệu`
- `:1055` (#11 Bảng dữ liệu) → `Nhóm theo chiều phân tích tùy loại BC. Cột sắp xếp. Sticky header. Hàng tổng cộng (bold)` · điều kiện hiển thị `Khi có dữ liệu`

**Tác nhân** — `:192` → `**Tác nhân:** CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`. Cột "Tác nhân" của chính
dòng 178 trên bảng cũng ghi CB Nghiệp vụ / CB Phê duyệt. **QTHT không nằm trong tác nhân của FR-IX-02.**

**IM LẶNG về:**
- Vùng theo lĩnh vực phải là **biểu đồ** hay **cột trong bảng** — `:215` chỉ đòi dữ liệu `theo_linh_vuc[]`,
  `:1055` chỉ nói bảng "nhóm theo chiều phân tích tùy loại BC", không liệt kê tên cột cụ thể.
- Số lượng biểu đồ tối đa trên màn.
- Vai trò QTHT được thấy gì trên màn báo cáo.

---

## 3. Precondition

- Tài khoản: **`cbnv_tw` / `Test@1234`** (CB Nghiệp vụ Trung ương, `CB_NV_TW`) — đúng tác nhân `:192`,
  cùng cấp TW như đối tác. Đối chứng GAP vai trò: **`admin` / `Secret@123`** (QTHT) — đúng vai trò
  đối tác đã dùng.
- Màn: `https://18.143.165.120.nip.io/bao-cao` → Loại báo cáo **"BC Vụ việc đã tiếp nhận"**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Cục Bổ trợ tư pháp – Bộ Tư pháp
  (BTP-TW)**.
- Dữ liệu tiền đề: ≥1 vụ việc đã tiếp nhận trong khoảng, thuộc **≥2 kênh tiếp nhận khác nhau** và
  **≥2 lĩnh vực PL khác nhau** (xem mục 5). Chưa đủ thì seed thêm vụ việc qua luồng chuẩn.

---

## 4. Tiêu chí chấm

### Vế (b) — dữ liệu theo kênh + theo lĩnh vực (đặc tả NÓI RÕ, chấm được)

✅ **PASS khi ĐỦ cả 4:**
1. Sau khi bấm "Xem báo cáo" với bộ lọc ở mục 3, màn trình bày được số vụ việc **phân rã theo kênh
   tiếp nhận** — đọc ra được tên từng kênh kèm số lượng, ở bất kỳ dạng nào (bảng hoặc biểu đồ).
2. Màn trình bày được số vụ việc **phân rã theo lĩnh vực PL** — đọc ra được tên từng lĩnh vực kèm số
   lượng, ở bất kỳ dạng nào (bảng hoặc biểu đồ).
3. Tổng các giá trị của phân rã theo kênh **bằng** `tong_vu_viec` hiển thị trên màn; tổng phân rã theo
   lĩnh vực **bằng** `tong_vu_viec`. (Ba chiều không cộng khớp tổng ⇒ số đang sai, chưa được dùng.)
4. Phủ đủ M dạng ở mục 5 — mỗi kênh và mỗi lĩnh vực có dữ liệu đều xuất hiện đúng 1 lần, không trùng,
   không thiếu.

❌ **FAIL nếu bất kỳ:** không có chỗ nào trên màn đọc được phân rã theo kênh · không có chỗ nào đọc được
phân rã theo lĩnh vực · phân rã có nhưng tổng không khớp `tong_vu_viec` · có kênh/lĩnh vực trong M có dữ
liệu thật nhưng bị bỏ khỏi phân rã.

⛔ **KHÔNG được chấm Fail vì:**
- Phân rã theo lĩnh vực nằm trong **bảng** thay vì **biểu đồ** (hoặc ngược lại) — `:215` chỉ đòi dữ liệu,
  không chốt dạng trình bày.
- Tên cột trên bảng không đúng chữ "Theo kênh" / "Theo lĩnh vực" — đặc tả không quy định nhãn cột.
- Thiếu chiều `theo_don_vi[]` / `theo_ky[]` — hai chiều này đối tác **không nêu**; nếu thiếu thì xử theo
  §"Phát hiện mới", không kéo verdict case này.

### Vế (a) — biểu đồ TRÒN theo lĩnh vực

→ **cần BA vì kỳ vọng đối tác NGƯỢC với đặc tả nói rõ.** Đối tác đòi **biểu đồ tròn**; `:1065` chốt
UC125 = **Bar + Trend**, trong khi cùng bảng đó `:1064` / `:1067` có gán Donut cho UC khác ⇒ không phải
sót, mà là chọn có chủ đích. **QA không tự bác đối tác** — vẫn đo và chụp hiện trạng (dạng biểu đồ thực
tế đang render), không chấm Pass/Fail vế này.

**Điều kiện bỏ vế (a) khỏi danh sách hỏi BA:** nếu đo thấy màn **đã có** biểu đồ tròn theo lĩnh vực (bản
dựng làm đúng như đối tác mong đợi) ⇒ hết bất đồng, không hỏi BA nữa, chỉ ghi nhận hiện trạng.

---

## 5. Dạng dữ liệu phải phủ

**M = (số kênh tiếp nhận có dữ liệu) + (số lĩnh vực PL có dữ liệu)**, tối thiểu **2 + 2 = 4**.

- Kênh tiếp nhận — tập đóng 5 giá trị, nguồn `srs-fr-11-bao-cao.md:200`:
  `DVC` · `HE_THONG_KHAC` · `TRUC_TIEP` · `BUU_CHINH` · `DIEN_THOAI`.
  Bằng chứng đối tác đã cho thấy ≥2 kênh có dữ liệu (`Trực tiếp`, `Điện thoại`) ⇒ ngưỡng ≥2 là đạt được.
- Lĩnh vực PL — không phải tập đóng trong SRS (`:201` chỉ ghi `FK → DANH_MUC`); **nguồn xác định M** =
  đọc dropdown "Lĩnh vực PL" ngay trên màn SCR-IX-01 + đếm lĩnh vực thực có vụ việc trong khoảng bằng
  đường thứ hai (gọi thẳng API danh sách vụ việc). Ghi con số thực đo được vào báo cáo.

Đây là bug về **trường/chiều hiển thị dữ liệu** ⇒ cấm để `M = 1`. Nếu môi trường chỉ có 1 kênh hoặc 1
lĩnh vực có dữ liệu → **seed thêm** vụ việc qua luồng chuẩn cho đủ ≥2/≥2, và khai rõ đã seed gì ở báo cáo.

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên QTHT** (`BTP · TW`) — đọc từ góc phải màn cả 2 ảnh. KHÔNG thuộc tác nhân FR-IX-02 (`:192`) | Đo **cả 2 vai trò trên chính giao diện**: ① `cbnv_tw` (`CB_NV_TW`, TW) — đúng tác nhân `:192`; ② `admin` (**QTHT**, trùng khít đối tác) — đăng nhập UI, mở đúng bộ lọc đối tác, `Tổng vụ việc = 34`, `Thời điểm tạo 06/08/2026 13:36`. **Nhìn tận mắt màn QTHT render**: đủ bảng "Kênh tiếp nhận" (Trực tiếp 34) + bảng "Thống kê theo lĩnh vực pháp luật" (Dân sự 13 · Lao động 9 · Thương mại 9 · Thuế 3 = 34), biểu đồ là **cột + đường**, **không có biểu đồ tròn**. Ảnh `../bug-reports/image/VVDTN_04-04-QTHT-bieu-do-cot-va-duong-khong-co-tron.png`, `../bug-reports/image/VVDTN_04-05-QTHT-bang-kenh-va-bang-linh-vuc.png` | **Không** — GAP đóng bằng **quan sát thật trên vai trò đối tác**, không phải suy luận |
| Entity + trạng thái | VU_VIEC đã tiếp nhận, chỉ bản ghi đã duyệt (TPL bước 4, `:82`). Tổng trên màn đối tác = 27 (15/07) và 27 (31/07) | 45 vụ việc trong kỳ; trừ 1 `TU_CHOI` → **44**, khớp công thức `:203` "trừ từ chối". Đo bằng đường thứ hai `GET /api/v1/vu-viecs` (đếm thô, không lọc/gộp) | **Không** — khác số lượng (44 vs 27) không đổi bản chất câu hỏi "màn có/không có chiều phân rã" |
| Dữ liệu tiền đề | ≥2 kênh có dữ liệu (`Trực tiếp` ~27, `Điện thoại` ~1). Số lĩnh vực có dữ liệu: **không đọc được từ bằng chứng** | **2 kênh** (`TRUC_TIEP` 41 · `DOANH_NGHIEP` 3) + **4 lĩnh vực** (Thương mại 16 · Dân sự 13 · Lao động 12 · Thuế 3) — đếm độc lập từ danh sách vụ việc, khớp từng con số với báo cáo | **Không** — vượt ngưỡng ≥2 kênh / ≥2 lĩnh vực của mục 5, không phải seed thêm |
| Input / filter / giá trị nhập | Kỳ `NAM`, `tuNgay=2026-01-01`, `denNgay=2026-12-31`, `donViId=00000000-0000-4000-8000-000000000001` (BTP-TW). Kênh tiếp nhận + Lĩnh vực PL đều để trống | Đo **2 bộ lọc**: ① đúng bộ lọc đối tác (BTP-TW → tổng **34**); ② nới lên Toàn quốc (tổng **44**) để có ≥2 kênh. Kỳ/khoảng/2 ô lọc đặc thù giữ y hệt đối tác | **Không** — cả 2 bộ lọc đều hiện đủ 2 chiều kênh + lĩnh vực |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 27 vụ việc · M quan sát được = 2 kênh + ? lĩnh vực | N = 44 · **M = 2 kênh + 4 lĩnh vực = 6** (mục 5 đòi ≥4). Mỗi kênh và mỗi lĩnh vực có dữ liệu xuất hiện **đúng 1 lần**, không trùng không thiếu — đối chiếu 2 đường độc lập | **Không** — M thực đo vượt ngưỡng |

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict (không bị giới hạn "chỉ ô trống").

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001`
- Trạng thái entity: BC dạng tổng hợp, `Thời điểm tạo` = 15/07/2026 16:39 (vòng 1) và 31/07/2026 14:06 (vòng 2); `Tổng vụ việc` = 27 ở cả hai vòng
- Vai trò + env + bản dựng: **QTHT** · `htpldn-uat.ospgroup.vn` · **HTPLDN V1.0** (vòng 1) → **V1.0.2** (vòng 2)

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` bản V1.0/V1.0.2; đợt này
đo trên `18.143.165.120.nip.io` bản ghi ở đầu file. Verdict chỉ có hiệu lực cho env + bản dựng đã ghi;
Pass ở đây là **Pass tạm** cho tới khi bản dựng này lên env đối tác.
