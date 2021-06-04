# there's no description for how to check EOF

# input
words = []
s = input()
while s:
    words.append(s)
    # it's a unusual way to check if it's end of file in this section
    if s == "elephant" or s == "java":
        break
    s = input()

# process
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
cmp_lt = [list(word) for word in words]
len_lt = len(cmp_lt)
for i in range(len_lt):
    cmp_lt[i] = list(map(lambda ch: '' if not ch in vowels else ch, cmp_lt[i]))
    words[i] = (words[i], len(tuple(filter(None, cmp_lt[i]))))
res_lt = [item[0] for item in sorted(words, key=lambda word: word[1])]

# output
for res in res_lt:
    print(res)
