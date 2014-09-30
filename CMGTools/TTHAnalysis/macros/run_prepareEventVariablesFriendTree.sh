#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir OUTPUT_$TF
python prepareEventVariablesFriendTree.py -q 1nh -N 200000 -t ttHLepTreeProducerBase /afs/cern.ch/work/m/mdjordje/TTH/TREES_250513_HADD OUTPUT_$TF > bsub_all_$TF.sh
chmod +x bsub_all_$TF.sh

