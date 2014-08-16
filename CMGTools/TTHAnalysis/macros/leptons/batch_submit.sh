#!/bin/sh

for arg in mu_pteta_high_b mu_pteta_low_b mu_pteta_high_e mu_pteta_low_e el_pteta_high_cb el_pteta_low_cb el_pteta_high_fb el_pteta_low_fb el_pteta_high_ec el_pteta_low_ec
do
   chmod +x submit_script.sh
   bsub -q 8nh submit_script.sh $arg
done

