from random import randint 
import random

def random_player(x_or_o, x_positions, o_positions):
    move = (0, 0)
    while move in x_positions + o_positions:
        x = randint(0, 2)
        y = randint(0, 2)
        move = (x, y)
    return move 

def smart_player(x_or_o, x_positions, o_positions):
    move = (1,1)
    diagonal_priority = [(0,0), (2,0), (0,2), (2,2)]
    vertical_priority = [(0,1), (1,0), (2,1), (1,2)]


# <----------------------------------------------------------------->
    # while move in x_positions + o_positions:
    #     # x ,y = random.choice(diagonal_priority)
    #     if not any(pos in diagonal_priority for pos in o_positions):
    #         x,y = random.choice(diagonal_priority)
    #     move = (x,y)

    # else:
    #     x = randint(0, 2)
    #     y = randint(0, 2)
    #     move = (x, y)

# <--------------------------GPT-------------------------------->
    # if (1, 1) not in x_positions + o_positions:
    #     return (1, 1)

    # if not any(pos in diagonal_priority for pos in x_positions):
    #     while move in x_positions + o_positions:
    #         move = random.choice(diagonal_priority)
    # else:
    #     while move in x_positions + o_positions:
    #         move = (random.randint(0, 2), random.randint(0, 2))
# <------------------------------------------------------>
######################################
    # while move in x_positions + o_positions:
    #     if diagonal_priority not in x_positions + o_positions:
    #         x ,y = random.choice(diagonal_priority)
    #         move = (x,y)
    #         print("hello")
    #     # elif vertical_priority not in x_positions + o_positions:
    #     else:
    #         x ,y = random.choice(vertical_priority)
    #         move = (x,y)
    #         print("world")


# <--------------------------------------------------------->

    # while move in x_positions + o_positions:
    #     # 대각선 위치에 O가 없으면 대각선 위치 중 하나를 선택
    #     if not any(pos in o_positions for pos in diagonal_priority):
    #         move = random.choice(diagonal_priority)
    #     else:
    #         # 대각선이 다 찼으면 다른 우선순위 위치를 선택
    #         if not any(pos in vertical_priority for pos in x_positions + o_positions):
    #             move = random.choice(vertical_priority)
    #         # else:
    #         #     # 모든 우선순위 위치가 차있으면 남은 모든 위치에서 랜덤 선택
    #         #     move = (random.randint(0, 2), random.randint(0, 2))

# <-------------------------------------------------------->
#####################################################################
#####################################################################
#####################################################################
# 이상하긴 하지만 돌아가긴 하는 코드
    while move in x_positions + o_positions:
        diagonal_free = True

        for pos in diagonal_priority:
            if pos not in x_positions or pos not in o_positions:
                diagonal_free = False
                break
        
        if diagonal_free:
            x, y = random.choice(diagonal_priority)
            move = (x, y)
            print("hello")
        else:
            x = randint(0, 2)
            y = randint(0, 2)
            move = (x, y)
#####################################################################
#####################################################################
#####################################################################



    return move

    
#<--------------------------------------------------------------------------->
#     # 승리할 수 있는 위치 확인
#     for move in available_moves(x_positions + o_positions):
#         if x_or_o == 'X':
#             x_positions.append(move)
#         else:
#             o_positions.append(move)
        
#         if check_win(x_positions if x_or_o == 'X' else o_positions):
#             return move
        
#         if x_or_o == 'X':
#             x_positions.remove(move)
#         else:
#             o_positions.remove(move)


#     # 방어 전략
#     opponent_positions = o_positions if x_or_o == 'X' else x_positions
#     for move in available_moves(x_positions + o_positions):
#         opponent_positions.append(move)
        
#         if check_win(opponent_positions):
#             opponent_positions.remove(move)
#             return move
        
#         opponent_positions.remove(move)

#     # 승리 전략
#     while move in x_positions + o_positions:
#         if not any(pos in o_positions for pos in diagonal_priority):
#             move = random.choice(diagonal_priority)
#         elif not any(pos in x_positions + o_positions for pos in vertical_priority):
#             move = random.choice(vertical_priority)
#         else:
#             move = (random.randint(0, 2), random.randint(0, 2))    


#     # while move in x_positions + o_positions:
#     #     print()


#     return move

# def available_moves(positions):
#     """게임 보드에서 가능한 모든 빈 위치를 찾습니다."""
#     all_moves = [(x, y) for x in range(3) for y in range(3)]
#     return [move for move in all_moves if move not in positions]

# def check_win(positions):
#     """주어진 위치에서 승리 조건을 확인합니다."""
#     win_conditions = [
#         [(0, 0), (0, 1), (0, 2)],
#         [(1, 0), (1, 1), (1, 2)],
#         [(2, 0), (2, 1), (2, 2)],
#         [(0, 0), (1, 0), (2, 0)],
#         [(0, 1), (1, 1), (2, 1)],
#         [(0, 2), (1, 2), (2, 2)],
#         [(0, 0), (1, 1), (2, 2)],
#         [(0, 2), (1, 1), (2, 0)],
#     ]
#     for condition in win_conditions:
#         if all(pos in positions for pos in condition):
#             return True
#     return False



#<--------------------------------------------------------------------------->

    # return random_player(x_or_o, x_positions, o_positions)