import pandas as pd
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 筛选出年龄在18到30岁，分数在80到100分的学生
students = pd.read_excel('{}/Students.xlsx'.format(path), index_col='ID')
students = students.loc[students.Age.apply(lambda a: 18 <= a < 30)] \
    .loc[students.Score.apply(lambda s: 80 <= s < 100)]
print(students)