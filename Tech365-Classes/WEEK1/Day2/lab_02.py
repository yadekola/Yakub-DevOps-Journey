# Create a dictionary called `devops_engineer` containing:

# - name
# - age
# - role
# - experience
# - city
# - email

devops_engineer = {
    "name": "Yakub Adekola Ojo",
    "age": 20,
    "role": "DevOps Engineer",
    "experience": "beginner",
    "city": "Lagos State",
    "email": "yakubadekolaojo059@gmail.com"
}

# Then:

# 1. Print the name.
print(devops_engineer["name"])
# 2. Print the role.
print(devops_engineer["role"])
# 3. Add a GitHub username.
devops_engineer.update({"GitHub": "yadekola"})
print(devops_engineer)
# 4. Change the city.
devops_engineer.update({"city": "Kwara State"})
print(devops_engineer)
# 5. Change the experience.
devops_engineer.update({"experience": "Intermediate"})
print(devops_engineer)
# 6. Remove the age.
devops_engineer.pop("age")
print(devops_engineer)
# 7. Print all keys.
print(devops_engineer.keys())
# 8. Print all values.
print(devops_engineer.values())
# 9. Print all key-value pairs.
print(devops_engineer.items())


# 2. List of Dictionaries

# A list can contain multiple dictionaries.

# ```python
# staff = [
#     {"name": "Wale", "gender": "male"},
#     {"name": "Mary", "gender": "female"},
#     {"name": "John", "gender": "male"}
# ]

# print(staff[0]["name"])
# print(staff[1]["gender"])
# print(staff[2]["name"])


### Real-world idea

["Joy", "Ade", "Mary", "John"]
# This structure can represent employees, customers, servers, applications, users, or cloud resources.


Tech365 = [
     {
        "Employees_data" :[
            {
            "userID": 63729754,
            "name": "Mr Wale",
            "role": "DebOps_Engineer",
            "city": "Lagos State",
            "experience": "master",
            "DevOps_Tools": ["Docker", "Kubernetes", "Jenkins", "Ansible", "Terraform", "Git", "Prometheus", "Grafana", "Nagios", "ELK Stack"]
            },
            {
            "userID": 63729754,
            "name": "Mr Larry",
            "role": "Backend_Developer",
            "city": "Lagos State",
            "experience": "master",
            "Backend_Tools": ["Node.js", "Django", "Flask", "Ruby on Rails", "Spring Boot", "Express.js", "Laravel", "ASP.NET", "Phoenix", "Koa"]
            },
            {
            "userID": 63729754,
            "name": "Mr John",
            "role": "Front_end Developer",
            "city": "Lagos State",
            "experience": "master",
            "Front_end_tools": ["React","Angular", "Vue.js", "Bootstrap", "jQuery", "Sass", "Less", "Tailwind CSS", "Material-UI", "Foundation"]
            },
            {
            "userID": 63729754,
            "name": "Mr Sulaimen",
            "role": "Data_Science",
            "city": "Lagos State",
            "experience": "master",
            "Data_Science_Tools": ["Python", "R", "SQL", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Matplotlib", "Scikit-learn", "Jupyter Notebook"]
            },
            {
            "userID": 63729754,
            "name": "Mrs Mary",
            "role": "Ui_Ux_Design",
            "city": "Lagos State",
            "experience": "master",
            "Ui_Ux_Tools": ["Adobe XD", "Sketch", "Figma", "InVision", "Axure RP", "Marvel", "Balsamiq", "Proto.io", "Framer", "Zeplin"]
            }   
        ],
        "Student_data": [
            {
                "userId": 38942872,
                "name": "Mr Debe",
                "role_enroll": "DevOps_coures"
                "addrees": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                }
            },
            {
                "userId": 38942872,
                "name": "Mr Ibrahim",
                "role_enroll": "DevOps_coures"
                "addrees": {
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
    }
]






# {
#         "Front_end_Tutor":["Ade","John"{
#             "Front_end_tools"= ]
#         }]
#     } 
