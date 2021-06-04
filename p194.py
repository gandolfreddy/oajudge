
# input
n = int(input())
nums = list(map(int, input().split(',')))

# process
hash_lt = []
len_nums = len(nums)
for i in range(len_nums):
    hash_val = nums[i] % n
    while hash_val in hash_lt:
        hash_val = (hash_val+1) % n
    hash_lt.append(hash_val)
result = ','.join(map(str, hash_lt))

# output
print(result)
