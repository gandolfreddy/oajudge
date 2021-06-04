
# input
s = list(input())

# process
result = ''
pre_ch = ''
len_s = len(s)
for i in range(len_s):
    if pre_ch and s[i] == '+':
        result += pre_ch
    elif pre_ch and s[i] == '-':
        result = result[:-1]
    elif pre_ch and s[i] == '*':
        result = result*2
    elif s[i] != '+' and s[i] != '-' and s[i] != '*':
        result += s[i]
        pre_ch = s[i]

# output
print(result)
