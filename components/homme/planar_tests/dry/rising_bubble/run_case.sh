
#!/bin/bash


mkdir -p theta-nh/run-150
cd theta-nh/run-150
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev150-native.cpu < ../../theta-nh/namelist-150.nl > rb-150-theta-nh.log
cd ../..

mkdir -p theta-nh/run-300
cd theta-nh/run-300
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev300-native.cpu < ../../theta-nh/namelist-300.nl > rb-300-theta-nh.log
cd ../..

mkdir -p plots
cd plots
rm *.png
cd ..
python3 make_plots.py
mv *.png plots
