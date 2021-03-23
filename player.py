from gestures import Choices


class User():
    def __init__(self):
        super().__init__()

    def make_choice(self):
        user_action = Choices().Gesture()
        print(f'user chose {user_action}')
        if computer_action == user_action:
            print(f'Both users selected {user_action}. Draw')
        elif computer_action == "rock":
            if user_action == "scissors" or "lizard":
                print("You win")
            else:
                print("You lose..")
        elif computer_action == "paper":
            if user_action == "rock" or "spock":
                print("You win")
            else:
                print("You lose..")
        elif computer_action == "scissors":
            if user_action == "paper" or "lizard":
                print("You win")
            else:
                print("You lose..")
        elif computer_action == "lizard":
            if user_action == "paper" or "spock":
                print("You win")
            else:
                print("You lose..")
        elif computer_action == "spock":
            if user_action == "scissors" or "rock":
                print("You win")
            else:
                print("You lose..")





