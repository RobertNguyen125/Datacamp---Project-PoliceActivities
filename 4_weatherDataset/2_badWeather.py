import pandas as pd
import matplotlib.pyplot as plt
weather = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/weather.csv')

# create new df from WT0 - WT22:
WT = weather.loc[:,'WT01':'WT22']
print(WT.head())

weather['bad_conditions'] = WT.sum(axis=1)
weather['bad_conditions'] = weather['bad_conditions'].fillna(0).astype('int')
weather['bad_conditions'].plot(kind='hist')
# plt.show()

# count unique values in bad_conditions columns:
print(weather['bad_conditions'].value_counts().sort_index())

mapping = {0:'good', 1:'bad', 2:'bad', 3: 'bad', 4: 'bad',
            5: 'worse', 6: 'worse', 7: 'worse', 8: 'worse', 9: 'worse'}
# map the rating
weather['rating']= weather.bad_conditions.map(mapping)
print(weather['rating'].value_counts())
# create a list of weather_rating in logic order:
cat = ['good', 'bad', 'worse']
# change type to categorical:
weather['rating'] = weather.rating.astype('category', ordered=True, categories=cat)
print(weather['rating'].head())
weather.to_csv('/Users/apple/desktop/policeActivities/dataset/weather1.csv')
