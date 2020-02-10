import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
print(ri['violation'])
# Filter df: create female and male DF
female = ri[ri['driver_gender']=='F']
male = ri[ri['driver_gender']=='M']

# Percentage of unique violation
print(female.violation.value_counts(normalize=True))
print(male.violation.value_counts(normalize=True))

# filter by  multiple conditions:
female_arrested = ri[(ri['driver_gender']=='F') & (ri['is_arrested']==True)]
print(female_arrested)

# compare speeding outcomes between 2 genders
# df: female_speeding:
female_speeding = ri[(ri['driver_gender']=='F') & (ri['violation']=='Speeding')]
print(female_speeding.head())
# df: male_speeding
male_speeding = ri[(ri['driver_gender']=='M')&(ri['violation']=='Speeding')]
print(male_speeding.head())
# compute the stop outcome for both
print(female_speeding['stop_outcome'].value_counts(normalize=True))
print(male_speeding['stop_outcome'].value_counts(normalize=True))
