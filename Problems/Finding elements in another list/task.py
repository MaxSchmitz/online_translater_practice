first_list = [int(n) for n in input().split()]
second_list = [int(n) for n in input().split()]
output_list = []

def binary_search(elements, target):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


for elem in first_list:
    output_list.append(binary_search(second_list, elem))

str_output = [str(elem) for elem in output_list]
print(' '.join(str_output))