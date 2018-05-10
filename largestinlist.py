a = [2,4,9,6,7,3,8,11]
large = a[0]
for i in range(len(a)):
    if (a[i] > large):
        large = a[i]
print(large)