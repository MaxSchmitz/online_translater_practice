def find_last(text, pattern):
    indexes = []
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            indexes.append(i)

    if indexes:
        return indexes.pop()
    else:
        return -1

# my_text = 'aaabbaaabbaaabbaaabb'
# my_pattern = 'bb'
my_text = input()
my_pattern = input()

print(find_last(my_text, my_pattern))


