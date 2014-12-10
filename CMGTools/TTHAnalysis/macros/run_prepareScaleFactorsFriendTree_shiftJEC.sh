#!/bin/sh

mkdir OUTPUT_SF_shiftJEC
python prepareScaleFactorsFriendTree.py -q 1nh -N 50000 /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_shiftJEC OUTPUT_SF_shiftJEC > lsub_all_sf_shiftJEC.sh --tree treeProducerSusyMultilepton
chmod +x lsub_all_sf_shiftJEC.sh

