import random

target=random.randint(1,100)

print("..Game started...")

while(True):
    user_choice=input("Guess the target or Quit(Q): ")
    if(user_choice=="Q"): 
        break

    user_choice=int(user_choice)
    if(user_choice==target):
        print("Sucess: Correct Guess !!")
        break
    elif(user_choice<target):
        print("Your number is too small. Take a bigger guess..,")
        print("\n")
    else:
        print("Your number is too big. Take a smaller guess...")
        print("\n")


print("-------GAME OVER-------")