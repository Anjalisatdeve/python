a={10:100, 20:200, 30:300, 40:400}
b={30:300, 40:400, 50:500, 60:600}

for i in b:
    if i in a.keys():
        a[i]+=b[i]
    else:
        a[i]=b[i]
        
print(a)