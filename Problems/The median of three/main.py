def choose_median(start, middle, end):
    # finish the method for finding the median
    pivot = [start, middle, end]
    pivot.sort()
    return pivot[1]


def partition(lst, pivot, start, end):
    # add necessary modifications
    # don't forget to print the result of the partition!
    pivot = lst.index(pivot)
    print(f'index of pivot is {pivot}')
    j = start

    for i in range(start, end):
        if lst[i] <= lst[pivot]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


# read the input list
# and call the methods
lst = [int(n) for n in '3 6 5 2 4'.split()]
my_pivot = choose_median(lst[0], lst[len(lst) // 2], lst[len(lst)-1])
print(f'pivot is {my_pivot}')
partition(lst, my_pivot, 0, len(lst) - 1)
print(f'list after partion {lst}')
