# Arrey
# names=("Wale" "Mary" "John")
# echo ${names[2]}
# echo ${names[-1]}
# echo ${names[@]}
# echo ${names[@]:1:2}

# Case
# arrugument more like a parameter
choice=$1
case $choice in 
    start)
    echo "starting...";;
    stop)
    echo "stopping...";;
    restart)
    echo "restarting...";;
    *)
    echo "Invalid Choice";;
esac

if [ -f "Wale.txt"  ]; then
echo "file alread exit"
else
touch wale.txt
echo "File Created Successfully"
fi

if [ -d "Tech365"  ]; then
echo "file alread exit"
else
mkdir Tech365
echo "File Created Successfully"
fi
