
# input
n = int(input())

# process & output
for i in range(1, n+1):
    sqr_num = i * i
    if sqr_num < n:
        print(sqr_num)
