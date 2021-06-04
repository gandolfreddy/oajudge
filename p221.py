
# input
scores = list(map(int, input().split()))

# process
len_score = len(scores)
res_lt = []
for i in range(len_score-1):
    for j in range(i+1, len_score):
        if scores[i] < scores[j]:
            res_lt.append(j-i)
            break
        if j == len_score-1:
            res_lt.append(0)
res_lt.append(0)
result = ' '.join(map(str, res_lt))

# output
print(result)
