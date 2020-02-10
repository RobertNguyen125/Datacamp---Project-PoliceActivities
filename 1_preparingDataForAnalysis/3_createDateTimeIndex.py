# use string method to manipulate the data: df.columns.str.replace()
# to combine columns: df.['column1'].str.cat(df['column2'], sep='')
# convert to datetime format: to_datetime()

import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
print(ri.head())
# combined 'stop_date' and 'stop_time' columns
combined = ri['stop_date'].str.cat(ri['stop_time'], sep =' ')
# convert 'combined' to  datetime format: stop_datetime
ri['stop_datetime'] = pd.to_datetime(combined)
print(ri['stop_datetime'].dtype)
# set_index as stop_datetime
ri.set_index('stop_datetime', inplace=True)
