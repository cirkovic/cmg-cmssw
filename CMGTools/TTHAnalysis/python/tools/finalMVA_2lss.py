from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *

class FinalMVA_2LSS:
    def __init__(self):
        self._MVAs = {}
        self._vars_1_6 = [ 
                ##MVAVar("lep2AbsEta", func = lambda ev : min(abs(ev.LepGood[0]_eta),abs(ev.LepGood[1]_eta))),
                #MVAVar("lep2AbsEta", func = lambda ev : ev.lep2AbsEta),
                #MVAVar("lep2Pt",     func = lambda ev : ev.lep2Pt),
                #MVAVar("MHT",        func = lambda ev : ev.MHT),
                #MVAVar("mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                #MVAVar("MT_met_lep1",    func = lambda ev : ev.MT_met_lep1),
                #MVAVar("sum_pt",         func = lambda ev : ev.sum_pt) 
                
                #MVAVar("lep2AbsEta", func = lambda ev : min(abs(ev.LepGood[0]_eta),abs(ev.LepGood[1]_eta))),
                MVAVar("abs(LepGood_eta[1])", func = lambda ev : abs(ev.LepGood_eta[1])),
                MVAVar("LepGood_pt[1]",     func = lambda ev : ev.LepGood_pt[1]),
                MVAVar("mhtJet25",        func = lambda ev : ev.mhtJet25),
                MVAVar("mindr_lep2_jet", func = lambda ev : ev.mindr_lep2_jet),
                MVAVar("MT_met_lep1",    func = lambda ev : ev.MT_met_lep1),
                MVAVar("htJet25",         func = lambda ev : ev.htJet25)
                
#   factory->AddVariable("lep2AbsEta := abs(LepGood_eta[1])", 'F');
#   factory->AddVariable("lep2Pt := LepGood_pt[1]", 'F');
#   factory->AddVariable("MHT : = mhtJet25", 'F');
#   factory->AddVariable("mindr_lep2_jet : = mindr_lep2_jet", 'F');
#   factory->AddVariable("MT_met_lep1 : = MT_met_lep1", 'F');
#   factory->AddVariable("sum_pt : = htJet25", 'F');

# <Variables NVar="6">
#   <Variable VarIndex="0" Expression="abs(LepGood_eta[1])" Label="lep2AbsEta" Title="lep2AbsEta" Unit="" Internal="lep2AbsEta" Type="F" Min="4.14125301e-04" Max="2.39864707e+00"/>
#   <Variable VarIndex="1" Expression="LepGood_pt[1]" Label="lep2Pt" Title="lep2Pt" Unit="" Internal="lep2Pt" Type="F" Min="2.00183353e+01" Max="2.89519775e+02"/>
#   <Variable VarIndex="2" Expression="mhtJet25" Label="MHT" Title="MHT" Unit="" Internal="MHT" Type="F" Min="3.35981560e+00" Max="5.82284241e+02"/>
#   <Variable VarIndex="3" Expression="mindr_lep2_jet" Label="mindr_lep2_jet" Title="mindr_lep2_jet" Unit="" Internal="mindr_lep2_jet" Type="F" Min="3.75625700e-01" Max="3.77640629e+00"/>
#   <Variable VarIndex="4" Expression="MT_met_lep1" Label="MT_met_lep1" Title="MT_met_lep1" Unit="" Internal="MT_met_lep1" Type="F" Min="7.54927099e-02" Max="7.47827637e+02"/>
#   <Variable VarIndex="5" Expression="htJet25" Label="sum_pt" Title="sum_pt" Unit="" Internal="sum_pt" Type="F" Min="1.95648254e+02" Max="2.18754688e+03"/>
# </Variables>
        ]
        P="/afs/cern.ch/work/c/cirkovic/Milos_02-10-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/finalMVA/2lss/";
        self._MVAs["MVA_2LSS_4j_6var_25ns"] = MVATool("MVA_2LSS_4j_6var_25ns", 
            P+"25ns/weights/ttbar_BDTG.weights.xml",
            self._vars_1_6)
        self._MVAs["MVA_2LSS_4j_6var_50ns"] = MVATool("MVA_2LSS_4j_6var_50ns",
            P+"50ns/weights/ttbar_BDTG.weights.xml",
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

