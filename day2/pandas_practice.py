import pandas as pd

students = {
    "name": ["Hailey", "John", "Emma"],
    "grade": [95, 82, 91]

}

df = pd.DataFrame(students)

print(df)

print()
print("Average Grade:")
print(df["grade"].mean())
