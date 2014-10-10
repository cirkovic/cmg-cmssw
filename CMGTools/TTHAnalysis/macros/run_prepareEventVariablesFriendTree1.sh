#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir OUTPUT_1_$TF
python prepareEventVariablesFriendTree1.py -q 1nh -N 50000 -t treeProducerSusyMultilepton -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_08-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT_081014_203308/evVarFriend_{cname}.root --vector /afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/TREES OUTPUT_1_$TF > bsub_1_all_$TF.sh
chmod +x bsub_1_all_$TF.sh

