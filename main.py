from run_game import RunGame
from gestures import Choices
from human import Human
from comphuman import Computer

if __name__ == '__main__':

    run_game = RunGame().run_gesture()
    player1 = Computer()
    player2 = Human()
    correct_value = Choices()
    print(Choices().Gesture)
    print()
    RunGame().run_game(player1, player2)
    # game_gesture = Choices().show_choices()
    Choices().is_valid(correct_value)
    RunGame().winner(player1, player2)
print("\n---------------\n")

