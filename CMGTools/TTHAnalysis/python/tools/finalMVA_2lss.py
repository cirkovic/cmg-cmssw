from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS:
    def __init__(self):
        self._MVAs = {}
        self._vars_1_6 = [ 
                MVAVar("abs(LepGood_eta[1])", func = lambda ev : abs(ev.LepGood_eta[1])),
                MVAVar("LepGood_pt[1]",     func = lambda ev : ev.LepGood_pt[1]),
                MVAVar("mhtJet25",        func = lambda ev : ev.mhtJet25),
                MVAVar("mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                MVAVar("MT_met_lep1",    func = lambda ev : ev.MT_met_lep1),
                MVAVar("htJet25",         func = lambda ev : ev.htJet25) 
        ]
        P="/afs/cern.ch/user/c/cirkovic/www/25-03-2015/Trainings/2/finalMVA/categorized/TTBAR_TTW/";
        self._MVAs["MVA_2LSS_default_ttbar"] = MVATool("MVA_2LSS_default_ttbar", 
            P+"ttbar_default/weights/ttbar_default_BDTG.weights.xml",
            self._vars_1_6)
        self._MVAs["MVA_2LSS_default_ttW"] = MVATool("MVA_2LSS_default_ttW",
            P+"ttW_default/weights/ttW_default_BDTG.weights.xml",
            self._vars_1_6)
    def listBranches(self):
        return self._MVAs.keys()
    def __call__(self,event):
        return dict([ (name, mva(event)) for name, mva in self._MVAs.iteritems()])

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("ttHLepTreeProducerBase")
    tree.AddFriend("sf/t", argv[2])
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = FinalMVA_2LSS()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

