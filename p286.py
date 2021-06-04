
# input
t_lt = list(map(int, input().split()))
names_lt = input().split()

# process
len_t = len(t_lt)
lt = [(t_lt[0], names_lt[0])]
lt += [(t_lt[i]-t_lt[i-1], names_lt[i]) for i in range(1, len_t)]
lt.sort(key=lambda elem: elem[0])

# output
print(lt[0][1])
