# need to modify the input which includes "exit" command but not in description
import json


# input & process & output
dir_dt = json.loads(input())
ops = input().split()
cur_dir = "home"
pre_dir_lt = []

while ops[0] != "exit":
    if ops[0] == "ls":
        print(','.join(dir_dt[cur_dir]))
    elif ops[0] == "pwd":
        print(f"{'/'.join(pre_dir_lt)}/{cur_dir}")
    elif ops[0] == "rmdir":
        if ops[1] in dir_dt[cur_dir]:
            dir_dt[cur_dir].remove(ops[1])
        else:
            print(f"rmdir {ops[1]} error")
    elif ops[0] == "mkdir":
        dir_dt[ops[1]] = []
        dir_dt[cur_dir].append(ops[1])
    elif ops[0] == "cd":
        if ops[1] in dir_dt[cur_dir]:
            pre_dir_lt.append(cur_dir)
            cur_dir = ops[1]
        else:
            if ops[1] == "..":
                cur_dir = pre_dir_lt[-1] if pre_dir_lt else cur_dir
            else:
                print(f"cd {ops[1]} error")
    ops = input().split()
