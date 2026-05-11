# Evidence — BUG-BC-DATA-SCOPE-LEAK (R4 audit 2026-05-11 14:35:00, bộ acc 08)

> Capture method: `mcp__chrome-devtools__evaluate_script` chạy `fetch('/api/v1/bao-cao/<...>')` trong `isolatedContext` riêng cho mỗi role. JWT lấy từ `localStorage.getItem('auth-store')` của session đang active.

## Setup

| Role | User | `donViId` | `capDonVi` | Session context |
|------|------|-----------|-----------|------------------|
| TW (control) | `cb_nv_tw_08` | — (TW root) | TW | isolatedContext `role-cb-tw` |
| BN | `cb_nv_bn_08` (BTC) | `00000000-0000-4000-8001-000000000002` | BN | isolatedContext `role-cb-bn` |
| DP | `cb_nv_dp_08` (Sở BG) | (Sở BG UUID) | DP | isolatedContext `role-cb-dp` |

## BC-001 — Hỏi đáp pháp luật, Kỳ Năm 2026

```
GET /api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31
```

| Role | tongHoiDap | tongHoiDapDaTraLoi | tongHoiDapChoTraLoi | tyLeTraLoi (%) | Expected |
|------|-----------:|------------------:|--------------------:|---------------:|----------|
| TW | 25 | 22 | 3 | 88 | 25 (full national) — ✅ |
| BN (BTC) | 25 | 22 | 3 | 88 | 0 (BTC chưa nhận hỏi đáp ngành) — ❌ LEAK |
| DP (Sở BG) | 25 | 22 | 3 | 88 | 0 (Sở BG chưa nhận hỏi đáp) — ❌ LEAK |

## BC-004 — Vụ việc đã hoàn thành, Kỳ Năm 2026

```
GET /api/v1/bao-cao/vu-viec?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&trangThai=HOAN_THANH
```

| Role | tongVuViec | tongChiPhi (VND) | Expected |
|------|-----------:|-----------------:|----------|
| TW | 19 | 205.292.242 | 19 (full national) — ✅ |
| BN (BTC) | 19 | 205.292.242 | 1 (~12M theo seed BTC) — ❌ LEAK |
| DP (Sở BG) | 19 | 205.292.242 | 6 (~103M theo seed Sở BG) — ❌ LEAK |

## BC-021 — Số lượng TVV trên hệ thống

```
GET /api/v1/bao-cao/tu-van-vien?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31
```

| Role | tongTvv | tongCgChuyenSau | tongNht | Expected |
|------|--------:|----------------:|--------:|----------|
| TW | 8 | 3 | 2 | 8 (full national) — ✅ |
| BN (BTC) | 8 | 3 | 2 | 0 (BN không có TVV nội bộ) — ❌ LEAK |
| DP (Sở BG) | 8 | 3 | 2 | 0 (DP không có TVV nội bộ) — ❌ LEAK |

## BC-022 — Chi phí HTPL theo đơn vị, Kỳ Năm 2026

```
GET /api/v1/bao-cao/chi-phi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&groupBy=donVi
```

| Role | Response shape | Expected |
|------|----------------|----------|
| TW | Array 7 đơn vị (BTC + 6 Sở), tổng `tongChiPhi=205.292.242` | Full breakdown — ✅ |
| BN (BTC) | Same array 7 đơn vị | Chỉ row BTC (~12M) — ❌ LEAK |
| DP (Sở BG) | Same array 7 đơn vị | Chỉ row Sở BG (~103M) — ❌ LEAK |

## Counter-evidence — Dashboard module SCOPE ĐÚNG

```
GET /api/v1/dashboard/overview
```

| Role | vuViec | hoiDap | tvv | Verdict |
|------|-------:|-------:|----:|---------|
| TW | 19 | 25 | 8 | ✅ scope đúng TW |
| BN (BTC) | 0 | 0 | 0 | ✅ scope đúng BN (= seed thực tế) |
| DP (Sở BG) | 0 | 0 | 0 | ✅ scope đúng DP (= seed thực tế) |

→ Khẳng định BE đã có middleware scope theo `donViId` đang chạy trên `/dashboard` nhưng KHÔNG được apply cho controller `/bao-cao`. Bug isolated tới service `BaoCaoService` (hoặc tương đương) — chỉ cần inject scope guard tương tự dashboard là fix.

## Phân tích root cause (giả thuyết)

1. **Service Báo cáo gọi raw query** thay vì repository tier có scope guard. Cần code review file `bao-cao.service.ts` (hoặc `.controller.ts`) so với `dashboard.service.ts`.
2. **Middleware scope chưa wire cho prefix `/api/v1/bao-cao`** — kiểm tra danh sách route áp `dataScopeMiddleware`.
3. **`donViId` claim trong JWT bị strip** ở 1 đường truyền sang BaoCaoService — log JWT decode payload tại entry controller xác minh.

## Reproduction script (paste vào Console DevTools sau khi login từng role)

```js
const get = async (url) => {
  const auth = JSON.parse(localStorage.getItem('auth-store')||'{}');
  const tok = auth?.state?.accessToken;
  const r = await fetch(url, {headers:{Authorization:`Bearer ${tok}`}, credentials:'include'});
  return {status:r.status, body: await r.json()};
};
console.table({
  hoiDap: await get('/api/v1/bao-cao/hoi-dap?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31'),
  vuViec: await get('/api/v1/bao-cao/vu-viec?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&trangThai=HOAN_THANH'),
  tvv:    await get('/api/v1/bao-cao/tu-van-vien?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31'),
  dashbd: await get('/api/v1/dashboard/overview'),
});
```
