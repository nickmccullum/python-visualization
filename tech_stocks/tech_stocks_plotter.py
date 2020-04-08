import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from datetime import datetime

tech_stocks_data = pd.read_csv('https://raw.githubusercontent.com/nicholasmccullum/python-visualization/master/tech_stocks/GOOG_MSFT_FB_AMZN_data.csv')
tech_stocks_data.sort_values('Period', ascending = True, inplace = True)


google = tech_stocks_data['Alphabet Inc Price']
amazon = tech_stocks_data['Amazon.com Inc Price']
facebook = tech_stocks_data['Facebook Inc Price']
microsoft = tech_stocks_data['Microsoft Corp Price']
dates = tech_stocks_data['Period']

x = []
for date in tech_stocks_data['Period']:
    x.append(datetime.strptime(date, '%Y-%m-%d %H:%M:%S').year)
    

plt.figure(figsize=(16,12))

#Plot 1
plt.subplot(2,2,1)
plt.xticks(np.arange(0, len(x) + 1)[::365], x[::365])
plt.plot(dates, google)
plt.title('Alphabet (GOOG) (GOOGL) Stock Price')

#Plot 2
plt.subplot(2,2,2)
plt.xticks(np.arange(0, len(x) + 1)[::365], x[::365])
plt.plot(dates, amazon)
plt.title('Amazon (AMZN)) Stock Price')

#Plot 3
plt.subplot(2,2,3)
plt.xticks(np.arange(0, len(x) + 1)[::365], x[::365])
plt.plot(dates, facebook)
plt.title('Facebook (FB) Stock Price')

#Plot 4
plt.subplot(2,2,4)
plt.xticks(np.arange(0, len(x) + 1)[::365], x[::365])
plt.plot(dates, microsoft)
plt.title('Microsoft (MSFT) Stock Price')
