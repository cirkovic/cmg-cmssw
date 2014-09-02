#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_01-09-2014/CMSSW_7_0_6_patch3/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_01-09-2014/CMSSW_7_0_6_patch3/src/CMGTools/TTHAnalysis/macros/leptons

case $1 in
	1 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_high_b")' ;;
	2 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_low_b")' ;;
	3 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_high_e")' ;;
	4 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_low_e")' ;;
	5 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_cb")' ;;
	6 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_cb")' ;;
	7 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_fb")' ;;
	8 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_fb")' ;;
	9 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_ec")' ;;
	10 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_ec")' ;;
esac

