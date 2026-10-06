#!/usr/bin/env python3
"""Chấm tệp PDF xuất từ màn Báo cáo thống kê theo chuẩn đã khóa của lô.

Đọc file <MãTC>-pdf-capture.json do trình duyệt bắt được, giải mã ra <MãTC>.pdf,
rồi đối chiếu từng mục của chuẩn PASS. In bảng kết quả + trích toàn văn tệp.

    python3 files/kiem-tep-pdf.py SLHDVM_07
"""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BATCH = os.path.dirname(HERE)
EV = os.path.join(BATCH, "evidence")

# Khuôn tên tệp theo Phụ lục E §H8: {TenBaoCao}_{YYYYMMDD_HHmm}.pdf
KHUON_TEN = re.compile(r"^[A-Za-z0-9]+_\d{8}_\d{4}\.pdf$")
A4_W, A4_H = 595.28, 841.89
CAU_LOI_CU = "Không thể tạo file xuất"


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Dùng: python3 kiem-tep-pdf.py <MãTC>")
    ma = sys.argv[1]
    cap = os.path.join(EV, f"{ma}-pdf-capture.json")
    if not os.path.isfile(cap):
        raise SystemExit(f"❌ Không thấy {cap}")
    d = json.load(open(cap, encoding="utf-8"))

    if d.get("loi"):
        print(f"❌ TRÌNH DUYỆT BÁO LỖI: {d['loi']}")
        for k in ("coSan", "modal", "toasts", "manHinh"):
            if d.get(k):
                print(f"   {k}: {str(d[k])[:400]}")
        raise SystemExit(1)

    ten = ((d.get("tenTep") or d.get("names")) or [""])[0]
    pdf_path = os.path.join(EV, f"{ma}.pdf")
    open(pdf_path, "wb").write(base64.b64decode(d["b64"]))

    import fitz
    doc = fitz.open(pdf_path)
    page = doc[0]
    full = "\n".join(p.get_text() for p in doc)
    flat = re.sub(r"\s+", " ", full)
    fonts = sorted({f[3] for f in page.get_fonts()})
    rect = page.rect

    ck = []
    ck.append(("Tên tệp đúng khuôn {TenBaoCao}_{YYYYMMDD_HHmm}.pdf",
               bool(KHUON_TEN.match(ten)), ten))
    ck.append(("Quốc hiệu ở đầu trang",
               "CỘNG HÒA XÃ HỘI CHỦ NGHĨA" in flat, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" if "CỘNG HÒA XÃ HỘI CHỦ NGHĨA" in flat else "(thiếu)"))
    ck.append(("Tiêu ngữ ở đầu trang",
               "Độc lập - Tự do - Hạnh phúc" in flat, "Độc lập - Tự do - Hạnh phúc" if "Độc lập - Tự do - Hạnh phúc" in flat else "(thiếu)"))
    coquan = re.search(r"(CỤC[^\n]*?|SỞ TƯ PHÁP[^\n]*?)(?=CỘNG HÒA)", flat)
    ck.append(("Tên cơ quan ban hành ở đầu trang",
               bool(coquan), coquan.group(1).strip() if coquan else "(thiếu)"))
    ngayky = re.search(r"Ngày \d{2} tháng \d{2} năm \d{4}", flat)
    ck.append(("Ngày ký ở cuối trang", bool(ngayky), ngayky.group(0) if ngayky else "(thiếu)"))
    ck.append(("Dòng NGƯỜI XUẤT BÁO CÁO", "NGƯỜI XUẤT BÁO CÁO" in flat, "có" if "NGƯỜI XUẤT BÁO CÁO" in flat else "(thiếu)"))
    ck.append(("Chỗ trống cho con dấu", "(Ký, ghi rõ họ tên và đóng dấu)" in flat, "có" if "(Ký, ghi rõ họ tên và đóng dấu)" in flat else "(thiếu)"))
    ck.append(("Họ tên cán bộ xuất báo cáo", "CB Nghiệp vụ - Trung ương" in flat, "CB Nghiệp vụ - Trung ương #05" if "CB Nghiệp vụ - Trung ương" in flat else "(thiếu)"))
    ck.append(("Khổ A4 dọc (595,28 × 841,89 pt)",
               abs(rect.width - A4_W) < 1 and abs(rect.height - A4_H) < 1,
               f"{rect.width:.2f} × {rect.height:.2f} pt"))
    ck.append(("Phông Times New Roman (bản tương thích Tinos)",
               any("Tinos" in f for f in fonts), ", ".join(fonts)))
    ck.append(("Đầu tệp có tên báo cáo", bool(re.search(r"\bBC [A-ZĐÁÀẢÃẠÂĂÊÔƠƯ]", flat)),
               (re.search(r"BC [^\n]{3,70}", full) or [""])[0] if re.search(r"BC [^\n]{3,70}", full) else "(thiếu)"))
    ck.append(("Đầu tệp có 'Kỳ báo cáo:'", "Kỳ báo cáo:" in flat,
               (re.search(r"Kỳ báo cáo:[^\n]*", full) or [""])[0] if "Kỳ báo cáo:" in flat else "(thiếu)"))
    ck.append(("Đầu tệp có 'Đơn vị:'", "Đơn vị:" in flat,
               (re.search(r"Đơn vị:[^\n]*", full) or [""])[0] if "Đơn vị:" in flat else "(thiếu)"))
    ck.append(("Đầu tệp có 'Ngày tạo:'", "Ngày tạo:" in flat,
               (re.search(r"Ngày tạo:[^\n]*", full) or [""])[0] if "Ngày tạo:" in flat else "(thiếu)"))
    ck.append(("Không tái hiện câu 'Không thể tạo file xuất'",
               CAU_LOI_CU not in flat and not any(CAU_LOI_CU in str(t) for t in (d.get("toasts") or [])),
               "không thấy" ))

    print(f"===== {ma} =====")
    print(f"Tệp: {ten}  ·  {d.get('size')} byte  ·  {doc.page_count} trang")
    print(f"Cờ chữ ký số (sigflags) = {doc.get_sigflags()}  → -1 nghĩa là KHÔNG ký số (đúng chủ trương, không chấm FAIL)")
    if d.get("toasts"):
        print(f"Thông báo trên màn: {d['toasts']}")
    print()
    dat = 0
    for ten_muc, ok, gt in ck:
        print(f"  {'✅' if ok else '❌'} {ten_muc:<52} {gt}")
        dat += 1 if ok else 0
    print()
    print(f"KẾT QUẢ: {dat}/{len(ck)} mục đạt" + ("  → PASS" if dat == len(ck) else "  → CÒN LỖI"))
    print()
    print("==== SỐ LIỆU TRÊN MÀN (để đối chiếu bằng mắt) ====")
    print((d.get("manHinh") or "(không có)")[:1200])
    print()
    print("==== TOÀN VĂN TỆP PDF ====")
    print(doc[0].get_text())
    return 0 if dat == len(ck) else 1


if __name__ == "__main__":
    sys.exit(main())
