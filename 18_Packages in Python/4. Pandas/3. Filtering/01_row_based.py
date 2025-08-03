import pandas as pd 
# create  a dataframe...
df=pd.DataFrame({
    'A':[2,4,3],
    "b":['a','b','c'],
    'C':[4.5,89.0,98.8]
})
# print data
print(df)

filtered_df=df[df["A"]>2]   #   A  b     C
print(filtered_df)          #   1  4  b  89.0
                            #   2  3  c  98.8