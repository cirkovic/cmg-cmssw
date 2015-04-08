# ./run_mcAnalysis.sh [--pV [--eP [--cS]]]

echo
echo "-- ee final state --"
#rm -rf output_ee_final_state/*
python mcAnalysis.py mca-PHYS14.txt ttH-multilepton/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/21-03-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/TEST1 --s2v --tree treeProducerSusyMultilepton -u --oD output_ee_final_state ${1} ${2}
echo
echo "-- mumu final state --"
#rm -rf output_mumu_final_state/*
python mcAnalysis.py mca-PHYS14.txt ttH-multilepton/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/21-03-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/TEST1 --s2v --tree treeProducerSusyMultilepton -u --oD output_mumu_final_state ${1} ${2}
echo
