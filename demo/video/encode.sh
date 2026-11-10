#!/usr/bin/env bash
# Encode the filmed shots into one MP4. Usage: encode.sh <shots-dir> <out.mp4>
set -euo pipefail
SHOTS="$1"; OUT="$2"; TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
LAST=$(python3 -c "import json;print(len(json.load(open('$SHOTS/shots.json'))))")
python3 - "$SHOTS" "$LAST" > "$TMP/plan.txt" <<'PY'
import json, sys
shots = json.load(open(sys.argv[1] + "/shots.json")); last = int(sys.argv[2])
for i, s in enumerate(shots, 1):
    fade = ""
    if i == 1: fade = ",fade=t=in:st=0:d=0.6"
    if i == last: fade = f",fade=t=out:st={s['seconds']-0.8}:d=0.8"
    print(s["file"], s["seconds"], fade)
PY
: > "$TMP/list.txt"
while read -r f secs fade; do
  ffmpeg -nostdin -hide_banner -loglevel error -y -framerate 30 -i "$SHOTS/$f" \
    -vf "scale=1920:1080,format=yuv420p,loop=-1:1,trim=duration=${secs}${fade:-}" \
    -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p -r 30 "$TMP/${f%.jpg}.tmp.mp4"
  mv "$TMP/${f%.jpg}.tmp.mp4" "$TMP/${f%.jpg}.mp4"
  echo "file '$TMP/${f%.jpg}.mp4'" >> "$TMP/list.txt"
done < "$TMP/plan.txt"
ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i "$TMP/list.txt" -c copy "$TMP/video.mp4"
ffmpeg -hide_banner -loglevel error -y -i "$TMP/video.mp4" -f lavfi -i anullsrc=r=48000:cl=stereo \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 64k -shortest -movflags +faststart "$OUT.tmp.mp4"
mv "$OUT.tmp.mp4" "$OUT"
