from ROOT import *

file1 = TFile.Open("roc_2lss_mumu.root")
file2 = TFile.Open("roc_2lss_em.root")
file3 = TFile.Open("roc_2lss_ee.root")

graph1 = file1.Get("MVA")
graph2 = file2.Get("MVA")
graph3 = file3.Get("MVA")

graph1.SetLineColor(3)
graph2.SetLineColor(4)
graph3.SetLineColor(5)

c = TCanvas()
c.SetGrid()
graph1.Draw()
graph2.Draw("same")
graph3.Draw("same")

input("Press enter to continue...")

