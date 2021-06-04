
# input
lt = list(map(int, input().split()))
n = int(input())

# process
cnt = 0
len_lt = len(lt)
for i in range(len_lt-2):
    for j in range(i+1, len_lt-1):
        for k in range(j+1, len_lt):
            if lt[i]+lt[j]+lt[k] < n:
                cnt += 1
# output
print(cnt)
