
# input
nums = list(map(int, input().split()))
levels = input().split()

# process
len_n = len(nums)
lt = [[levels[i], nums[i]] for i in range(len_n)]
level_lt = []
res_lt = []

lt.sort(key=lambda elem: elem[0])
for i in range(len_n):
    if not lt[i][0] in level_lt:
        level_lt.append(lt[i][0])
        res_lt.append(str(lt[i][1]))
        lt[i][0] = ''
lt.sort(key=lambda elem: elem[0], reverse=True)
for i in range(len_n):
    if lt[i][0]:
        level_lt.append(lt[i][0])
        res_lt.append(str(lt[i][1]))
        lt[i][0] = ''
res = ' '.join(res_lt)

# output
print(res)
