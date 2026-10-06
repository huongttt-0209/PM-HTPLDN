# BA confirmation needed — Lô B6 · Vụ việc HTPL — 2026-08-06

> **⚠️ File này là bản ghi gốc của lô, KHÔNG phải bản gửi BA.**
> Bản gửi BA là [`cau-hoi-BA-tong-hop-2026-08-06.md`](../../reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md) — cả 8 mục → **Mục 6–13**.

> Gom các điểm QA **không tự chốt được** vì đặc tả im lặng. Bug có căn cứ đặc tả rõ đã log ở
> [`bug-report.md`](bug-report.md) — không lặp ở đây.
>
> **Môi trường + bản dựng đã đo:** `https://18.143.165.120.nip.io` (env nội bộ) ·
> `HTPLDN · V1.0.8` · bó mã FE `assets/index-CNwX9JjX.js` · `GET /` `last-modified 06/08/2026 09:51:16` giờ VN.
>
> **Nguồn quote số dòng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

---

## KTHSYCHTPL_11 (phát sinh khi verify, đối tác KHÔNG nêu) — nhãn lựa chọn kết luận "Đạt — chuyển sang phân công" hứa một việc mà hệ thống cố ý không làm

**Bối cảnh**

- Dòng Excel: **45**, tab `bug`, mã TC `KTHSYCHTPL_11`. Verdict của case này là **Pass** — mục hỏi BA dưới
  đây **không** làm đổi verdict đó, nêu riêng vì đặc tả im lặng.
- Màn: chi tiết vụ việc → phiếu **"Kiểm tra hồ sơ"** → ô **Kết luận**.
- Điểm phát sinh: ô Kết luận có 3 lựa chọn, lựa chọn đầu tiên hiển thị nguyên văn
  **"Đạt — chuyển sang phân công"**.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, Chrome DevTools MCP, tài khoản `cbnv_dp_01` (vai trò **CB_NV_DP**, cấp Địa phương).
- Ô Kết luận có đúng 3 lựa chọn: **"Đạt — chuyển sang phân công"** · "Không đạt — từ chối hồ sơ" ·
  "Yêu cầu bổ sung".
- Chọn "Đạt" rồi Xác nhận → hệ thống **giữ nguyên** trạng thái **"Đang kiểm tra"** (đúng đặc tả), và thông
  báo hiện lên lại ghi **"Kiểm tra hồ sơ đạt — sẵn sàng phân công"** — tức **thông báo nói đúng**, chỉ có
  **nhãn trong ô chọn** là nói "chuyển sang phân công".
- Vụ việc chỉ sang "Đã phân công" sau khi cán bộ bấm [Phân công], chọn người xử lý và xác nhận.
- Bằng chứng: `image/KTHSYCHTPL_11-02-phieu-kiem-tra-6-hang-muc-3-lua-chon-ket-luan.png` (ô Kết luận bung
  ra đủ 3 lựa chọn) · `image/KTHSYCHTPL_11-03-ngay-sau-luu-Dat-badge-van-Dang-kiem-tra.png` (ngay sau khi
  lưu Đạt, badge vẫn "Đang kiểm tra").

**Điểm đặc tả im lặng**

- `srs-fr-05-vu-viec.md:522` chỉ quy định **giá trị** của trường kết luận (`DAT` / `KHONG_DAT` /
  `YEU_CAU_BO_SUNG`), **không** quy định chữ hiển thị của từng lựa chọn trên màn.
- `srs-fr-05-vu-viec.md:541`, `:564`, `:2288` quy định rõ **hành vi**: kết luận Đạt làm vụ việc *sẵn sàng
  phân công* nhưng **vẫn giữ** "Đang kiểm tra"; chỉ chuyển "Đã phân công" khi đã chọn người/tổ chức xử lý.
- Hệ thống **làm đúng hành vi**, nhưng **nhãn lựa chọn** lại mô tả một việc khác với việc nó làm. Đặc tả
  không có dòng nào chốt chữ cho nhãn này ⇒ QA không tự kết luận đúng/sai được.

**Vì sao đáng hỏi**

Đây đúng là điều đối tác đã hiểu nhầm: kỳ vọng ghi trong phiếu UAT của `KTHSYCHTPL_11` là *"Hệ thống chuyển
trạng thái hồ sơ: Đang kiểm tra → Đã phân công"*. BA đã chốt ngày **2026-07-16** rằng kỳ vọng đó không đúng
(`srs-fr-05-vu-viec.md:22`). Nhưng nhãn trên màn hiện vẫn đang **nói y như kỳ vọng đã bị bác**, nên người
dùng tiếp theo rất dễ hiểu nhầm lại và mở phiếu lỗi lặp lại.

**Câu hỏi cần BA xác nhận**

1. Nhãn lựa chọn kết luận Đạt **có cần đổi chữ** cho khớp hành vi đã chốt hay không? Nếu có, BA chốt giúp
   chữ chuẩn (gợi ý theo đúng ngôn ngữ đặc tả `:541` và đúng chữ thông báo hệ thống đang dùng:
   **"Đạt — sẵn sàng phân công"**).
2. Nếu BA giữ nguyên nhãn hiện tại, xin xác nhận để QA ghi thành **quy ước đã chốt** và các vòng UAT sau
   không mở lại phiếu ở điểm này.

**Đề xuất QA tạm thời**

- Chưa có trả lời của BA: QA **không** log thành lỗi (đặc tả im lặng về chữ nhãn), giữ verdict
  `KTHSYCHTPL_11` = **Pass**.
- Nếu BA chốt **đổi nhãn** → mở 1 dòng lỗi mới mức **Minor**, owner **Dev FE**, chỉ sửa chữ hiển thị,
  không đụng hành vi.
- Nếu BA chốt **giữ nhãn** → ghi vào tiêu chí case như một mục "không được chấm Fail vì", đóng lại vĩnh viễn.

---

## TKHSYCHTPL_03 — Mã của mức "Sắp hết hạn": `SAP_HET` hay `SAP_HET_HAN`? *(đặc tả tự mâu thuẫn)*

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case này là **Pass** — mục hỏi BA dưới
  đây **không** làm đổi verdict đó.
- Nội dung kiểm tra: cán bộ nghiệp vụ (`CB_NV_TW`) đặt ô lọc **"Mức SLA" = "Sắp hết hạn"** trên màn
  **Vụ việc HTPL / Danh sách** (`SCR-V.I-01`) rồi bấm [Tìm kiếm].
- Điểm phát sinh: cùng **một** mức cảnh báo đang được đặt **hai mã khác nhau** ở hai chỗ trong bộ đặc tả.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, Chrome DevTools MCP, tài khoản `cbnv_tw_01` (vai trò **CB_NV_TW**, cấp TW),
  môi trường `https://18.143.165.120.nip.io`, bản dựng `HTPLDN · V1.0.8`.
- Ô lọc bung ra **đúng 4 lựa chọn**; chọn "Sắp hết hạn" → giao diện gửi lên **`mucSla=SAP_HET`**, máy chủ
  trả **HTTP 200** và **2 bản ghi**, không có thông báo lỗi nào.
- Gọi thẳng máy chủ bằng mã còn lại: `mucSla=SAP_HET_HAN` → **HTTP 422**, `ERR-VAL-SYS-00-01`, nội dung
  *"mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG"*.
  ⇒ Máy chủ hiện chỉ chấp nhận `SAP_HET`.
- Bằng chứng: `image/TKHSYCHTPL_03-01-dropdown-Muc-SLA-4-lua-chon.png` ·
  `image/TKHSYCHTPL_03-03-Sap-het-han-lan1-ra-2-ket-qua-khong-loi.png` ·
  `image/TKHSYCHTPL_03-04-Sap-het-han-cot-Canh-bao-thoi-han-dung-muc.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Nhóm **Vụ việc** ghi mã là **`SAP_HET`**:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1644` — ô lọc "Mức SLA":
     `BINH_THUONG / SAP_HET / QUA_HAN / QUA_HAN_NGHIEM_TRONG`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2031` — ràng buộc thực thể:
     `CHECK IN ('BINH_THUONG','SAP_HET','QUA_HAN','QUA_HAN_NGHIEM_TRONG')`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1516` — bảng ánh xạ:
     `` `SAP_HET` | Sắp hết hạn | Vàng ``

2. Nhóm **Báo cáo**, nhóm **Hỏi đáp** và **bản ghi quyết định của BA** lại ghi **`SAP_HET_HAN`**:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:245` — tham số `muc_sla`:
     `BINH_THUONG / SAP_HET_HAN / QUA_HAN / QUA_HAN_NGHIEM_TRONG`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:979` — bảng mức cảnh báo:
     `SAP_HET_HAN | <= 50% còn lại | Vàng | Thông báo CB NV`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1043` và `:1107` — cột
     và nhãn cảnh báo thời hạn, cùng dùng `SAP_HET_HAN`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md:1317` — mục sửa đổi
     **BR-SLA-02**, ghi rõ **cite BA 2026-05-04**: bốn mức mang mã
     `BINH_THUONG/SAP_HET_HAN/QUA_HAN/QUA_HAN_NGHIEM_TRONG`

**Câu hỏi cần BA xác nhận**

Mức cảnh báo **"Sắp hết hạn"** phải mang mã chuẩn nào trên toàn hệ thống?

1. **Hướng 1 — `SAP_HET`** (theo nhóm Vụ việc): giữ nguyên hiện trạng của màn Vụ việc; phải rà lại nhóm
   Báo cáo và nhóm Hỏi đáp cùng bản ghi quyết định BR-SLA-02 cho khớp.
2. **Hướng 2 — `SAP_HET_HAN`** (theo BR-SLA-02 bản BA chốt 2026-05-04, nhóm Báo cáo và nhóm Hỏi đáp):
   phải sửa nhóm Vụ việc (cả ô lọc, ràng buộc thực thể lẫn dữ liệu đang lưu).

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: dù BA chọn mã nào, cả hai bản đặc tả
  đều đòi ô lọc phải **trả danh sách theo mức đã chọn**, và **cả hai** bảng Error Handling của màn này
  (`srs-fr-05-vu-viec.md:149` và `:692-693`) đều **không có** mục lỗi nào cho giá trị mức SLA. Hiện trạng
  đã đáp ứng yêu cầu nghiệp vụ đó ⇒ giữ **Pass**.
- QA **không tự đề xuất đổi mã**: đổi theo hướng 1 thì bộ lọc bên Báo cáo và Hỏi đáp lệch theo, đổi theo
  hướng 2 thì phải chuyển đổi dữ liệu đang lưu của Vụ việc. Đây là quyết định phạm vi hệ thống, thuộc BA.
- Sau khi BA chốt: nếu chọn hướng 2 thì mở phiếu riêng cho việc đồng bộ mã + chuyển đổi dữ liệu, owner
  `Dev BE`; nếu chọn hướng 1 thì mở phiếu sửa đặc tả, owner `BA`.

---

## TKHSYCHTPL_03 (phát sinh khi verify, đối tác KHÔNG nêu) — bộ lọc chỉ chạy khi bấm [Tìm kiếm], trong khi đặc tả ghi "change → filter"

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case là **Pass** — mục này **không**
  làm đổi verdict.
- Màn: **Vụ việc HTPL / Danh sách** (`SCR-V.I-01`), thanh bộ lọc.
- Điểm phát sinh: hai hàng **trong cùng một bảng thành phần màn hình** mô tả hai cách kích hoạt lọc khác nhau.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, tài khoản `cbnv_tw_01`, bản dựng `HTPLDN · V1.0.8`.
- Chọn xong một mức trong ô "Mức SLA" mà **chưa** bấm [Tìm kiếm]: đếm được **0** yêu cầu danh sách gửi đi,
  bảng vẫn giữ nguyên 52 bản ghi chưa lọc. Đo lại bằng **hai cách thao tác khác nhau** (chuột và bàn phím)
  đều cho cùng kết quả.
- Chỉ khi bấm **[Tìm kiếm]** thì mới có **đúng 1** yêu cầu `GET /api/v1/vu-viecs?mucSla=…` và bảng mới đổi.
- Bằng chứng: `image/TKHSYCHTPL_03-02-da-chon-Sap-het-han-truoc-khi-bam-Tim-kiem.png` (đã chọn mức, bảng
  chưa đổi) · `image/TKHSYCHTPL_03-09-lan2-sau-tai-lai-da-chon-Sap-het-han-bang-ban-phim.png` (chọn bằng
  bàn phím, bảng vẫn chưa đổi) · `image/TKHSYCHTPL_03-03-Sap-het-han-lan1-ra-2-ket-qua-khong-loi.png`
  (sau khi bấm [Tìm kiếm] thì bảng đổi).

**Điểm mâu thuẫn trong SRS v3.5**

1. `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1644` (hàng 9) đặt hành vi
   của ô "Mức SLA" là **`change → filter`** — tức đổi giá trị là lọc ngay. Bảy hàng khác của cùng thanh lọc
   (`:1639` → `:1645`) cũng ghi `change → filter`.
2. Nhưng `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1646` (hàng 11) lại
   liệt kê một thành phần riêng — **"Nút Tìm kiếm / Xóa bộ lọc"** — với hành vi **`click → query / reset`**,
   điều kiện hiển thị **"Luôn"**. Nếu mọi ô đã lọc ngay khi đổi giá trị thì nút này không còn việc gì làm.

**Câu hỏi cần BA xác nhận**

Trên thanh lọc của `SCR-V.I-01`, đổi giá trị một ô lọc thì danh sách phải **lọc ngay**, hay phải **chờ cán
bộ bấm [Tìm kiếm]**?

1. **Hướng 1 — lọc ngay khi đổi giá trị** (theo hàng 9): hiện trạng đang **thiếu** hành vi này; nút
   [Tìm kiếm] chỉ còn vai trò chạy lại.
2. **Hướng 2 — chờ bấm [Tìm kiếm]** (theo hàng 11): hiện trạng **đúng**; cần sửa cột "Hành vi" của các hàng
   ô lọc trong đặc tả cho khớp, tránh vòng UAT sau lại mở phiếu ở điểm này.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: đối tác không nêu vế này, và chính đối
  tác cũng thao tác theo hướng 2 (chọn mức rồi bấm [Tìm kiếm]) nên phép đo của case không bị ảnh hưởng.
- Nếu BA chọn hướng 1 → mở 1 phiếu mức **Medium**, owner `Dev FE`.
- Nếu BA chọn hướng 2 → cập nhật cột "Hành vi" của các hàng ô lọc trong `SCR-V.I-01`, owner `BA`.

---

## TKHSYCHTPL_03 (phát sinh khi verify, đối tác KHÔNG nêu) — hồ sơ chưa có thời hạn xử lý vẫn lọt bộ lọc "Bình thường" và hiện dấu "—"

**Bối cảnh testcase**

- Dòng Excel: **50**, tab `bug`, mã TC `TKHSYCHTPL_03`. Verdict của case là **Pass** — mục này **không**
  làm đổi verdict.
- Màn: **Vụ việc HTPL / Danh sách**, cột **"Cảnh báo thời hạn"** và ô lọc **"Mức SLA"**.

**Kết quả verify UI hiện tại**

- Verify ngày **06/08/2026**, tài khoản `cbnv_tw_01`, bản dựng `HTPLDN · V1.0.8`.
- Lọc "Mức SLA" = **"Bình thường"** trả **38** bản ghi. Trong đó **2** bản ghi —
  `VV-BTP-TW-20260731-002` và `VV-BTP-TW-20260712-002` — đều ở trạng thái **Mới tạo**, **chưa có ngày tiếp
  nhận** nên **chưa có thời hạn xử lý**, và cột "Cảnh báo thời hạn" hiện dấu **"—"** thay vì một trong bốn nhãn.
- Đọc lại từ máy chủ: hai bản ghi này mang `mucDoCanhBao = BINH_THUONG` (đúng **giá trị mặc định** của
  trường theo đặc tả), `deadline = null`, `ngayTiepNhan = null` ⇒ giao diện và máy chủ **khớp nhau**, việc
  chúng lọt bộ lọc "Bình thường" là **nhất quán với dữ liệu đang lưu**, không phải lỗi hiển thị.
- Bằng chứng: `image/TKHSYCHTPL_03-05-Binh-thuong-trang1-20-dong-tren-38.png` ·
  `image/TKHSYCHTPL_03-06-Binh-thuong-trang2-18-dong-21-38.png`

**Điểm đặc tả im lặng**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2031` để trường mức cảnh báo
  ở cột "Bắt buộc" = **`N`** và đặt **mặc định `'BINH_THUONG'`** ⇒ đặc tả **cho phép** bản ghi chưa được tính
  mức, và tự động gán nó vào nhóm "Bình thường".
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1436` cho biết công việc tự
  động **chỉ quét vụ việc đang hoạt động** (`DA_TIEP_NHAN`, `DANG_KIEM_TRA`, `DA_PHAN_CONG`, `DANG_XU_LY`,
  `CHO_PHE_DUYET`) ⇒ hồ sơ **Mới tạo** không nằm trong diện được tính mức.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1656` mô tả cột này chỉ có
  **4 mức**, không nói hồ sơ chưa tính được mức thì hiện gì và thuộc nhóm lọc nào.
- ⇒ Đặc tả **không có dòng nào** chốt: hồ sơ chưa có thời hạn xử lý thì (i) hiện gì ở cột cảnh báo và
  (ii) có được coi là "Bình thường" khi lọc hay không.

**Câu hỏi cần BA xác nhận**

Hồ sơ **chưa có thời hạn xử lý** (chưa tiếp nhận) phải được đối xử thế nào trên màn danh sách?

1. **Coi là "Bình thường"** — giữ nguyên hiện trạng: lọt bộ lọc "Bình thường", cột cảnh báo hiện "—".
2. **Đứng ngoài 4 mức** — không lọt bất kỳ mức nào của bộ lọc "Mức SLA"; cột cảnh báo vẫn hiện "—".

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `TKHSYCHTPL_03`: đặc tả im lặng, và tiêu chí chấm của
  case đã chốt trước khi đo là không lấy điểm này để chấm Fail.
- Nếu BA chọn hướng 2 → mở 1 phiếu mức **Minor**, owner `Dev BE` (loại hồ sơ chưa có thời hạn khỏi bộ lọc mức).
- Nếu BA chọn hướng 1 → ghi thành quy ước đã chốt để các vòng UAT sau không mở lại phiếu ở điểm này.

---

## CNKQHT_07 — Chữ trên thông báo sau khi cập nhật kết quả: "Đã cập nhật kết quả" hay "Đã cập nhật kết quả hỗ trợ"?

> Đo trên bản dựng `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` ·
> `GET /` `last-modified 06/08/2026 14:13:15` giờ VN.

**Hiện trạng đo được**

- Sau khi người được phân công bấm **[Cập nhật kết quả]**, thông báo trên màn hiện đúng **1 khung · 1 mốc giờ**,
  nguyên văn: **"Đã cập nhật kết quả"**. Lặp lại giống hệt ở cả 4 lần bấm, trên 3 hồ sơ khác nhau.
- Ô "Kết quả mong đợi" của phiếu UAT ghi **"Đã cập nhật kết quả hỗ trợ"** — lệch 1 chữ so với thực tế.
- Bằng chứng: `image/cnkqht07-04-d1-nhom6-sau-cap-nhat-15h45.png` ·
  `image/cnkqht07-15-d1b-form-khong-tep-khong-ghichu-truoc-khi-bam.png`

**Điểm đặc tả im lặng**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1100-1114` (FR-V.I-15 §Processing
  và §Postconditions) **không có dòng nào** quy định chữ hiển thị trên màn sau khi lưu kết quả.
- Bảng "Thông báo riêng SCR-V.I-03" (`srs-fr-05-vu-viec.md:1773-1785`) **không có dòng** cho thao tác
  "Cập nhật kết quả hỗ trợ"; dòng gần nhất (`:1782`) thuộc FR-V.I-16 — một chức năng khác.
- ⇒ Không có căn cứ đặc tả để chấm chữ hiện tại là đúng hay sai.

**Câu hỏi cần BA xác nhận**

Chữ trên thông báo sau khi cập nhật kết quả hỗ trợ nên chốt theo hướng nào?

1. **Giữ nguyên "Đã cập nhật kết quả"** — coi ô Kết quả mong đợi của phiếu UAT là diễn đạt tự do, không phải yêu cầu.
2. **Đổi thành "Đã cập nhật kết quả hỗ trợ"** cho khớp phiếu UAT và khớp tên hộp thoại "Cập nhật kết quả hỗ trợ".

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `CNKQHT_07`: đối tác chỉ phản ánh vế thông báo cho cán bộ
  nghiệp vụ; chữ trên màn thuộc vế đối tác không nêu, và đặc tả im lặng.
- Nếu BA chọn hướng 2 → mở 1 phiếu mức **Trivial**, owner `Dev FE` (sửa chuỗi hiển thị).
- Nếu BA chọn hướng 1 → ghi thành quy ước để các vòng UAT sau không mở lại phiếu ở điểm này.

---

## CNKQHT_07 (phát sinh khi verify, đối tác KHÔNG nêu) — cập nhật kết quả lần sau mà không đính tệp thì tệp của lần trước còn hay mất?

> Cùng bản dựng và cùng phép đo với mục trên.

**Hiện trạng đo được**

- Vụ việc `VV-BTP-TW-20260806-003` được cập nhật kết quả **2 lần**: lần đầu có đính 1 tệp, lần sau chỉ nhập nội dung
  và **không** đính tệp nào.
- Sau lần sau, Nhóm 6 hiện **nội dung mới** nhưng **vẫn giữ tệp của lần đầu**. Không có thông báo nào cho người
  thao tác biết tệp cũ được giữ lại.
- Bằng chứng: `image/cnkqht07-16-d1b-nhom6-sau-cap-nhat-khong-tep-16h06.png`

**Điểm đặc tả im lặng**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1094-1096` chỉ ghi tệp kết quả là
  đầu vào **tùy chọn**, không nói lần cập nhật sau mà bỏ trống thì tệp cũ bị thay, bị xóa hay được giữ.
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1104-1105` (bước "Tạo/cập nhật
  KET_QUA_VU_VIEC" và "Lưu tài liệu kết quả") cũng không mô tả nhánh "không có tệp mới".
- ⇒ Đặc tả không chốt hành vi giữ/thay/xóa tệp khi cập nhật nhiều lần.

**Câu hỏi cần BA xác nhận**

Khi người được phân công cập nhật kết quả lần thứ hai trở đi mà không đính tệp mới, hệ thống nên:

1. **Giữ nguyên tệp cũ** — như hiện trạng.
2. **Bỏ tệp cũ** để hồ sơ luôn khớp đúng lần cập nhật mới nhất.
3. **Giữ cả hai** dưới dạng danh sách nhiều tệp có mốc thời gian.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `CNKQHT_07`: đây là vế "lưu nội dung, tệp và ghi chú" mà đối tác
  không nêu, và đặc tả im lặng.
- Nếu BA chọn hướng 2 hoặc 3 → mở 1 phiếu mức **Minor**, owner `Dev BE` + `Dev FE`.
- Nếu BA chọn hướng 1 → ghi thành quy ước đã chốt.

---

## DGKQHTVV_01 — Vụ việc đã ở "Đã đánh giá" thì bên còn lại có được vào đánh giá không? *(đặc tả tự mâu thuẫn)*

> Bản dựng đã đo cho case này: `HTPLDN · V1.0.8` · bó mã FE `assets/index-DIABnbIr.js` ·
> `GET /` `last-modified 06/08/2026 14:13:15` giờ VN (**khác bó mã ghi ở đầu file** — có triển khai mới xen
> giữa lô).

**Bối cảnh**

- Dòng Excel: **64**, tab `bug`, mã TC `DGKQHTVV_01`. Verdict của case là **Reopen** vì nhánh doanh nghiệp
  không có đường vào chức năng đánh giá — mục hỏi BA dưới đây **không** làm đổi verdict đó, và cũng
  **không** phải căn cứ của verdict.
- Chức năng: đánh giá kết quả hỗ trợ vụ việc (Nhóm 8 trên màn chi tiết vụ việc), `FR-V.I-17 / UC67`.
- Đặc tả cho phép **hai loại người đánh giá độc lập nhau** — cán bộ nghiệp vụ và doanh nghiệp — mỗi loại
  chấm đúng 1 lần cho 1 vụ việc. Lần chấm đầu tiên đẩy vụ việc sang **"Đã đánh giá"**. Vậy **bên còn lại**
  vào chấm khi vụ việc **đang ở "Đã đánh giá"** thì có được không?

**Đặc tả nói lệch nhau ở 2 chỗ**

| Dòng | Nguyên văn | Hàm ý |
|---|---|---|
| `srs-fr-05-vu-viec.md:1197` | "\| PRE-02 \| VV ở trạng thái HOAN_THANH hoặc **DA_DANH_GIA** \|" | **Được** |
| `srs-fr-05-vu-viec.md:1734` | "\| 11 \| content \| Accordion 8 — Đánh giá… \| CB NV/DN nhập trực tiếp \| **Khi VV ở HOAN_THANH hoặc DA_DANH_GIA** \|" | **Được** |
| `srs-fr-05-vu-viec.md:1811` | "\| Thanh thao tác \| …**[Đánh giá]** (khi trạng thái = \"Hoàn thành\" / **\"Đã đánh giá\"** + chưa đánh giá)… \|" | **Được** |
| `srs-fr-05-vu-viec.md:1740-1754` (bảng nút hành động **chế độ cán bộ**) | Chỉ có **một** dòng cho chức năng đánh giá — `:1751` *"\| HOAN_THANH \| [Đánh giá] (gộp MH-05.9) \| CB NV/DN \| Mở Accordion 8. Gửi → DA_DANH_GIA \|"*; **không có** dòng nào cho trạng thái `DA_DANH_GIA` | **Không được** |

**Hiện trạng đo được**

- Trên bản dựng đang đo, vụ việc `VV-QA-008` đang mang nhãn **"Đã đánh giá"** nhưng **không kèm bản ghi
  đánh giá nào**; cán bộ nghiệp vụ mở chi tiết ra thì **không thấy đường vào đánh giá**, Nhóm 8 vẫn ở
  trạng thái rỗng ⇒ hệ thống đang chạy theo hướng **`:1751`** (chỉ mở ở "Hoàn thành").
- **Chưa dựng được** đúng tình huống "một bên chấm trước, bên còn lại vào chấm": muốn có nó phải có đánh
  giá của phía doanh nghiệp, mà phía doanh nghiệp đang bị chặn hoàn toàn (đã log ở
  [`bug-report.md`](bug-report.md) — `BUG-VV-DGKQHTVV-01`).
- Bằng chứng: `image/DGKQHTVV_01-10-D3-VV-QA-008-trang-thai-Da-danh-gia-khong-co-nut-Danh-gia.png`

**Câu hỏi cần BA xác nhận**

Khi vụ việc **đã ở "Đã đánh giá"** vì một loại người đánh giá đã chấm, loại còn lại vào chấm thì:

1. **Vẫn được chấm** — theo `:1197` / `:1734` / `:1811`; khi đó `:1751` thiếu một dòng cho trạng thái
   "Đã đánh giá" và cần bổ sung.
2. **Không được chấm** — theo `:1751`; khi đó `:1197`, `:1734`, `:1811` cần bỏ trạng thái "Đã đánh giá",
   và hệ quả là **mỗi vụ việc trên thực tế chỉ nhận được 1 đánh giá**, trái với ràng buộc dữ liệu
   `:2108` / `:2116` (mỗi vụ việc tối đa 1 đánh giá của cán bộ nghiệp vụ **và** 1 của doanh nghiệp).

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `DGKQHTVV_01`: đây là điểm đặc tả tự mâu thuẫn, không
  phải sai lệch so với một yêu cầu đã chốt.
- Nếu BA chọn hướng 1 → mở 1 phiếu mức **Major**, owner `Dev BE` + `Dev FE`, và ghép luôn vào lần fix
  `BUG-VV-DGKQHTVV-01` (cùng vùng chức năng).
- Nếu BA chọn hướng 2 → cần chốt lại luôn ý nghĩa của ràng buộc "tối đa 2 đánh giá / vụ việc", vì hướng 2
  làm ràng buộc đó không bao giờ dùng tới.

---

## DGKQHTVV_01 — Đánh giá vụ việc xong thì điểm trung bình của tư vấn viên có phải cập nhật không? *(đặc tả tự mâu thuẫn)*

> Cùng bản dựng và cùng đợt đo với mục trên.

**Bối cảnh**

- Cùng chức năng `FR-V.I-17 / UC67`. Điểm phát sinh khi đọc đặc tả để dựng thước đo, **không** phải do
  đối tác phản ánh.
- Mục *Postconditions* và bảng *Processing* của cùng một use case nói ngược nhau về việc điểm trung bình
  của tư vấn viên có được cập nhật sau khi đánh giá vụ việc hay không.

**Đặc tả nói lệch nhau ở 2 chỗ**

| Dòng | Nguyên văn | Hàm ý |
|---|---|---|
| `srs-fr-05-vu-viec.md:1233` (Postconditions) | "- Điểm TVV được cập nhật" | Đánh giá vụ việc **có** làm đổi điểm tư vấn viên |
| `srs-fr-05-vu-viec.md:1223` (Processing bước 9) | "…nguồn dữ liệu là DANH_GIA_SAU_VU_VIEC (đối tượng do FR-IV quản lý), **không phải** DANH_GIA_VU_VIEC. **UC67 chỉ tạo DANH_GIA_VU_VIEC; trigger cập nhật điểm TVV nằm ở module FR-IV**" | Đánh giá vụ việc **không** làm đổi điểm tư vấn viên |

**Hiện trạng đo được**

- QA **cố ý không chấm** điểm này trong vòng verify: hai dòng đặc tả ngược nhau nên không có thước đo
  hợp lệ. Đã ghi thẳng vào thước đo của case là **cấm chấm Fail** vì "điểm tư vấn viên không đổi".
- Vòng này đã tạo **2 bản ghi đánh giá** hợp lệ (`VV-BTP-TW-20260806-003` và `-004`, cùng bộ điểm
  9 · 8 · 10) — dữ liệu sẵn sàng để đo lại ngay khi BA chốt hướng.

**Câu hỏi cần BA xác nhận**

Sau khi đánh giá kết quả hỗ trợ **một vụ việc**, điểm trung bình của tư vấn viên phụ trách:

1. **Phải cập nhật ngay** — khi đó `:1223` cần bỏ câu "UC67 chỉ tạo DANH_GIA_VU_VIEC", và cần chốt luôn
   công thức lấy từ nguồn nào.
2. **Không cập nhật** — điểm tư vấn viên chỉ do đợt đánh giá của nhóm chức năng khác quyết định; khi đó
   `:1233` cần bỏ dòng "Điểm TVV được cập nhật".

**Đề xuất QA tạm thời**

- **Không** log thành lỗi và **không** đổi verdict `DGKQHTVV_01`.
- BA chốt xong → bổ sung đúng **một** tiêu chí đo được vào thước đo của chức năng này cho các vòng sau
  (hiện đang bỏ trống có chủ ý).
