CURRDIR=`pwd`
for sample in ttbar
do
#    for i in 23j 4j 5j 6j 7j 8Lj
#    do
#       CASE=${sample}_${i}
#       mkdir $CASE
#       cd $CASE
#       COMMAND='root -l -b -q '"'"'../trainMVA_2lss.cxx("'$CASE'")'"'"' 2>&1 | tee STDOUT.txt &'
#       eval $COMMAND
#       cd $CURRDIR
#    done
    for i in 23j_6var 23j_9var 4j_6var 4j_10var 4j_15var
    do
       CASE=${sample}_${i}
       mkdir $CASE
       cd $CASE
       COMMAND='root -l -b -q '"'"'../trainMVA_2lss_default.cxx("'$CASE'")'"'"' 2>&1 | tee STDOUT.txt &'
       eval $COMMAND
       cd $CURRDIR
    done
done

