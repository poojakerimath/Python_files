import pandas as pd
df = pd.read_csv('employees.csv')
print(df.head())

print("\n average salary:", df['Salary'].mean)
print("\n Employees in engineering:\n", df[df['Department']=='Engineering'])
print("\nSalary by Department:\n", df.groupby('Department')['Salary'].mean())
