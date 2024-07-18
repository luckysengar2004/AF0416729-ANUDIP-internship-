# PROBLEM ON DICTIONARY:- Creating table using Dictionary
import pandas as pd 
from tabulate import tabulate

student_data = [
    {"stdid": 1, "stdname": "Rahul Sharma", "class": 10, "age": 15, "hindi": 85, "english": 78, "maths": 92, "science": 88, "computer": 90},
    {"stdid": 2, "stdname": "Anjali Verma", "class": 10, "age": 16, "hindi": 80, "english": 82, "maths": 95, "science": 91, "computer": 89},
    {"stdid": 3, "stdname": "Rohan Mehta", "class": 10, "age": 15, "hindi": 75, "english": 80, "maths": 88, "science": 85, "computer": 87},
    {"stdid": 4, "stdname": "Neha Singh", "class": 10, "age": 16, "hindi": 90, "english": 88, "maths": 94, "science": 92, "computer": 93},
    {"stdid": 5, "stdname": "Amit Patel", "class": 10, "age": 15, "hindi": 78, "english": 75, "maths": 85, "science": 80, "computer": 82},
    {"stdid": 6, "stdname": "Priya Sinha", "class": 10, "age": 16, "hindi": 88, "english": 84, "maths": 89, "science": 87, "computer": 90},
    {"stdid": 7, "stdname": "Suresh Kumar", "class": 10, "age": 15, "hindi": 82, "english": 79, "maths": 90, "science": 86, "computer": 88},
    {"stdid": 8, "stdname": "Rita Desai", "class": 10, "age": 16, "hindi": 85, "english": 83, "maths": 92, "science": 89, "computer": 91},
    {"stdid": 9, "stdname": "Vikram Joshi", "class": 10, "age": 15, "hindi": 77, "english": 76, "maths": 84, "science": 81, "computer": 83},
    {"stdid": 10, "stdname": "Sneha Reddy", "class": 10, "age": 16, "hindi": 89, "english": 85, "maths": 91, "science": 90, "computer": 92},
    {"stdid": 11, "stdname": "Ravi Gupta", "class": 10, "age": 15, "hindi": 80, "english": 78, "maths": 86, "science": 84, "computer": 85},
    {"stdid": 12, "stdname": "Sunita Malhotra", "class": 10, "age": 16, "hindi": 87, "english": 82, "maths": 90, "science": 88, "computer": 89}
]
header = ["stdid","stdname","class","age","hindi","english","maths","science","computer"]

# complete students detail in column form
df=pd.DataFrame(data=student_data,columns=header)
print(df)

# to show the data in the form of table using the tabulate library of python
student_tabulate= tabulate(df,headers=header,tablefmt="grid")
print(student_tabulate)


# Q-1 student with more than 80 marks in english
for student in student_data:
    if(student['english']>80):
        a = student.values()
        print(a)
print()

#  Q-2 name and age of students with more marks than 40 in maths
for student in student_data:
    if(student['maths']>40):
        print(end="  "f"Name:{student['stdname']}"+"  ")
        print(f"Age:{student['age']}")
print()



# Q-3- Student name and age of top four scrorer in maths:-
# Extract Maths scores and corresponding student details
math_scores = [(value['Maths'], value['stdname'], value['Age']) for value in Students.values()]

# Sort based on Maths scores in descending order
math_scores.sort(reverse=True, key=lambda x: x[0])

# Get top four scorers
top_four_scorers = math_scores[:4]

# Display the names and ages of top four scorers
for score, name, age in top_four_scorers:
    print(f"Name: {name}, Age: {age}")
