from itertools import count


L = [1,2,4,6,-5,3,7,6,10]

min = L[0]
index = 0
count = 0
for i in L:
    if i<min:
        min = i
        index=count
    count+=1
print(min)
print(index) 