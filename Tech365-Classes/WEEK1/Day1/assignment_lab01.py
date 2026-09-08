# String
data="1:A, 2:B, 3:C, 4:D, 5:E"
print(type(data)) # Know the type of data fiest
print(len(data)) # Know all the numbers in total
print(data[0])  # Print out only 1
print(data[5])  # Print out only 2
print(data[10]) # Print out only 3
print(data[15]) # Print out only 4
print(data[20]) # Print out only 5
print(data[:25:5]) # Print out the total number requiest 12345



#2
student_score=[1,2,3,[4,5,[6,7]]]
print(type(student_score))
print(len(student_score))
student_score[3][2][1]= 8
print(student_score)

# #3
words="I am here"
print(type(words))
# print(len(words.split()[::-1]))
print(list(reversed(words.split())))
print(" ".join(list(reversed(words.split()))))
# print(words[0])
# print(words)

# print(words.())


# #4
num='123456789'
print(type(num))
print(len(num))
print(num[-1])
print(num[-2])
print(num[-3])
print(num[-4])
print(num[-5])
print(num[-6])
print(num[-7])
print(num[-8])
print(num[-1:-9:-1])

#5
# 1. Collaburation
# 2. Fast Delivery And Integration
# 3. Reduce Human Error
# 4. Availability Of Scale Up OR Scaled Down
# 5  Uses Of Automation Tools



# 6.

tools=["Git","Linux", "Docker", "Jenkins"]
print(len(tools))
tools.append("Kubernetes")
tools.append("AWS")
print(tools)

# 8.
tools.remove("Linux")
print(tools)

9
tools.insert(2, "GitHub Actions")
tools.remove("Jenkins")
print(tools)

# 10
print(len(tools))
print(tools[0:4:2])