# Bảng đối chiếu điều kiện — CTTLV_01 (row 270) — BC Chương trình theo lĩnh vực (FR-IX-22)

**Đối tác phản ánh:** "Dữ liệu hiển thị Không xác định" — báo cáo hiện lĩnh vực = "Không xác định".

**Loại bug:** Data/mapping (phụ thuộc data nguồn + FE map linh_vuc_id → tên) → BẮT BUỘC bảng đối chiếu, 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ (xem báo cáo thống kê) | `cbnv_tw_04` (CB_NV_TW, Toàn quốc) — cùng vai trò | Không |
| Loại báo cáo | BC "Chương trình theo lĩnh vực" (FR-IX-22 / UC145) | BC "Chương trình theo lĩnh vực", Năm 2026, Toàn quốc | Không |
| Phạm vi đơn vị | Toàn hệ thống | Toàn quốc | Không |
| Dữ liệu tiền đề (CT có/không lĩnh vực) | Có CT hiển thị "Không xác định" | Có **cả 2 loại**: CT có lĩnh vực (Thương mại) + CT không gán lĩnh vực → đủ để kiểm tra map đúng/sai | Không |
| Kiểm chứng nguồn (linh_vuc_id per CT) | — | Truy `GET /api/v1/chuong-trinh-htpls` đọc `linhVucId` từng CT để đối chiếu với nhãn báo cáo | Không |

**Kết luận:** 0 GAP. Có đủ CT hai loại (có/không lĩnh vực); kiểm chứng được nhãn báo cáo so với `linhVucId` nguồn.

**Đo 2 phương pháp (bug candidate ≠ bug):**

- **UI + API báo cáo** `GET /api/v1/bao-cao/ct-theo-linh-vuc` (Năm 2026, Toàn quốc): bảng 2 nhóm — **"Không xác định": 3 CT** (`linhVucId:null`), **"Thương mại": 1 CT** (`linhVucId:"bbbb…001c"`). Tổng CT = 4. UI khớp API.
- **Kiểm chứng nguồn** `GET /api/v1/chuong-trinh-htpls`: 3 CT nhóm "Không xác định" đều có **`linhVucId=null` tại nguồn** (CT-0002 DANG_THUC_HIEN, CT-0003 HOAN_THANH, CT-0004 DA_DUYET — đều là CT QA seed tạo KHÔNG gán lĩnh vực). CT-0001 "verify Thương mại" có `linhVucId=Thương mại` tại nguồn → báo cáo hiển thị **đúng "Thương mại"**, KHÔNG bị nhầm thành "Không xác định".
- → Báo cáo **trung thực với nguồn**: CT có lĩnh vực map đúng tên; CT không gán lĩnh vực gom vào "Không xác định". KHÔNG có lỗi map linh_vuc_id → tên. "Không xác định" là nhãn đúng cho CT `linhVucId=null`.

**SRS:**
- `srs-fr-11-bao-cao.md:982` — §Output FR-IX-22: `ten_linh_vuc | text | Luôn`. Với CT `linh_vuc_id=null`, "Không xác định" là nhãn mặc định hợp lý (không có tên lĩnh vực).
- `srs-fr-11-bao-cao.md:987` — AC: "bảng: hàng = lĩnh vực, cột = số CT + số DN". Bảng phải đếm ĐỦ CT; nếu bỏ CT null lĩnh vực sẽ undercount (tổng phải = 4). Gom vào "Không xác định" giữ tổng đúng.

**Verdict: Reject** — web hoạt động đúng. "Không xác định" phản ánh chính xác 3 CT tạo không gán lĩnh vực (nguồn `linhVucId=null`); CT có lĩnh vực (Thương mại) vẫn map đúng, không bị nhầm. Không tái hiện lỗi map / lỗi hiển thị. Muốn hết "Không xác định" thì phải gán lĩnh vực cho các CT đó khi tạo.

> **Quan sát ngoài case (không log bug):** CT `CTHTPL-SEED-0001` (Thương mại, DA_CONG_BO) KHÔNG được báo cáo đếm (Thương mại = 1 chứ không phải 2). Theo `input/input.md`, CT seed này có `donVi RỖNG` + `ngayCongBo=null` → bị loại khỏi báo cáo scope đơn vị/kỳ. Là seed artifact đã biết, không phải lỗi sản phẩm — nêu ở phần "bất thường" cuối batch để BA/QA nắm.
