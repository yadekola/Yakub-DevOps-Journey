students = [
  { "name": "Wale", "grade": 10 },
  { "name": "Mary", "grade": 15 },
  { "name": "John", "grade": 19 },
  { "name": "Audu", "grade": 9 },
]

# for i in students:
#     # print(i)
#     if i["grade"] < 10:
#         print(i["name"])



# functions

def add_it():
    print(2 + 2)

add_it()


# finction parameter
def add_it(x,y):
    print(x + y)

add_it(2,3)
add_it(2,5)
add_it(4,5)
add_it(9,9)



# def add(x)
#     return(x x x)


def welcome(username="guest"):
    return "Welcome " + username

print(welcome ("Wale"))

# I want to use input to a user to add they name and use function


import calculator as calculator
calculator.div_it(20,5)


from calculator import *
add_it(4,6)

# from Data.signup import *

# username()


#inbuiot modules

# import math
# import os

# print(math.cos(90))
# os.rmdir("Tech365")
# os.mkdir("Tech365")
# print(os.getcwd())
# os.chdir("Day1")
# os.mkdir("Tech365")
# print(os.getcwd())

# To work with files

myfile = open("wale.txt", "w")
myfile.write("Life is not hard")
myfile.close()


myfile = open("wale.txt", "a")
myfile.write(" DevOps Training")
myfile.close()



myfile = open("wale.txt", "a")
myfile.write("\nDevOps Training")
myfile.close()




myfile = open("wale.txt", "r")
print(myfile.read())



