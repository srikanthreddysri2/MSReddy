a = int(input("starts from:- "))
b = int(input("to:- "))
c = ('0','2','4','6','8')
d = ('1','3','5','7','9')
while(str(a).endswith(c)):
    print (a)
    a = a+2
    if(a>b):
        break
    continue
while(str(a).endswith(d)):
    print (a+1)
    a = a+2
    if(a>=b):
        break
    continue


