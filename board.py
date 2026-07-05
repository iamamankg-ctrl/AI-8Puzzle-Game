class Board:
    def __init__(self):
        self.state = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 0
        ]

    def get_value(self, index):
        return self.state[index]