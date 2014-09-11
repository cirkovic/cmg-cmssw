echo 5_3_19:
echo 2lss_mumu:
python mcAnalysis.py mca_sh.txt -p ttHWW,TT bins/2lss_mumu.txt -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -F sf/t /afs/cern.ch/user/c/cirkovic/backup_02-09-2014/27-08-2014/2_1/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_ee:
python mcAnalysis.py mca_sh.txt -p ttHWW,TT bins/2lss_ee.txt -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -F sf/t /afs/cern.ch/user/c/cirkovic/backup_02-09-2014/27-08-2014/2_1/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 2lss_em:
python mcAnalysis.py mca_sh.txt -p ttHWW,TT bins/2lss_em.txt -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -F sf/t /afs/cern.ch/user/c/cirkovic/backup_02-09-2014/27-08-2014/2_1/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 3l_tight:
python mcAnalysis.py mca_sh.txt -p ttHWW,TT bins/3l_tight.txt -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -F sf/t /afs/cern.ch/user/c/cirkovic/backup_02-09-2014/27-08-2014/2_1/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton
echo 4l:
python mcAnalysis.py mca_sh.txt -p ttHWW,TT bins/4l.txt -P /afs/cern.ch/work/c/cirkovic/TREES_53X_170714_1 -F sf/t /afs/cern.ch/user/c/cirkovic/backup_02-09-2014/27-08-2014/2_1/evVarFriend_{cname}.root -l 19.6 -j 6 --s2v --tree treeProducerSusyMultilepton

