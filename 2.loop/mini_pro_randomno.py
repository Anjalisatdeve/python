import random
num=random.randint(1,11)
tries=0
while True:
    guess=int(input("Enter a number between 1 and 10: "))
    
    if guess==num:
        tries+=1
        print(f"Congratulations! You guessed the number {num} in {tries} tries.")
        break
    elif guess<num:
        tries+=1
        print("Too low! Try again.")
    elif guess>num:
        tries+=1
        print("Too high! Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 10.")        