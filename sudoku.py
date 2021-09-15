BOARD_FILE = "board2.txt"

def read_board():
    # Reads the board from a file as a string and splits it up
    # into a list of lists with each row being a list.
    with open(BOARD_FILE, 'r') as f:
        from_file = f.read()
    
    from_file = from_file.split("\n")
    board = []

    for row in from_file:
        r = [int(i) for i in row]
        board.append(r)
    
    return board

def solve(board):
    # Solves the sudoku puzzle

    # Finds the next empty square on the board
    row, col = get_empty(board)

    if row is None:
        # Solved!
        pass

def possible():
    # Checks if the value can be entered in the square
    pass

def get_empty(board):
    # Returns the next empty square on the board
    # Returns None if there is no more empty squares
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0:
                return y, x
    
    return None, None

def main():
    board = read_board()
    solve(board)

if __name__ == "__main__":
    main()