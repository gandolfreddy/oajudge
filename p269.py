
# input
mat = []
while True:
    try:
        m = input().split()
        mat.append(m)
    except:
        break

# process
ta = "小明"
pos = None
for i, m in enumerate(mat):
    if ta in m:
        pos = (i, m.index(ta))

# output
print(pos)
