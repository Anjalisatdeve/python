fruits = ["apple","banana", "cherry", "date", "elderberry"]
print("By mannualyy printing the elements of the list")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

print("By using for loop to print the elements of the list")
for i in range(len(fruits)):
    print(fruits[i])

print("By using for loop to print the elements of the list directly")
for i in fruits:
    print(i)    


print("print by sclicing the list")
print(fruits[0:3])
print(fruits[1:4])