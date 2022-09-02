L = [1,2,4,6,-5,3,7,6,10]

for j in range(len(L)):
    m = L[j]
    idx =j
    c =j
    for i in range(j,len(L)):
        if L[i]<m:
            m = L[i]
            idx = c
        c+=1
    tmp = L[j]
    L[j] = m
    L[idx] = tmp

print(L)



        
