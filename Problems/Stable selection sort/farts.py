def farts(array, left, right, value):
    if left >= right:
        return 0
    elif left == right - 1:
        if array[left] == value:
            return 1
        else:
            return 0
    else:
        middle = (left + right) // 2
        return farts(array, left, middle, value) + farts(array, middle, right, value)

print(farts([1, 2, 3, 5, 5], 0, 5, 5))
print(farts([1, 2, 3, 3, 3], 0, 4, 3))
print(farts([1, 2, 3, 4, 5], 0, 4, 5))
print(farts([2, 2, 2, 2, 2], 0, 4, 2))
print(farts([1, 1, 1, 2, 2], 1, 3, 1))