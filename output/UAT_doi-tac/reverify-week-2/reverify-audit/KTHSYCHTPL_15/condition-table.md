# KTHSYCHTPL_15 — Bảng đối chiếu điều kiện

**Case:** Cán bộ nghiệp vụ **không thuộc cùng đơn vị** với hồ sơ → kiểm tra hồ sơ (FR-V.I-06 UC56).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_15.jpg` — tài khoản **CB_NV_TW** ("Cán bộ NV Trung ương"), mở hộp thoại "Kiểm tra hồ sơ" trên vụ việc của **đơn vị khác**, tick đủ Đạt, kết luận "Đạt — chuyển sang phân công" → bấm Xác nhận → hiện **2 thông báo lỗi**: *"Đơn vị của người phê duyệt khác đơn vị của bản ghi"*.
**Đối tác phản ánh:** thông báo hiển thị là *"Đơn vị của người phê duyệt khác đơn vị của bản ghi"*, trong khi kỳ vọng *"Bạn không có quyền kiểm tra vụ việc của đơn vị khác"*.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" | Không |
| Entity + trạng thái (state machine) | Vụ việc ở trạng thái **"Đã tiếp nhận"** (nút [Kiểm tra hồ sơ] còn hiện) | VV-STP-AG-20260712-002 — trạng thái **"Đã tiếp nhận"** | Không |
| Dữ liệu tiền đề (hồ sơ thuộc **đơn vị KHÁC** với cán bộ đang thao tác) | Vụ việc thuộc đơn vị khác đơn vị của user (BE trả lỗi lệch đơn vị) | Đã **tự seed**: đăng nhập `cbnv_dp` (Sở Tư pháp An Giang) tạo `VV-STP-AG-20260712-002`, sau đó đăng nhập `cbnv_tw` (Trung ương) thao tác lên chính vụ việc đó ⇒ đúng tình huống "cán bộ khác đơn vị với hồ sơ" | Không |
| Input / giá trị nhập (kết luận) | Tick đủ 6 hạng mục Đạt + kết luận "Đạt — chuyển sang phân công" | Tick đủ 6/6 Đạt + kết luận "Đạt — chuyển sang phân công" | Không |

## Quan sát (real-data) — 1 lần bấm Xác nhận

**Vòng 1 (bug gốc):**
```json
{"toastCountFromOneClick": 2,
 "toasts": ["Đơn vị của người phê duyệt khác đơn vị của bản ghi",
            "Đơn vị của người phê duyệt khác đơn vị của bản ghi"],
 "stateAfter": "Đã tiếp nhận"}
```

**Re-test 2026-07-15 (sau dev fix) — MutationObserver đếm .ant-message-notice-wrapper:**
```json
{"toastCountFromOneClick": 1,
 "toasts": ["Bạn không có quyền kiểm tra vụ việc của đơn vị khác"],
 "stateAfter": "Đã tiếp nhận"}
```
→ **PASS:** message đổi sang đúng vai trò/thao tác ("kiểm tra vụ việc", tiếng Việt thuần, bỏ jargon "bản ghi"), và **chỉ hiện 1 lần**.

Log: `retest-observer-log.json` · Ảnh flow: `../../bug-reports/image/BUG-KTHSYCHTPL_15-retest-thongbao-dung-vaitro-1lan.png` (toast top-center sau modal nên không lọt khung; số liệu quyết định lấy từ observer).

## Đối chiếu SRS (Cổng 3)

**Phần ĐÚNG (không phải bug):** hệ thống **chặn đúng** — vụ việc giữ nguyên trạng thái "Đã tiếp nhận", không bị kiểm tra bởi cán bộ khác đơn vị. Đúng FR-V.I-06 §Processing bước 1 (`srs-fr-05:533` — "Kiểm tra quyền + phân quyền theo đơn vị", BR-AUTH-01).

**Phần SAI → Open:** nội dung thông báo từ chối.

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1577` (§Thông báo người dùng chung của module): *"Không có quyền truy cập | Toast error | **'Bạn không có quyền thực hiện thao tác này'**"*. Các FR khác cùng module đều theo mẫu nêu rõ **người dùng** + **hành động bị chặn**: `:773` ERR-PC-05 *"Bạn không có quyền phân công VV của đơn vị khác"* · `:996` ERR-PD-02 · `:1225` ERR-DG-VV-04 · `:1382` ERR-CK-VV-02 · `:466` ERR-AUTH-01.
- **Thực tế web** — *"Đơn vị của người phê duyệt khác đơn vị của bản ghi"*:
  1. **Sai vai trò/hành động**: gọi người đang thao tác là **"người phê duyệt"**, trong khi thao tác là **kiểm tra hồ sơ** do **Cán bộ Nghiệp vụ** thực hiện (không có bước phê duyệt nào ở đây).
  2. **Dùng từ kỹ thuật "bản ghi"** (record) — trái quy ước BA "tiếng Việt thuần, không jargon kỹ thuật" (`srs-fr-02-hoi-dap.md:21`).
  3. **Không nói người dùng cần làm gì / vì sao bị chặn** theo mẫu "Bạn không có quyền…".
  4. **Hiển thị lặp 2 lần** cho 1 lần thao tác (trùng pattern đã log ở `BUG-CNTTTVV_06`).

**Kết luận:** hành vi chặn đúng, nhưng **thông báo sai vai trò + sai mẫu SRS + lặp 2 lần** → **Open**. Kỳ vọng của đối tác ("Bạn không có quyền kiểm tra vụ việc của đơn vị khác") **khớp với mẫu SRS**, nên đây không phải tranh chấp đặc tả.
