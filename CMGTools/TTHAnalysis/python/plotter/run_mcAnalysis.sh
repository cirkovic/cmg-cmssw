# ./run_mcAnalysis.sh [--pV [--eP [--cS]]]

#INPUT=/afs/cern.ch/work/c/cirkovic/Synchronization/19-10-2015/CMSSW_7_4_12_patch4/src/CMGTools/TTHAnalysis/cfg/Test_allttHsync/
#INPUT=/afs/cern.ch/work/c/cirkovic/Synchronization/19-10-2015/CMSSW_7_4_12_patch4/src/CMGTools/TTHAnalysis/cfg/TEST1/Test_allttHsync
#INPUT=/afs/cern.ch/work/c/cirkovic/Synchronization/19-10-2015/CMSSW_7_4_12_patch4/src/CMGTools/TTHAnalysis/cfg/Test_all
#INPUT=/afs/cern.ch/work/c/cirkovic/Synchronization/19-10-2015/CMSSW_7_4_12_patch4/src/CMGTools/TTHAnalysis/cfg/TTHForSynch
INPUT=/afs/cern.ch/work/b/botta/TTHForSynch/TTHnobb

#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/20-10-2015/Synchronization/2
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/20-10-2015/Synchronization/3
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/20-10-2015/Synchronization/4
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/20-10-2015/Synchronization/6
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/21-10-2015/Synchronization/1
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/26-10-2015/Synchronization/1
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/26-10-2015/Synchronization/2
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/26-10-2015/Synchronization/3
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/27-10-2015/Synchronization/1
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/27-10-2015/Synchronization/2
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/27-10-2015/Synchronization/3
#OUTBASE=/afs/cern.ch/user/c/cirkovic/www/29-10-2015/Synchronization/2
OUTBASE=/afs/cern.ch/user/c/cirkovic/www/30-10-2015/Synchronization/1

FTREES=""
FTREES="$FTREES -F sf/t /afs/cern.ch/work/c/cirkovic/Synchronization/29-10-2015/CMSSW_7_4_12_patch4/src/CMGTools/TTHAnalysis/macros/FTREES/LepGoodInds/evVarFriend_{cname}.root"

OUTPUT=${OUTBASE}/electrons/
echo "-- electrons --"
rm -rf ${OUTPUT}
mkdir -p ${OUTPUT}
#echo "     event      pT  Eta  Phi      E pdgID charge    miniIso miniIsoCharged miniIsoNeutral   jetPtRel jetCSV jetPtRatio  sip3D    dxy     dz  segmentCompatibility" > ${OUTPUT}/cut1.txt
python mcAnalysis.py bins/mca-SYNC.txt bins/electrons.txt -P $INPUT $FTREES --s2v --tree treeProducerSusyMultilepton -u --oD ${OUTPUT} --pV --lepType=electron ${2} #&
echo

OUTPUT=${OUTBASE}/muons/
echo "-- muons --"
rm -rf ${OUTPUT}
mkdir -p ${OUTPUT}
#echo "     event      pT  Eta  Phi      E pdgID charge    miniIso miniIsoCharged miniIsoNeutral   jetPtRel jetCSV jetPtRatio  sip3D    dxy     dz  eleMVA" > ${OUTPUT}/cut1.txt
python mcAnalysis.py bins/mca-SYNC.txt bins/muons.txt -P $INPUT $FTREES --s2v --tree treeProducerSusyMultilepton -u --oD ${OUTPUT} --pV --lepType=muon ${2} #&
echo

