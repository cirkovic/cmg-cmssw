#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/python/plotter

case $1 in
   1 )
		python rocCurves.py -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_mumu.txt roc_2lss.txt -o OT_roc_mumu -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv OT_roc_mumu.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/08-09-2014/1/1/1
		rm OT_roc_mumu
		;;
	2 )
		python rocCurves.py -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_em.txt roc_2lss.txt -o OT_roc_em -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv OT_roc_em.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/08-09-2014/1/1/2
		rm OT_roc_em
		;;
	3 )
		python rocCurves.py -P /afs/cern.ch/work/c/cirkovic/05-09-2014/25ns -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_MVA_25ns.txt bins/2lss_ee.txt roc_2lss.txt -o OT_roc_ee -F sf/t /afs/cern.ch/work/c/cirkovic/05-09-2014/25nsLepMVAFT/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv OT_roc_ee.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/08-09-2014/1/1/3
		rm OT_roc_ee
		;;
#	4 )
#		python rocCurves.py -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -j 6 -f -l 19.6 mca_sh.txt bins/3l_tight.txt roc_3l.txt -o OT_roc_3l -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/3/evVarFriend_{cname}.root --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/4/sfFriend_{cname}.root -W 'puWeight*LepEff_3lep' -p 'TTW,TT' --sp 'TTW' -X 'lep MVA' --tree treeProducerSusyMultilepton --s2v
#		mv OT_roc_3l.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/5/4
#		rm OT_roc_3l
#		;;
#	5 )
#		python rocCurves.py -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -j 6 -f -l 19.6 mca_sh.txt bins/4l.txt roc_4l.txt -o OT_roc_4l -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/1/evVarFriend_{cname}.root -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/3/evVarFriend_{cname}.root --FM sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/4/sfFriend_{cname}.root -W 'puWeight*LepEff_4lep' -p 'TTW,TT' --sp 'TTW' -X 'lep12 MVA,lep34 MVA' --tree treeProducerSusyMultilepton --s2v -X '2B tight'
#		mv OT_roc_4l.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/31-08-2014/2/5/5
#		rm OT_roc_4l
#		;;
esac

