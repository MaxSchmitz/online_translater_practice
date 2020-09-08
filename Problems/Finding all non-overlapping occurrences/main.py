
def find_no_overlaps(text, pattern):
    indexes = []
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            if indexes:
                if i < len(pattern) - indexes[len(indexes) - 1]:
                    pass
                    # print(f'{indexes[len(indexes) - 1]} and i is {i}')
                elif i + len(pattern) >= len(text):
                    pass
                    # print('end too long')
                else:
                    # print(i + len(pattern))
                    indexes.append(i)
            else:
                indexes.append(i)

    return indexes

my_text = input()
my_pattern = input()

print(find_no_overlaps(my_text, my_pattern))