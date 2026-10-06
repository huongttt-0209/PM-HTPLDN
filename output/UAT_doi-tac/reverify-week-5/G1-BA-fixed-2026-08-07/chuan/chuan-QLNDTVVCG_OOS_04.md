# Chuẩn đối chiếu — Cụm B: `QLNDTVVCG_OOS_04` (dòng 362) — nhật ký thao tác kèm lý do từ chối

> **File này KHÔNG chứa verdict.** Chỉ là chuẩn để agent đo đối chiếu.
>
> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> — file chính `srs-fr-12-tv-chuyen-sau.md` (**1.681 dòng**, mtime 06/08/2026 22:52), phụ trợ `srs-v3.5.md`.
> **Mọi số dòng do chính lượt này mở file đọc lại 2026-08-07.**

---

## 🔴 CẢNH BÁO SỐ 1 — SỐ DÒNG 198 ĐÃ LỆCH, DÒNG THẬT LÀ **204**

Sheet (dòng 362, ô *Kết quả mong đợi*) và phiếu BA mục 6 đều quote `srs-fr-12-tv-chuyen-sau.md:198`.
**Đọc lại file hôm nay: dòng 198 là dòng kẻ tiêu đề bảng, không phải bước 6.** File đã được sửa 06/08 để áp
kết luận BA nên nội dung trôi xuống **+6 dòng**.

| Nội dung | Sheet / phiếu BA ghi | **Dòng THẬT (2026-08-07)** |
|---|---|---|
| Bước 6 *"Ghi nhật ký thao tác (kèm lý do từ chối)"* — khối **CG từ chối** | `:198` | **`:204`** |
| Bước 5 *"Gửi thông báo CB NV…"* — khối **CG từ chối** | `:197` | **`:203`** |
| Bước 3 *"Yêu cầu lý do từ chối (bắt buộc)"* | `:195` | **`:201`** |
| Khuôn khối Nhật ký thao tác (SCR-X1-02 thành phần 8) | `:1160` | **`:1173`** (`:1160` nay là dòng Layout tổng quan) |
| Bảng chuyển trạng thái — CG từ chối | `:1521` | **`:1548`** |

Quote sai bản = chuẩn vô giá trị. **Dùng cột phải.**

---

## 🔴 CẢNH BÁO SỐ 2 — LÝ DO **KHÔNG** HIỆN VỚI TÀI KHOẢN CHUYÊN GIA. ĐO BẰNG CG = FAIL OAN

Brief mô tả luồng Pass là *"CG bấm [Từ chối nhiệm vụ] + nhập lý do → **mở lại chi tiết** → khối Nhật ký thao
tác"* — **không nói mở lại bằng vai trò nào**. Đặc tả nói rõ là **phải bằng vai trò nội bộ**, và **CG cố ý
không được thấy lý do**:

> `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1173` (SCR-X1-02, thành phần 8) — *"| 8 | content | Accordion: Nhật ký
> thao tác | timeline | Lịch sử chuyển trạng thái + CUD. Khuôn dòng: \"dd/mm/yyyy HH:mm -- {User} -- {Hành
> động}\". **Riêng hành động Từ chối (CG từ chối nhận việc · CB PD từ chối phê duyệt) và Hủy yêu cầu: thêm dòng
> phụ \"Lý do: {nội dung}\"** — chỉ hiện phần lý do, KHÔNG mở các trường khác của bản chụp hồ sơ `[BA chốt
> 2026-08-06]`. **Dòng phụ Lý do chỉ hiện với vai trò nội bộ** (CB NV, CB PD, NHT theo phạm vi đơn vị);
> **KHÔNG** hiện với người trong mạng lưới tư vấn — họ vẫn xem được phần còn lại của khối nhật ký như trước.
> Nhãn hành động lấy từ bảng action-level `TU_VAN_CHUYEN_SAU` (`srs-v3.5.md` §3.4.2) — thao tác Từ chối phải
> có nhãn riêng, không gộp vào \"Cập nhật\" | — | mode chi tiết |"*

Hai tiêu chí chấp nhận viết tách bạch **hai vai trò, hai kỳ vọng ngược nhau**:

> `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:347` — *"- **Given** CB NV mở hồ sơ đã có lượt từ chối **When** xem khối
> Nhật ký thao tác **Then** thấy dòng hành động \"Từ chối\" kèm dòng phụ \"Lý do: …\" `[BA chốt 2026-08-06]`"*
>
> `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:348` — *"- **Given** CG mở chính hồ sơ đó **When** xem khối Nhật ký thao
> tác **Then** thấy đủ các dòng nhật ký nhưng **không** thấy dòng phụ \"Lý do\" `[BA chốt 2026-08-06]`"*

⇒ **Đo bằng `qa_tvvseed28` (CG) rồi chấm Reopen vì "không thấy lý do" là FAIL OAN — và là đúng cái bẫy đặc
tả cố ý dựng.** Vế "hiện lý do" **bắt buộc** đo bằng **`cbnv_tw_04`** (hoặc CB NV/CB PD/NHT cùng đơn vị).

---

## 🔴 CẢNH BÁO SỐ 3 — SAU KHI TỪ CHỐI, CG BỊ ĐƯA VỀ MÀN DANH SÁCH

CG **không ở lại được** màn chi tiết sau khi bấm Từ chối — nên bước *"mở lại chi tiết"* của brief, nếu làm
bằng CG, sẽ là một lần điều hướng ngược:

> `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1189` — *"| CG bấm **[Từ chối]** | **HẾT** — bước 4 Processing xóa
> `chuyen_gia_id`; hồ sơ trả về hàng chờ của CB NV, CG không còn phần việc nào trên đó | **Quay về màn danh
> sách** + toast |"*
>
> `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1196` — *"- **Câu chữ thông báo sau khi CG từ chối:** **\"Đã từ chối yêu
> cầu tư vấn\"** `[BA chốt 2026-08-06]` — bám vốn từ của entity (`ma_tu_van` = *\"Mã yêu cầu TV\"*, `noi_dung`
> = *\"Nội dung yêu cầu TV\"*)"*

⚠️ Hai điểm này (điều hướng + câu chữ toast) là **nội dung của phiếu `QLNDTVVCG_26`, không phải phiếu này**.
Gặp lệch thì **ghi nhận**, không kéo verdict `OOS_04`.

---

## 0. Điều kiện phải dựng lại

| Hạng mục | Yêu cầu | Căn cứ |
|---|---|---|
| **Vai trò 1 — dựng tiền đề** | `cbnv_tw_04` (`CB_NV_TW`, `Test@1234`) — tạo bản ghi TVCS + phân công CG | `srs-fr-12:176` bước 1 *"Kiểm tra quyền CB NV và phạm vi đơn vị"*; `srs-v3.5.md:1440` `TVCS_ASSIGN` = `CB_NV_{cap}` |
| **Vai trò 2 — người bấm Từ chối** | `qa_tvvseed28` (`Test@1234`) — Tư vấn viên + Chuyên gia tư vấn, `loai_tvv = CG`, **Cục Bổ trợ tư pháp – BTP, cấp TW** | `srs-v3.5.md:1442` `TVCS_REJECT` = CG, scope `record.chuyen_gia_id = current_user` AND `trang_thai = PHAN_CONG` AND có lý do. Tài khoản: `output/UAT_doi-tac/input/input.md:78-80` |
| **Vai trò 3 — người ĐỌC nhật ký để ra verdict** | 🔴 **`cbnv_tw_04`** (hoặc CB NV/CB PD/NHT cùng đơn vị) — **KHÔNG dùng `qa_tvvseed28`** | `:1173` + `:347` + `:348` (cảnh báo 2) |
| **State entity cần có** | ≥1 bản ghi `TU_VAN_CHUYEN_SAU` ở trạng thái **`PHAN_CONG`** (giao diện hiện *"Phân công"*), `chuyen_gia_id` = `qa_tvvseed28` | `srs-fr-12:200` — *"| 2 | Kiểm tra trạng thái hiện tại = PHAN_CONG | SM-TVCS |"* |
| **Đơn vị** | Bản ghi phải thuộc **cùng đơn vị** với CB NV đọc nhật ký (BTP·TW) | `:1173` — *"NHT theo phạm vi đơn vị"*; BR-AUTH-08 `srs-v3.5.md:5529` |
| **Lý do từ chối** | Chuỗi có **dấu nhận dạng riêng** (vd `QA G1 OOS_04 - ly do tu choi 20260807 <giờ>`), ghi lại **nguyên văn** trước khi bấm | Để phân biệt với 2 lượt từ chối cũ ngày 06/08 còn tồn trong nhật ký |
| **Bản dựng + môi trường** | `https://18.143.165.120.nip.io`; ghi nhãn bản dựng; tải lại trang bằng địa chỉ trước khi verify | Luật chung lô §3 |

🔴 **Hai bản ghi lượt 06/08 đã DÙNG HẾT, không tái sử dụng được:** `TVCS-20260806-0002` và `TVCS-20260803-0003`
đều đã bị từ chối, nay ở `TIEP_NHAN` với `chuyenGiaId = null`. Muốn dùng lại thì **phải phân công lại**
(đưa về `PHAN_CONG`), hoặc tạo bản ghi mới.

---

## 1. Đặc tả đối chiếu — nguyên văn, số dòng đọc lại 2026-08-07

### 1.1 Dòng quyết định

| Dòng | Nguyên văn |
|---|---|
| 🔴 `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:204` | *"| 6 | Ghi nhật ký thao tác (kèm lý do từ chối) — **lý do hiển thị trên khối Nhật ký thao tác của hồ sơ** (SCR-X1-02 thành phần 8), nhãn hành động là \"Từ chối\" (không gộp vào \"Cập nhật\") `[BA chốt 2026-08-06]` | BR-DATA-05 |"* |
| 🔴 `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1173` | (trích đủ ở cảnh báo 2) |
| 🔴 `srs-v3.5/srs-v3.5.md:1442` | *"| TVCS_REJECT | **Từ chối nhận việc** (nhãn hiển thị trên Nhật ký thao tác: \"Từ chối\", KHÔNG gộp vào \"Cập nhật\") | CG | `record.chuyen_gia_id = current_user` AND `record.trang_thai = PHAN_CONG` AND có lý do từ chối | FR-X.1-01 |"* |
| `srs-v3.5/srs-fr-12-tv-chuyen-sau.md:347` · `:348` | (trích đủ ở cảnh báo 2) |

⇒ **Bảng action-level `TU_VAN_CHUYEN_SAU` mà `:1173` viện dẫn là CÓ THẬT** — nằm ở
`srs-v3.5/srs-v3.5.md:1428–1448`, tiêu đề `:1428` *"**TU_VAN_CHUYEN_SAU — Action-level permissions**
`[BA chốt 2026-08-06 — UAT tuần 5]`"*. Nhãn *"Từ chối"* lấy từ đó (`:1442`).

### 1.2 Dòng nền — luồng CG từ chối (khối *Processing — CG từ chối*, `:195–204`)

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-12:195` | *"**Processing — CG từ chối** (PHAN_CONG → TIEP_NHAN) `[GAP-X.1-01]`"* |
| `srs-fr-12:199` | *"| 1 | Kiểm tra user là CG được phân công cho bản ghi này | BR-AUTH-01 |"* |
| `srs-fr-12:200` | *"| 2 | Kiểm tra trạng thái hiện tại = PHAN_CONG | SM-TVCS |"* |
| `srs-fr-12:201` | *"| 3 | Yêu cầu lý do từ chối (bắt buộc) | — |"* |
| `srs-fr-12:202` | *"| 4 | Xóa liên kết chuyen_gia_id, trạng thái → TIEP_NHAN | — |"* |
| `srs-fr-12:203` | *"| 5 | Gửi thông báo CB NV (in-app + email): CG từ chối, cần phân công lại — **nội dung thông báo phải đính kèm lý do từ chối** `[BA chốt 2026-08-06]` | BR-NOTIF-01 |"* |
| `srs-fr-12:1548` | *"| PHAN_CONG | TIEP_NHAN | CG từ chối | Có lý do | TB CB NV kèm lý do từ chối (in-app + email); quay lại chọn CG khác | FR-X.1-01 | BR-NOTIF-01 |"* |

### 1.3 Dòng nền — ràng buộc phân công (dựng tiền đề)

| Dòng | Nguyên văn (rút gọn) |
|---|---|
| `srs-fr-12:168` | *"> **Chỉ Chuyên gia được nhận việc tư vấn chuyên sâu** `[BA chốt 2026-08-06]`. … nội dung tư vấn chuyên sâu **chỉ giao cho loại `CG`**."* |
| `srs-fr-12:177` | *"| 2 | Kiểm tra trạng thái hiện tại = TIEP_NHAN | SM-TVCS |"* |
| `srs-fr-12:178` | *"| 3 | Kiểm tra CG được chọn: phải **loại Chuyên gia (`loai_tvv = 'CG'`)**, đang hoạt động, chuyên môn phù hợp lĩnh vực `[BA chốt 2026-08-06]` | — |"* |
| `srs-fr-12:1169` | *"… Chuyên gia (dropdown searchable WHERE `trang_thai` hoạt động AND `loai_tvv = 'CG'`; **khoá ở chế độ thêm mới** — hồ sơ luôn vào trạng thái Tiếp nhận với ô này trống; việc gán người tư vấn chỉ thực hiện qua nút [Phân công CG] …"* |
| `srs-fr-12:1175` | *"| 9 | action-bar | Thanh hành động cố định | … TIEP_NHAN: [Hủy] [Lưu] [Phân công CG ->] / **PHAN_CONG: [Hủy yêu cầu] + (CG được phân công: [Chấp nhận] [Từ chối])** …"* |
| `srs-fr-12:1180` | *"- Phân công CG (gộp từ MH-12.4): modal overlay với gợi ý TOP 5 CG (lĩnh vực khớp, điểm TB DESC, workload ASC) + tìm kiếm CG thủ công + ghi chú + info SLA (2 ngày LV xác nhận)"* |

⚠️ Lưu ý dựng: `:1169` nói ô Chuyên gia bị **khoá ở chế độ thêm mới** — hồ sơ mới **luôn** vào `TIEP_NHAN`
với ô Chuyên gia trống. Việc gán **chỉ** làm được qua nút **[Phân công CG]**. Đừng cố gán ngay lúc tạo.

---

## 2. Luồng dựng lại tiền đề — công thức đầy đủ

### 2.1 Đường giao diện (đường chính, khuyến nghị)

```
B1. Đăng nhập cbnv_tw_04 / Test@1234  (mã xác thực ở MailHog http://18.143.165.120:8025)
B2. Menu Tư vấn → Tư vấn pháp luật chuyên sâu  (SCR-X1-01)
B3. [+ Thêm yêu cầu TV] → nhập DN + Lĩnh vực PL + Tiêu đề + Nội dung TV + Ngày tư vấn → Lưu
    ⇒ bản ghi mới ở TIEP_NHAN, ô Chuyên gia trống (:1169)
    GHI LẠI mã bản ghi TVCS-{YYYYMMDD}-{SEQ}
B4. Mở chi tiết bản ghi → [Phân công CG] → chọn qa_tvvseed28 → xác nhận
    ⇒ trạng thái PHAN_CONG, ô Chuyên gia = "QA TVV Seed28 Active"   (:178, :1180)
B5. Đăng xuất. Đăng nhập qa_tvvseed28 / Test@1234
B6. Mở chi tiết CHÍNH bản ghi đó → thanh hành động hiện [Chấp nhận] [Từ chối]   (:1175)
B7. GHI LẠI mốc giờ + chuỗi lý do đã soạn → bấm [Từ chối] → nhập lý do → xác nhận
    ⇒ kỳ vọng: toast + quay về màn danh sách (:1189, :1196 — ngoài phạm vi phiếu này)
    ⇒ bản ghi về TIEP_NHAN, Chuyên gia = "Chưa phân công"   (:202)
B8. 🔴 Đăng xuất. Đăng nhập LẠI cbnv_tw_04  ← BƯỚC KHÔNG ĐƯỢC BỎ
B9. Mở chi tiết bản ghi → bung Accordion "Nhật ký thao tác" → đọc dòng MỚI NHẤT
```

**Nếu muốn tiết kiệm bước B3:** phân công lại một trong hai bản ghi lượt 06/08 (`TVCS-20260806-0002` /
`TVCS-20260803-0003`) — cả hai đang ở `TIEP_NHAN`, thuộc DN *"Cong ty TNHH QA UAT Kiem Thu"*, đơn vị BTP·TW.
Chỉ cần B4 → B9. Nhưng khi đó nhật ký sẽ có **nhiều lượt từ chối chồng nhau** → bắt buộc phân biệt bằng
**mốc giờ + chuỗi lý do có dấu nhận dạng riêng**.

### 2.2 Đường đối chứng độc lập (đúng 1 đường, khác đường giao diện)

Lượt 06/08 đã dùng: `GET /api/v1/noi-dung-tu-van-cs/{id}/audit-logs` — trả bản ghi nhật ký của chính hồ sơ đó.
Kết quả lượt 06/08: **18 trường** (loại thực thể, mã thực thể, hành động, người thực hiện, thời gian, IP, điểm
gọi, mã phản hồi, phiên, phân hệ, họ tên, vai trò, đơn vị…), **không** có trường mang lý do; giá trị hành động
là `UPDATE`.

⇒ Phép đối chứng lần này: gọi lại chính đường đó, xem (a) có **trường mang lý do** chưa, (b) giá trị **hành
động** đã tách khỏi `UPDATE` chưa. **CẤM tự đoán đường dẫn khác** — cần thì bắt lời gọi thật của màn chi tiết
hoặc tra `/api/docs-json`.

⚠️ Hai đường mâu thuẫn (màn hiện lý do nhưng dữ liệu không có trường lý do, hoặc ngược lại) ⇒ **ghi cả hai**,
không tự chọn một bên.

---

## 3. Chuẩn chấm — 2 vế, thiếu 1 là không đạt

Phiếu BA mục 6 chốt: yêu cầu *"ghi nhật ký kèm lý do từ chối"* là **ĐẠT — không phải lỗi**; phần đang đo là
**cải tiến đã duyệt** gồm **2 việc dev**:

| Vế | Nội dung | Căn cứ | Đạt khi |
|---|---|---|---|
| **B-1 — Nhãn thao tác** | Dòng nhật ký của lượt từ chối mang **nhãn riêng "Từ chối"**, không gộp vào "Cập nhật" | `:204` + `srs-v3.5.md:1442` | Dòng mới nhất (khớp mốc giờ B7) hiện nhãn hành động riêng cho việc từ chối. Vẫn là "Cập nhật" / `UPDATE` → **không đạt** |
| **B-2 — Lý do có kiểm soát** | Dòng đó có **dòng phụ "Lý do: {nội dung}"**, đúng chuỗi đã nhập ở B7 | `:204` + `:1173` + `:347` | Đọc bằng **cbnv_tw_04** thấy đủ chuỗi lý do. Không thấy → **không đạt** |

**Ba ràng buộc phụ của B-2, kiểm luôn trong cùng lượt:**

1. **Chỉ hiện phần lý do, KHÔNG mở các trường khác của bản chụp hồ sơ** (`:1173`). Nếu khối nhật ký bung ra
   toàn bộ trường của bản ghi thì đó là **làm quá**, đúng điều dev cảnh báo và BA chặn → ghi nhận rõ.
2. **Khuôn dòng gốc giữ nguyên** — *"dd/mm/yyyy HH:mm -- {User} -- {Hành động}"* (`:1173`); các hành động
   **khác** Từ chối/Hủy **không** được mọc thêm dòng phụ.
3. **Vai trò mạng lưới tư vấn không thấy dòng phụ** (`:348`). Đo bổ sung bằng `qa_tvvseed28`: thấy đủ các dòng
   nhật ký nhưng **không** thấy dòng "Lý do". Nếu CG **thấy** lý do → đó là lệch đặc tả theo chiều ngược,
   ghi nhận (đây là ràng buộc bảo mật BA đặt ra, không phải điều đối tác đòi).

---

## 4. Bẫy chấm sai

### 4.1 Bẫy **FAIL oan / Reopen oan**

1. 🔴 **Đọc nhật ký bằng chính tài khoản `qa_tvvseed28`.** Đặc tả **cố ý** ẩn dòng lý do với vai trò mạng lưới
   tư vấn (`:348`, `:1173`). Đây là bẫy số 1 của case này.
2. 🔴 **Đọc bản ghi CŨ ngày 06/08 rồi chấm.** Lý do được ghi lúc từ chối; bản ghi từ chối **trước** khi dev sửa
   đã đóng băng dữ liệu ở dạng cũ → dòng cũ không có lý do là **bình thường**. Phép thử quyết định **phải là
   một lượt từ chối MỚI** chạy hôm nay.
3. **Chấm Fail vì thông báo gửi CB NV không kèm lý do.** Đó là `:203`, thuộc phiếu `QLNDTVVCG_26`, không phải
   phiếu này.
4. **Chấm Fail vì không tự quay về danh sách / toast sai câu chữ.** `:1189`, `:1196` — thuộc `QLNDTVVCG_26`.
5. **Chấm Fail vì nhãn không đúng từng chữ "Từ chối".** SRS đòi **nhãn riêng, tách khỏi "Cập nhật"**
   (`:204`, `:1442`). Nhãn "Từ chối nhiệm vụ" / "Từ chối yêu cầu tư vấn" vẫn thoả — chấm theo **có tách nhãn
   hay không**, không theo từng chữ.
6. **Chấm Fail vì bảng dữ liệu của hồ sơ không có cột lý do.** Đặc tả **cố ý** không tạo cột — phiếu BA mục 6
   dẫn tiền lệ đã chốt cho thao tác hủy. Lý do sống ở nhật ký, đúng thiết kế.
7. **Chấm Fail vì tab mở lâu.** Tải lại trang bằng địa chỉ, ghi nhãn bản dựng trước khi verify.

### 4.2 Bẫy **PASS oan**

1. 🔴 **Thấy nhãn "Từ chối" là Pass.** Đó mới là B-1. B-2 (dòng phụ Lý do, đúng chuỗi đã nhập) chưa đo.
2. 🔴 **Thấy chữ "Lý do" mà không đối chiếu nội dung.** Phải so **đúng chuỗi có dấu nhận dạng riêng** đã ghi ở
   B7 — nếu không sẽ nhầm với lý do của lượt 06/08 còn tồn trong nhật ký.
3. **Nhầm nguồn lý do.** Lượt 06/08 đã chứng minh lý do **có** xuất hiện trong **nội dung thông báo** gửi CB NV
   (*"Lý do: QA FLOW04 QLNDTVVCG_26 - ly do tu choi ban ghi B luc 20260806"*). Thấy lý do ở **màn Thông báo**
   ≠ thấy ở **khối Nhật ký thao tác của hồ sơ**. Phải đọc đúng khối `Accordion: Nhật ký thao tác` trên
   **SCR-X1-02**.
4. **Không kiểm ràng buộc "chỉ hiện phần lý do".** Bung hết trường bản chụp cũng "có lý do" nhưng trái `:1173`.
5. **Dùng `admin` để đọc nhật ký.** Không phải vai trò đặc tả nêu (`:1173` liệt kê CB NV, CB PD, NHT) và quyền
   rộng che lỗi phạm vi → verdict vô hiệu.

---

## 5. Danh sách CHƯA XÁC MINH ĐƯỢC — agent đo phải tự xác nhận trên màn

| # | Điểm | Vì sao chưa xác minh được từ file | Phải làm gì |
|---|---|---|---|
| B-1 | Nhãn tiếng Việt thật của thao tác từ chối trên nhật ký | SRS chỉ đòi *"nhãn riêng, không gộp vào Cập nhật"* (`:204`, `:1442`); không chốt chuỗi | Chụp dòng nhật ký, ghi nguyên văn nhãn; chấm theo **có tách nhãn**, không theo chữ |
| B-2 | Khuôn hiển thị dòng phụ Lý do (xuống dòng / cùng dòng / tooltip) | `:1173` chỉ ghi *"thêm dòng phụ \"Lý do: {nội dung}\""*, không đặc tả cách trình bày | Chấm theo **đọc được đủ nội dung lý do**, không theo cách trình bày |
| B-3 | Nhãn nút trên thanh hành động: "Từ chối" (`:1175`) hay "Từ chối nhiệm vụ" (chữ trong sheet) | Hai nguồn ghi khác nhau; SRS `:1175` ghi **[Từ chối]** | Ghi lại nhãn nút thật; không chấm verdict theo nhãn nút |
| B-4 | Có bản ghi TVCS nào **sẵn** ở `PHAN_CONG` gán cho `qa_tvvseed28` không | Hai bản ghi lượt 06/08 đã bị tiêu thụ (về `TIEP_NHAN`, `chuyenGiaId = null`) | Quét danh sách TVCS bằng `cbnv_tw_04` trước; không có thì dựng theo §2.1 |
| B-5 | Đường dẫn thật của lời gọi đọc nhật ký ở bản dựng hôm nay | Lượt 06/08 dùng `/api/v1/noi-dung-tu-van-cs/{id}/audit-logs`; SRS không đặc tả đường dẫn | Bắt lời gọi thật khi bung khối nhật ký, hoặc tra `/api/docs-json`. **Không đoán** |
| B-6 | `qa_tvvseed28` còn `loai_tvv = CG` và còn hoạt động không | `input.md:78-80` ghi là CG nhưng cũng ghi *"Nếu cần loại TVV thuần … đổi lại loại"* — trạng thái có thể đã bị đổi | Kiểm ngay ở bước B4: nếu tài khoản **không hiện trong dropdown Phân công CG** thì đó là do `loai_tvv`/trạng thái, **không phải bug của case này** |
