#!/bin/bash
# getdl.sh <ext> <dest-path>  — copy file .<ext> mới nhất trong ~/Downloads sang <dest>
# CHỈ chấp nhận file được tạo trong 240 giây gần nhất -> tránh Pass nhầm bằng file cũ.
set -e
EXT="$1"; DEST="$2"
F=$(ls -t "$HOME/Downloads"/*."$EXT" 2>/dev/null | head -1)
if [ -z "$F" ]; then echo "❌ KHONG CO FILE .$EXT nao trong ~/Downloads"; exit 1; fi
NOW=$(date +%s)
MT=$(stat -f %m "$F")
AGE=$((NOW-MT))
if [ "$AGE" -gt 240 ]; then
  echo "❌ FILE CU: $F (tao cach day ${AGE}s > 240s) => KHONG PHAI file vua tai. Coi nhu tai THAT BAI."
  exit 2
fi
echo "FILE: $F  (age ${AGE}s, $(stat -f %z "$F") bytes)"
cp "$F" "$DEST"
echo "COPIED -> $DEST"
