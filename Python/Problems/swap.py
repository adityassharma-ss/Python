def swap(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L

L = [2,3,6,7]

L2 = swap(L,1,3)
print(L2)