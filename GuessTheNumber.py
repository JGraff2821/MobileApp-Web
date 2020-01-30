import random
def numberFilter(guess):
  if(int(guess)>=0 and int(guess) <=1000):
    return True
  else:
    return False

def userHint(guess, answer):
  Guess = int(guess)
  Answer = int (answer)
  if(Guess == Answer):
    print("Congrats! You got it!")
    return 0
  elif(Guess<Answer):
    print("Your answer was low...")
    return -1
  elif(Guess>Answer):
    print("Your answer was high...")
    return 1

print("Hello! Welcome to Guess the Number! The answe will range from 0-100, good luck!")
Continue = True
Answer =(random.randint(0,100))
while(Continue):
  Guess = input("What is your guess? ")
  if(numberFilter(Guess)):
    hint = userHint(Guess,Answer)
    if(hint == 0):
      Continue = False
  else:
    print("Your guess was not within the bounds (Numbers 0-100)")
