import pandas as pd

print(pd.__version__)

A = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(A)
print(A.values)
print(type(A))
print(A['a':'c'])