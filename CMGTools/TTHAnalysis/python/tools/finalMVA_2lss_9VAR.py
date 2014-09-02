from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS_9VAR:
    def __init__(self):
        self._MVAs = {}
        self._vars_1_9 = [
                MVAVar("abs(LepGood_eta[1])", func = lambda ev : abs(ev.LepGood_eta[1])),
                MVAVar("mindr_lep2_jet",    func = lambda ev : ev.mindr_lep2_jet),
                MVAVar("htJet25",           func = lambda ev : ev.htJet25),
                MVAVar("avg_dr_jet",        func = lambda ev : ev.avg_dr_jet),
                MVAVar("mindr_lep1_jet",    func = lambda ev : ev.mindr_lep1_jet),
                MVAVar("htJet25 - (sum_abspz - abs(sum_sgnpz))",    func = lambda ev : ev.htJet25 - (ev.sum_abspz - abs(ev.sum_sgnpz))),
                MVAVar("htJet25/sum_abspz",    func = lambda ev : ev.htJet25/ev.sum_abspz),
                MVAVar("m_tjjb := min(m_tjjb, 330)", func = lambda ev : min(ev.m_tjjb, 330)),
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
        ]

        P="/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/2/";
        self._MVAs["MVA_2LSS_4j_9var"] = MVATool("MVA_2LSS_4j_9var",
            P+"9VAR/ttbar/weights/ttbar_BDTG.weights.xml",
            self._vars_1_9)

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
            self.sf = FinalMVA_2LSS_9VAR()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

