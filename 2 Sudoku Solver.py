def find_empty_location(board):
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == 0:
        return row, col
  return None

def is_valid_placement(board, num, row, col):
  # Check row
  for i in range(len(board[0])):
    if board[row][i] == num and col != i:
      return False

  # Check column
  for i in range(len(board)):
    if board[i][col] == num and row != i:
      return False

  # Check 3x3 box
  box_start_row = row - row % 3
  box_start_col = col - col % 3
  for i in range(box_start_row, box_start_row + 3):
    for j in range(box_start_col, box_start_col + 3):
      if board[i][j] == num and (i, j) != (row, col):
        return False
  return True

def solve(board):
  empty_location = find_empty_location(board)
  if not empty_location:
    return True

  row, col = empty_location
  for i in range(1, 10):
    if is_valid_placement(board, i, row, col):
      board[row][col] = i

      if solve(board):
        return True

      board[row][col] = 0

  return False

def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - -")
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")
      print(board[i][j], end=" ")
    print()


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(board):
  print_board(board)
else:
  print("Board cannot be solved!")
