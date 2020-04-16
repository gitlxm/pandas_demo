import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# console中显示的最大列数
pd.options.display.max_columns=50
homes = pd.read_excel('{}/home_data.xlsx'.format(path))
print(homes.head())

# 查看每一列与其他列之间的关系，相关性
print(homes.corr())

# 散点图
# homes.plot.scatter(x='sqft_living', y='price')

# 直方图
# homes.sqft_living.plot.hist(bins=100)
# # 将横轴重铺，让横轴的显示的区间更合适
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)

# 密度图
homes.sqft_living.plot.kde()
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)

plt.show()

