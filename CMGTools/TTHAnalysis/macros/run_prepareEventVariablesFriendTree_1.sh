#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_1_OUTPUT_$TF
python prepareEventVariablesFriendTree_1.py -q 1nh -N 50000 -t ttHLepTreeProducerBase -F ttHLepTreeProducerBase/t /afs/cern.ch/work/c/cirkovic/Categorization_240914/CMSSW_5_3_14/src/CMGTools/TTHAnalysis/macros/FT_OUTPUT_270914_163546/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/TREES_250513_HADD_DATA FT_1_OUTPUT_$TF > bsub_1_all_$TF.sh
chmod +x bsub_1_all_$TF.sh

