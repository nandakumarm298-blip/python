import pandas as pd
s=pd.Series()
print(s)

import numpy as np
arr=np.array([10,20,30,40,50,60])
S=pd.Series(arr)
print(S)

data={'a':10,'b':20,'c':30}
S=pd.Series(data)
print(S)

S=pd.Series([10,20,30,40,50,60])
print(S[1:4])

x=[10,20,30,40,50]
t=pd.DataFrame(x)
print(t)

data=[{'a':1,'b':2},{'a':2,'b':4,'c':8}]
table=pd.DataFrame(data)
print(table)

import pandas
data={'one':pandas.Series([1,2,3],index=['a','b','c']),'two':pandas.Series([1,2,3,4],index=['a','b','c','d'])}
table=pandas.DataFrame(data)
print(table)

import pandas as pd
# DataFrame add and delete the column
data={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])}
table=pd.DataFrame(data)
table['three']=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(table)

del table['one']
print(table)

table.pop('two')
print(table)


import pandas as pd
# DataFrame add and delete the column
data={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])}
table=pd.DataFrame(data)
table['three']=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(table)

print(table.iloc[2])

# appending the data
# Assuming 'table' is already defined earlier

row=pd.DataFrame([[11,12,13],[14,15,16]],columns=['one','two','three'])
# Use pd.concat to add the new rows
table=pd.concat([table,row],ignore_index=True)
print(table)


table=table.drop(0)
print(table)


import numpy as np
import pandas as pd

df_test = pd.DataFrame(np.random.rand(5, 5),['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z', 'A'])
print(df_test)

print(df_test[['W','A']])

print(df_test.loc['A'])

print(df_test.loc[['A'],['W']])

