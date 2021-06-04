# the description needs modifying

# input
n = int(input())
works = []
for i in range(n):
    work = input().split()
    works.append((work[0], int(work[1])))

# process & output
works.sort(key=lambda work: work[1])
len_w = len(works)
i, cnt = works[0][1], 0
while cnt != len_w:
    cnt, ws = 0, []
    for w, t in works:
        if not i % t:
            ws.append(w)
            cnt += 1
    if ws:
        print(i, ' '.join(ws))
    i += 1
