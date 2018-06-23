k=[3,4]

L=[1,2,k]

copy = L[:]
othercopy = L.copy()

copy[2][1]='new'
print(L)