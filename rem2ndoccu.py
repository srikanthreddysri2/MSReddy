a = [2,5,9,4,7,2,7,5,3]
b = a.index(7)
c = a.index(7,b+1)
del a[c]
print (a)