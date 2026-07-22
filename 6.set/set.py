s={1,2,3,4,5,5,4}
print(s)
#output:- {1, 2, 3, 4, 5} duplicates nhi deti

# print(s[0]) # ye error dega kyuki set me index nhi hota

s1=hash("hello")
print(s1) 
# output:-5645190365099968764 hash value denga

# set traversing
a={1,8,9,2,4,7,3}
for i in a:
    print(i)
#output:yese sequence me print hoga
# 1
# 2
# 3
# 4
# 7
# 8
# 9  

# set methods
s2={1,2,3,4,5}
s2.add(6)
print(s2) 
# output:- {1, 2, 3, 4, 5, 6} add method se element add hoga

s3={1,2,3,4,5}
s3.remove(2)
print(s3)
# output:- {1, 3, 4, 5} remove method se element remove hoga

s4={1,2,3,4,5}
s4.discard(3)
print(s4)
# output:- {1, 2, 4, 5} discard method se element remove hoga, lekin agar element exist nhi karta to error nhi dega

s5={1,2,3,4,5}
s5.pop()
print(s5)
# output:- {2, 3, 4, 5} pop method se random element remove hoga, lekin ye last element remove nhi karta, ye random element remove karta hai  
