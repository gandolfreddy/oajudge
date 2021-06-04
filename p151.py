
# input
n = int(input())

# process & output
k = 65
for i in range(1, n+1):
    for j in range(i):
        print(chr(k), end='')
        k += 1
        if k-65 > 25:
            k = 65
    print()
