#!/bin/sh

if [ -z "$2" ]
	then name=evVarFriend
	else name=$2
fi

command='ls '$1'/'$name'_*.chunk0.root'

for file in `$command`
do
  string_to_replace=".chunk0."
  string_to_replace_chunk0_with1="."
  string_to_replace_chunk0_with2=".chunk*."
  hadd -f ${file/$string_to_replace/$string_to_replace_chunk0_with1} ${file/$string_to_replace/$string_to_replace_chunk0_with2}
done

