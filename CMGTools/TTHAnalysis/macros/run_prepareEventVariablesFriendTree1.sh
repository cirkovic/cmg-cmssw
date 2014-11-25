#!/bin/sh

mkdir OUTPUT1
python prepareEventVariablesFriendTree1.py -q 1nh -N 50000 /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT OUTPUT1 > bsub_all_1.sh --tree treeProducerSusyMultilepton
chmod +x bsub_all_1.sh

