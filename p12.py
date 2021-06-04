mandarin = (
    '', "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"
)
carry = (
    '', "拾", "佰", "仟"
)


# input
num = int(input())

# process
result = ''
c = 0

while num:
    r = num % 10
    if r:
        result = mandarin[r] + carry[c] + result
    c += 1
    num = num // 10

# output
print(result)
