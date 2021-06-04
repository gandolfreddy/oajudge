
# input
n = int(input())
pros = []
for i in range(n):
    pros.append(list(map(int, input().split()))+[0])

# process
len_p = len(pros)
for i in range(len_p):
    ratio = pros[i][1] // pros[i][0]
    diff = pros[i][1] - pros[i][0]
    if pros[i][0]+diff == pros[i][2]-diff:
        pros[i][4] = pros[i][3] + diff
    else:
        pros[i][4] = pros[i][3] * ratio

# output
for pro in pros:
    print(' '.join(map(str, pro)))
