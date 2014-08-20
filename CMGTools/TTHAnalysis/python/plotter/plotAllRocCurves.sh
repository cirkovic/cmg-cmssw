#2lss mumu, em, ee

#python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_ROC1.txt bins/2lss_mumu_ROC1.txt roc_2lss_ROC1.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
#mv roc_2lss_ROC1.root roc_2lss_mumu.root
#mv roc_2lss_ROC1.png roc_2lss_mumu.png

#python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_ROC1.txt bins/2lss_em_ROC1.txt roc_2lss_ROC1.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
#mv roc_2lss_ROC1.root roc_2lss_em.root
#mv roc_2lss_ROC1.png roc_2lss_em.png

#python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_ROC1.txt bins/2lss_ee_ROC1.txt roc_2lss_ROC1.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
#mv roc_2lss_ROC1.root roc_2lss_ee.root
#mv roc_2lss_ROC1.png roc_2lss_ee.png

#3l
python rocCurves.py -P /afs/cern.ch/work/g/gpetrucc/TREES_53X_170714 -j 6 -f -l 19.6 mca-2lss-dataBCat4Plots_ROC1.txt bins/2lss_ee_ROC1.txt roc_2lss_ROC1.txt -F sf/t /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/19-08-2014/2/2/evVarFriend_{cname}.root --tree treeProducerSusyMultilepton --s2v
mv roc_2lss_ROC1.root roc_2lss_ee.root
mv roc_2lss_ROC1.png roc_2lss_ee.png

#4l

