# do not mention how to deal with avg (like floor(), round(), or just use // operator)

# input & process
account = list(map(int, input().split()))
ops = input().split()
op, content1, content2 = '', 0, 0
if len(ops) == 2:
    op, content1 = ops
else:
    op, content1, content2 = ops
content1 = int(content1)
content2 = int(content2)
while op != 'q':
    if op == 'a':
        account.append(content1)
    elif op == 'r':
        account.remove(content1)
    elif op == 'p':
        if content1 < len(account):
            account.pop(content1)
    elif op == 'e':
        if content1 in account:
            account[account.index(content1)] = content2
    elif op == 'm':
        if content1 < len(account):
            account[content1] = content2
    ops = input().split()
    if len(ops) == 2:
        op, content1 = ops
    else:
        op, content1, content2 = ops
    content1 = int(content1)
    content2 = int(content2)
if content1 < len(account):
    avg = sum(account)/len(account)
else:
    avg = "Error"

# output
len_a = len(account)
for i, n in enumerate(account):
    if i < len_a-1:
        print(n, end=' ')
    else:
        print(n)
if content1 < len(account):
    print(float(account[content1]), end=' ')
print(avg)
