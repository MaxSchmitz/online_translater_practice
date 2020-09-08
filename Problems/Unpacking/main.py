items_list = []
def unpack(input_tuple):
    # your code here

    for item in input_tuple:
        if type(item) is tuple:
            unpack(item)
        else:
            items_list.append(item)
    return tuple(items_list)

hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')

print(unpack(hobbies_Adam))