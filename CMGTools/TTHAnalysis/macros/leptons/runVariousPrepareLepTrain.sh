for i in `ls /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/25ns`
do
    python prepareLepTrain.py /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/25ns/$i train$i.root --vector --tree treeProducerSusyMultilepton
done

