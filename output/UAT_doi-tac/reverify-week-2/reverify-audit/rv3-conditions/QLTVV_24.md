# Bang doi chieu dieu kien - QLTVV_24 (re-verify 2026-07-15)

| Điều kiện | Bug gốc / bug reopen | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW - sửa hồ sơ TVV | `cbnv_tw` / CB_NV_TW, banner BTP - TW | Không |
| Màn hình / bản ghi | Form Chỉnh sửa Tư vấn viên, TVV-BTP-TW-0002 | `/chuyen-gia-tvv/98cfd963-3cd3-4c8a-bfa9-625460824d6d/chinh-sua`, TVV-BTP-TW-0002 | Không |
| Data / input | Ảnh chân dung `.png` hợp lệ | Upload `.tmp-upload/anh-chan-dung-qa.png`, `image/png`, 429 B, natural size 120x160 | Không |
| Thao tác | Tải PNG vào Ảnh chân dung -> bấm Lưu -> kiểm tra chi tiết + download | PATCH `/api/v1/tu-van-viens/98cfd963-3cd3-4c8a-bfa9-625460824d6d` trả 200; chi tiết hiển thị avatar bằng `<img>`; GET `/files/71bcd8f1-8e6e-4b45-a9ca-887552ecaf5e/download` trả 200 | Không |

Ket luan: 0 GAP. Bug da duoc fix: PNG duoc chap nhan, luu thanh cong, anh chan dung hien thi tren man chi tiet va endpoint download tra 200.

Evidence: `output/UAT_doi-tac/reverify-week-2/bug-reports/image/rv3-QLTVV_24-after-save-avatar-png.png`
