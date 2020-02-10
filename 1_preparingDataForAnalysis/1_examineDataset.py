import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
print(ri.info())

# count the number of missing  values in each columns: .isnull()
print(ri.isnull().sum())

# drop unnecessary columns: 'county_name' and 'state'
ri.drop(['county_name', 'state'], axis='columns', inplace=True)
print(ri.head())

# drop rows with n/a: driver_gender
# check the null value before:
print(ri.isnull().sum())
ri.dropna(subset=['driver_gender'], inplace=True)
#check the null value after:
print(ri.isnull().sum())
