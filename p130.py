
# input
# lst = list(map(int, input().split()))
lst = list(map(int, "0 0 0 0".split()))
# lst = list(map(int, "-5 -3 1 2 4 8".split()))

# process & output
def bi_search(n, l, r):
    while l != r:
        m = (l+r) // 2
        if lst[m] == n: return m
        elif lst[m] > n: r = m
        else: l = m + 1
    return None

len_l = len(lst)
for i in range(len_l):
    for j in range(i+1, len_l):
        k = bi_search(0-lst[i]-lst[j], j+1, len_l)
        if k:
            cnt_k = lst[j+1:].count(lst[k])
            for n in range(cnt_k):
                print(f"{lst[i]} {lst[j]} {lst[k]}")
           
