#!/bin/sh

mkdir OUTPUT1_shiftJEC
python prepareEventVariablesFriendTree1.py -q 1nh -N 50000 /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_shiftJEC OUTPUT1_shiftJEC > bsub_all_1_shiftJEC.sh --tree treeProducerSusyMultilepton
chmod +x bsub_all_1_shiftJEC.sh

