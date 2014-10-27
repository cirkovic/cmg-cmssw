#!/bin/sh

TF=shiftJEC_down
mkdir OUTPUT_$TF
python prepareEventVariablesFriendTree_1.py -q 1nh -N 50000 -t treeProducerSusyMultilepton ../cfg/OUTPUT_$TF OUTPUT_$TF > bsub_1_all_$TF.sh
chmod +x bsub_1_all_$TF.sh

