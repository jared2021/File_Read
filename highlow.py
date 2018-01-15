#Have a variable for a randomly generated number
import random
#random.randrange(1,101) = randomly_generated_number
randomly_generated_number = random.randrange(1,101)
guessNum=0
print("I have a number between 1 and 100 take a guess, and I will tell you if you are too high, too low, or correct.")
keepGoing=True
while keepGoing:
    inputed_number=int(input())
    if inputed_number > randomly_generated_number:
        print("Too high.")
        guessNum=guessNum + 1
    elif inputed_number<randomly_generated_number:
        print("Too low.")
        guessNum=guessNum +1
    else:
        print("Correct")
        print(guessNum)
        keepGoing=False
#Have a variable for the number of guesses taken
#Have a variable for the inputed number
#print instructions for the game
#repeat through the following steps until our variable inputed number is equal to the variable randomly generated number
#ask for user input for the inputed number variable
#set user input as variable for inputed number
#if variable inputed number is greater than variable randomly generated number print too high
#if variable inputed number is less than variable randomly generated number print too low
#if variable inputed number is equal to the variable randomly generated number print you got it
#use >= as greater than equal to;<= as less than equal to; use== to check for equality
#increment the number of guesses(add one to the variable number of guesses)
#x++ means to increment (increase by one)the variable x or just say x=x+1 and store it as x
#stop loop if variable inputed number is equal to the variable randomly generated number
#print the number of turns it took to complete the game