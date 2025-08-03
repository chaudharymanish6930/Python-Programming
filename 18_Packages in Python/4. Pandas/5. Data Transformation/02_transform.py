import pandas as pd

dgf=pd.Series({
    4:[9,8,7,6,5,4]
})
print(dgf)

transform=dgf.apply(lambda x: x*3)
print(transform)