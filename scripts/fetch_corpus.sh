#!/usr/bin/env sh
# Fetch the demo corpus at the pinned commits (the snapshots the demo report was produced on).
# Usage: scripts/fetch_corpus.sh <corpus_dir>
set -eu
DEST="${1:-corpus}"
mkdir -p "$DEST"
fetch() {  # fetch <owner/repo> <dir> <commit>
  d="$DEST/$2"
  if [ ! -d "$d/.git" ]; then git init -q "$d"; git -C "$d" remote add origin "https://github.com/$1"; fi
  git -C "$d" fetch -q --depth 1 origin "$3"
  git -C "$d" checkout -q FETCH_HEAD
  echo "$2 @ $3"
}
fetch python-attrs/attrs attrs    8f767776326faaed11e6c2974798787f6e19b343
fetch psf/black          black    20622e1259c29bda81831962ace1348ba1921c84
fetch pallets/click      click    36baa15ff831b939a22bc527cd76ce653ef6f66d
fetch pallets/flask      flask    d318b683471101618febed18996405ad26462110
fetch encode/httpx       httpx    b5addb64f0161ff6bfe94c124ef76f6a1fba5254
fetch pytest-dev/pytest  pytest   51e9a9f148cd2509a31e3fa0d2b1b3204c2b0dd7
fetch psf/requests       requests dae7ef63b4df6eded86637f251fc4e3a06c3b479
fetch Textualize/rich    rich     9d8f9a372cc5916fd4781fec207ced7ddac2f08f
