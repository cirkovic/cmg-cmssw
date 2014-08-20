cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros

case $1 in
   1 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTH ;;
   2 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsSem ;;
   3 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 0 ;;
   4 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 1 ;;
   5 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 2 ;;
	6 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 3 ;;
	7 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 4 ;;
	8 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 5 ;;
	9 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 6 ;;
	10 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 7 ;;
	11 )
		python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 8 ;;
esac

