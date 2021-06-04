
# input
tree_lt = list(map(int, input().split(',')))

# process
finest_id = 0
max_amount = 0
len_tree_lt = len(tree_lt)
for i in range(len_tree_lt):
    if i == 0:
        amount = tree_lt[i] + tree_lt[i+1]
    elif i == len_tree_lt-1:
        amount = tree_lt[i] + tree_lt[i-1]
    else:
        amount = tree_lt[i-1] + tree_lt[i] + tree_lt[i+1]
    if max_amount < amount:
        max_amount = amount
        finest_id = i

# output
print(finest_id)
