#!/bin/sh

source /afs/cern.ch/user/g/gpetrucc/sh/init_root528_afs
if [ ${1: -5} == ".root" ]
then
	root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("'$1'")'
else
	if [[ $1 != "" ]]
		then path=$1
		else path=/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/21-08-2014/2/1
	fi
if [[ $1 != "" ]]
	then
		case $2 in
			1 )  arg=mu_pteta_low_b.root   ;;
			2 )  arg=mu_pteta_high_b.root  ;;
			3 )  arg=mu_pteta_low_e.root   ;;
			4 )  arg=mu_pteta_high_e.root  ;;
			5 )  arg=el_pteta_low_cb.root  ;;
			6 )  arg=el_pteta_low_fb.root  ;;
			7 )  arg=el_pteta_low_ec.root  ;;
			8 )  arg=el_pteta_high_cb.root ;;
			9 )  arg=el_pteta_high_fb.root ;;
			10 ) arg=el_pteta_high_ec.root ;;
		esac	
	else path=/afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/21-08-2014/2/1
	fi

	root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("'$path'/'$arg'")'
fi

