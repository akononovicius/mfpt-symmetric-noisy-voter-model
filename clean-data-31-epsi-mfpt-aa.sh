#!/usr/bin/env sh

cd data || exit

f="epsi-mfpt-aa.csv"
sort -t',' -k1,1n -k2,2n "$f" > "sorted.$f"
mv -f "sorted.$f" "$f"

cd ..
