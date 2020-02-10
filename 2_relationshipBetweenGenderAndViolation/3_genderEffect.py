# the mean of boolean represents the percentage of series that is True

import pandas as pd

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')

# calculate search rate by counting values
print(ri2['search_conducted'].value_counts())
# calculate search rate by mean
print(ri2['search_conducted'].mean())

# compare search rate by genders
print(ri2[ri2['driver_gender']=='F']['search_conducted'].mean())
print(ri2[ri2['driver_gender']=='M']['search_conducted'].mean())
# compare simultanenously
print(ri2.groupby('driver_gender')['search_conducted'].mean())

# check other factors affecting search rate
print(ri2.groupby(['driver_gender', 'violation']).search_conducted.mean())
print(ri2.groupby(['violation', 'driver_gender']).search_conducted.mean())
