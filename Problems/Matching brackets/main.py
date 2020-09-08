from collections import deque

# put your python code here
def check_brackets(user_input):
    my_stack = deque()
    for character in user_input:
        # print(character)
        if character == '(':
            # print(f'pushin {character} ')
            my_stack.append(character)
            # print(f'so {my_stack}')
        elif character == ')' and len(my_stack) > 0:
            # print(f'poppin {character}')
            my_stack.pop()
            # print(f'so {my_stack}')
        elif character == ')' and len(my_stack) == 0:
            # print('why am i here')
            return 'ERROR'

    if len(my_stack) > 0:
        return 'ERROR'
        # print(f'because {my_stack}')
    else:
        return 'OK'



print(check_brackets(input()))