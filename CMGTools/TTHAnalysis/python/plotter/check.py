from ROOT import *
from array import array
#from CMGTools.TTHAnalysis import TPieE
#import CMGTools.TTHAnalysis.loadlibs

#gROOT.ProcessLine(".L TPieEx.cc++")
#gSystem.Load("libTPieE")

v = array('d', [0.2, 1.1, 0.6, 0.9, 2.3])
c = array('i', [2, 3, 4, 5, 6])
names = [ array( 'c', 'string1\0' ), array( 'c', 'string2\0' ), array( 'c', 'string3\0' ), array( 'c', 'string4\0' ), array( 'c', 'string5\0' ) ]
a = array( 'l', map( lambda x: x.buffer_info()[0], names ) )

print v
print c

c1 = TCanvas()
#p = TPie("p", "Pie", 5, v, None, None)
p = TPie("ThePie","ThePie",len(v),v,c)
p.SetRadius(.2)
p.SetLabelsOffset(0.01)
p.SetLabelFormat("#splitline{%val (%perc)}{%txt}")
p.Draw("nol <")

input("Press key to exit...")

