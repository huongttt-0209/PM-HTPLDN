# Audit — TPDBC_02 (Resolved)

**Chức năng:** Trình phê duyệt báo cáo (FR-VI-08, Tab Báo cáo).
**Đối tác báo:** Nút "Trình phê duyệt" hiện dù đợt sai state / báo cáo chưa lưu.
**Verdict:** **Resolved** — không tái hiện trên bản hiện tại; nút được gate theo state, chỉ hiện khi đợt tới giai đoạn báo cáo và báo cáo đã tự lưu (Dự thảo). Đối tác có bằng chứng ⇒ không Reject, chuyển Verify=Resolved (khớp quy ước 42 dòng sheet: P=Reject + Verify=Resolved).

## Re-verify LIVE 2026-07-23 (Chrome DevTools MCP · cbnv_hn · env nip.io)

Chạy lại đủ luồng để kiểm cả 2 vế claim đối tác ("nút hiện ở SAI state" + "báo cáo CHƯA lưu"):

| Bước | Đợt / State | Quan sát tab Báo cáo | Ảnh |
|---|---|---|---|
| Test âm 1 | DG-20260720-0004 · **Thực hiện** | "Chưa hoàn thành đánh giá" — **KHÔNG có** nút Trình phê duyệt | `relive-01-thuchien-no-button.png` |
| Test âm 2 | DG-20260720-0003 · **Đang đánh giá** | "Chưa hoàn thành đánh giá" — **KHÔNG có** nút | (cùng dạng, đã xác nhận qua snapshot) |
| Test dương | DG-20260720-0003 · **Đã đánh giá → Lập báo cáo** (sau "Hoàn tất chấm điểm") | Báo cáo BCDG-20260723-0002 **tự tạo, Trạng thái "Dự thảo"** + nút **"Trình phê duyệt" HIỆN** | `relive-02-baocao-button-present-draft-saved.png` |
| Trình PD | click Trình phê duyệt | Hộp xác nhận "Trình phê duyệt báo cáo? Báo cáo sẽ được gửi cho cán bộ phê duyệt." | `relive-03-confirm-dialog.png` |
| Kết quả | xác nhận | Đợt → **Chờ phê duyệt**, báo cáo → **Chờ phê duyệt**, nút biến mất (gated lại) | `relive-04-submitted-chophe-duyet.png` |

**Kết luận re-verify:** Nút "Trình phê duyệt" được UI gate chặt theo state — VẮNG ở Thực hiện + Đang đánh giá, chỉ HIỆN khi đợt tới giai đoạn báo cáo, và **khi hiện thì báo cáo ĐÃ tự lưu (Dự thảo)** rồi biến mất sau khi trình. Cả 2 vế claim đối tác đều bị phủ định. → **Resolved** (không tái hiện, chức năng đúng).

> ⚠️ **Mutation dữ liệu:** re-verify đã đẩy đợt **DG-20260720-0003** từ "Đang đánh giá" → "Chờ phê duyệt" (hoàn tất chấm điểm 1/1 VV + trình PD). Đợt này gốc là seed "kiem thu CVVDG_03 THDG_03 THDG_05 TPDBC_03" — nếu các case đó cần lại state "Đang đánh giá" phải seed đợt mới.

## Điều kiện tái hiện
- Account `cbnv_hn` (CB_NV_DP Hà Nội). Đợt DGHQ-B1-20260720, tab Báo cáo.

## Quan sát
- Sau khi hoàn tất chấm điểm, đợt tự chuyển sang **BAO_CAO** và bản báo cáo nháp (BCDG-20260720-0001, trạng thái DU_THAO) được tạo/lưu **tự động**.
- API xác nhận: `GET /api/v1/ke-hoach-danh-gias/{id}` → `trangThai = "BAO_CAO"`; `GET .../bao-cao` → record tồn tại, `trangThai = "DU_THAO"`.
- Nút "Trình phê duyệt" chỉ hiện ở đúng trạng thái BAO_CAO này (đúng precondition FR-VI-08).
- Các ô Nội dung / Nhận xét tổng thể / Kiến nghị để trống là hợp lệ — SRS FR-VI-07 để các ô này **không bắt buộc**.
- Bấm nút → hộp xác nhận "Trình phê duyệt báo cáo? Báo cáo sẽ được gửi cho cán bộ phê duyệt" → xác nhận → toast success "Đã trình phê duyệt", đợt chuyển CHO_PHE_DUYET.

## Đối chiếu SRS
- FR-VI-08 Preconditions (`srs-fr-08-danh-gia.md:629-632`): "Đợt ở trạng thái BAO_CAO" + "BC đã được lưu" — **cả hai đều thỏa** khi nút hiện.
- Không có căn cứ nào cho thấy nút hiện ở trạng thái sai hoặc khi báo cáo chưa có record.

## Kết luận
Không tái hiện "nút hiện sai state / báo cáo chưa lưu". → **Resolved**.

**Evidence:** chuỗi live 2026-07-23 `relive-01`…`relive-04` (bảng trên). Ảnh cũ `trinh-pd-thanh-cong.png` chỉ show màn báo cáo đã hoàn thành (không rõ hộp xác nhận/toast) — đã thay bằng chuỗi live đầy đủ.
