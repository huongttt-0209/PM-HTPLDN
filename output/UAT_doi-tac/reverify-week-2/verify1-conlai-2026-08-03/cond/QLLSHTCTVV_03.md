# QLLSHTCTVV_03 — Bảng đối chiếu điều kiện

Bug phụ thuộc dữ liệu tiền đề (tab rỗng thì không có gì để tràn) và bề rộng khung nhìn → BẮT BUỘC điền bảng (QA_VERIFY_PROTOCOL §Quy tắc VÀNG). Không dùng miễn trừ `--static-bug`.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — nhãn góc phải ảnh: "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_02` — vai trò `CB_NV_TW`, đơn vị `BTP · TW`; là tác nhân hợp lệ của FR-IV-10 (dòng 764). Không dùng admin | Không |
| Entity + **trạng thái** (state machine) | Tư vấn viên `TVV-BTP-TW-0032` "TVV R11 Verify Mail Fix", badge **"Đang hoạt động"**, điểm header 4.0/5, ngày công nhận 08/05/2026 | Tư vấn viên `TVV-BTP-TW-0002` "QA TVV Seed28 Active", badge **"Đang hoạt động"**, điểm header 4.1/5, ngày công nhận 12/07/2026 | Không |
| Dữ liệu tiền đề (số vụ việc + có điểm đánh giá) | Tab "**Lịch sử hỗ trợ (4)**" — 4 bản ghi, có dòng đã có sao đánh giá; thống kê "Đã hoàn thành 2 · Điểm trung bình 8.3" | Tab "**Lịch sử hỗ trợ (6)**" — 6 bản ghi, 2 dòng có sao vàng (`VV-...0730-001` điểm 9.0, `VV-...0712-001` điểm 8.7); thống kê "Tổng 6 · Hoàn thành 3 · Điểm trung bình 8.9". Không phải seed — dữ liệu có sẵn | Không |
| Input / bề rộng khung nhìn | Khung nhìn của đối tác đủ hẹp để 5 sao vỡ 2 dòng (ảnh: 4 sao hàng trên + 1 sao hàng dưới, vùng khoanh đỏ) | Đo ở **3 mốc**: 1440×900 (khung nhìn chuẩn của dự án) → vỡ 6/6 dòng · 1600×900 → vỡ 6/6 dòng · 1920×1000 → không vỡ. Tái hiện đúng hiện tượng trong ảnh đối tác ở 2/3 mốc | Không |

**Kết luận: 0 GAP** — đúng vai trò, đúng trạng thái entity, đủ dữ liệu tiền đề (có vụ việc + có điểm đánh giá), và đã tái hiện đúng hiện tượng đối tác chụp.

**Ghi chú không tính GAP:** môi trường đối tác là `htpldn-uat.ospgroup.vn` (ảnh chụp 29/07/2026), môi trường giao cho QA là `18.143.165.120.nip.io` (bản dựng V1.0.5, test 03/08/2026). QA_VERIFY_PROTOCOL §Ca biên đã lường trước chênh lệch môi trường này. Mã tư vấn viên khác nhau (0032 vs 0002) nhưng **cùng loại entity, cùng trạng thái, cùng đơn vị BTP·TW, cùng có lịch sử hỗ trợ kèm điểm** — điều kiện tương đương, và bug là lỗi bố cục của bảng nên không phụ thuộc bản ghi cụ thể (đã chứng minh bằng việc vỡ ở **cả 6/6 dòng**, không phải 1 dòng cá biệt).
