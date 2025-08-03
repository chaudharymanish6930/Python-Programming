import pandas as pd

df=pd.DataFrame({
    "A":[1,2,3,4,5],
    "B":["a","b","c","d","e"],
    "C":[1.2,2.4,3.6,4.8,6.0]
})

print(df)

selected_columns=df.loc[:,"B":"C"] 
print(selected_columns)