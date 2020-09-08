def discounts(x, y):
    message = "I won't buy it!"
    assert y <= .5 * x, message
    return 'I will buy it!'

# discounts(10, 5)
# discounts(10, 10)