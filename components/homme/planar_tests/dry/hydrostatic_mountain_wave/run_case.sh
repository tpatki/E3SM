
#!/bin/bash


mkdir -p theta-nh/run
cd theta-nh/run
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev200-native.cpu < ../../theta-nh/namelist.nl > hmw-theta-nh.log
cd ../..

mkdir -p theta-h/run
cd theta-h/run
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev200-native.cpu < ../../theta-h/namelist.nl > hmw-theta-h.log
cd ../..

mkdir -p preqx/run
cd preqx/run
rm *.*
mpirun.mpich -np $1 ../../../execs/preqx-nlev200-native.cpu < ../../preqx/namelist.nl > hmw-preqx.log
cd ../..

mkdir -p plots
cd plots
rm *.png
cd ..
python3 make_plots.py
mv *.png plots
