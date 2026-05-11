# Evidence — BUG-BC-DATA-SCOPE-LEAK (R6 retest 2026-05-11 16:55:00 → 16:57:44, bộ acc 08)

> Capture method: `mcp__chrome-devtools__evaluate_script` chạy `fetch('/api/v1/bao-cao/<...>', { credentials: 'include' })` trong `isolatedContext` riêng cho mỗi role (`role-cb_nv_bn_08-r6`, `role-cb_nv_dp_08-r6`, `role-cb_pd_bn_08-r6`, `role-cb_pd_dp_08-r6`). Login full UI flow (login + OTP 666666). Dùng cookie HttpOnly + auth-store thay vì JWT manual.

## Trạng thái sau dev claim fix: **KHÔNG fix — leak vẫn còn 4/4 role**

| Role | User | `donViId` | `capDonVi` | Session context | Verify time (UTC) |
|------|------|-----------|-----------|------------------|-------------------|
| BN (NV) | `cb_nv_bn_08` (BTC) | `00000000-0000-4000-8001-000000000002` | BN | role-cb_nv_bn_08-r6 | 09:57:44 |
| DP (NV) | `cb_nv_dp_08` (Sở BG) | `00000000-0000-4000-8002-000000000008` | DP | role-cb_nv_dp_08-r6 | 09:55:17 |
| BN (PD) | `cb_pd_bn_08` (BTC) | `00000000-0000-4000-8001-000000000002` | BN | role-cb_pd_bn_08-r6 | 09:55:57 |
| DP (PD) | `cb_pd_dp_08` (Sở BG) | `00000000-0000-4000-8002-000000000008` | DP | role-cb_pd_dp_08-r6 | 09:56:58 |

## BC-001 — `GET /api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=<myDV>`

| Role | tongHoiDap | daTraLoi | choTraLoi | tyLeTraLoi (%) | Expected (scoped) | Verdict |
|------|-----------:|---------:|----------:|---------------:|-------------------|---------|
| BN (CB_NV_BN BTC) | 26 | 7 | 19 | 26.9 | 0 (BTC chưa có hỏi đáp ngành) | ❌ LEAK |
| DP (CB_NV_DP Sở BG) | 26 | 7 | 19 | 26.9 | 0 (Sở BG chưa có hỏi đáp) | ❌ LEAK |
| BN (CB_PD_BN BTC) | 26 | 7 | 19 | 26.9 | 0 | ❌ LEAK |
| DP (CB_PD_DP Sở BG) | 26 | 7 | 19 | 26.9 | 0 | ❌ LEAK |

→ Cả 4 role nhận **`tongHoiDap=26` (full national)** thay vì 0 theo seed thực BTC/Sở BG. `theoLinhVuc` payload giống hệt nhau cross-role: Lao động 16 + Doanh nghiệp 5 + Đất đai 3 + Sở hữu trí tuệ 1 + Đầu tư 1.

## BC-004 — `GET /api/v1/bao-cao/vu-viec-hoan-thanh?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`

| Role | tongVuViec | theoDonVi breakdown | Expected (scoped) | Verdict |
|------|-----------:|---------------------|-------------------|---------|
| BN (CB_NV_BN BTC) | 4 | `[Cục Bổ trợ TP (3), Sở Tư pháp An Giang (1)]` | 0 (BTC không có VV hoàn thành trong seed) | ❌ LEAK |
| DP (CB_NV_DP Sở BG) | 4 | `[]` | 0 (Sở BG không có VV hoàn thành) | ❌ LEAK |
| BN (CB_PD_BN BTC) | 4 | `[Cục Bổ trợ TP (3), Sở Tư pháp An Giang (1)]` | 0 | ❌ LEAK |
| DP (CB_PD_DP Sở BG) | 4 | `[]` | 0 | ❌ LEAK |

→ `theoDonVi` ở 2 role BN có giá trị có nghĩa (cho cấp BN nhìn được phân bố quốc gia), 2 role DP trả `[]` (FE filter đơn giản). Cả 4 trường hợp `tongVuViec=4` (full national) **không scope theo `donViId` người dùng**.

## Counter-evidence — Dashboard module SCOPE ĐÚNG (so sánh control)

`GET /api/v1/dashboard?nam=2026&tuNgay=2026-01-01&denNgay=2026-12-31`

| Role | HOI_DAP_MOI | VU_VIEC_HOAN_THANH | CHUYEN_GIA_TVV | appliedFilter.donViId | Verdict |
|------|-------------|--------------------:|----------------:|------------------------|---------|
| BN (CB_NV_BN BTC) | 0 | 0 | 0 | `...8001-000000000002` (BTC) | ✅ scope đúng |
| DP (CB_NV_DP Sở BG) | 0 | 0 | 0 | `...8002-000000000008` (Sở BG) | ✅ scope đúng |
| BN (CB_PD_BN BTC) | 0 | 0 | 0 | `...8001-000000000002` (BTC) | ✅ scope đúng |
| DP (CB_PD_DP Sở BG) | 0 | 0 | 0 | `...8002-000000000008` (Sở BG) | ✅ scope đúng |

→ Khẳng định pattern R4/R5 không đổi sau R6: `/api/v1/dashboard/*` apply scope middleware đúng với cả 4 role; `/api/v1/bao-cao/*` **vẫn không apply** dù cùng app, cùng auth context.

## Root cause unchanged — fix chưa được merge cho controller Báo cáo

Pattern R4 → R5 → R6 giữ nguyên:

1. `BaoCaoService` (hoặc tương đương) vẫn gọi raw query không scope `donViId` từ JWT.
2. Middleware `dataScopeMiddleware` vẫn chỉ wire cho `/api/v1/dashboard/*`, chưa apply cho prefix `/api/v1/bao-cao/*`.
3. `donViId` claim trong JWT/cookie có trong context (dashboard đọc được) → tách layer authorization của báo cáo chưa pull từ context.

## Reproduction script (paste vào DevTools Console sau khi login từng role)

```js
const get = async (url) => {
  const r = await fetch(url, { credentials: 'include' });
  return { status: r.status, body: await r.json() };
};
const me = await get('/api/v1/auth/me');
const myDV = me.body?.data?.donViId;
console.table({
  user_donViId: myDV,
  hoiDap_scoped: (await get(`/api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=${myDV}`)).body?.data?.tongHoiDap,
  hoiDap_nofilter: (await get('/api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31')).body?.data?.tongHoiDap,
  vuViecHoanThanh: (await get('/api/v1/bao-cao/vu-viec-hoan-thanh?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31')).body?.data?.tongVuViec,
  dashboard_HD: (await get('/api/v1/dashboard?nam=2026&tuNgay=2026-01-01&denNgay=2026-12-31')).body?.data?.kpis?.find(k=>k.kpiCode==='HOI_DAP_MOI')?.giaTri
});
```

Expected khi đã fix: cả 4 role `hoiDap_scoped` + `hoiDap_nofilter` + `vuViecHoanThanh` trả 0 (vì BTC + Sở BG đều chưa có data); thực tế R6 → 26 / 26 / 4.

## R6 phụ — Export PDF + XLSX retest (cb_pd_dp_08, 2026-05-11 09:57:22)

Test gửi qua field `formatXuat` (dev R6 đổi từ `dinhDang` → `formatXuat`):

**PDF universal 422 (4/4 sample):**

| loaiBaoCao | status | error.code | error.message |
|------------|:------:|------------|---------------|
| BC_HOI_DAP | 422 | ERR-RPT-EXPORT-01 | Không thể tạo file PDF. Vui lòng thử lại sau hoặc xuất Excel. |
| BC_VU_VIEC_HOAN_THANH | 422 | ERR-RPT-EXPORT-01 | Không thể tạo file PDF. Vui lòng thử lại sau hoặc xuất Excel. |
| BC_CHI_PHI_CHI_TRA | 422 | ERR-RPT-EXPORT-01 | Không thể tạo file PDF. Vui lòng thử lại sau hoặc xuất Excel. |
| BC_SO_LUONG_CG_TVV | 422 | ERR-RPT-EXPORT-01 | Không thể tạo file PDF. Vui lòng thử lại sau hoặc xuất Excel. |

**XLSX 2 BC analytic vẫn unsupported, control PASS:**

| loaiBaoCao | status | content-type | content-length | error.message |
|------------|:------:|--------------|----------------|---------------|
| BC_VV_THEO_LINH_VUC | 422 | application/json | 198 | Loại báo cáo không hỗ trợ xuất |
| BC_DANH_GIA_HIEU_QUA_HTPL | 422 | application/json | 198 | Loại báo cáo không hỗ trợ xuất |
| BC_HOI_DAP (control) | 200 | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | 6393 bytes (PK header `[80,75,3,4]`) | — |

→ PDF universal bug + XLSX partial support bug **chưa fix** trong R6. Pattern không đổi từ R5.

**Lưu ý contract change:** Body export R5 dùng `dinhDang` → R6 dev đổi thành `formatXuat`. Gửi sai field → 422 `ERR-VAL-SYS-00-01` "formatXuat must be one of XLSX, PDF". Test script cũ cần adapt.
