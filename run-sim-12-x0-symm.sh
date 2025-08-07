#!/usr/bin/env bash

python sim_x0_mfpt_aa.py "data/x0-symm-epsi0.csv" --rate 0 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 1700910181
python sim_x0_mfpt_aa.py "data/x0-symm-epsi8.csv" --rate 0.8 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 1970241829
python sim_x0_mfpt_aa.py "data/x0-symm-epsi16.csv" --rate 1.6 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 4207108774
python sim_x0_mfpt_aa.py "data/x0-symm-epsi24.csv" --rate 2.4 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 2166870293
python sim_x0_mfpt_aa.py "data/x0-symm-epsi32.csv" --rate 3.2 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 2803799752
python sim_x0_mfpt_aa.py "data/x0-symm-epsi40.csv" --rate 4.0 --n-x-0 31 --to-left 0.2 --to-right 0.8 --seed 4142616228
