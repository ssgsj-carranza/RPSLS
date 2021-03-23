from player import Player
from gestures import Choices


class Human(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self):
        # player2choice = input("Choose gesture ")
        # while player2choice not in Choices().Gesture:
        #     player2choice = input("Please enter valid input ")
        #     return input()
        return input("Choose gesture ")