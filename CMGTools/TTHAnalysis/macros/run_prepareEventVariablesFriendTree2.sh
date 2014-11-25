#!/bin/sh

mkdir OUTPUT2
python prepareEventVariablesFriendTree2.py -q 1nh -N 50000 --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT1/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT OUTPUT2 --tree treeProducerSusyMultilepton > bsub_all_2.sh
chmod +x bsub_all_2.sh

