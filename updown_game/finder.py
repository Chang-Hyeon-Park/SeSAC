"""Implement a better finder to find the right argument for the function. 

Your job is to implement a function that accepts another function(call this f) and additional information(related to possible candidates) as input, and returns the argument that f returns True. 

As a hint, f will return 'up' or 'down'. When f needs larger input value to return True, it will return 'up'. Else, it will return 'down'. 

You will be asked to implement 2 finder functions; naive_finder and smart_finder. 

1) naive_finder

Function naive_finder assumes that the test function only accepts integer inputs; therefore, naive_finder can (naively) iterate all the possible candidates. It will take long - but that's why it's called naive.  Function naive_finder accepts another function f and a candidate list as input. When naive_finder is called, it iterates over all possible candidates, applies all candidates to the function one at a time, and returns when the result is True. 

naive_finder should be able to find right argument for updown_game.updown_game_easy and updown_game.updown_game_medium. 

2) smart_finder

Function smart_finder accepts another function, and the max/min value of the input for the function f. To implement the smart_finder function, think of how you actually play '업다운 게임'. 

smart_finder should be able to find right argument for updown.game.updown_game_hard and animation.check_collision. 
"""

def manual_finder(f):
    while True:
        i = input(f'Guess the argument!\nGuess is: ')
        res = f(float(i))
        if res is True:
            print(f'You found the right argument!; {float(i)}')
            return float(i)
            
        print(res) 
    

# def naive_finder(f, lst = list(range(5))):
    # pass

# def naive_finder(f, lst):
#     for i in lst:
#         if f(i):
#             return i
#     return None

def naive_finder(f, lst = list(range(5))):
    for i in lst:
        result = f(i)
        print(f"Trying {i}: Result {result}")
        if result == True:
            return i
    return None


def smart_finder(f, min_input = 0, max_input = 100):
    '''
        half = max_input의 절반 받아야함.
        if half가 true면:
            small_random_int값 반환
            break
        
        elif return == 'down':
            재귀로 다시 호출
            smart_finder(f, min_input, max_input == half)
        
        elif return == 'up':
            재귀로 다시 호출
            smart_finder(f, half, max_inpu)
    '''
    # half = max_input//2
    # while 1:
    #     if f(half):
    #         return half
    #         break
    #     elif f(half) == 'down':
    #         smart_finder(f,min_input,half)
    #     elif f(half) == 'up':
    #         smart_finder(f,half,max_input)

    
    cnt=0
    while 1:
        half = (min_input + max_input) / 2
        result = f(half)
        print(f"Trying {half}: Result {result}")  # 각 시도와 그 결과를 출력합니다
        print(f"Attempts : {cnt}\n")
        cnt += 1
        if result == True:
            return half
        elif result == 'down':
            max_input = half - 1
        elif result == 'up':
            min_input = half + 1

        elif result == None:
            max_input = max_input - 2
            min_input = min_input + 1
        else:
            break
    
