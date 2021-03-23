from gestures import Choices
from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self):
        computer_choice = random.choice(Choices().Gesture)
        print('computer chose....')
        return computer_choice