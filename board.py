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

    def get_value(self, index):
        return self.state[index]

    def get_empty_index(self):
        return self.state.index(0)

    def move(self, index):
        empty = self.get_empty_index()

        row1, col1 = divmod(index, 3)
        row2, col2 = divmod(empty, 3)

        # Chỉ cho phép di chuyển nếu ô được chọn nằm cạnh ô trống
        if abs(row1 - row2) + abs(col1 - col2) == 1:
            self.state[index], self.state[empty] = (
                self.state[empty],
                self.state[index]
            )

            # Tăng số bước sau khi di chuyển thành công
            self.moves += 1

            return True

        return False

    def shuffle(self):
        for _ in range(100):
            empty = self.get_empty_index()

            row, col = divmod(empty, 3)

            moves = []

            if row > 0:
                moves.append(empty - 3)

            if row < 2:
                moves.append(empty + 3)

            if col > 0:
                moves.append(empty - 1)

            if col < 2:
                moves.append(empty + 1)

            self.move(random.choice(moves))

        # Sau khi xáo trộn thì đưa bộ đếm về 0
        self.moves = 0

    def is_solved(self):
        return self.state == [
            1, 2, 3,
            4, 5, 6,
            7, 8, 0
        ]