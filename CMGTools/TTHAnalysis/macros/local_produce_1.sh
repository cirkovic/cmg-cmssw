#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros

case $1 in
   1 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTH ;;
   2 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsSem ;;
   3 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 0 ;;
   4 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 1 ;;
   5 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 2 ;;
	6 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 3 ;;
	7 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 4 ;;
	8 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 5 ;;
	9 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 6 ;;
	10 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 7 ;;
	11 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTJetsLep -c 8 ;;
	12 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTWJets ;;
	13 )
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d TTZJets ;;
	14 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 0 ;;
	15 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 1 ;;
	16 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 2 ;;
	17 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 3 ;;
	18 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 4 ;;
	19 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronAB -c 5 ;;
	20 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 0 ;;
	21 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 1 ;;
	22 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 2 ;;
	23 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 3 ;;
	24 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 4 ;;
	25 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 5 ;;
	26 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronC -c 6 ;;
	27 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 0 ;;
	28 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 1 ;;
	29 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 2 ;;
	30 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 3 ;;
	31 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 4 ;;
	32 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 5 ;;
	33 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleElectronD -c 6 ;;
	34 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 0 ;;
	35 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 1 ;;
	36 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 2 ;;
	37 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 3 ;;
	38 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 4 ;;
	39 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 5 ;;
	40 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 6 ;;
	41 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 7 ;;
	42 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuAB -c 8 ;;
	43 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 0 ;;
	44 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 1 ;;
	45 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 2 ;;
	46 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 3 ;;
	47 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 4 ;;
	48 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 5 ;;
	49 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 6 ;;
	50 )	
		python prepareEventVariablesFriendTree_1.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/c/cirkovic/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1 --vector  -d DoubleMuC -c 7 ;;
esac

