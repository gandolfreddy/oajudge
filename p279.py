
# input
nums = list(map(int, input().split()))

# process
nums.sort()
nums_s = ' '.join(map(str, nums))

# output
print(nums_s)
