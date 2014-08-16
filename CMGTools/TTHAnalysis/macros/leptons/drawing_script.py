from ROOT import *
import sys

f = TFile.Open("/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/16-08-2014/trainTTJetsLep.root")
gDirectory.cd("rec")

t.Draw(">>elist", "pt<1000")
elist = gDirectory.Get("elist");
t.SetEventList(elist)

c = TCanvas()
c.SetLogy()
t.Draw("pt>>hpt_1")
#c.Print("hpt_1.png")

input("Press Enter to continue...")

sys.exit()

t.Draw("pt>>hpt_2(100, 0, 10000)")
#c.Print("hpt_2.png")
t.Draw("pt>>htp_3(100, 0, 5000)")
#c.Print("hpt_3.png")
t.Draw("pt>>htp_4(100, 0, 1750)")
#c.Print("hpt_4.png")
t.Draw("pt>>htp_5(100, 0, 1500)")
#c.Print("hpt_5.png")
t.Draw("pt>>htp_6(100, 0, 1300)")
#c.Print("hpt_6.png")
t.Draw("pt>>htp_7(100, 0, 1000)")
#c.Print("hpt_7.png")
input("Press Enter to continue...")

