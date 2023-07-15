import random
from high_art import logo, vs
from high_game_data import data

# generate a random account from the game data
def random_account_data():
    return random.choice(data)

# format the random account for the user
def format_data(account):
    """format the random account and return th formatted data to thr user """
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

# check the user guess if its correct
def check_guess(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

# Display the logo
def play_game():
    print(logo)
    scores = 0
    should_continue = True
    a_account = random_account_data()
    b_account = random_account_data()
    

    # allow the user to continue playing if they guess right
    while should_continue:
        a_account = b_account
        b_account = random_account_data()

        # checking if they both have same generated data and re-generate if that true
        while a_account == b_account:
            b_account = random_account_data()
        # print the random acount for the user to compare with from the genrated data
        print(f"Compare A: {format_data(a_account)}")
        print(vs)
        print(f"Against B: {format_data(b_account)}")
        # Allow the user to guess the account with the highest follower
        user_guess = input("Who has more follower? Type 'A' or 'B': ").lower()
        a_follower_count = a_account['follower_count']
        b_follower_count = b_account['follower_count']
        answer = check_guess(user_guess, a_follower_count, b_follower_count)

        # if the user guess right their score should increase
        if answer:
            scores += 1
            # track the user score and display its if they guess right
            print(f"You're right! Current score: {scores}")
            
            # if the user guess wrong the programe stop and display their final scores
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {scores}")

play_game()
    
  