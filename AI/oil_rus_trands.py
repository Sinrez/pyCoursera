import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel('gdprussia.xlsx')

plt.scatter(df.oilprice, df.gdp)
plt.xlabel('oil price (US$)')
plt.ylabel('GDP, Russia (bln US$)')

reg = linear_model.LinearRegression()
reg.fit(df[['oilprice']], df.gdp)

plt.plot(df.oilprice, reg.predict(df[['oilprice']]))