from computer import Computer
from player import User

class Players:
    def __init__(self, user_action, computer_action):
        self.player = user_action
        self.computer = computer_action

    def user_choice(self):
        user_action = input("Enter a choice")
        return user_action


    def comp_choice(self):
        computer_action = input("Choose gesture")
        return computer_action








# welcome message
# display rules
#ask user to select gesture
#guesture round first to win 2
#ask user to reselect gesture
#end game
#display winner
