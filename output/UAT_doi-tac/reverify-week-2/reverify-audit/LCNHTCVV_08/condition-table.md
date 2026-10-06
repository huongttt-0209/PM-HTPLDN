# LCNHTCVV_08 — Bảng đối chiếu điều kiện

**Case:** Phân công vụ việc thành công — thông báo hiển thị (FR-V.I-09 UC59 · SCR-V.I-03 §Thông báo riêng).

**Evidence đối tác:** `partner-evidence/LCNHTCVV_08.webm` (54,1 giây) — **CÓ khoảnh khắc lỗi**.
Đã bóc khung hình toàn bộ video; khoảnh khắc lỗi ở **giây 12,55 → 14,06**: URL `htpldn-uat.ospgroup.vn/vu-viec/71cb2ab1-...`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**.
Sau khi bấm [Xác nhận] trong cửa sổ Phân công, màn hình hiện **ĐỒNG THỜI 2 thông báo**:
thông báo **xanh "Đã phân công"** + thông báo **đỏ "ERR-STATE-VI-10-01: Vụ việc không ở trạng thái cho phép phân công"**.
Khung hình: `partner-frame-12s-14s-2-thong-bao.jpg`.

**Đối tác phản ánh:** Hệ thống hiển thị đồng thời 2 thông báo — "Đã phân công" và lỗi "ERR-STATE-VI-10-01".

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header video "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Entity + trạng thái trước thao tác | VV ở trạng thái cho phép phân công (thanh hành động có [Phân công] + [Kiểm tra lại]) | `VV-BTP-TW-20260712-005` (cùng đơn vị TW) — seed sang **"Đang kiểm tra"** (Kiểm tra hồ sơ 6/6 Đạt) ⇒ mở được cửa sổ Phân công (VV-003 gốc nay đã "Đã phân công") | Không |
| Quan hệ đơn vị (phải ĐÚNG đơn vị để thao tác chạy được, khác case _07) | VV thuộc cùng đơn vị người thao tác ⇒ phân công **thành công** (có thông báo "Đã phân công") | VV thuộc **Bộ Tư pháp — Trung ương**, `cbnv_tw` cũng thuộc Trung ương ⇒ phân công **thành công thật** (máy chủ trả kết quả tạo mới) | Không |
| Input (đã chọn đủ người rồi mới bấm Xác nhận) | Đã chọn người được phân công rồi mới bấm [Xác nhận] | Đã chọn `[TVV] QA TVV Seed28 Active (TVV-BTP-TW-0002)` rồi bấm **[Xác nhận]** | Không |

## Quan sát (real-data) — cbnv_tw phân công VV cùng đơn vị (Đang kiểm tra)

**Vòng 1 (bug gốc):**
```json
{"so_thong_bao_hien_ra": 2,
 "noi_dung": ["✅ Đã phân công", "❌ ERR-STATE-VI-10-01: Vụ việc không ở trạng thái cho phép phân công"]}
```

**Re-test 2026-07-15 (sau dev fix) — MutationObserver + list_network_requests:**
```json
{"so_thong_bao_hien_ra": 1,
 "toast": {"type": "success", "text": "Đã phân công vụ việc cho QA TVV Seed28 Active. Hệ thống đã gửi thông báo."},
 "errorCount": 0,
 "trang_thai_VV_sau_thao_tac": "Đã phân công",
 "network": {"POST /phan-cong": 201, "GET /goi-y-tvv (reload phụ)": 409,
             "ghi_chu": "409 phụ vẫn xảy ra nội bộ nhưng FE KHÔNG còn bắn ra toast cho người dùng"}}
```
→ **PASS:** chỉ 1 toast success kèm **tên người được phân công** (đúng SRS dòng 1768); hết toast lỗi ERR-STATE-VI-10-01.

Log: `retest-observer-log.json` · Ảnh: `../../bug-reports/image/BUG-LCNHTCVV_08-retest-chi-1-toast-thanhcong.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1768` (SCR-V.I-03 §Thông báo riêng): khi *"Phân công thành công"* → hệ thống hiển thị **1 thông báo thành công** duy nhất: **"Đã phân công vụ việc cho {tên người được phân công}. Hệ thống đã gửi thông báo."**
- **SRS chỉ cho phép hiện thông báo lỗi khi thao tác THẤT BẠI** — `srs-fr-05-vu-viec.md:770` (FR-V.I-09 §Error Handling, dòng E1, mã **ERR-PC-01**): câu *"Vụ việc không ở trạng thái cho phép phân công"* chỉ dùng cho tình huống **VV không ở trạng thái hợp lệ ⇒ phân công bị CHẶN**.
- **Thực tế web:** phân công **thành công** (trạng thái VV đã chuyển sang "Đã phân công") nhưng hệ thống **đồng thời** bắn thêm **thông báo lỗi đỏ** nói vụ việc *không ở trạng thái cho phép phân công* — **mâu thuẫn trực tiếp với kết quả thật**.
- **Hệ quả nghiệp vụ:** cán bộ không biết mình phân công được hay chưa; nhìn thông báo đỏ sẽ tưởng thất bại và bấm lại / báo lỗi lên cấp trên, trong khi vụ việc đã chuyển người xử lý.
- **Mã lỗi `ERR-STATE-VI-10-01` không tồn tại trong SRS** (đã tra toàn bộ bộ SRS v3.5) — và việc phơi mã lỗi kỹ thuật ra người dùng cuối cũng không đúng cách trình bày thông báo mà SRS quy định.

**Kết luận:** **Open**. Tái hiện đúng hiện tượng đối tác quay được: 1 lần bấm [Xác nhận] → hiện đồng thời thông báo thành công **và** thông báo lỗi.

> Ghi nhận thêm (gộp chung bug này, không tách riêng): nội dung thông báo thành công trên web chỉ là **"Đã phân công"**, thiếu tên người được phân công so với câu SRS dòng 1768 quy định.
