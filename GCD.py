a = int(input("enter first number: "))
b = int(input("enter second number: "))
x = 1
temp = x
if(a>0 and b>0):
    if(a>b):
        for i in range(2,b+1):
            if(a%i == 0):
                if(b%i == 0):
                    temp = x*i
                    continue
                continue
            continue
    else:
        for i in range(2,a+1):
            if(a%i == 0):
                if(b%i == 0):
                    temp = x*i
                    continue
                continue
            continue
print(temp)