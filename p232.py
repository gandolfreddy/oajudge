
# input & process
n = int(input())
legs = []
for i in range(n):
    leg = input().split()
    leg = [leg[0]] + list(map(int, leg[1:]))
    leg.insert(3, leg[3]/(((leg[1]**2+leg[2]**2)**0.5)**2))
    legs.append(leg)

# process
result = sorted(
    legs,
    key=lambda leg: leg[-2:],
    reverse=True
)

# output
for res in result:
    print(res[0])
