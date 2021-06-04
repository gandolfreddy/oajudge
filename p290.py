
# input
n = int(input())
scores = list(map(int, input().split()))

# process
scores.sort()
scores_s = ' '.join(map(str, scores))

best_fail, worst_pass = None, None
len_scores = len(scores)
if scores[-1] < 60:
    best_fail = scores[-1]
    worst_pass = "worst case"
elif scores[0] >= 60:
    best_fail = "best case"
    worst_pass = scores[0]
else:
    for i in range(len_scores):
        if scores[i] >= 60 and scores[i-1] < 60:
            best_fail = scores[i-1]
            worst_pass = scores[i]

# output
print(scores_s)
print(best_fail)
print(worst_pass)
