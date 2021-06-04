
# input
in_lt = []
while True:
    try:
        in_lt.append(input())
    except:
        break

# process
out_s = '-'.join(in_lt)

# output
print(out_s)
