import math

def merge(left, right):

    return left + right

def count_merge_operations(lst, count):
    print(f'count is {count}')
    if len(lst) > 1:
        count += 1
    if len(lst) < 2:
        print('small')
        return 1
    mid = len(lst) // 2
    left = count_merge_operations(lst[:mid], count)

    right = count_merge_operations(lst[mid:], count)


    return merge(left, right)

print(count_merge_operations(input().split(), 0))
