# the picture is unable to show up
from copy import deepcopy

# input
n = int(input())
countries = []
for i in range(n):
    start, end = tuple(map(int, input().split()))
    st = {i for i in range(start, end)}
    countries.append(st)

# process
len_c = len(countries)
max_inter_range = 0
for i in range(len_c):
    temp_lt = deepcopy(countries)
    temp_lt.remove(countries[i])
    inter = temp_lt[0]
    for country in temp_lt[1:]:
        inter &= country
    max_inter_range = max(max_inter_range, len(inter))

# output
print(max_inter_range)
