#!/bin/sh

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

