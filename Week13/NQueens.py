class NQueens:

    def __init__(self, size):
        self.board = []
        self.size = size
        self.number_of_queens = 0
        self.is_solved = False
        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append(" ")

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    def _is_row_open(self, row):
        return 'Q' not in self.board[row]

    def _is_diagonal_up_open(self,row, column):
        row -= 1
        column -= 1
        while row >= 0 and column >= 0:
            if self.board[row][column] == "Q":
                return False
            row -= 1
            column -= 1
        return True

    def _is_diagonal_down_open(self,row, column):
        row += 1
        column -= 1
        while row < len(self.board) and column >= 0:
            if self.board[row][column] == "Q":
                return False
            row += 1
            column -= 1
        return True

    def _can_place_queen(self, row, column):
        return self._is_row_open(row) and \
            self._is_diagonal_up_open(row, column) and \
            self._is_diagonal_down_open(row, column)

    def solve(self):
        if self.is_solved or self.number_of_queens == self.size:
            self.is_solved = True
            return
        for row in range(self.size):
            if not self.is_solved and self._can_place_queen(row, self.number_of_queens):
                self.board[row][self.number_of_queens] = 'Q'
                self.number_of_queens += 1
                self.solve()
                if not self.is_solved:
                    self.number_of_queens -= 1
                    self.board[row][self.number_of_queens] = ' '

puzzle = NQueens(20)
puzzle.solve()
print(puzzle)