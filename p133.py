
# input
s = input()

# process
check_lt = list()
for ch in s:
    if ch == '(':
        check_lt.append(ch)
    elif check_lt:
        check_lt.pop()
    else:
        check_lt.append(ch)
        break
result = (check_lt == [])

# output
print(result)
