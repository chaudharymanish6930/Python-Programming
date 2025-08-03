import pandas as pd
df=pd.DataFrame({
    "a":[1,2,3,4,5],
    "b":[6,7,8,9,10],
    "c":[11,12,13,14,15]
})
print(df)
print("______--------_______")

# side by side indexing number in it.....
# 1
filtered_df=df[df["a"]>3]
print(1,filtered_df,"\n")
# ouput
# 1    a   b   c
# 3  4   9  14
# 4  5  10  15

# 2
filtered_df=df[df["a"]>1]
print(2,filtered_df,"\n")
# ouput
# 2  a   b   c
# 1  2   7  12
# 2  3   8  13
# 3  4   9  14
# 4  5  10  15

# 3
filtered_df=df[df["a"]>2]
print(3,filtered_df,"\n")
# ouput
# 3  a   b   c
# 2  3   8  13
# 3  4   9  14
# 4  5  10  15

# 4
filtered_df=df[df["b"]>3]
print(4,filtered_df,"\n")
# ouput
# 4  a   b   c
# 0  1   6  11
# 1  2   7  12
# 2  3   8  13
# 3  4   9  14
# 4  5  10  15

# 5
filtered_df=df[df["c"]>4]
print(filtered_df,"\n")
# ouput
# 5  a   b   c
# 0  1   6  11
# 1  2   7  12
# 2  3   8  13
# 3  4   9  14
# 4  5  10  15