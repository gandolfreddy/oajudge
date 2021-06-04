
# input & process
m_dt = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
        '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
res_lt = []
while True:
    content = input()
    if content == 'end':
        break
    y, m, d = map(int, content.split(', '))
    if str(m) in m_dt and (d >= 1 and d <= m_dt[str(m)]):
        res_lt.append("OK")
    else:
        res_lt.append("error")

# output
for res in res_lt:
    print(res)
