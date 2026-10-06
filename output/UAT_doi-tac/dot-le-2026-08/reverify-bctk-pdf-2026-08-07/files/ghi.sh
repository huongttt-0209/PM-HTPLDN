#!/bin/bash
# Ghi verdict 1 dòng lô BCTK-PDF vào tab `bug`.
#   ./ghi.sh <row> <MãTC> pass "<lý do audit>"
#   ./ghi.sh <row> <MãTC> reopen "<lý do audit>"   (cần note/<MãTC>-ketqua-verify.txt)
set -euo pipefail
ROOT="/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk"
BATCH="output/UAT_doi-tac/reverify-bctk-pdf-2026-08-07"
cd "$ROOT"

ROW="$1"; MATC="$2"; VERDICT="$3"; REASON="${4:-Lo BCTK-PDF 2026-08-07}"
EXPR_R="$BATCH/files/expect-cu/${ROW}-${MATC}-R-cu.txt"
EXPT_T="$BATCH/files/expect-cu/${ROW}-${MATC}-T-cu.txt"
NOTE="$BATCH/note/${MATC}-ketqua-verify.txt"

ARGS=(--spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s
      --sheet-title 'bug' --sheet-gid 1714340219
      --row "$ROW" --id-column 'Mã TC' --id-value "$MATC"
      --expect-file "Trạng thái dev fix=$EXPR_R"
      --reason "$REASON")

if [ "$VERDICT" = "pass" ]; then
  ARGS+=(--set 'Trạng thái dev fix=Test done')
elif [ "$VERDICT" = "reopen" ]; then
  [ -f "$NOTE" ] || { echo "❌ Thiếu file note $NOTE"; exit 2; }
  ARGS+=(--set 'Trạng thái dev fix=Reopen'
         --expect-file "Kết quả verify=$EXPT_T"
         --set-file "Kết quả verify=$NOTE")
else
  echo "❌ verdict phải là pass hoặc reopen"; exit 2
fi

python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py "${ARGS[@]}" 2>&1 \
  | grep -vE "FutureWarning|warnings\.warn|NotOpenSSLWarning|urllib3 v2 only|^  warnings|eol_message"
