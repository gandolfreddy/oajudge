
# input
nums = list(map(int, input().split()))

# process
product = 1
n_nums = list(filter(lambda n: n < 0, nums))
p_nums = list(filter(lambda n: n >= 0, nums))
if len(n_nums) >= 2:
    choice1 = n_nums[-1]*n_nums[-2]*p_nums[-1]*p_nums[-2]
else:
    choice1 = 1
choice2 = p_nums[-1]*p_nums[-2]*p_nums[-3]*p_nums[-4]
product = choice1 if choice1 > choice2 else choice2

# output
print(product)
