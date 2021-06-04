
# input
n = int(input())
works = []
for i in range(n):
    work = input().split()
    works.append((work[0], int(work[1]), int(work[2])))

# process


def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


works.sort(key=lambda work: work[1])
len_w = len(works)
denominator = 1
for i in range(n-1):
    denominator *= gcd(works[i][1], works[i+1][1])
fraction = 1
for i in range(n):
    fraction *= works[i][1]
lcm = int(fraction/denominator)
pos, t = 0, 1
scheduling = [works[pos][0]]
log = f"{scheduling[-1]}"
while t != lcm:
    for work in works:
        if not t % work[1]:
            scheduling += [work[0]]*work[2]
            break
    if scheduling and log[-1] == scheduling[-1]:
        scheduling.pop()
        if scheduling and log[-1] != scheduling[-1]:
            scheduling.pop()
    if not scheduling:
        pos += 1
        if pos < len_w:
            scheduling += [works[pos][0]]*works[pos][2]
    log += scheduling[-1] if scheduling else 'X'
    t += 1

# output
print(log)
