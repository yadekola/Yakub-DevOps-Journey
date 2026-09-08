# Dictionary data structure to store user information
# Dictionary keys represent user IDs, and values are dictionaries containing user details
# Dictionary data type: {user_id: {name: str, email: str, age: int}}

# (variable) student: dict[str, Any]
student = {"name": "Wale", "age": 20, "gender": "Male"}

# indexing the dictionary to access values
print(student["name"])  # Output: Wale
print(student["age"])   # Output: 20
print(student["gender"])  # Output: Male

#dictionary methods
print(student.keys())    # Output: dict_keys(['name', 'age', 'gender
print(student.get("gender"))  # Output: Male
print(student.items())   # Output: dict_items([('name', 'Wale'), ('age', 20), ('gender', 'Male')])
print(student.values())  # Output: dict_values(['Wale', 20, 'Male'])

student.pop("age")  # Removes the 'age' key-value pair from the dictionary
print(student)  # Output: {'name': 'Wale', 'gender': 'Male'}

student.update({"age": 21})  # Updates the 'age' key with a new value
print(student)  # Output: {'name': 'Wale', 'gender': 'Male', 'age': 21}

student.update({"email": "wale@example.com"})  # Adds a new key-value pair for 'email' to the dictionary
print(student)  # Output: {'name': 'Wale', 'gender': 'Male', 'age': 21, 'email': 'wale@example.com'}

student.update({"age": 22, "gender": "Female", "State": "Lagos"})  # Updates the 'age' and 'gender' keys with new values and adds a new key-value pair for 'State'
print(student)  # Output: {'name': 'Wale', 'gender': 'Female', 'age': 22, 'email': 'wale@example.com', 'State': 'Lagos'}

student.update({"name": "Mary"})  # Updates the 'name' key with a new value
print(student)  # Output: {'name': 'Mary', 'gender': 'Male', 'age': 21, 'email': 'wale@example.com'}

student.popitem()  # Removes the last inserted key-value pair from the dictionary
print(student)  # Output: {'name': 'Mary', 'gender': 'Male', 'age': 21}



staff=[

    {"name": "Wale", "gender": "male"},
    {"name": "Mary", "gender": "female"},
    {"name": "John", "gender": "male"}
]

print(staff[0]["name"])  # Output: Wale
print(staff[1]["gender"])  # Output: female
print(staff[2]["name"])  # Output: John

# Nested dictionary
# What is a nested dictionary?
# A nested dictionary is a dictionary that contains another dictionary as a value for one of its keys

address = {
    "name": "Wale",
    "age": 20,
    "location": {
        "city": "Lagos",
        "state": "Lagos State",
        "zip": [20001, 20002, 20003]
    }
}

print(address["location"]["city"])  # Output: Lagos
print(address["location"]["zip"][1])  # Output: 20002
print(address["location"]["zip"][2])  # Output: 20003

record = {'k1': [{'nest_key': ['this is deep', ['tech365']]}]}
print(record["k1"])
print(record['k1'][0]['nest_key'])  # Output: ['this is deep', ['tech365']]
print(record['k1'][0]['nest_key'][0])  # Output: this is deep
print(record['k1'][0]['nest_key'][1])  # Output: ['tech365']
print(record['k1'][0]['nest_key'][1][0])  # Output: tech365


result = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
]

print(result[0]["title"])  # Output: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
print(result[1]["title"])  # Output: qui est esse
print(result[0]["body"])  # Output: quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto   


data = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
  }
]

print(data[0]["address"]["geo"]["lng"])  # Output: 81.1496


# What is a dictionary comprehension?
# A dictionary comprehension is a concise way to create dictionaries in Python. It allows you to generate a new dictionary by applying an expression to each item in an iterable, such as a list or another dictionary. 


# Set date structure to store unique values
# Set data type: {value1, value2, value3, ...}
# Sets are unordered collections of unique elements, meaning they do not allow duplicate values. They are useful for storing and manipulating data where uniqueness is important.   
# what is a set in python?
# A set is a built-in data structure in Python that represents an unordered collection of unique elements
# Sets are mutable, meaning you can add or remove elements from a set after it has been created. However, sets do not support indexing or slicing like lists or tuples, and they do not maintain the order of elements. 

data = {1,1,1,1,2,2,2,3,3,3,4,4,4}
print(data)  # Output: {1, 2, 3, 4} - duplicates are removed

x = {1, 2, 3}
y = {3, 4, 5}

print(x.union(y))  # Output: {1, 2, 3, 4, 5} - union of two sets
print(x.intersection(y))  # Output: {3} - intersection of two sets
print(x.difference(y))  # Output: {1, 2} - difference of two sets
print(x.symmetric_difference(y))  # Output: {1, 2, 4, 5} - symmetric difference of two sets
print(x.isdisjoint(y))  # Output: False - checks if two sets have no elements in common
print(x.issubset(y))  # Output: False - checks if x is a subset of y

x.add(6)  # Adds an element to the set
print(x)  # Output: {1, 2, 3, 6}

x.add(3)  # Adding an existing element does not change the set
print(x)  # Output: {1, 2, 3, 6}

x.update([7, 8, 9])  # Adds multiple elements to the set
print(x)  # Output: {1, 2, 3, 6, 7, 8, 9}

x.remove(2)  # Removes an element from the set
print(x)  # Output: {1, 3, 6, 7,

x.discard(10)  # Removes an element from the set if it exists, does nothing if it doesn't
print(x)  # Output: {1, 3, 6, 7,

y.clear()  # Removes all elements from the set
print(y)  # Output: set() - an empty set



# Tuple immulable data structure to store ordered values
# Tuple data type: (value1, value2, value3, ...)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months[0])  # Output: January
print(months[1])  # Output: February
print(months[-1])  # Output: December

months_list = list(months)  # Convert tuple to list
print(months_list)  # Output: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# months_list.append("New Month")  # Add a new month to the list


age = 18
salary = 500.1234567

# Operators in Python
# Arithmetic operators: +, -, *, /, %, **, //

print(5+3)  # Output: 8
print(5-3)  # Output: 2
print(5*3)  # Output: 15
print(5/3)  # Output: 1.6666666666666667
print(5%3)  # Output: 2 modulus operator returns the remainder of the division
print(10%3)  # Output: 1
print(5**3)  # Output: 125 
print(100//3)  # Output: 33 Floor division operator returns the largest integer less than or equal to the division result
print(5//3)  # Output: 1 Floor division operator returns the largest integer less than or equal to the division result

# Comparison operators: ==, !=, >, <, >=, <=
print(5 > 3)  # Output: True
print(5 < 3)  # Output: False
print(5 >= 3)  # Output: True >= operator returns True if the left operand is greater than or equal to the right operand, otherwise it returns False
print(5 <= 3)  # Output: False 
print(5 == 3)  # Output: False == operator returns True if the left operand is equal to the right operand, otherwise it returns False
print(5 != 3)  # Output: True != operator returns True if the left operand is not equal to the right operand, otherwise it returns False

# Logical operators: and, or, not
print(True and False)  # Output: False
print(True or False)  # Output: True
print(not True)  # Output: False

5 > 3 and 5 < 10  # Output: True And operator returns True if both conditions are True, otherwise it returns False
5 > 3 or 2 > 3  # Output: True Or operator returns True if at least one condition is True, otherwise it returns False
print(not(3 > 7))  # Output: True Not operator returns True if the condition is False, otherwise it returns False

# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=

x = 5
y = 2
x += y  # x = x + y
print(x)  # Output: 7

x -= y  # x = x - y
print(x)  # Output: 5

x *= y  # x = x * y
print(x)  # Output: 10

x /= y  # x = x / y
print(x)  # Output: 5.0

x %= y  # x = x % y
print(x)  # Output: 1.0

x **= y  # x = x ** y
print(x)  # Output: 1.0

x //= y  # x = x // y
print(x)  # Output: 0.0



# Control flow statements in Python
# Control flow statements are used to control the flow of execution in a program based on certain conditions





# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote.")
# else:
#     print("Not eligible to vote.")






# age = input("Enter your age: ")
# age = int(age)
# if age >= 18:
#     print("You can vote.")
# else:
#     print("Not eligible to vote.")





# color = "red"

# if color == "red":
#     print("Your favorite color is red.")
# elif color == "green":
#     print("Your favorite color is green.")
# elif color == "blue":
#     print("Your favorite color is blue.")
# else:
#     print("Your favorite color is not invalid color.")





# color = input("Enter your favorite color: ")
# if color == "red":
#     print("Your favorite color is red.")
# elif color == "blue":
#     print("Your favorite color is blue.")
# else:
#     print("Your favorite color is not red or blue.")


# While loop in Python
# A while loop is used to execute a block of code repeatedly as long as a given condition is true. The loop will continue to run until the condition becomes false.
# initial value, condition, action, increment/decrement


# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# y = 2
# while y <= 50:
#     print(y)
#     y += 2


# 2468 10 in while loop
# z = 2
# while z <= 10:
#     print(z)
#     z += 2


#for loop in Python
# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The loop will continue until all items in the sequence have been processed.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in numbers:
#     print(n)

# print(type(numbers))  # Output: <class 'list'>


# print(list(range(1, 11, 2)))  # Output: [1, 3, 5, 7, 9]
# print(list(range(1, 11)))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# for i in range(1, 11):
#     print(i)



x = 3

if x >= 5:
    if x <= 5:
        print("A")
    else:
        print("B")
elif x == 5:
    print("C")
else:
    print("D")