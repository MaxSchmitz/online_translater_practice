class WordError(Exception):
    def __str__(self):
        return "There is a bad word!"

    def __init__(self, word):
        self.message = "The word %s has a 'w' in it!" % str(word)
        super().__init__(self.message)


def check_w_letter(word):

    if 'w' in word:
        raise WordError(word)
    else:
        return word



