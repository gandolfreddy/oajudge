
# input & process
ps = input().split()
len_ps = len(ps)
ps_dt = {name: dict(zip(ps, [0]*len_ps)) for name in ps}

while True:
    try:
        costs = input().split()
        len_costs = len(costs)
        if len_costs == 2:
            spent = int(costs[1])
            for p in ps:
                ps_dt[costs[0]][p] += spent // len_ps
        elif costs[-1].isdigit():
            spent, m = int(costs[1]), 0
            for i, cost in enumerate(costs[2:]):
                if cost.isdigit():
                    m_cost = int(cost)
                    ps_dt[costs[0]][costs[i+2-1]] += m_cost
                    m += m_cost
            spent -= m
            ps_dt[costs[0]][costs[0]] += spent
        elif costs[-1][-1] == '%':
            spent, m = int(costs[1]), 0
            for i, cost in enumerate(costs[2:]):
                if cost[-1] == '%':
                    discount = int(cost[:-1])
                    ps_dt[costs[0]][costs[i+2-1]] += spent * discount // 100
                    m += spent * discount // 100
            spent -= m
            ps_dt[costs[0]][costs[0]] += spent
        else:
            len_people = len(costs[2:]) + 1
            spent = int(costs[1]) // len_people
            ps_dt[costs[0]][costs[0]] += spent
            for p in costs[2:]:
                ps_dt[costs[0]][p] += spent
    except:
        break

total_costs = {p: 0 for p in ps}
for v in ps_dt.values():
    for p in ps:
        total_costs[p] += v[p]

owe_dt = {name: dict(zip(ps, [0]*len_ps)) for name in ps}
for k, v in ps_dt.items():
    for p in ps:
        if p != k:
            owe_dt[k][p] += v[p] - ps_dt[p][k]

# output
for p in ps:
    print(p, end=' ')
    print(total_costs[p], end=' ')
    n = 0
    for k, v in owe_dt[p].items():
        if v < 0:
            print(k, end=' ')
            print(f"{-1*v}", end=' ')
        n += v
    n_s = f"+{n}" if n > 0 else n
    print(n_s)
