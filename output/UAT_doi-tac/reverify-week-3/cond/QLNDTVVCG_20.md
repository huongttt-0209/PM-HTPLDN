# Bảng đối chiếu điều kiện — QLNDTVVCG_20 (Nhật ký thao tác không hiển thị dữ liệu)

- **Row:** 285 · **Verdict:** Reject
- **Đối tác phản ánh:** Nhóm "Nhật ký thao tác" KHÔNG hiển thị dữ liệu dù bản ghi đã qua hết các trạng thái (evidence video `QLNDTVVCG_20.webm`, frame ~t011: mở nhóm Nhật ký trên TVCS-20260527-0001 DA_DUYET → hiện "Chưa có nhật ký hoạt động.").
- **SRS:** BR-DATA-05 "Ghi nhật ký thao tác" — mọi bước Processing (create/phân công/hoàn thành/phê duyệt/hủy) đều ghi nhật ký (`input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:143,146,163,197,209`); màn hiển thị timeline nhóm Nhật ký (`...:1146`).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ TW (CB_NV_TW), env `htpldn-uat.ospgroup.vn` | `cbnv_tw_03` (CB_NV_TW, BTP·TW), env nip.io | Không |
| Entity + **trạng thái** | TVCS-20260527-0001 · DA_DUYET · các mốc ngày (bắt đầu/hoàn thành/tạo) **đều 27/05/2026** → dấu hiệu bản ghi nạp sẵn/backdate, không thao tác thật theo thời gian | (a) TVCS-SEED-0001 · DA_DUYET · **nạp thẳng DB** (id `5eed...`) → Nhật ký **0 dòng**; (b) TVCS-20260721-0001 · TIEP_NHAN · **tạo qua UI hôm nay** → Nhật ký **1 dòng "Tạo mới"** | Không |
| Dữ liệu tiền đề: bản ghi có thao tác audit thật | bản ghi (được cho là) đã qua thao tác | bản ghi TVCS-20260721-0001 có thao tác CREATE thật qua UI | Không |

**Ghi chú đóng GAP trạng thái:**
- Điểm mấu chốt: đối tác thấy **0 dòng** (kể cả dòng "tạo mới" cũng không có). Trên nip.io, **bất kỳ** bản ghi có thao tác thật đều hiển thị ≥1 dòng nhật ký. Bản ghi hiển thị trống CHỈ là bản ghi nạp thẳng DB (không phát sinh audit event) — đúng với seed của mình VÀ khớp dấu hiệu bản ghi đối tác (3 mốc ngày trùng 27/05/2026 = backdate/seed).
- Bằng chứng đối chiếu trực tiếp:
  - API `GET /noi-dung-tu-van-cs/{seed}/audit-logs` → `data:[], total:0` (bản seed DB).
  - API `GET /noi-dung-tu-van-cs/{TVCS-20260721-0001}/audit-logs` → `total:1`, entry `hanhDong:CREATE`, `nguoiThucHien: cbnv_tw_02`, `thoiGian: 2026-07-21T11:07:05`, `endpoint: POST /noi-dung-tu-van-cs (201)`.
  - UI render đúng: bảng Nhật ký (Thời gian/Hành động/Người thực hiện/Vai trò) → dòng "21/07/2026 18:07 · Tạo mới · CB Nghiệp vụ - Trung ương #02 (cbnv_tw_02) · Cán bộ Nghiệp vụ TW".
- **Kết luận:** Chức năng Nhật ký (ghi + hiển thị) hoạt động đúng khi có thao tác thật → defect "không hiển thị dữ liệu" KHÔNG tái hiện. Nhật ký trống là hệ quả của bản ghi seed nạp thẳng DB, không phải lỗi chức năng.
- **Phạm vi đã kiểm:** thao tác CREATE (ghi + render). Việc log ĐẦY ĐỦ cho mọi bước chuyển trạng thái (phân công/hoàn thành/phê duyệt) thuộc luồng workflow (batch D) — nhưng không ảnh hưởng verdict vì đối tác báo "0 dòng" (kể cả create), mà create đã chứng minh ghi + render đúng.

**Evidence:**
- `reverify-audit/QLNDTVVCG_20/frames-fine/t011.11s.jpg` (đối tác — "Chưa có nhật ký hoạt động.")
- `reverify-audit/QLNDTVVCG_20/qlndtvvcg_20-nhatky-taomoi-nip.png` (nip.io — Nhật ký hiển thị dòng "Tạo mới")
