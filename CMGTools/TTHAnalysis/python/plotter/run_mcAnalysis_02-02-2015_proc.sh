# ./run_mcAnalysis_02-02-2015.sh --pV

PS=""

echo
echo "-- loose electrons --"
mkdir output_loose_electrons
python mcAnalysis.py mca-PHYS14.txt bins/2lss_ee_LooseLeptons.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_loose_electrons ${1} 2>&1 | tee STDOUT_loose_electrons.txt &
PS="$PS $!"
echo
echo "-- loose muons --"
mkdir output_loose_muons
python mcAnalysis.py mca-PHYS14.txt bins/2lss_mumu_LooseLeptons.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_loose_muons ${1} 2>&1 | tee STDOUT_loose_muons.txt &
PS="$PS $!"
echo
echo "-- tight electrons --"
mkdir output_tight_electrons
python mcAnalysis.py mca-PHYS14.txt bins/2lss_ee_TightLeptons.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_tight_electrons ${1} 2>&1 | tee STDOUT_tight_electrons.txt &
PS="$PS $!"
echo
echo "-- tight muons --"
mkdir output_tight_muons
python mcAnalysis.py mca-PHYS14.txt bins/2lss_mumu_TightLeptons.txt -P /afs/cern.ch/work/c/cirkovic/Synchronization/23-01-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/cfg/LOCAL -j 6 --s2v --tree treeProducerSusyMultilepton -u --oD output_tight_muons ${1} 2>&1 | tee STDOUT_tight_muons.txt &
PS="$PS $!"
echo

wait $PS

cat STDOUT_*.txt

