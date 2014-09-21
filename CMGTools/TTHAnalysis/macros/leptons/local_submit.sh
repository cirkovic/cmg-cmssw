#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Retraining_200914/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Retraining_200914/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/leptons

case $1 in
   0 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("mu_pteta_high_b")' ;;
   1 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("mu_pteta_low_b")' ;;
   2 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("mu_pteta_high_e")' ;;
   3 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("mu_pteta_low_e")' ;;
   4 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_high_cb")' ;;
   5 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_low_cb")' ;;
   6 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_high_fb")' ;;
   7 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_low_fb")' ;;
   8 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_high_ec")' ;;
   9 )
      root.exe -b -l -q trainTTH.root trainTTJetsLep.root trainTTJetsSem.root trainTTJetsHad.root 'trainLeptonID.cxx("el_pteta_low_ec")' ;;
esac

