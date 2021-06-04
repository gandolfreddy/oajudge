
# input
ch = input()
paragraph = input().split()

# process
len_p = len(paragraph)
ch_upper = ch.upper()
for i in range(len_p):
    if paragraph[i][0] == ch:
        paragraph[i] = paragraph[i].replace(paragraph[i][0], ch_upper)
paragraph = ' '.join(paragraph)

# output
print(paragraph)
