from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS_2:
    def __init__(self):
        self._MVAs = {}
        self._vars= [                 
                MVAVar("mhtJet25 := min(mhtJet25, 300)", func = lambda ev : min(ev.mhtJet25,300)),
                MVAVar("jet1Pt := min(Jet_pt[0], 300)", func = lambda ev : min(ev.Jet_pt[0],300)),
                MVAVar("jet2Pt := min(Jet_pt[1], 300)", func = lambda ev : min(ev.Jet_pt[1],300)),
                MVAVar("htJet25 := min(htJet25, 1000)", func = lambda ev : min(ev.htJet25,1000)),
                #MVAVar("htJet25ratio1224Lep := (LepGood_pt[0]*(abs(LepGood_eta[0])<1.2) + LepGood_pt[1]*(abs(LepGood_eta[1])<1.2) + Jet_pt[0]*(abs(Jet_eta[0]) < 1.2) + Jet_pt[1]*(abs(Jet_eta[1]) < 1.2) + Jet_pt[2]*(abs(Jet_eta[2]) < 1.2) + Jet_pt[3]*(abs(Jet_eta[3]) < 1.2) + Jet_pt[4]*(abs(Jet_eta[4]) < 1.2) + Jet_pt[5]*(abs(Jet_eta[5]) < 1.2) + Jet_pt[6]*(abs(Jet_eta[6]) < 1.2) + Jet_pt[7]*(abs(Jet_eta[7]) < 1.2))/ (LepGood_pt[0] + LepGood_pt[1] + Jet_pt[0]*(abs(Jet_eta[0]) < 2.4) + Jet_pt[1]*(abs(Jet_eta[1]) < 2.4) + Jet_pt[2]*(abs(Jet_eta[2]) < 2.4) + Jet_pt[3]*(abs(Jet_eta[3]) < 2.4) + Jet_pt[4]*(abs(Jet_eta[4]) < 2.4) + Jet_pt[5]*(abs(Jet_eta[5]) < 2.4) + Jet_pt[6]*(abs(Jet_eta[6]) < 2.4) + Jet_pt[7]*(abs(Jet_eta[7]) < 2.4))", func = lambda ev : (ev.LepGood_pt[0]*(abs(ev.LepGood_eta[0])<1.2) + ev.LepGood_pt[1]*(abs(ev.LepGood_eta[1])<1.2) + ev.Jet_pt[0]*(abs(ev.Jet_eta[0]) < 1.2) + ev.Jet_pt[1]*(abs(ev.Jet_eta[1]) < 1.2) + ev.Jet_pt[2]*(abs(ev.Jet_eta[2]) < 1.2) + ev.Jet_pt[3]*(abs(ev.Jet_eta[3]) < 1.2) + ev.Jet_pt[4]*(abs(ev.Jet_eta[4]) < 1.2) + ev.Jet_pt[5]*(abs(ev.Jet_eta[5]) < 1.2) + ev.Jet_pt[6]*(abs(ev.Jet_eta[6]) < 1.2) + ev.Jet_pt[7]*(abs(ev.Jet_eta[7]) < 1.2))/ (ev.LepGood_pt[0] + ev.LepGood_pt[1] + ev.Jet_pt[0]*(abs(ev.Jet_eta[0]) < 2.4) + ev.Jet_pt[1]*(abs(ev.Jet_eta[1]) < 2.4) + ev.Jet_pt[2]*(abs(ev.Jet_eta[2]) < 2.4) + ev.Jet_pt[3]*(abs(ev.Jet_eta[3]) < 2.4) + ev.Jet_pt[4]*(abs(ev.Jet_eta[4]) < 2.4) + ev.Jet_pt[5]*(abs(ev.Jet_eta[5]) < 2.4) + ev.Jet_pt[6]*(abs(ev.Jet_eta[6]) < 2.4) + ev.Jet_pt[7]*(abs(ev.Jet_eta[7]) < 2.4))),
                MVAVar("bestMTopHadPt := min(max(bestMTopHadPt,0),400)", func = lambda ev : min(max(ev.bestMTopHadPt,0),400)),
        ]
        P="/afs/cern.ch/work/c/cirkovic/Milos_11-07-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/ttbar_output/weights/";
        self._MVAs["finalMVA_2LSS_2"] = MVATool("ee", P+"ttbar_LD.weights.xml", self._vars, rarity=True) 
        
    def listBranches(self):
        return self._MVAs.keys()
    def __call__(self,event):
        return dict([ (name, mva(event)) for name, mva in self._MVAs.iteritems()])

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("ttHLepTreeProducerBase")
    #tree.AddFriend("sf/t", argv[2])
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = FinalMVA_2LSS_2()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

