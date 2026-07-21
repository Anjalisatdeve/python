l=[1,67,98,34,9]
largest=l[0]
second_largest=l[0]
for i in l:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i    
print(f"The largest number in the list is {largest}")
print(f"The second largest number in the list is {second_largest}")        