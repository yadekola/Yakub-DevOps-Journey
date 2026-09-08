# To print the sum of 2 and 2, you can use the following code:
print(2+2)

print("Wale")

print("2 + 2")

# This is a comment by using # or ctrl + / to comment multiple lines

# Variables
first_name = "Wale"
age = 18
print(first_name, age)
print(age)
# print("I am " + str(age) + " year old" )
print("I am" , age , "year old" )

# Variables rules
# 2. Variable names cannot start with a number e.g 2 numbers.
# 2. Variable names cannot contain spaces eg. first name
# 3. Variable cannot contain special characters except underscore _ eg. !@#$%&^()
# 1. Variable names can only contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive.
# 4. Variable names cannot be the same as reserved keywords in Python.

# Data types
# 1. String
address = 'soji Adepegba close, ikeja, lagos state'
print(type(address))
print(len(address))

# indexing and slicing
print(address[3])
print(address[-1])



# slicing with step
print(address[0:5])
print(address[0:10:2])

number=(123456789)
print(type(number))

#string methods
# 1. upper()
print(address.upper())
# 2. lower()
print(address.lower())
# 3. capitalize()
print(address.capitalize())
# 4. title()
print(address.title())
# 5. count()
print(address.count("a"))
# 6. count() lowercase
print(address.lower().count("a"))
# 7. endswith()
print(address.endswith("e"))
# 8. startswith()
print(address.startswith("a"))
# 9. find()
print(address.find("Adepegba"))
# 10. index()
print(address.index("ikeja"))
# 11. replace()
print(address.replace("Adepegba", "Adepeju"))
# 12. split()
# print(address.split(""))
print(address.split(","))

# 13. strip()
username = "  Wale   "
print(username.strip())

# list data type
# 1. list
names = ["Wale", "John", "Mary", "Bola"]
print(type(names))
print(names[:2])

# list methods
# 1. pop()
names.pop()
print(names)
# 2. append()
names.append("Tolu")
print(names)
# 3. remove()
names.remove("John")
print(names)
# 4. insert()
names.insert(1, "John")
# print(names)
# 5. extend()
# names.extend(["address"])
# names.extend(["Tolu", "Bola"])
# print(names)
# # 6. sort()
# names.sort()
# print(names)
# # 7. reverse()
# names.reverse()
# print(names)



# 8. clear()

# backup = names.copy()
# print(backup)
# names.clear()
# print(names)


# 9. nested list
data = [[1,2,3], [4,5,6], [7,8,9]]
# print(data[3][1])

print(data.extend([10,11,12]))
