from curses.ascii import isdigit
import random
userInput = input("Enter a number: ")

if userInput.isdigit():
    userInput = int(userInput)
    
    if userInput <= 0:
        print("Enter a number above 0")
        quit()
else:
    print("Enter a number next time ")
    quit()

randomNumber = random.randrange(userInput)

guesses = 0 
tries = 3
guessCount = 0
while guessCount < tries:
    guesses += 1
    guess = input("guess a number")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number next time")
        continue
    
    if guess == randomNumber:
        print("you got it right")
        break
    else:
        if guess < randomNumber:
            print("you are below the number")
        else:
            print("you are above the number")
    guessCount += 1

if guessCount >= tries:
    print("you ran out of tries")
else:
    print(f"you got it in {guesses} attempts :)")




# print(randomNumber)