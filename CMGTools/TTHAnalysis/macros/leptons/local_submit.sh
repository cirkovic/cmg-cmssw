#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/macros/leptons

case $1 in
	1 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_high_b")' ;;
	2 )
      root -l -q 'trainLeptonID.cxx("mu_pteta_meduim_b")' ;;
	3 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_low_b")' ;;
	4 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_high_e")' ;;
	5 )
      root -l -q 'trainLeptonID.cxx("mu_pteta_meduim_e")' ;;
	6 )
		root -l -q 'trainLeptonID.cxx("mu_pteta_low_e")' ;;
	7 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_cb")' ;;
	8 )
		root -l -q 'trainLeptonID.cxx("el_pteta_meduim_cb")' ;;
	9 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_cb")' ;;
	10 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_fb")' ;;
	11 )
		root -l -q 'trainLeptonID.cxx("el_pteta_meduim_fb")' ;;
	12 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_fb")' ;;
	13 )
		root -l -q 'trainLeptonID.cxx("el_pteta_high_ec")' ;;
	14 )
      root -l -q 'trainLeptonID.cxx("el_pteta_meduim_ec")' ;;
	15 )
		root -l -q 'trainLeptonID.cxx("el_pteta_low_ec")' ;;
esac

