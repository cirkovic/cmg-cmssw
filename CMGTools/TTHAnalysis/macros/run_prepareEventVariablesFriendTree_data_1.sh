#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_DATA_1_OUTPUT_$TF
python prepareEventVariablesFriendTree_1.py -q 8nh -N 50000 -t ttHLepTreeProducerBase -F sf/t /afs/cern.ch/work/c/cirkovic/Categorization_240914/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/FT_DATA_OUTPUT_250914_103448/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/TREES_250513_HADD_DATA FT_DATA_1_OUTPUT_$TF > bsub_data_1_all_$TF.sh
chmod +x bsub_data_1_all_$TF.sh

