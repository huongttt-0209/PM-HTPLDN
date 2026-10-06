# Bảng đối chiếu điều kiện — QLTKND_06 (row 167)

**Case:** Màn Quản lý tài khoản (SCR-VIII-03) — tìm kiếm không ra kết quả → thông báo empty-state.
**Đối tác phản ánh:** hiện chữ "Trống"; kỳ vọng "Không tìm thấy tài khoản phù hợp".
**Verdict:** `BA confirm` (actual tái hiện đúng "Trống"; SRS silent về message empty-search cho màn này).

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLTKND_06.jpg) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT") | admin / QTHT | Không |
| Entity + trạng thái | Màn `/quan-tri/tai-khoan`, list có data (201 TK), lọc còn 0 | Màn `/quan-tri/tai-khoan`, list có data (27 TK), lọc còn 0 | Không |
| Input / filter / giá trị nhập | Từ khóa "tkm" + bộ lọc kết hợp → 0 kết quả | Từ khóa "zzxqwnonexistent999" → 0 kết quả | Không |

**0 GAP.** Cùng màn, cùng vai trò QTHT, cùng loại kết quả (query không match → 0 bản ghi → empty-state).

## Kết quả test (real-data, artifact)

- Search "zzxqwnonexistent999" → `list_network_requests`/DOM: 0 dòng bảng.
- `document.querySelector('.ant-empty')` tồn tại, `innerText = "Trống"` (component empty mặc định AntD, KHÔNG phải placeholder "Chức năng đang phát triển").
- Ảnh: `reverify-audit/QLTKND_06/empty-trong.png`.

## Đối chiếu SRS
- SCR-VIII-03 (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1642-1673`): §Thành phần màn hình + Form KHÔNG có dòng nào quy định thông báo khi tìm kiếm không có kết quả. Grep toàn file: message "Không tìm thấy..." chỉ xuất hiện cho các màn khác (mẫu phản hồi dòng 1773, nhật ký dòng 1910), KHÔNG cho màn Tài khoản.
- → SRS **silent** về nội dung message empty-search cho SCR-VIII-03.

## Kết luận
Đối tác quan sát ĐÚNG (hiện "Trống"), nhưng kỳ vọng message ngữ cảnh "Không tìm thấy tài khoản phù hợp" **KHÔNG được SRS quy định** cho màn này → bất đồng về ĐẶC TẢ (SRS silent) → **BA confirm**. Cross-ref: cùng bản chất với QLDMCQDVQL_05 (B5) — nghi 1 component empty-state dùng chung; B5 cũng đã verdict `BA confirm`. QA KHÔNG tự Reject (đối tác quan sát đúng thực tế).
