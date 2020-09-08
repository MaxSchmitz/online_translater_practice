# put your python code here
def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged

def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

my_list = [int(a) for a in input().split()]
sorted = merge_sort(my_list)
print(*sorted)

