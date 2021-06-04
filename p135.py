
# input
lt = input().split()

# process
dt = {chr(ord('a')+i): i+1 for i in range(26)}


def weight_sum(s):
    w_sum = 0
    s = s.lower()
    for ch in s:
        if ch >= 'a' and ch <= 'z':
            w_sum += dt[ch]
        else:
            return 0
    return w_sum


result = sorted(lt, key=weight_sum)

# output
print(result)
