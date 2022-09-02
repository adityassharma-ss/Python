import numpy as np
import numpy.linalg as la # linear algebra library

A = np.arange(100)

b = A[3:10]
print(b)

b[0] = -1200

print(b) 

b = A[3:10].copy()

idx = np.argwhere(A==-1200)[0][0]
print(idx)

E = (np.round(10*np.random.rand(5,4)))
print(E)
print(E[1,2])
print(E[1,:])

print(la.inv(np.random.rand(3,3)))

print(E.sort(axis=1))



# print[A::5]

B = (A==-1200)*np.arange(A.size)
print(A.indices(-1200))

