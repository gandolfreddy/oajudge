
# input
fee1, fee2 = list(map(int, input().split()))
init_x, init_y = list(map(int, input().split()))
move = input().split()
route_lt = []
while move[0] != '0':
    route_lt.append((move[0], int(move[1])))
    move = input().split()

# process
max_moves = [0, 0, 0, 0]  # [E, W, S, N]
total_move = 0
for route in route_lt:
    direct, dist = route
    if direct == 'E':
        init_x += dist
        max_moves[0] = max(max_moves[0], dist)
    elif direct == 'W':
        init_x -= dist
        max_moves[1] = max(max_moves[1], dist)
    elif direct == 'S':
        init_y -= dist
        max_moves[2] = max(max_moves[2], dist)
    elif direct == 'N':
        init_y += dist
        max_moves[3] = max(max_moves[3], dist)
    total_move += dist
final_x, final_y = init_x, init_y
total_fee = fee1*total_move + fee2*sum(max_moves)

# output
print(final_x, final_y)
print(total_fee)
