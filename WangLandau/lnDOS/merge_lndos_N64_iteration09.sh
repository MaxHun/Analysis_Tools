#!/bin/bash

#array=$(ls | grep -a 'final_HGLnDOS')
array=(data/N64_windows/*iteration09*HG*.dat)

echo $array
# get length of an array
arraylength=${#array[@]}


python3 OverlapAndAverage.py ${array[0]} ${array[1]} "out.dat"

for (( i=2; i<${arraylength}; i++ ));
do
  echo $i " / " ${arraylength} " : " ${array[$i]}
  winOne="out.dat" #${array[$i]}
  winTwo=${array[$i]}
  winOut="out.dat"
  
  python3 OverlapAndAverage.py $winOne $winTwo $winOut
  
done
echo "Die Schleife ist zu Ende"

name=${array[0]}".dat"
name=${name#data/N64_windows/}
name=${name%Solvent*}"HGLnDOS_iteration09.dat"
##mv out.dat $name

#datname="out.dat" ${array[0]%.bfm*}"_HGLnDOS_shifted.dat"
#echo $name
python3 ShiftToZero.py "out.dat" $name #${name:19}
#echo ${array[0]%.bfm*:19}"_HGLnDOS_shifted.dat"



#echo ${array[0]%.bfm*}"_HGLnDOS_shifted.dat"

