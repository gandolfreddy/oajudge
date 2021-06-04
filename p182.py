# input
lt_s = list(input())

# process
result = ','.join(map(lambda ch: str(ord(ch)-96), lt_s))

# output
print(result)
