# 대부분 솔루션과 강의해주신 내용 보고 참고하면서 이해했습니다.
# 스스로 코딩한 부분은 많지는 않습니다...



import sys 
try:
    from solution.exceptions import InvalidTokenException, NotClosedParenthesesException
except ImportError:
    from exceptions import InvalidTokenException, NotClosedParenthesesException

tokens = ['(', ')']

def find_matching_pair(text, idx):
    """For a given text of parentheses and idx, find the index of matching parentheses in the text. 

    Args:
        str text 
        int idx 
    Returns:
        int
    Raises:
        InvalidTokenException: When the input contains invalid character.
        NotClosedParenthesesException: When it is impossible to find the matching parentheses. 
        ValueError: When the input idx is larger or equal to len(text) or is smaller than 0. 
    
    Examples:
        find_matching_pair('()', 0)
        >> 1 
        find_matching_pair('(())', 1)
        >> 2
        find_matching_pair(')', 0)
        >> NotClosedParenthesesException 
    """

    '''
        find_matching_pair(text, idx)
        - text : parentheses string
        - idx : user wanted index position
        매칭되는걸 찾아야한다.
    '''
    
    # # Raises
    # text_len = len(text)
    # if text[idx] != '(':
    #     return print("NotClasedParenthesesException")
    
    # for char in text:
    #     if char != '(' or char != ')':
    #         return print("InvalidTokenException")

    # if idx > text_len or idx < 0:
    #     return print("InvalidTokenException")

    # # find_matching_pair
    # s = 0
    # flag = False
    
    # for i, char in enumerate(text):
    #     if char =='(':
    #         offset = 1
    #     else:
    #         offset = -1
        
    #     s += offset

    #     if i == idx:
    #         flag = s
    #     elif flag - 1 == s and flag:
    #         return i


    # --------------------------------------------------------
    # <teacher's solution>
    s = 0
    for i, char in enumerate(text[idx:]):
        if char == '(':
            s += 1
        elif char == ')':
            s -= 1
        
        if s == 0:
            return i + idx
# ------------------------------------------------
# <유경님 코드 질문>
    # for i,x  in enumerate(text[idx:], start=idx):
    #     if x == tokens[0]:
    #         num += 1
    #     elif x == tokens[1]:
    #         num -= 1
    #         if num ==0:
    #             pair_idx = i
    #             break
# ----------------------------------------------

def determine_if_rule0(text):
    if text == '':
        return True
    else:
        return False
    # return text == ''

def determine_if_rule1(text):
    # start = text[0]
    # end = text[len(text)-1]
    # left = { start : text[0], end : text[0] }
    # # mid
    # right = { start : text[len(text)-1], end : text[len(text)-1] }

    # return False 
    return not determine_if_rule0(text) and find_matching_pair(text, 0) == len(text) - 1

def determine_if_rule2(text):
    # return False 
    return not (determine_if_rule0(text) or determine_if_rule1(text))

def parse_empty_string():
    return {'node' : '', 'rule' : 0}

def default_node_information(text, offset):
    res = {} # res 딕셔너리 초기화
    
    res['node'] = text
    res['start'] = offset
    res['end'] = len(text) - 1 + offset

    return res

def update_rule1_data(text, res):
    # assert determine_if_rule1(text)

    # matching_idx = find_matching_pair(text, 0)

    # res['rule'] = 1
    # res['left'] = {
    #     'node' : '(',
    #     'start' : 0,
    #     'end' : 0
    # }
    # res['right'] = {
    #     'node' : ')',
    #     'start' : matching_idx,
    #     'end' : matching_idx
    # }
    
    # return res 
    assert determine_if_rule1(text)

    matching_idx = find_matching_pair(text, 0)

    res['rule'] = 1        
    res['left'] = {
        'node': '(', 
        'start': 0, 
        'end': 0, 
    }
    res['right'] = {
        'node': ')', 
        'start': matching_idx, 
        'end': matching_idx, 
    }    
    
    return res 

def update_rule1_mid(text, res):
    assert determine_if_rule1(text)

    matching_idx = find_matching_pair(text, 0)

    res['mid'] = parse_parentheses_with_offset(text[1: matching_idx],1)
    
    return res 

def update_rule2_data(text, res):
    assert determine_if_rule2(text)

    res['rule'] = 2
    
    return res 

def update_rule2_nodes(text, res):
    assert determine_if_rule2(text)

    matching_idx = find_matching_pair(text, 0)

    node_indices = [(0, matching_idx)]

    while matching_idx != len(text) - 1:
        node_start_idx = matching_idx + 1
        if node_start_idx == len(text) - 1:
            break
        matching_idx = find_matching_pair(text, node_start_idx)
        node_indices.append((node_start_idx, matching_idx))
    
    res['nodes'] = [parse_parentheses_with_offset(text[start:end+1], start) for start, end in node_indices]

    return res 

# <-------------------------강사님 수업 코드-------------------->
# def update_rule2_nodes(text,res):
#     assert determine_if_rule2(text)

#     result = []
#     idx = 0
#     while idx < len(text) - 1:
#         jdx = find_matching_pair(text, idx)
#         result.append((text[idx:jdx+1],idx))
#         idx = jdx + 1
    
#     res['nodes'] = [parse_parentheses_with_offset(text, idx) for text, idx in result]

#     return res
# <------------------------------------------------------------->


def parse_parentheses(text):
    """For the given string, parse it in the form of dict. 

    For detailed explanation about the parsing process and the result format, consult parentheses/documents/assignment.txt file. 

    Args:
        str text
    Returns:
        dict 
    Raises:
        InvalidTokenException: When the input contains invalid character.
        NotClosedParenthesesException: When the input have a syntax error.
    Examples:

    parse_parentheses('')
    >> {
            'node': '',
            'rule': 0,  
    }
    parse_parentheses('()')
    >> {
            'node': '()', 
            'start': 0, 
            'end': 1,
            'rule': 1, 
            'left': {
                'node': '(', 
                'start': 0, 
                'end': 0, 
            },
            'mid': {
                'node': '', 
                'rule': 0, 
            }, 
            'right': {
                'node': ')',
                'start': 1, 
                'end': 1,   
            },
    }
    parse_parentheses('(())')   
    >> {
            'node': '(())', 
            'start': 0, 
            'end': 3, 
            'rule': 1, 
            'left': {
                'node': '(', 
                'start': 0, 
                'end': 0, 
            }, 
            'mid': {}, // Same as parse_parentheses('()'), except for start/end attributes. 
            'right': {
                'node': ')', 
                'start': 3, 
                'end': 3, 
            }
    }
    parse_parentheses('()()')
    >> {
            'node': '()()', 
            'start': 0, 
            'end': 3, 
            'rule': 2, 
            'nodes': [
                {...},  // Same as parse_parentheses('()').
                {...},  // Same as parse_parentheses('()'), except for start/end attributes. 
            ]
    }
    parse_parentheses('(()())')
    >> {
            'node': '(()())', 
            'start': 0, 
            'end': 5, 
            'rule': 1, 
            'left': {...}, // Same as parse_parentheses('()')['left'] 
            'mid': {...}, // Same as parse_parentheses('()()'), except for start/end attributes. 
            'right': {...}, // Same as parse_parentheses('()')['left'], except for start/end attributes. 
    }
    """ 

    return parse_parentheses_with_offset(text)

def parse_parentheses_with_offset(text, offset = 0):
    rule0 = determine_if_rule0(text)
    rule1 = determine_if_rule1(text) 
    rule2 = determine_if_rule2(text) 

    if rule0: # rule 0 : para -> ''
        return parse_empty_string()
    
    res = default_node_information(text, offset)

    if rule1: # rule 1 : para -> ( para )
        res = update_rule1_data(text, res)
        res = update_rule1_mid(text, res)
    elif rule2: # rule 2  : para -> para1 para2 ...
        res = update_rule2_data(text, res) 
        res = update_rule2_nodes(text, res)     
    else:
        assert False, 'Something goes wrong' 
    
    return res 

def main():
    args = sys.argv
    with open(f'{sys.argv[1]}', 'r') as f:
        text = f.read().strip()
        print(parse_parentheses(text))

if __name__ == '__main__':
    # print(determine_if_rule0(''))
    # print(determine_if_rule0('()'))
    main()




'''
( ( ( ) ( ) ) )
( ( ) ( ) )	-> offset = 1



(	(	)	(	)	)
0	1	2	3	4	5

res { node : text , start : 0 , end :  5 }

matching_idx = 5

res { rule : 1 , node : text, start : 0 , end 5, left { node : '(', start : 0, end : 0 }, right {node : ')' , 


mid

matching_idx = 5

(	(	)	(	)	)
X	1	2	3	4	X

text[1:5] => 1	2	3	4
offset = 1

	-> default_node_information(text[1:5], 1)
		node : text[1:5]
		start = 1
		end = 4

		-> update_rule2_data
			-> rule : 2
			matching_idx = 2
			node_indices = [(0, 2)]

			while 2 != 3
				node_start_idx = 3
				if node_start_idx(3) == 3
					break

		res['nodes'] = parse_parentheses_with_offset(text[1:5], 1) for start, end in node_indices

		-----> for start, end in node_indices
				res['nodes'] = parse_parentheses_with_offset(text[start(1) : end(4) + 1, start(1)]	
					-> 다시 검증해서 들어가라.

'''