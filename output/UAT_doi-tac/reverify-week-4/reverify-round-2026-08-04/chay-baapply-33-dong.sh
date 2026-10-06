#!/bin/bash
# Áp quyết định BA lên 33 dòng đang chờ (BƯỚC 2 — QA_BA_APPLY_PROTOCOL).
#   ./chay-baapply-33-dong.sh            → dry-run (mặc định, KHÔNG ghi)
#   ./chay-baapply-33-dong.sh --write    → ghi thật
#
# Giãn nhịp 15s/dòng vì quota đọc Sheets là 60 request/phút/user, mỗi lần gọi đọc ~4 request.
set -u
cd "$(dirname "$0")/../.." || exit 1             # về .../output/UAT_doi-tac

R="reverify-week-4/reverify-round-2026-08-04"
BA="$R/phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md"
NOTES="$R/notes-baapply"
COND="$R/cond/xuat-pdf-21-phieu.md"
EV="$R/evidence/bao-cao-hoi-dap-2026-08-04.pdf"
T2="UAT_TGPL Doanh Nghiệp-tuần 2"
T3="UAT_TGPL Doanh Nghiệp-tuần 3"
LOG="$R/ket-qua-chay-$( [ "${1:-}" = "--write" ] && echo write || echo dryrun ).log"

FLAG="--dry-run"; [ "${1:-}" = "--write" ] && FLAG=""
: > "$LOG"
OK=0; FAIL=0

# --- vòng 1: 12 dòng, mode baapply (ghi P+Q+R, giữ P nếu P='dev done') ---
ba() {  # tab row maTC status noteFile
  echo "════ row $2 $3 → $4 (baapply)" | tee -a "$LOG"
  if UAT_TAB="$1" python3 tools/sheet_write.py --mode baapply --row "$2" --ma-tc "$3" \
       --status "$4" --note-file "$NOTES/$5" --ba-source "$BA" $FLAG >>"$LOG" 2>&1; then
    OK=$((OK+1)); echo "   ✅ ok"
  else
    FAIL=$((FAIL+1)); echo "   ❌ DỪNG — xem $LOG"; tail -6 "$LOG" | sed 's|^|      |'
  fi
  sleep 15
}

ba "$T2" 116 KTDGKQHT_02        Open   116-KTDGKQHT_02.txt
ba "$T2" 120 PDKHDTTH_04        Reject 120-PDKHDTTH_04.txt
ba "$T2" 122 DKTGMLTVV_04       Reject 122-DKTGMLTVV_04.txt
ba "$T2" 123 DKTGMLTVV_05       Open   123-DKTGMLTVV_05.txt
ba "$T2" 125 QLLSHTCTVV_03      Open   125-QLLSHTCTVV_03.txt
ba "$T2" 126 QLLSHTCTVV_04      Open   126-QLLSHTCTVV_04.txt
ba "$T2" 127 NHSYC_01           Open   127-NHSYC_01.txt
ba "$T2" 135 QLDXDTTH_11        Open   135-QLDXDTTH_11.txt
ba "$T2" 145 TKHSYCHTPL_OOS_01  Open   145-TKHSYCHTPL_OOS_01.txt
ba "$T3" 331 QLDMTCTV_OOS_05    Open   331-QLDMTCTV_OOS_05.txt
ba "$T3" 332 QLDMTCTV_OOS_06    Reject 332-QLDMTCTV_OOS_06.txt
ba "$T3" 339 QLDMTCTV_OOS_13    Open   339-QLDMTCTV_OOS_13.txt

# --- vòng 2: 21 phiếu Xuất PDF, mode reverify2 Reopen (ghi W+X+Y) ---
rv2() {  # row maTC
  echo "════ row $1 $2 → Reopen (reverify2)" | tee -a "$LOG"
  if UAT_TAB="$T3" python3 tools/sheet_write.py --mode reverify2 --row "$1" --ma-tc "$2" \
       --status Reopen --note-file "$NOTES/xuat-pdf-21-phieu.txt" \
       --evidence "$EV" --condition-table "$COND" \
       --vong2-do-dev-build "Dev đánh dấu dev done cho nhóm Xuất PDF nhưng chưa ai đo lại; QA đo lại 04/08/2026 trên bản dựng V1.0.5 theo yêu cầu của BA" \
       $FLAG >>"$LOG" 2>&1; then
    OK=$((OK+1)); echo "   ✅ ok"
  else
    FAIL=$((FAIL+1)); echo "   ❌ DỪNG — xem $LOG"; tail -6 "$LOG" | sed 's|^|      |'
  fi
  sleep 15
}

rv2 192 SLHDVM_07;        rv2 197 VVDTN_07;         rv2 204 VVDHT_07
rv2 210 VVDHTHT_07;       rv2 217 VVTTG_06;         rv2 223 CLDTBDDDR_07
rv2 228 LDTBDDDR_07;      rv2 231 CGTVPL_07;        rv2 234 DGHQHTPL_07
rv2 240 VVTDVQL_07;       rv2 244 VVTLV_06;         rv2 247 VVTLHDN_06
rv2 249 VVTTGCT_06;       rv2 251 CPHTCT_07;        rv2 254 CPCTHTTDVQL_07
rv2 258 CPCTHTTLHDN_07;   rv2 261 CPCTHTTTG_06;     rv2 265 SLCTHT_07
rv2 269 CTTDVQL_05;       rv2 274 CTTLV_06;         rv2 276 CTTTG_05

echo
echo "═══════════════════════════════════════"
echo "  Chế độ : $( [ -z "$FLAG" ] && echo 'GHI THẬT' || echo 'DRY-RUN (không ghi)' )"
echo "  Thành công : $OK / 33"
echo "  Bị chặn    : $FAIL"
echo "  Log đầy đủ : $LOG"
echo "═══════════════════════════════════════"
