
# input
n = int(input())

# process


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


result = factorial(n)

# output
print(result)
