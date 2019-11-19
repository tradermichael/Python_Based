# Author: Michael Le
# Date: 10/15/2019
# Description: Asks the user for number, then for guesses. If too high or too low, player will be notified. At the end, number of tries will be printed
correctnumber = int(input("Enter the number for the player to guess.\n"))
Guess = 0
Guess_count = 1
Guess = int(input("Enter your guess.\n"))
while Guess != correctnumber:
    if Guess > correctnumber:
        print("Too high - try again:")
    elif Guess < correctnumber:
        print("Too low - try again:")
    Guess = int(input())
    Guess_count +=1
print("You guessed it in", str(Guess_count), "tries.")