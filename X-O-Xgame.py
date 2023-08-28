import random as r

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# Define a function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Define a function to handle a player's turn
def check(player):
    if player == "O":
        comp_turn(player)
    else:
        take_turn(player)


# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (
        (board[0] == board[1] == board[2] != "-")
        or (board[3] == board[4] == board[5] != "-")
        or (board[6] == board[7] == board[8] != "-")
        or (board[0] == board[3] == board[6] != "-")
        or (board[1] == board[4] == board[7] != "-")
        or (board[2] == board[5] == board[8] != "-")
        or (board[0] == board[4] == board[8] != "-")
        or (board[2] == board[4] == board[6] != "-")
    ):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"


# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    computer_player = "O"
    game_over = False
    while not game_over:
        check(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = computer_player if current_player == "X" else "X"


# Define a function to make a winning move
def check_win_move(player):
    for i in range(9):
        if board[i] == "-":
            board[i] = player
            if check_game_over() == "win":
                return i
            else:
                board[i] = "-"
    return None


# Define a function to handle the computer's turn
def comp_turn(player):
    print(player + "'s turn.")
    # Check for a winning move
    win_move = check_win_move(player)
    if win_move is not None:
        board[win_move] = player
    else:
        # Check for a blocking move
        user_win_move = check_win_move("X" if player == "O" else "O")
        if user_win_move is not None:
            board[user_win_move] = player
        else:
            # Randomly place the symbol
            position = r.randrange(1, 10)
            position = int(position) - 1
            while board[position] != "-":
                position = r.randrange(1, 10)
                position = int(position) - 1
            board[position] = player
    print_board()


# Define a function to handle the user's turn
def take_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")
    position = int(position) - 1
    while board[position] != "-":
        position = (
            int(input("Position already taken. Choose a different position: ")) - 1
        )
    board[position] = player
    print_board()


# Start the game
if __name__=="__main__":
	play_game()

while True:
        answer = input("Do you want to play again? (Y/N): ")
        if answer.lower() == "y" or answer.lower == "yes":
            board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            print("--------------------------------------")
            play_game()
        else:
         break