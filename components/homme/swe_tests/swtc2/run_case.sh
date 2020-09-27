
#!/bin/bash


mkdir -p run-$2-$3
cd run-$2-$3
rm -rf *

if [ "$3" = "rrm" ]
then
mpirun.mpich -np $1 ../../execs/sweqx-$2.cpu < ../swtc2-rrm.nl > swtc2.log
else
mpirun.mpich -np $1 ../../execs/sweqx-$2.cpu < ../swtc2.nl > swtc2.log
fi
