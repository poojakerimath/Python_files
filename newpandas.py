import pandas as pd

# Load the CSV file
df = pd.read_csv('employees.csv')

# Display the first few rows
print(df.head())

# Example operations
print(df['Department'].value_counts())         # Count employees per department
print(df[df['Salary'] > 65000])                # Filter high salaries
print(df['Salary'].mean())                     # Average salary
