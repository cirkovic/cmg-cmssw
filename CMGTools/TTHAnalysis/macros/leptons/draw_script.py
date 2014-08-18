from ROOT import *
import time

#file = TFile.Open("/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/18-08-2014/1/trainTTJetsLepSig.root")
file = TFile.Open("/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/18-08-2014/1/trainTTJetsLepBgd.root")
file.cd("rec")

c_1 = TCanvas()
c_1.SetLogy()
t.Draw("pt>>hpt_1")
#time.sleep(1)
#c.Print("hpt_1.png")

c_2 = TCanvas()
c_2.SetLogy()
#t.Draw("pt>>hpt_2(100, 0, 1000)")
t.Draw("pt>>hpt_2(100, 0, 500)")
#time.sleep(1)
#c.Print("hpt_2.png")

c_3 = TCanvas()
c_3.SetLogy()
#t.Draw("pt>>hpt_3(100, 0, 800)")
t.Draw("pt>>hpt_3(100, 0, 400)")
#time.sleep(1)
#c.Print("hpt_3.png")

input("Press Enter to continue...")

