from players import Players
from gestures import Choices
import random

class Computer:
    def __init__(self):
        super().__init__()

    def make_choice(self):
        computer_action = random.choice([Choices])
        print(f'computer chose {computer_action}')
        if user_action == computer_action:
            print(f'Both users selected {user_action}. Draw')
        elif user_action == "rock":
            if computer_action == "scissors" or "lizard":
                print("You win")
            else:
                print("You lose..")
        elif user_action == "paper":
            if computer_action == "rock" or "spock":
                print("You win")
            else:
                print("You lose..")
        elif user_action == "scissors":
            if computer_action == "paper" or "lizard":
                print("You win")
            else:
                print("You lose..")
        elif user_action == "lizard":
            if computer_action == "paper" or "spock":
                print("You win")
            else:
                print("You lose..")
        elif user_action == "spock"
            if computer_action == "scissors" or "rock":
                print("You win")
            else:
                print("You lose..")