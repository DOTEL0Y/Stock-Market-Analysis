import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

msft = pd.read_csv('D:\Work\Stats\excel-python\Stock-Market\MSFT-Stock-Analysis\MSFT.csv')
sony = pd.read_csv('SONY.csv')
DataX = msft
print(DataX.describe(),DataX.info())
sns.lineplot(
    x="Date",y="Open",data=msft
)
sns.lineplot(
    x='Date',y='Open',data=sony,
)
sns.set_style('dark')
sns.despine(left=False)
plt.show()