import numpy as np

A = np.round(10*np.random.rand(2,3))

print(A)

print(A+3)

print(A+(np.arange(2).reshape(2,1)))

A= np.random.permutation(np.arange(10))

print(A)

print(np.sort(A))

A = A[::-1]
print(A) 