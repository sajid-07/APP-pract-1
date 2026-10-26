import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# Step 0: Automatically create 'student.csv' if it doesn't exist locally
# -------------------------------------------------------------------------
csv_filename = 'student.csv'

if not os.path.exists(csv_filename):
    sample_data = {
        'roll_number': [101, 102, 103, 104, 105, 106, 107, 108],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],
        'study_hours': [2.5, 5.0, 7.5, 3.0, 8.0, 6.5, 4.0, 9.0],
        'marks': [55, 72, 88, 60, 92, 78, 68, 95]
    }
    pd.DataFrame(sample_data).to_csv(csv_filename, index=False)
    print(f"Sample dataset '{csv_filename}' created successfully.\n")


# -------------------------------------------------------------------------
# Task 1: Read the CSV file into a Pandas DataFrame
# -------------------------------------------------------------------------
df = pd.read_csv(csv_filename)


# -------------------------------------------------------------------------
# Task 2: Display the first five records and dataset information
# -------------------------------------------------------------------------
print("--- First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
df.info()
print("\n" + "="*50 + "\n")


# -------------------------------------------------------------------------
# Task 3: Calculate the average, maximum, and minimum marks
# -------------------------------------------------------------------------
avg_marks = df['marks'].mean()
max_marks = df['marks'].max()
min_marks = df['marks'].min()

print(f"Average Marks : {avg_marks:.2f}")
print(f"Maximum Marks : {max_marks}")
print(f"Minimum Marks : {min_marks}")
print("\n" + "="*50 + "\n")


# -------------------------------------------------------------------------
# Task 4: Identify students who scored more than 75 marks
# -------------------------------------------------------------------------
high_scorers = df[df['marks'] > 75]

print("--- Students Scoring > 75 Marks ---")
print(high_scorers[['roll_number', 'name', 'marks']])
print("\n" + "="*50 + "\n")


# -------------------------------------------------------------------------
# Task 5: Generate a bar chart showing marks obtained by each student
# -------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df['name'], df['marks'], color='skyblue', edgecolor='black')
plt.title('Marks Obtained by Each Student')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# -------------------------------------------------------------------------
# Task 6: Generate a histogram showing the distribution of student marks
# -------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df['marks'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency (Number of Students)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# -------------------------------------------------------------------------
# Task 7: Generate a scatter plot showing study hours vs marks
# -------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df['study_hours'], df['marks'], color='purple', s=70, edgecolors='black')
plt.title('Relationship Between Study Hours and Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()