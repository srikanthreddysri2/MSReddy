a = [1,2,3,4,1,1,5,2,3,1,3,2]
b = set(a)
c = list(b)
count = 0
for i in range(len(c)):
    for j in range(len(a)):
        if(c[i] == a[j]):
            count += 1
    if(count > 1):
        print("element "+str(c[i])+" is repeated "+ str(count)+" times in the list [a]")
    count = 0