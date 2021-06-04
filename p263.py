
# input
goods = []
while True:
    good = input().split(',')
    if good[0] == "end":
        break
    goods.append(good)

customers = []
while True:
    try:
        customers.append(input().split())
    except:
        break

# process
res_lt = []
for customer in customers:
    item = ''
    for good in goods:
        if customer[0] == good[0][-3:] and customer[1] == good[1]:
            item = good[2]
            res_lt.append(item)
            goods.remove(good)
            break
    if not item:
        res_lt.append("Check again!")

# output
for res in res_lt:
    print(res)
