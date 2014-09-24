#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_OUTPUT_$TF
#python prepareEventVariablesFriendTree.py -q 8nh -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/Retraining_200914/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/cfg/OUTPUT FT_OUTPUT_$TF --vector > bsub_all_$TF.sh
python prepareEventVariablesFriendTree.py -q 8nh -t ttHLepTreeProducerBase /afs/cern.ch/work/c/cirkovic/TREES_250513_HADD FT_OUTPUT_$TF > bsub_all_$TF.sh
chmod +x bsub_all_$TF.sh

