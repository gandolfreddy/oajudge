
# input & process & output
finest = 0
finest_n, n = 1, 1
while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    sum_performance = sum(nums)
    if finest < sum_performance:
        finest = sum_performance
        finest_n = n
    n += 1

# output
print(f"{finest_n} {finest}")
