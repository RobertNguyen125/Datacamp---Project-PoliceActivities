import pandas as pd
import matplotlib.pyplot as plt
weather = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/weather.csv')

print(weather[['TAVG', 'TMIN', 'TMAX']].describe())
weather.plot(kind='box')
plt.show()

# plotting differences in temperature
weather['TDIFF'] = weather.TMAX - weather.TMIN
print(weather['TDIFF'].describe())
weather.TDIFF.plot(kind='hist', bins=20)
plt.show()
