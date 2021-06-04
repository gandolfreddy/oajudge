
# input
n = int(input())
things = {}
for i in range(n):
    item = input().split()
    name, cost = item[0], item[1:]
    things[name] = cost
m = int(input())
wish_lt = []
for i in range(m):
    wish_lt.append(input())

# process


def get_cost(item):
    len_t_item = len(things[item])
    if len_t_item < 2:
        things[item] = [int(things[item][0])]
        return things[item][0]
    cost = int(things[item][0])
    for i in range(1, len_t_item):
        things[things[item][i]] = [get_cost(things[item][i])]
        cost += things[things[item][i]][0]
    things[item] = [cost]
    return cost


for k in things.keys():
    len_tk = len(things[k])
    things[k][0] = int(things[k][0])
    if len_tk < 2:
        continue
    else:
        for i in range(1, len_tk):
            things[k][i] = get_cost(things[k][i])
        things[k] = [sum(things[k])]

# output
for wish in wish_lt:
    print(things[wish][0])
