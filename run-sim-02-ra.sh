#!/usr/bin/env bash

python sim_x0_mfpt_ra.py "data/ra-epsi0.csv" --rate 0 --to-left 0.03 --to-right 0.63 --seed 799254634
python sim_x0_mfpt_ra.py "data/ra-epsi5.csv" --rate 0.5 --to-left 0.03 --to-right 0.63 --seed 499616498
python sim_x0_mfpt_ra.py "data/ra-epsi10.csv" --rate 1.0 --to-left 0.03 --to-right 0.63 --seed 697778681
python sim_x0_mfpt_ra.py "data/ra-epsi15.csv" --rate 1.5 --to-left 0.03 --to-right 0.63 --seed 74485942
python sim_x0_mfpt_ra.py "data/ra-epsi20.csv" --rate 2.0 --to-left 0.03 --to-right 0.63 --seed 4167170705
python sim_x0_mfpt_ra.py "data/ra-epsi25.csv" --rate 2.5 --to-left 0.03 --to-right 0.63 --seed 4231316412
