# the last one in Hint is wrong

pieces_lt = []
while True:
    n = int(input())
    if n < 0:
        break
    piece = n*(n+1)//2 + 1
    pieces_lt.append(piece)

# output
for piece in pieces_lt:
    print(piece)
