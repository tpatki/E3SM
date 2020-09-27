
#!/bin/bash


mkdir -p run-$2-$3
cd run-$2-$3
rm -rf *

if [ "$3" = "rrm" ]
then
mpirun.mpich -np $1 ../../execs/sweqx-$2.cpu < ../swtc6-rrm.nl > swtc6.log
else
mpirun.mpich -np $1 ../../execs/sweqx-$2.cpu < ../swtc6.nl > swtc6.log
fi
