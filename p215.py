
# input & process
def padding_zero(num, t):
    num_s = str(num)
    len_n = len(num_s)
    amount = 3-len_n if t == "name" or t == "cat" else 4-len_n
    for i in range(amount):
        num_s = '0' + num_s
    return num_s


lib = {}
name_lib, cat_lib, in_lib = 1, 1, 1
while True:
    content = input()
    if content == '0':
        break
    if not content in lib:
        if not lib:
            name_lib = "001"
        else:
            name_lib = int(lib[list(lib.keys())[-1]][0][:3]) + 1
    else:
        name_lib = lib[content][0][:3]
    cat_lib = "001" if not content in lib else int(lib[content][-1][3:6])+1
    if not content in lib:
        lib[content] = []
    lib[content].append(
        padding_zero(name_lib, "name") +
        padding_zero(cat_lib, "cat") +
        padding_zero(in_lib, "in")
    )
    in_lib += 1

# output
for key, value in lib.items():
    print(key, end=' ')
    print(' '.join(value))
