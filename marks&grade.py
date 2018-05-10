a = int(input("enter 1st subject marks:- "))
b = int(input("enter 2nd subject marks:- "))
c = int(input("enter 3rd subject marks:- "))
d = int(input("enter 4th subject marks:- "))
e = int(input("enter 5th subject marks:- "))
s = (a+b+c+d+e)
print("Total marks secured:- "+str(s))
p = s/5
print("percentage obtained:- "+str(p))
if(p > 60):
    print ("First Class, grade 'A'")
if(p<60 and p>50):
    print("Second class, grade 'B'")
if(p<50 and p>40):
    print("Third class, grade 'C'")
if(p<40):
    print("Failed in exams")