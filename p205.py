
# input
n1 = int(input())
n2 = int(input())

# process
result = 0
if n1 % 2 and n2 % 2:
    result = n1 - n2
elif not n1 % 2 and not n2 % 2:
    result = n1 + n2
else:
    result = n1 * n2

# output
print(result)
