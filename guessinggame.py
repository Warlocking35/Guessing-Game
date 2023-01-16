import random
answer = random.randint(1, 100)
choose = input("Would you like to play a guessing game? 'Yes' or 'No': ")


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
            break
else:
    print("Have a good day!")
