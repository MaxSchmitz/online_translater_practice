def has_prefix(word, prefix):
    for i in range(len(prefix)):
        if word[i] != prefix[i]:
            return False
    return True


prefix = input()
words = input().split()

for word in words:
    if has_prefix(word, prefix):
        print(word)
