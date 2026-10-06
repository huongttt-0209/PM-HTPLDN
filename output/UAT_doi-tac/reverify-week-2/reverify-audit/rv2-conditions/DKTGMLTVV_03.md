# Bảng đối chiếu điều kiện — DKTGMLTVV_03 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (đối tác); bug ghi kiểm chéo CB_NV_TW cho kết quả như nhau | CB_NV_TW — `cbnv_tw` (role-independent theo ghi chú bug) | Không |
| Màn hình | Form Thêm mới TVV, nhóm "Nghề nghiệp" | `/chuyen-gia-tvv/tao-moi`, nhóm "Nghề nghiệp" | Không |
| Thao tác kiểm | Liệt kê trường nhóm Nghề nghiệp, tìm "Chứng chỉ hành nghề" + "Mô tả kinh nghiệm" | Cả 2 field có mặt: "Chứng chỉ hành nghề" (ô văn bản) + "Mô tả kinh nghiệm" (ô văn bản dài 0/5000) | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Nhóm "Nghề nghiệp" nay có đủ "Chứng chỉ hành nghề" và "Mô tả kinh nghiệm".
