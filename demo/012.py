import pandas as pd
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
employees = pd.read_excel(f'{path}/Employees.xlsx', index_col='ID')
# split会将Full Name按空格拆分成一列[xxx, yyy]，如果使用expand=True参数，则会变成两列：xxx, yyy
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1].str.upper()
print(employees)