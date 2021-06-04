
# input
ids_lt = input().split()

# process
res_lt = []
for id_s in ids_lt:
    point = 0
    if id_s[:3] == "b06":
        point += 3
    if id_s[:3] == "b07":
        point += 1
    last_3nums = int(id_s[-3:])
    if not (last_3nums % 3 and last_3nums % 5 and last_3nums % 7):
        point += 2
    if not last_3nums % 2:
        point += 1
    last_5nums = id_s[-5:]
    product = 1
    for nums in last_5nums:
        if nums != '0':
            product *= int(nums)
    point += (len(str(product))-1) * 1
    if id_s[0] == 'b' and id_s[3] == '9':
        point = 0
    res_lt.append((point, id_s))
res_lt.sort(key=lambda res: res[0], reverse=True)

# output
print(f"{res_lt[0][0]},{res_lt[0][1]}")
