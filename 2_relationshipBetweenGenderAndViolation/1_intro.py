# count unique value: .value_counts() | Best for categorical data
# express in percentage: .value_counts(normalize=True)
# filtering DF rows: df[df['column'] == '']

import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
# count the unique values of violation columns
print(ri.violation.value_counts())
# percentage of each unique violation
print(ri.violation.value_counts(normalize=True))
