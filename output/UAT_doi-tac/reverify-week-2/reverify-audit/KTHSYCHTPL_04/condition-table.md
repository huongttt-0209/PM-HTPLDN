# KTHSYCHTPL_04 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị Nhóm 2 — Nội dung Yêu cầu (SCR-V.I-03, Accordion 2).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_04.jpg` — đối tác bôi đậm nhãn **"Deadline"** trong nhóm "Nội dung Yêu cầu" (VV-BTP-TW-20260525-001, "Đang kiểm tra").
**Đối tác phản ánh:** tên trường "Thời hạn xử lý" đang hiển thị bằng **tiếng Anh** ("Deadline").

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW — header "Cán bộ NV Trung ương / CB_NV_TW" | `cbnv_tw` — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" | Không |
| Entity + trạng thái (state machine) | VV-BTP-TW-20260525-001 — trạng thái "Đang kiểm tra" | VV-BTP-TW-20260712-003 — trạng thái "Đang kiểm tra" | Không |

## Quan sát (real-data)

Nhóm "Nội dung Yêu cầu" trên web QA — **nhãn "Deadline" là nhãn tiếng Anh duy nhất**, 6 nhãn còn lại đều tiếng Việt:

```json
[{"label":"Tiêu đề"},{"label":"Lĩnh vực"},{"label":"Loại hình"},{"label":"Kênh tiếp nhận"},
 {"label":"Ưu tiên"},{"label":"Ngày tiếp nhận"},{"label":"Deadline","value":"31/07/2026"}]
```

Ảnh: `KTHSYCHTPL_04-web-nhan-deadline-tieng-anh.png`

→ **Actual của đối tác TÁI HIỆN đúng** (nhãn thật sự là "Deadline", tiếng Anh). Tranh chấp nằm ở **expected/spec**, không phải ở thực tế.

## Đối chiếu SRS (Cổng 3) — SRS mâu thuẫn giữa các nguồn

1. **SCR-V.I-03 Accordion 2** (`srs-fr-05-vu-viec.md:1720`) liệt kê các trường: `tieu_de, noi_dung_yeu_cau, linh_vuc, loai_hinh_ho_tro, vu_viec_vuong_mac, ghi_chu` — **KHÔNG có trường thời hạn/deadline nào**. → SRS **im lặng** về nhãn của trường này trên màn chi tiết.
2. **Cùng file srs-fr-05 lại dùng chính chữ "Deadline" làm NHÃN CỘT hiển thị:** `srs-fr-05-vu-viec.md:1637` — "| 19 | table | **Deadline SLA** | date | dd/mm/yyyy (110px)" (SCR-V.I-01). Tức là trong module này, SRS **tự đặt nhãn UI có tiếng Anh**.
3. **Ngược lại, BA đã chốt quy ước UI "Tiếng Việt thuần, không jargon kỹ thuật"** và **bỏ đúng chữ "deadline"**: `srs-fr-02-hoi-dap.md:21` — *"dòng 13a bỏ 'deadline' + 'CAU_HINH_SLA' → 'hạn xử lý' + 'mức độ phức tạp'"*; `srs-fr-04-chuyen-gia-tvv.md:20` — *"text hiển thị user-facing → tiếng Việt thuần"*. Ở module Hỏi đáp, trường tương đương được BA đặt nhãn **"Thời hạn xử lý"** (`srs-fr-02:1105`).
4. **Thêm mâu thuẫn nội bộ trong chính lô UAT này:** bug **BUG-QLTNVV_02** (đã log Open ở vòng trước) lại yêu cầu app đổi nhãn cột danh sách **về đúng "Deadline SLA"** theo SRS dòng 1637 — tức là đang yêu cầu hướng **ngược lại** với kỳ vọng "tiếng Việt" của case này.

**Kết luận:** actual đối tác đúng; nhưng expected ("Thời hạn xử lý") **không có trong SRS module Vụ việc**, và 2 nguồn (quy ước tiếng Việt thuần của BA vs nhãn "Deadline SLA" trong srs-fr-05) **mâu thuẫn nhau** → **BA confirm**, QA không tự quyết. Đã ghi vào `ba-confirmation-needed-week-2.md`.
