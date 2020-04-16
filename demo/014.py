import pandas as pd
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
students = pd.read_excel(f'{path}/Students_Duplicates.xlsx')
# 去掉重复的数据，keep='first'保留前面的，keep='last'保留后面的
# students.drop_duplicates(subset='Name', inplace=True, keep='first')
# print(students)

# 找到并列出重复的数据
dupe = students.duplicated(subset='Name')
# dupe = dupe[dupe == True]
dupe = dupe[dupe]
print(students.iloc[dupe.index])

