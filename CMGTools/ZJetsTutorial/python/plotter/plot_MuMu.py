import imp
import math
import copy
import time
import re

from CMGTools.ZJetsTutorial.plotter.ZDataMC import ZDataMC
from CMGTools.ZJetsTutorial.plotter.prepareComponents import prepareComponents
from CMGTools.ZJetsTutorial.plotter.rootutils import *
from CMGTools.RootTools.Style import *
from ROOT import kPink, TH1, TPaveText, TPad, TChain

  
NBINS = 100
XMIN  = 0
XMAX  = 200



def makePlot( var, anaDir, selComps, weights,
              nbins=None, xmin=None, xmax=None,
              cut='', weight='weight', embed=False, shift=None,
              VVgroup=None, treeName=None):

    oscut = cut + ' && diL_charge==0'
    print 'making the plot:', var, 'cut', oscut
    osign = ZDataMC(var, anaDir,
                    selComps, weights, nbins, xmin, xmax,
                    cut=oscut, weight=weight, 
                    treeName = treeName)    
    if VVgroup:
        osign.Group('VV',VVgroup)
    return osign


def normalizeDY(selComps, weight=None):
    if weight is None:
        weight = 'weight'    
    oscut = 'diL_charge==0 && leg1_relIso05<0.1 && leg2_relIso05<0.1'
    print 'normalizing with cut', oscut,
    min = 80
    max = 100
    nbins = max - min
    osign = ZDataMC('diL_mass', anaDir,
                    selComps, weights, nbins, min, max,
                    cut=oscut, weight=weight, 
                    treeName = treeName)
    factor = osign.Hist('Data').Integral(True, min, max) / osign.Hist('Ztt').Integral(True, min, max)
    # import pdb; pdb.set_trace()
    weights['Ztt'].addWeight *= factor
    print 'factor=',factor 
    print weights['Ztt']

def plot(var, cut=None,
         nbins=100, xmin=0, xmax=200, weight=None):
    if weight is None:
        weight = 'weight'
    if cut is None:
        cut = options.cut
    osign = makePlot( var, anaDir, selComps, weights,
                      nbins, xmin, xmax,
                      cut, weight=weight,
                      VVgroup=cfg.VVgroup, treeName=treeName)
    draw(osign)
    print osign
    return osign
    

if __name__ == '__main__':

    import copy
    from optparse import OptionParser
    from CMGTools.RootTools.RootInit import *
    from CMGTools.H2TauTau.proto.plotter.officialStyle import officialStyle
    officialStyle(gStyle)


    parser = OptionParser()
    parser.usage = '''
    %prog <anaDir> <cfgFile>

    cfgFile: analysis configuration file, see CMGTools.H2TauTau.macros.MultiLoop
    anaDir: analysis directory containing all components, see CMGTools.H2TauTau.macros.MultiLoop.
    hist: histogram you want to plot
    '''
    parser.add_option("-H", "--hist", 
                      dest="hist", 
                      help="histogram list",
                      default='diL_mass')
    parser.add_option("-C", "--cut", 
                      dest="cut", 
                      help="cut to apply in TTree::Draw",
                      default='1')
    parser.add_option("-c", "--channel", 
                      dest="channel", 
                      help="channel: TauEle or TauMu (default)",
                      default='TauMu')
    parser.add_option("-E", "--embed", 
                      dest="embed", 
                      help="Use embedd samples.",
                      action="store_true",
                      default=False)
    parser.add_option("-B", "--blind", 
                      dest="blind", 
                      help="Blind.",
                      action="store_true",
                      default=False)
    parser.add_option("-b", "--batch", 
                      dest="batch", 
                      help="Set batch mode.",
                      action="store_true",
                      default=False)
    parser.add_option("-p", "--prefix", 
                      dest="prefix", 
                      help="Prefix for the root files, eg. MC to get MC_eleTau_vbf.root",
                      default=None)
    parser.add_option("-n", "--nbins", 
                      dest="nbins", 
                      help="Number of bins",
                      default=None)
    parser.add_option("-m", "--min", 
                      dest="xmin", 
                      help="xmin",
                      default=None)
    parser.add_option("-M", "--max", 
                      dest="xmax", 
                      help="xmax",
                      default=None)
    parser.add_option("-g", "--higgs", 
                      dest="higgs", 
                      help="Higgs mass: 125, 130,... or dummy",
                      default=None)
    
    (options,args) = parser.parse_args()

        
    cutstring = options.cut
    
    if len(args) != 2:
        parser.print_help()
        sys.exit(1)
    if options.batch:
        gROOT.SetBatch()
    if options.nbins is None:
        NBINS = 200
        XMIN = 70
        XMAX = 120
    else:
        NBINS = int(options.nbins)
        XMIN = float(options.xmin)
        XMAX = float(options.xmax)
    
    dataName = 'Data'

    #WARNING!
    weight='weight'
    
    anaDir = args[0].rstrip('/')

        
    cfgFileName = args[1]
    file = open( cfgFileName, 'r' )
    cfg = imp.load_source( 'cfg', cfgFileName, file)
    embed = options.embed

    treeName = 'ZJetsTreeProducer'

    aliases = None
    selComps, weights, zComps = prepareComponents(
        anaDir, cfg.config, aliases,
        options.embed,
        channel=options.channel, higgsMass=options.higgs,
        forcedLumi = 5000.)

    normalizeDY( selComps )
    
    ocan = buildCanvas()

    jetcut = 'jet1_pt>30 && jet1_looseJetId>0.5 && jet1_puJetId>0.5 && diL_charge==0 && leg1_relIso05<0.1 && leg2_relIso05<0.1 && diL_charge==0 && abs(diL_mass-91.2)<15'
    osign = plot(options.hist, options.cut, NBINS, XMIN, XMAX)
    
