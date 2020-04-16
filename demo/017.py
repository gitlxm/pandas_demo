import pandas as pd
import numpy as np
import os

pd.options.display.max_columns = 999
path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
orders = pd.read_excel(f'{path}/Orders_17.xlsx')
# 增加一列Year，它的值从Date这一列中取year的值
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
# print(orders.head())

# pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
# print(pt1)

groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)

