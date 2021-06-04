from json import loads

# input
dt1 = loads(input())
dt2 = loads(input())

# process & output
dt1 = dict(sorted(list(dt1.items()), key=lambda item: len(item[1])))
dt2 = dict(sorted(list(dt2.items()), key=lambda item: len(item[1])))
for k in dt1.keys():
    len_k = len(dt1[k])
    is_name_there = False
    for i in range(len_k):
        if dt1[k][i] != dt2[k][i]:
            if not is_name_there:
                print(k)
                is_name_there = True
            print(i, dt1[k][i], dt2[k][i])
