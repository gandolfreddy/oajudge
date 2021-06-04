from math import floor, ceil

# input
lt = list(map(float, input().split()))

# process
result = 0
len_lt = len(lt)
if len_lt % 2:
    result = lt[len_lt//2]
else:
    result = (lt[len_lt//2]+lt[len_lt//2-1]) / 2

# output
print(result)
