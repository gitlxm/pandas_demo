import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
# 以Name为横轴，以分数为纵轴，绘制柱状图
# 读取Excel文件
students = pd.read_excel('{}/Students.xlsx'.format(path))
# 筛选出年龄在18到30岁，分数在80到100分的学生
students = students.loc[students.Age.apply(lambda a: 18 <= a < 30)] \
    .loc[students.Score.apply(lambda s: 80 <= s < 100)]
# 按照分数排序，倒序
students.sort_values(by='Score', ascending=False, inplace=True)
# bar：柱状图
plt.bar(students.Name, students.Score, color='orange')
plt.xlabel('Name', fontweight='bold')
plt.ylabel('Score', fontweight='bold')
plt.title('International Student by Score', fontsize=16, fontweight='bold')
# 拿到坐标轴,gca:Get the current axes
ax = plt.gca()
# 重设横坐标，label以水平右边的位置旋转45度
ax.set_xticklabels(students.Name, rotation=45, ha='right')
# 拿到中间图形区域,gcf:Get the current figure
f = plt.gcf()
f.subplots_adjust(left=0.14, bottom=0.3)
plt.show()