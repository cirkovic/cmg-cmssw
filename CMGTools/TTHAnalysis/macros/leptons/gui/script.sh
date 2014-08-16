source /afs/cern.ch/user/g/gpetrucc/sh/init_root528_afs

mkdir el_pteta_high_cb el_pteta_high_fb el_pteta_low_ec mu_pteta_high_b mu_pteta_low_b el_pteta_high_ec el_pteta_low_cb  el_pteta_low_fb mu_pteta_high_e mu_pteta_low_e

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_high_cb.root")'
mv plots el_pteta_high_cb

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_high_fb.root")'
mv plots el_pteta_high_fb

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_low_ec.root")'
mv plots el_pteta_low_ec

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("mu_pteta_high_b.root")'
mv plots mu_pteta_high_b

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("mu_pteta_low_b.root")'
mv plots mu_pteta_low_b

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_high_ec.root")'
mv plots el_pteta_high_ec

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_low_cb.root")'
mv plots el_pteta_low_cb

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("el_pteta_low_fb.root")'
mv plots el_pteta_low_fb

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("mu_pteta_high_e.root")'
mv plots mu_pteta_high_e

root -l '/afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00g/x86_64-slc5-gcc43-opt/root/tmva/test/TMVAGui.C("mu_pteta_low_e.root")'
mv plots mu_pteta_low_e


