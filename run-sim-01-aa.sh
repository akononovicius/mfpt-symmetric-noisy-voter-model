#!/usr/bin/env bash

python sim_x0_mfpt_aa.py "data/aa-epsi0.csv" --rate 0 --to-left 0.03 --to-right 0.63 --seed 1557575040
python sim_x0_mfpt_aa.py "data/aa-epsi5.csv" --rate 0.5 --to-left 0.03 --to-right 0.63 --seed 2042542324
python sim_x0_mfpt_aa.py "data/aa-epsi10.csv" --rate 1.0 --to-left 0.03 --to-right 0.63 --seed 2274082704
python sim_x0_mfpt_aa.py "data/aa-epsi15.csv" --rate 1.5 --to-left 0.03 --to-right 0.63 --seed 687825993
python sim_x0_mfpt_aa.py "data/aa-epsi20.csv" --rate 2.0 --to-left 0.03 --to-right 0.63 --seed 342763353
python sim_x0_mfpt_aa.py "data/aa-epsi25.csv" --rate 2.5 --to-left 0.03 --to-right 0.63 --seed 3601522571
