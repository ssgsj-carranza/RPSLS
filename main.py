from run_game import RunGame
from gestures import Choices
from human import Human
from comphuman import Computer

if __name__ == '__main__':

    run_game = RunGame().run_gesture()
    player1 = Computer()
    player2 = Human()
    print(Choices().Gesture)
    print()
    RunGame().run_game(player1, player2)
    game_gesture = Choices().show_choices()