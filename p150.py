
# input
nums = list(map(int, input().split()))

# process
first = max(nums)
nums.remove(first)
second = max(nums)
diff = first - second

# output
print(diff)
