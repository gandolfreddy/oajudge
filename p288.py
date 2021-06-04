
# input
n = int(input())

# process & output
for i in range(1, n+1):
    res = ''
    if not i % 3 and not i % 5:
        res = "拍手拍頭"
    elif not i % 3:
        res = "拍手"
    elif not i % 5:
        res = "拍頭"
    else:
        res = i
    print(res)
