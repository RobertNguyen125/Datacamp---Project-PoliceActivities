import pandas as pd

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')

ri2['frisk'] = ri2.search_type.str.contains('Protective Frisk', na=False)

# create dataframe search, where the contains the True value
searched = ri2[ri2['search_conducted']==True]
#calculate the frisk rate by taking the mean of frisk
print(searched.frisk.mean())
# calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())
