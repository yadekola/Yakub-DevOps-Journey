# Assignment
# 1. record = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}



record = {
    'k1':
    [1,2,
        {'k2':
            ['this is tricky',{
                    'tough':[1,2,
                      ['python']]
                }
            ]
        }
    ]
}

# # print out python from the record above

# print(record['k1'][2]["k2"][1]["tough"][2][0])

# 2. data = [
#   {
#     "id": 1,
#     "name": "Leanne Graham",
#     "username": "Bret",
#     "email": "Sincere@april.biz",
#     "address": {
#       "street": "Kulas Light",
#       "suite": "Apt. 556",
#       "city": "Gwenborough",
#       "zipcode": "92998-3874",
#       "geo": {
#         "lat": "-37.3159",
#         "lng": "81.1496"
#       }
#     }
#   }
# ]



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

# # print put 81.1496 from the data above
print(data[0]["address"]["geo"]["lng"])

# 3. create a program that takes a score and shows the grade based on the score

# eg.

# 90 - 100 ("Grade A")
# 70 - 89 ("Grade B")
# 50 - 69 ("Grade c")
# 30 - 49 ("Grade D")
# 0 - 29 ("Grade F")

grade_score = int(input("Enter your score to know your grade: "))

if 90 <= grade_score <= 100:
    print("Grade A")
elif 70 <= grade_score <= 89:
    print("Grade B")
elif 50 <= grade_score <= 69:
    print("Grade C")
elif 30 <= grade_score <= 49:
    print("Grade D")
elif 0 <= grade_score <= 29:
    print("Grade F" )
else:
    print("Invalid score")


if grade_score >= 90 and grade_score <= 100:
    print("grand A")
elif grade_score >= 70 and grade_score <= 90:
    print("grant B")
elif grade_score >= 50 and grade_score <= 70:
    print("grant C")
elif grade_score >= 30 and grade_score <= 50:
    print("grant D")
elif grade_score >= 0 and gr

# 4. record = "this is the time to attend python training"

record = "this is the time to attend python training"

 # bring out the words that start from 't'

for i in record.split():
    if i.startswith("t"):
        print(i)



# 5. words = 'Python is not hard. Do you agree'



words = 'Python is not hard. Do you agree'


# Print every word in this sentence above that has an even number of letters
for x in words.split():
    if len(x) % 2 == 0:
        print(x)


print(len(words))

print(words.split())
# print(len(words) % 2 == 0)
# print(words)