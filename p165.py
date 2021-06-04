
# input & process
n = int(input())
strength_pw = []
for i in range(n):
    s = input()
    lt = list(s)
    len_lt = len(lt)
    n_digit, n_lower, n_upper, n_other = 0, 0, 0, 0
    for j in range(len_lt):
        if lt[j].isnumeric():
            n_digit += 1
        elif lt[j].islower():
            n_lower += 1
        elif lt[j].isupper():
            n_upper += 1
        else:
            n_other += 1
    strength_pw.append(
        (len_lt*(n_upper*2+n_lower*1.5+n_digit)+n_other**2, s)
    )

result = sorted(strength_pw, key=lambda pw: pw[0], reverse=True)

# output
for item in result:
    print(item[1])
