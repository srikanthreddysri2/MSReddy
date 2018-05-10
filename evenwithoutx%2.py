a = int(input("starts from:- "))
b = int(input("to:- "))
c = ('0','2','4','6','8')
for i in range(a,b+1):
    d = str(i)
    if(d.endswith(c)):
        print (i)