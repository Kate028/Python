"""
Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced.
The clue can be multiples, divisible, greater or smaller, or a combination of all."""

import random
import math

player_name = input("Hello, What can I call you? ")

# take lower value from user
lower_value = int(input("Enter lower value: "))

# take upper value from user
upper_value = int(input("Enter upper value: "))

print("\nOkay! "+ player_name + " Good luck ! ")

# Generating random number between lower and upper value
x = random.randint(lower_value, upper_value)
# The math.log() method returns the natural logarithm of a number, or the logarithm of number to base.

print("\n You've only ", round(math.log(upper_value-lower_value +1, 2)),
      "chances to guess the integer! \n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper_value - lower_value +1 , 2):
    count += 1

# Taking guesses number as input 
    guess = int(input("Guess a number: "))

    # Check the conditions
    if x == guess:
        print("Congrats you got it ", count, "try")

        # once guessed, break the loop else keep on guessing
        break
    elif x > guess:
        print("You guessed too smaall!")
    elif x < guess:
        print("You guessed too high!")

if count >= math.log(upper_value - lower_value +1, 2):    
    print("\n The number is %d" % x) 
    print("\t Better luck next time!")




