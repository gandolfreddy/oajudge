# input
edges_lt = input().split()

# process
edges_lt = sorted(map(int, edges_lt))
edges = ' '.join(map(str, edges_lt))

a, b, c = edges_lt
result = ''
if a+b <= c:
    result = "No"
elif a*a+b*b < c*c:
    result = "Obtuse"
elif a*a+b*b == c*c:
    result = "Right"
elif a*a+b*b > c*c:
    result = "Acute"

# output
print(edges)
print(result)
