from CMGTools.TTHAnalysis.treeReAnalyzer import *
from CMGTools.TTHAnalysis.tools.mvaTool import *
import sys

class FinalMVA_2LSS:
    def __init__(self):
        self._MVAs = {}
        lines = []
        #self._path="/afs/cern.ch/user/c/cirkovic/www/06-03-2015/Trainings/1/finalMVA/categorized/"
        self._path="/afs/cern.ch/user/c/cirkovic/www/25-03-2015/Trainings/1/finalMVA/categorized/"
        with open(self._path+"variables_2lss.txt") as f:
        #with open(self._path+"variables_3l.txt") as f:
            lines = f.readlines()
            varnames = [vn for vn in [lines[i][:-1] for i in xrange(0, len(lines), 4)] if vn[0] != '#']
            vardefs = [vd for vd in [lines[i][:-1] for i in xrange(2, len(lines), 4)] if vd[0] != '#']
            #print zip(varnames, vardefs)
            #sys.exit()
        self._VAR_TABLE = []
        for item in zip(varnames, vardefs):
            self._VAR_TABLE.append(MVAVar(item[0], func = eval('lambda ev : '+item[1])))
        self._vars = {}
        #with open(self._path+"labeled_indexes_2lss.txt") as f:
        with open(self._path+"labeled_indexes_2lss.txt") as f:
        #with open(self._path+"labeled_indexes_3l.txt") as f:
            lines = f.readlines()
            catnames = [vn for vn in [lines[i][:-1] for i in xrange(0, len(lines), 3)] if vn[0] != '#']
            catdefs = [vd for vd in [lines[i][:-1] for i in xrange(1, len(lines), 3)] if vd[0] != '#']
            lines = catdefs
            for catname, line in zip(catnames, lines):
                self._vars.update({catname : []})
                for i in xrange(0, 10):
                    line = line.replace("  ", " ")
                line = line.split(' ')
                #print line
                for i in line:
                    #print i
                    self._vars[catname].append(self._VAR_TABLE[int(i)])
            #sys.exit()
        #P=self._path+"RETTBAR/";
        #P=self._path+"RETTBAR/";
        #P=self._path+"RETTBAR_20/";
        P=self._path+"TTBAR_TTW/";
        #P=self._path+"REMIX/";
        dirs = ['ttW_4jee', 'ttW_4jem', 'ttW_4jmm', 'ttW_5Ljee', 'ttW_5Ljem', 'ttW_5Ljmm', 'ttbar_4jee', 'ttbar_4jem', 'ttbar_4jmm', 'ttbar_5Ljee', 'ttbar_5Ljem', 'ttbar_5Ljmm']
        #dirs = ['ttbar_4j', 'ttbar_5Lj', 'ttbar_45j', 'ttbar_6Lj']
        #dirs = ['ttbar_4j', 'ttbar_5Lj', 'ttbar_45j']
        #dirs = ['ttbar_6Lj']
        #dirs = ['ttbar_23jBloose', 'ttbar_23jBtight', 'ttbar_4jBloose', 'ttbar_4jBtight', 'ttbar_4LjBloose', 'ttbar_4LjBtight', 'ttbar_5LBloose', 'ttbar_5LjBtight']
        #Nvars = 6
        for d in dirs:
            print d
            #for var in self._vars[d][0:Nvars]:
            for var in self._vars[d]:
                print "\t", var.name
            print
            self._MVAs["MVA_2LSS_{0}".format(d)] = MVATool("MVA_2LSS_{0}".format(d),
                P+"{0}/weights/{0}_BDTG.weights.xml".format(d),
                #self._vars[d][0:Nvars])
                self._vars[d])
        #sys.exit()
    def listBranches(self):
        return self._MVAs.keys()
    def __call__(self,event):
        return dict([ (name, mva(event)) for name, mva in self._MVAs.iteritems()])

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    #tree.AddFriend("sf/t", argv[2])
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = FinalMVA_2LSS()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

