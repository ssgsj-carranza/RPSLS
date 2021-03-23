from gestures import Choices
from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self):
        print(f'choose gesture {random.choice(Choices().Gesture)}')