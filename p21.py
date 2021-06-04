
# input & process
t = int(input())
for i in range(t):
    wall_n = int(input())
    walls = list(map(int, input().split()))
    pre_w = walls[0]
    h_jp, l_jp = 0, 0
    for wall in walls[1:]:
        if pre_w > wall:
            h_jp += 1
        elif pre_w < wall:
            l_jp += 1
        pre_w = wall

    # output
    print(f"Case {i+1}: {l_jp} {h_jp}")
