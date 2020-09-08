def has_suffix(word, suffix):
    for i in range(1, len(suffix)+1):
        if word[len(word)-i] != suffix[len(suffix)-i]:
            return False
    return True


# Change the next line
extension = ".py"
n = int(input())

for i in range(n):
    file = input()
    if has_suffix(file, extension):
        print(file)