def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]
    return None
def is_board_full(board):
    return all(cell != '-' for row in board for cell in row)

def play_game():
    board = [['-' for i in range(3)] for j in range(3)]
    current_player = 'X'
    player_names = {'X': 'User1', 'O': 'User2'}
    while True:
        print_board(board)
        print(f"{player_names[current_player]}'s turn (mark: {current_player})")
        row = input("Enter the row (0-2): ")
        col = input("Enter the column (0-2): ")
        if not (row.isdigit() and col.isdigit()):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        row = int(row)
        col = int(col)
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == '-':
                board[row][col] = current_player
            else:
                print("Cell already taken. Try again.")
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(player_names[winner] +"wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid input. Please enter numbers between 0 and 2.")
play_game()
