echo 25ns:
echo 2lss_mumu:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_ee:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_em:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_em.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 3l_tight:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/3l_tight.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 4l:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/4l.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton


echo 50ns:
echo 2lss_mumu:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_50ns.txt bins/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/50ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/50nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_ee:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_50ns.txt bins/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/50ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/50nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_em:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_50ns.txt bins/2lss_em.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/50ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/50nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 3l_tight:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_50ns.txt bins/3l_tight.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/50ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/50nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 4l:
python mcAnalysis.py mca-2lss-dataBCat4Plots_MVA_50ns.txt bins/4l.txt -P /afs/cern.ch/work/c/cirkovic/05-09-2014/50ns -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/50nsLepMVAFT/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton

