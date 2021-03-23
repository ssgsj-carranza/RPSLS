from player import Player
from human import Human
from comphuman import Computer

class RunGame:

    def run_gesture(self):
        self.welcome_message()
        self.display_rules()
        # self.choose_gesture()

    def welcome_message(self):
        input("Welcome to RPSLS! Press enter to start")
        print()

    def display_rules(self):
        print("Choose your gesture, best out of 3")


    def run_game(self, player1, player2 ):
        while player1.rounds_won < 3 and player2.rounds_won < 3:
            player1choice = player1.get_gesture()
            player2choice = player2.get_gesture()
            if player1choice == player2choice:
                print(f'Both users selected {player1choice}. Draw')
            elif player2choice == "rock":
                if player1choice == "scissors" or "lizard":
                    print("You win")
                    player2.rounds_won += 1
                else:
                    print("You lose..")
            elif player2choice == "paper":
                if player1choice == "rock" or "spock":
                    print("You win")
                    player2.rounds_won += 1
                else:
                    print("You lose..")
            elif player2choice == "scissors":
                if player1choice == "paper" or "lizard":
                    print("You win")
                    player2.rounds_won +=1
                else:
                    print("You lose..")
            elif player2choice == "lizard":
                if player1choice == "paper" or "spock":
                    print("You win")
                    player2.rounds_won += 1
                else:
                    print("You lose..")
            elif player2choice == "spock":
                if player1choice == "scissors" or "rock":
                    print("You win")
                    player2.rounds_won += 1
                else:
                    print("You lose..")

# def choose_gesture(self):
#     print("select from list of gestures")