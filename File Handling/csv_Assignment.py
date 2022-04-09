import csv
import os

os.chdir(r"C:\Users\RASHMI\PycharmProjects\pythonWorkspace\Files\csv_files")

# 1.. WAP to read all the names of employees in employee.csv

# using reader
# with open("employees.csv") as file:
#     obj = csv.reader(file)
#     next(obj)
#     for data in obj:
#         print(data[0])

# using dictreader
# with open("employees.csv") as file:
#     obj = csv.DictReader(file)
#     for data in obj:
#         print(data["name"])

# 2.. WAP to print only the salaries that are > 70000

# using reader
# with open("employees.csv") as file:
#     obj = csv.reader(file)
#     for data in obj:
#         if data[-1] > "70000":
#             print(data[-1])


# using dictreader
# with open("employees.csv") as file:
#     obj = csv.DictReader(file)
#     for data in obj:
#         if data["pay"] > "70000":
#              print(data["pay"])

# 3.. WAP to group male and female employees in the file

# using reader
# with open("employees.csv") as file:
#     f = []
#     m = []
#     obj = csv.reader(file)
#     next(obj)
#     for items in obj:
#         if items[1] == "female":
#             f.append(items[0])
#         else:
#             m.append(items[0])
#     print(f"Female: {f}\nMale: {m}")

# using Dictreader


# 4.. Group employees based on their team
with open("employees.csv") as file:
    d = {}
    obj = csv.reader(file)
    next(obj)
    for data in obj:
        print(data)
