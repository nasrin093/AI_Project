class NQueensSolver:
    def __init__(self, n):
        """
        Initialize the N-Queens Solver with the board size.

        Args:
            n (int): The size of the board (n x n).
        """
        self.n = n
        self.solutions = []

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

    def solve_n_queens_util(self, board, col):
        """
        Utility function to solve the N-Queens problem recursively.

        Args:
            board (list): The current state of the board.
            col (int): The current column index.

        Returns:
            None
        """
        if col >= self.n:
            self.solutions.append([row[:] for row in board])
            return

        for i in range(self.n):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                self.solve_n_queens_util(board, col + 1)
                board[i][col] = 0

    def solve_n_queens(self):
        """
        Solve the N-Queens problem and print the solutions.

        Returns:
            None
        """
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.solve_n_queens_util(board, 0)

        if not self.solutions:
            print("Solution does not exist")
            return

        print("Number of solutions:", len(self.solutions))
        for idx, sol in enumerate(self.solutions, start=1):
            print(f"Solution {idx}:")
            for row in sol:
                print(" ".join(str(cell) for cell in row))
            print()


if __name__ == "__main__":
    N = 4  # Change this to the desired board size
    solver = NQueensSolver(N)
    solver.solve_n_queens()
