l=[2,6,9,1,78,45,23,90,65,32]
max=l[0]
index=0
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
        index=i
print(f"The largest number in the list is {max}")
print("The index of largest element is ",index)
