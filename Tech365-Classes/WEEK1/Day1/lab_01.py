first_name="Yakub"
last_name="Ojo"
age=20
city="Lagos"
role="DevOPs Engineer"
expreience='Beginner'

print(
    first_name,
    last_name,
    age,
    city,
    role,
    expreience
)

print(first_name)
print(last_name)
print(age)
print(city)
print(role)
print(expreience)


print(first_name.upper())
print(last_name.lower())
print(role.title())
print(first_name.replace("Yakub", "Adekola"))
print(expreience.split())



topic="One important lesson was understanding the difference between AWS infrastructure management and Linux system management"
print(topic.title())



print(list(reversed(topic.split())))

print(",".join(list(reversed(topic.split()))))