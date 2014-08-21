#!/bin/sh

source /afs/cern.ch/user/g/gpetrucc/sh/init_root528_afs
if [[ $1 != "" ]]
then path=$1
else path=/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/21-08-2014/2/1
fi

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("'$path'/mu_pteta_high_b.root")'


