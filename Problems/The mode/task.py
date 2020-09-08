user_input = input()
#output should be 5
from collections import Counter

text_list = user_input.split()
freq_counter = Counter(text_list)

print(freq_counter.most_common()[0][0])