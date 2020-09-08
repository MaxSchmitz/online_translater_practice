from collections import deque

n = int(input())
actions = deque()
read_books = deque()
unread_books = deque()
for item in range(n):
    actions.append(input().split(" ", 1))
while actions:
    next_action = actions[-1][0]
    if next_action == 'BUY':
        unread_books.append(actions.pop())
    elif next_action == 'READ':
        read_books.append(actions.pop())


print(unread_books)
print(read_books)
for item in read_books:
    if len(item) > 1:
        print(item[1])