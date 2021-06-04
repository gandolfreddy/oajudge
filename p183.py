# input
lt_n = input().split(',')

# process
result = ''.join(map(lambda n: chr(int(n)+96), lt_n))

# output
print(result)
