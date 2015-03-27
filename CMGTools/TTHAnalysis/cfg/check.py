from ROOT import *

f = TFile.Open('TEST/TTH_sync/treeProducerSusyMultilepton/tree.root')
t = f.Get('tree')

i = 0
for e in t:
    print e.evt
    for il in xrange(e.nLepGood):
        #print '\t', e.LepGood_pdgId[il], e.LepGood_mvaTTH[il]
        print '\t', e.LepGood_pdgId[il], e.LepGood_mvaSusy[il]
    if i > 10: break
    i += 1
    
