a = [4, 7, 5, 6, 1, 2, 10]
b = [2, 5, 4, 1, 7, 11, 12]
d = []
e = []
f = []
a.sort()
for x in range(len(a)):
    i = [1,x]
    d.append(i)
for y in range(len(b)):
    j = [0,y]
    e.append(j)
g = (d+e)
for z in range(len(g)):
    h = g[z][1]
    f.append(h)
print (f)
