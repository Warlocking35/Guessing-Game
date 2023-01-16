import random
import time
# This tells us what the number range is for us to guess in
answer = random.randint(1, 100)
choose = input("Would you like to play a guessing game? 'Yes' or 'No': ")

# This loop is the game itself allowing us to guess numbers between 1 and 100
if choose == "Yes":
    print("Please guess a number between 1 and 100: ")
    guess = int(input())
    while True:
        if guess < answer:
            print("Please guess higher")
            guess = int(input())

        elif guess > answer:
            print("Please guess lower")
            guess = int(input())

        else:
            print("Good job! You guessed it correctly!")
            print("Automatic close in T-10 seconds.")
            time.sleep(10) # This will tell the file to stop running for 10 seconds
            break # This tells the file that the program is finished and can be closed out.
else:
    print("Have a good day!")
    print("Automatic close in T-10 seconds.")
    time.sleep(10) # This is the same as the last sleep, 
    # but also now works as a break because it is the last thing in the file to run
    # So it closes out Automatically. 
