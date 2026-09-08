# Tech365 DevOps & Python Practice Workbook

## Purpose

This workbook contains the Python topics covered in today's Tech365 class, organized into practical notes and hands-on exercises.

The goal is to learn by doing: understand the concept, write code, run it, debug errors, and connect the exercise to a real DevOps scenario.

---

# PART 1 — PYTHON DATA STRUCTURES

## 1. Dictionary

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Wale",
    "age": 20,
    "gender": "Male"
}

print(student["name"])
print(student["age"])
print(student["gender"])
```

### Important dictionary methods

```python
print(student.keys())
print(student.get("gender"))
print(student.items())
print(student.values())

student.pop("age")
student.update({"age": 21})
student.update({"email": "wale@example.com"})
student.popitem()
```

### Practice

Create a dictionary called `devops_engineer` containing:

- name
- age
- role
- experience
- city
- email

Then:

1. Print the name.
2. Print the role.
3. Add a GitHub username.
4. Change the city.
5. Change the experience.
6. Remove the age.
7. Print all keys.
8. Print all values.
9. Print all key-value pairs.

---

# 2. List of Dictionaries

A list can contain multiple dictionaries.

```python
staff = [
    {"name": "Wale", "gender": "male"},
    {"name": "Mary", "gender": "female"},
    {"name": "John", "gender": "male"}
]

print(staff[0]["name"])
print(staff[1]["gender"])
print(staff[2]["name"])
```

### Real-world idea

This structure can represent employees, customers, servers, applications, users, or cloud resources.

---

# 3. Nested Dictionaries

A dictionary can contain another dictionary.

```python
address = {
    "name": "Wale",
    "age": 20,
    "location": {
        "city": "Lagos",
        "state": "Lagos State",
        "zip": [20001, 20002, 20003]
    }
}

print(address["location"]["city"])
print(address["location"]["zip"][1])
```

Think about nested access from outside to inside:

```text
dictionary
   ↓
location
   ↓
zip
   ↓
index
```

---

# 4. Deeply Nested Data

```python
record = {
    "k1": [
        {
            "nest_key": [
                "this is deep",
                ["tech365"]
            ]
        }
    ]
}

print(record["k1"])
print(record["k1"][0]["nest_key"])
print(record["k1"][0]["nest_key"][0])
print(record["k1"][0]["nest_key"][1])
print(record["k1"][0]["nest_key"][1][0])
```

This is useful practice because real APIs often return deeply nested JSON data.

---

# 5. Working With API-Like Data

Example:

```python
result = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae"
    }
]

print(result[0]["title"])
print(result[1]["title"])
print(result[0]["body"])
```

### DevOps connection

APIs, monitoring systems, cloud services, and automation tools frequently return structured JSON data.

You need to be comfortable navigating dictionaries and lists to extract the information you need.

---

# 6. Deep API Data

```python
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

print(data[0]["address"]["geo"]["lng"])
```

---

# PART 2 — SETS

## 7. What is a Set?

A set is an unordered collection of unique values.

Duplicates are automatically removed.

```python
data = {1, 1, 1, 2, 2, 3, 3, 4}

print(data)
```

Expected:

```text
{1, 2, 3, 4}
```

Sets are useful when uniqueness matters.

---

## 8. Set Operations

```python
x = {1, 2, 3}
y = {3, 4, 5}

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))
print(x.isdisjoint(y))
print(x.issubset(y))
```

### Set modification

```python
x.add(6)
x.add(3)
x.update([7, 8, 9])
x.remove(2)
x.discard(10)
y.clear()
```

### Important difference

`remove()` raises an error if the value does not exist.

`discard()` does not raise an error if the value does not exist.

---

# PART 3 — TUPLES

## 9. Tuple

A tuple is an ordered, immutable collection.

```python
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

print(months[0])
print(months[1])
print(months[-1])
```

Convert a tuple to a list:

```python
months_list = list(months)
print(months_list)
```

### Key idea

List:

```text
Mutable → can be changed
```

Tuple:

```text
Immutable → cannot be changed directly
```

---

# PART 4 — PYTHON OPERATORS

## 10. Arithmetic Operators

```python
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 % 3)
print(5 ** 3)
print(100 // 3)
```

Operators:

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
%    Modulus
**   Exponentiation
//   Floor division
```

---

# 11. Comparison Operators

```python
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)
print(5 == 3)
print(5 != 3)
```

Comparison expressions return:

```text
True
False
```

---

# 12. Logical Operators

```python
print(True and False)
print(True or False)
print(not True)

print(5 > 3 and 5 < 10)
print(5 > 3 or 2 > 3)
print(not (3 > 7))
```

Operators:

```text
and
or
not
```

---

# 13. Assignment Operators

```python
x = 5
y = 2

x += y
x -= y
x *= y
x /= y
x %= y
x **= y
x //= y
```

These are shortcuts for operations such as:

```python
x += y
```

which means:

```python
x = x + y
```

---

# PART 5 — CONTROL FLOW

## 14. if / else

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote.")
else:
    print("Not eligible to vote.")
```

---

# 15. if / elif / else

```python
color = input("Enter your favorite color: ")

if color == "red":
    print("Your favorite color is red.")
elif color == "blue":
    print("Your favorite color is blue.")
else:
    print("Your favorite color is not red or blue.")
```

---

# 16. While Loop

A while loop repeats while a condition remains true.

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

Even numbers:

```python
z = 2

while z <= 10:
    print(z)
    z += 2
```

---

# 17. For Loop

A for loop iterates through a sequence.

```python
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    print(n)
```

Using range:

```python
for i in range(1, 11):
    print(i)
```

Odd numbers:

```python
print(list(range(1, 11, 2)))
```

---

# PART 6 — DEBUGGING

## 18. Nested Conditions

Study this carefully:

```python
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
```

Question:

What will this program print?

Explain why.

---

# PART 7 — REAL-LIFE DEVOPS PROJECT PRACTICE

## Project: Cloud Infrastructure Inventory System

You are a junior DevOps engineer working for a company called CloudNova.

The company wants a simple Python program to keep track of its infrastructure.

Start with:

```python
servers = [
    {
        "name": "web-server-01",
        "environment": "production",
        "os": "Linux",
        "ip": "10.0.1.10",
        "status": "running"
    },
    {
        "name": "web-server-02",
        "environment": "staging",
        "os": "Linux",
        "ip": "10.0.1.11",
        "status": "running"
    },
    {
        "name": "database-01",
        "environment": "production",
        "os": "Linux",
        "ip": "10.0.2.10",
        "status": "stopped"
    }
]
```

### Your tasks

### Task 1
Print the name of the first server.

### Task 2
Print the IP address of the database server.

### Task 3
Print the status of `web-server-02`.

### Task 4
Change the database server status from:

```text
stopped
```

to:

```text
running
```

### Task 5
Add a new server.

The server should contain:

```text
name
environment
os
ip
status
```

### Task 6
Print the total number of servers.

### Task 7
Create a set containing the operating systems used by all servers.

### Task 8
Create a list containing all server names.

### Task 9
Use a loop to print:

```text
Server: web-server-01 | Status: running
```

for every server.

### Task 10
Use an `if` statement to print:

```text
web-server-01 is healthy
```

if its status is `"running"`.

---

# PART 8 — HARDER REAL-LIFE CHALLENGE

Create:

```python
deployments = [
    {
        "application": "frontend",
        "environment": "production",
        "version": "v1.2.0",
        "status": "success"
    },
    {
        "application": "backend",
        "environment": "production",
        "version": "v2.1.0",
        "status": "failed"
    },
    {
        "application": "payment-api",
        "environment": "staging",
        "version": "v1.5.2",
        "status": "success"
    }
]
```

Write a program that:

1. Prints every application.
2. Prints every version.
3. Counts the number of successful deployments.
4. Counts the number of failed deployments.
5. Prints only failed deployments.
6. Prints only production deployments.
7. Changes the backend deployment status from `failed` to `success`.
8. Prints the updated backend record.
9. Creates a set containing all environments.
10. Prints the total number of deployments.

---

# PART 9 — INTERVIEW-STYLE QUESTIONS

Answer these in your own words.

1. What is a dictionary?
2. What is the difference between a list and a dictionary?
3. What is a nested dictionary?
4. Why are dictionaries useful when working with API responses?
5. What is a set?
6. Why does a set remove duplicates?
7. What is the difference between `remove()` and `discard()`?
8. What is a tuple?
9. What is the difference between a list and tuple?
10. What is the difference between `==` and `=`?
11. What is the difference between `and` and `or`?
12. What is an `if` statement?
13. What is a loop?
14. What is the difference between `while` and `for`?
15. Why is control flow important in automation?

---

# PART 10 — DEVOPS CONNECTION

For each concept, think about a real DevOps use case:

```text
Dictionary      → API responses / configuration data
List            → servers / containers / packages
Set             → unique IPs / unique environments
Tuple           → fixed configuration values
Operators       → calculations / comparisons
if statements   → deployment decisions
while loops     → repeated checks
for loops       → processing servers/resources
```

The objective is not just to memorize Python syntax.

The goal is to eventually write automation such as:

```text
Read infrastructure data
        ↓
Check server status
        ↓
Identify failed servers
        ↓
Make a decision
        ↓
Take an automated action
        ↓
Report the result
```

---

# FINAL PROJECT CHALLENGE

Do not use the solution from this workbook.

Build a Python program called:

```text
devops_inventory.py
```

It should manage:

- Servers
- Applications
- Environments
- Deployment status

Your program must use:

- Variables
- Lists
- Dictionaries
- Nested dictionaries
- Sets
- Tuples
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- `if / elif / else`
- `for` loops
- `while` loops

### Rule

Do not worry if your first attempt fails.

Run it.

Read the error.

Try to understand it.

Fix it.

Run it again.

That debugging cycle is part of the learning.

---

## Progression

We can build from this foundation into:

```text
Python Basics
      ↓
Functions
      ↓
Modules
      ↓
File Handling
      ↓
Exception Handling
      ↓
JSON
      ↓
APIs
      ↓
Python Automation
      ↓
Linux Automation
      ↓
AWS Automation
      ↓
CI/CD
      ↓
Real DevOps Projects
```
