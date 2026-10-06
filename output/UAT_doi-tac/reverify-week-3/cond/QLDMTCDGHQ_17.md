# Bảng đối chiếu điều kiện — QLDMTCDGHQ_17 (row 159)

**Case:** Danh mục Tiêu chí đánh giá hiệu quả — phân trang khi tổng > 20 record.
**Đối tác phản ánh:** Lỗi phân trang khi tổng > 20 record.
**Loại bug:** Phân trang (data-dependent) → cần bảng đối chiếu.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLDMTCDGHQ_17.webm) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT" góc phải video) | admin / QTHT | Không |
| Entity + trạng thái | DM Tiêu chí ĐG hiệu quả, list, 21 record (>20, 2 trang) | DM Tiêu chí ĐG hiệu quả, list, 23 record (>20, 2 trang) — TỰ SEED thêm 22 record QTHTB6TC01-22 (ban đầu chỉ 1) | Không |
| Dữ liệu tiền đề | Tổng > 20 → ≥2 trang, page 2 chỉ vài record cuối | 23 record → trang 1=20, trang 2=3 (đúng điều kiện >20) | Không |
| Input / filter (thao tác phân trang) | Click sang trang 2 (page indicator=2) | Click sang trang 2 + round-trip về trang 1 | Không |

**0 GAP.** Đã seed đúng điều kiện >20 record của đối tác (§Nguyên tắc 4 — tiền đề tạo được). Sau test đã dọn 22 record seed, trả tab về 1 record (100%).

## Kết quả test (real-data, artifact)

- Seed 22 record QTHTB6TC01-22 (trọng số 1 mỗi record → tổng 122%, cảnh báo "Tổng trọng số: 122% (cần đúng 100%)" — khớp behavior đối tác 150%). Tổng 23 record.
- **Trang 1** (`?page=1&pageSize=20`): hiện đúng 20 record (QTHTB2TCHQ … QTHTB6TC19), footer "1-20 / 23 mục", page 1 active, nút trang 2 khả dụng. Ảnh `reverify-audit/QLDMTCDGHQ_17/page1.png`.
- **Click sang trang 2** (`?page=2&pageSize=20`): hiện đúng **3 record trang 2** (QTHTB6TC20, TC21, TC22), footer "21-23 / 23 mục", page 2 active. **KHÔNG lặp lại record trang 1, KHÔNG trùng record, số đếm đúng.** Ảnh `page2.png`.
- **Round-trip về trang 1**: hiện lại đúng 20 record (…TC19), footer "1-20 / 23 mục". Bảng re-render đúng mỗi lần đổi trang.
- Backend API cũng đúng: `/api/v1/danh-muc?...&page=2&pageSize=20` trả 3 record riêng (total=23, totalPages=2, overlap trang 1↔2 = rỗng).

→ Phân trang hoạt động đúng SRS (20/trang — `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:91` + `:1607`), text "{từ}-{đến} / {tổng}" đúng, không trùng/sai đếm/không đứng yên.

**Lỗi đối tác báo (phân trang lỗi khi >20) KHÔNG tái hiện.** → Reject + đối tác kiểm tra lại (video đối tác trang 2 hiện lại record trang 1 — nghi build cũ; build hiện tại đã fix).
