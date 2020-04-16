import pandas as pd
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
students = pd.read_excel('{}/Student_score.xlsx'.format(path), sheet_name='Students')
scores = pd.read_excel('{}/Student_score.xlsx'.format(path), sheet_name='Scores')

# left join, fillna(0)将NaN用0代替, left_on, right_on
table = students.merge(scores, how='left', on='ID').fillna(0)
# 将Score设置成int型
table.Score = table.Score.astype(int)
print(table)