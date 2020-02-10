# .crosstab(), short for cross_tabulation
import pandas as pd
import matplotlib.pyplot as plt

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')
table = pd.crosstab(ri2['driver_race'], ri2['driver_gender']) # NOTE: frequency table in form of dataframe
print(table)
# check the result of frequency table
asian_female = ri2[(ri2['driver_gender']=='F') & (ri2['driver_race']=='Asian')]
print(asian_female.shape)

table = table.loc['Asian':'Hispanic']
print(table)

# create stacked bar plot
# table.plot(kind='bar', stacked=True)
# plt.show()

# district violation
# create frequency table with distric and violation
all_zones =  pd.crosstab(ri2['district'],ri2['violation'])
print(all_zones)
# slice the dataframe to get k1-k3:
k_zones = all_zones.loc['Zone K1': 'Zone K3']
print(k_zones)
