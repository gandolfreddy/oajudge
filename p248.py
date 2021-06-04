
# input
s = input()
t = input()

# process


def isSubStr(s, t):
    t_lt = list(t)
    t = ''.join(filter(lambda ch: ch in s, t_lt))
    return s in t


result = isSubStr(s, t)

# output
print(result)
