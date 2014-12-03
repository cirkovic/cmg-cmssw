import os

from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle
from CMGTools.RootTools.physicsobjects.Electron import Electron
from CMGTools.RootTools.physicsobjects.Muon import Muon
from CMGTools.TTHAnalysis.tools.EfficiencyCorrector import EfficiencyCorrector

from CMGTools.RootTools.utils.DeltaR import bestMatch, bestMatch1, bestMatchPrint
from CMGTools.RootTools.physicsobjects.RochesterCorrections import rochcor
from CMGTools.RootTools.physicsobjects.MuScleFitCorrector   import MuScleFitCorr
from CMGTools.RootTools.physicsobjects.ElectronCalibrator import EmbeddedElectronCalibrator
from CMGTools.TTHAnalysis.electronCalibrator import ElectronCalibrator
from CMGTools.TTHAnalysis.tools.MuonMVA import MuonMVA

from ROOT import CMGMuonCleanerBySegmentsAlgo
cmgMuonCleanerBySegments = CMGMuonCleanerBySegmentsAlgo()

class ttHLepAnalyzerSusy( Analyzer ):

    
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(ttHLepAnalyzerSusy,self).__init__(cfg_ana,cfg_comp,looperName)
        if self.cfg_ana.doMuScleFitCorrections and self.cfg_ana.doMuScleFitCorrections != "none":
            if self.cfg_ana.doMuScleFitCorrections not in [ "none", "prompt", "prompt-sync", "rereco", "rereco-sync" ]:
                raise RuntimeError, 'doMuScleFitCorrections must be one of "none", "prompt", "prompt-sync", "rereco", "rereco-sync"'
            rereco = ("prompt" not in self.cfg_ana.doMuScleFitCorrections)
            sync   = ("sync"       in self.cfg_ana.doMuScleFitCorrections)
            self.muscleCorr = MuScleFitCorr(cfg_comp.isMC, rereco, sync)
            if hasattr(self.cfg_ana, "doRochesterCorrections") and self.cfg_ana.doRochesterCorrections:
                raise RuntimeError, "You can't run both Rochester and MuScleFit corrections!"
        else:
            self.cfg_ana.doMuScleFitCorrections = False
        if self.cfg_ana.doElectronScaleCorrections == "embedded":
            self.electronEnergyCalibrator = EmbeddedElectronCalibrator()
        else:
            self.electronEnergyCalibrator = ElectronCalibrator(cfg_comp.isMC)
        if hasattr(cfg_comp,'efficiency'):
            self.efficiency= EfficiencyCorrector(cfg_comp.efficiency)
        self.muonMVAIdFull = MuonMVA("Full", "%s/src/CMGTools/TTHAnalysis/data/leptonMVA/muonMVAId_train70XFull_BDTG.weights.xml" % os.environ['CMSSW_BASE'])
    #----------------------------------------
    # DECLARATION OF HANDLES OF LEPTONS STUFF   
    #----------------------------------------
        

    def declareHandles(self):
        super(ttHLepAnalyzerSusy, self).declareHandles()

        #leptons
        self.handles['muons'] = AutoHandle(self.cfg_ana.muons,"std::vector<pat::Muon>")            
        self.handles['electrons'] = AutoHandle(self.cfg_ana.electrons,"std::vector<pat::Electron>")            
    
        #rho for muons
        self.handles['rhoMu'] = AutoHandle( self.cfg_ana.rhoMuon, 'double')
        #rho for electrons
        self.handles['rhoEle'] = AutoHandle( self.cfg_ana.rhoElectron, 'double')

    def beginLoop(self):
        super(ttHLepAnalyzerSusy,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')

    #------------------
    # MAKE LEPTON LISTS
    #------------------

    
    def makeLeptons(self, event):
        ### inclusive leptons = all leptons that could be considered somewhere in the analysis, with minimal requirements (used e.g. to match to MC)
        event.inclusiveLeptons = []
        ### selected leptons = subset of inclusive leptons passing some basic id definition and pt requirement
        ### other    leptons = subset of inclusive leptons failing some basic id definition and pt requirement
        event.selectedLeptons = []
        event.selectedMuons = []
        event.selectedElectrons = []
        event.otherLeptons = []
        
#        with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
#            f.write('{0:6}{1:6}{2:10}\n'.format(event.run, event.lumi, event.eventId))
        with open('prompt_bestMatch.txt', 'a') as f:
             f.write('{0:6}{1:6}{2:10}\n'.format(event.run, event.lumi, event.eventId))
        event.myLeptons = []

        #muons
        allmuons = self.makeAllMuons(event)
        for mu in allmuons:
            # inclusive, very loose, selection
            if (mu.track().isNonnull() and mu.muonID(self.cfg_ana.inclusive_muon_id) and 
                    mu.pt()>self.cfg_ana.inclusive_muon_pt and abs(mu.eta())<self.cfg_ana.inclusive_muon_eta and 
                    abs(mu.dxy())<self.cfg_ana.inclusive_muon_dxy and abs(mu.dz())<self.cfg_ana.inclusive_muon_dz):
                event.inclusiveLeptons.append(mu)
                # basic selection
                cut0_passed = mu.muonID(self.cfg_ana.loose_muon_id)
                cut1_passed = mu.pt() > self.cfg_ana.loose_muon_pt
                cut2_passed = abs(mu.eta()) < self.cfg_ana.loose_muon_eta
                cut3_passed = abs(mu.dxy()) < self.cfg_ana.loose_muon_dxy
                cut4_passed = abs(mu.dz()) < self.cfg_ana.loose_muon_dz
                cut5_passed = mu.relIso03 < self.cfg_ana.loose_muon_relIso
                cut6_passed = mu.absIso03 < (self.cfg_ana.loose_muon_absIso if hasattr(self.cfg_ana,'loose_muon_absIso') else 9e99)
                myMu = mu
                myMu.cut0_passed = cut0_passed
                myMu.cut1_passed = cut1_passed
                myMu.cut2_passed = cut2_passed
                myMu.cut3_passed = cut3_passed
                myMu.cut4_passed = cut4_passed
                myMu.cut5_passed = cut5_passed
                myMu.cut6_passed = cut6_passed
#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
#                    f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.4f}{7:8.4f}      '.format(mu.pdgId(), mu.pt(), mu.eta(), mu.phi(), mu.dxy(), mu.dz(), mu.relIso03, mu.absIso03))
#                    f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}    '.format(cut0_passed, cut1_passed, cut2_passed, cut3_passed, cut4_passed, cut5_passed, cut6_passed))
#                mu.muonID(self.cfg_ana.loose_muon_id, wtuple=('prompt_debug_bdt_passing_mu_el_cuts.txt',))
                mu.muonID1(self.cfg_ana.loose_muon_id, wtuple=(myMu,))
#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f: f.write('\n')

#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
#                    f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.4f}{7:8.4f}      '.format(myMu.pdgId(), myMu.pt(), myMu.eta(), myMu.phi(), myMu.dxy(), myMu.dz(), myMu.relIso03, myMu.absIso03))
#                    f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}    '.format(myMu.cut0_passed, myMu.cut1_passed, myMu.cut2_passed, myMu.cut3_passed, myMu.cut4_passed, myMu.cut5_passed, myMu.cut6_passed))
#                    f.write('              {0:8}'.format(myMu.id))
#                    f.write('\n')
                event.myLeptons.append(myMu)

                if (mu.muonID(self.cfg_ana.loose_muon_id) and 
                        mu.pt() > self.cfg_ana.loose_muon_pt and abs(mu.eta()) < self.cfg_ana.loose_muon_eta and 
                        abs(mu.dxy()) < self.cfg_ana.loose_muon_dxy and abs(mu.dz()) < self.cfg_ana.loose_muon_dz and
                        mu.relIso03 < self.cfg_ana.loose_muon_relIso and 
                        mu.absIso03 < (self.cfg_ana.loose_muon_absIso if hasattr(self.cfg_ana,'loose_muon_absIso') else 9e99)):
                    mu.looseIdSusy = True
                    event.selectedLeptons.append(mu)
                    event.selectedMuons.append(mu)
                else:
                    mu.looseIdSusy = False
                    event.otherLeptons.append(mu)

        #electrons        
        allelectrons = self.makeAllElectrons(event)

        looseMuons = event.selectedLeptons[:]
        for ele in allelectrons:
            ## remove muons if muForEleCrossCleaning is not empty
            ## apply selection
            if ( ele.electronID(self.cfg_ana.inclusive_electron_id) and
                    ele.pt()>self.cfg_ana.inclusive_electron_pt and abs(ele.eta())<self.cfg_ana.inclusive_electron_eta and 
                    abs(ele.dxy())<self.cfg_ana.inclusive_electron_dxy and abs(ele.dz())<self.cfg_ana.inclusive_electron_dz and 
                    ele.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()<=self.cfg_ana.inclusive_electron_lostHits ):
                event.inclusiveLeptons.append(ele)
                # basic selection
                cut0_passed = ele.electronID(self.cfg_ana.loose_electron_id)
                cut1_passed = ele.pt()>self.cfg_ana.loose_electron_pt
                cut2_passed = abs(ele.eta())<self.cfg_ana.loose_electron_eta
                cut3_passed = abs(ele.dxy()) < self.cfg_ana.loose_electron_dxy
                cut4_passed = abs(ele.dz())<self.cfg_ana.loose_electron_dz
                cut5_passed = ele.relIso03 <= self.cfg_ana.loose_electron_relIso
                cut6_passed = ele.absIso03 < (self.cfg_ana.loose_electron_absIso if hasattr(self.cfg_ana,'loose_electron_absIso') else 9e99)
                cut7_passed = ele.gsfTrack().trackerExpectedHitsInner().numberOfLostHits() <= self.cfg_ana.loose_electron_lostHits
                cut8_passed = True if (hasattr(self.cfg_ana,'notCleaningElectrons') and self.cfg_ana.notCleaningElectrons) else (bestMatchPrint(ele, looseMuons)[1] > self.cfg_ana.min_dr_electron_muon)
                myEl = ele
                myEl.cut0_passed = cut0_passed
                myEl.cut1_passed = cut1_passed
                myEl.cut2_passed = cut2_passed
                myEl.cut3_passed = cut3_passed
                myEl.cut4_passed = cut4_passed
                myEl.cut5_passed = cut5_passed
                myEl.cut6_passed = cut6_passed
                myEl.cut7_passed = cut7_passed
                myEl.cut8_passed = cut8_passed

#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
#                    f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.3f}{7:8.3f}{8:6}'.format(ele.pdgId(), ele.pt(), ele.eta(), ele.phi(), ele.dxy(), ele.dz(), ele.absIso03, ele.relIso03, ele.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()))
#                    f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}{7:2}{8:2}'.format(cut0_passed, cut1_passed, cut2_passed, cut3_passed, cut4_passed, cut5_passed, cut6_passed, cut7_passed, cut8_passed))
#                ele.electronID(self.cfg_ana.loose_electron_id, wtuple=('prompt_debug_bdt_passing_mu_el_cuts.txt',))
                ele.electronID1(self.cfg_ana.loose_electron_id, wtuple=(myEl,))
#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f: f.write('\n')

#                with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
#                    f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.3f}{7:8.3f}{8:6}'.format(myEl.pdgId(), myEl.pt(), myEl.eta(), myEl.phi(), myEl.dxy(), myEl.dz(), myEl.absIso03, myEl.relIso03, myEl.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()))
#                    f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}{7:2}{8:2}'.format(myEl.cut0_passed, myEl.cut1_passed, myEl.cut2_passed, myEl.cut3_passed, myEl.cut4_passed, myEl.cut5_passed, myEl.cut6_passed, myEl.cut7_passed, myEl.cut8_passed))
#                    f.write('  {0:8.3f}{1:+8.3f}{2:2}{3:2}'.format(myEl.scEta, myEl.mvaNTV0, myEl.case, myEl.ret))
#                    f.write('\n')
                event.myLeptons.append(myEl)

                if (ele.electronID(self.cfg_ana.loose_electron_id) and
                         ele.pt()>self.cfg_ana.loose_electron_pt and abs(ele.eta())<self.cfg_ana.loose_electron_eta and 
                         abs(ele.dxy()) < self.cfg_ana.loose_electron_dxy and abs(ele.dz())<self.cfg_ana.loose_electron_dz and 
                         ele.relIso03 <= self.cfg_ana.loose_electron_relIso and
                         ele.absIso03 < (self.cfg_ana.loose_electron_absIso if hasattr(self.cfg_ana,'loose_electron_absIso') else 9e99) and
                         ele.gsfTrack().trackerExpectedHitsInner().numberOfLostHits() <= self.cfg_ana.loose_electron_lostHits and
                         ( True if (hasattr(self.cfg_ana,'notCleaningElectrons') and self.cfg_ana.notCleaningElectrons) else (bestMatch1(ele, looseMuons)[1] > self.cfg_ana.min_dr_electron_muon) )):
                    event.selectedLeptons.append(ele)
                    event.selectedElectrons.append(ele)
                    ele.looseIdSusy = True
                else:
                    event.otherLeptons.append(ele)
                    ele.looseIdSusy = False
#        with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f: f.write('\n')

        event.otherLeptons.sort(key = lambda l : l.pt(), reverse = True)
        event.selectedLeptons.sort(key = lambda l : l.pt(), reverse = True)
        event.selectedMuons.sort(key = lambda l : l.pt(), reverse = True)
        event.selectedElectrons.sort(key = lambda l : l.pt(), reverse = True)
        event.inclusiveLeptons.sort(key = lambda l : l.pt(), reverse = True)

        event.myLeptons.sort(key = lambda l : l.pt(), reverse = True)
        
        event.myGoodLeptons = []
        event.myNonGoodLeptons = []
        
        if event.genHiggsDecayMode == 15 or event.genHiggsDecayMode == 23 or event.genHiggsDecayMode == 24:
            with open('prompt_debug_bdt_passing_mu_el_cuts.txt', 'a') as f:
                f.write('{0:6}{1:6}{2:10}'.format(event.run, event.lumi, event.eventId))
                ngood = 0
                for myLep in event.myLeptons:
                    if ((abs(myLep.pdgId()) == 13) and myLep.cut0_passed and myLep.cut1_passed and myLep.cut2_passed and myLep.cut3_passed and myLep.cut4_passed and myLep.cut5_passed and myLep.cut6_passed) or ((abs(myLep.pdgId()) == 11) and myLep.cut0_passed and myLep.cut1_passed and myLep.cut2_passed and myLep.cut3_passed and myLep.cut4_passed and myLep.cut5_passed and myLep.cut6_passed and myLep.cut7_passed and myLep.cut8_passed):
                        event.myGoodLeptons.append(myLep)
                        ngood += 1
                    else:
                        event.myNonGoodLeptons.append(myLep)
                is2l          = True if ngood >= 2 else False
                is2lss        = is2l and (True if event.myGoodLeptons[0].charge()*event.myGoodLeptons[1].charge() > 0 else False)
                is2lss_mumu   = True if is2lss and abs(event.myGoodLeptons[0].pdgId()) == 13 and abs(event.myGoodLeptons[1].pdgId()) == 13 else False
                is2lss_ee     = True if is2lss and abs(event.myGoodLeptons[0].pdgId()) == 11 and abs(event.myGoodLeptons[1].pdgId()) == 11 else False
                is2lss_em     = True if is2lss and abs(event.myGoodLeptons[0].pdgId()) <> abs(event.myGoodLeptons[1].pdgId()) else False
                ispt2020_mumu = True if is2lss_mumu and (event.myGoodLeptons[0].pt()>20 and event.myGoodLeptons[1].pt()>20) else False
                ispt2020_ee   = True if is2lss_ee and (event.myGoodLeptons[0].pt()>20 and event.myGoodLeptons[1].pt()>20) else False
#                isLepMVA_mumu = True if ispt2020_mumu and (min(event.myGoodLeptons[0].mvaTTH, event.myGoodLeptons[1].mvaTTH) > 0.7) else False
#                isLepMVA_ee   = True if ispt2020_ee and (min(event.myGoodLeptons[0].mvaTTH, event.myGoodLeptons[1].mvaTTH) > 0.7) else False
#                isTghChr_mumu = True if isLepMVA_mumu and (event.myGoodLeptons[0].tightCharge > 1 and event.myGoodLeptons[0].tightCharge > 1) else False
#                isTghChr_ee   = True if isLepMVA_ee and (event.myGoodLeptons[0].tightCharge > 1 and event.myGoodLeptons[1].tightCharge > 1) and (event.myGoodLeptons[0].convVeto>0 and event.myGoodLeptons[1].convVeto>0) and (event.myGoodLeptons[0].lostHits == 0 and event.myGoodLeptons[1].lostHits == 0) else False
#                is2bLoose_mumu = True if isTghChr_mumu and event.nBJetLoose25 >= 2 else False
#                is2bLoose_ee   = True if isTghChr_ee and event.nBJetLoose25 >= 2 else False
#                is4j_mumu      = True if is2bLoose_mumu and event.nJet25>=4 else False
#                is4j_ee        = True if is2bLoose_ee and event.nJet25>=4 else False
#                f.write('                                                                                                             {0:3}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}{7:2}\n'.format(ngood, is2l, is2lss, is2lss_mumu, is2lss_ee, is2lss_em, ispt2020_mumu, ispt2020_ee))
                f.write('                                                                                                             {0:3}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}\n'.format(ngood, is2l, is2lss, is2lss_mumu, is2lss_ee, ispt2020_mumu, ispt2020_ee))
                for myLep in (event.myGoodLeptons + event.myNonGoodLeptons):
                    if   abs(myLep.pdgId()) == 13:
                        f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.4f}{7:8.4f}      '.format(myLep.pdgId(), myLep.pt(), myLep.eta(), myLep.phi(), myLep.dxy(), myLep.dz(), myLep.relIso03, myLep.absIso03))
                        f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}    '.format(myLep.cut0_passed, myLep.cut1_passed, myLep.cut2_passed, myLep.cut3_passed, myLep.cut4_passed, myLep.cut5_passed, myLep.cut6_passed))
                        f.write('              {0:8}               '.format(myLep.id))
                    elif abs(myLep.pdgId()) == 11:
                        f.write('                          {0:+5}{1:8.2f}{2:+6.2f}{3:+6.2f}{4:+8.3f}{5:+8.3f}{6:8.3f}{7:8.3f}{8:6}'.format(myLep.pdgId(), myLep.pt(), myLep.eta(), myLep.phi(), myLep.dxy(), myLep.dz(), myLep.absIso03, myLep.relIso03, myLep.gsfTrack().trackerExpectedHitsInner().numberOfLostHits()))
                        f.write('  {0:2}{1:2}{2:2}{3:2}{4:2}{5:2}{6:2}{7:2}{8:2}'.format(myLep.cut0_passed, myLep.cut1_passed, myLep.cut2_passed, myLep.cut3_passed, myLep.cut4_passed, myLep.cut5_passed, myLep.cut6_passed, myLep.cut7_passed, myLep.cut8_passed))
                        f.write('  {0:8.3f}{1:+8.3f}{2:2}{3:2}               '.format(myLep.scEta, myLep.mvaNTV0, myLep.case, myLep.ret))
                    f.write('\n')
                f.write('\n')

        for lepton in event.selectedLeptons:
            if hasattr(self,'efficiency'):
                self.efficiency.attachToObject(lepton)

    def makeAllMuons(self, event):
        """
               make a list of all muons, and apply basic corrections to them
        """
        # Start from all muons
        allmuons = map( Muon, self.handles['muons'].product() )

        # Muon scale and resolution corrections (if enabled)
        if self.cfg_ana.doMuScleFitCorrections:
            for mu in allmuons:
                self.muscleCorr.correct(mu, event.run)
        elif self.cfg_ana.doRochesterCorrections:
            for mu in allmuons:
                corp4 = rochcor.corrected_p4(mu, event.run) 
                mu.setP4( corp4 )

        # Clean up dulicate muons (note: has no effect unless the muon id is removed)
        if self.cfg_ana.doSegmentBasedMuonCleaning:
            isgood = cmgMuonCleanerBySegments.clean( self.handles['muons'].product() )
            newmu = []
            for i,mu in enumerate(allmuons):
                if isgood[i]: newmu.append(mu)
            allmuons = newmu

        # Attach the vertex to them, for dxy/dz calculation
        for mu in allmuons:
            mu.associatedVertex = event.goodVertices[0]

        # Compute relIso in 0.3 and 0.4 cones
        for mu in allmuons:
            mu.absIso03 = (mu.pfIsolationR03().sumChargedHadronPt + max( mu.pfIsolationR03().sumNeutralHadronEt +  mu.pfIsolationR03().sumPhotonEt -  mu.pfIsolationR03().sumPUPt/2,0.0))
            mu.absIso04 = (mu.pfIsolationR04().sumChargedHadronPt + max( mu.pfIsolationR04().sumNeutralHadronEt +  mu.pfIsolationR04().sumPhotonEt -  mu.pfIsolationR04().sumPUPt/2,0.0))
            mu.relIso03 = mu.absIso03/mu.pt()
            mu.relIso04 = mu.absIso04/mu.pt()

        # Compute MVA Id: 
        for mu in allmuons:
            mu.mvaIdValue = self.muonMVAIdFull(mu)
        return allmuons

    def makeAllElectrons(self, event):
        """
               make a list of all electrons, and apply basic corrections to them
        """
        allelectrons = map( Electron, self.handles['electrons'].product() )

        ## Duplicate removal for fast sim (to be checked if still necessary in latest greatest 5.3.X releases)
        allelenodup = []
        for e in allelectrons:
            dup = False
            for e2 in allelenodup:
                if abs(e.pt()-e2.pt()) < 1e-6 and abs(e.eta()-e2.eta()) < 1e-6 and abs(e.phi()-e2.phi()) < 1e-6 and e.charge() == e2.charge():
                    dup = True
                    break
            if not dup: allelenodup.append(e)
        allelectrons = allelenodup

        # fill EA for rho-corrected isolation
        for ele in allelectrons:
          ele.rho = float(self.handles['rhoEle'].product()[0])
          SCEta = abs(ele.superCluster().eta())
          if (abs(SCEta) >= 0.0   and abs(SCEta) < 1.0   ) : ele.EffectiveArea = 0.13 # 0.130;
          if (abs(SCEta) >= 1.0   and abs(SCEta) < 1.479 ) : ele.EffectiveArea = 0.14 # 0.137;
          if (abs(SCEta) >= 1.479 and abs(SCEta) < 2.0   ) : ele.EffectiveArea = 0.07 # 0.067;
          if (abs(SCEta) >= 2.0   and abs(SCEta) < 2.2   ) : ele.EffectiveArea = 0.09 # 0.089;
          if (abs(SCEta) >= 2.2   and abs(SCEta) < 2.3   ) : ele.EffectiveArea = 0.11 # 0.107;
          if (abs(SCEta) >= 2.3   and abs(SCEta) < 2.4   ) : ele.EffectiveArea = 0.11 # 0.110;
          if (abs(SCEta) >= 2.4)                           : ele.EffectiveArea = 0.14 # 0.138;

        # Electron scale calibrations
        if self.cfg_ana.doElectronScaleCorrections:
            for ele in allelectrons:
                self.electronEnergyCalibrator.correct(ele, event.run)

        # Attach the vertex
        for ele in allelectrons:
            ele.associatedVertex = event.goodVertices[0]

        # Compute relIso with R=0.3 and R=0.4 cones
        for ele in allelectrons:
            if self.cfg_ana.ele_isoCorr=="rhoArea" :
                 ele.absIso03 = (ele.chargedHadronIso(0.3) + max(ele.neutralHadronIso(0.3)+ele.photonIso(0.3)-ele.rho*ele.EffectiveArea,0))
                 ele.absIso04 = (ele.chargedHadronIso(0.4) + max(ele.neutralHadronIso(0.4)+ele.photonIso(0.4)-ele.rho*ele.EffectiveArea,0))
            elif self.cfg_ana.ele_isoCorr=="deltaBeta" :
                 ele.absIso03 = (ele.pfIsolationVariables().sumChargedHadronPt + max( ele.pfIsolationVariables().sumNeutralHadronEt + ele.pfIsolationVariables().sumPhotonEt - ele.pfIsolationVariables().sumPUPt/2,0.0))
                 ele.absIso04 = 0.
            else :
                 raise RuntimeError, "Unsupported ele_isoCorr name '" + str(self.cfg_ana.ele_isoCorr) +  "'! For now only 'rhoArea' and 'deltaBeta' are supported."
            ele.relIso03 = ele.absIso03/ele.pt()
            ele.relIso04 = ele.absIso04/ele.pt()

        # Set tight MVA id
        for ele in allelectrons:
            if self.cfg_ana.ele_tightId=="MVA" :
                 ele.tightIdResult = ele.electronID("POG_MVA_ID_Trig_full5x5")
            elif self.cfg_ana.ele_tightId=="Cuts_2012" :
                 ele.tightIdResult = -1 + 1*ele.electronID("POG_Cuts_ID_2012_Veto") + 1*ele.electronID("POG_Cuts_ID_2012_Loose") + 1*ele.electronID("POG_Cuts_ID_2012_Medium") + 1*ele.electronID("POG_Cuts_ID_2012_Tight")
            else :
                 raise RuntimeError, "Unsupported ele_tightId name '" + str(self.cfg_ana.ele_tightId) +  "'! For now only 'MVA' and 'Cuts_2012' are supported."

        
        return allelectrons 

    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        #call the leptons functions
        self.makeLeptons(event)

        return True
