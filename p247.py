from json import loads

# input & process & output
dir_dt = loads(input())
cur_dt = dir_dt["home"]
pre_lt = []
abs_path = ["home"]
while True:
    ops = input().split()
    if ops[0] == 'quit':
        break
    elif ops[0] == 'ls':
        for k in cur_dt.keys():
            print(k)
    elif ops[0] == 'pwd':
        print('/'.join(abs_path))
    elif ops[0] == 'cd':
        if ops[1] in cur_dt:
            pre_lt.append(cur_dt)
            cur_dt = cur_dt[ops[1]]
            abs_path.append(ops[1])
        elif ops[1] == "..":
            abs_path.pop()
            cur_dt = pre_lt.pop()
        else:
            print("error")
