
# input
nums = list(map(int, input().split(',')))

# process
result = False
len_nums = len(nums)
for i in range(1, len_nums):
    if sum(nums[:i]) == sum(nums[i:]):
        result = True
        break

# output
print(result)
