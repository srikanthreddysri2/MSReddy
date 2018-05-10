a = ['Maddula','Srikanth','Reddy']
b = []
g = []
for i in range(len(a)):
    c = str(len(a[i]))
    d = (c+a[i])
    b.append(d)
b.sort()
for j in range(len(b)):
    e = b[j][1:]
    g.append(e)
print (g)