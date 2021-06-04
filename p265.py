# it doesn't mention if there is EOF or not

# input
dt, p_cnt = {}, 0
while True:
    try:
        ps = input().split()
        p_cnt += 1
        if not ps[0] in dt:
            dt[ps[0]] = [ps[1], ps[2]]
    except:
        break
p_cnt -= 1

# process
start = list(dt.keys())[0]
pre_p = start
cur_p = dt[pre_p][0]
while cur_p != start and p_cnt != 0:
    if dt[cur_p][0] == pre_p:
        dt[cur_p][0], dt[cur_p][1] = dt[cur_p][1], dt[cur_p][0]
    pre_p = cur_p
    cur_p = dt[pre_p][0]
    p_cnt -= 1

result = p_cnt == 0 and cur_p == start

# output
print(result)
