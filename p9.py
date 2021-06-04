# input
start = int(input())
end = int(input())

# process
start = start if start % 2 else start+1
tp = tuple(range(start, end+1))

# output
print(sum(tp[:end+1:2]))
