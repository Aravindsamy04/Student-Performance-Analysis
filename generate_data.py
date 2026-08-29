import pandas as pd
import random

random.seed(42)

names = [
    "Arun", "Rahul", "Karthik", "Vijay", "Ajay",
    "Priya", "Divya", "Sneha", "Ananya", "Keerthi",
    "Riya", "Harini", "Nithya", "Swetha", "Pooja"
]

genders = ["Male", "Female"]

departments = ["AI&DS", "CSE", "ECE", "EEE", "IT"]

data = []

for i in range(1, 101):

    name = random.choice(names)

    gender = random.choice(genders)

    department = random.choice(departments)

    attendance = random.randint(55, 100)

    study_hours = round(random.uniform(1, 8), 1)

    assignment_score = random.randint(40, 100)

    internal_marks = random.randint(40, 100)

    python = random.randint(35, 100)

    sql = random.randint(35, 100)

    maths = random.randint(35, 100)

    placement_status = random.choice(
        ["Placed", "Not Placed"]
    )

    data.append([
        i,
        name,
        gender,
        department,
        attendance,
        study_hours,
        assignment_score,
        internal_marks,
        python,
        sql,
        maths,
        placement_status
    ])

columns = [
    "Student_ID",
    "Name",
    "Gender",
    "Department",
    "Attendance",
    "Study_Hours",
    "Assignment_Score",
    "Internal_Marks",
    "Python",
    "SQL",
    "Maths",
    "Placement_Status"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("students.csv", index=False)

print("Dataset created successfully!")
print(df.head())