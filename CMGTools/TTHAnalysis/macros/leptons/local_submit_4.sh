#!/bin/sh

source /afs/cern.ch/sw/lcg/external/gcc/4.9.1/x86_64-slc6-gcc48-opt/setup.sh
source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.20/x86_64-slc6-gcc48-opt/root/bin/thisroot.sh

#arg=mu_pteta_high_b
#arg=mu_pteta_low_b
#arg=mu_pteta_high_e
arg=mu_pteta_low_e
#arg=el_pteta_high_cb
#arg=el_pteta_low_cb
#arg=el_pteta_high_fb
#arg=el_pteta_low_fb
#arg=el_pteta_high_ec
#arg=el_pteta_low_ec

root -l -q 'trainLeptonID.cxx("'$arg'")'

