import random


class Board:
    def __init__(self):
        self.state = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 0
        ]

        # Đếm số bước đi
        self.moves = 0

    # Lấy giá trị tại vị trí index
    def get_value(self, index):
        return self.state[index]

    # Lấy vị trí ô trống
    def get_empty_index(self):
        return self.state.index(0)

    # Di chuyển một ô
    def move(self, index):
        empty = self.get_empty_index()

        row1, col1 = divmod(index, 3)
        row2, col2 = divmod(empty, 3)

        # Chỉ cho phép di chuyển nếu ô nằm cạnh ô trống
        if abs(row1 - row2) + abs(col1 - col2) == 1:

            self.state[index], self.state[empty] = (
                self.state[empty],
                self.state[index]
            )

            self.moves += 1
            return True

        return False

    # Xáo trộn bàn cờ
    def shuffle(self):

        for _ in range(100):

            empty = self.get_empty_index()

            row, col = divmod(empty, 3)

            possible = []

            if row > 0:
                possible.append(empty - 3)

            if row < 2:
                possible.append(empty + 3)

            if col > 0:
                possible.append(empty - 1)

            if col < 2:
                possible.append(empty + 1)

            move = random.choice(possible)

            self.state[empty], self.state[move] = (
                self.state[move],
                self.state[empty]
            )

        self.moves = 0

    # Kiểm tra chiến thắng
    def is_solved(self):
        return self.state == [
            1, 2, 3,
            4, 5, 6,
            7, 8, 0
        ]

    # ======================
    # Dành cho AI Solver
    # ======================

    # Lấy trạng thái hiện tại
    def get_state(self):
        return tuple(self.state)

    # Gán trạng thái mới
    def set_state(self, state):
        self.state = list(state)