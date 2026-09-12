#!/bin/bash
echo "Welcome to bash"
name="Wela"
age=18
role="DevOps"

echo "Welcome $name, I live in Lagos State. "

echo "enter your name: "
read 

read -p "Enter your age : age
echo "your age is $age"

read -s -p "Enter your passwork: password

age=17
if[ $age -ge 18 ]; then
echo "you can vote"
else
echo "Not eligible"
fi

if (( age > 17 ));then
echo "you can vote"
else
echo "Not eligible"
fi

for i in 1 2 3 4 5
do
echo $i
done

for i in {1..10..2}
do
echo $i
done

count=1
while (( count < 6 ))
do
echo $count
(( count++ ))

option=$1

case $option in 
    start)
        echo"Starting...";;
    stop)
        echo"Starting...";;
    restart)
        echo"Starting...";;
esac

echo "Run the script with 2 argument eg. bash script 5 6"
add(){
    sun=$(( $1 + $2 ))
    echo "Sun is : $sun"
}
add $1 $2

name=("Wale", "Mary", "John")
echo ${name[@]}
echo ${#name[@]}
name [3]="Peter"
echo ${name[@]}

echo ${name[1]}
echo ${name[@]:1:2}

file="wale.txt"
if [ -f "$file" ]; then
echo "file already exist"
else
touch wale.txt
fi