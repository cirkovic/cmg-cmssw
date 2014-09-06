#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros

case $1 in
   1 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/06-09-2014/1 --vector  -d DYJetsM10 ;;
esac

