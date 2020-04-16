import pandas as pd
import os

# 旋转数据表
pd.options.display.max_columns = 999
path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
table = pd.read_excel(f'{path}/Videos.xlsx', index_col='Month')
table = table.transpose()
print(table)