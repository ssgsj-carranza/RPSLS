from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def get_gesture(self):
        print("Choose gesture")