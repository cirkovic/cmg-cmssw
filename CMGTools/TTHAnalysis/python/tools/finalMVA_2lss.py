from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS:
    def __init__(self):
        self._MVAs = {}
        self._vars_23j = [ 
                MVAVar("abs(LepGood2_eta)", func = lambda ev : abs(ev.LepGood2_eta)),
                MVAVar("mhtJet25", func = lambda ev : ev.mhtJet25),
                MVAVar("MT_met_lep1", func = lambda ev : ev.MT_met_lep1),
                MVAVar("htJet25", func = lambda ev : ev.htJet25),
                MVAVar("MT_met_leplep", func = lambda ev : ev.MT_met_leplep),
                MVAVar("Jet1_pt", func = lambda ev : ev.Jet1_pt),
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25 - (ev.sum_abspz - abs(ev.sum_sgnpz))),
        ]
        self._vars_4j = [
                MVAVar("abs(LepGood2_eta)", func = lambda ev : abs(ev.LepGood2_eta)),
                MVAVar("mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                MVAVar("htJet25", func = lambda ev : ev.htJet25),
                MVAVar("mindr_lep1_jet", func = lambda ev : ev.mindr_lep1_jet),
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25 - (ev.sum_abspz - abs(ev.sum_sgnpz))),
                MVAVar("htJet25/sum_abspz", func = lambda ev : ev.htJet25/ev.sum_abspz),
                MVAVar("min(m_tjjb,330)", func = lambda ev : min(ev.m_tjjb, 330)),
                MVAVar("min(m_tlvb,330)", func = lambda ev : min(ev.m_tlvb, 330)),
        ]
        P="/afs/cern.ch/work/c/cirkovic/Categorization_240914/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/"
        self._MVAs["MVA_2LSS_23j"] = MVATool("MVA_2LSS_23j", 
            P+"23j/weights/ttbar_BDTG.weights.xml",
            self._vars_23j)
        self._MVAs["MVA_2LSS_4j"] = MVATool("MVA_2LSS_4j", 
            P+"4j/weights/ttbar_BDTG.weights.xml",
            self._vars_4j)
        self._MVAs["MVA_2LSS_23j_2l_cat"] = CategorizedMVA(
            [ ( lambda ev: abs(ev.LepGood1_pdgId) == 11 and abs(ev.LepGood2_pdgId) == 11,
                    MVATool("MVA_2LSS_23j_ee", P+"23j/weights/ttbar_BDTG.weights.xml", self._vars_23j) ),
              ( lambda ev: abs(ev.LepGood1_pdgId) == 13 and abs(ev.LepGood2_pdgId) == 13,
                    MVATool("MVA_2LSS_23j_mm", P+"23j/weights/ttbar_BDTG.weights.xml", self._vars_23j) ),
              ( lambda ev: abs(ev.LepGood1_pdgId) != abs(ev.LepGood2_pdgId),
                    MVATool("MVA_2LSS_23j_em", P+"23j/weights/ttbar_BDTG.weights.xml", self._vars_23j) ) ]
        )
        self._MVAs["MVA_2LSS_4j_2l_cat"] = CategorizedMVA(
            [ ( lambda ev: abs(ev.LepGood1_pdgId) == 11 and abs(ev.LepGood2_pdgId) == 11,
                    MVATool("MVA_2LSS_4j_ee", P+"4j/weights/ttbar_BDTG.weights.xml", self._vars_4j) ),
              ( lambda ev: abs(ev.LepGood1_pdgId) == 13 and abs(ev.LepGood2_pdgId) == 13,
                    MVATool("MVA_2LSS_4j_mm", P+"4j/weights/ttbar_BDTG.weights.xml", self._vars_4j) ),
              ( lambda ev: abs(ev.LepGood1_pdgId) != abs(ev.LepGood2_pdgId),
                    MVATool("MVA_2LSS_4j_em", P+"4j/weights/ttbar_BDTG.weights.xml", self._vars_4j) ) ]
        )
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

