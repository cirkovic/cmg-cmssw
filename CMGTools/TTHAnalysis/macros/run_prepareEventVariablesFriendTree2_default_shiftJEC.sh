#!/bin/sh

mkdir OUTPUT2_default_shiftJEC
python prepareEventVariablesFriendTree2_default.py -q 1nh -N 50000 --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT1_shiftJEC/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_shiftJEC OUTPUT2_default_shiftJEC --tree treeProducerSusyMultilepton > lsub_all_2_default_shiftJEC.sh
chmod +x lsub_all_2_default_shiftJEC.sh

