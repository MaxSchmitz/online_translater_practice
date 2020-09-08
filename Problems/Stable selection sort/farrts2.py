def method(array, left, right):
    if left == right:
        if array[left] % 2 == 0:
            return 1
        else:
            return 0
    else:
        middle = (left + right) // 2
        return method(array, left, middle) + method(array, middle + 1, right)


print(method([2, 2, 2, 2, 2, 2, 2], 0, 1))