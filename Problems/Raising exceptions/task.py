class NegativeSumError(Exception):
    def __str__(self):
        return "There is a negative result!"

    def __init__(self, num):
        self.message = "The integer %s is below 0!" % str(num)
        super().__init__(self.message)

def sum_with_exceptions(a, b):

    c = a + b
    if c < 0:
        raise NegativeSumError(c)
    else:
        return c

