def contains_upto_permutations(text, pattern):
    text_dict = {letter:text.count(letter) for letter in text}
    pattern_dict = {letter:pattern.count(letter) for letter in pattern}
    # print(text_dict)
    # print(pattern_dict)
    try:
        for letter in pattern_dict:
            if pattern_dict[letter] > text_dict[letter]:
                return False
    except KeyError:
        return False
    return True


# my_text = 'abracadabra'
# my_pattern = 'aacd'
my_text = input()
my_pattern = input()
print(contains_upto_permutations(my_text, my_pattern))