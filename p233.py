
# input
n = int(input())
open_areas = {}
for i in range(n):
    cur_state = input().split()
    open_areas[cur_state[0]] = int(cur_state[1])
wish_lt = input().split()
open_limit = int(input())

# process
len_w = len(wish_lt)
wish_lt = [(wish_lt[i], open_areas[wish_lt[i]]) for i in range(len_w)]
wish_lt.sort(key=lambda state: state[1])
result = ' '.join([state[0] for state in wish_lt[:open_limit]])

# output
print(result)
