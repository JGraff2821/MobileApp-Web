import random

print("Hello! Welcome to Dice Roll!")
doIRoll = True
while(doIRoll):
  DieOne = random.randint(1,6)
  DieTwo = random.randint(1,6)
  print("You rolled a ",DieOne," and a ",DieTwo,". ")
  answer = input("Do you want to roll again? (Y/N) ")
  if(answer=="Y"):
    print("Yay!")
  elif(answer=="N"):
    print("Have a great one!")
    doIRoll = False
  else:
    print("Invalid Input, Have a great one!")
    doIRoll = False
  print("\n")
