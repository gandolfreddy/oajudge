
# input
a = int(input())
b = int(input())
c = int(input())

# process
edges = [a, b, c]
edges.sort()
a, b, c = edges
result = (a**2+b**2 == c**2)

# output
print(result)
