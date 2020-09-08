def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] >= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j

def quick_sort(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)

dates = [int(n) for n in input().split()]
# dates = [int(n) for n in '1991 1984 2002 1998'.split()]
# print(dates)
quick_sort(dates, 0, len(dates) - 1)
print(*dates)