import pandas as pd
# create dataframe
df=pd.DataFrame({
    "A":[1,2,3,4,5],
    "B":["a","b","c","d","e"],
    "C":[1.2,2.4,3.6,4.8,6.0]
})
# print the data
print(df)

selected_rows=df.loc[1:3]
print(selected_rows)