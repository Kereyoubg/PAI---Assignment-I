class NQueens:
    def __init__(self, n, board):
        self.n = n
        for col in range(n):
            self.solve(board, col)

    def solve(self, board, col):
        if col >= self.n: # complete
            return True

        for row in range(self.n):
            if self.is_safe(board, row, col):
                board[row][col] = 1

                if self.solve(board, col + 1):
                    return True
                board[row][col] = 0
        return False


    def is_safe(self, board, row, col):
        # check column
        for place in range(col):
            if board[row][place] == 1:
                return False

        # check positive diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # check negative diagonal
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

table = [[0 for x in range(4)] for y in range(4)]
lowerDiagonal = [0 for x in range(7)]
upperDiagonal = [0 for x in range(7)]

nq = NQueens(4, table)
print(table)
