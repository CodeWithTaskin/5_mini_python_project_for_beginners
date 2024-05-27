import random as r
num = r.randint(1,20)

guessCount = 0
while True:
    guessNum = int(input("Guess a number: "))
    if num > guessNum:
        print("Higher")
        guessCount += 1
    elif num < guessNum:
        print("Lower")
        guessCount += 1
    else:
        print("Currect Guess")
        print(f"You take {guessCount} times to guess the Answer")
        break