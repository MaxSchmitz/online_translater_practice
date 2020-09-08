# put your python code here
def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i][1] < lst[start][1]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
        elif lst[i][1] == lst[start][1]:
            if lst[i][0] < lst[start][0]:
                j += 1
                lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


def quick_sort_age(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort_age(lst, start, j - 1)
    quick_sort_age(lst, j + 1, end)


n = int(input())
# n = 3
students = []

for student in range(n):
    students.append(input().split(" "))

students = [(n[0], int(n[1])) for n in students]
# print(students)


quick_sort_age(students, 0, len(students) - 1)
for student in students:
    print(student[0])
