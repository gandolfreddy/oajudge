
# input
chs = input().split()
para = input()

# process
result = ' '.join(
    [str(para.count(chs[i].lower())+para.count(chs[i].upper()))
     for i in range(3)]
)

# output
print(result)
