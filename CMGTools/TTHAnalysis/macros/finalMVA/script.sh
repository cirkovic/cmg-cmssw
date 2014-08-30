ch=2lss

for NVAR in 7VAR 9VAR
do
	for arg in ttW ttbar mix
	do
		root -l -q $ch/'trainMVA_'$ch'_'$NVAR'.cxx("'$arg'")'
		mkdir -p output/$ch/$NVAR/$arg
		mv $arg.root weights output/$ch/$NVAR/$arg
	done
done

