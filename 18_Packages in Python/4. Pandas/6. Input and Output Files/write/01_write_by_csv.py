import pandas as pd

df=pd.DataFrame({
    'a':[9,8,7,8],
    'name':['manish','sahil','aryan','osheen'],
    "age":[24,32,12,25],
    "city":['new york',"america",'rajasthan','australia']
})

df.to_csv('D:/python/01upload on github/18_Packages in Python/4. Pandas/6. Input and Output Files/write/wite.csv',index=False)
