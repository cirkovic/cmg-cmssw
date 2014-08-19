cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros


source /afs/cern.ch/sw/lcg/external/gcc/4.9.1/x86_64-slc6-gcc48-opt/setup.sh
source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.20/x86_64-slc6-gcc48-opt/root/bin/thisroot.sh


#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTH

#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsSem

#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 0
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 1
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 2
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 3
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 4
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 5
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 6
#python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 7
python prepareEventVariablesFriendTree.py -N 500000 -T 'sf' -t treeProducerSusyMultilepton /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2 --vector  -d TTJetsLep -c 8

