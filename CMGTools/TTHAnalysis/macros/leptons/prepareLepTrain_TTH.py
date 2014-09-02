#!/usr/bin/env python
from CMGTools.TTHAnalysis.treeReAnalyzer import *

import os, ROOT
if "/smearer_cc.so" not in ROOT.gSystem.GetLibraries(): 
    ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/TTHAnalysis/python/plotter/smearer.cc+" % os.environ['CMSSW_BASE']);
if "/mcCorrections_cc.so" not in ROOT.gSystem.GetLibraries(): 
    ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/TTHAnalysis/python/plotter/mcCorrections.cc+" % os.environ['CMSSW_BASE']);

def plausible(rec,gen):
    dr = deltaR(rec,gen)
    if abs(rec.pdgId) == 11 and abs(gen.pdgId) != 11:   return False
    if abs(rec.pdgId) == 13 and abs(gen.pdgId) != 13:   return False
    if dr < 0.3: return True
    if gen.pt < abs(rec.pdgId) == 13 and gen.pdgId != rec.pdgId: return False
    if dr < 0.7: return True
    if min(rec.pt,gen.pt)/max(rec.pt,gen.pt) < 0.3: return False
    return True

class LepTreeProducer(Module):
    def beginJob(self):
        self.t = PyTree(self.book("TTree","t","t"))
        self.t.branch("dr_in","F")
        self.t.branch("ptf_in","F")
        self.t.branch("CSV_in","F")
        #self.t.branch("dr_out","F")
        #self.t.branch("ptf_out","F")
        #self.t.branch("CSV_out","F")
        self.t.branch("good","I")
        self.t.branch("nJet25","I")
        self.t.branch("nBJetLoose25","I")
        self.t.branch("nBJetMedium25","I")
        self.t.branch("puWeight","F")
        #self.t.branch("nVert","F")
        #self.copyvars = [ 'relIso','chargedIso','mvaId','pt','eta','pdgId','innerHits','tightId',"mva","LepGood"]
        #for C in self.copyvars: self.t.branch(C,"F")
        n=8
        self.t.branch("relIso03","F",n)
        self.t.branch("relIso04","F",n)
        self.t.branch("chargedHadRelIso03","F",n)
        self.t.branch("chargedHadRelIso04","F",n)
        self.t.branch("mvaId","F",n)
        self.t.branch("pt","F",n)
        self.t.branch("eta","F",n)
        self.t.branch("pdgId","I",n)
        #self.t.branch("innerHits","I",n)
        self.t.branch("tightId","I",n)
        self.t.branch("mvaTTH","F",n)
        # these I can't copy since I need
        for C in [ 'sip3d','dxy','dz' ]: self.t.branch(C,"F")
        self.first = True
    Nevt = 0
    def analyze(self,event):
        #print self.Nevt
        self.Nevt += 1
        #if event.nLepGood < 3: return False
        #jet = Collection(event,"Jet")
        #lep = Collection(event,"LepGood","nLepGood",8)
        #glep = Collection(event,"GenLep")
        #gtau = Collection(event,"GenLepFromTau")
        listGenLep = []
        for i in range(event.nGenLep): listGenLep.append((event.GenLep_eta[i], event.GenLep_phi[i], event.GenLep_pdgId[i], event.GenLep_pt[i]))
        listGenLepFromTau = []
        #print event.nGenLepFromTau, range(event.nGenLepFromTau)
        for i in range(event.nGenLepFromTau): listGenLepFromTau.append((event.GenLepFromTau_eta[i], event.GenLepFromTau_phi[i], event.GenLepFromTau_pdgId[i], event.GenLepFromTau_pt[i]))
        #for l in lep:
        for i in range(event.nLepGood):
            #print "\t", i
            self.t.sip3d = ROOT.scaleSip3dMC(event.LepGood_sip3d[i], event.LepGood_pdgId[i],event.LepGood_pt[i],event.LepGood_eta[i],event.LepGood_mcMatchId[i],event.LepGood_mcMatchAny[i]) if self.corr else event.LepGood_sip3d[i]
            self.t.dz    = ROOT.scaleDzMC(   event.LepGood_dz[i],    event.LepGood_pdgId[i],event.LepGood_pt[i],event.LepGood_eta[i],event.LepGood_mcMatchId[i],event.LepGood_mcMatchAny[i]) if self.corr else event.LepGood_dz[i]
            self.t.dxy   = ROOT.scaleDxyMC(  event.LepGood_dxy[i],   event.LepGood_pdgId[i],event.LepGood_pt[i],event.LepGood_eta[i],event.LepGood_mcMatchId[i],event.LepGood_mcMatchAny[i]) if self.corr else event.LepGood_dxy[i]
            (dr,ptf) = (event.LepGood_jetDR[i],event.LepGood_jetPtRatio[i])
            self.t.dr_in  = ROOT.correctJetDRMC(dr,event.LepGood_pdgId[i],event.LepGood_pt[i],event.LepGood_eta[i],event.LepGood_mcMatchId[i],event.LepGood_mcMatchAny[i])       if self.corr else dr
            self.t.ptf_in = ROOT.correctJetPtRatioMC(ptf,event.LepGood_pdgId[i],event.LepGood_pt[i],event.LepGood_eta[i],event.LepGood_mcMatchId[i],event.LepGood_mcMatchAny[i]) if self.corr else ptf
            self.t.CSV_in = event.LepGood_jetBTagCSV[i]
            #(j,dr) = closest(l, jet)
            #ptot = j.p4() + event.LepGood_p4()
            #self.t.dr_out = dr
            #self.t.ptf_out = event.LepGood_pt[i]/ptot.Pt()
            #self.t.CSV_out = j.btagCSV
            #(gmatch,dr) = closest(event.LepGood[i],glep,presel=plausible)
            (gmatch,dr) = self.closest((event.LepGood_eta[i], event.LepGood_phi[i], event.LepGood_pdgId[i], event.LepGood_pt[i]), listGenLep, presel=self.plausible)
            #print "\t\t", gmatch, len(listGenLep), event.nLepGood
            if dr < 1.5 and abs(event.GenLep_pdgId[gmatch]) == abs(event.LepGood_pdgId[i]):
                self.t.good = 20 if dr < 0.5 else 2
            else:
                #(gmatch,dr) = closest(l,gtau,presel=plausible)
                (gmatch,dr) = self.closest((event.LepGood_eta[i], event.LepGood_phi[i], event.LepGood_pdgId[i], event.LepGood_pt[i]), listGenLepFromTau, presel=self.plausible)
                #print "\t\t\t", gmatch, len(listGenLepFromTau), event.nLepGood
                if dr < 1.5 and abs(event.GenLepFromTau_pdgId[gmatch]) == abs(event.LepGood_pdgId[i]):
                    self.t.good = 10 if dr < 0.5 else 1
                else: 
                    self.t.good = -event.LepGood_mcMatchAny[i]
            self.t.fill()
            #for C in self.copyvars: setattr(self.t, C, getattr(l,C))
            self.t.relIso03 = event.LepGood_relIso03
            self.t.relIso04 = event.LepGood_relIso04
            self.t.chargedHadRelIso03 = event.LepGood_chargedHadRelIso03
            self.t.chargedHadRelIso04 = event.LepGood_chargedHadRelIso04
            self.t.mvaId = event.LepGood_mvaId
            self.t.pt = event.LepGood_pt
            self.t.eta = event.LepGood_eta
            self.t.pdgId = event.LepGood_pdgId
            #self.t.innerHits = event.LepGood_innerHits
            self.t.tightId = event.LepGood_tightId
            self.t.mvaTTH = event.LepGood_mvaTTH
            self.t.nJet25 = event.nJet25
            self.t.nBJetLoose25 = event.nBJetLoose25
            self.t.nBJetMedium25 = event.nBJetMedium25
            self.t.puWeight = event.puWeight
            #self.t.nVert = event.nVert
            self.t.fill()
#### ========= UTILITIES =======================
#(gmatch,dr) = closest(l,glep,presel=plausible)
#(gmatch,dr) = closest((event.LepGood_eta[i], event.LepGood_phi[i]), (event.LepGood_eta, event.LepGood_phi),presel=plausible)

#(gmatch,dr) = closest((event.LepGood_eta[i], event.LepGood_phi[i]), (event.LepGood_eta, event.LepGood_phi))

    #def deltaPhi(phi1,phi2):
    #    ## Catch if being called with two objects
    #    if type(phi1) != float and type(phi1) != int:
    #        phi1 = phi1.phi
    #    if type(phi2) != float and type(phi2) != int:
    #        phi2 = phi2.phi
    #    ## Otherwise
    #    dphi = (phi1-phi2)
    #    while dphi >  pi: dphi -= 2*pi
    #    while dphi < -pi: dphi += 2*pi
    #    return dphi
    def deltaR(self, rec, gen):
        ## catch if called with objects
        #if eta2 == None:
        #    return deltaR(eta1,phi1,eta2,phi2)
        ## otherwise
        return hypot(rec[0]-gen[0], deltaPhi(rec[1], gen[1]))
    def plausible(self, rec, gen):
        dr = self.deltaR(rec, gen)
        if abs(rec[2]) == 11 and abs(gen[2]) != 11:   return False
        if abs(rec[2]) == 13 and abs(gen[2]) != 13:   return False
        if dr < 0.3: return True
        if gen[3] < abs(rec[2]) == 13 and gen[2] != rec[2]: return False
        if dr < 0.7: return True
        if min(rec[3],gen[3])/max(rec[3],gen[3]) < 0.3: return False
        return True
    #def closest(object,list,presel=lambda x,y: True):
    def closest(self, object, list, presel=lambda x,y: True):
        ret = None; drMin = 999
        #for x in list:
        for x in range(len(list)):
            if not presel(object, list[x]): continue
            dr = self.deltaR(object, list[x])
            if dr < drMin: 
                ret = x; drMin = dr
        return (ret,drMin)

from sys import argv
f = ROOT.TFile.Open(argv[1])
t = f.Get("treeProducerSusyMultilepton")
print "Reading %s (%d entries)" % (argv[1], t.GetEntries())

booker = Booker(argv[2] if len(argv) >= 3 else "lepTree.root")
prod = LepTreeProducer("rec",booker)
if len(argv) >= 4 and argv[3] == "NoCorr": 
    print "Will not apply corrections"
    prod.corr = False
else:
    print "Will apply corrections"
    prod.corr = True
el = EventLoop([ prod, ])
maxEv = (int(argv[4]) if len(argv) >= 5 else -1)
print "max entries: ",maxEv
el.loop([t], maxEvents=maxEv)
booker.done()
