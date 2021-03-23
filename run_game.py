from player import Player
from human import Human
from comphuman import Computer
from gestures import Choices

class RunGame:

    def run_gesture(self):
        self.welcome_message()
        self.display_rules()
        # self.choose_gesture()

    def welcome_message(self):
        input("Welcome to RPSLS! Press enter to play")
        print()

    def display_rules(self):
        print("Choose your gesture, best out of 3")

    def run_game(self, player1, player2):
        while player1.rounds_won < 3 and player2.rounds_won < 3:
            player1choice = player1.get_gesture()
            player2choice = player2.get_gesture()
            if player1choice == player2choice:
                print(f'Both users selected {player1choice}. Draw')
            if player1choice and player2choice not in Choices().Gesture:
                print("Enter valid gesture")
            elif player2choice == "rock":
                if player1choice == "scissors" or player1choice == "lizard":
                    print(f'You win {player2choice} beats {player1choice}')
                    player2.rounds_won += 1
                elif player1choice == "spock" or player1choice == "paper":
                    print(f'You lost..{player1choice} beats {player2choice}')
                    player1.rounds_won += 1
            elif player2choice == "paper":
                if player1choice == "rock" or player1choice == "spock":
                    print(f'You win {player2choice} beats {player1choice}')
                    player2.rounds_won += 1
                elif player1choice == "scissors" or player1choice == "lizard":
                    print(f'You lost..{player1choice} beats {player2choice}')
                    player1.rounds_won += 1
            elif player2choice == "scissors":
                if player1choice == "paper" or player1choice == "lizard":
                    print(f'You win {player2choice} beats {player1choice}')
                    player2.rounds_won += 1
                elif player1choice == "rock" or player1choice == "spock":
                    print(f'You lost..{player1choice} beats {player2choice}')
                    player1.rounds_won += 1
            elif player2choice == "lizard":
                if player1choice == "paper" or player1choice == "spock":
                    print(f'You win {player2choice} beats {player1choice}')
                    player2.rounds_won += 1
                elif player1choice == "scissors" or player1choice == "rock":
                    print(f'You lost..{player1choice} beats {player2choice}')
                    player1.rounds_won += 1
            elif player2choice == "spock":
                if player1choice == "scissors" or player1choice == "rock":
                    print(f'You win {player2choice} beats {player1choice}')
                    player2.rounds_won += 1
                elif player1choice == "paper" or player1choice == "lizard":
                    print(f'You lost..{player1choice} beats {player2choice}')
                    player1.rounds_won += 1

    def winner(self, player1, player2):
        if player1.rounds_won == 3:
            print(f'{player1} wins')
        else:
            print(f'{player2} wins')


print("\n---------------\n")


    # def play_again(self):
    #     replay = input("Play again? (y/n)").lower()
    #     while replay != "y" and replay != "n":
    #         replay = input("Please enter valid input: ").lower()
    #         if replay == "n":
    #             break


# def choose_gesture(self):
#     print("select from list of gestures")