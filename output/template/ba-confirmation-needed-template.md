# BA confirmation needed — [PHẠM VI / ĐỢT] — [YYYY-MM-DD]

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `bug-report-*.md`).

> **2 dạng case — chọn đúng bộ mục cho từng TC:**
> - **Dạng A — QA đã có kết luận, cần BA phản hồi đối tác.** Dùng khi đối chiếu SRS xong QA khẳng định được (vd expected của đối tác sai so với SRS, hoặc web đúng SRS). Bộ mục: *Bối cảnh → Đối chiếu SRS → Citation → Kết quả verify UI → Kết luận QA → Nội dung đề xuất BA phản hồi đối tác*.
> - **Dạng B — SRS tự mâu thuẫn, QA không tự chốt được.** Dùng khi 2 chỗ trong SRS nói khác nhau, phải BA chọn source truth. Bộ mục: *Bối cảnh → Kết quả verify UI → Điểm mâu thuẫn trong SRS → Câu hỏi cần BA xác nhận → Đề xuất QA tạm thời (kèm nhánh nếu-thì)*.
> - Xoá phần dạng không dùng cho từng TC. Một file có thể chứa nhiều TC thuộc cả 2 dạng.

> **Quy tắc citation (BẮT BUỘC):** mọi khẳng định SRS phải trỏ `path/tới/file-srs.md:LINE` — mở file verify số dòng thực, KHÔNG dùng số dòng từ trí nhớ.
> - **Nguồn DUY NHẤT được quote số dòng (chốt 2026-07-25):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (vd `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1113`).
> - **KHÔNG quote số dòng từ `input/srs-update-2026-5-5/`** — bản này là trích của BA khi viết phiếu UAT, chỉ để tham chiếu; lệch cả số dòng (~+5..+14) lẫn nội dung so với bản chốt. Quote nhầm bản → bug/BA-question invalid.
> - Module chưa cover trong bản chốt → fallback `input/srs-v3/` + ghi rõ version dùng ngay trong mục Citation.
> - Xem CLAUDE.md §Quick reference dòng "🔴 SRS — NGUỒN DUY NHẤT".

---

<!-- =========================================================================
     DẠNG A — QA đã kết luận, cần BA phản hồi đối tác
     (copy block dưới cho mỗi TC thuộc dạng A; xoá comment này sau khi điền)
========================================================================= -->

## [MÃ_TC] — [Tiêu đề ngắn: điểm khác biệt giữa expected của đối tác và SRS]

**Bối cảnh testcase**

- Dòng Excel: [số dòng], mã TC `[MÃ_TC]`.
- Nội dung kiểm tra: [role] [thao tác / màn hình đang kiểm tra].
- Expected trong file UAT:
  - [gạch đầu dòng expected của đối tác, quote nguyên trạng thái / nút / hành vi].
  - [gạch đầu dòng tiếp theo nếu có].
- Actual đối tác ghi: [đối tác quan sát gì].

**Đối chiếu SRS v3.5**

- [khẳng định SRS 1 — mô tả yêu cầu nghiệp vụ, KHÔNG prescribe implementation].
- [khẳng định SRS 2].
- [khẳng định SRS 3 — nêu rõ điều kiện enable/disable/cấm nếu liên quan state].

**Citation**

- `[path/tới/srs-fr-NN-x.md]:[LINE]`
- `[path/tới/srs-fr-NN-x.md]:[LINE]`

**Kết quả verify UI hiện tại**

- Verify lại ngày [DD/MM/YYYY] qua [Chrome DevTools MCP / method], dùng tài khoản UAT `[username]/[role]`.
- Mở URL `[URL đã test]`.
- [quan sát 1: UI hiển thị gì].
- [quan sát 2: record / trạng thái / nút quan sát được].
- [quan sát 3: đối chiếu quan sát với SRS → đúng/sai chỗ nào].
- Evidence: `[screenshots/<tên-ảnh>.png]`

**Kết luận QA**

- `[MÃ_TC]` [không phải bug theo SRS v3.5 / là bug — nêu rõ].
- [web hiện tại đúng/sai SRS ở điểm nào].
- [nếu expected đối tác sai → liệt kê từng điểm sai]:
  - [điểm sai 1];
  - [điểm sai 2].

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị [cập nhật expected của `[MÃ_TC]` theo SRS v3.5 / xác nhận hướng xử lý]:

- [đề xuất cụ thể 1].
- [đề xuất cụ thể 2].
- Verdict QA đề xuất: `[Không phải bug theo SRS / Cần BA xác nhận / Vẫn lỗi — owner: Dev FE|BE]`, [gửi Dev xử lý / không gửi Dev].

---

<!-- =========================================================================
     DẠNG B — SRS tự mâu thuẫn, cần BA chốt source truth
     (copy block dưới cho mỗi TC thuộc dạng B; xoá comment này sau khi điền)
========================================================================= -->

## [MÃ_TC] (và [MÃ_TC phụ nếu chung 1 vấn đề]) — [Tiêu đề ngắn màn hình / tab đang tranh cãi]

**Bối cảnh testcase**

- Dòng Excel: [số dòng], mã TC `[MÃ_TC]`.
- [Dòng Excel: [số dòng], mã TC `[MÃ_TC phụ]` — nếu gộp nhiều TC cùng vấn đề].
- Nội dung kiểm tra: [role] [thao tác / màn hình đang kiểm tra].
- Expected trong file UAT: [tóm tắt expected đối tác].

**Kết quả verify UI hiện tại**

- Mở đúng [tab / màn hình] trên UI, URL là `[URL]`.
- [quan sát 1: UI thực tế hiển thị gì / trống hay có data].
- [quan sát 2: cột / nút / action quan sát được].
- [quan sát 3: điểm nào đang phù hợp SRS].
- Evidence: `[screenshots/<tên-ảnh>.png]`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo [FR-... / mục A], [SRS nói hướng 1]:
   - [chi tiết 1]
   - [chi tiết 2]

   Citation:
   - `[path/tới/srs-fr-NN-x.md]:[LINE]`
   - `[path/tới/srs-fr-NN-x.md]:[LINE]`

2. Nhưng [SCR-... / mục B] lại [nói hướng 2 khác]:
   - [chi tiết 1]
   - [chi tiết 2]

   Citation:
   - `[path/tới/srs-fr-NN-x.md]:[LINE]`
   - `[path/tới/srs-fr-NN-x.md]:[LINE]`

**Câu hỏi cần BA xác nhận**

[Nêu 1 câu hỏi rõ ràng về đúng màn hình / tab / TC đang xét]. Cần được hiểu theo hướng nào?

1. **[Hướng 1 — theo nguồn A]:** [mô tả hành vi mong đợi nếu chọn hướng 1].
2. **[Hướng 2 — theo nguồn B]:** [mô tả hành vi mong đợi nếu chọn hướng 2].

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho [`[MÃ_TC]` (và `[MÃ_TC phụ]`)]: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: [UI hiện tại là `Vẫn lỗi` / `Đúng`], owner dự kiến `[Dev FE / Dev BE / QA update expected]`.
- Nếu BA chọn hướng 2: [UI hiện tại có thể không phải lỗi / cần cập nhật lại expected testcase cho khớp SRS]. [Điểm nào đang đúng].
