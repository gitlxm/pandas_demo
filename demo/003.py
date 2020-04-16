import pandas as pd
import os
from datetime import date, timedelta


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 自动填充
# 跳过前三行，只读取第C，D，E，F列
books = pd.read_excel('{}/books.xlsx'.format(path), skiprows=3, usecols='C:F', index_col=None,
                      dtype={'ID': str, 'InStore': str, 'Date': str})

# 自动填充每一列
start = date(2019, 1, 1)
for i in books.index:
    # 方式1：找到ID这个series，修改它的每一行
    # books['ID'].at[i] = i + 1
    # 方式2：直接修改单元格
    books.at[i, 'ID'] = i+1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'

    # Date每一行比上一行加一天
    # books['Date'].at[i] = start + timedelta(days=i)

    # Date每一行比上一行加一月
    books['Date'].at[i] = add_month(start, i)

    # Date每一行比上一行加一年
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)

books.set_index('ID', inplace=True)
print(books)

books.to_excel('{}/New_Books.xlsx'.format(path))
