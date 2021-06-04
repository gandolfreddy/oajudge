
# input
n = int(input())

# process
cnt = 0
while n != 0:
    n = n-1 if n % 2 else n//2
    cnt += 1

# output
print(cnt)
