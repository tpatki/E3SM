#!/bin/bash

cd swtc2
rm -rf cs rrm
mkdir -p cs
mkdir -p rrm
./run_case.sh $1 new cs
./run_case.sh $1 orig cs
python3 make_plots.py cs
mv *.png cs
./run_case.sh $1 new rrm
./run_case.sh $1 orig rrm
python3 make_plots.py rrm
mv *.png rrm
cd ..

cd swtc5
rm -rf cs rrm
mkdir -p cs
mkdir -p rrm
./run_case.sh $1 new cs
./run_case.sh $1 orig cs
python3 make_plots.py cs
mv *.png cs
./run_case.sh $1 new rrm
./run_case.sh $1 orig rrm
python3 make_plots.py rrm
mv *.png rrm
cd ..

cd swtc6
rm -rf cs rrm
mkdir -p cs
mkdir -p rrm
./run_case.sh $1 new cs
./run_case.sh $1 orig cs
python3 make_plots.py cs
mv *.png cs
./run_case.sh $1 new rrm
./run_case.sh $1 orig rrm
python3 make_plots.py rrm
mv *.png rrm
cd ..
