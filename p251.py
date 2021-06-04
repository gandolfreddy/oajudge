from math import ceil

# input
threshold = int(input())
lt, all_lt = [], []
while True:
    item = input().split()
    if item[0] == "end":
        break
    name,  item_lt = item[0], item[1:]
    lt.append([name,  item_lt])
    all_lt += [item for item in item_lt if not item in all_lt]

# process 1: get recommand value & items


def probability_calc(elem1, elem2):
    st1, st2 = set(elem1), set(elem2)
    st = st1 & st2
    return (ceil(len(st)/len(st1)*100), st2-st)


len_lt = len(lt)
match_lt = [set() for i in range(len_lt)]
for i in range(len_lt):
    tmp_lt = lt[:i] + lt[i+1:]
    len_tmp = len(tmp_lt)
    for j in range(len_tmp):
        matchs = probability_calc(lt[i][1], tmp_lt[j][1])
        matchs = matchs[1] if matchs[0] >= threshold else set()
        match_lt[i] |= matchs

# process 2: for placing the result in order
res_lt = [[] for i in range(len_lt)]
for i, item in enumerate(lt):
    res_lt[i].append(item[0])
    for elem in all_lt:
        if elem in match_lt[i]:
            res_lt[i].append(elem)
    res_lt[i] = ' '.join(res_lt[i])

# output
for res in res_lt:
    print(res)
