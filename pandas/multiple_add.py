import pandas as pd
import numpy as np


# initatilize
df=pd.DataFrame(np.zeros(0,dtype=[('ProductID', 'i4'),('ProductName', 'a50')]))

print df

rows_list = []

dict1 = {}
dict1['ProductID'] = 123
dict1['ProductName'] = '12313'
dict1['Score'] = 4554

dict2 = {}
dict2['ProductID'] = 456
dict2['ProductName'] = '213231'
dict2['Score'] = 3232

rows_list.append(dict1)
rows_list.append(dict2)



df = pd.DataFrame(rows_list)     
print df