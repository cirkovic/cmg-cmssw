for i in {1..8}
do
	sed -i 's/LepGood'$i'_pdgId/LepGood_pdgId['$(( $i - 1 ))']/g' $1
	sed -i 's/LepGood'$i'_charge/LepGood_charge['$(( $i - 1 ))']/g' $1
	sed -i 's/LepGood'$i'_pt/LepGood_pt['$(( $i - 1 ))']/g' $1
	sed -i 's/LepGood'$i'_eta/LepGood_eta['$(( $i - 1 ))']/g' $1
	sed -i 's/LepGood'$i'_phi/LepGood_phi['$(( $i - 1 ))']/g' $1
	sed -i 's/LepGood'$i'_mass/LepGood_mass['$(( $i - 1 ))']/g' $1
	
	sed -i 's/Jet'$i'_pt/Jet_pt['$(( $i - 1 ))']/g' $1
	sed -i 's/Jet'$i'_eta/Jet_eta['$(( $i - 1 ))']/g' $1
done

sed -i 's/met/met_pt/g' $1

