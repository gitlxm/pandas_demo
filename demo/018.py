import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

path = os.path.abspath(os.path.join(os.getcwd(), "../demo/data"))
sales = pd.read_excel(f'{path}/Sales.xlsx', dtype={'Month': str, 'Revenue': float})


slope, intercept, r_value, p_value, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='red')
plt.title(f'y={slope}*x+{intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.show()