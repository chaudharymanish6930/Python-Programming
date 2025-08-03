import pandas as pd

df=pd.DataFrame({
    "A":[1,3,5,7,9],
    "B":[2,4,6,8,10]
})

transform=df.apply(lambda x: x*3)
print(transform)