# Audit — PDHSVV_03 (row 8) · CB Phê duyệt khác đơn vị bấm Phê duyệt — "thông báo lặp (duplicate) + sai wording"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/PDHSVV_03.jpg` (`fetch_evidence.py --row 8`). Ảnh: CB_PD_TW mở vụ việc VV-BKH-20260526-001 (đơn vị BKH, "Chờ phê duyệt"), sau khi bấm Phê duyệt hiện **2 thông báo xếp chồng** cùng nội dung "Đơn vị của người phê duyệt khác đơn vị của bản ghi".
- Frame chứa LỖI đối tác báo: 2 khung thông báo giống hệt nhau (duplicate) + nội dung thông báo (wording) khác đặc tả.

### 3 dữ kiện neo (từ evidence + cột sheet)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB phê duyệt **khác đơn vị** với đơn vị tạo/quản lý vụ việc; vụ việc ở **"Chờ phê duyệt"** |
| (b) | Hiện tượng đối tác báo (cột "Kết quả thực tế") | (1) **thông báo hiển thị lặp** (2 khung); (2) **nội dung thông báo sai** so với đặc tả |
| (c) | Kỳ vọng đối tác (cột "Kết quả mong đợi") | Chặn phê duyệt chéo đơn vị + hiển thị **đúng 1 thông báo** với nội dung theo đặc tả |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh PDHSVV_03 — CB PD khác đơn vị bấm Phê duyệt vụ việc "Chờ phê duyệt", hệ thống chặn nhưng hiện 2 thông báo trùng nội dung, và nội dung thông báo dùng từ kỹ thuật.
2. **Đối tác phản ánh CỤ THỂ:** 2 ý — (1) thông báo lặp; (2) sai wording.
3. **Data + bước tái hiện:** dựng vụ việc địa phương ở "Chờ phê duyệt" → login CB PD khác đơn vị (`cbpd_tw` TW vs vụ việc An Giang) → bấm [Phê duyệt] → đo số khung thông báo + số request (bộ bắt thông báo) + đọc nội dung.

## Bảng đối chiếu điều kiện

→ [`../../cond/PDHSVV_03.md`](../../cond/PDHSVV_03.md) — **0 GAP** về role/state/data. Đã dựng đúng tiền đề (vụ việc An Giang → CHO_PHE_DUYET) và test đúng vai trò đối tác (CB PD khác đơn vị).

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

### Ý (1) — Thông báo lặp (duplicate)

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-13 §Error Handling E2 | Khi CB PD không cùng cấp → chặn, hiển thị **1** thông báo lỗi (mã ERR-PD-02) | `srs-fr-05-vu-viec.md:1002` |

→ Kết quả test trên env được giao: **KHÔNG tái hiện lặp**. Đo bằng `tools/toast-capture.js` (tự kiểm `soObserverDangSong = 1`, KHÔNG lọc trùng, đọc `innerText`, đếm request) qua **3 lần** bấm Phê duyệt — mỗi lần **1 request** `POST /api/v1/vu-viecs/{id}/phe-duyet` (403) và **đúng 1 khung thông báo** (`SO_KHUNG = 1`, `BI_LAP = false`); network log CDP (`list_network_requests`) chỉ 1 POST /phe-duyet [403]; ảnh chụp chỉ có 1 thông báo. → **Không log bug cho ý này** (không tái hiện — tránh false bug theo quy tắc 3-step verify).

### Ý (2) — Sai wording

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-13 §Error Handling E2 (ERR-PD-02 "CB PD không cùng cấp") | Message hiển thị phải là **"Bạn không có quyền phê duyệt vụ việc này"** | `srs-fr-05-vu-viec.md:1002` |

→ Kết quả test: thông báo hiển thị **"Đơn vị của người phê duyệt khác đơn vị của bản ghi"** — (a) khác nội dung SRS quy định; (b) lộ từ kỹ thuật **"bản ghi"** (record CSDL) ra giao diện người dùng cuối. ❌ **Vi phạm** — cùng loại lộ thuật ngữ kỹ thuật/nội bộ với BUG-VV-MALOI-LO-UI (lẫn mã lỗi) và BUG-PDHSVV_02 (lộ UUID). → Log **BUG-PDHSVV_03** (Minor).

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Tiền đề (seed): VV-STP-AG-20260712-003 (id `23892656-...`, đơn vị Sở Tư pháp An Giang, gốc DANG_XU_LY). `nht_ag_uat2` (người xử lý cùng đơn vị) cập nhật kết quả (`cap-nhat-ket-qua` → 201) → `trinh-phe-duyet` (201) → **CHO_PHE_DUYET**. Không đổi vai trò/đơn vị người phê duyệt.
- `cbpd_tw` (CB_PD_TW, BTP·TW — **khác đơn vị** với An Giang) mở chi tiết → bấm [Phê duyệt] → hộp thoại xác nhận → [Phê duyệt].
- **Ý (1):** 3 lần bấm — mỗi lần 1 request POST /phe-duyet (403) + 1 khung thông báo, không lặp. Ảnh: `BUG-PDHSVV_03-toast-1-sai-wording.png` (đúng 1 thông báo).
- **Ý (2):** nội dung thông báo = "Đơn vị của người phê duyệt khác đơn vị của bản ghi" (observer bắt được 3/3 lần, giống nhau). SRS (:1002) quy định "Bạn không có quyền phê duyệt vụ việc này".

## Verdict

**`Open`** — Case có **lỗi thật** ở ý (2) wording: thông báo chặn phê duyệt chéo đơn vị hiển thị sai nội dung so với đặc tả + lộ từ kỹ thuật "bản ghi" (vi phạm FR-V.I-13 E2 ERR-PD-02 :1002). Đã log **BUG-PDHSVV_03** (Minor). Ý (1) "thông báo lặp" **không tái hiện** trên env được giao (chỉ 1 request + 1 thông báo, đo bằng observer đã tự kiểm) → không log bug cho ý này. Verdict tổng của case = Open (do ≥1 ý là lỗi thật — ý wording).
