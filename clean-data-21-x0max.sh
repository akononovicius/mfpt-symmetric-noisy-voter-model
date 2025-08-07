#!/usr/bin/env sh

cd data || exit

for f in x0max-epsi*.csv; do
    sort -t',' -k1,1n -k2,2n "$f" > "sorted.$f"
    mv -f "sorted.$f" "$f"
done

cd ..
