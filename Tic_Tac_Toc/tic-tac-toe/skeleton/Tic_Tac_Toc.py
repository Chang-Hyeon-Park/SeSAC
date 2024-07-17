'''
    틱택토 짜려면
    1. 3 X 3 Board있어야함
    2. 순서를 정해야함(가위바위보) (굳이 안해도 됨)
    3. 내가 먼저 한다면 입력하고 싶은 곳의 좌표 입력받음
        ex) 1, 1
    4. (1,1)자리에 O가 표시된 채로 배열 출력
    5. 컴퓨터가 랜덤으로 비어있는 곳의 값을 X로 표시 후 배열 출력
    6. 사용자 입력 받아서 반복
    
    <승리 조건>
     - 사용자가 놓은 자리가 3개가 연속될 때 승리
     - 조건 나눠서 승리할 수 있는 경우의 수 써놓기?
     - ex) (0,0) - (0,1) / (0,2)
                 - (1,0) / (2,0)
                 - (1,1) / (2,2)

           (0,1) - (0,0) / (0,2)
                 - (1,1) / (2,1)

           (0,2) - (0,0) / (0,1)
                 - (1,1) / (2,0)
                 - (1,2) / (2,2)
            
           (1,0) - (0,0) / (2,0)
                 - (1,1) / (1,2)
        
           (1,1) - (0,0) / (2,2)
                 - (1,0) / (1,2)
                 - (2,0) / (0,2)
                 - (0,1) / (2,1)

           (1,2) - (1,0) / (1,1)
                 - (0,2) / (2,2)
            
           (2,0) - (0,0) / (1,0)
                 - (1,1) / (0,2)
                 - (2,1) / (2,2)

           (2,1) - (2,0) / (2,2)
                 - (0,1) / (1,1)

           (2,2) - (0,0) / (1,1)
                 - (2,0) / (2,1)
                 - (0,2) / (1,2)
'''

# default_board = [3][3]

'''
for i in range(3):
    print(' ----------', end=' ')
print()
for i in range(3):
    print('|           |           |          |')

for i in range(3):
    print(' ----------', end=' ')
print()
for i in range(3):
    print('|           |           |          |')

for i in range(3):
    print(' ----------', end=' ')
print()
for i in range(3):
    print('|           |           |          |')

for i in range(3):
    print(' ----------', end=' ')

'''

'''
for k in range(3):
    for i in range(3):
        print(' ----------', end=' ')
    print()
    for i in range(3):
        print('|           |           |          |')
for i in range(3):
    print(' ----------', end=' ')
'''
# def empty_board()
'''
for k in range(3):
    for i in range(3):
        board += ' ----------'
    board += '\n'
    for i in range(3):
        board += '|           |           |          |'
for i in range(3):
    board += ' ----------'
'''


game_status = {'x_positions' : [], 'o_positiions' : []}

def empty_board(x_size = 3, y_size = 3, x_cell_size=5, y_cell_size=3):
    board = ''

    # for k in range(3):
    #     for i in range(3):
    #         board += ' ----------'
    #     board += '\n'
    #     for i in range(3):
    #         board += '|           |           |          |'
    # for i in range(3):
    #     board += ' ----------'
    




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

    x_or_o = ('X','O')
    player_choice =[]
    computer_choice=[]

    player_choice_pick = []
    computer_choice_pick = []

    pick = ''
    for i in range(3):
        for j in range(3):
            pick.append(i,j)
    


    if player_choice == 'X':
        game_status['x_positions'].append(pick)
    
    elif player_choice == 'O':
        game_status['o_positions'].append(pick)

    # 차 있는 곳은 넣을 수 없도록.

    for i in enumerate(pick):
        if player_choice == 'X' and player_choice_pick == game_status['x_positions']:
            return print("Can't choose that place")
        elif player_choice == 'O' and player_choice_pick == game_status['o_positions']:
            return print("Can't choose that place")
    
    


    pass

def check_winlose(game_status):


    pass


def display(game_status):

    
    pass

if __name__ =='__main__':
    empty_board(x_size = 4, y_size=6, x_cell_size = 7, y_cell_size=3)