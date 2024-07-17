game_status = {'x_positions' : [], 'o_positions' : []} 

def empty_board(x_size = 3, y_size = 3, x_cell_size=5, y_cell_size=3):
    """Create an empty board. 

    The board is made of horizontal lines, made with - and vertical lines, made with |. 

    (optional) When there are no x_cell_size and y_cell_size arguments, default to arbitary size of your choice. Just make it consistent. 
    """
    board = ''

    # for k in range(3):
    #     for i in range(3):
    #         board += ' ---------- '
    #     board += '\n'
    #     for i in range(3):
    #         board += '|           |           |          |\n'
    # for i in range(3):
    #     board += ' ---------- '

    # --------------------------------------------------------------    

    # for k in range(y):
    #     for i in range(x):
    #         board += ' ---------- '
    #     board += '\n'

    #     for i in range(y):
    #         board += '|'
    #         for j in range(x):
    #             board += '           |'
    #         board += '\n'
    
    # for i in range(x):
    #         board += ' ---------- '

    # --------------------------------------------------------------  

    #<------------------------------강사님 코드 -------------------->
    hline = (' ' + '-' * x_cell_size) * x_size
    # print(hline)

    for y in range(y_size):
        print(hline)
        for z in range(y_cell_size):
            for x in range(x_size):
                print('|' + ' ' * x_cell_size , end='')
            print('|')
    print(hline)
    
    #<-----------------------------강사님 코드 --------------------->
    


    return board 

def play(game_status, x_or_o, coordinate):
    """Main function for simulating tictactoe game moves. 

    Tictactoe game is executed by two player's moves. In each move, each player chooses the coordinate to place their mark. It is impossible to place the mark on already taken position. 

    A move in the tictactoe game is composed of two components; whether who ('X' or 'O') made the move, and how the move is made - the coordinate of the move. 

    Coordinate in our tictactoe system will use the coordinate system illustrated in the example below. 
    
    Example 1. 3 * 4 tictactoe board. 
    
         ---------- ---------- ----------
        |          |          |          |
        |  (0,0)   |  (1,0)   |  (2,0)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,1)   |  (1,1)   |  (2,1)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,2)   |  (1,2)   |  (2,2)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,3)   |  (1,3)   |  (2,3)   |
        |          |          |          |
         ---------- ---------- ----------
        """
    

    # x_or_o = ('X','O')
    # player_choice =[]
    # computer_choice=[]

    # player_choice_pick = []
    # computer_choice_pick = []

    # pick = ''
    # for i in range(3):
    #     for j in range(3):
    #         pick.append(i,j)
    

    # if player_choice == 'X':
    #     game_status['x_positions'].append(pick)
    
    # elif player_choice == 'O':
    #     game_status['o_positions'].append(pick)

    # # 차 있는 곳은 넣을 수 없도록.
    # for i in enumerate(pick):
    #     if player_choice == 'X' and player_choice_pick == game_status['x_positions'] and player_choice_pick != game_status['o_positions']:
    #         return print("Can't choose that place")
    #     elif player_choice == 'O' and player_choice_pick == game_status['o_positions'] and player_choice_pick != game_status['x_positions']:
    #         return print("Can't choose that place")

# <----------------------------------------------------------------------->

    # if coordinate in game_status['x_positions'] + game_status['o_positions']:
    #     raise ValueError(f'{coordinate} already taken')
    # if x_or_o == 'X':
    #     game_status['x_positions'].append(coordinate)
    # elif x_or_o =='O':
    #     game_status['o_positions'].append(coordinate)


# <----------------------------------------------------------------------->

# <------------------------------강사님 코드------------------------------->

    if coordinate in game_status['x_positions'] + game_status['o_positions']:
        assert False
    if x_or_o == 'X':
        game_status['x_positions'].append(coordinate)
    elif x_or_o == 'O':
        game_status['o_positions'].append(coordinate)



# <------------------------------강사님 코드------------------------------->

    pass 

def check_winlose(game_status):
    """Check the game status; game status should be one of 'X wins', 'O wins', 'tie', 'not decided'. 
    """

    # check_game_status = ['X wins','O wins','tie','not decided']
    # player_choice =[]

    # win_case = {
    #     {(0,0),(0,1),(0,2)},
    #     {(0,0),(1,0),(2,0)},
    #     {(0,0),(1,1),(2,2)},
    #     {(0,1),(0,0),(0,2)},
    #     {(0,1),(1,1),(2,1)},
    #     {(0,2),(0,0),(0,1)},
    #     {(0,2),(1,1),(2,0)},
    #     {(0,2),(1,2),(2,2)},
    #     {(1,0),(0,0),(2,0)},
    #     {(1,0),(1,1),(1,2)},
    #     {(1,1),(0,0),(2,2)},
    #     {(1,1),(1,0),(1,2)},
    #     {(1,1),(2,0),(0,2)},
    #     {(1,1),(0,1),(2,1)},
    #     {(1,2),(1,0),(1,1)},
    #     {(1,2),(0,2),(2,2)},
    #     {(2,0),(0,0),(1,0)},
    #     {(2,0),(1,1),(0,2)},
    #     {(2,0),(2,1),(2,2)},
    #     {(2,1),(2,0),(2,2)},
    #     {(2,1),(0,1),(1,1)},
    #     {(2,2),(0,0),(1,1)},
    #     {(2,2),(2,0),(2,1)},
    #     {(2,2),(0,2),(1,2)}
    # }

# <---------------------------win_case = 8------------------------------->
    # win_case = [
    #     [(0,0),(0,1),(0,2)],
    #     [(0,0),(1,0),(2,0)],
    #     [(0,0),(1,1),(2,2)],
    #     [(0,1),(1,1),(2,1)],
    #     [(0,2),(1,1),(2,0)],
    #     [(0,2),(1,2),(2,2)],
    #     [(1,0),(1,1),(1,2)],
    #     [(2,0),(2,1),(2,2)],
    # ]


# <---------------------------------------------------------------------->

    # if game_status['x_positions'].isin(win_case) and player_choice == 'X':
    #     return check_game_status[0]
    # elif game_status['o_positions'].isin(win_case) and player_choice =='O':
    #     return check_game_status[1]
    # else:
    #     return check_game_status[2:3]

# <---------------------------------------------------------------------->


    # for i in win_case:
    #     if game_status['x_positions'].isin(win_case):
    #         return check_game_status[0]
    #     elif game_status['o_positions'].isin(win_case):
    #         return check_game_status[1]
    #     elif len(game_status['x_positions']) + len(game_status['o_positions']) == 9:
    #         return check_game_status[2]
    #     else:
    #         return check_game_status[3]

# <---------------------------------------------------------------------->
    
    # x_positions = [] lsit, win_case = {} set 값의 비교 자체가 불가
    # In Addition x_positions 는 4,5개까지 가능
    # ==> isin으로 비교는 비교 자체가 불가능


    # if game_status['x_positions'].isin(win_case):
    #     return check_game_status[0]
    # elif game_status['o_positions'].isin(win_case):
    #     return check_game_status[1]
    # elif len(game_status['x_positions']) + len(game_status['o_positions']) == 9:
    #     return check_game_status[2]
    # else:
    #     return check_game_status[3]


# <------------------------------------------------------------------>
    # for win in win_case:
    #     if win[0] in game_status['x_positions'] and win[1] in game_status['x_positions'] and win[2] in game_status['x_positions']:
    #         return check_game_status[0]
    #     elif win[0] in game_status['o_positions'] and win[1] in game_status['o_positions'] and win[2] in game_status['o_positions']:
    #         return check_game_status[1]
    #     elif len(game_status['x_positioins']) + len(game_status['o_positions']) == 9:
    #         return check_game_status[2]
    #     else:
    #         return check_game_status[3]
        
# <------------------------------------------------------------------>

# <---------------------------강사님 코드----------------------->

    winning_positions = [
        [(0,0),(0,1),(0,2)],
        [(0,0),(1,0),(2,0)],
        [(0,0),(1,1),(2,2)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,1),(2,0)],
        [(0,2),(1,2),(2,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
    ]

    # winning_positions들 중 하나에 있는 모든 자리만 X 아니면 O가 다 먹고 있으면 먹은 사람이 승리한것

    if determine_if_x_wins(game_status, winning_positions):
        return 'X wins'
    elif determine_if_o_wins(game_status, winning_positions):
        return 'O wins'
    elif len(game_status['x_positions'] + game_status['o_positions']) == 9:
        return 'tie'
    else:
        return 'not decided'
        

def determine_if_x_wins(game_status, winning_positions):
    x_pos = game_status['x_positions']
    for win in winning_positions:
        a,b,c = win
        if a in x_pos and b in x_pos and c in x_pos:
            return True
    return False

def determine_if_o_wins(game_status, winning_positions):
    o_pos = game_status['o_positions']
    for win in winning_positions:
        a,b,c = win
        if a in o_pos and b in o_pos and c in o_pos:
            return True
    return False

# <---------------------------강사님 코드----------------------->


def display(game_status, x_size = 3, y_size = 3, x_cell_size=5, y_cell_size=3):
    """Display the current snapshot of the board. 

    'Snapshot' should contain following components. 

    - The board itself 
    - Moves that are already made

    For clarification, see provided examples. 

    Example 1. 
    When TictactoeGame instance t have following attributes; 
    - x_positions = [(0,0), (2,0), (2,1), (1,2)]
    - o_positions = [(1,0), (1,1), (0,2), (2,2)]

    t.display()
    >> 
     ---------- ---------- ----------
    |          |          |          |
    |    X     |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |          |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |    O     |    X     |    O     |
    |          |          |          |
     ---------- ---------- ----------

    """

# <---------------------------------------------------------------------->
    # board = [3][3]
    # x_positions = []
    # o_positions = []

    # for i in enumerate(x_positions):
    #     board = x_positions
    
    # for i in enumerate(o_positions):
    #     board = o_positions

    # pass 
# <---------------------------------------------------------------------->

# <---------------------------강사님 코드 ------------------------------->

    hline = (' ' + '-' * x_cell_size) * x_size
    # print(hline)

    for y in range(y_size):
        print(hline)
        for z in range(y_cell_size):
            for x in range(x_size):
                if z == 1:
                    if (x, y) in game_status['x_positions']:
                        print('|' + ' ' * (x_cell_size//2) + 'X' + ' ' * (x_cell_size//2), end='')
                    elif (x,y) in game_status['o_positions']:
                        print('|' + ' ' * (x_cell_size//2) + 'O' + ' ' * (x_cell_size//2), end='')
                    else:
                        print('|' + ' ' * x_cell_size, end='')
                else:
                    print('|' + ' ' * x_cell_size, end='')
            print('|')
    print(hline)

# <---------------------------강사님 코드 ------------------------------->













# if __name__ == '__main__':
#     t = TictactoeGame()
#     print(t.empty_board())
    # t.play('X', (0,0))
    # t.display()


# if __name__ == '__main__':
#     print(empty_board(5,7))
    # t.play('X', (0,0))
    # t.display()

# if __name__ == '__main__':
#     play(game_status, 'X', (1,1))
#     # t.play('X', (0,0))
#     # t.display()

# if __name__ =='__main__':
#     empty_board(x_size = 4, y_size=6, x_cell_size = 7, y_cell_size=3)


# if __name__ =='__main__':
#     display(game_status = {'x_positions' : [(0,0)], 'o_positions' : [(1,0)]})