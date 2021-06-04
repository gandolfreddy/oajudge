from datetime import date, timedelta


# input
d1 = tuple(map(int, input().split()))
diff_days = int(input())

# process
d1 = date(d1[0], d1[1], d1[2])
diff_days = timedelta(days=diff_days)
d2 = d1 + diff_days
result = d2.isoformat()

# output
print(result)
