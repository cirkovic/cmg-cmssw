#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_1_OUTPUT_$TF
python prepareEventVariablesFriendTree_1.py -q 8nh -t ttHLepTreeProducerBase -F sf/t /afs/cern.ch/work/c/cirkovic/Categorization_240914/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/FT_OUTPUT_240914_170333/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/TREES_250513_HADD FT_1_OUTPUT_$TF > bsub_1_all_$TF.sh
chmod +x bsub_1_all_$TF.sh

