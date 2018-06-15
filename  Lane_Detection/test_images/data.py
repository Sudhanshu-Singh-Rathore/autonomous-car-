import pandas as pd
import datetime
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
#

# web_stats={'Day':[1,2,3,4,5],
#            'Visitors':[43,54,56,67,89],
#            'Bounce Rate':[65,72,36,87,54]
#             }
# df=pd.DataFrame(web_stats)

#To set a particular column as an index
# df.set_index('Day', inplace=True)
# print(df.head())

# print(np.array(df[['Bounce_Rate','Visitors']]))
# print(np.array(df.Visitors))

start=datetime.datetime(2010,1,1)
end=datetime.datetime(2015,8,22)

df=web.DataReader('AAPL','yahoo',start,end)

print(df)
print(df.head())
df['Adj Close'].plot()
plt.legend()
plt.show()
