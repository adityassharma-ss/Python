import numpy as np
import matplotlib.pyplot as plt

A = np.arange(1, 100)
print(A)

A = np.arange(1, 100,3)
print(A)

print(range(10))


print(list(range(10)))

A=np.random.permutation(np.arange(10))
print(A)

print(np.random.randint(20,100))

print(plt.hist(A,bins=100))

D = np.arange(100).reshape(4,25)
print(D)
(print(D.shape ))