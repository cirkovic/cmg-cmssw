# ./run_mcAnalysis_03-12-2014.sh --pV
echo
echo "-- mumu --"
mkdir output_mumu
python mcAnalysis.py mca-CSA14.txt bins/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/03-12-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_mumu ${1}
echo
echo "-- ee --"
mkdir output_ee
python mcAnalysis.py mca-CSA14.txt bins/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/03-12-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/cfg/OUTPUT -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_ee ${1}
echo

