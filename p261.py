
# input
item = input().split()
price = list(map(int, input().split()))
changes = int(input())

# process
menu = dict(zip(price, item))
buy_s = ''
for p in price:
    if changes-p in menu:
        buy_s = f"{menu[p]} {menu[changes-p]}"
        break

# output
print(buy_s)
