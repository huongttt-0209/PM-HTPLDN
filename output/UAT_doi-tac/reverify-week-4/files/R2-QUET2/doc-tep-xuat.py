#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump noi dung tep xuat (xlsx / docx / pdf) theo dinh dang log R2."""
import sys, os, datetime, re

# chi flag khi that su giong ngay/gio: 2026-07-28 | 28/07/2026 | 16:48:34
DATE_RE = re.compile(r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}:\d{2}')

def dump_xlsx(path, max_rows=None):
    import openpyxl
    wb = openpyxl.load_workbook(path)
    out = []
    for ws in wb.worksheets:
        out.append("")
        out.append("--- Sheet '%s'  vung=%s  (%d dong x %d cot)" % (
            ws.title, ws.dimensions, ws.max_row, ws.max_column))
        out.append("")
        out.append("[NOI DUNG TEP -- tung o: gia tri | kieu | dinh dang o]")
        last = ws.max_row if not max_rows else min(ws.max_row, max_rows)
        if last < ws.max_row:
            out.append("  (in %d dong dau; %d dong con lai cung cau truc -- xem muc thong ke cuoi khoi)"
                       % (last, ws.max_row - last))
        for r in range(1, last + 1):
            cells = []
            for c in range(1, ws.max_column + 1):
                cell = ws.cell(row=r, column=c)
                if cell.value is None:
                    continue
                v = cell.value
                t = type(v).__name__
                flag = ""
                if isinstance(v, (datetime.datetime, datetime.date, datetime.time)):
                    flag = "NGAY/GIO"
                    t = "datetime" if isinstance(v, datetime.datetime) else t
                elif isinstance(v, str) and DATE_RE.search(v):
                    flag = "NGAY/GIO dang CHUOI"
                sv = str(v)
                cells.append("     %-5s %-104s | %-9s | %-20s %s" % (
                    cell.coordinate, "'" + sv + "'", t, cell.number_format or 'General', flag))
            if cells:
                out.append("  Dong %d:" % r)
                out.extend(cells)
    return "\n".join(out)


def dump_docx(path):
    import docx
    d = docx.Document(path)
    out = []
    out.append("")
    out.append("--- Word: %d doan van + %d bang" % (len(d.paragraphs), len(d.tables)))
    out.append("")
    out.append("[NOI DUNG TEP -- doan van]")
    for i, p in enumerate(d.paragraphs, 1):
        if p.text.strip():
            st = p.style.name if p.style is not None else '(khong style)'
            out.append("  P%-3d [%s] '%s'" % (i, st, p.text))
    for ti, t in enumerate(d.tables, 1):
        out.append("")
        out.append("  --- Bang %d: %d dong x %d cot" % (ti, len(t.rows), len(t.columns)))
        for ri, row in enumerate(t.rows, 1):
            vals = [c.text.replace("\n", " / ") for c in row.cells]
            out.append("     B%d.R%-3d %s" % (ti, ri, " | ".join("'" + v + "'" for v in vals)))
    return "\n".join(out)


def dump_pdf(path):
    import fitz
    doc = fitz.open(path)
    out = []
    out.append("")
    out.append("--- PDF: %d trang" % doc.page_count)
    out.append("")
    out.append("[NOI DUNG TEP -- van ban tung trang]")
    for pi in range(doc.page_count):
        page = doc[pi]
        out.append("  --- Trang %d" % (pi + 1))
        for ln in page.get_text().splitlines():
            if ln.strip():
                out.append("     | " + ln)
    return "\n".join(out)


if __name__ == '__main__':
    p = sys.argv[1]
    kind = sys.argv[2] if len(sys.argv) > 2 else None
    if not kind:
        with open(p, 'rb') as f:
            magic = f.read(4)
        if magic[:2] == b'PK':
            kind = 'docx' if 'docx' in p.lower() or 'word' in p.lower() else 'xlsx'
        elif magic[:4] == b'%PDF':
            kind = 'pdf'
    mr = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print("# tep: %s   (%d byte)  loai=%s" % (os.path.basename(p), os.path.getsize(p), kind))
    if kind == 'xlsx':
        print(dump_xlsx(p, mr))
    elif kind == 'docx':
        print(dump_docx(p))
    else:
        print(dump_pdf(p))
