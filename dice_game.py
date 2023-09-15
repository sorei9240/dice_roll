import random

minimum_value = 1
maximum_value = 6
name = input("Welcome! What is your name? ")

print(f"Hi {name}, let's play a dice rolling game!")


def roll_dice():
    print("Now rolling...")
    return random.randint(minimum_value, maximum_value)

def play_game():
    while True:
        result = roll_dice()
        print(f"You've rolled a {result}!")

        roll_again = input("Do you want to play again? (yes/no): ").lower()
        if roll_again != "yes":
            break

play_game()
print("Thanks for playing!")
