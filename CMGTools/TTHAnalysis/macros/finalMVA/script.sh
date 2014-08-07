cd 2lss
echo "EXE 2lss"

opt=ttbar; mkdir ${opt}_output; root -l -q 'script.C("'${opt}'")'; mv *.root weights ${opt}_output;

cd ..
