# print("start")
# print(10/0)
# print("end")
# error: ZeroDivisionError: division by zero start print hoonga lekin end print nahi hoga because error aayega and program terminate ho jaayega

# how to error handling in python

"""a=int(input("Enter a number: "))
try:
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("end")"""
# by this type hmm error handle kr skte  h
"""output:-Enter a number: 0
       Error: Division by zero is not allowed.
       end"""
"""output:-Enter a number: 1
       10.0
       end"""

# hrr time nhi pta honga ki konsa error aayega so for this
"""a=int(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an err as {err}")

print("end")
"""
"""output:Enter a number: 0
          Sorry there is an err as division by zero
          end"""
# yha bta diya isne ki konsa error h

# how to use else
# if error nhi aya error wale staments ke bdle else wala statement print honga
"""a=int(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an err as {err}")
else:
    print("Thier is no expection")    

print("end")"""
"""Enter a number: 3
3.3333333333333335
Thier is no expection
end"""
"""Enter a number: 0
Sorry there is an err as division by zero
end"""

# use of finally
# code m error rhe ya nhi rhe ye finally m jo rhega vo chlega hi
"""a=int(input("Enter a number: "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an err as {err}")
else:
    print("Thier is no expection") 
finally:
    print("I will run no matter what!")       

print("end")"""
"""Enter a number: 0
Sorry there is an err as division by zero
I will run no matter what!
end"""
"""Enter a number: 10
1.0
Thier is no expection
I will run no matter what!
end"""

# raise:-khud se error raise krna
age=int(input("Tell your age:- "))
if age<10 or age>18:
    raise ValueError("your age must be betwwen 10 & 18")
else:
    print("Welcome to the clud")
# yese khud error bhej skt h
"""Tell your age:- 7
   Traceback (most recent call last):
   File "c:\Users\riyas\OneDrive\Desktop\DA\8.Exception_handling\error.py", line 82, in <module>
   raise ValueError("your age must be betwwen 10 & 18")
   ValueError: your age must be betwwen 10 & 18    """