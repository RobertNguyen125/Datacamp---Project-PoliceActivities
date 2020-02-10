import pandas as pd

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
# because value_counts excludes missing value by default, we put dropna=False argument
print(ri2['search_type'].value_counts(dropna=False))
print(ri2['search_type'].value_counts())

# create new column: inventory
ri2['inventory'] = ri2.search_type.str.contains('Inventory', na=False)
print(ri2['inventory'].mean()) # NOTE: this result is false as it includes all the missing value from total search

print(ri2[ri2['search_conducted']==True].inventory.mean()) # NOTE: this takes into account the search that actually happened
