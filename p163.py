# the description shall be modified as "return x, if 1 <= x <= 4"

# input
n = int(input())

# process


def f(x):
    if x >= 1 and x <= 4:
        return x
    return f(x-1)+f(x-2)*2+f(x-3)*3+f(x-4)*4


result = f(n)

# output
print(result)
