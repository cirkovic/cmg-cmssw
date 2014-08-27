#!/bin/sh

cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/CMSSW_5_3_19/src/CMGTools/TTHAnalysis/python/plotter

case $1 in
   1 )
		python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots.txt bins/2lss_mumu.txt roc_2lss_mumu.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_1/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv roc_2lss_mumu.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_2/1
		rm roc_2lss_mumu.root
		;;
	2 )
		python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots.txt bins/2lss_em.txt roc_2lss_em.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_1/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv roc_2lss_em.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_2/2
      rm roc_2lss_em.root
		;;
	3 )
		python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots.txt bins/2lss_ee.txt roc_2lss_ee.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_1/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv roc_2lss_ee.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_2/3
      rm roc_2lss_ee.root
		;;
	4 )
		python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots.txt bins/3l_tight.txt roc_3l.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_1/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
		mv roc_3l.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_2/4
      rm roc_3l.root
		;;
	5 )
		python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots.txt bins/4l.txt roc_4l.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_1/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v -X 2B
		mv roc_4l.png /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/2_2/5
      rm roc_4l.root
		;;
esac

