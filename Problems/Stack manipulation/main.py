from collections import deque

my_stack = deque()
n = int(input())
for i in range(n):
    user_input = input().split(" ")
    if user_input[0] == 'PUSH':
        my_stack.append(user_input[1])
    elif user_input[0] == 'POP':
        my_stack.pop()

while my_stack:
    print(my_stack.pop())

