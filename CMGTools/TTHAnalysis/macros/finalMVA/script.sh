ch=2lss

for arg in ttW ttbar
do
	root -l -q $ch/'trainMVA_'$ch'.cxx("'$arg'")'
	mkdir -p output/$ch/$arg
	mv $arg.root weights output/$ch/$arg
done

