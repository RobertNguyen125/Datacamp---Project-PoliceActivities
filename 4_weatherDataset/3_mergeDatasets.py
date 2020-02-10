import pandas as pd
import matplotlib.pyplot as plt
weather = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/weather1.csv')
ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')

ri2.reset_index(inplace=True)
print(ri2.head())
weather_rating = weather[['DATE','rating']]
print(weather_rating.head())

# merge ri2 and weather_rating
ri_weather = pd.merge(left=ri2, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')
print(ri_weather.shape)
ri_weather.set_index('stop_datetime', inplace=True)
print(ri_weather.head())

# calculate overall arrest_rate
print(ri_weather['is_arrested'].mean())
# calculate arrest rate for each weather rating
print(ri_weather.groupby('rating')['is_arrested'].mean())
# calculate arrest rate for each violation and weather rating
arrest_rate = ri_weather.groupby(['violation', 'rating'])['is_arrested'].mean()
print(arrest_rate.head())
# access multilevel index
moving_bad = arrest_rate.loc['Moving violation', 'bad']
speeding_all =  arrest_rate.loc['Speeding']
print(moving_bad)

# unstack to create dataframe
print(arrest_rate.unstack())
# use pivot_table to create the same thing
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))
