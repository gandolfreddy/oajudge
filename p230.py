# the sample input 1 is in a wrong form

# input
m, n = tuple(map(int, input().split()))
o, p = tuple(map(int, input().split()))
mat = []
for i in range(m):
    mat += list(map(int, input().split()))

# process
new_mat = []
for i in range(o):
    row = []
    bias = p * (i % o)
    for j in range(bias, p+bias):
        row.append(str(mat[j]))
    new_mat.append(row)
new_mat = [' '.join(row) for row in new_mat]

# output
for row in new_mat:
    print(row)
