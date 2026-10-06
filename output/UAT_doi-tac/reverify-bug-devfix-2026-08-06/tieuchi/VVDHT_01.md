Mã case: VVDHT_01 (tab `bug` dòng 183)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (`HTPLDN · V1.0.8`) — đo 06/08/2026 14:04

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có (chưa từng qua vòng soát nội bộ).

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc đang hỗ trợ** (SCR-IX-01, `loai=vu-viec-dang-ho-tro`). **1 vế duy nhất:**
*"Đơn vị có dữ liệu thống kê nhưng khi chọn **người hỗ trợ** hệ thống thông báo 'Không có dữ liệu báo cáo
cho kỳ và đơn vị đã chọn'."*

**Bằng chứng đã mở xem:** `../partner-evidence/VVDHT_01.webm` (73 giây, đã trích 19 frame về
`../frames/VVDHT_01/`, xem tới khoảnh khắc lỗi).

| Frame | Thấy gì |
|---|---|
| `t060.22s.jpg` | Bản dựng **V1.0**, vai trò **Cán bộ NV Trung ương `CB_NV_TW`** (BTP·TW) — **đúng tác nhân**. Loại BC `BC Vụ việc đang hỗ trợ`, Kỳ **Năm** 01/01/2026–31/12/2026, Đơn vị **Cục Bổ trợ tư pháp – BTP-TW**, **NHT phụ trách = `Race test`**, Mức SLA để trống. Vùng kết quả: ảnh empty-state + dòng **"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"**. Nút `Xuất Excel` / `Xuất PDF` bị **làm mờ**. |
| `t072.25s.jpg` | Cùng màn, cùng bộ lọc, đổi **NHT phụ trách = `TVV BUG dup test`** → **vẫn** ra đúng câu "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn". |

**Điểm mấu chốt bằng chứng KHÔNG cho biết:** hai NHT đối tác chọn (`Race test`, `TVV BUG dup test` — tên
nghe như tài khoản rác) **có thật sự đang phụ trách vụ việc nào không**. Video không mở màn Vụ việc để
đối chiếu. ⇒ Đây là GAP phải tự dựng tiền đề mới đóng được (mục 3 + mục 5).

**TKM phản hồi lần 1 (28/7):** *"Lỗi chưa được fix"* — không kèm ảnh mới, không nêu đã chọn NHT nào.

---

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.

**FR-IX-03: BC Vụ việc đang hỗ trợ (UC126)**

- `:234` (Mô tả) → `Báo cáo snapshot vụ việc đang xử lý tại thời điểm query, phân theo mức SLA, người hỗ trợ, đơn vị.`
- `:236` (Tác nhân) → `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`
- `:244` (Input đặc thù) → `| 1 | nht_id | identifier | N | FK → NGUOI_DUNG | — | Chọn |` — cột "Bắt buộc" = **N** ⇒ bộ lọc **tùy chọn**
- `:247` (Công thức) → `Đếm số vụ việc đang xử lý (snapshot tại thời điểm query), theo phạm vi đơn vị`
- `:249` (Dimensions) → `Đơn vị, NHT phân công, SLA (bình thường / sắp hết hạn / quá hạn / quá hạn nghiêm trọng)`
- `:261` (Output đặc thù) → `| 5 | theo_nht[] | structured | Luôn | {nht_id, ho_ten, so_vv, qua_han} |`

**Error / empty state:**

- `:113` (Error Handling chung E3) → `| E3 | Không có dữ liệu | INF-RPT-01 | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | INFO |`
- `:1057` (SCR-IX-01 thành phần #13) → `content | Empty state | empty | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | — | Khi không có dữ liệu`
- `:125` (AC chung) → `**Given** không có dữ liệu **When** tạo BC **Then** hiển thị "Không có dữ liệu"`

⇒ Câu thông báo đối tác gặp **chính là câu đặc tả quy định cho trường hợp KHÔNG CÓ DỮ LIỆU**. Nó chỉ là
lỗi khi **thật sự có dữ liệu** mà hệ thống vẫn trả empty. Đây là trục chấm của case này.

**IM LẶNG về:**
- Dropdown "NHT phụ trách" liệt kê **những ai** — mọi tài khoản, hay chỉ NHT đang phụ trách ≥1 vụ việc
  trong phạm vi + kỳ đã chọn. `:244` chỉ ghi `FK → NGUOI_DUNG`, không nói điều kiện lọc danh sách.
- Có phải hiện cảnh báo riêng khi người dùng chọn một NHT không có vụ việc nào hay không.

---

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw` / `Test@1234`** (`CB_NV_TW`, cấp TW) — **trùng khít vai trò đối tác**
  đã dùng trong video.
- Màn: `https://18.143.165.120.nip.io/bao-cao` → Loại báo cáo **"BC Vụ việc đang hỗ trợ"**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Cục Bổ trợ tư pháp – BTP-TW**,
  Mức SLA để trống.
- **Dữ liệu tiền đề bắt buộc tự dựng** (bằng chứng đối tác không cho biết ai là "đúng người"):
  1. Xác định bằng **đường thứ hai** (gọi thẳng API danh sách vụ việc / báo cáo khi **không** lọc NHT)
     ra tập NHT đang phụ trách vụ việc trong phạm vi + kỳ, kèm số vụ việc từng người.
  2. Chốt **NHT-A** = một người có **≥1** vụ việc đang xử lý (đọc từ `theo_nht[]`).
  3. Chốt **NHT-B** = một người **có mặt trong dropdown** nhưng **0** vụ việc đang xử lý.
  4. Nếu không tồn tại NHT-A → **seed** một vụ việc và phân công cho một NHT qua luồng chuẩn, khai rõ
     bản ghi nào / đổi gì / env nào vào báo cáo.

---

## 4. Tiêu chí chấm

✅ **PASS khi ĐỦ cả 4:**

1. **Không lọc NHT** (để trống), cùng kỳ + đơn vị mục 3 → báo cáo ra dữ liệu, đọc được tổng vụ việc đang
   xử lý và phân rã theo người hỗ trợ (`theo_nht[]`, `:261`).
2. **Lọc đúng NHT-A** (người có ≥1 vụ việc, xác định ở mục 3) → báo cáo **ra dữ liệu**, **không** hiện
   câu `"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"`.
3. Số vụ việc trả về khi lọc NHT-A **bằng đúng** số vụ việc của chính người đó trong phân rã
   `theo_nht[]` ở bước 1 (hai phép đo phải khớp nhau).
4. Phủ đủ M dạng ở mục 5 — kết quả nhất quán trên **mọi** NHT-A đã thử (không phải chỉ 1 người may mắn).

❌ **FAIL nếu:** lọc **NHT-A** (đã chứng minh có ≥1 vụ việc đang xử lý trong đúng kỳ + đơn vị đó) mà báo
cáo vẫn hiện empty state / không ra dữ liệu · hoặc số khi lọc NHT-A lệch số của người đó trong
`theo_nht[]` · hoặc bước 1 (không lọc) ra dữ liệu nhưng **mọi** NHT-A đều ra empty.

⛔ **KHÔNG được chấm Fail vì:**
- Chọn **NHT-B** (người không phụ trách vụ việc nào) mà ra `"Không có dữ liệu báo cáo cho kỳ và đơn vị đã
  chọn"` — đó là **đúng đặc tả** `:113` / `:1057` / `:125`.
- Dropdown NHT có liệt kê cả người không có vụ việc — `:244` **im lặng** về điều kiện lọc danh sách này.
  Nếu đây là điểm bất đồng còn lại sau khi đo → đẩy sang **cần BA**, không chấm Fail.
- Nút Xuất Excel/PDF bị làm mờ khi chưa có dữ liệu — `:1052`/`:1053` quy định nút chỉ dùng được **sau khi
  đã "Xem báo cáo"**.

---

## 5. Dạng dữ liệu phải phủ

**M = 4 dạng NHT**, để phân biệt "hệ thống lọc sai" với "người được chọn vốn không có việc":

| # | Dạng | Kỳ vọng theo đặc tả |
|---|---|---|
| 1 | **Không lọc NHT** (để trống) | Ra dữ liệu + phân rã `theo_nht[]` |
| 2 | **NHT-A₁** — có ≥1 vụ việc đang xử lý | Ra dữ liệu, số khớp `theo_nht[]` |
| 3 | **NHT-A₂** — một NHT khác cũng có ≥1 vụ việc (nếu tồn tại) | Ra dữ liệu, số khớp `theo_nht[]` |
| 4 | **NHT-B** — có trong dropdown, 0 vụ việc | Empty state — đây là ĐÚNG, dùng làm đối chứng âm |

**Nguồn xác định M:** ① `:249` Dimensions nêu rõ chiều "NHT phân công" · ② `:261` output `theo_nht[]` liệt
kê từng người kèm `so_vv` ⇒ chính danh sách này quyết định ai là NHT-A, ai là NHT-B · ③ dropdown "NHT phụ
trách" ngay trên màn SCR-IX-01.

Nếu môi trường chỉ có **1** NHT có vụ việc → dạng 3 bỏ, ghi rõ lý do vào mục 6; **không** được bỏ dạng 2
hoặc dạng 4 (thiếu dạng 4 thì không phân biệt được lỗi lọc với dữ liệu rỗng thật).

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Cán bộ NV Trung ương `CB_NV_TW`** (BTP·TW) — đúng tác nhân `:236` | `cbnv_tw` (`CB_NV_TW`, BTP·TW) — **trùng khít vai trò + cấp đối tác**, đo trên chính giao diện | **Không** |
| Entity + trạng thái | VU_VIEC **đang xử lý** — snapshot tại thời điểm query (`:247`), không phụ thuộc kỳ theo cách của các BC khác | Cùng loại: vụ việc đang xử lý. Tổng thực đo **14** (BTP-TW) · **19** (Toàn quốc), `Thời điểm tạo 06/08/2026 14:04` | **Không** |
| Dữ liệu tiền đề | Đối tác khẳng định "đơn vị CÓ dữ liệu" nhưng **video không chứng minh** 2 NHT được chọn có vụ việc nào không → chính là GAP phải tự dựng | **Đã tự dựng bằng đường thứ hai** (`theo_nht[]` khi không lọc): **NHT-A₁** = `QA TVV Seed28 Active` (4 vụ, 2 quá hạn — có trong dropdown); **NHT-A₂** = `acf00fb8…` (1 vụ, chỉ thấy ở phạm vi Toàn quốc); **NHT-B** = `QA Reverify TVV 0805`, `QA UAT DKTGMLTVV 13 V108`, `Chuyên gia UAT QLNDTVVCG 38` (0 vụ). Hai tên đối tác chọn (`Race test`, `TVV BUG dup test`) **không tồn tại** trong 42 tư vấn viên của env này | **Không** — GAP đóng bằng dữ liệu thực đo, không suy luận |
| Input / filter / giá trị nhập | Kỳ `NAM`, 01/01/2026–31/12/2026, `donViId=00000000-0000-4000-8000-000000000001` (BTP-TW), Mức SLA trống. **NHT phụ trách**: `Race test` (t060) rồi `TVV BUG dup test` (t072) | Giữ nguyên kỳ + khoảng + đơn vị + Mức SLA trống của đối tác; **thêm nhánh đối tác không thử**: để trống NHT. Ô NHT lần lượt: (trống) → NHT-A₁ → NHT-B | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | Đối tác thử **2 NHT**, cả 2 đều là tài khoản tên "test"; **không** thử nhánh để trống NHT, **không** thử NHT có việc thật | Phủ đủ **M = 4**: ① không lọc → **14**, có bảng "Thống kê theo người hỗ trợ" · ② NHT-A₁ → **4**, KHÔNG empty state, khớp đúng số của người đó ở ① · ③ NHT-A₂ → **1**, khớp `theo_nht[]` · ④ 3 NHT-B → empty state đúng câu đặc tả, nút Xuất mờ | **Không** |

**Sửa đổi giữa chừng (14:10):** dạng ③ phải **nới đơn vị** từ BTP-TW lên **Toàn quốc** vì trong phạm vi BTP-TW
chỉ có **1** NHT đang phụ trách vụ việc. Giữ nguyên vai trò, chỉ nới phạm vi dữ liệu — mục 5 đã cho phép bỏ
dạng ③ trong tình huống này, nhưng nới được thì đo còn hơn bỏ. Khai rõ ở đây theo yêu cầu của flow.

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict.

**Phát hiện mới trên chính màn này, KHÔNG kéo verdict case** (xử riêng theo §Phát hiện mới):
① `theo_nht[]` trả về một mục có `ten` **rỗng** (`acf00fb8…`) — trái `:261` đòi trường `ho_ten`. ② Chính người
đó **không có trong dropdown "NHT phụ trách"** (nguồn `/tu-van-viens`, 42 mục) — tức một người đang phụ trách
vụ việc lại không chọn được để lọc.
> **Đính chính 14:42 (đo lại trên giao diện):** ban đầu tôi ghi mục này hiện thành "một dòng trắng". Kiểm lại
> ở phạm vi Toàn quốc thì giao diện **có** thế chỗ bằng nhãn **"(Không xác định)"** (ảnh
> `../bug-reports/image/BCTK_QA03-nguoi-ho-tro-khong-xac-dinh.png`) — dữ liệu máy chủ vẫn trả `ten: ""`.
> Bản chất lỗi không đổi (không định danh được người đang phụ trách), nhưng mô tả phải đúng cái người dùng thấy.

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-dang-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001`
- Trạng thái entity: vùng kết quả rỗng (empty state), nút Xuất bị làm mờ; NHT được chọn: `Race test`, `TVV BUG dup test`
- Vai trò + env + bản dựng: **CB_NV_TW** · `htpldn-uat.ospgroup.vn` · **HTPLDN V1.0** · quay 15/07/2026 16:53

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0; đợt này đo trên
`18.143.165.120.nip.io` bản ghi ở đầu file ⇒ Pass ở đây là **Pass tạm**. Ngoài ra bản dựng đối tác dùng
là bản **cũ nhất** trong 6 case đợt này (V1.0, 15/07), trong khi TKM khẳng định 28/7 vẫn lỗi mà không kèm
ảnh mới — nêu rõ điều này trong báo cáo nếu verdict là Pass.
