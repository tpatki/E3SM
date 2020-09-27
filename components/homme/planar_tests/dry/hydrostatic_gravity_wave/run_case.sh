
#!/bin/bash

mkdir -p theta-nh/run-$2
cd theta-nh/run-$2
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev20-native.cpu < ../../theta-nh/namelist-$2.nl > hgw-$2-theta-nh.log
cd ../..

mkdir -p theta-h/run-$2
cd theta-h/run-$2
rm *.*
mpirun.mpich -np $1 ../../../execs/theta-l-nlev20-native.cpu < ../../theta-h/namelist-$2.nl > hgw-$2-theta-h.log
cd ../..

mkdir -p preqx/run-$2
cd preqx/run-$2
rm *.*
mpirun.mpich -np $1 ../../../execs/preqx-nlev20-native.cpu < ../../preqx/namelist-$2.nl > hgw-$2-preqx.log
cd ../..

mkdir -p plots/$2
cd plots/$2
rm *.png
cd ../..
python3 make_plots.py $2
mv *.png plots/$2


