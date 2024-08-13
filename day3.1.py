def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    
    if [player, player, player] in win_conditions:
        return True
    return False

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            
            if board[row][col] != ' ':
                print("This cell is already taken. Try again.")
                continue
            
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        
        except (IndexError, ValueError):
            print("Invalid input. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
