import pandas as pd

# Load the dataset
df = pd.read_csv("survey.csv")

# Print the number of rows and columns
print("Dataset shape:", df.shape)

# Print the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Print all column names
print("\nColumn names:")
print(df.columns.tolist())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

df = df.drop(columns=["state"])

df["self_employed"] = df["self_employed"].fillna("No")

df["work_interfere"] = df["work_interfere"].fillna("Don't know")

df = df[(df["Age"] >= 18) & (df["Age"] <= 65)]

def clean_gender(g):
    g = g.lower()
    if "male" in g:
        return "Male"
    elif "female" in g:
        return "Female"
    else:
        return "Other"

df["Gender"] = df["Gender"].apply(clean_gender)


# Clean data

# Drop columns with too many missing values (safe even if already removed)
df = df.drop(columns=["comments", "state"], errors='ignore')


# 2. Fill missing values
df["self_employed"] = df["self_employed"].fillna("No")
df["work_interfere"] = df["work_interfere"].fillna("Don't know")

# 3. Filter out unrealistic ages
df = df[(df["Age"] >= 18) & (df["Age"] <= 65)]

# 4. Normalize gender values
def clean_gender(g):
    g = str(g).lower()
    if "male" in g:
        return "Male"
    elif "female" in g:
        return "Female"
    else:
        return "Other"

df["Gender"] = df["Gender"].apply(clean_gender)

# Print to verify changes
print("\nData cleaned! New shape:", df.shape)
print("\nGender counts:")
print(df["Gender"].value_counts())

import matplotlib.pyplot as plt

# 1. Gender Distribution
gender_counts = df["Gender"].value_counts()
plt.figure(figsize=(6, 4))
gender_counts.plot(kind="bar", color=["skyblue", "orange"])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Mental Health Treatment by Gender
treatment_by_gender = df.groupby("Gender")["treatment"].value_counts().unstack()
treatment_by_gender.plot(kind="bar", stacked=True, figsize=(8, 5))
plt.title("Mental Health Treatment by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Treatment by company size
treatment_by_size = df.groupby("no_employees")["treatment"].value_counts().unstack()
treatment_by_size.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Mental Health Treatment by Company Size")
plt.xlabel("Number of Employees")
plt.ylabel("Number of People")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Remote work vs. mental health treatment
remote_treatment = df.groupby("remote_work")["treatment"].value_counts().unstack()
remote_treatment.plot(kind="bar", stacked=True, figsize=(8, 5))
plt.title("Mental Health Treatment by Remote Work Status")
plt.xlabel("Remote Work")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
