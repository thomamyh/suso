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
    pass

def possible():
    # Checks if the value can be entered in the square
    pass

def get_empty():
    # Returns the next empty square on the board
    pass

def main():
    board = read_board()
    print(board)

if __name__ == "__main__":
    main()