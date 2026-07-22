d={1: "one", 2: "two", 3: "three",4:56,5:89,6:"hello"}
print(d)

# accessing values from dictionary
print(d[1]) # output:- one
print(d[2]) # output:- two
print(d[3]) # output:- three

# updating values in dictionary
d[1] = "new one"
print(d[1]) # output:- new one

# deleting values from dictionary
del d[1]    
print(d)  # output:- {2: 'two', 3: 'three', 4: 56, 5: 89, 6: 'hello'}

# traversing dictionary
d1={10:100, 20:200, 30:300, 40:400}
for i in d1:
    print(f"Key: {i}, Value: {d1[i]}")
# output:-  Key: 10, Value: 100
#           Key: 20, Value: 200
#           Key: 30, Value: 300
#           Key: 40, Value: 400
    print(d1[i]) # output:- 100 200 300 400


