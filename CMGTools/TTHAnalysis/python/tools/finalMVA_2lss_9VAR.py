from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS_9VAR:
    def __init__(self):
        self._MVAs = {}
        self._vars = [ 
                MVAVar("abs(LepGood2_eta)", func = lambda ev : abs(ev.LepGood2_eta)),
                #MVAVar("LepGood2_pt",     func = lambda ev : ev.LepGood2_pt),
                #MVAVar("mhtJet25",        func = lambda ev : ev.mhtJet25),
                MVAVar("mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                #MVAVar("MT_met_lep1",    func = lambda ev : ev.MT_met_lep1),
                MVAVar("htJet25",         func = lambda ev : ev.htJet25), 
		
		MVAVar("avg_dr_jet",      func = lambda ev : ev.avg_dr_jet),
                MVAVar("mindr_lep1_jet",   func = lambda ev : ev.mindr_lep1_jet),
                #MVAVar("MT_met_leplep",    func = lambda ev : ev.MT_met_leplep),
                
		#MVAVar("numJets_float",    func = lambda ev : ev.nJet25),
                
		#MVAVar("b1_jet_pt",      func = lambda ev : ev.Jet1_pt),
                #MVAVar("b2_jet_pt",      func = lambda ev : ev.Jet2_pt),
                #MVAVar("lep1Pt",         func = lambda ev : ev.LepGood1_pt),
                MVAVar("htJet25 - (sum_abspz - abs(sum_sgnpz))",    func = lambda ev : ev.htJet25 - (ev.sum_abspz - abs(ev.sum_sgnpz))),
                MVAVar("htJet25/sum_abspz",    func = lambda ev : ev.htJet25/ev.sum_abspz),
 
		MVAVar("m_tjjb := min(m_tjjb, 330)", func = lambda ev : min(ev.m_tjjb, 330)),
                MVAVar("m_tlvb := min(m_tlvb, 330)", func = lambda ev : min(ev.m_tlvb, 330)),
		#MVAVar("m_Wjj := min(m_Wjj, 330)", func = lambda ev : min(ev.m_Wjj, 330)),
                #MVAVar("mt_Wlv := min(mt_Wlv, 330)", func = lambda ev : min(ev.mt_Wlv, 330))
		
        ]
        
	#P="/afs/cern.ch/user/a/abrinke1/public/MultiLepton/BDT_weights/";
        #self._MVAs["MVA_2LSS_4j_6var"] = MVATool("MVA_2LSS_4j_6var", 
        #    P+"SS_ge4jge1t_useSide_2_6var_test/TMVAClassification_BDTG.weights.xml",
        #    self._vars)
        
	#P="/afs/cern.ch/work/m/mdjordje/CMG/TEST/CMSSW_5_3_14/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/weights/";
	#self._MVAs["MVA_2LSS_4j_8var"] = MVATool("MVA_2LSS_4j_8var", P+"ttbar_BDTG.weights.xml", self._vars)
	
	P="/afs/cern.ch/work/m/mdjordje/CMG/TEST/CMSSW_5_3_14/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/weights/";
	self._MVAs["MVA_2LSS_4j_9VAR"] = MVATool("MVA_2LSS_4j_9VAR", P+"ttbar_BDTG.weights.xml", self._vars)
	
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

