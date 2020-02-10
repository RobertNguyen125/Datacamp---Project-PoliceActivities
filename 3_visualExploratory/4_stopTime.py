import pandas as pd
import matplotlib.pyplot as plt

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
print(ri2['stop_duration'].unique())

mapping = {'0-15 Min':8, '16-30 Min':23, '30+ Min':45}
ri2['stop_minute']= ri2['stop_duration'].map(mapping)
print(ri2['stop_minute'].unique())

# calculate the mean 'stop_minute' for each 'violation_raw'
stop_length = ri2.groupby('violation_raw').stop_minute.mean()
stop_length.sort_values().plot(kind='barh')
plt.show()
