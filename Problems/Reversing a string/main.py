from collections import deque

n = int(input())
my_stack = deque()
for item in range(n):
    my_stack.append(input())
while len(my_stack):
    print(my_stack.pop())