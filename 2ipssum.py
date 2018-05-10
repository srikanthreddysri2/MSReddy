#import functools
a = [int(x) for x in input().split(",")]
b = [int(y) for y in input().split(" ")]
c = list(map(lambda x, y: x + y, a, b))
# d = ""
# for i in c:
#     print(i)
#     d += (str(i))
# print (d)
print(str(c).replace(" ","").replace(",","@"))