#!/usr/bin/env sh

for f in fig*.py; do
    python3 "$f"
done

if command -v "gs" > /dev/null; then
    find figs/ -maxdepth 1 -name "*.pdf" \
        -exec gs -q -o {}.opt -dNoOutputFonts -sPAPERSIZE=a4 -sDEVICE=pdfwrite {} \; \
        -exec mv {}.opt {} \;
fi
