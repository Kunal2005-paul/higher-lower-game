import os
from random import randint
from art import logo as LOGO, vs as VS        # importing the 'Higher Lower Game' logo ans 'VS' logo
from game_data import data as DATA      # importing the array of DATA for this game




def unique_choice(prev_option):
    """It returns a unique index which will be selected as a question"""
    while True:
        new_option = randint(0, len(DATA)-1)
        if prev_option != new_option:
            return new_option
        
def show_question(option1, option2):
    """It prints the two selected questions"""
    print(f"Compare A: {DATA[option1]['name']}, a {DATA[option1]['description']}, from {DATA[option1]['country']}")
    print(VS)
    print(f"Compare B: {DATA[option2]['name']}, a {DATA[option2]['description']}, from {DATA[option2]['country']}")

def check_answer(option1, option2):
    """It takes two index of 'DATA' array and returns which 'follower_count' is greater, based on positional arguments"""
    answer1 = DATA[option1]['follower_count']
    answer2 = DATA[option2]['follower_count']
    if answer1 > answer2:
        return "a"
    else:
        return "b"







def game():
    """The main 'Higher Lower Game' function"""
    score = 0
    option1 = randint(0, len(DATA)-1)
    option2 = unique_choice(option1)
    print(LOGO)
    show_question(option1, option2)
    keep_playing = True

    while keep_playing:
        actual_answer = check_answer(option1, option2).lower()
        # print(actual_answer)      # To print the actual answer previously
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        os.system("cls")    # for cleaning the terminal
        print(LOGO)

        if user_answer == actual_answer:
            score += 1
            print(f"You are right! Current score: {score}")
            if actual_answer == "a":
                option2 = unique_choice(option1)
                show_question(option1, option2)
            elif actual_answer == "b":
                option1 = option2
                option2 = unique_choice(option1)
                show_question(option1, option2)
        else:
            print(f"Sorry that's wrong your final score is: {score}")
            break




game()