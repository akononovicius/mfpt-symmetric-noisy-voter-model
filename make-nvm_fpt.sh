#!/usr/bin/env sh

cd nvm_fpt || ( echo "nvm_fpt directory is missing."; exit )

make all && make clean

cd ..
