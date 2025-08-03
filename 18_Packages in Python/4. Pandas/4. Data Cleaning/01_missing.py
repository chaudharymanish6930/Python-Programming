import pandas as pd
import numpy as np

df=pd.DataFrame({
    "a":[1,2,np.nan,4,5],
    "b":[np.nan,7,8,9,10],
    "c":[11,12,13,np.nan,15]
})
print(df)

missed_value=df.isna()
print(missed_value)

# outputs.....
#      a     b     c
# 0  1.0   NaN  11.0
# 1  2.0   7.0  12.0
# 2  NaN   8.0  13.0
# 3  4.0   9.0   NaN
# 4  5.0  10.0  15.0
#        a      b      c
# 0  False   True  False
# 1  False  False  False
# 2   True  False  False
# 3  False  False   True
# 4  False  False  False