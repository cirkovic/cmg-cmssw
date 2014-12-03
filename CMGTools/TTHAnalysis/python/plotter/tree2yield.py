#!/usr/bin/env python
from math import *
import re
import os, os.path
from array import array

## safe batch mode
import sys
args = sys.argv[:]
sys.argv = ['-b']
import ROOT
sys.argv = args
ROOT.gROOT.SetBatch(True)

from copy import *

from CMGTools.TTHAnalysis.plotter.mcCorrections import *
from CMGTools.TTHAnalysis.plotter.fakeRate import *

from ROOT import *

if "/functions_cc.so" not in ROOT.gSystem.GetLibraries(): 
    ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/TTHAnalysis/python/plotter/functions.cc+" % os.environ['CMSSW_BASE']);

def scalarToVector(x):
    x0 = x
    x = re.sub(r"(LepGood|Lep|JetFwd|Jet|GenTop|SV)(\d)_(\w+)", lambda m : "%s_%s[%d]" % (m.group(1),m.group(3),int(m.group(2))-1), x)
    x = re.sub(r"\bmet\b", "met_pt", x)
    return x

class CutsFile:
    def __init__(self,txtfileOrCuts,options=None):
        if type(txtfileOrCuts) == list:
            self._cuts = deepcopy(txtfileOrCuts[:])
        elif isinstance(txtfileOrCuts,CutsFile):
            self._cuts = deepcopy(txtfileOrCuts.cuts())
        else:
            self._cuts = []
            file = open(txtfileOrCuts, "r")
            if not file: raise RuntimeError, "Cannot open "+txtfileOrCuts+"\n"
            for cr,cn,cv in options.cutsToAdd:
                if re.match(cr,"entry point"): self._cuts.append((cn,cv))
            for line in file:
              try:
                if len(line.strip()) == 0 or line.strip()[0] == '#': continue
                while line.strip()[-1] == "\\":
                    line = line.strip()[:-1] + file.next()
                (name,cut) = [x.strip().replace(";",":") for x in line.replace("\:",";").split(":")]
                if name == "entry point" and cut == "1": continue
                if options.startCut and not re.search(options.startCut,name): continue
                if options.startCut and re.search(options.startCut,name): options.startCut = None
                self._cuts.append((name,cut))
                for cr,cn,cv in options.cutsToAdd:
                    if re.match(cr,name): self._cuts.append((cn,cv))
                if options.upToCut and re.search(options.upToCut,name):
                    break
              except ValueError, e:
                print "Error parsing cut line [%s]" % line.strip()
                raise 
            for ci in options.cutsToInvert:  self.invert(ci)
            for ci in options.cutsToExclude: self.remove(ci)
            for cr,cn,cv in options.cutsToReplace: self.replace(cr,cn,cv)
    def __str__(self):
        newstring = ""
        for cut in self._cuts:
            newstring += "{0} : {1}\n".format(cut[0],cut[1])
        return newstring[:-1]
    def remove(self,cut):
        self._cuts = [(cn,cv) for (cn,cv) in self._cuts if not re.search(cut,cn)]
        return self
    def invert(self,cut):
        for i,(cn,cv) in enumerate(self._cuts[:]):
            if re.search(cut,cn):
                if cn.startswith("not ") and re.match(r"!\(.*\)", cv):
                    self._cuts[i] = (cn[4:], cv[2:-1])
                else:
                    self._cuts[i] = ("not "+cn, "!("+cv+")")
        return self
    def replace(self,cut,newname,newcut):       
        for i,(cn,cv) in enumerate(self._cuts[:]):
            if re.search(cut,cn):
                self._cuts[i] = (newname, newcut)
        return self
    def cuts(self):
        return self._cuts[:]
    def sequentialCuts(self):
        if len(self._cuts) == 0: return []
        ret = [ (self._cuts[0][0], "(%s)" % self._cuts[0][1]) ]
        for (cn,cv) in self._cuts[1:]:
            ret.append( ( cn, "%s && (%s)" % (ret[-1][1], cv) ) )
        return ret
    def nMinusOne(self):
        return CutsFile(self.nMinusOneCuts())
    def nMinusOneCuts(self):
        ret = []
        for cn,cv in self._cuts[1:]:
            nm1 = " && ".join("(%s)" % cv1 for cn1,cv1 in self._cuts if cn1 != cn)
            ret.append(("all but "+cn, nm1))
        return ret
    def allCuts(self,n=-1):
        return " && ".join("(%s)" % x[1] for x in (self._cuts[0:n+1] if n != -1 and n+1 < len(self._cuts) else self._cuts))
    def addAfter(self,cut,newname,newcut):
        for i,(cn,cv) in enumerate(self._cuts[:]):
            if re.search(cut,cn):
                self._cuts.insert(i+1,(newname, newcut))
                break
        return self
    def insert(self,index,newname,newcut):
        self._cuts.insert(index,(newname, newcut))
        return self
    def add(self,newname,newcut):
        self._cuts.append((newname,newcut))
        return self
    def setParams(self,paramMap):
        self._cuts = [ (cn.format(**paramMap), cv.format(**paramMap)) for (cn,cv) in self._cuts ]

class PlotSpec:
    def __init__(self,name,expr,bins,opts):
        self.name = name
        self.expr = expr
        self.bins = bins
        self.opts = opts
    def hasOption(self,name):
        return (name in self.opts)
    def getOption(self,name,default=None):
        return self.opts[name] if (name in self.opts) else default

class TreeToYield:
    def __init__(self,root,options,scaleFactor=1.0,name=None,cname=None,settings={},treename=None):
        self._name  = name  if name != None else root
        self._cname = cname if cname != None else self._name
        self._fname = root
        self._isInit = False
        self._options = options
        self._treename = treename if treename else options.tree
        self._weight  = (options.weight and 'data' not in self._name and '2012' not in self._name and '2011' not in self._name )
        self._isdata = 'data' in self._name
        self._weightString  = options.weightString if not self._isdata else "1"
        self._scaleFactor = scaleFactor
        self._fullYield = 0 # yield of the full sample, as if it passed the full skim and all cuts
        self._settings = settings
        loadMCCorrections(options)            ## make sure this is loaded
        self._mcCorrs = globalMCCorrections() ##  get defaults
        if 'SkipDefaultMCCorrections' in settings: ## unless requested to 
            self._mcCorrs = []                     ##  skip them
        if self._isdata: self._mcCorrs = [] ## no MC corrections for data
        if 'MCCorrections' in settings:
            self._mcCorrs = self._mcCorrs[:] # make copy
            for cfile in settings['MCCorrections'].split(','): 
                self._mcCorrs.append( MCCorrections(cfile) )
        if 'FakeRate' in settings:
            self._FR = FakeRate(settings['FakeRate'])
            ## add additional weight correction 
            self._weightString += "* (" + self.adaptDataMCExpr(self._FR.weight()) + ")"
            ## modify cuts to get to control region
            self._mcCorrs = self._mcCorrs + self._FR.cutMods()  + self._FR.mods()
            self._weight = True
        #print "Done creation  %s for task %s in pid %d " % (self._fname, self._name, os.getpid())
    def setScaleFactor(self,scaleFactor):
        self._scaleFactor = scaleFactor
    def getScaleFactor(self):
        return self._scaleFactor
    def setFullYield(self,fullYield):
        self._fullYield = fullYield
    def name(self):
        return self._name
    def hasOption(self,name):
        return (name in self._settings)
    def getOption(self,name,default=None):
        if name in self._settings: return self._settings[name]
        return default
    def setOption(self,name,value):
        self._settings[name] = value
    def adaptDataMCExpr(self,expr):
        ret = expr
        if self._isdata:
            ret = re.sub(r'\$MC\{.*?\}', '', re.sub(r'\$DATA\{(.*?)\}', r'\1', expr));
        else:
            ret = re.sub(r'\$DATA\{.*?\}', '', re.sub(r'\$MC\{(.*?)\}', r'\1', expr));
        return ret
    def adaptExpr(self,expr,cut=False):
        ret = self.adaptDataMCExpr(expr)
        for mcc in self._mcCorrs:
            ret = mcc(ret,self._name,self._cname,cut)
        return ret
    def _init(self):
        if "root://" in self._fname:
            ROOT.gEnv.SetValue("TFile.AsyncReading", 1);
            ROOT.gEnv.SetValue("XNet.Debug", -1); # suppress output about opening connections
            #self._tfile = ROOT.TFile.Open(self._fname+"?readaheadsz=200000") # worse than 65k
            #self._tfile = ROOT.TFile.Open(self._fname+"?readaheadsz=32768") # worse than 65k
            self._tfile = ROOT.TFile.Open(self._fname+"?readaheadsz=65535") # good
            #self._tfile = ROOT.TFile.Open(self._fname+"?readaheadsz=0") #worse than 65k
        else:
            self._tfile = ROOT.TFile.Open(self._fname)
        if not self._tfile: raise RuntimeError, "Cannot open %s\n" % self._fname
        t = self._tfile.Get(self._treename)
        if not t: raise RuntimeError, "Cannot find tree %s in file %s\n" % (self._treename, self._fname)
        self._tree  = t
        #self._tree.SetCacheSize(10*1000*1000)
        if "root://" in self._fname: self._tree.SetCacheSize()
        self._friends = []
        friendOpts = self._options.friendTrees[:]
        friendOpts += (self._options.friendTreesData if self._isdata else self._options.friendTreesMC)
        for tf_tree,tf_file in friendOpts:
            tf = self._tree.AddFriend(tf_tree, tf_file.format(name=self._name, cname=self._cname)),
            self._friends.append(tf)
        self._isInit = True
    def getYields(self,cuts,noEntryLine=False):
        self._file_i = 0
        if not self._isInit: self._init()
        report = []; cut = ""
        cutseq = [ ['entry point','1'] ]
        if noEntryLine: cutseq = []
        sequential = False
        if self._options.nMinusOne: 
            cutseq = cuts.nMinusOneCuts()
            cutseq += [ ['all',cuts.allCuts()] ]
            sequential = False
        elif self._options.final:
            cutseq = [ ['all', cuts.allCuts()] ]
        else:
            cutseq += cuts.cuts();
            sequential = True
        for cn,cv in cutseq:
            if sequential:
                if cut: cut += " && "
                cut += "(%s)" % cv
            else:
                cut = cv
            report.append((cn,self._getYield(self._tree,cut)))
        if self._options.fullSampleYields and not noEntryLine:
            report.insert(0, ('full sample', [self._fullYield,0]) )
        return report
    def prettyPrint(self,report):
        # maximum length of the cut descriptions
        clen = max([len(cut) for cut,yields in report]) + 3
        cfmt = "%%-%ds" % clen;

        fmtlen = 12
        nfmtL = "    %8d"
        nfmtS = "    %8.3f" if self._weight else nfmtL

        if self._options.errors:
            nfmtS+=u"%8.3f"
            nfmtL+=u"%8.3f"
            fmtlen+=8
        if self._options.fractions:
            nfmtS+="%7.1f%%"
            nfmtL+="%7.1f%%"
            fmtlen+=8

        print "cut".center(clen),"yield".center(fmtlen)
        print "-"*((fmtlen+1)+clen)
        for i,(cut,(nev,err)) in enumerate(report):
            print cfmt % cut,
            den = report[i-1][1][0] if i>0 else 0
            fraction = nev/float(den) if den > 0 else 1
            if self._options.nMinusOne: 
                fraction = report[-1][1][0]/nev if nev > 0 else 1
            toPrint = (nev,)
            if self._options.errors:    toPrint+=(err,)
            if self._options.fractions: toPrint+=(fraction*100,)
            if self._weight and nev < 1000: print nfmtS % toPrint,
            else                          : print nfmtL % toPrint,
            print ""
    def _printArr(self, title, arr, last=False, ndecs=2):
        i = 0
        for e in arr:
            if i > 0:
               self._o_txt.write(self._txt_delimiter+str(round(e, ndecs)))
               self._o_csv.write(self._csv_delimiter+str(round(e, ndecs)))
            else:
               self._o_txt.write(str(round(e, ndecs)))
               self._o_csv.write(str(round(e, ndecs)))
            i += 1
        if not last:
           self._o_txt.write(self._txt_delimiter)
           self._o_csv.write(self._csv_delimiter)
    def _printArrEl(self, arr, index=0, prefix='', form='', sufix='', first=False):
        form = prefix+'{0:'+form+'}'+sufix
        self._o_txt.write(form.format(arr[index]))
        if not first:
           self._o_csv.write(self._csv_delimiter+form.format(arr[index]))
        else:
           self._o_csv.write(form.format(arr[index]))
    def _getYield(self,tree,cut):
        if self._weight:
            if self._isdata: cut = "(%s)     *(%s)*(%s)" % (self._weightString,                    self._scaleFactor, self.adaptExpr(cut,cut=True))
            else:            cut = "(%s)*(%s)*(%s)*(%s)" % (self._weightString,self._options.lumi, self._scaleFactor, self.adaptExpr(cut,cut=True))
            if self._options.doS2V:
                cut  = scalarToVector(cut)
            ROOT.gROOT.cd()
            if ROOT.gROOT.FindObject("dummy") != None: ROOT.gROOT.FindObject("dummy").Delete()
            histo = ROOT.TH1F("dummy","dummy",1,0.0,1.0); histo.Sumw2()
            x = array('i',[0])
            tree.SetBranchAddress( "evt", x )
            i = 0
            while tree.GetEntry(i):
               #print cut, "\tnLepGood: ", x[0]
               print "evt: ", x[0]
               i += 1
            nev = tree.Draw("0.5>>dummy", cut, "goff")
            return [ histo.GetBinContent(1), histo.GetBinError(1) ]
        else: 
            if self._options.doS2V:
                cut  = scalarToVector(cut)
            
#            if self._file_i >= 2:
#            if True:
#            if False:
            if self._options.prtVars:
               tree1 = tree.Clone()
               elname = 'elist_cut'+str(self._file_i)
               tree1.Draw('>>'+elname,self.adaptExpr(cut,cut=True))
               elist = gDirectory.Get(elname)
               elist.Print()
               tree1.SetEventList(elist)
#               f_dummy = TFile.Open('f_dummy.root','RECREATE')
               tree2 = tree1.CopyTree("")
#               tree2.ResetBranchAddresses()
               
               b_run = array('i',[0])
               b_lumi = array('i',[0])
               b_evt = array('i',[0])
               #b_LepGood_charge = array('i',[0, 0])
               #b_LepGood_convVeto = array('i',[0, 0])
               #b_LepGood_lostHits = array('i',[0, 0])
               #b_LepGood_mvaTTH = array('f',[0, 0])
               b_LepGood_pdgId = array('i',[0, 0])
               b_LepGood_pt = array('f',[0, 0])
               b_LepGood_eta = array('f',[0, 0])
               b_LepGood_phi = array('f',[0, 0])
               #b_LepGood_tightCharge = array('i',[0, 0])
               b_met_pt = array('f',[0])
               #b_mhtJet25 = array('f',[0])
               #b_minMllAFAS = array('f',[0])
               #b_nBJetLoose25 = array('i',[0])
               #b_nBJetMedium25 = array('i',[0])
               #b_nJet25 = array('i',[0])
               #b_nLepGood10 = array('i',[0])
               b_met_phi = array('f',[0])
               b_nJet25 = array('i',[0])
#               b_GenHiggsDecayMode = array('i', [0])

               tree2.SetBranchAddress("run", b_run)
               tree2.SetBranchAddress("lumi", b_lumi)
               tree2.SetBranchAddress("evt", b_evt)
               #tree2.SetBranchAddress("LepGood_charge", b_LepGood_charge)
               #tree2.SetBranchAddress("LepGood_convVeto", b_LepGood_convVeto)
               #tree2.SetBranchAddress("LepGood_lostHits", b_LepGood_lostHits)
               #tree2.SetBranchAddress("LepGood_mvaTTH", b_LepGood_mvaTTH)
               tree2.SetBranchAddress("LepGood_pdgId", b_LepGood_pdgId)
               tree2.SetBranchAddress("LepGood_pt", b_LepGood_pt)
               tree2.SetBranchAddress("LepGood_eta", b_LepGood_eta)
               tree2.SetBranchAddress("LepGood_phi", b_LepGood_phi)
               #tree2.SetBranchAddress("LepGood_tightCharge", b_LepGood_tightCharge)
               tree2.SetBranchAddress("met_pt", b_met_pt)
               #tree2.SetBranchAddress("mhtJet25", b_mhtJet25)
               #tree2.SetBranchAddress("minMllAFAS", b_minMllAFAS)
               #tree2.SetBranchAddress("nBJetLoose25", b_nBJetLoose25)
               #tree2.SetBranchAddress("nBJetMedium25", b_nBJetMedium25)
               #tree2.SetBranchAddress("nJet25", b_nJet25)
               #tree2.SetBranchAddress("nLepGood10", b_nLepGood10)
               tree2.SetBranchAddress("met_phi", b_met_phi)
               tree2.SetBranchAddress("nJet25", b_nJet25)
#               tree2.SetBranchAddress("GenHiggsDecayMode", b_GenHiggsDecayMode)
               
               self._o_txt = open(self._options.outDir+'/cut'+str(self._file_i)+'.txt', 'wb')
               self._o_csv = open(self._options.outDir+'/cut'+str(self._file_i)+'.csv', 'wb')
               #varTitles = ['evt', 'LepGood1_charge', 'LepGood2_charge', 'LepGood1_convVeto', 'LepGood2_convVeto', 'LepGood1_lostHits', 'LepGood2_lostHits', 'LepGood1_mvaTTH', 'LepGood2_mvaTTH', 'LepGood1_pdgId', 'LepGood2_pdgId', 'LepGood1_pt', 'LepGood2_pt', 'LepGood1_eta', 'LepGood2_eta', 'LepGood1_phi', 'LepGood2_phi', 'LepGood1_tightCharge', 'LepGood2_tightCharge', 'met_pt', 'mhtJet25', 'minMllAFAS', 'nBJetLoose25', 'nBJetMedium25', 'nJet25', 'nLepGood10']
               #varTitles = ['evt', 'LepGood1_pdgId', 'LepGood2_pdgId', 'LepGood1_pt', 'LepGood2_pt', 'LepGood1_eta', 'LepGood2_eta', 'LepGood1_phi', 'LepGood2_phi', 'met_pt']
               #varTitles = ['evt', 'LepGood1_pdgId', 'LepGood1_pt', 'LepGood1_eta', 'LepGood1_phi', 'LepGood2_pdgId', 'LepGood2_pt', 'LepGood2_eta', 'LepGood2_phi', 'met_pt']
               #self._o_txt.write(varTitles[0])
               #self._o_csv.write(varTitles[0])
               self._txt_delimiter = ' '
               self._csv_delimiter = ','
               #for title in varTitles[1:]:
               #   self._o_txt.write(self._txt_delimiter+title)
               #   self._o_csv.write(self._csv_delimiter+title)
               #self._o_txt.write('\n')
               #self._o_csv.write('\n')
               
               i = 0
               while tree2.GetEntry(i):
                  '''
                  self._printArr("evt", b_evt)
                  #self._printArr("LepGood_charge", b_LepGood_charge)
                  #self._printArr("LepGood_convVeto", b_LepGood_convVeto)
                  #self._printArr("LepGood_lostHits", b_LepGood_lostHits)
                  #self._printArr("LepGood_mvaTTH", b_LepGood_mvaTTH)
                  self._printArr("LepGood_pdgId", b_LepGood_pdgId)
                  self._printArr("LepGood_pt", b_LepGood_pt, ndecs=2)
                  self._printArr("LepGood_eta", b_LepGood_eta, ndecs=2)
                  self._printArr("LepGood_phi", b_LepGood_phi, ndecs=1)
                  #self._printArr("LepGood_tightCharge", b_LepGood_tightCharge)
                  self._printArr("met_pt", b_met_pt)
                  #self._printArr("mhtJet25", b_mhtJet25)
                  #self._printArr("minMllAFAS", b_minMllAFAS)
                  #self._printArr("nBJetLoose25", b_nBJetLoose25)
                  #self._printArr("nBJetMedium25", b_nBJetMedium25)
                  #self._printArr("nJet25", b_nJet25)
                  #self._printArr("nLepGood10", b_nLepGood10, last=True)
                  '''
                  self._printArrEl(b_run, form='6', first=True)
                  self._printArrEl(b_lumi, form='7')
                  self._printArrEl(b_evt, form='11')
                  self._printArrEl(b_LepGood_pdgId, 0, form='+5')
                  self._printArrEl(b_LepGood_pt, 0, form='8.2f')
                  self._printArrEl(b_LepGood_eta, 0, form='+6.2f')
                  self._printArrEl(b_LepGood_phi, 0, form='+6.2f')
                  self._printArrEl(b_LepGood_pdgId, 1, form='+6')
                  self._printArrEl(b_LepGood_pt, 1, form='8.2f')
                  self._printArrEl(b_LepGood_eta, 1, form='+6.2f')
                  self._printArrEl(b_LepGood_phi, 1, form='+6.2f')
                  self._printArrEl(b_met_pt, form='10.1f')
                  self._printArrEl(b_met_phi, form='+7.2f')
                  self._printArrEl(b_nJet25, prefix='    ', form='<2')
#                  self._printArrEl(b_GenHiggsDecayMode, form='5')
                  self._o_txt.write('\n')
                  self._o_csv.write('\n')
                  i += 1
               self._o_txt.close()
               self._o_csv.close()

            self._file_i += 1
               
            npass = tree.Draw("1",self.adaptExpr(cut,cut=True),"goff");
            return [ npass, sqrt(npass) ]
    def _stylePlot(self,plot,spec):
        ## Sample specific-options, from self
        if self.hasOption('FillColor'):
            plot.SetFillColor(self.getOption('FillColor',0))
            plot.SetFillStyle(self.getOption('FillStyle',1001))
        else:
            plot.SetFillStyle(0)
            plot.SetLineWidth(self.getOption('LineWidth',1))
        plot.SetLineColor(self.getOption('LineColor',1))
        plot.SetMarkerColor(self.getOption('MarkerColor',1))
        plot.SetMarkerStyle(self.getOption('MarkerStyle',20))
        plot.SetMarkerSize(self.getOption('MarkerSize',1.6))
        ## Plot specific-options, from spec
        plot.GetYaxis().SetTitle(spec.getOption('YTitle',spec.getOption("YTitle","Events")))
        plot.GetXaxis().SetTitle(spec.getOption('XTitle',spec.name))
        plot.GetXaxis().SetNdivisions(spec.getOption('XNDiv',510))
    def getPlot(self,plotspec,cut):
        ret = self.getPlotRaw(plotspec.name, plotspec.expr, plotspec.bins, cut, plotspec)
        # fold overflow
        if ret.ClassName() in [ "TH1F", "TH1D" ] :
            n = ret.GetNbinsX()
            if plotspec.getOption('IncludeOverflows',True) and ret.ClassName() != "TProfile":
                ret.SetBinContent(1,ret.GetBinContent(0)+ret.GetBinContent(1))
                ret.SetBinContent(n,ret.GetBinContent(n+1)+ret.GetBinContent(n))
                ret.SetBinError(1,hypot(ret.GetBinError(0),ret.GetBinError(1)))
                ret.SetBinError(n,hypot(ret.GetBinError(n+1),ret.GetBinError(n)))
            rebin = plotspec.getOption('rebinFactor',0)
            if plotspec.bins[0] != "[" and rebin > 1 and n > 5:
                while n % rebin != 0: rebin -= 1
                if rebin != 1: ret.Rebin(rebin)
            if plotspec.getOption('Density',False):
                for b in xrange(1,n+1):
                    ret.SetBinContent( b, ret.GetBinContent(b) / ret.GetXaxis().GetBinWidth(b) )
                    ret.SetBinError(   b, ret.GetBinError(b) / ret.GetXaxis().GetBinWidth(b) )
        self._stylePlot(ret,plotspec)
        return ret
    def getPlotRaw(self,name,expr,bins,cut,plotspec):
        unbinnedData2D = plotspec.getOption('UnbinnedData2D',False) if plotspec != None else False
        profile1D      = plotspec.getOption('Profile1D',False) if plotspec != None else False
        if self._options.doS2V:
            expr = scalarToVector(expr)
        if not self._isInit: self._init()
        if self._weight:
            if self._isdata: cut = "(%s)     *(%s)*(%s)" % (self._weightString,                    self._scaleFactor, self.adaptExpr(cut,cut=True))
            else:            cut = "(%s)*(%s)*(%s)*(%s)" % (self._weightString,self._options.lumi, self._scaleFactor, self.adaptExpr(cut,cut=True))
        if self._options.doS2V:
            cut  = scalarToVector(cut)
        if ROOT.gROOT.FindObject("dummy") != None: ROOT.gROOT.FindObject("dummy").Delete()
        histo = None
        canKeys = False
        if ":" in expr.replace("::","--") and not profile1D:
            if bins[0] == "[":
                xbins, ybins = bins.split("*")
                xedges = [ float(f) for f in xbins[1:-1].split(",") ]
                yedges = [ float(f) for f in ybins[1:-1].split(",") ]
                histo = ROOT.TH2F("dummy","dummy",len(xedges)-1,array('f',xedges),len(yedges)-1,array('f',yedges))
            else:
                (nbx,xmin,xmax,nby,ymin,ymax) = bins.split(",")
                histo = ROOT.TH2F("dummy","dummy",int(nbx),float(xmin),float(xmax),int(nby),float(ymin),float(ymax))
                unbinnedData2D = (self._name == "data") and unbinnedData2D
        else:
            if bins[0] == "[":
                edges = [ float(f) for f in bins[1:-1].split(",") ]
                if profile1D: 
                    histo = ROOT.TProfile("dummy","dummy",len(edges)-1,array('f',edges))
                else:
                    histo = ROOT.TH1F("dummy","dummy",len(edges)-1,array('f',edges))
            else:
                (nb,xmin,xmax) = bins.split(",")
                if profile1D:
                    histo = ROOT.TProfile("dummy","dummy",int(nb),float(xmin),float(xmax))
                else:
                    histo = ROOT.TH1F("dummy","dummy",int(nb),float(xmin),float(xmax))
                    canKeys = True
            unbinnedData2D = False
        histo.Sumw2()
        if unbinnedData2D:
            self._tree.Draw("%s" % (self.adaptExpr(expr)), cut)
            graph = ROOT.gROOT.FindObject("Graph").Clone(name)
            return graph
        drawOpt = "goff"
        if profile1D: drawOpt += " PROF";
        self._tree.Draw("%s>>%s" % (self.adaptExpr(expr),"dummy"), cut, drawOpt)
        if canKeys and histo.GetEntries() > 0 and histo.GetEntries() < self.getOption('KeysPdfMinN',100) and not self._isdata and self.getOption("KeysPdf",False):
            #print "Histogram for %s/%s has %d entries, so will use KeysPdf " % (self._cname, self._name, histo.GetEntries())
            if "/TH1Keys_cc.so" not in ROOT.gSystem.GetLibraries(): 
                ROOT.gROOT.ProcessLine(".L %s/src/CMGTools/TTHAnalysis/python/plotter/TH1Keys.cc+" % os.environ['CMSSW_BASE']);
            (nb,xmin,xmax) = bins.split(",")
            histo = ROOT.TH1KeysNew("dummyk","dummyk",int(nb),float(xmin),float(xmax))
            self._tree.Draw("%s>>%s" % (self.adaptExpr(expr),"dummyk"), cut, "goff")
            self.negativeCheck(histo)
            return histo.GetHisto().Clone(name)
        #elif not self._isdata and self.getOption("KeysPdf",False):
        #else:
        #    print "Histogram for %s/%s has %d entries, so won't use KeysPdf (%s, %s) " % (self._cname, self._name, histo.GetEntries(), canKeys, self.getOption("KeysPdf",False))
        self.negativeCheck(histo)
        return histo.Clone(name)
    def negativeCheck(self,histo):
        if not self._options.allowNegative: 
            if "TH1" in histo.ClassName():
                for b in xrange(0,histo.GetNbinsX()+2):
                    if histo.GetBinContent(b) < 0: histo.SetBinContent(b, 0.0)
            elif "TH2" in histo.ClassName():
                for bx in xrange(0,histo.GetNbinsX()+2):
                    for by in xrange(0,histo.GetNbinsY()+2):
                        if histo.GetBinContent(bx,by) < 0: histo.SetBinContent(bx,by, 0.0)
    def __str__(self):
        mystr = ""
        mystr += str(self._fname) + '\n'
        mystr += str(self._tfile) + '\n'
        mystr += str(self._weight) + '\n'
        mystr += str(self._scaleFactor)
        return mystr

def addTreeToYieldOptions(parser):
    parser.add_option("-l", "--lumi",           dest="lumi",   type="float", default="19.7", help="Luminosity (in 1/fb)");
    parser.add_option("-u", "--unweight",       dest="weight",       action="store_false", default=True, help="Don't use weights (in MC events)");
    parser.add_option("-W", "--weightString",   dest="weightString", type="string", default="1", help="Use weight (in MC events)");
    parser.add_option("--fsy", "--full-sample-yield",  dest="fullSampleYields", action="store_true", default=False, help="Compute also the yield as if all events passed");
    parser.add_option("-f", "--final",  dest="final", action="store_true", help="Just compute final yield after all cuts");
    parser.add_option("-e", "--errors",  dest="errors", action="store_true", help="Include uncertainties in the reports");
    parser.add_option("--tf", "--text-format",   dest="txtfmt", type="string", default="text", help="Output format: text, html");
    parser.add_option("-S", "--start-at-cut",   dest="startCut",   type="string", help="Run selection starting at the cut matched by this regexp, included.") 
    parser.add_option("-U", "--up-to-cut",      dest="upToCut",   type="string", help="Run selection only up to the cut matched by this regexp, included.") 
    parser.add_option("-X", "--exclude-cut", dest="cutsToExclude", action="append", default=[], help="Cuts to exclude (regexp matching cut name), can specify multiple times.") 
    parser.add_option("-I", "--invert-cut",  dest="cutsToInvert",  action="append", default=[], help="Cuts to invert (regexp matching cut name), can specify multiple times.") 
    parser.add_option("-R", "--replace-cut", dest="cutsToReplace", action="append", default=[], nargs=3, help="Cuts to invert (regexp of old cut name, new name, new cut); can specify multiple times.") 
    parser.add_option("-A", "--add-cut",     dest="cutsToAdd",     action="append", default=[], nargs=3, help="Cuts to insert (regexp of cut name after which this cut should go, new name, new cut); can specify multiple times.") 
    parser.add_option("-N", "--n-minus-one", dest="nMinusOne", action="store_true", help="Compute n-minus-one yields and plots")
    parser.add_option("-t", "--tree",          dest="tree", default='ttHLepTreeProducerTTH', help="Pattern for tree name");
    parser.add_option("-G", "--no-fractions",  dest="fractions",action="store_false", default=True, help="Don't print the fractions");
    parser.add_option("-F", "--add-friend",    dest="friendTrees",  action="append", default=[], nargs=2, help="Add a friend tree (treename, filename). Can use {name}, {cname} patterns in the treename") 
    parser.add_option("--FMC", "--add-friend-mc",    dest="friendTreesMC",  action="append", default=[], nargs=2, help="Add a friend tree (treename, filename) to MC only. Can use {name}, {cname} patterns in the treename") 
    parser.add_option("--FD", "--add-friend-data",    dest="friendTreesData",  action="append", default=[], nargs=2, help="Add a friend tree (treename, filename) to data trees only. Can use {name}, {cname} patterns in the treename") 
    parser.add_option("--mcc", "--mc-corrections",    dest="mcCorrs",  action="append", default=[], nargs=1, help="Load the following file of mc to data corrections") 
    parser.add_option("--s2v", "--scalar2vector",     dest="doS2V",    action="store_true", default=False, help="Do scalar to vector conversion") 
    parser.add_option("--neg", "--allow-negative-results",     dest="allowNegative",    action="store_true", default=False, help="If the total yield is negative, keep it so rather than truncating it to zero") 
    parser.add_option("--pV", "--printVariables",     dest="prtVars",    action="store_true", default=False, help="Print values of the variables relevant for the mcAnalysis cuts")
    parser.add_option("--oD", "--output-directory", dest="outDir",  type="string", default=None, help="Path to the output directory")

def mergeReports(reports):
    import copy
    one = copy.deepcopy(reports[0])
    for i,(c,x) in enumerate(one):
        one[i][1][1] = pow(one[i][1][1], 2)
    for two in reports[1:]:
        for i,(c,x) in enumerate(two):
            one[i][1][0] += x[0]
            one[i][1][1] += pow(x[1],2)
    for i,(c,x) in enumerate(one):
        one[i][1][1] = sqrt(one[i][1][1])
    return one

def mergePlots(name,plots):
    one = plots[0].Clone(name)
    if "TGraph" in one.ClassName():
        others = ROOT.TList()
        for two in plots[1:]: 
            others.Add(two)
        one.Merge(others)
    else:         
        for two in plots[1:]: 
            one.Add(two)
    return one

