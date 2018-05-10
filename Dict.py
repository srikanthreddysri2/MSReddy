a = {"net_username":"Username1" , "net_password":"password1" , "net_host":"host1"}
b = {"net.username":"Username2" , "net.password":"password2" , "net.host":"host2"}
c = {}
for y in b.keys():
    for x in a.keys():
        a[x] = b[y]
print(a)