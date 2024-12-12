# a shorter solution

import random
from game_data import data

WINNER = ""
SCORE = 0
TURNS = 5
USER_CHOICE = ""


def options():
    first_option = random.choice(data)
    second_option = random.choice(data)
    while first_option == second_option:
        second_option = random.choice(data)
    return [first_option, second_option]


def evaluate_choice(WINNER, answer):
    if answer == WINNER:
        return True
    else:
        return False


while TURNS > 0:
    option_1 = options()[0]
    option_2 = options()[1]
    print(f"Compare A: {option_1['name']}, a {option_1['description']}, from {option_1['country']}"
          f"\nVS.\nB: {option_2['name']}, a {option_2['description']}, "
          f"from {option_2['country']}.")
    loop = True
    while loop:
        USER_CHOICE = input("Who has more followers? Type 'A' or 'B': ").upper()
        if USER_CHOICE == 'A' or USER_CHOICE == 'B':
            if option_1['follower_count'] > option_2['follower_count']:
                WINNER = "A"
                loop = False
                break
            elif option_2['follower_count'] > option_1['follower_count']:
                WINNER = "B"
                loop = False
                break
        else:
            print("That is not a valid answer.")
    if evaluate_choice(WINNER, USER_CHOICE):
        SCORE += 1
        print(f"You're right! Current score: {SCORE}/5")
    else:
        print(f"That is incorrect. Current score: {SCORE}/5.")
    TURNS -= 1
print(f"Your final score is {SCORE}/5.")
