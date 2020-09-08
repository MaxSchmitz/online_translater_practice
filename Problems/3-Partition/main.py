# put your python code here
def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] < lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[start], lst[j] = lst[j], lst[start]

    k = j

    for i in range(j + 1, end + 1):
        if lst[i] == lst[j]:
            k += 1
            lst[i], lst[k] = lst[k], lst[i]

    return j, k

my_lst = [int(a) for a in input().split()]
pivot = my_lst[0]
partition(my_lst, 0, len(my_lst)-1)
pivots = []
for index, item in enumerate(my_lst):
    if item == pivot:
        pivots.append(index)
print(f'{pivots[0]} {pivots[-1]}')
print(*my_lst)
