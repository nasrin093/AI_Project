class NQueensSolver:
    def __init__(self, n):
        """
        Initialize the N-Queens Solver with the board size.

        Args:
            n (int): The size of the board (n x n).
        """
        self.n = n
        self.solutions = set()

    def is_safe(self, board, row, col):
        """
        Check if it's safe to place a queen at the given position.

        Args:
            board (list): The current state of the board.
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def apply_rule(self, board, row, col):
        """
        Apply the rule to place a queen at the given position.

        Args:
            board (list): The current state of the board.
            row (int): The row index to place the queen.
            col (int): The column index to place the queen.

        Returns:
            None
        """
        board[row][col] = 1

    def remove_rule(self, board, row, col):
        """
        Remove the rule for placing a queen at the given position.

        Args:
            board (list): The current state of the board.
            row (int): The row index to remove the queen.
            col (int): The column index to remove the queen.

        Returns:
            None
        """
        board[row][col] = 0

    def backtrack(self, board, col):
        """
        Perform backtracking to find all solutions of the N-Queens problem.

        Args:
            board (list): The current state of the board.
            col (int): The current column index.

        Returns:
            None
        """
        if col >= self.n:
            solution = tuple(tuple(row) for row in board)  # Convert board to hashable tuple
            self.solutions.add(solution)
            return

        for row in range(self.n):
            if self.is_safe(board, row, col):
                self.apply_rule(board, row, col)
                self.backtrack(board, col + 1)
                self.remove_rule(board, row, col)

    def solve_n_queens(self):
        """
        Solve the N-Queens problem and print the solutions.

        Returns:
            None
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.backtrack(board, 0)

        if not self.solutions:
            print("No solution exists.")
        else:
            print("Number of solutions:", len(self.solutions))
            for idx, solution in enumerate(self.solutions, start=1):
                print("Solution", idx, ":")
                for row in solution:
                    print(row)
                print()


if __name__ == "__main__":
    N = 4  # Change this to the desired board size
    solver = NQueensSolver(N)
    solver.solve_n_queens()
