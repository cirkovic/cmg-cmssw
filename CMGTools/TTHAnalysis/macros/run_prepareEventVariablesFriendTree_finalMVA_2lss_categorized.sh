#!/bin/sh

OUTDIR=${1}
rm -rf $OUTDIR bsub_all_${OUTDIR}.sh
mkdir $OUTDIR
python prepareEventVariablesFriendTree_finalMVA_2lss_categorized.py -q 1nh -N 50000 --tree treeProducerSusyMultilepton --FMC sf/t /afs/cern.ch/work/c/cirkovic/Milos_23-02-2015/CMSSW_7_2_3/src/CMGTools/TTHAnalysis/macros/FT_eventVars_2lss/evVarFriend_{cname}.root /afs/cern.ch/work/c/cirkovic/TREES_72X_newPresel_small $OUTDIR > bsub_all_${OUTDIR}.sh
chmod +x bsub_all_${OUTDIR}.sh

