
# input
index_lt = list(map(int, input().split()))
names_lt = input().split()
dt = dict(zip(index_lt, names_lt))
ta = int(input())

# process
result = dt.get(ta, "not found")

# output
print(result)