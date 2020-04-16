import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 读取Excel文件
students = pd.read_excel('{}/Interational_Students.xlsx'.format(path), index_col='From')
# counterclock=False:逆时针
students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()