
# input
words = input().split()
prefix = input()

# process
len_w, len_p = len(words), len(prefix)
matched = []
for i in range(len_w):
    if words[i][:len_p] == prefix:
        matched.append(words[i])
result = ' '.join(matched)

# output
print(result)
