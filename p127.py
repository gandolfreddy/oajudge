
# input
n = int(input())

# process


def fibo(n):
    if n <= 2:
        return n
    return fibo(n-1)+fibo(n-2)+fibo(n-3)


result = fibo(n)

# output
print(result)
