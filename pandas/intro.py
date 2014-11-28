import pandas as pd
import numpy as np


# initatilize
df=pd.DataFrame(np.zeros(0,dtype=[('ProductID', 'i4'),('ProductName', 'a50')]))

print df

# adding data to data frame
df = df.append({'ProductID':1234, 'ProductName':'a', 'Score':1},ignore_index=True)
df = df.append({'ProductID':1234, 'ProductName':'a', 'Score':2},ignore_index=True)
df = df.append({'ProductID':1234, 'ProductName':'b', 'Score':2},ignore_index=True)
df = df.append({'ProductID':1234, 'ProductName':'b', 'Score':2},ignore_index=True)
print df

# grouping data
print df.groupby('ProductID').agg({'Score': np.mean})

# group multiple data
print df.groupby(['ProductID', 'ProductName']).agg({'Score': np.mean})