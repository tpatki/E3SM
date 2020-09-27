
#!/bin/bash


mkdir -p theta-nh/run-64
cd theta-nh/run-64
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev64-native.cpu < ../../theta-nh/namelist-64.nl > dc-64-theta-nh.log
cd ../..

mkdir -p theta-nh/run-128
cd theta-nh/run-128
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev128-native.cpu < ../../theta-nh/namelist-128.nl > dc-128-theta-nh.log
cd ../..

mkdir -p theta-nh/run-256
cd theta-nh/run-256
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev256-native.cpu < ../../theta-nh/namelist-256.nl > dc-256-theta-nh.log
cd ../..

mkdir -p plots
cd plots
rm *.png
cd ..
python3 make_plots.py
mv *.png plots
