from ROOT import *

f = TFile('/afs/cern.ch/work/c/cirkovic/Milos_11-07-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/TEST_TTH_vs_TTJets_PU20bx25_Output_Directory/TTHTauTau_PU20bx25/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root')
f.ls()
treeProducerSusyMultilepton.Print()
alist = []
for event in treeProducerSusyMultilepton:
	print event.LepGood_eta
	for entry in event.LepGood_eta:
		print entry
	alist += [event.LepGood_eta]
print len(alist)

