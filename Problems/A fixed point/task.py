
def binary_search(elements):
    iterations = 0
    left, right = 0, len(elements) - 1

    while left <= right:
        iterations +=1
        middle = (left + right) // 2

        if elements[middle] == middle:
            # print(f'iterations = {iterations}')
            return True
        elif middle < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return False

my_list = [int(n) for n in input().split()]


print(binary_search(my_list))