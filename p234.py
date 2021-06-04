
# input
n = int(input())

# process


def f(x):
    if x == 1:
        return x
    elif x % 2:
        k = (x-1) // 2
        return f(k)+f(k+1)
    else:
        k = x
        while not k % 2:
            k //= 2
        return f(k)


result = f(n)

# output
print(result)
