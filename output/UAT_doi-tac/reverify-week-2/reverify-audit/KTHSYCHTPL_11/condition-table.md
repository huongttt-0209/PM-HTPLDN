# KTHSYCHTPL_11 — Bảng đối chiếu điều kiện

**Case:** Nút "Hoàn tất kiểm tra" khi chọn kết luận Đạt (SCR-V.I-03 · FR-V.I-06 UC56).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_11.jpg` — VV-QA-R7-SLA-QHNT, trạng thái **"Đang kiểm tra"**, tài khoản **CB NV DP 01 (AG) / CB_NV_DP**; thanh hành động chỉ có **[Phân công]** + **[Kiểm tra lại]**, KHÔNG có "Hoàn tất kiểm tra".
**Đối tác phản ánh:** không có nút "Hoàn tất kiểm tra", thay bằng "Kiểm tra lại".
**Kết quả mong đợi của case:** (1) trạng thái "Đang kiểm tra" → "Đã phân công"; (2) **ghi người kiểm tra và thời điểm kiểm tra**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_DP** — header "CB NV DP 01 (AG) / CB_NV_DP" (cấp Địa phương) | **`cbnv_dp`** — header "CB Nghiệp vụ - Địa phương / CB_NV_DP" (đã đăng nhập lại đúng vai trò cấp ĐP, không dùng tài khoản TW) | Không |
| Entity + trạng thái (state machine) | VV-QA-R7-SLA-QHNT — trạng thái **"Đang kiểm tra"** | VV-STP-AG-20260712-001 — trạng thái **"Đang kiểm tra"** | Không |
| Dữ liệu tiền đề (đã đánh dấu đủ 6 hạng mục checklist) | Nhóm "Kết quả kiểm tra" đã có checklist 6 hạng mục | Đã tick **đủ 6/6 hạng mục Đạt** (C01→C06 hiển thị ✓) rồi mới quan sát | Không |
| Input / giá trị nhập (kết luận) | Kết luận: Đạt (theo mô tả case) | Chọn kết luận **"Đạt — chuyển sang phân công"** rồi Xác nhận | Không |

## Quan sát (real-data) — sau khi chọn kết luận Đạt, đúng vai trò CB_NV_DP

```json
{"role":"CB_NV_DP","state":"Đang kiểm tra","buttons":["Phân công","Kiểm tra lại"],
 "accordion4":"C01..C06 đều ✓ | Kết luận: đã có dữ liệu | Lần BS 0/3"}
```

Ảnh: `../../bug-reports/image/BUG-KTHSYCHTPL_11-web-ketqua-kiemtra-thieu-nguoi-kiem-tra-va-ngay.png`

## Đối chiếu SRS (Cổng 3) — tách 2 ý

### Ý A — Không có nút "Hoàn tất kiểm tra" (thay bằng "Kiểm tra lại") → SRS TỰ MÂU THUẪN → đưa BA

- `srs-fr-05-vu-viec.md:1736` (bảng nút hành động): trạng thái `DANG_KIEM_TRA` → nút **[Hoàn tất Kiểm tra]**, "Kết luận: **Đạt → DA_PHAN_CONG**".
- NHƯNG `srs-fr-05-vu-viec.md:2280` (SM-VUVIEC): transition `DANG_KIEM_TRA → DA_PHAN_CONG` yêu cầu **"Đạt + chọn người/tổ chức xử lý"** — tức chỉ kết luận Đạt thôi thì CHƯA đủ để sang DA_PHAN_CONG.
- Web đang làm theo hướng dòng 2280: kết luận Đạt → vẫn ở `DANG_KIEM_TRA` (toast *"Kiểm tra hồ sơ đạt — sẵn sàng phân công"*), phải bấm **[Phân công]** chọn người xử lý mới sang "Đã phân công". Kết luận kiểm tra đã được ghi nhận (checklist 6/6 ✓ hiển thị trong nhóm "Kết quả kiểm tra").
- ⇒ Hai dòng SRS quy định **khác nhau** về thời điểm chuyển trạng thái. QA **không tự quyết** → đã ghi vào `ba-confirmation-needed-week-2.md`.

### Ý B — KHÔNG ghi người kiểm tra + thời điểm kiểm tra → **Open**

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1722` (SCR-V.I-03, Thành phần row 7 — Accordion 4 "Kết quả Kiểm tra"): "Checklist 6 hạng mục (ĐẠT/KHÔNG_ĐẠT) từ UC106 + **kết luận** + **lý do** + **người kiểm tra** + **ngày**".
- **Kỳ vọng của chính case** cũng ghi: *"Ghi người kiểm tra và thời điểm kiểm tra"*.
- **Thực tế web** — nhóm "Kết quả kiểm tra" chỉ có bảng 6 hạng mục + dòng **"Kết luận: đã có dữ liệu"** + "Lần BS 0/3". **KHÔNG có người kiểm tra, KHÔNG có ngày kiểm tra**, và ô kết luận in **chuỗi placeholder "đã có dữ liệu"** thay vì kết luận thực (Đạt / Không đạt / Yêu cầu bổ sung).
- ⇒ **THIẾU 3 thông tin SRS bắt buộc** (kết luận thực, người kiểm tra, ngày kiểm tra) → **Open**.

**Verdict tổng:** **Open** theo ý B (§"1 case gộp nhiều lỗi con": Open nếu ≥1 ý Open). Ý A tách sang BA confirm.
