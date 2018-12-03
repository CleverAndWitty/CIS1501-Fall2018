class Maze():
    START = 'S'
    END = 'E'
    WALL = 'W'
    EMPTY = ' '
    DEAD_END = 'X'
    VISITED = '.'

    def __init__(self):
        self.maze = [
            [ 'S', 'W', ' ', ' ', ' ', ' ' ],
            [ ' ', 'W', ' ', 'W', 'W', ' ' ],
            [ ' ', ' ', ' ', ' ', ' ', ' ' ],
            [ ' ', 'W', ' ', 'W', ' ', 'W' ],
            [ ' ', ' ', ' ', 'W', ' ', 'W' ],
            [ ' ', 'W', 'W', 'W', ' ', 'E']
            ]
        self.unsolved = True

    def solve(self):
        self._solve(0, 0)

    def _is_valid_row(self, row):
        return 0 <= row < len(self.maze)

    def _is_valid_column(self, row, col):
        return 0 <= col < len(self.maze[row])

    def _is_open_space(self, row, col):
        return self.maze[row][col] in [Maze.EMPTY, Maze.END]

    def _can_move(self, row, col):
        return self._is_valid_row(row) and self._is_valid_column(row, col) and self._is_open_space(row, col)

    def _solve(self, row, col):
        # Check for Base case and if solved
        if self.maze[row][col] == Maze.END:
            self.unsolved = False
        else:
            self.maze[row][col] = Maze.VISITED

        # Right
        if self.unsolved and self._can_move(row, col + 1):
            self._solve(row, col + 1)

        # Down
        if self.unsolved and self._can_move(row + 1, col):
            self._solve(row + 1, col)

        # Left
        if self.unsolved and self._can_move(row, col - 1):
            self._solve(row, col - 1)

        # Up
        if self.unsolved and self._can_move(row - 1, col):
            self._solve(row - 1, col)

        if self.unsolved:
            self.maze[row][col] = Maze.DEAD_END

    def __str__(self):
        return "\n".join(str(row) for row in self.maze)


maze = Maze()
maze.solve()
print(maze)