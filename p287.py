
# input
n = int(input())

# process
ori_n = n
while not n % 4:
    n //= 4
result = n == 1 and ori_n != 1

# output
print(result)
