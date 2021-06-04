
# input
n = int(input())

# process


def fibo(n):
    lt = [0, 1]
    if n <= 1:
        return lt[:n+1]
    for i in range(2, n+1):
        fn_1 = lt[i-1]
        fn_2 = lt[i-2]
        lt.append(fn_1+fn_2)
    return lt


result = fibo(n)

# output
print(result)
