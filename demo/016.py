import pandas as pd
import os

# 加载纯文本文件
path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data/016"))

students1 = pd.read_csv(f'{path}/Students.csv', index_col='ID')
students2 = pd.read_csv(f'{path}/Students.tsv', sep='\t', index_col='ID')
students3 = pd.read_csv(f'{path}/Students.txt', sep='|', index_col='ID')

print(students1)
print(students2)
print(students3)