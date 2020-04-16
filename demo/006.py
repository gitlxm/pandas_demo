import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 读取Excel文件
users = pd.read_excel('{}/Users.xlsx'.format(path))
# 扩展一个Total列，用于按照Total来排序
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True)
print(users)

# 分组柱状图：横轴x=Name，其他三列分组作为纵轴
# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'])
# barh:横向柱状图，stacked=True：拼接柱状图，将三列数据拼接到一起
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
plt.tight_layout()
plt.show()