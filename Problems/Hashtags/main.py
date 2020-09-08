import re

user_input = input().split()

# print(user_input)
for hashtag in user_input:
    if re.match('#[\w]+$', hashtag):
        print(hashtag[1:])
    elif re.match('#[\w]+[ .,!?#]$', hashtag):
        print(hashtag[1:len(hashtag)-1])
#