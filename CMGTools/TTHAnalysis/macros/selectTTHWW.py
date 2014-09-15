from ROOT import *

f1 = TFile.Open("TTH/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root")
t1 = f1.Get("treeProducerSusyMultilepton")
#t1.Print()
print t1.GetEntries()
t1.Draw(">>elist","GenHiggsDecayMode == 24")
elist = gDirectory.Get("elist")
t1.SetEventList(elist)
f2 = TFile("TTHWW/treeProducerSusyMultilepton/treeProducerSusyMultilepton_tree.root","RECREATE")
t2 = t1.CopyTree("")
print t2.GetEntries()
t2.Write()
f2.Close()

