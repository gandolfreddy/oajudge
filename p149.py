
# input
nums = list(map(int, input().split()))

# process
diff = 0
for num in nums:
    diff = diff+1 if num % 2 else diff-1
diff = abs(diff)

# output
print(diff)
