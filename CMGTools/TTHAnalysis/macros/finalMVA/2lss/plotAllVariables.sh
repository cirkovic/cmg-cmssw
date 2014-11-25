for i in `find ttbar_* -name '*.root'`; do cd `dirname $i`; root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("'`basename $i`'")'; cd ..; done
for i in `ls ttbar_*/plots -d`; do cp /afs/cern.ch/user/c/cirkovic/www/11-10-2014/1/3l/3l_4j_6var_test/plots/index.php $i; done

