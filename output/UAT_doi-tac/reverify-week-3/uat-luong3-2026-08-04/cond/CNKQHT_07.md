# Bảng đối chiếu điều kiện — CNKQHT_07 (dòng 315) — Cập nhật kết quả hỗ trợ có gửi thông báo cho CBNV phụ trách

**Kết luận:** Pass — bấm "Cập nhật kết quả" trên vụ việc đang xử lý thì cán bộ nghiệp vụ phụ trách nhận được thông báo ngay, đúng giây bấm.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:30, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Người được phân công xử lý vụ việc (TVV/CG) | `huongcg` — Chuyên gia kiêm Tư vấn viên, là người hỗ trợ được phân công của chính vụ việc | Không |
| Vai trò người nhận | Cán bộ nghiệp vụ **phụ trách vụ việc đó** | `cb_nv_tw_01` — người tiếp nhận vụ việc (đọc `nguoiTiepNhanId` của bản ghi để xác định, không đoán) | Không |
| Entity + trạng thái | Hồ sơ vụ việc "Đang xử lý" | `VV-BTP-TW-20260525-001`, trạng thái "Đang xử lý" (bước 6) | Không |
| Dữ liệu tiền đề | Vụ việc đã tiếp nhận – kiểm tra – phân công – xác nhận tham gia | Có sẵn đủ chuỗi trên Dòng thời gian: Tạo 25/05 → Tiếp nhận + Kiểm tra 23/06 → Phân công 09/07 → Xác nhận phân công 10/07 | Không |
| Thao tác / input | Nhập nội dung + tải tệp rồi bấm "Cập nhật kết quả" | Nhập nội dung có chuỗi nhận dạng `QA-KQ-V2-0408-742199` + đính kèm tệp `ketqua-cnkqht07-v2.png` + ghi chú, bấm "Xác nhận" | Không |

**Bằng chứng:**
- `image/CNKQHT_07-v2-01-luu-ket-qua-noi-dung-tep-luu-vet.png` — mục "Kết quả hỗ trợ" hiện đúng nội dung vừa nhập, tệp vừa đính kèm nằm đầu danh sách, Dòng thời gian có dòng "Cập nhật kết quả · 04/08/2026 14:30 · huongcg".
- `image/CNKQHT_07-v2-02-cbnv-phutrach-nhan-thongbao.png` — mở chuông bằng chính tài khoản `CB Nghiệp vụ TW 01 · CB_NV_TW`: mục "Kết quả hỗ trợ đã được cập nhật - VV-BT…" / "Người được phân công đã cập nhật kết quả hỗ trợ vụ việc…", một phút trước.
- Đếm hộp thông báo trước/sau bằng `GET /api/v1/thong-baos`: trước 453 mục, không có mục nào của vụ việc này → sau 455 mục, mục mới `Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260525-001` ghi nhận lúc `07:30:35Z`, trùng đúng giây với thời điểm bấm `07:30:35.860Z`.
- Bộ bắt thông báo (`soObserverDangSong = 1`): 1 request `POST /api/v1/vu-viecs/{id}/cap-nhat-ket-qua`, 1 khung thông báo "Đã cập nhật kết quả" — không lặp.
