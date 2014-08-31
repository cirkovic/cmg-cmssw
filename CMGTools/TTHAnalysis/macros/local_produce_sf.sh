#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros

case $1 in
   1 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTH ;;
   2 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsSem ;;
   3 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 0 ;;
   4 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 1 ;;
   5 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 2 ;;
	6 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 3 ;;
	7 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 4 ;;
	8 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 5 ;;
	9 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 6 ;;
	10 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 7 ;;
	11 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTJetsLep -c 8 ;;
	12 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTWJets ;;
	13 )
		python prepareScaleFactorsFriendTree.py -N 500000 -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/30-08-2014/2/3 --vector  -d TTZJets ;;
esac

