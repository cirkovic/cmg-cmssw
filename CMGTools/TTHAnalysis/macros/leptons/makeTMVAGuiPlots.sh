case_i=1

ls_command='ls /afs/cern.ch/work/c/cirkovic/Milos_13-08-2014/27-08-2014/'${case_i}'/*.root'

n=0
for i in `$ls_command`
do
	n=$(( $n + 1 ))
	./checkTMVAGui.sh $i
	mv plots plots_all_${case_i}/plots_$n
done

