# Defining the board as a list of lists
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define the function to print the board
def print_board():
    print("  0  1  2")
    print("0 " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print(" ---+---+---")
    print("1 " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print(" ---+---+---")
    print("2 " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

# Defining the function to check if the game is over and player has won
def check_win(player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:     
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:   
        return True

    # No win
    return False

# Defining a function to check if the board is full
def check_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# Define players
players = ["X", "O"]
current_player = 0  # Initialize current player

# Game loop setup
while True:
    print_board()

    # Get player input
    move = input("Player " + players[current_player] + ", enter your move (row_column): ")
    move = move.split()
    
    # Validate input length
    if len(move) != 2:
        print("Invalid input, please enter row and column.")
        continue

    row = int(move[0])
    col = int(move[1])

    # Check if the move is valid
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
        print("Invalid move, try again")
        continue
    
    # Make the move
    board[row][col] = players[current_player]

    # Check if the player has won
    if check_win(players[current_player]):
        print_board()  # Print the final board
        print("Player " + players[current_player] + " wins!")
        break

    # Check if board is full
    if check_full():
        print_board()  # Print the final board
        print("It's a tie!")
        break

    # Switch players
    current_player = (current_player + 1) % 2





