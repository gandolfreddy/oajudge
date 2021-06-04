from datetime import datetime


# input
d1 = tuple(map(int, input().split()))
d2 = tuple(map(int, input().split()))

# process
d1 = datetime(d1[0], d1[1], d1[2])
d2 = datetime(d2[0], d2[1], d2[2])
diff_day = d2 - d1
result = abs(diff_day.days)

# output
print(result)
