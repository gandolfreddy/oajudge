
# input
total = int(input())
ls = list(map(int, input().split()))
ps = list(map(int, input().split()))

# process
dt = dict(zip(ls, ps))
dp = {}


def get_price(l):
    if l == 1:
        return dt[l]
    best = dt[l]
    for i in range(1, l):
        k = f"{l}{i}"
        if not k in dp:
            dp[k] = get_price(l-i)+get_price(i)
        best = max(best, dp[k])
    return best


res = get_price(total)

# output
print(res)
