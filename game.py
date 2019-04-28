

class GameBoard:
    def __int__(self):
        print("Init Board")

    def setup(self):
        print("Setup Board")

    def update(self):
        print("Update Board")

    def clear(self):
        print("Clear Board")


class GameClass:
    def __init__(self):
        pass
        self.game_pieces = {0: "*", 1: "X", 2: "O"}


a = GameBoard()
a.update()

game = GameClass()







