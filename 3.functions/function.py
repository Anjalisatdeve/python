a=8
print(a)
def my_function():
    b=5
    print(b)
my_function()

def my_function2(name):
    print("Hello " + name)
my_function2("Alice")

def sum(a,b=9):
    print(f"The sum of {a} and {b} is {a+b}")
sum(3,4)   
sum(7) 

def pallindrome(word):
    rev = " "
    for i in range(len(word)-1,-1,-1):
        rev = rev + word[i]
    if rev == word:
        print(f"{word} is a pallindrome")
    else:
        print(f"{word} is not a pallindrome")
pallindrome("madam")
pallindrome("hello")        


