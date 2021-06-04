
# input
nums = tuple(map(int, input().split()))

# process
longest_con = 0
con = 0
len_n = len(nums)
for i in range(1, len_n):
    if nums[i]-1 == nums[i-1]:
        con += 1
    else:
        con = 0
longest_con = con+1 if con else con

# output
print(longest_con)
