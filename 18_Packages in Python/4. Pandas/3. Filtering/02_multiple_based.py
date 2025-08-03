import pandas as pd
df=pd.DataFrame({
    "a":[1,2,3,4,5],
    "b":[6,7,8,9,10],
    "c":[11,12,13,14,15]
})
print(df)
print("______--------_______")
filtered_df=df[(df["a"]>1) & (df["a"]<5)]
# side by side indexing number in it.....
print(1,filtered_df)

filtered_df=df[df["a"]>1 & (df["a"]<3)]
print(2,filtered_df)

filtered_df=df[df["a"]>2]
print(3,filtered_df)

filtered_df=df[df["a"]>3]
print(4,filtered_df)

filtered_df=df[df["a"]>4]
print(filtered_df)