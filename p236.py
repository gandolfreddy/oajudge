
# input & process & output
c_e_dt, e_c_dt = {}, {}
while True:
    content = input().split()
    if content[0] == 'Q':
        break
    if content[0] == 'I':
        if content[1] in c_e_dt:
            result = "[fail]"
        else:
            c_e_dt[content[1]] = content[2]
            e_c_dt[content[2]] = content[1]
            result = "[succeed]"
    elif content[0] == 'C':
        result = c_e_dt[content[1]] if content[1] in c_e_dt else "[fail]"
    elif content[0] == 'E':
        result = e_c_dt[content[1]] if content[1] in e_c_dt else "[fail]"
    print(result)
