echo
echo "-- mumu --"
python mcAnalysis.py mca-CSA14.txt bins/2lss_mumu.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT1_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_default_complete/evVarFriend_{cname}.root -P /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_complete -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u
echo "-- em --"
echo
python mcAnalysis.py mca-CSA14.txt bins/2lss_em.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT1_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_default_complete/evVarFriend_{cname}.root -P /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_complete -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u
echo
echo "-- ee --"
python mcAnalysis.py mca-CSA14.txt bins/2lss_ee.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT1_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_complete/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/OUTPUT2_default_complete/evVarFriend_{cname}.root -P /afs/cern.ch/work/c/cirkovic/Milos_21-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_complete -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u
echo

