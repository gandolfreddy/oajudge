# input
nums = list(map(int, list(input())))

# process
nums.sort()
len_n = len(nums)
if nums[0] == 0:
    for i in range(1, len_n):
        if nums[i] != 0:
            nums[0], nums[i] = nums[i], nums[0]
            break
nums = ''.join((map(str, nums)))

# output
print(nums)
