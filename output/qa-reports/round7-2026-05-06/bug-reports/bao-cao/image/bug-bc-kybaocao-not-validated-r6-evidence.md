# Evidence — BUG-BC-KYBAOCAO-NOT-VALIDATED (R6 2026-05-11 17:41:09, account `cb_nv_tw_08`)

> Capture method: `mcp__chrome-devtools__evaluate_script` chạy 7 biến thể `fetch('/api/v1/bao-cao/hoi-dap?...')` với khác giá trị `kyBaoCao` trong cùng session `role-cb_nv_tw_08-r6` để loại trừ scope/auth variance.

## SRS contract (srs-v3/srs-fr-11-bao-cao.md §Input chung)

Line 67:
```
| 1 | ky_bao_cao | text | Y | TUAN / THANG / QUY / NAM / KHOANG | — | Chọn |
```

Line 1194 (validation table):
```
| 5 | ky_bao_cao | text | Y | CHECK IN ('TUAN','THANG','QUY','NAM','KHOANG') | — | Kỳ |
```

→ Spec rõ: `kyBaoCao` **required (Y)** + enum `{TUAN, THANG, QUY, NAM, KHOANG}`. BE phải:
1. Reject 422 nếu missing.
2. Reject 422 nếu giá trị ngoài enum.
3. Aggregate output `theoKy` khác nhau theo từng giá trị enum.

## Quan sát BE behavior R6

| Test variant | URL query (rút gọn) | status | tongHoiDap | theoKy keys | Verdict |
|--------------|---------------------|:------:|-----------:|-------------|---------|
| Missing | `?tuNgay=2026-01-01&denNgay=2026-12-31` (KHÔNG có kyBaoCao) | 200 | 26 | `["2026-05", null]` | ❌ phải 422 |
| Empty | `?kyBaoCao=&tuNgay=...&denNgay=...` | 200 | 26 | `["2026-05", null]` | ❌ phải 422 |
| Invalid token | `?kyBaoCao=INVALID_KY&...` | 200 | 26 | `["2026-05", null]` | ❌ phải 422 |
| Random string | `?kyBaoCao=XYZ&...` | 200 | 26 | `["2026-05", null]` | ❌ phải 422 |
| Valid NGAY (không in enum) | `?kyBaoCao=NGAY&...` | 200 | 26 | `["2026-05", null]` | ❌ phải 422 (NGAY ngoài enum SRS) |
| Valid TUAN (in enum) | `?kyBaoCao=TUAN&...` | 200 | 26 | `["2026-05", null]` | ⚠️ status đúng nhưng theoKy KHÔNG aggregate theo tuần |
| Valid QUY (in enum) | `?kyBaoCao=QUY&...` | 200 | 26 | `["2026-05", null]` | ⚠️ status đúng nhưng theoKy KHÔNG aggregate theo quý |
| Valid NAM (in enum) | `?kyBaoCao=NAM&...` | 200 | 26 | `["2026-05", null]` | ⚠️ giả sử "2026-05" là sai, phải `["2026"]` |
| **No dates** (control) | `?` (không có tuNgay/denNgay) | **422** | — | — | ✅ validation OK cho tuNgay/denNgay |

→ **Cả 8/8 variant kyBaoCao trả response IDENTICAL** (cùng `tongHoiDap=26`, cùng breakdown `theoLinhVuc` 5 dòng, cùng `theoDonVi` 3 đơn vị, cùng `theoKy` 2 entry `2026-05` + `null`).

→ BE hoàn toàn **ignore** param `kyBaoCao`. Aggregation `theoKy` hardcode chia theo tháng (chỉ có "2026-05" + null cho HD chưa có tháng) bất kể giá trị `kyBaoCao` nhập vào.

→ Control test no-dates 422 confirm BE có validation layer cho `tuNgay/denNgay` nhưng **bỏ qua hoàn toàn** validation cho `kyBaoCao` cùng request.

## So sánh với SRS Output spec

Line 93:
```
| 2 | ky_bao_cao | text | Luôn | Kỳ đã chọn |
```

BE response KHÔNG có field `kyBaoCao` trong output `data` (chỉ có `tongHoiDap, daTraLoi, theoLinhVuc, theoDonVi, theoKy`). Vi phạm Output spec luôn.

## Reproduction script

```js
const get = async (url) => {
  const r = await fetch(url, { credentials: 'include' });
  return { status: r.status, body: await r.json() };
};
const base = '/api/v1/bao-cao/hoi-dap?tuNgay=2026-01-01&denNgay=2026-12-31';
console.table({
  missing:  (await get(base)).body?.data,
  empty:    (await get(`${base}&kyBaoCao=`)).body?.data,
  invalid:  (await get(`${base}&kyBaoCao=INVALID_KY`)).body?.data,
  random:   (await get(`${base}&kyBaoCao=XYZ`)).body?.data,
  ngay:     (await get(`${base}&kyBaoCao=NGAY`)).body?.data,
  tuan:     (await get(`${base}&kyBaoCao=TUAN`)).body?.data,
  thang:    (await get(`${base}&kyBaoCao=THANG`)).body?.data,
  quy:      (await get(`${base}&kyBaoCao=QUY`)).body?.data,
  nam:      (await get(`${base}&kyBaoCao=NAM`)).body?.data,
  khoang:   (await get(`${base}&kyBaoCao=KHOANG`)).body?.data,
  no_dates: await get('/api/v1/bao-cao/hoi-dap')  // 422 control
});
```

Expected khi đã fix:
- Missing/empty/invalid/random/NGAY → 422 `ERR-VAL-SYS-00-01` `{field: "kyBaoCao", message: "kyBaoCao must be one of TUAN, THANG, QUY, NAM, KHOANG"}`.
- TUAN: `theoKy` keys định dạng tuần (vd `"2026-W19"`).
- THANG: `theoKy` keys định dạng tháng (vd `"2026-05"`).
- QUY: `theoKy` keys định dạng quý (vd `"2026-Q2"`).
- NAM: `theoKy` keys định dạng năm (vd `"2026"`).
- KHOANG: `theoKy` aggregation theo khoảng tự chọn.

## Phân tích root cause (giả thuyết)

1. **Controller `/bao-cao/hoi-dap` không decorate `@IsEnum`** trên field `kyBaoCao` của DTO. Validation pipeline class-validator bỏ qua.
2. **Service aggregation logic hardcode** chia theo tháng (`GROUP BY DATE_TRUNC('month', ngay_tao)`) thay vì switch case theo enum `kyBaoCao`.
3. **DTO Output type** thiếu field `kyBaoCao` echo lại theo Output spec line 93.

## Scope test — 12 BC sub-route với `kyBaoCao=INVALID`

| BC | Endpoint | status | Verdict |
|----|----------|:------:|---------|
| BC-001 Hỏi đáp PL | `/bao-cao/hoi-dap` | **200** | ❌ silently accept (bug) |
| BC-002 VV tiếp nhận | `/bao-cao/vu-viec-tiep-nhan` | 422 | ✅ validate đúng |
| BC-003 VV đang HT | `/bao-cao/vu-viec-dang-ho-tro` | 422 | ✅ |
| BC-004 VV hoàn thành | `/bao-cao/vu-viec-hoan-thanh` | 422 | ✅ |
| BC-006 Lớp ĐT đang DR | `/bao-cao/lop-dao-tao-dang-dien-ra` | 422 | ✅ |
| BC-007 Lớp ĐT đã DR | `/bao-cao/lop-dao-tao-da-dien-ra` | 422 | ✅ |
| BC-008 Chất lượng ĐT | `/bao-cao/chat-luong-dao-tao` | 422 | ✅ |
| BC-009 Số lượng CG/TVV | `/bao-cao/so-luong-cg-tvv` | 422 | ✅ |
| BC-010 Đánh giá hiệu quả | `/bao-cao/danh-gia-hieu-qua` | **200** | ❌ silently accept (bug) |
| BC-015 Chi phí chi trả | `/bao-cao/chi-phi-chi-tra` | 422 | ✅ |
| BC-020 Số lượng CT hỗ trợ | `/bao-cao/so-luong-ct-ho-tro` | 422 | ✅ |
| BC-021 CT theo đơn vị | `/bao-cao/ct-theo-don-vi` | 422 | ✅ |

→ **10/12 PASS validation, 2/12 FAIL**. Bug **isolated tới 2 BC**: BC-001 (`/hoi-dap`) + BC-010 (`/danh-gia-hieu-qua`). 10 BC khác đã có `@IsEnum` decorator chạy đúng. 2 BC này có thể dùng DTO khác / chưa migrate sang validation base hoặc decorator commented out.

→ Suggest dev: clone `@IsEnum(KyBaoCao)` decorator từ DTO của 10 BC PASS sang DTO của 2 BC FAIL. Fix 2 chỗ chứ không phải base DTO.
