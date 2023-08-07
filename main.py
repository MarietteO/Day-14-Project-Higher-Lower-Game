import random
from art import logo
from game_data import data

SCORE = 0

def choose_items():
    """Choose two distinct items from the data."""
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    if choice_b != choice_a:
        return [choice_a, choice_b]
    else:
        return choose_items()

def ask_input(choice_items):
    """Ask the user to compare two items and get their guess."""
    choice_a = choice_items[0]
    choice_b = choice_items[1]
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print("VS.")
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    return [guess]

def compare_items(random_items):
    """Compare the follower counts of two items and determine the winner."""
    follower_list = [item['follower_count'] for item in random_items]
    choice_a_follower = follower_list[0]
    choice_b_follower = follower_list[1]
    if choice_a_follower > choice_b_follower:
        return ['a', choice_a_follower]
    else:
        return ['b', choice_b_follower]

def evaluate_user_answer(correct_answer, user_answer):
    """Check if the user's answer matches the correct answer."""
    if user_answer == correct_answer:
        return True
    else:
        return False

def adjust_score():
    """Increase the global score by 1."""
    global SCORE
    SCORE += 1
    return SCORE

def switch_items(chosen_items):
    """Switch one of the items while keeping the other item."""
    choice_a = chosen_items[1]
    choice_b = random.choice(data)
    return [choice_a, choice_b]

# Display the game logo
print(logo)

# Choose the initial items for the game
items = choose_items()

# Start the game loop
game = True
while game:
    # Ask the user for input and compare items
    user_guess = ask_input(items)
    winning_list = compare_items(items)
    winning_item = winning_list[0].split()
    
    # Evaluate user's answer and update score accordingly
    if evaluate_user_answer(winning_item, user_guess):
        adjust_score()
        print(f"You're right! Current score: {SCORE}")
        items = switch_items(items)
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        game = False  # End the game loop
