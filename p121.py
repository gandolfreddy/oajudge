
# input
l = input().split()

# process


def longest_str(l):
    res_s = ""
    for s in l:
        if len(res_s) < len(s):
            res_s = s
    return res_s


result = longest_str(l)

# output
print(result)
