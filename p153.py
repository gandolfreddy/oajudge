
# input
nums = list(map(int, input().split()))

# process
diff = 0
max_odd = -10000000
max_even = -10000000
for num in nums:
    if num % 2:
        if num > max_odd:
            max_odd = num
    else:
        if num > max_even:
            max_even = num
diff = abs(max_odd-max_even)

# output
print(diff)
