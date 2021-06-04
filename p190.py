
# input
nums = input().split()

# process
cmp_lt = []
len_nums = len(nums)
for i in range(len_nums):
    cmp_lt.append((
        nums[i], int(''.join(sorted(list(nums[i]), reverse=True)))
    ))
cmp_lt = sorted(cmp_lt, key=lambda elem: elem[1])
res_lt = [elem[0] for elem in cmp_lt]

# output
print(res_lt)
