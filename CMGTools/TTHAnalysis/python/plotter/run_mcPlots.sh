python mcPlots.py mca-2lss-dataBCat_PHYS14_ee.txt ttH-multilepton/2lss_ee.txt ttH-multilepton/mvaVars_2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/TREES_72X_newPresel_small --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_23-02-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_eventVars_2lss/evVarFriend_{cname}.root --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_24-03-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_finalMVA_2lss/evVarFriend_{cname}.root -l 10.0 -j 6 --s2v --tree treeProducerSusyMultilepton -X '2B tight' --rebin 2 -f --pdir /afs/cern.ch/user/c/cirkovic/www/25-03-2015/plots/1/ee

python mcPlots.py mca-2lss-dataBCat_PHYS14_em.txt ttH-multilepton/2lss_em.txt ttH-multilepton/mvaVars_2lss_em.txt -P /afs/cern.ch/work/c/cirkovic/TREES_72X_newPresel_small --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_23-02-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_eventVars_2lss/evVarFriend_{cname}.root --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_24-03-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_finalMVA_2lss/evVarFriend_{cname}.root -l 10.0 -j 6 --s2v --tree treeProducerSusyMultilepton -X '2B tight' --rebin 2 -f --pdir /afs/cern.ch/user/c/cirkovic/www/25-03-2015/plots/1/em

python mcPlots.py mca-2lss-dataBCat_PHYS14_mumu.txt ttH-multilepton/2lss_mumu.txt ttH-multilepton/mvaVars_2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/TREES_72X_newPresel_small --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_23-02-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_eventVars_2lss/evVarFriend_{cname}.root --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_24-03-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_finalMVA_2lss/evVarFriend_{cname}.root -l 10.0 -j 6 --s2v --tree treeProducerSusyMultilepton -X '2B tight' --rebin 2 -f --pdir /afs/cern.ch/user/c/cirkovic/www/25-03-2015/plots/1/mumu
