from player import Player
from gestures import Choices


class Human(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self):
        # player2choice = input("Choose gesture ")
        # while player2choice not in Choices().Gesture:
        #     input("Please enter valid gesture ")
        # if input is Choices().Gesture:
        #     return input("Choose gesture")
        return input("Choose gesture ")