# NO

# input & process
name_lt = input().split()
owed_lt = list(map(int, input().split()))
dt = dict(zip(name_lt, owed_lt))
while True:
    try:
        name = input()
        # output
        print(dt[name])
    except:
        break