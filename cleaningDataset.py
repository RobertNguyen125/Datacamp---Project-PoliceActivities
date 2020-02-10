import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
print(ri.shape)
# drop unnecessary columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)
ri.dropna(subset=['driver_gender'], inplace=True)
# propert datatype for 'is_arrested'
ri['is_arrested'] = ri['is_arrested'].astype('bool')
print(ri.is_arrested.dtype)

# create datime index
combined = ri['stop_date'].str.cat(ri['stop_time'], sep =' ')
ri['stop_datetime']=pd.to_datetime(combined)
print(ri['stop_datetime'].dtype)
ri.set_index('stop_datetime', inplace=True)
print(ri.index.dtype)

# print(ri.head())

ri.to_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
print(ri2.index)
