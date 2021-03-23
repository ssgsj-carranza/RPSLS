class Gesture:
    def __init__(self):
        self.choice1 = "rock"
        self.choice2 = "paper"
        self.choice3 = "scissors"
        self.choice4 = "lizard"
        self.choice5 = "spock"


class Choices:
    def __init__(self):
        self.Gesture = list()
        self.Gesture += ["rock", "paper", "scissors", "lizard", "spock"]

    def is_valid(self, correct_value):
        if correct_value in self.Gesture:
            return True
        else:

            return False

    def show_choices(self):
        print(self.Gesture)



