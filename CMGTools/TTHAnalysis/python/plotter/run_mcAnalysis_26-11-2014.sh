echo
echo "-- mumu --"
python mcAnalysis.py mca-CSA14_sync_26-11-2014.txt bins/2lss_mumu_sync.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/26-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_TTH_sync_deltaBeta_doPuId -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u
echo
echo "-- ee --"
python mcAnalysis.py mca-CSA14_sync_26-11-2014.txt bins/2lss_ee_sync.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/26-11-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT_TTH_sync_deltaBeta_doPuId -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u
echo

