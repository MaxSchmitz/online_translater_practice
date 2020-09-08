def contains2d(text, pattern):


def get_matrix():
    n, m = [int(i) for i in input().split()]
    matrix = []
    for row in range(n):
        matrix.append(input())
    return matrix

my_text = get_matrix()
my_pattern = get_matrix()
print(contains2d(my_text, my_pattern))