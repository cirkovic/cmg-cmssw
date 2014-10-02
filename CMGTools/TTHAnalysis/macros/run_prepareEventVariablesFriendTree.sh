#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_OUTPUT_$TF
python prepareEventVariablesFriendTree.py -q 1nh -N 50000 -t treeProducerSusyMultilepton --vector /afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/TREES FT_OUTPUT_$TF > bsub_all_$TF.sh
chmod +x bsub_all_$TF.sh

