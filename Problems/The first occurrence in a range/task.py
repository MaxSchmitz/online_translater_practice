def search(numbers, target, a, b):
    index = -1

    for i, elem in enumerate(numbers):
        if a <= i < b:
            if elem == target:
                index = i
                break

    return index



num_list = [int(num) for num in input().split()]
target_num = int(input())
a, b = [int(num) for num in input().split()]

print(search(num_list, target_num, a, b))