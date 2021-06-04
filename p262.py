# the descirption needs modifying

# input
s_lt = input().split()

# process
others_tp = ('to', 'a', 'an', 'the', 'from', 'for', 'of', 'and', 'in')
s_lt[0] = s_lt[0].capitalize()
s_lt = list(map(
    lambda word: word.capitalize() if not word in others_tp else word,
    s_lt
))
s = ' '.join(s_lt)

# output
print(s)
