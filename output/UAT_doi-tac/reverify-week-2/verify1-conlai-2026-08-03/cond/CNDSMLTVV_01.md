# CNDSMLTVV_01 — Bảng đối chiếu điều kiện

Bug phụ thuộc vai trò / trạng thái entity / dữ liệu tiền đề → BẮT BUỘC điền bảng (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — nhãn góc phải ảnh: "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_02` — vai trò `CB_NV_TW`, đơn vị `BTP · TW` (donViId `00000000-0000-4000-8000-000000000001`, capDonVi `TW`), có quyền `publish_tu_van_vien` | Không |
| Entity + **trạng thái** (state machine) | Tư vấn viên ở tab "Đang hoạt động" — mọi dòng trong ảnh đều badge xanh "Đang hoạt động" | 2 TVV ở tab "Đang hoạt động": `TVV-STP-AG-0001` + `TVV-SEED-0001`, cột Trạng thái = "Đang hoạt động" | Không |
| Dữ liệu tiền đề | Điều kiện case (cột H): hồ sơ "Đang hoạt động" **và CHƯA được công khai** | Cả 2 TVV đã chọn đều có cột Công khai = **"Chưa công khai"** trước khi bấm (đọc DOM + ảnh `CNDSMLTVV_01-01-truoc-khi-bam.png`) | Không |
| Input / filter / giá trị nhập | Tích chọn nhiều ứng viên → bấm "Công khai hàng loạt" từ màn danh sách (`/chuyen-gia-tvv/danh-sach`) | Tích chọn 2 dòng ("Đã chọn 2 mục") → bấm "Công khai lên Cổng PLQG" trên thanh hành động hàng loạt, cùng màn `/chuyen-gia-tvv/danh-sach` (SCR-IV-01) | Không |

**Kết luận: 0 GAP** — đã tái hiện đúng vai trò, đúng trạng thái entity, đúng tiền đề "Đang hoạt động + chưa công khai", đúng lối vào hàng loạt của đối tác.

**Ghi chú không tính GAP:** môi trường của đối tác là `htpldn-uat.ospgroup.vn` (ảnh chụp 25/07/2026), môi trường được giao cho QA là `18.143.165.120.nip.io` (bản dựng V1.0.5, test 03/08/2026). QA_VERIFY_PROTOCOL §Ca biên đã lường trước: "env được giao luôn khác env đối tác log" — đây là chênh lệch mặc định của đợt verify, không phải điều kiện QA bỏ sót.
