from CMGTools.TTHAnalysis.treeReAnalyzer import *

class LepGoodInds:
    def __init__(self):
 	self.branches = [ "LepGood_index" ]
    def listBranches(self):
        return self.branches[:]	
    def __call__(self,event):
        # make python lists as Collection does not support indexing in slices
        leps = [l for l in Collection(event,"LepGood","nLepGood",4)]
        ret = dict([(name,[]) for name in self.branches])
        ret["LepGood_index"] = [i for i in xrange(0, len(leps))]
    	return ret

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = LepGoodInds()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

        
