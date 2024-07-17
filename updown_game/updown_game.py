import random 

small_max_num = 10
max_num = 10000000
small_random_int = random.randint(0, small_max_num)
random_int = random.randint(0, max_num)
random_float = random.uniform(0, max_num)

def updown_game_easy(guess):
    if guess > small_random_int:
        return 'down'
    elif guess < small_random_int:
        return 'up'
    return guess == small_random_int

def updown_game_medium(guess):
    if guess > random_int:
        return 'down'
    elif guess < random_int:
        return 'up'
    return guess == random_int

def updown_game_hard(guess):
    if guess - random_float > 0.001:
        return 'down'
    elif guess - random_float < -0.001:
        return 'up' 
    return abs(random_float - guess) < 0.001


# if __name__ == '__main__':
#     from finder import manual_finder
#     from time import time 

#     begin = time()
#     print(manual_finder(updown_game_easy))
#     end = time()

#     print(end - begin)
    

# if __name__ == '__main__':
#     from finder import manual_finder
#     from finder import naive_finder
#     from time import time 

#     lst = list(range(small_max_num + 1))

#     begin = time()
#     result = naive_finder(updown_game_easy,lst)
#     print("Correct guess:", result)
#     # print(naive_finder(updown_game_easy, lst))
#     end = time()

#     print("Time taken:", end - begin)
#     print("Expected value:", small_random_int)
#     # print(end - begin)


############################################################
############################################################
## naive_finder
# if __name__ == '__main__':
#     from finder import naive_finder
#     from time import time 

#     lst = list(range(small_max_num + 1))

#     begin = time()
#     print("Correct guess:", naive_finder(updown_game_easy,lst))
#     end = time()

#     print("Time taken:", end - begin)
#     print("Expected value:", small_random_int)
#     # print(end - begin)
############################################################
############################################################



# if __name__ == '__main__':
#     from finder import smart_finder
#     from time import time 

#     begin = time()
#     print(smart_finder(updown_game_easy))
#     end = time()

#     print(end - begin)


##############################################
##############################################
# # smart_finder / updown_game_medium
# if __name__ == '__main__':
#     from finder import smart_finder
#     from time import time 

#     begin = time()
#     print("Correct guess:", smart_finder(updown_game_medium, 0, max_num))  # small_max_num을 최대값으로 설정
#     end = time()
#     print("Time taken:", end - begin)
#     print("Expected value:", max_num)
#     # print(end - begin)

#############################################
#############################################

# smart_finder / updown_game_hard
if __name__ == '__main__':
    from finder import smart_finder
    from time import time 

    begin = time()
    print("Correct guess:", smart_finder(updown_game_hard, 0, max_num))  # small_max_num을 최대값으로 설정
    end = time()
    print("Time taken:", end - begin)
    print("Expected value:", max_num)
    # print(end - begin)