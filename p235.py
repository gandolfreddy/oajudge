
# input
scores = [(i, int(n)) for i, n in enumerate(input().split())]

# process
scores.sort(key=lambda score: score[1])
result = ' '.join([str(score[0]) for score in scores])

# output
print(result)
