
# input
n = int(input())

# process & output
k = 1
for i in range(1, n+1):
    for j in range(i):
        print(k, end='')
        k += 1
        if k > 9:
            k = 0
    print()
