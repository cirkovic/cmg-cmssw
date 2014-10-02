#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_1_OUTPUT_$TF
python prepareEventVariablesFriendTree_1.py -q 1nh -N 50000 -t treeProducerSusyMultilepton --vector -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/FT_OUTPUT_021014_151628/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/TREES FT_1_OUTPUT_$TF > bsub_1_all_$TF.sh
chmod +x bsub_1_all_$TF.sh

