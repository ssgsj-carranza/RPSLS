from run_game import RunGame
from gestures import Choices

if __name__ == '__main__':
    run_game = RunGame().run_gesture()
    game_gesture = Choices().show_choices()