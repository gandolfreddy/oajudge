
# input
nums = list(map(int, input().split()))

# process
lt = []
inner_lt = []
len_n = len(nums)
for i in range(1, len_n):
    inner_lt.append(nums[i-1])
    if nums[i]-1 != nums[i-1]:
        lt.append(inner_lt)
        inner_lt = []

lt.append(inner_lt)
lt[-1].append(nums[-1])

len_lt = len(lt)
for i in range(len_lt):
    lt[i] = list(map(str, lt[i]))

# output
for i in range(len_lt):
    print(' '.join(lt[i]))
