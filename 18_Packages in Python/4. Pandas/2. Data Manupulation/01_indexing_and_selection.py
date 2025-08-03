import pandas as pd
#create dataframe
df=pd.DataFrame({
    "a":[1,2,3,4,5],
    "b":[6,7,8,9,10],
    "c":[11,12,13,14,15]
})

# print the data
print(df)

value=df.loc[0,'a']
print(value,"0,'a'")

value=df.loc[3,'b']
print(value,"3,b")

value=df.loc[4,'c']
print(value,"4,c")

value=df.loc[2,'a']
print(value,"2,a")