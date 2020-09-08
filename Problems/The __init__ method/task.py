# class NotWordError(Exception):
#     def __init__(self, word):
#         self.message = word + " is not a word, sorry!"
#         super().__init__(self.message)

def check_word(word):
    if '0' in word:
        raise NotWordError(word)
    else:
        return word

def error_handling(word):
    try:
        return print(check_word(word))
    except NotWordError as err:
        print(err)

# error_handling('w0rd')
# error_handling('word')