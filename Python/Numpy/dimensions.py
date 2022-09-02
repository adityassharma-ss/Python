import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.ndim)

b = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(b.ndim)

print(b.shape[0],b.shape[1],b.shape[2])

print(b[1,0,2])

B = np.array([[1,2,3,-1],[2,4,5,9]])
print(B.ndim)

print(B[1,2])

C = np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])

print(C.ndim)

print(C[1,0,2])
print(type(C))

print(C.shape)

A = np.array([2])
print(A.ndim)

B = np.array(3)
print(B.ndim)

print(C.size)
print(C.nbytes)