import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


df["Total_Marks"] = (
    df["Python"]
    + df["SQL"]
    + df["Maths"]
)


df["Average_Marks"] = df["Total_Marks"] / 3


print("\nStudent Marks:")

print(
    df[
        [
            "Name",
            "Python",
            "SQL",
            "Maths",
            "Total_Marks",
            "Average_Marks"
        ]
    ].head(10)
)


def performance(avg):

    if avg >= 80:
        return "Excellent"

    elif avg >= 60:
        return "Good"

    elif avg >= 40:
        return "Average"

    else:
        return "Poor"


df["Performance"] = df["Average_Marks"].apply(performance)


print("\nStudent Performance:")

print(
    df[
        [
            "Name",
            "Average_Marks",
            "Performance"
        ]
    ].head(10)
)


top_students = df.sort_values(
    "Average_Marks",
    ascending=False
)

print("\nTop 10 Students:")

print(
    top_students[
        [
            "Name",
            "Department",
            "Average_Marks"
        ]
    ].head(10)
)


department_performance = (
    df.groupby("Department")["Average_Marks"]
    .mean()
    .sort_values(ascending=False)
)

print("\nDepartment-wise Average Marks:")

print(department_performance)


print("\nSubject-wise Average Marks:")

print("Python:", df["Python"].mean())
print("SQL:", df["SQL"].mean())
print("Maths:", df["Maths"].mean())


correlation = df[
    [
        "Attendance",
        "Average_Marks"
    ]
].corr()

print("\nAttendance vs Average Marks Correlation:")

print(correlation)


at_risk = df[
    (df["Attendance"] < 75)
    &
    (df["Average_Marks"] < 50)
]

print("\nAt-Risk Students:")

print(
    at_risk[
        [
            "Name",
            "Department",
            "Attendance",
            "Average_Marks",
            "Performance"
        ]
    ]
)


performance_count = df["Performance"].value_counts()

print("\nPerformance Distribution:")

print(performance_count)



df.to_csv(
    "student_performance_processed.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")