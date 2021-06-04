
# input
n = int(input())

# process & output
for i in range(2*n-1):
    if i+1 <= n:
        print(' '*(n-i-1), end='')
        print('*'*(2*i+1), end='')
    else:
        print(' '*(i-n+1), end='')
        print('*'*(2*(2*n-1-i)-1), end='')
    print()
