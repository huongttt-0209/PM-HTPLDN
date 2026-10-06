# Bảng đối chiếu điều kiện — DGTVV_02 (row 78)

**Claim đối tác:** Khu vực tổng hợp điểm đánh giá (đầu thẻ) hiển thị thang 1–10 (8.3/10), trong khi tài liệu yêu cầu thang 1–5.

**Evidence đã xem:** `partner-evidence/DGTVV_02.jpg` (full-res) — màn Chi tiết TVV `06748bb5-e5d4-453f-9490-f07b17fd0a4a`, tab "Đánh giá", role CB_NV_TW. Frame chứa lỗi: header thẻ "8.3/10" + thanh 10 sao; 3 tiêu chí "Chuyên môn 4.5/10 · Thái độ 5.0/10 · Đúng hạn 4.0/10"; bảng đánh giá render 10 sao/tiêu chí.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw` — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Entity + trạng thái (state machine) | Tư vấn viên, trạng thái "Đang hoạt động", đã công nhận | Tư vấn viên `TVV-BTP-TW-0002` (id 98cfd963-3cd3-4c8a-bfa9-625460824d6d), trạng thái "Đang hoạt động", ngày công nhận 12/07/2026 | Không |
| Dữ liệu tiền đề | TVV đã có đánh giá (2 đánh giá) → khối tổng hợp hiển thị điểm | TVV đã có đánh giá (1 đánh giá, điểm 4.0) → khối tổng hợp hiển thị điểm (không rơi vào trạng thái rỗng "—/5") | Không |
| Input / filter | — (bug hiển thị, không phụ thuộc input) | — | Không |

**Kết luận:** 0 GAP → đủ điều kiện chốt verdict.

## Cổng 3 — SRS vs web (dạng gạch đầu dòng)

- **SRS** `srs-fr-04-chuyen-gia-tvv.md:1570` — SCR-IV-03 cell 23 tab "Đánh giá": "(a) Khối tổng hợp: số lớn **4.5/5** + **5 sao** + ({N} đánh giá); (b) 3 thanh tiến trình: Chuyên môn, Thái độ, Đúng hạn (**trung bình 1–5** mỗi tiêu chí)".
  **Web:** Khối tổng hợp "**4.0/5**" + **5 sao** + "(1 đánh giá)"; 3 thanh tiến trình Chuyên môn **4.0/5** · Thái độ **4.0/5** · Đúng hạn **4.0/5** → ✅ Đủ.
- **SRS** `srs-fr-04-chuyen-gia-tvv.md:1541` (SCR-IV-03 cell 3 header thẻ: "Điểm đánh giá trung bình (sao)") + `:1445` ("Ví dụ: 4.5/5 + 5 sao").
  **Web:** Header thẻ "**4.0/5**" + widget đúng **5 sao** (a11y tree: 5 radio "star") → ✅ Đủ.
- **SRS** `srs-fr-04-chuyen-gia-tvv.md:703-706` — FR-IV-09 (UC47): 3 điểm thang 1–5, star-rating 5 sao.
  **Web:** Bảng danh sách đánh giá render widget **5 sao** mỗi tiêu chí (`.ant-rate` = 5 `li` × 4 widget) → ✅ Đủ.

**Không tái hiện** hành vi đối tác báo (thang 1–10). Web đúng SRS → `Reject`.

**Artifact quan sát:** `reverify-audit/DGTVV_02/web-tab-danhgia-thang-1-5-va-5-sao.png` (full-res, loại claim = Hiển thị/render — ảnh đúng phần tử tranh chấp: khối tổng hợp + 3 thanh tiêu chí + bảng đánh giá).
