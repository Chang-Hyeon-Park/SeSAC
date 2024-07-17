# 전역 변수로 보드 상태와 게임 상태를 관리
board = [[' ' for _ in range(3)] for _ in range(3)]
game_status = {'x_positions': [], 'o_positions': []}

def empty_board():
    """Create an empty board as a string."""
    board_str = ""
    for k in range(3):
        board_str += ' ---------- ---------- ----------\n'
        for _ in range(3):
            board_str += '|           |           |           |\n'
    board_str += ' ---------- ---------- ----------'
    return board_str

def display_board():
    """Display the current snapshot of the board."""
    board_str = ""
    for row in board:
        board_str += ' ---------- ---------- ----------\n'
        board_str += '|           |           |           |\n'
        board_str += '|   ' + '   |   '.join(row) + '   |\n'
        board_str += '|           |           |           |\n'
    board_str += ' ---------- ---------- ----------'
    print(board_str)

def play(x_or_o, coordinate):
    """Simulate a move in the TicTacToe game."""
    row, col = coordinate
    if board[row][col] == ' ':
        board[row][col] = x_or_o
        if x_or_o == 'X':
            game_status['x_positions'].append(coordinate)
        else:
            game_status['o_positions'].append(coordinate)
        return True
    else:
        print("Can't choose that place")
        return False

def check_winlose():
    """Check the game status; return 'X wins', 'O wins', 'tie', or 'not decided'."""
    win_case = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # rows
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # columns
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]                           # diagonals
    ]

    for case in win_case:
        if all(pos in game_status['x_positions'] for pos in case):
            return 'X wins'
        if all(pos in game_status['o_positions'] for pos in case):
            return 'O wins'
    
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return 'tie'
    
    return 'not decided'

# 게임 시작
print(empty_board())
display_board()

# 플레이어의 움직임 (예: 첫 번째 플레이어가 (0, 0)에 'X'를 놓음)
play('X', (0, 0))
display_board()
play('O', (1, 1))
display_board()

# 게임 상태 확인
print(check_winlose())
