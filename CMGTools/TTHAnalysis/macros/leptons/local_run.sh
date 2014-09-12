cd /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src
cmsenv
cd /afs/cern.ch/work/c/cirkovic/Milos_03-09-2014/CMSSW_7_0_6_patch1/src/CMGTools/TTHAnalysis/macros/leptons

case $3 in
   0 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("mu_pteta_high_b")' ;;
   1 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("mu_pteta_low_b")' ;;
   2 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("mu_pteta_high_e")' ;;
   3 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("mu_pteta_low_e")' ;;
   4 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_high_cb")' ;;
   5 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_low_cb")' ;;
   6 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_high_fb")' ;;
   7 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_low_fb")' ;;
   8 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_high_ec")' ;;
   9 )
      root.exe -b -l -q $1 $2 'trainLeptonID.cxx("el_pteta_low_ec")' ;;
esac

