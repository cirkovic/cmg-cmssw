# ./run_mcAnalysis_28-01-2015.sh --pV
echo
echo "-- mumu --"
mkdir output_mumu
python mcAnalysis.py mca-PHYS14.txt bins/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_mumu ${1}
echo
echo "-- ee --"
mkdir output_ee
python mcAnalysis.py mca-PHYS14.txt bins/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_ee ${1}
echo

