
# input
dishs = input()
hates = input()

# process
cnt = 0
for hate in hates:
    cnt += dishs.count(hate)

# output
print(cnt)
