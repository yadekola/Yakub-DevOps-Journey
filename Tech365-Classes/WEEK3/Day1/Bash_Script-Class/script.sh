# #!/bin/bash

# echo "hello"

# age=18
# echo "Your age is $age. You are no longer underage boy"

# echo "Enter your username: "
# read username
# echo "Welcome $username to are new opportunity to be great in Life"

# # -p mean to prompt or request 
# read -p "Enter your name: " name
# echo "Welcome $name for the great event of startup of growing your business"

# # -s mean security
# read -s -p "Enter your password: " password
# echo "Successfull"

# # if statement 
# read -p "Enter your age: " age
# if [ $age -ge 18 ]; then
# echo "You can vote"
# else
# echo "Not eligible"
# fi

# read -p "Enter your age: " age
# if [ $age -le 18 ]; then
# echo "You can vote"
# else
# echo "Not eligible"
# fi

# # From using the signs <, >, >=, <=, == we have to you to bracke (())
# read -p "Enter your age: " age
# if (($age > 17))
# then
# echo "You can vote"
# else
# echo "Not eligible"
# fi


# # loop
# for i in 1 2 3 4 5; do
# echo "$i"
# done

# for i in {2..10..2}; do
# echo "$i"
# done

# # while loop
# num=1
# while [ $num -le 5 ]; do
# echo "$num"
# (( num++ ))
# done

# num=1
# while (( $num < 6 )); do
# echo "$num"
# (( num++ ))
# done

# # Function in Bash scripting
# add(){
#     echo $(( $1 + $2 ))
# }

add(){
    result=$(( $1 + $2 ))
    echo "$result: $result"
    # echo $(( $1 + $2 ))
}

# add $1 $2

# sub(){
#     echo $(( $1 - $2 ))
# }

# sub $1 $2

# mult(){
#     echo $(( $1 * $2 ))
# }

# mult $1 $2

# divid(){
#     echo $(( $1 / $2 ))
# }

# divid $1 $2