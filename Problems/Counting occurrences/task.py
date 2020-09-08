def count(numbers, target):
    target_count = 0

    for elem in numbers:
        if elem == target:
            target_count += 1
    return target_count

print(count(input().split(), input()))