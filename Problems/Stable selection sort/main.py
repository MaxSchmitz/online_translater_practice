def selection_sort(elements):
    for i in range(len(elements) - 1):
        index = i

        for j in range(i + 1, len(elements)):
            if len(elements[j]) < len(elements[index]):
                index = j

        key = elements[index]
        while index > i:
            elements[index] = elements[index - 1]
            index -= 1
        elements[i] = key
        # elements[i], elements[index] = elements[index], elements[i]


n = int(input())
# names = ['Kate', 'Mike', 'Nick', 'Sam', 'Bob', 'Karl']
names = []
for name in range(n):
    names.append(input())

selection_sort(names)
for name in names:
    print(name)