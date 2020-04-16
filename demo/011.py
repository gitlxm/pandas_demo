import pandas as pd
import os

def score_valiation(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

# students = pd.read_excel('/Users/liujun/PycharmProjects/pandas_demo/demo/data/Students_Data.xlsx')
path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
students = pd.read_excel('{}/Students_Data.xlsx'.format(path))

# axis=1表示行
students.apply(score_valiation, axis=1)
# print(students)

