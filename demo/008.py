import pandas as pd
from matplotlib import pyplot as plt
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 读取Excel文件
orders = pd.read_excel('{}/Orders.xlsx'.format(path), index_col='Week')
print(orders)
print(orders.columns)

# 折线图
# orders.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
# 叠加区域图
orders.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(orders.index, fontsize=8)
plt.show()