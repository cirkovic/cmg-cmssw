from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
#from PhysicsTools.HeppyCore.utils.deltar import deltaR
from CMGTools.TTHAnalysis.leptonMVA import LeptonMVA
import os
import ROOT

        
class LeptonPrinter( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(LeptonPrinter,self).__init__(cfg_ana,cfg_comp,looperName)
        self.estimator = ROOT.heppy.EGammaMvaEleEstimatorFWLite()
        self.sxmls = ROOT.vector(ROOT.string)()
        weights_files = [
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml.gz",
        ]
        for f in weights_files: self.sxmls.push_back(f)
        #self.estimator.initialize("BDT", self.estimator.kNonTrigCSA14, True, self.sxmls)
        self.estimator.initialize("BDT", self.estimator.kNonTrigPhys14, True, self.sxmls)
        #self.estimator.initialize("BDT", self.estimator.kNonTrigPhys14, False, self.sxmls)

        self.estimator1 = ROOT.heppy.EGammaMvaEleEstimatorFWLite()
        self.sxmls = ROOT.vector(ROOT.string)()
        weights_files = [
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EB_5_25ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EE_5_25ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EB_10_25ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EE_10_25ns_BDT.weights.xml.gz",
        ]
        for f in weights_files: self.sxmls.push_back(f)
        #self.estimator1.initialize("BDT1", self.estimator1.kNonTrigCSA14, True, self.sxmls)
        self.estimator1.initialize("BDT1", self.estimator1.kNonTrigCSA14, False, self.sxmls)
        
        self.estimator2 = ROOT.heppy.EGammaMvaEleEstimatorFWLite()
        self.sxmls = ROOT.vector(ROOT.string)()
        weights_files = [
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EB_5_50ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EE_5_50ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EB_10_50ns_BDT.weights.xml.gz",
            "EgammaAnalysis/ElectronTools/data/CSA14/EIDmva_EE_10_50ns_BDT.weights.xml.gz",
        ]
        for f in weights_files: self.sxmls.push_back(f)
        #self.estimator2.initialize("BDT2", self.estimator2.kNonTrigCSA14, True, self.sxmls)
        self.estimator2.initialize("BDT2", self.estimator2.kNonTrigCSA14, False, self.sxmls)

        self.estimator3 = ROOT.heppy.EGammaMvaEleEstimatorFWLite()
        self.sxmls = ROOT.vector(ROOT.string)()
        weights_files = [
             "EgammaAnalysis/ElectronTools/data/CSA14/TrigIDMVA_50ns_EB_BDT.weights.xml.gz",
             "EgammaAnalysis/ElectronTools/data/CSA14/TrigIDMVA_50ns_EE_BDT.weights.xml.gz",
        ]
        for f in weights_files: self.sxmls.push_back(f)
        #self.estimator3.initialize("BDT3", self.estimator3.kTrigCSA14, True, self.sxmls)
        self.estimator3.initialize("BDT3", self.estimator3.kTrigCSA14, False, self.sxmls)

        self.estimator4 = ROOT.heppy.EGammaMvaEleEstimatorFWLite()
        self.sxmls = ROOT.vector(ROOT.string)()
        weights_files = [
             "EgammaAnalysis/ElectronTools/data/CSA14/TrigIDMVA_25ns_EB_BDT.weights.xml.gz",
             "EgammaAnalysis/ElectronTools/data/CSA14/TrigIDMVA_25ns_EE_BDT.weights.xml.gz",
        ]
        for f in weights_files: self.sxmls.push_back(f)
        #self.estimator4.initialize("BDT4", self.estimator4.kTrigCSA14, True, self.sxmls)
        self.estimator4.initialize("BDT4", self.estimator4.kTrigCSA14, False, self.sxmls)

        self.leptonMVAKindTTH = getattr(self.cfg_ana, "leptonMVAKindTTH", "Susy")
        #self.leptonMVAKindTTH = "SusyWithBoost" # --- <FATAL> BDTG                     : You declared 12 variables in the Reader while there are 9 variables declared in the file
        self.leptonMVAPathTTH = getattr(self.cfg_ana, "leptonMVAPathTTH", "CMGTools/TTHAnalysis/data/leptonMVA/tth/%s_BDTG.weights.xml")
        if self.leptonMVAPathTTH[0] != "/": self.leptonMVAPathTTH = "%s/src/%s" % ( os.environ['CMSSW_BASE'], self.leptonMVAPathTTH)
        if self.cfg_ana.printMVA:
            self.leptonMVATTH = LeptonMVA(self.leptonMVAKindTTH, self.leptonMVAPathTTH, self.cfg_comp.isMC, self.cfg_ana.fname)
        else:
            self.leptonMVATTH = LeptonMVA(self.leptonMVAKindTTH, self.leptonMVAPathTTH, self.cfg_comp.isMC)

        with open(self.cfg_ana.fname, 'w') as f:
            f.write('run:ls:event:pdgId:pT:Eta:Phi:dxy:dz:relIso:sip3D\n')
            #f.write('run:ls:event:pdgId:pT:Eta:Phi:dxy:dz:relIso:sip3D:prompt MVA:ele MVA ID / isPFMuon:lost hits / isGlobalMuon:isGsfCtfScPixChargeConsistent / chargeFlip:passConversionVeto / isTrackerMuon:global normalized chi2:chi2 local:track kink:valid Frac:segment compatibility\n')
            #f.write('run:ls:event,pdgId,pT,Eta,Phi,dxy,dz,relIso,sip3D,prompt MVA,ele MVA ID / isPFMuon,lost hits / isGlobalMuon,isGsfCtfScPixChargeConsistent / chargeFlip,passConversionVeto / isTrackerMuon,global normalized chi2,chi2 local,track kink,valid Frac,segment compatibility,\n')
            #f.write('event,pdgId,pT,Eta,Phi,dxy,dz,relIso,sip3D,prompt MVA,ele MVA ID / isPFMuon,lost hits / isGlobalMuon,isGsfCtfScPixChargeConsistent / chargeFlip,passConversionVeto / isTrackerMuon,global normalized chi2,chi2 local,track kink,valid Frac,segment compatibility,isLooseMuon\n')

    def declareHandles(self):
        super(LeptonPrinter, self).declareHandles()

    def beginLoop(self, setup):
        super(LeptonPrinter,self).beginLoop(setup)
        #self.counters.addCounter('events')
        #count = self.counters.counter('events')
        #count.register('all events')
        #count.register('accepted events')

    def PrintLeptons(self, event):
        #slines = []
        for ele in event.selectedElectrons:
             #if (event.genHiggsDecayMode in [15, 23, 24]) and len(event.selectedLeptons) == 2:
             if True:
                  #event,pdgId,pT,Eta,Phi,dxy,dz,relIso,sip3D,prompt MVA,ele MVA ID,lost hits,isGsfCtfScPixChargeConsistent,passConversionVeto
                  sline = ""
                  sline += "%d:" % event.run
                  sline += "%d:" % event.lumi
                  sline += "%d:" % event.eventId
                  #sline += "%d," % event.genHiggsDecayMode
                  #sline += "%d," % len(event.selectedLeptons)
                  sline += "%+d:" % ele.pdgId()
                  sline += "%6.6g:" % ele.pt()
                  sline += "%+6.6g:" % ele.eta()
                  sline += "%+6.6g:" % ele.phi()
                  sline += "%6.6g:" % abs(ele.dxy())
                  sline += "%6.6g:" % abs(ele.dz())
                  sline += "%6.6g:" % ele.relIso03
                  sline += "%6.6g" % ele.sip3D()
                  '''
                  #sline += ","
                  #sline += "%6.6g," % ele.mvaValueTTH
                  #sline += "%6.6g," % ele.mvaValueSusy
                  sline += "%6.6g," % self.leptonMVATTH(ele)
                  sline += "%6.6g," % ele.mvaRun2("NonTrigPhys14")
#                  sline += "%6.6g," % self.estimator.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, True, self.cfg_ana.fname)
#                  sline += "%6.6g," % self.estimator.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, True, self.cfg_ana.fname)
 #                 sline += "%6.6g," % self.estimator.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, True)
 #                 sline += "%6.6g," % self.estimator.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, True)
                  #sline += "%6.6g," % self.estimator.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, False)
 #                 sline += "%6.6g," % self.estimator1.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, False)
 #                 sline += "%6.6g," % self.estimator1.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, False)
 #                 sline += "%6.6g," % self.estimator2.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, False)
 #                 sline += "%6.6g," % self.estimator2.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, False)
 #                 sline += "%6.6g," % self.estimator3.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, False)
 #                 sline += "%6.6g," % self.estimator3.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, False)
 #                 sline += "%6.6g," % self.estimator4.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, True, False)
 #                 sline += "%6.6g," % self.estimator4.mvaValue(ele.physObj, ele.associatedVertex, ele.rho, False, False)
                  #sline += ","
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Loose")
 #                 sline += "%6.6g," % ele.electronID("POG_MVA_ID_Run2_NonTrig_Loose") #POG_MVA_ID_NonTrig_full5x5
                  #sline += "%6.6g," % ele.mvaNonTrigV0(False)
                  #  sline += "%6.6g," % ele.mvaNonTrigV0(full5x5=True) #POG_MVA_ID_NonTrig_full5x5
                  #sline += "%6.6g," % ele.mvaIDLoose()
                  #sline += "%6.6g," % ele.mvaIDTight()
                  #sline += "%6.6g," % ele.mvaIDLoose(full5x5=True)
                  #sline += "%6.6g," % ele.mvaIDTight(full5x5=True)
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Loose")
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Tight")
                  #sline += "%d," % ele.lostInner()
                  sline += "%d," % ele.gsfTrack().hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS)
                  sline += "%d," % ele.isGsfCtfScPixChargeConsistent()
                  sline += "%d" % ele.passConversionVeto()
                  #sline += ","
                  #sline += "%6.6g," % ele.mvaRun2("NonTrigPhys14","Tight")
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Loose")
                  #sline += "%6.6g," % ele.mvaNonTrigV0(False)
                  #sline += "%6.6g," % ele.mvaNonTrigV0(True) #POG_MVA_ID_NonTrig_full5x5
                  #sline += "%6.6g," % ele.mvaIDLoose()
                  #sline += "%6.6g," % ele.mvaIDTight()
                  #sline += "%6.6g," % ele.mvaIDLoose(full5x5=True)
                  #sline += "%6.6g," % ele.mvaIDTight(full5x5=False)
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Loose")
                  #sline += "%6.6g," % ele.mvaIDRun2("NonTrigPhys14","Tight")
                  '''
                  sline += "\n"
                  sline = sline.replace(" ", "")
                  #f.write(sline)
                  #slines.append(sline)
                  if self.cfg_ana.printMVA:
                      f = open(self.cfg_ana.fname, "r")
                      contents = f.readlines()
                      f.close()
                      contents.insert(-3, sline)
                      f = open(self.cfg_ana.fname, "w")
                      contents = "".join(contents)
                      f.write(contents)
                      f.close()
                  else:
                      f = open(self.cfg_ana.fname, "a")
                      f.write(sline)
                      f.close()

        for mu in event.selectedMuons:
             #if (event.genHiggsDecayMode in [15, 23, 24]) and len(event.selectedLeptons) == 2:
             if True:
                  #event,pdgId,pT,Eta,Phi,dxy,dz,relIso,sip3D,prompt MVA,isPFMuon,isGlobalMuon,chargeFlip,isTrackerMuon,global normalized chi2,chi2 local,track kink,valid Frac,segment compatibility,isLooseMuon
                  sline = ""
                  sline += "%d:" % event.run
                  sline += "%d:" % event.lumi
                  sline += "%d:" % event.eventId
                  #sline += "%d," % event.genHiggsDecayMode
                  #sline += "%d," % len(event.selectedLeptons)
                  sline += "%+d:" % mu.pdgId()
                  sline += "%6.6g:" % mu.pt()
                  sline += "%+6.6g" % mu.eta()
                  sline += "%+6.6g:" % mu.phi()
                  sline += "%6.6g:" % abs(mu.dxy())
                  sline += "%6.6g:" % abs(mu.dz())
                  sline += "%6.6g:" % mu.relIso03
                  sline += "%6.6g" % mu.sip3D()
                  '''
                  #sline += "%6.6g," % mu.muonID("POG_ID_Medium")
                  #sline += "%6.6g," % mu.physObj.isLooseMuon()
                  #sline += "%6.6g," % mu.segmentCompatibility()
                  #sline += "%6.6g," % mu.mvaRun2("NonTrigPhys14")
                  #sline += "%6.6g," % mu.mvaValueTTH
                  #sline += "%6.6g," % mu.mvaValueSusy
                  sline += "%6.6g," % self.leptonMVATTH(mu)
                  sline += "%d,"% mu.isPFMuon()
                  sline += "%d,"% mu.isGlobalMuon()
                  sline += "%6.6g," % (mu.innerTrack().ptError()/mu.innerTrack().pt())
                  sline += "%d," % mu.isTrackerMuon()
                  sline += "%6.6g," % (mu.globalTrack().normalizedChi2() if mu.isPFMuon() and mu.isGlobalMuon() else -1)
                  sline += "%6.6g," % mu.combinedQuality().chi2LocalPosition
                  sline += "%6.6g," % mu.combinedQuality().trkKink
                  sline += "%6.6g," % mu.innerTrack().validFraction()
                  sline += "%6.6g" % mu.segmentCompatibility()
                  #sline += "%6.6g" % mu.physObj.isLooseMuon()
                  '''
                  sline += "\n"
                  sline = sline.replace(" ", "")
                  #f.write(sline)
                  #slines.append(sline)
                  if self.cfg_ana.printMVA:
                      f = open(self.cfg_ana.fname, "r")
                      contents = f.readlines()
                      f.close()
                      contents.insert(-3, sline)
                      f = open(self.cfg_ana.fname, "w")
                      contents = "".join(contents)
                      f.write(contents)
                      f.close()
                  else:
                      f = open(self.cfg_ana.fname, "a")
                      f.write(sline)
                      f.close()

        #with open(self.cfg_ana.fname, 'a') as f:
#             for sline in slines:
#                  f.write(sline)

#        f = open(self.cfg_ana.fname, "r")
#        contents = f.readlines()
#        f.close()

#        for sline in slines:
#             contents.insert(-3, sline)

#        f = open(self.cfg_ana.fname, "w")
#        contents = "".join(contents)
#        f.write(contents)
#        f.close()

    def process(self, event):
        self.readCollections( event.input )
        #self.counters.counter('events').inc('all events')
        
        #print "CIRKOVIC in PrintLeptons"

        #if hasattr(self.cfg_ana, 'minJets25'):
        #    n25 = len([ j for j in event.cleanJets if j.pt() > 25 ])
        #    if n25 < self.cfg_ana.minJets25: 
        #        return False

        #self.makeHadTopDecays(event)
        self.PrintLeptons(event)

        #self.counters.counter('events').inc('accepted events')
        return True
