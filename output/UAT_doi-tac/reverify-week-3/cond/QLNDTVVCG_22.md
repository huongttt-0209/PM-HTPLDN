# Bảng đối chiếu điều kiện — QLNDTVVCG_22 (Modal Phân công CG: Chuyên môn "—" + chú thích SLA)

- **Row:** 286 · **Verdict:** BA confirm
- **Đối tác phản ánh:** (1) Modal Phân công CG KHÔNG hiện "Chuyên môn" của TVV/CG dù có data; (2) thiếu chú thích "Chuyên gia sẽ được gửi thông báo...". Evidence `QLNDTVVCG_22.jpg` (modal CG "huongcg — Đất đai, Hình sự, Lao động, Thuế", Chuyên môn = —).
- **SRS:** modal Phân công (`input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1153`) — "gợi ý TOP 5 CG (lĩnh vực khớp...) + tìm CG + ghi chú + info SLA (2 ngày LV xác nhận)"; pattern hiện chuyên môn khi chọn CG (`...:1142`); "chuyên môn phù hợp lĩnh vực" (`...:160`).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ TW (CB_NV_TW) | `cbnv_tw_03` (CB_NV_TW, BTP·TW) | Không |
| Entity + **trạng thái** | Record TIEP_NHAN → mở modal Phân công | TVCS-20260721-0001 · TIEP_NHAN → mở modal Phân công | Không |
| Dữ liệu tiền đề: pool CG + field chuyên môn | CG "huongcg" — dropdown hiện lĩnh vực (Đất đai, Hình sự, Lao động, Thuế); Chuyên môn = — | CG "QA TVV Seed28 Active" — dropdown hiện lĩnh vực "Thương mại"; Chuyên môn = —. API CG: `chuyenNganh:null`, `linhVucText:"Thương mại"`, `dienThoai/email` có | Không |

**Phát hiện root cause (đóng GAP data):**
- API modal load CG `GET /tu-van-viens?...&loaiTvv=CG&linhVucIds=<record.linhVuc>` → 1 CG, object:
  `hoTen:"QA TVV Seed28 Active"`, **`chuyenNganh: null`**, **`linhVucText: "Thương mại"`**, `dienThoai:"0912280028"`, `email:"qa.tvvseed28@..."`.
- Nhãn dropdown "QA TVV Seed28 Active — Thương mại" lấy từ **`linhVucText`** (Lĩnh vực), KHÔNG phải chuyên môn.
- Bảng chi tiết trong modal: **SĐT + Email populate đúng** (từ dienThoai/email); **"Chuyên môn: —"** vì field này map vào **`chuyenNganh` = null**.
- → App render "—" đúng với giá trị `chuyenNganh=null`. Vấn đề là **ngữ nghĩa/mapping**: "Chuyên môn" nên hiển thị lĩnh vực/chuyên môn CG có sẵn (`linhVucText`) hay là field `chuyenNganh` (đang trống)? SRS "hiện chuyên môn" không định nghĩa field cụ thể. → **BA quyết**, KHÔNG prescribe fix (tránh talk-past như BUG-PC-INACTIVE).
- Khác với case đối tác "dù CÓ data": data chuyên môn thực (`chuyenNganh`) là **null** — thứ đối tác thấy (Thương mại) là **lĩnh vực** (field khác). Reproduce đúng hiện tượng (Chuyên môn —) nhưng nguyên nhân là field mapping + null, không phải FE giấu data cùng field.

**Chú thích SLA (ý 2):** modal CÓ banner "SLA: Chuyên gia có 2 ngày làm việc để xác nhận tham gia." — thỏa "info SLA (2 ngày LV)" (SRS dòng 1153). Wording "Chuyên gia sẽ được gửi thông báo..." đối tác kỳ vọng là thiết kế UX, SRS không quy định → BA quyết có bổ sung không.

**Evidence:**
- `partner-evidence/QLNDTVVCG_22.jpg` (đối tác — Chuyên môn —)
- `reverify-audit/QLNDTVVCG_22/qlndtvvcg_22-modal-chuyenmon-rong-nip.png` (nip.io — Chuyên môn —, SLA banner)
