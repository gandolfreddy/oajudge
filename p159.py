
# input
nums = tuple(map(int, input().split()))

# process
cnt = 0
for n in range(nums[1]+1):
    r = int(n**0.5)
    if r**2 == n:
        cnt += 1

# output
print(cnt)
