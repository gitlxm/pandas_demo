import pandas as pd
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
students = pd.read_excel(f'{path}/Students_13.xlsx')
scores = students[['Test_1', 'Test_2', 'Test_3']]

# 按行求和和平均值，会为表格增加两列
students['Total'] = scores.sum(axis=1)
students['Average'] = scores.mean(axis=1)


# 按列求平均值，会为表格增加一行
col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'

students = students.append(col_mean, ignore_index=True)

print(students)