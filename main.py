from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or hard:")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



# function to check user's guess against actual answer.


def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! the answer is {answer}")


# choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"The answer is {answer}")

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number")



# make function to set difficulty.



# let the user guess a number.
guess = int(input("Make a guess: "))

# track the number of turns and reduce by 1 if they get it wrong.

# repeat the guessing functionality if they get it wrong.
