# Functional Test Report — R7.7.1 Hỏi đáp Phase 8 (rerun blocked/unrun TC)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | PM HTPLDN |
| Môi trường | http://103.172.236.130:3000/ |
| Ngày chạy | 2026-05-10 19:39-19:49 ICT |
| Tool | Playwright browser automation |
| Account | `cb_pd_tw_04` / OTP `666666` |
| Scope | Rerun các TC R7.7.1 còn chưa chạy được sau Phase 7 |

## Kết luận

Phase 8 chạy lại các TC còn defer/block trong R7.7.1. Kết quả: **1 TC mới PASS (HD-054)**, **1 TC PARTIAL/FAIL UX (HD-055)**, **HD-053 vẫn Open**, và **12 TC vẫn không thể chạy end-to-end** do Cổng PLQG/TVN_BRIDGE chưa deploy hoặc thiếu tooling time-travel/backdated seed.

## Verdict

| TC | Mục tiêu | Kết quả Phase 8 | Evidence |
|---|---|---|---|
| HD-053 | Modal Công khai CR-01 có ảnh đại diện + nút "Dùng ảnh hệ thống mặc định" | **FAIL / bug vẫn Open**. Modal vẫn chỉ có button Close, Hủy, Công khai. Không có text/button "Dùng ảnh hệ thống mặc định". Upload ảnh vẫn chỉ `.jpg, .png ≤5MB`, chưa thấy `.gif`. | `image/r7-7-1-phase8-hd053-modal-reverify.png` |
| HD-054 | Submit Công khai OK: state `CONG_KHAI`, `congKhai=true`, `thoiGianDangTai=NOW()` | **PASS**. Submit modal trên HD-20260509-010 trả `POST /cong-khai` 200. API verify `trangThai=CONG_KHAI`, `congKhai=true`, `thoiGianDangTai=2026-05-10T12:46:11.741Z`, `moTaCongKhai` persisted. Sau test đã hủy công khai để restore về `DA_DUYET`; API verify `thoiGianDangTai=null`. | `image/r7-7-1-phase8-hd054-before-submit.png`, `image/r7-7-1-phase8-hd054-after-submit.png`, `image/r7-7-1-phase8-hd054-after-restore.png` |
| HD-055 | Công khai API fail giữ state `DA_DUYET`, hiện ERR-PD-04 + nút "Thử lại" | **PARTIAL / UX fail**. Inject 500 cho `POST /api/v1/hoi-daps/{id}/cong-khai`: state giữ đúng `DA_DUYET`, `congKhai=false`, `thoiGianDangTai=null`. Nhưng modal không hiện lỗi `ERR-PD-04`, không có text lỗi phân biệt mạng/máy chủ/nghiệp vụ, không có nút "Thử lại"; modal chỉ đứng yên. | `image/r7-7-1-phase8-hd055-before-injected-fail.png`, `image/r7-7-1-phase8-hd055-after-injected-fail.png` |
| HD-027 | DN tạo HOI_DAP qua Cổng PLQG inbound API | **BLOCKED**. 7 candidate endpoint + POST inbound vẫn 404 `ERR-SYS-00-04-01`. | endpoint probe |
| HD-045 | TVN_BRIDGE inbound từ phiên Tư vấn nhanh ESCALATE | **BLOCKED**. Cổng PLQG/FR-13 bridge chưa có endpoint/data. | endpoint probe |
| HD-047 | Badge/tooltip "Từ Tư vấn nhanh" + link lịch sử gốc | **BLOCKED**. Không có bản ghi `kenhTiepNhan=TVN_BRIDGE` để mở list/detail. | `image/r7-7-1-phase8-hd048-tvn-bridge-filter-empty.png` |
| HD-048 | Filter TVN_BRIDGE count >= 1 | **BLOCKED**. API `?kenhTiepNhan=TVN_BRIDGE` trả `total=0`, UI filter "Từ Tư vấn nhanh" hiển thị "Không có dữ liệu". | `image/r7-7-1-phase8-hd048-tvn-bridge-filter-empty.png` |
| HD-060 | CR-06 DN chọn cơ quan tiếp nhận | **BLOCKED**. Cần Cổng PLQG inbound/DN portal flow; endpoint inbound vẫn 404. | endpoint probe |
| HD-061 | CR-06 default Sở TP theo tỉnh DN | **BLOCKED**. Cần Cổng PLQG inbound/DN portal flow; endpoint inbound vẫn 404. | endpoint probe |
| HD-062 | Scope theo `don_vi_id` bản ghi CR-06 | **BLOCKED**. Cần seed được HD từ CR-06 trước; chưa có dữ liệu HD CR-06. | endpoint probe |
| HD-057 | Không auto-close sau 30+ ngày | **BLOCKED bởi data/tooling**. 19/19 bản ghi hiện tại đều `mucDoCanhBao=BINH_THUONG`; không có DA_DUYET/CONG_KHAI backdated 30+ ngày. | API list probe |
| HD-022b | SLA SAP_HET_HAN vàng | **BLOCKED bởi time-travel/backdated data**. 19/19 bản ghi hiện tại đều `mucDoCanhBao=BINH_THUONG`; không có record ratio 50-100%. | API list probe |
| HD-022c | SLA QUA_HAN đỏ | **BLOCKED bởi time-travel/backdated data**. Không có record ratio >100%. | API list probe |
| HD-022d | SLA QUA_HAN_NGHIEM_TRONG đen | **BLOCKED bởi time-travel/backdated data**. Không có record ratio >200%. | API list probe |

## Endpoint Probe

Tất cả endpoint Cổng PLQG candidate vẫn 404:

```text
GET  /api/v1/cong-plqg/inbound/hoi-dap     404 ERR-SYS-00-04-01
GET  /api/v1/cong-plqg/health              404 ERR-SYS-00-04-01
GET  /api/v1/cong-plqg/status              404 ERR-SYS-00-04-01
GET  /api/v1/cong-plqg/hoi-dap             404 ERR-SYS-00-04-01
GET  /api/v1/inbound/cong-plqg/hoi-dap     404 ERR-SYS-00-04-01
GET  /api/v1/external/hoi-daps             404 ERR-SYS-00-04-01
GET  /api/v1/cong-plqg/inbound             404 ERR-SYS-00-04-01
POST /api/v1/cong-plqg/inbound/hoi-dap     404 ERR-SYS-00-04-01
```

`GET /api/v1/hoi-daps?kenhTiepNhan=TVN_BRIDGE&size=20` trả `total=0`, `data=[]`.

## Cumulative R7.7.1

Trước Phase 8: **42/60 PASS Phase 7**.

Sau Phase 8:

- **+1 PASS mới:** HD-054.
- **Không nâng HD-053:** bug default image button vẫn Open.
- **HD-055:** state guard đúng nhưng UX lỗi fail handling.
- **Còn blocked:** HD-027/045/047/048/057/060/061/062 + HD-022b/c/d.

Tạm tính functional pass mới: **43/60 PASS**, nếu chấp nhận HD-054 là TC mới unblocked. Các TC phụ thuộc Cổng PLQG vẫn chưa thể full-run.

## Files

- `image/r7-7-1-phase8-hd053-detail-before-modal.png`
- `image/r7-7-1-phase8-hd053-modal-reverify.png`
- `image/r7-7-1-phase8-hd054-before-submit.png`
- `image/r7-7-1-phase8-hd054-after-submit.png`
- `image/r7-7-1-phase8-hd054-restore-confirm.png`
- `image/r7-7-1-phase8-hd054-after-restore.png`
- `image/r7-7-1-phase8-hd055-before-injected-fail.png`
- `image/r7-7-1-phase8-hd055-after-injected-fail.png`
- `image/r7-7-1-phase8-hd048-tvn-bridge-filter-empty.png`

