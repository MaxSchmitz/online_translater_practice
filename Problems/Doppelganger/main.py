from collections.abc import Hashable
# the object_list has already been defined
# write your code here

def get_doppelgangers(objects):
    object_list = []
    for thing in objects:
        if isinstance(thing, Hashable):
            object_list.append(thing)
        else:
            pass
    return object_list

# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
hashable_list = get_doppelgangers(object_list)
my_dict = {i:hashable_list.count(i) for i in hashable_list}
count = 0
for key in my_dict:
    if my_dict[key] > 1:
        count += my_dict[key]

print(count)
# print(my_dict)

