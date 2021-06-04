from math import floor

# input
discounts = []
for i in range(5):
    discounts.append(input().split())
price = int(input())

# process
for discount in discounts:
    if discount[0] == '$':
        price -= int(discount[1])
    else:
        price *= int(discount[0]) / 10
price = floor(price)

# output
print(price)
