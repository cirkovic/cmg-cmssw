ch=2lss

for NVAR in 6VAR #7VAR 9VAR
do
	for arg in ttbar ttW mix
	do
		root -l -q $ch/'trainMVA_'$ch'_'$NVAR'.cxx("'$arg'")'
		mkdir -p $ch/output/$NVAR/$arg
		mv $arg.root weights $ch/output/$NVAR/$arg
	done
done

