from ROOT import *

f = TFile.Open("/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/20-08-2014/1/1/trainTTJetsSem2.root");
f.ls()

f.cd("rec")

c1 = TCanvas()
c1.SetLogy()
t.Draw("trkKink>>h_trkKink(100, 0, 30)")

c2 = TCanvas()
c2.SetLogy()
t.Draw("caloCompatibility>>h_caloCompatibility")

c3 = TCanvas()
c3.SetLogy()
t.Draw("globalTrackChi2>>h_globalTrackChi2(100, 0, 100)")

c4 = TCanvas()
c4.SetLogy()
t.Draw("trackerLayers>>h_trackerLayers")

input("Press enter to continue...")

