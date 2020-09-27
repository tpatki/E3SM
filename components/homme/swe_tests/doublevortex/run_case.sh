
#!/bin/bash

mkdir -p run
cd run
rm *.*

mpirun.mpich -np $1 ../../execs/sweqx-new.cpu < ../dblvortex.nl > dblvortex.log

cd ..
mkdir -p plots
cd plots
rm *.png
cd ..
python3 make_plots.py
mv *.png plots
