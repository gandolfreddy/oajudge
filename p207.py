
# input & process & output
name_dt = {}
phone_dt = {}
while True:
    cmd = input().split()
    if cmd[0] == 'a':
        name_dt[cmd[1]] = cmd[2]
        phone_dt[cmd[2]] = cmd[1]
    elif cmd[0] == 's':
        if cmd[1] in name_dt:
            print(name_dt[cmd[1]])
        elif cmd[1] in phone_dt:
            print(phone_dt[cmd[1]])
        else:
            print(f"Cannot find {cmd[1]}")
    else:
        break
