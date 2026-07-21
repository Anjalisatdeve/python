num=int(input("Enter a number:"))
even=0
odd=0
for i in range(1,num+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)