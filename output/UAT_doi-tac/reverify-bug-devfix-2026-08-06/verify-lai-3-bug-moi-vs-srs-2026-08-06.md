# Kiểm lại 3 lỗi QA tự phát hiện — đối chiếu đặc tả + đo lại bằng cách khác

**Ngày:** 06/08/2026 · **Env:** `https://18.143.165.120.nip.io` · bản dựng **V1.0.8**
**Đặc tả:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`
**Lý do làm việc này:** khi log 3 dòng mới (365 `BCTK_QA02` · 366 `BCTK_QA03` · 367 `BCTK_QA04`) mới chỉ
làm 2/3 bước của quy trình bắt buộc — đã mở đúng file đặc tả đọc đúng số dòng, nhưng **chưa đo lại bằng
phương pháp thứ hai** để loại các cách giải thích khác. File này bù nốt bước đó.

**Kết luận chung: cả 3 đều là lỗi thật.** Trong đó **2 dòng đang mô tả hẹp hơn sự thật** (366 và 367) —
xem mục "Cần sửa lại nội dung đã ghi".

---

## 1. `BCTK_QA02` — bấm [Xem báo cáo] lần 2 làm hai nút Xuất bị mờ

**Giả thuyết ngược cần loại:** neo đặc tả cũ (`:1052`/`:1053`) chỉ nói về *điều kiện hiển thị*, mà hai nút
vẫn hiện — chỉ là mờ. Vậy có thể lập luận "không trái đặc tả".

**Đã loại bằng một neo chặt hơn** — tiêu chí nghiệm thu, không phải điều kiện hiển thị:

> `srs-fr-11-bao-cao.md:123` — **Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4
> Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`

Đặc tả nghiệm thu bằng hành vi "nhấn → tải file". Nút mờ thì **không nhấn được**, nên tiêu chí này không
thoả trong khi màn vẫn đang hiện đúng báo cáo. Kèm `:1052`/`:1053` ("Sau khi đã Xem báo cáo") thì điều kiện
để nút dùng được đã thoả rồi mà nút vẫn bị khoá.

**Đo lại bằng cách khác — loại giả thuyết "chỉ một loại báo cáo" và "chỉ một vai trò":**

| Lần đo | Loại báo cáo | Vai trò | Sau [Xem báo cáo] lần 1 | Sau lần 2 |
|---|---|---|---|---|
| 1 | BC Vụ việc đã tiếp nhận | CB Phê duyệt TW | dùng được | **mờ cả 2 nút** |
| 2 | BC Vụ việc theo thời gian | CB Phê duyệt TW | dùng được | **mờ cả 2 nút** |
| 3 (bổ sung) | BC Vụ việc đã hoàn thành | QTHT | dùng được | **mờ cả 2 nút** |

Lần 3 đo lúc 15:43, màn vẫn hiện đủ số liệu (Tổng vụ việc 18 · Thành công 3 · Tỷ lệ 16.7%) — tức không
phải "hết dữ liệu nên khoá nút". Bấm lần 3 không hồi phục; chỉ đổi bộ lọc hoặc tải lại trang mới hồi phục.

**Verdict: lỗi thật.** Chỉ cần bổ sung neo `:123` vào ô "Kết quả mong đợi" cho chặt.

---

## 2. `BCTK_QA03` — bảng theo người hỗ trợ có dòng "(Không xác định)"

**Giả thuyết ngược cần loại:** dữ liệu env hỏng — tài khoản đó vốn không có họ tên, nên báo cáo trả rỗng
là *đúng dữ liệu*, không phải lỗi phần mềm.

**Đã loại — người này có tên đầy đủ trong chính danh sách Người hỗ trợ của hệ thống:**

```
GET /api/v1/nguoi-ho-tro   → 1 bản ghi:
   mã          NHT-STP-AG-0001
   họ tên      "QA NHT An Giang UAT2"
   id          43e2b415-9edb-4e9d-bf5d-0fa5f30cdc65
   người dùng  acf00fb8-10a0-46f9-a79c-b6bc40f7372b   ← đúng mã mà báo cáo trả về kèm tên rỗng
```

Tra thêm hồ sơ tài khoản `acf00fb8-…` → **200**, `hoTen = "QA NHT An Giang UAT2"`, `username = nht_ag_uat2`,
`trangThai = HOAT_DONG`, vai trò có `NHT`. Vậy **tên tồn tại ở hai chỗ**, báo cáo vẫn trả rỗng.

Đối chiếu đặc tả:

> `:261` (FR-IX-03, output #5) — `theo_nht[] | structured | **Luôn** | {nht_id, ho_ten, so_vv, qua_han}`
> `:244` (FR-IX-03, bộ lọc #1) — `nht_id | identifier | N | **FK → NGUOI_DUNG**`

Đặc tả buộc phần theo người hỗ trợ **luôn** kèm `ho_ten`, và khoá tra cứu là người dùng. Bản ghi này thoả
mọi điều kiện đó mà vẫn ra rỗng.

**Dấu hiệu chỉ ra cùng một chỗ hỏng cho cả 2 triệu chứng:** bộ lọc "NHT phụ trách" có 42 mục và không mục
nào là người này; danh sách Người hỗ trợ chỉ có **1** người — chính là người này. Nghĩa là báo cáo và bộ lọc
đang tra "người hỗ trợ" từ một nguồn danh sách **khác** với danh sách Người hỗ trợ, nên người này rơi ra
ngoài ở cả hai chỗ. Lọc báo cáo theo đúng mã người này (`nhtId=acf00fb8-…`) vẫn trả `ten: ""` với
`tongVuViec: 2` — tức dữ liệu vụ việc có, chỉ mất tên.

**Verdict: lỗi thật, và nặng hơn mô tả đang ghi** — mô tả cũ để ngỏ khả năng "dữ liệu thiếu tên"; thực tế
tên có sẵn.

---

## 3. `BCTK_QA04` — lọc một đơn vị thì phần "Theo đơn vị" rỗng

**Giả thuyết ngược cần loại:** đây là chủ ý thiết kế — đã lọc về một đơn vị thì khỏi liệt kê lại đơn vị đó.

**Đã loại bằng đối chứng nội bộ sản phẩm.** Đo cùng lúc 5 loại báo cáo × 2 phạm vi (Năm 2026 · một đơn vị =
Cục Bổ trợ tư pháp vs Toàn quốc), đếm số dòng ở phần "Theo đơn vị":

| Loại báo cáo | Lọc 1 đơn vị | Toàn quốc | Đặc tả |
|---|---|---|---|
| BC Vụ việc đã tiếp nhận | **0 dòng** ❌ | 4 dòng | `:216` FR-IX-02 — `theo_don_vi[] … **Luôn**` |
| BC Vụ việc đang hỗ trợ | **0 dòng** ❌ | 4 dòng | `:262` FR-IX-03 — `theo_don_vi[] … **Luôn**` |
| BC Vụ việc đã hoàn thành | **0 dòng** ❌ | 3 dòng | `:305` FR-IX-04 — `theo_don_vi[] … **Luôn**` |
| BC Vụ việc theo thời gian | 1 dòng ✅ | 4 dòng | `:338` FR-IX-05 |
| BC Vụ việc theo đơn vị | 1 dòng ✅ | 4 dòng | FR-IX-11 |

Hai loại cuối gặp **đúng tình huống đó** và vẫn trả 1 dòng đúng đơn vị đang lọc. Vậy không thể là chủ ý
thiết kế — cùng một sản phẩm đang xử lý hai kiểu khác nhau cho cùng một tình huống, và 3 loại còn lại
trái chữ "Luôn" trong đặc tả.

Tổng vụ việc vẫn ra đúng ở cả hai phạm vi (38/55 · 18/25 · 15/18), nên **số liệu không sai** — chỉ mất phần
theo đơn vị. Giữ nguyên mức **nhẹ**.

**Verdict: lỗi thật, phạm vi rộng gấp 3 lần dòng đang ghi** (dòng 367 chỉ nêu BC Vụ việc đang hỗ trợ).

---

## 4. Cần sửa lại nội dung đã ghi trên bảng

| Dòng | Ô cần sửa | Vì sao |
|---|---|---|
| 365 `BCTK_QA02` | Kết quả mong đợi (thêm neo `:123`) · Kết quả thực tế (thêm lần đo thứ 3) | Neo hiện tại còn lỏng; đã có thêm bằng chứng |
| 366 `BCTK_QA03` | Mô tả · Kết quả mong đợi · Kết quả thực tế | Mô tả đang để ngỏ "dữ liệu thiếu tên" — thực tế tên có sẵn trong danh sách Người hỗ trợ |
| 367 `BCTK_QA04` | Tên chức năng · Mô tả · Kết quả mong đợi · Kết quả thực tế | Đang ghi 1 loại báo cáo, thực tế **3** loại; thiếu đối chứng 2 loại làm đúng |

Nội dung sửa: `note/BCTK_QA02-fields-sua.json` · `note/BCTK_QA03-fields-sua.json` ·
`note/BCTK_QA04-fields-sua.json` (bản `-fields.json` không có hậu tố là bản log lần đầu, giữ để đối soát).

## 5. ✅ Đã ghi lên bảng — 06/08/2026, sau khi người chủ bảng đồng ý

Hai chỗ vướng đã được gỡ:

1. `tools/sheet_fix_row_fields.py` được nới danh sách tab cho phép, thêm `"bug"` (kèm ghi chú lý do trong
   mã nguồn) — cùng kiểu `sheet_add_bug_row.py` đã allow-list tab này từ trước. Sửa vào công cụ đã
   commit, **không** viết script dùng-một-lần, **không** sửa tay trên bảng.
2. Người chủ bảng đồng ý cho ghi đè ô "Kết quả thực tế" của **ba dòng 365–367** (dòng QA tự tạo, nội dung
   trong đó là của QA). Không đụng ô "Kết quả thực tế" của bất kỳ dòng nào khác.

| Dòng | Số ô đã ghi | Ô nào |
|---|---|---|
| 365 `BCTK_QA02` | 2 | Kết quả mong đợi · Kết quả thực tế |
| 366 `BCTK_QA03` | 3 | Mô tả · Kết quả mong đợi · Kết quả thực tế |
| 367 `BCTK_QA04` | 7 | Tên chức năng · Mô tả · Điều kiện · Dữ liệu đầu vào · Các bước thực hiện · Kết quả mong đợi · Kết quả thực tế |

Chạy `--dry-run` trước từng dòng, guard "Mã TC phải khớp" đều qua (đúng dòng), ghi xong đọc lại khớp
100%. Đọc lại lần hai bằng đường khác (đọc thẳng bảng) xác nhận `Trạng thái = Fail`, `Dopai = bug`,
`Ảnh/vieo 1` **không bị đụng** ở cả 3 dòng. Nhật ký: `tools/sheet_fix_row_fields.log`.

**Còn một điểm chưa cân:** ô bằng chứng của dòng 367 vẫn là tệp Excel của **một** loại báo cáo, trong khi
nội dung dòng nay nói về **ba** loại. Số liệu ma trận 5 loại × 2 phạm vi đã lưu ở
`bug-reports/image/BCTK_QA04-ma-tran-5-loai-bao-cao-x-2-pham-vi.json` nhưng **chưa** tải lên Drive và
chưa gắn vào bảng — cần quyết có thêm ô bằng chứng thứ hai cho dòng đó hay không.
