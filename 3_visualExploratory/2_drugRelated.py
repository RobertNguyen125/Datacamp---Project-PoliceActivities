import pandas as pd
import matplotlib.pyplot as plt

ri2 = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/ri2.csv')

# print(ri2.columns)
# convert index to datetimeindex
ri2.index = pd.to_datetime(ri2['stop_datetime'])
# calculate the annual rate of drug-related stop
annual_drug_rate = ri2.drugs_related_stop.resample('A').mean()
# annual_drug_rate.plot()
# plt.show()
# plt.savefig('/Users/apple/desktop/policeActivities/3_visualExploratory/3_annualDrugRate.png')

# annual search rate
annual_search_rate = ri2['search_conducted'].resample('A').mean()
print(annual_search_rate)
# concat annual_search_rate and annual_drug_rate:
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')
annual.plot(subplots=True)
plt.show()
plt.savefig('/Users/apple/desktop/policeActivities/3_visualExploratory/2_drugVsSearch.png')
