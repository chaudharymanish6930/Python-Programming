import pandas as pd
import numpy as np
data = np.array([[1,4],[2,5],[3,6]])
df = np.dataFrame(data, index=['A','B','C'], columns=['Column1','Column2'])
print(df)