#!/bin/bash

for src in ./*; do
  [ -f "$src" ] || continue
  name=$(basename "$src")
  for dst in ~/204595_github/*/"$name"; do
    [ -f "$dst" ] && cp -f "$src" "$dst"
  done
done