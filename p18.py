
# input
n = int(input())
amounts = [tuple(map(int, input().split())) for i in range(n)]

# process
BIG_INT = 10000000000
dp = {}


def change_coin(amount, coin_ks):
    if amount < coin_ks[0]:
        return 0 if not amount else BIG_INT
    else:
        coin = BIG_INT-1
        for coin_k in coin_ks:
            if amount < coin_k:
                break
            cal_res = f"{amount}{coin_k}"
            if not cal_res in dp:
                dp[cal_res] = change_coin(amount-coin_k, coin_ks)
            coin = min(coin, dp[cal_res])
        return coin+1


coins = []
for item in amounts:
    amount = item[0]
    coin_ks = item[1:]
    coin_n = change_coin(amount, coin_ks)
    if coin_n == BIG_INT:
        coin_n = -1
    coins.append(coin_n)

# output
for coin_n in coins:
    print(coin_n)
