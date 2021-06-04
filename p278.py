
# input
n = int(input())

# process & output
for i in range(n):
    graph = ''
    if i == 0 or i == n-1:
        graph = '*' * n
    else:
        graph = '*' + ' '*(n-2) + '*'
    print(graph)
