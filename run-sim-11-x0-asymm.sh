#!/usr/bin/env bash

python sim_x0_mfpt_aa.py "data/x0-asymm-epsi0.csv" --rate 0 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 713516238
python sim_x0_mfpt_aa.py "data/x0-asymm-epsi8.csv" --rate 0.8 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 1653131865
python sim_x0_mfpt_aa.py "data/x0-asymm-epsi16.csv" --rate 1.6 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 2934629161
python sim_x0_mfpt_aa.py "data/x0-asymm-epsi24.csv" --rate 2.4 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 1754156553
python sim_x0_mfpt_aa.py "data/x0-asymm-epsi32.csv" --rate 3.2 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 1091973634
python sim_x0_mfpt_aa.py "data/x0-asymm-epsi40.csv" --rate 4 --n-x-0 31 --to-left 0.1 --to-right 0.7 --seed 3097803421
