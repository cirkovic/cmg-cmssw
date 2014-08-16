from ROOT import *

f = TFile.Open("/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/16-08-2014/trainTTJetsLep.root")
gDirectory.cd("rec")
c = TCanvas()
c.SetLogy()
t.Draw("pt>>hpt_1")
#c.Print("hpt_1.png")
#t.Draw("pt>>hpt_2(10, 0, 10000)")
#c.Print("hpt_2.png")
#t.Draw("pt>>htp_3(100, 0, 3000)")
#c.Print("hpt_3.png")
#t.Draw("pt>>htp_4(100, 0, 1500)")
#c.Print("hpt_4.png")
#t.Draw("pt>>htp_5(100, 0, 500)")
#c.Print("hpt_5.png")
input("Press Enter to continue...")

