#!/usr/bin/env bash
# Build dist/almanac.zip (SKILL.md and references only) and run the official
# UGREEN skill kit checker on the unzipped copy.
#
# Usage: UGREEN_KIT=/path/to/uliya-skill-kit scripts/package.sh
# The kit is not included in this repository; download it from the hackathon page.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"
mkdir -p "$DIST"
rm -f "$DIST/almanac.zip"

(cd "$ROOT/skill" && zip -q -X -r "$DIST/almanac.zip" almanac/SKILL.md almanac/references/*.md)
unzip -l "$DIST/almanac.zip"

if [[ -z "${UGREEN_KIT:-}" ]]; then
  echo "UGREEN_KIT not set; skipping the checker." >&2
  exit 0
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
unzip -q "$DIST/almanac.zip" -d "$TMP"
(cd "$UGREEN_KIT" && node scripts/check-skill.mjs "$TMP/almanac") | tee "$DIST/checker-result.json"
