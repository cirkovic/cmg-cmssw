#!/bin/sh

mkdir OUTPUT_SF
python prepareScaleFactorsFriendTree.py -q 1nh -N 50000 /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT OUTPUT_SF > bsub_all_sf.sh --tree treeProducerSusyMultilepton
chmod +x bsub_all_sf.sh

