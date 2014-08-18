#!/bin/sh

#cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_7_0_6_patch1/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/leptons
root -l -q 'trainLeptonID.cxx("'$1'")'

