def kth(numbers, target, k):
    occurence = 0
    index = -1
    for i, elem in enumerate(numbers):
        if elem == target:
            occurence += 1
            if occurence == k:
                index = i
                break
    return index


a = list(map(int, input().split()))
b = int(input())
c = int(input())
print(kth(a, b, c))

