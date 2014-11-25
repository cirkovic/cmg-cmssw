CURRDIR=`pwd`
for sample in ttbar
do
    for i in 23j 4j 5j 6j 7j 8Lj
    do
#       for ch in mm em ee
#       do
#           CASE=${sample}_${i}_${ch}
#           mkdir $CASE
#           cd $CASE
#           COMMAND='root -l -b -q '"'"'../trainMVA_2lss.cxx("'$CASE'")'"'"' 2>&1 | tee STDOUT.txt &'
#           eval $COMMAND
#           cd $CURRDIR
#       done
       CASE=${sample}_${i}
       mkdir $CASE
       cd $CASE
       COMMAND='root -l -b -q '"'"'../trainMVA_2lss.cxx("'$CASE'")'"'"' 2>&1 | tee STDOUT.txt &'
       eval $COMMAND
       cd $CURRDIR
    done
done

