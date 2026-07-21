a="csdsgvdldg@#787253bdjhdyg"
digit=0
char=0
symbol=0
for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1 
    else:
        symbol+=1

print("Total digits:",digit)
print("Total characters:",char)
print("Total symbols:",symbol)        
        