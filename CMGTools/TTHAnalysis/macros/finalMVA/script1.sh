ch=2lss

for arg in ttW ttbar mix ttW_mm ttbar_mm mix_mm ttW_me ttbar_me mix_me ttW_ee ttbar_ee mix_ee
do
	root -l -q $ch/'trainMVA_'$ch'_6VAR.cxx("'$arg'")'
	mkdir -p output1/$ch/$arg
	mv $arg.root weights output1/$ch/$arg
done

