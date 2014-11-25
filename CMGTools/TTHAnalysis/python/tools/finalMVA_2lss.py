from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS:
    def __init__(self):
        self._MVAs = {}
        self._vars_23j_6var = [
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz)) := htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25-(ev.sum_abspz-abs(ev.sum_sgnpz))),
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
                MVAVar("mindr_lep1_jet := mindr_lep1_jet", func = lambda ev : ev.mindr_lep1_jet),
                MVAVar("ht2l := min(LepGood_pt[0]+LepGood_pt[1],300)", func = lambda ev : min(ev.LepGood_pt[0]+ev.LepGood_pt[1],300)),
                MVAVar("MHT := mhtJet25", func = lambda ev : ev.mhtJet25),
                MVAVar("Jet_pt2 := min((Jet_pt[0])if(nJet>0)else(0),(Jet_pt[1])if(nJet>1)else(0))", func = lambda ev : min((ev.Jet_pt[0])if(ev.nJet>0)else(0),(ev.Jet_pt[1])if(ev.nJet>1)else(0))),
        ]
        self._vars_4j_6var = [
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz)) := htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25-(ev.sum_abspz-abs(ev.sum_sgnpz))),
                MVAVar("MHT := mhtJet25", func = lambda ev : ev.mhtJet25),
                MVAVar("Jet2_btagCSV := max((Jet_btagCSV[1])if(nJet>1)else(-1),0)", func = lambda ev : max((ev.Jet_btagCSV[1])if(ev.nJet>1)else(-1),0)),
                MVAVar("mindr_lep1_jet := mindr_lep1_jet", func = lambda ev : ev.mindr_lep1_jet),
                MVAVar("max_Lep_eta := max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", func = lambda ev : max(abs(ev.LepGood_eta[0]),abs(ev.LepGood_eta[1]))),
        ]
        self._vars_5j_6var = [
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz)) := htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25-(ev.sum_abspz-abs(ev.sum_sgnpz))),
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
                MVAVar("MT_met_lep1 := MT_met_lep1", func = lambda ev : ev.MT_met_lep1),
                MVAVar("m_tjjb := min(m_tjjb, 330)", func = lambda ev : min(ev.m_tjjb, 330)),
                MVAVar("avg_dr_jet := avg_dr_jet", func = lambda ev : ev.avg_dr_jet),
                MVAVar("MHT := mhtJet25", func = lambda ev : ev.mhtJet25),
        ]
        self._vars_6j_6var = [
                MVAVar("m_tjjb := min(m_tjjb, 330)", func = lambda ev : min(ev.m_tjjb, 330)),
                MVAVar("MHT := mhtJet25", func = lambda ev : ev.mhtJet25),
                MVAVar("Jet2_btagCSV := max((Jet_btagCSV[1])if(nJet>1)else(-1),0)", func = lambda ev : max((ev.Jet_btagCSV[1])if(ev.nJet>1)else(-1),0)),
                MVAVar("avg_dr_jet := avg_dr_jet", func = lambda ev : ev.avg_dr_jet),
                MVAVar("mindr_lep1_jet := mindr_lep1_jet", func = lambda ev : ev.mindr_lep1_jet),
                MVAVar("min_Lep_eta := min(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", func = lambda ev : min(abs(ev.LepGood_eta[0]),abs(ev.LepGood_eta[1]))),
        ]
        self._vars_7j_6var = [
                MVAVar("htJet25-(sum_abspz-abs(sum_sgnpz)) := htJet25-(sum_abspz-abs(sum_sgnpz))", func = lambda ev : ev.htJet25-(ev.sum_abspz-abs(ev.sum_sgnpz))),
                MVAVar("lep2AbsEta := abs(LepGood_eta[1])", func = lambda ev : abs(ev.LepGood_eta[1])),
                MVAVar("Lep1_Q_eta := LepGood_eta[0]*LepGood_charge[0]", func = lambda ev : ev.LepGood_eta[0]*ev.LepGood_charge[0]),
                MVAVar("max_Lep_eta := max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", func = lambda ev : max(abs(ev.LepGood_eta[0]),abs(ev.LepGood_eta[1]))),
                MVAVar("min_Lep_eta := min(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", func = lambda ev : min(abs(ev.LepGood_eta[0]),abs(ev.LepGood_eta[1]))),
                MVAVar("MT_met_lep1 := MT_met_lep1", func = lambda ev : ev.MT_met_lep1),
        ]
        self._vars_8Lj_6var = [
                MVAVar("Jet2_btagCSV := max((Jet_btagCSV[1])if(nJet>1)else(-1),0)", func = lambda ev : max((ev.Jet_btagCSV[1])if(ev.nJet>1)else(-1),0)),
                MVAVar("MT_met_lep1 := MT_met_lep1", func = lambda ev : ev.MT_met_lep1),
                MVAVar("max_Lep_eta := max(abs(LepGood_eta[0]),abs(LepGood_eta[1]))", func = lambda ev : max(abs(ev.LepGood_eta[0]),abs(ev.LepGood_eta[1]))),
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
                MVAVar("mindr_lep2_jet := mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                MVAVar("mindr_lep1_jet := mindr_lep1_jet", func = lambda ev : ev.mindr_lep1_jet),
        ]
        P="/afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/";
        self._MVAs["MVA_2LSS_23j_6var"] = MVATool("MVA_2LSS_23j_6var",
            P+"ttbar_23j/weights/ttbar_23j_BDTG.weights.xml",
            self._vars_23j_6var)
        self._MVAs["MVA_2LSS_4j_6var"] = MVATool("MVA_2LSS_4j_6var",
            P+"ttbar_4j/weights/ttbar_4j_BDTG.weights.xml",
            self._vars_4j_6var)
        self._MVAs["MVA_2LSS_5j_6var"] = MVATool("MVA_2LSS_5j_6var",
            P+"ttbar_5j/weights/ttbar_5j_BDTG.weights.xml",
            self._vars_5j_6var)
        self._MVAs["MVA_2LSS_6j_6var"] = MVATool("MVA_2LSS_6j_6var",
            P+"ttbar_6j/weights/ttbar_6j_BDTG.weights.xml",
            self._vars_6j_6var)
        self._MVAs["MVA_2LSS_7j_6var"] = MVATool("MVA_2LSS_7j_6var",
            P+"ttbar_7j/weights/ttbar_7j_BDTG.weights.xml",
            self._vars_7j_6var)
        self._MVAs["MVA_2LSS_8Lj_6var"] = MVATool("MVA_2LSS_8Lj_6var",
            P+"ttbar_8Lj/weights/ttbar_8Lj_BDTG.weights.xml",
            self._vars_8Lj_6var)
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

