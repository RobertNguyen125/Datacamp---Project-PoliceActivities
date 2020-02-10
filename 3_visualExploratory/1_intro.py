import pandas as pd

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
# print(ri2.head())
# overall arrest rate
print(ri2['is_arrested'].mean())
# hourly arrest rate
ri2.index = pd.to_datetime(ri2['stop_datetime'])


hourly_arrest_rate = ri2.groupby(ri2.index.hour).is_arrested.mean()
print(hourly_arrest_rate)
