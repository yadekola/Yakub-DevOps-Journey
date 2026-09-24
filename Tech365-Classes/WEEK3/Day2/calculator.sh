#!/bin/bash

# Addition function
add() {
    result=$(($1 + $2))
    echo "Result: $result"
}

# Subtraction function
subtract() {
    result=$(($1 - $2))
    echo "Result: $result"
}

# Multiplication function
multiply() {
    result=$(($1 * $2))
    echo "Result: $result"
}

# Division function
divide() {
    if [ "$2" -eq 0 ]; then
        echo "Error: Cannot divide by zero."
    else
        result=$(($1 / $2))
        echo "Result: $result"
    fi
}

# Modulus function
modulus() {
    if [ "$2" -eq 0 ]; then
        echo "Error: Cannot calculate modulus by zero."
    else
        result=$(($1 % $2))
        echo "Result: $result"
    fi
}


echo "======================"
echo "   SIMPLE CALCULATOR"
echo "======================"

read -p "Enter first number: " num1
read -p "Enter second number: " num2

echo
echo "Select operation:"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "5. Modulus"

read -p "Enter your choice [1-5]: " choice

case $choice in
    1)
        add $num1 $num2
        ;;
    2)
        subtract $num1 $num2
        ;;
    3)
        multiply $num1 $num2
        ;;
    4)
        divide $num1 $num2
        ;;
    5)
        modulus $num1 $num2
        ;;
    *)
        echo "Invalid choice."
        ;;
esac