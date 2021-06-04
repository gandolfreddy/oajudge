
# input
n = int(input())

# process


def f(x):
    nums = [0 for i in range(x)]
    for i in range(4):
        nums[i] = i + 1
    for i in range(4, x):
        nums[i] = nums[i-1]*1 + nums[i-2]*2 + \
            nums[i-3]*3 + nums[i-4]*4
    return nums[x-1]


result = f(n)

# output
print(result)
