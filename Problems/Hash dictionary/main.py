from collections.abc import Hashable
# create your dictionary here
# objects = [3.14, '3.14', [3.14]]
objects_dict = {}
for thing in objects:
    if isinstance(thing, Hashable):
        objects_dict[thing] = hash(thing)
    else:
        pass

# print(objects_dict)



