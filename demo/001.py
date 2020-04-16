import pandas as pd

projects = pd.read_excel('/Users/liujun/Downloads/20200314.xlsx', header=0)
print(projects.shape)
# print(projects.columns)

print(projects.head(3))
print(projects.tail(3))

