a = int(input("enter any number:- "))
temp = a
rev = 0
while(temp>0):
    r = temp % 10
    rev = (rev * 10)+ r
    temp = temp // 10
print(rev)
if(a == rev):
    print("given number is palindrome")
else:
    print("given number is not a palindrome")