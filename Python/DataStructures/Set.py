S = {1,3,4.9,"name",3}
print(type(S))

print(3 in S)
S.add(56)
print(S)
S.update({23,"game",1})
print(S)
S.remove('game')
print(S)


S2 = {x**2 for x in range(2,20,3)}
print(S2)

print(32 in S2)