import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),"student_marker.csv"
)

df = pd.read_csv(file_path)
print(df)
print(df.shape)

#Checking column names
print(df.columns)
print(df.info())

#Checking for null values
print(df.isnull().sum())

#Basic statistics analysis
print(df.describe())

#Total marks
df['Total'] = df['Math'] + df['Physics'] + df['Chemistry'] + df['English'] + df['Computer']

# Average
df["Average"] = df[["Math", "Physics", "Chemistry", "English", "Computer"]].mean(axis=1)

#Result PASS/FAIL
df["Result"]=df[["Math","Physics","Chemistry","English","Computer"]].ge(40).all(axis=1).map({
    True: "PASS", False: "FAIL"
})
print(df)

# Highest Marks (Topper)
name = df.loc[df["Total"].idxmax(), "Name"]
highest_marks = df["Total"].max()

print("Highest mark scored by:", name)
print("Highest total marks:", highest_marks)

#Lowest Marks
name = df.loc[df["Total"].idxmin(), "Name"]
lowest_marks = df["Total"].min()

print("Lowest mark scored by:", name)
print("Lowest total marks:", lowest_marks)

df.to_csv("Analyzed_student_marker.csv", index=False)