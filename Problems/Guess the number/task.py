x = int(input())
lx, rx = (int(n) for n in input().split())
tries = 0

# put your code here
# Python3 Program for recursive binary search.

def binary_search(elements, target):
    iterations = 0
    left, right = 0, len(elements) - 1

    while left <= right:
        iterations +=1
        middle = (left + right) // 2

        if elements[middle] == target:
            # print(f'iterations = {iterations}')
            return iterations
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1


# Function call
tries = binary_search(range(lx, rx+1), x)


print(tries)