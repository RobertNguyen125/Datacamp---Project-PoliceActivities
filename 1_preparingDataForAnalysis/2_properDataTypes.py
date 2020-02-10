# important data type:
# int, float: enables mathetical operations
# datetime: enable data_based attributes and methods
# category: use less memory and run faster
# bool: enables logical and mathetical operations
# DF.dtype to check data type
# DF.'column'.astype('') = DF['columns'].astype('')

# fixing datatype: is_arrested
import pandas as pd

ri = pd.read_csv('/Users/apple/desktop/policeActivities/dataset/police.csv')
print(ri['is_arrested'].dtype)

ri['is_arrested'] = ri['is_arrested'].astype('bool')
print(ri['is_arrested'].dtype)
