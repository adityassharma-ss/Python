D = {23: "twothree", 'B':43, 'C':'CCD'}
print(type(D))

print(D[23])

D['newKey'] = "newValue"

print(D)

D2 = {"y":"YY","z":10}
D.update(D2)
print(D2)
print(D)

print(D.items())