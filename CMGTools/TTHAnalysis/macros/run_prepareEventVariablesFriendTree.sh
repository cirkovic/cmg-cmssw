#!/bin/sh

TF=`date +"%d%m%y_%H%M%S"`
mkdir FT_OUTPUT_$TF
python prepareEventVariablesFriendTree.py -q 1nh -N 50000 -t ttHLepTreeProducerBase /afs/cern.ch/work/c/cirkovic/TREES_250513_HADD_DATA FT_OUTPUT_$TF > bsub_all_$TF.sh
chmod +x bsub_all_$TF.sh

