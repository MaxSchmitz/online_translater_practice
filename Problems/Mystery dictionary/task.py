# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here

# word = 'banana'
# random_dict = {'banana': 'fruit'}

# try:
#     print(random_dict[word])
# except KeyError:
#     print('Not in the dictionary')

print(random_dict.setdefault(word, 'Not in the dictionary'))