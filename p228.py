
# input
start, end, step = tuple(map(int, input().split()))

# process
seq = range(start, end+1, step)
res_seq = ' '.join(map(str, tuple(range(start, end+1, step))))
sum_seq = sum(seq)

# output
print(res_seq)
print(sum_seq)
