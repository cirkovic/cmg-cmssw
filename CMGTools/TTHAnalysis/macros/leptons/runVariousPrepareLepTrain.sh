for j in 25ns 50ns
do
	for i in `ls /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/$j`
	do
   	 python prepareLepTrain.py /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/$j/$i train$i.root --vector --tree treeProducerSusyMultilepton
	done
done

