# do not mention how to deal with avg (like floor(), round(), or just use // operator)

# input & process
account = list(map(int, input().split()))
op, content = input().split()
content = int(content)
while op != 'q':
    if op == 'a':
        account.append(content)
    elif op == 'r':
        account.remove(content)
    elif op == 'p':
        if content < len(account):
            account.pop(content)
    op, content = input().split()
    content = int(content)
if content < len(account):
    avg = sum(account)//len(account)
else:
    avg = "Error"

# output
if content < len(account):
    print(account[content])
print(avg)
