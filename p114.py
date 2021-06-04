
# input
n = int(input())

# process & output
for i in range(1, n+1):
    if not n % i:
        print(i)
