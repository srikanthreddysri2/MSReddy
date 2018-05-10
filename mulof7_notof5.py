a = []
b = range(1000, 3000)
for x in b:
    if (x % 7 == 0) and (x % 5 != 0):
        a.append(x)
print (a)
