#for i in `ls ttbar_*/STDOUT.txt`; do echo $i; grep -A 29 "Ranking result (top variable is best ranked)" $i; echo; done > prompt.txt
#for i in `ls ttbar_*/STDOUT.txt`; do echo $i; grep -A 28 "Variable Importance" $i; echo; echo; echo; echo; echo; done > prompt.txt
for i in `ls ttbar_*/STDOUT.txt`; do echo $i; grep -A 8 "Variable Importance" $i; echo; done > prompt.txt
#for i in `ls ttbar_*/STDOUT.txt`; do echo $i; tail $i; echo; done > prompt.txt
