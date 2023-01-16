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
            print("Self-destruct in T-10 seconds.")

            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)  # This loop counts down from 10 every second before closing out of the terminal

            print("Self-destruction emanate, Good-bye.")
            time.sleep(1)

            break  # This tells the file that the program is finished and can be closed out.
else:
    print("Have a good day!")
    print("Self-destruct in T-10 seconds.")

    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)  # This loop counts down from 10 every second before closing out of the terminal

    print("Self-destruction emanate, Good-bye.")
    time.sleep(1)
    # but also now works as a break because it is the last thing in the file to run
    # So it closes out Automatically.
